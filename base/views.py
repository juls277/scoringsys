from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
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
    players_data = list(players.values('name', 'age_category', 'country'))
    return JsonResponse(players_data, safe=False)


def home(request):
    return render(request, 'menue.html')


def login(request):
    return render(request, 'login.html')


def court1(request):
    return render(request, 'court1.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if username == 'court1':
            auth_login(request, user)
            return redirect('court1')  # Redirect to home page after successful login
        elif username == 'court2':
            auth_login(request, user)
            return redirect('court2')
        elif username == 'court3':
            auth_login(request, user)
            return redirect('court3')
        elif username == 'court4':
            auth_login(request, user)
            return redirect('court4')
        elif username == 'court5':
            auth_login(request, user)
            return redirect('court5')
        elif username == 'court6':
            auth_login(request, user)
            return redirect('court6')
        elif username == 'court7':
            auth_login(request, user)
            return redirect('court7')
        elif username == 'court8':
            auth_login(request, user)
            return redirect('court8')
        elif username == 'court9':
            auth_login(request, user)
            return redirect('court9')

        elif user.is_superuser:  # Check if the user is an admin (superuser)
            auth_login(request, user)
            return redirect(reverse('admin:index'))
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


def court_one_view(request):
    return render(request, 'court_one.html')


def court_two_view(request):
    return render(request, 'court_two.html')


def court_three_view(request):
    return render(request, 'court_three.html')


def court_four_view(request):
    return render(request, 'court_four.html')


def court_five_view(request):
    return render(request, 'court_five.html')


def court_six_view(request):
    return render(request, 'court_six.html')


def court_seven_view(request):
    return render(request, 'court_seven.html')


def court_eight_view(request):
    return render(request, 'court_eight.html')


def court_nine_view(request):
    return render(request, 'court_nine.html')


def court1_view(request):
    # Retrieve selected age category from GET or default to "all"
    selected_age_category = request.GET.get('age_category', 'all')

    # Filter players based on the selected age category
    if selected_age_category == 'all' or selected_age_category.lower() == 'open':
        players = Player.objects.all()
    else:
        players = Player.objects.filter(age_categories__name=selected_age_category)

    # Group players by gender for display
    male_players = players.filter(gender='M')
    female_players = players.filter(gender='F')

    age_categories = Category.objects.all

    # Session variables
    player1_name = request.session.get('player1_name', '')
    player2_name = request.session.get('player2_name', '')
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets = request.session.get('player1_sets', [0, 0, 0])
    player2_sets = request.session.get('player2_sets', [0, 0, 0])

    # Handle form submissions
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
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets'] = player1_sets
        request.session['player2_sets'] = player2_sets
    male_players = sorted(male_players, key=lambda player: player.name)
    female_players = sorted(female_players, key=lambda player: player.name)

    # Prepare context
    context = {
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

    return render(request, 'court1.html', context)


def court2_view(request):
    # Retrieve selected age category from GET or default to "all"
    selected_age_category = request.GET.get('age_category', 'all')

    # Filter players based on the selected age category
    if selected_age_category == 'all' or selected_age_category.lower() == 'open':
        players = Player.objects.all()
    else:
        players = Player.objects.filter(age_categories__name=selected_age_category)

    # Group players by gender for display
    male_players = players.filter(gender='M')
    female_players = players.filter(gender='F')

    age_categories = Category.objects.all

    # Session variables
    player1_name = request.session.get('player1_name', '')
    player2_name = request.session.get('player2_name', '')
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets = request.session.get('player1_sets', [0, 0, 0])
    player2_sets = request.session.get('player2_sets', [0, 0, 0])

    # Handle form submissions
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
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets'] = player1_sets
        request.session['player2_sets'] = player2_sets
    male_players = sorted(male_players, key=lambda player: player.name)
    female_players = sorted(female_players, key=lambda player: player.name)

    # Prepare context
    context = {
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

    return render(request, 'court2.html', context)


def court3_view(request):
    # Retrieve selected age category from GET or default to "all"
    selected_age_category = request.GET.get('age_category', 'all')

    # Filter players based on the selected age category
    if selected_age_category == 'all' or selected_age_category.lower() == 'open':
        players = Player.objects.all()
    else:
        players = Player.objects.filter(age_categories__name=selected_age_category)

    # Group players by gender for display
    male_players = players.filter(gender='M')
    female_players = players.filter(gender='F')

    age_categories = Category.objects.all

    # Session variables
    player1_name = request.session.get('player1_name', '')
    player2_name = request.session.get('player2_name', '')
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets = request.session.get('player1_sets', [0, 0, 0])
    player2_sets = request.session.get('player2_sets', [0, 0, 0])

    # Handle form submissions
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
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets'] = player1_sets
        request.session['player2_sets'] = player2_sets
    male_players = sorted(male_players, key=lambda player: player.name)
    female_players = sorted(female_players, key=lambda player: player.name)

    # Prepare context
    context = {
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

    return render(request, 'court3.html', context)


def court4_view(request):
    # Retrieve selected age category from GET or default to "all"
    selected_age_category = request.GET.get('age_category', 'all')

    # Filter players based on the selected age category
    if selected_age_category == 'all' or selected_age_category.lower() == 'open':
        players = Player.objects.all()
    else:
        players = Player.objects.filter(age_categories__name=selected_age_category)

    # Group players by gender for display
    male_players = players.filter(gender='M')
    female_players = players.filter(gender='F')

    age_categories = Category.objects.all

    # Session variables
    player1_name = request.session.get('player1_name', '')
    player2_name = request.session.get('player2_name', '')
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets = request.session.get('player1_sets', [0, 0, 0])
    player2_sets = request.session.get('player2_sets', [0, 0, 0])

    # Handle form submissions
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
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets'] = player1_sets
        request.session['player2_sets'] = player2_sets
    male_players = sorted(male_players, key=lambda player: player.name)
    female_players = sorted(female_players, key=lambda player: player.name)

    # Prepare context
    context = {
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

    return render(request, 'court4.html', context)


def court5_view(request):
    # Retrieve selected age category from GET or default to "all"
    selected_age_category = request.GET.get('age_category', 'all')

    # Filter players based on the selected age category
    if selected_age_category == 'all' or selected_age_category.lower() == 'open':
        players = Player.objects.all()
    else:
        players = Player.objects.filter(age_categories__name=selected_age_category)

    # Group players by gender for display
    male_players = players.filter(gender='M')
    female_players = players.filter(gender='F')

    age_categories = Category.objects.all

    # Session variables
    player1_name = request.session.get('player1_name', '')
    player2_name = request.session.get('player2_name', '')
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets = request.session.get('player1_sets', [0, 0, 0])
    player2_sets = request.session.get('player2_sets', [0, 0, 0])

    # Handle form submissions
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
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets'] = player1_sets
        request.session['player2_sets'] = player2_sets
    male_players = sorted(male_players, key=lambda player: player.name)
    female_players = sorted(female_players, key=lambda player: player.name)

    # Prepare context
    context = {
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

    return render(request, 'court5.html', context)


def court6_view(request):
    # Retrieve selected age category from GET or default to "all"
    selected_age_category = request.GET.get('age_category', 'all')

    # Filter players based on the selected age category
    if selected_age_category == 'all' or selected_age_category.lower() == 'open':
        players = Player.objects.all()
    else:
        players = Player.objects.filter(age_categories__name=selected_age_category)

    # Group players by gender for display
    male_players = players.filter(gender='M')
    female_players = players.filter(gender='F')

    age_categories = Category.objects.all

    # Session variables
    player1_name = request.session.get('player1_name', '')
    player2_name = request.session.get('player2_name', '')
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets = request.session.get('player1_sets', [0, 0, 0])
    player2_sets = request.session.get('player2_sets', [0, 0, 0])

    # Handle form submissions
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
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets'] = player1_sets
        request.session['player2_sets'] = player2_sets
    male_players = sorted(male_players, key=lambda player: player.name)
    female_players = sorted(female_players, key=lambda player: player.name)

    # Prepare context
    context = {
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

    return render(request, 'court6.html', context)


def court7_view(request):
    # Retrieve selected age category from GET or default to "all"
    selected_age_category = request.GET.get('age_category', 'all')

    # Filter players based on the selected age category
    if selected_age_category == 'all' or selected_age_category.lower() == 'open':
        players = Player.objects.all()
    else:
        players = Player.objects.filter(age_categories__name=selected_age_category)

    # Group players by gender for display
    male_players = players.filter(gender='M')
    female_players = players.filter(gender='F')

    age_categories = Category.objects.all

    # Session variables
    player1_name = request.session.get('player1_name', '')
    player2_name = request.session.get('player2_name', '')
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets = request.session.get('player1_sets', [0, 0, 0])
    player2_sets = request.session.get('player2_sets', [0, 0, 0])

    # Handle form submissions
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
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets'] = player1_sets
        request.session['player2_sets'] = player2_sets
    male_players = sorted(male_players, key=lambda player: player.name)
    female_players = sorted(female_players, key=lambda player: player.name)

    # Prepare context
    context = {
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

    return render(request, 'court7.html', context)


def court8_view(request):
    # Retrieve selected age category from GET or default to "all"
    selected_age_category = request.GET.get('age_category', 'all')

    # Filter players based on the selected age category
    if selected_age_category == 'all' or selected_age_category.lower() == 'open':
        players = Player.objects.all()
    else:
        players = Player.objects.filter(age_categories__name=selected_age_category)

    # Group players by gender for display
    male_players = players.filter(gender='M')
    female_players = players.filter(gender='F')

    age_categories = Category.objects.all

    # Session variables
    player1_name = request.session.get('player1_name', '')
    player2_name = request.session.get('player2_name', '')
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets = request.session.get('player1_sets', [0, 0, 0])
    player2_sets = request.session.get('player2_sets', [0, 0, 0])

    # Handle form submissions
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
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets'] = player1_sets
        request.session['player2_sets'] = player2_sets
    male_players = sorted(male_players, key=lambda player: player.name)
    female_players = sorted(female_players, key=lambda player: player.name)

    # Prepare context
    context = {
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

    return render(request, 'court8.html', context)


def court9_view(request):
    # Retrieve selected age category from GET or default to "all"
    selected_age_category = request.GET.get('age_category', 'all')

    # Filter players based on the selected age category
    if selected_age_category == 'all' or selected_age_category.lower() == 'open':
        players = Player.objects.all()
    else:
        players = Player.objects.filter(age_categories__name=selected_age_category)

    # Group players by gender for display
    male_players = players.filter(gender='M')
    female_players = players.filter(gender='F')

    age_categories = Category.objects.all

    # Session variables
    player1_name = request.session.get('player1_name', '')
    player2_name = request.session.get('player2_name', '')
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets = request.session.get('player1_sets', [0, 0, 0])
    player2_sets = request.session.get('player2_sets', [0, 0, 0])

    # Handle form submissions
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
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets'] = player1_sets
        request.session['player2_sets'] = player2_sets
    male_players = sorted(male_players, key=lambda player: player.name)
    female_players = sorted(female_players, key=lambda player: player.name)

    # Prepare context
    context = {
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

    return render(request, 'court1.html', context)
