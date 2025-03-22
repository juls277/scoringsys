from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse, Http404
from .models import Player, Category


# Create your views here.
# views.py

def get_players(request):
    # Get gender filter from request parameters
    gender = request.GET.get('gender', None)
    players = Player.objects.all()
    if gender:
        players = players.filter(gender=gender)  # Filter players by gender

    # Return the player data as JSON
    players_data = list(players.values('name', 'age_categories__name', 'country'))
    return JsonResponse(players_data, safe=False)


def home(request):
    return render(request, 'menue.html')


def login(request):
    return render(request, 'login.html')


def court1(request):
    return render(request, 'court.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if username.startswith('court') and username[5:].isdigit():
            court_number = int(username[5:])
            auth_login(request, user)
            return redirect('court', court_number=court_number)  # Correct

        elif user.is_superuser:  # Check if the user is an admin (superuser)
            auth_login(request, user)
            return redirect(reverse('admin:index'))
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def scoreboard_view(request, court_number):
    if court_number not in {'1', '2', '3', '4', '5', '6', '7', '8', '9'}:
        raise Http404("Court does not exist")

    return render(
        request,
        'scoreboard.html',
        {'court_number': court_number}
    )


def court_view(request, court_number):
    selected_age_category = request.GET.get('age_category', 'all')

    if selected_age_category in ['all', 'open']:
        players = Player.objects.all()
    else:
        players = Player.objects.filter(age_categories__name=selected_age_category)

    male_players = players.filter(gender='M').order_by('name')
    female_players = players.filter(gender='F').order_by('name')

    age_categories = Category.objects.all()

    # Define unique session keys per court
    session_prefix = f'court{court_number}_'
    player1_name = request.session.get(session_prefix + 'player1_name', '')
    player2_name = request.session.get(session_prefix + 'player2_name', '')
    player1_score = int(request.session.get(session_prefix + 'player1_score', 0))
    player2_score = int(request.session.get(session_prefix + 'player2_score', 0))
    current_set = int(request.session.get(session_prefix + 'current_set', 1))
    player1_sets = request.session.get(session_prefix + 'player1_sets', [0, 0, 0])
    player2_sets = request.session.get(session_prefix + 'player2_sets', [0, 0, 0])

    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'increase1':
            player1_score += 1
        elif action == 'decrease1' and player1_score > 0:
            player1_score -= 1
        elif action == 'increase2':
            player2_score += 1
        elif action == 'decrease2' and player2_score > 0:
            player2_score -= 1
        elif action == 'switch':
            player1_name, player2_name = player2_name, player1_name
            player1_score, player2_score = player2_score, player1_score

        # Check if current set is won
        if current_set <= 3:
            if (player1_score >= 21 and player1_score - player2_score >= 2) or player1_score == 30:
                player1_sets[current_set - 1] = player1_score
                player2_sets[current_set - 1] = player2_score
                current_set += 1
                player1_score, player2_score = 0, 0
            elif (player2_score >= 21 and player2_score - player1_score >= 2) or player2_score == 30:
                player1_sets[current_set - 1] = player1_score
                player2_sets[current_set - 1] = player2_score
                current_set += 1
                player1_score, player2_score = 0, 0

        # Save updated session values
        request.session[session_prefix + 'player1_name'] = player1_name
        request.session[session_prefix + 'player2_name'] = player2_name
        request.session[session_prefix + 'player1_score'] = player1_score
        request.session[session_prefix + 'player2_score'] = player2_score
        request.session[session_prefix + 'current_set'] = current_set
        request.session[session_prefix + 'player1_sets'] = player1_sets
        request.session[session_prefix + 'player2_sets'] = player2_sets

    context = {
        'court_number': court_number,
        'male_players': male_players,
        'female_players': female_players,
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
        'current_set': current_set,
        'player1_sets': player1_sets,
        'player2_sets': player2_sets,
        'selected_age_category': selected_age_category,
        'age_categories': age_categories
    }

    # Dynamically render the correct template
    return render(request, f'court.html', context)

