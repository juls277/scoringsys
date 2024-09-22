from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User

# Create your views here.
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
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

from django.shortcuts import render

def scoreboard_view(request):
    # Retrieve scores from session, or initialize if not set
    player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))

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

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score

    context = {
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
    }

    return render(request, 'court1.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def court_one_view(request):
    return render(request, 'court_one.html')

def court_two_view(request):
    return render(request, 'court_two.html')

def court2_view(request):
      # Retrieve scores from session, or initialize if not set
    player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))

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

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score

    context = {
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
    }

    return render(request, 'court2.html', context)