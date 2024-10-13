from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.db import models
from .models import Player

# Create your views here.
# views.py

from .forms import PlayerSelectionForm

def get_players(request):
    players = Player.objects.all().values('name', 'age_category', 'country')
    return JsonResponse(list(players), safe=False)

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


def scoreboard_view(request):
    # Retrieve scores from session, or initialize if not set
    #player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    #player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    players = Player.objects.all().values('name', 'age_category', 'country')
    
    # Convert QuerySet to a list of dictionaries
    players_list = list(players)
    player1_name =  players_list
    player2_name = players_list
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets_0 = int(request.session.get('player1_sets.0', 0))
    player1_sets_1 = int(request.session.get('player1_sets.1', 0))
    player1_sets_2 = int(request.session.get('player1_sets.2', 0))
    player2_sets_0 = int(request.session.get('player2_sets.0', 0))
    player2_sets_1 = int(request.session.get('player2_sets.1', 0))
    player2_sets_2 = int(request.session.get('player2_sets.2', 0))

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

        while(current_set<=3):
            if (current_set == 1):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_0 == player1_score
                    player2_sets_0 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 2):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_1 == player1_score
                    player2_sets_1 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 3):        
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_2 == player1_score
                    player2_sets_2 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0


            

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets.0'] = player1_sets_0
        request.session['player1_sets.1'] = player1_sets_1
        request.session['player1_sets.2'] = player1_sets_2
        request.session['player2_sets.0'] = player1_sets_0
        request.session['player2_sets.1'] = player1_sets_1
        request.session['player2_sets.2'] = player1_sets_2


    context = {
        'players': players_list, 
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
        'current_set':current_set,
        'player1_sets.0':player1_sets_0,
        'player1_sets.1':player1_sets_1,
        'player1_sets.2':player1_sets_2,
        'player2_sets.0':player1_sets_0,
        'player2_sets.1':player1_sets_1,
        'player2_sets.2':player1_sets_2,
    }

    return render(request, 'court1.html', context)


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



def court2_view(request):
      # Retrieve scores from session, or initialize if not set
    # Retrieve scores from session, or initialize if not set
    #player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    #player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    players = Player.objects.all().values('name', 'age_category', 'country')
    
    # Convert QuerySet to a list of dictionaries
    players_list = list(players)
    player1_name =  players_list
    player2_name = players_list
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets_0 = int(request.session.get('player1_sets.0', 0))
    player1_sets_1 = int(request.session.get('player1_sets.1', 0))
    player1_sets_2 = int(request.session.get('player1_sets.2', 0))
    player2_sets_0 = int(request.session.get('player2_sets.0', 0))
    player2_sets_1 = int(request.session.get('player2_sets.1', 0))
    player2_sets_2 = int(request.session.get('player2_sets.2', 0))

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

        while(current_set<=3):
            if (current_set == 1):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_0 == player1_score
                    player2_sets_0 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 2):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_1 == player1_score
                    player2_sets_1 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 3):        
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_2 == player1_score
                    player2_sets_2 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0


            

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets.0'] = player1_sets_0
        request.session['player1_sets.1'] = player1_sets_1
        request.session['player1_sets.2'] = player1_sets_2
        request.session['player2_sets.0'] = player1_sets_0
        request.session['player2_sets.1'] = player1_sets_1
        request.session['player2_sets.2'] = player1_sets_2


    context = {
        'players': players_list, 
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
        'current_set':current_set,
        'player1_sets.0':player1_sets_0,
        'player1_sets.1':player1_sets_1,
        'player1_sets.2':player1_sets_2,
        'player2_sets.0':player1_sets_0,
        'player2_sets.1':player1_sets_1,
        'player2_sets.2':player1_sets_2,
    }

    return render(request, 'court2.html', context)

def court3_view(request):
      # Retrieve scores from session, or initialize if not set
    # Retrieve scores from session, or initialize if not set
    #player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    #player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    players = Player.objects.all().values('name', 'age_category', 'country')
    
    # Convert QuerySet to a list of dictionaries
    players_list = list(players)
    player1_name =  players_list
    player2_name = players_list
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets_0 = int(request.session.get('player1_sets.0', 0))
    player1_sets_1 = int(request.session.get('player1_sets.1', 0))
    player1_sets_2 = int(request.session.get('player1_sets.2', 0))
    player2_sets_0 = int(request.session.get('player2_sets.0', 0))
    player2_sets_1 = int(request.session.get('player2_sets.1', 0))
    player2_sets_2 = int(request.session.get('player2_sets.2', 0))

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

        while(current_set<=3):
            if (current_set == 1):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_0 == player1_score
                    player2_sets_0 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 2):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_1 == player1_score
                    player2_sets_1 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 3):        
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_2 == player1_score
                    player2_sets_2 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0


            

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets.0'] = player1_sets_0
        request.session['player1_sets.1'] = player1_sets_1
        request.session['player1_sets.2'] = player1_sets_2
        request.session['player2_sets.0'] = player1_sets_0
        request.session['player2_sets.1'] = player1_sets_1
        request.session['player2_sets.2'] = player1_sets_2


    context = {
        'players': players_list, 
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
        'current_set':current_set,
        'player1_sets.0':player1_sets_0,
        'player1_sets.1':player1_sets_1,
        'player1_sets.2':player1_sets_2,
        'player2_sets.0':player1_sets_0,
        'player2_sets.1':player1_sets_1,
        'player2_sets.2':player1_sets_2,
    }

    return render(request, 'court3.html', context)

def court4_view(request):
      # Retrieve scores from session, or initialize if not set
    # Retrieve scores from session, or initialize if not set
    #player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    #player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    players = Player.objects.all().values('name', 'age_category', 'country')
    
    # Convert QuerySet to a list of dictionaries
    players_list = list(players)
    player1_name =  players_list
    player2_name = players_list
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets_0 = int(request.session.get('player1_sets.0', 0))
    player1_sets_1 = int(request.session.get('player1_sets.1', 0))
    player1_sets_2 = int(request.session.get('player1_sets.2', 0))
    player2_sets_0 = int(request.session.get('player2_sets.0', 0))
    player2_sets_1 = int(request.session.get('player2_sets.1', 0))
    player2_sets_2 = int(request.session.get('player2_sets.2', 0))

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

        while(current_set<=3):
            if (current_set == 1):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_0 == player1_score
                    player2_sets_0 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 2):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_1 == player1_score
                    player2_sets_1 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 3):        
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_2 == player1_score
                    player2_sets_2 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0


            

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets.0'] = player1_sets_0
        request.session['player1_sets.1'] = player1_sets_1
        request.session['player1_sets.2'] = player1_sets_2
        request.session['player2_sets.0'] = player1_sets_0
        request.session['player2_sets.1'] = player1_sets_1
        request.session['player2_sets.2'] = player1_sets_2


    context = {
        'players': players_list, 
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
        'current_set':current_set,
        'player1_sets.0':player1_sets_0,
        'player1_sets.1':player1_sets_1,
        'player1_sets.2':player1_sets_2,
        'player2_sets.0':player1_sets_0,
        'player2_sets.1':player1_sets_1,
        'player2_sets.2':player1_sets_2,
    }

    return render(request, 'court4.html', context)

def court5_view(request):
      # Retrieve scores from session, or initialize if not set
    # Retrieve scores from session, or initialize if not set
    #player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    #player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    players = Player.objects.all().values('name', 'age_category', 'country')
    
    # Convert QuerySet to a list of dictionaries
    players_list = list(players)
    player1_name =  players_list
    player2_name = players_list
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets_0 = int(request.session.get('player1_sets.0', 0))
    player1_sets_1 = int(request.session.get('player1_sets.1', 0))
    player1_sets_2 = int(request.session.get('player1_sets.2', 0))
    player2_sets_0 = int(request.session.get('player2_sets.0', 0))
    player2_sets_1 = int(request.session.get('player2_sets.1', 0))
    player2_sets_2 = int(request.session.get('player2_sets.2', 0))

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

        while(current_set<=3):
            if (current_set == 1):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_0 == player1_score
                    player2_sets_0 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 2):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_1 == player1_score
                    player2_sets_1 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 3):        
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_2 == player1_score
                    player2_sets_2 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0


            

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets.0'] = player1_sets_0
        request.session['player1_sets.1'] = player1_sets_1
        request.session['player1_sets.2'] = player1_sets_2
        request.session['player2_sets.0'] = player1_sets_0
        request.session['player2_sets.1'] = player1_sets_1
        request.session['player2_sets.2'] = player1_sets_2


    context = {
        'players': players_list, 
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
        'current_set':current_set,
        'player1_sets.0':player1_sets_0,
        'player1_sets.1':player1_sets_1,
        'player1_sets.2':player1_sets_2,
        'player2_sets.0':player1_sets_0,
        'player2_sets.1':player1_sets_1,
        'player2_sets.2':player1_sets_2,
    }

    return render(request, 'court5.html', context)

def court6_view(request):
      # Retrieve scores from session, or initialize if not set
    # Retrieve scores from session, or initialize if not set
    #player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    #player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    players = Player.objects.all().values('name', 'age_category', 'country')
    
    # Convert QuerySet to a list of dictionaries
    players_list = list(players)
    player1_name =  players_list
    player2_name = players_list
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets_0 = int(request.session.get('player1_sets.0', 0))
    player1_sets_1 = int(request.session.get('player1_sets.1', 0))
    player1_sets_2 = int(request.session.get('player1_sets.2', 0))
    player2_sets_0 = int(request.session.get('player2_sets.0', 0))
    player2_sets_1 = int(request.session.get('player2_sets.1', 0))
    player2_sets_2 = int(request.session.get('player2_sets.2', 0))

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

        while(current_set<=3):
            if (current_set == 1):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_0 == player1_score
                    player2_sets_0 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 2):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_1 == player1_score
                    player2_sets_1 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 3):        
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_2 == player1_score
                    player2_sets_2 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0


            

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets.0'] = player1_sets_0
        request.session['player1_sets.1'] = player1_sets_1
        request.session['player1_sets.2'] = player1_sets_2
        request.session['player2_sets.0'] = player1_sets_0
        request.session['player2_sets.1'] = player1_sets_1
        request.session['player2_sets.2'] = player1_sets_2


    context = {
        'players': players_list, 
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
        'current_set':current_set,
        'player1_sets.0':player1_sets_0,
        'player1_sets.1':player1_sets_1,
        'player1_sets.2':player1_sets_2,
        'player2_sets.0':player1_sets_0,
        'player2_sets.1':player1_sets_1,
        'player2_sets.2':player1_sets_2,
    }

    return render(request, 'court6.html', context)

def court7_view(request):
      # Retrieve scores from session, or initialize if not set
    # Retrieve scores from session, or initialize if not set
    #player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    #player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    players = Player.objects.all().values('name', 'age_category', 'country')
    
    # Convert QuerySet to a list of dictionaries
    players_list = list(players)
    player1_name =  players_list
    player2_name = players_list
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets_0 = int(request.session.get('player1_sets.0', 0))
    player1_sets_1 = int(request.session.get('player1_sets.1', 0))
    player1_sets_2 = int(request.session.get('player1_sets.2', 0))
    player2_sets_0 = int(request.session.get('player2_sets.0', 0))
    player2_sets_1 = int(request.session.get('player2_sets.1', 0))
    player2_sets_2 = int(request.session.get('player2_sets.2', 0))

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

        while(current_set<=3):
            if (current_set == 1):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_0 == player1_score
                    player2_sets_0 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 2):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_1 == player1_score
                    player2_sets_1 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 3):        
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_2 == player1_score
                    player2_sets_2 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0


            

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets.0'] = player1_sets_0
        request.session['player1_sets.1'] = player1_sets_1
        request.session['player1_sets.2'] = player1_sets_2
        request.session['player2_sets.0'] = player1_sets_0
        request.session['player2_sets.1'] = player1_sets_1
        request.session['player2_sets.2'] = player1_sets_2


    context = {
        'players': players_list, 
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
        'current_set':current_set,
        'player1_sets.0':player1_sets_0,
        'player1_sets.1':player1_sets_1,
        'player1_sets.2':player1_sets_2,
        'player2_sets.0':player1_sets_0,
        'player2_sets.1':player1_sets_1,
        'player2_sets.2':player1_sets_2,
    }

    return render(request, 'court7.html', context)

def court8_view(request):
      # Retrieve scores from session, or initialize if not set
    # Retrieve scores from session, or initialize if not set
    #player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    #player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    players = Player.objects.all().values('name', 'age_category', 'country')
    
    # Convert QuerySet to a list of dictionaries
    players_list = list(players)
    player1_name =  players_list
    player2_name = players_list
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets_0 = int(request.session.get('player1_sets.0', 0))
    player1_sets_1 = int(request.session.get('player1_sets.1', 0))
    player1_sets_2 = int(request.session.get('player1_sets.2', 0))
    player2_sets_0 = int(request.session.get('player2_sets.0', 0))
    player2_sets_1 = int(request.session.get('player2_sets.1', 0))
    player2_sets_2 = int(request.session.get('player2_sets.2', 0))

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

        while(current_set<=3):
            if (current_set == 1):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_0 == player1_score
                    player2_sets_0 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 2):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_1 == player1_score
                    player2_sets_1 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 3):        
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_2 == player1_score
                    player2_sets_2 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0


            

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets.0'] = player1_sets_0
        request.session['player1_sets.1'] = player1_sets_1
        request.session['player1_sets.2'] = player1_sets_2
        request.session['player2_sets.0'] = player1_sets_0
        request.session['player2_sets.1'] = player1_sets_1
        request.session['player2_sets.2'] = player1_sets_2


    context = {
        'players': players_list, 
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
        'current_set':current_set,
        'player1_sets.0':player1_sets_0,
        'player1_sets.1':player1_sets_1,
        'player1_sets.2':player1_sets_2,
        'player2_sets.0':player1_sets_0,
        'player2_sets.1':player1_sets_1,
        'player2_sets.2':player1_sets_2,
    }

    return render(request, 'court8.html', context)

def court9_view(request):
      # Retrieve scores from session, or initialize if not set
    # Retrieve scores from session, or initialize if not set
    #player1_name = request.POST.get('name1', request.session.get('player1_name', 'Player 1'))
    #player2_name = request.POST.get('name2', request.session.get('player2_name', 'Player 2'))
    players = Player.objects.all().values('name', 'age_category', 'country')
    
    # Convert QuerySet to a list of dictionaries
    players_list = list(players)
    player1_name =  players_list
    player2_name = players_list
    player1_score = int(request.session.get('player1_score', 0))
    player2_score = int(request.session.get('player2_score', 0))
    current_set = int(request.session.get('current_set', 1))
    player1_sets_0 = int(request.session.get('player1_sets.0', 0))
    player1_sets_1 = int(request.session.get('player1_sets.1', 0))
    player1_sets_2 = int(request.session.get('player1_sets.2', 0))
    player2_sets_0 = int(request.session.get('player2_sets.0', 0))
    player2_sets_1 = int(request.session.get('player2_sets.1', 0))
    player2_sets_2 = int(request.session.get('player2_sets.2', 0))

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

        while(current_set<=3):
            if (current_set == 1):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_0 == player1_score
                    player2_sets_0 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 2):
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_1 == player1_score
                    player2_sets_1 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0
            if (current_set == 3):        
                if (player1_score == 19 and player2_score == 21 ) or (player1_score == 21 and player2_score == 19):
                    player1_sets_2 == player1_score
                    player2_sets_2 == player2_score
                    current_set+=1
                    player1_score = 0
                    player2_score = 0


            

        # Store updated values in session
        request.session['player1_name'] = player1_name
        request.session['player2_name'] = player2_name
        request.session['player1_score'] = player1_score
        request.session['player2_score'] = player2_score
        request.session['current_set'] = current_set
        request.session['player1_sets.0'] = player1_sets_0
        request.session['player1_sets.1'] = player1_sets_1
        request.session['player1_sets.2'] = player1_sets_2
        request.session['player2_sets.0'] = player1_sets_0
        request.session['player2_sets.1'] = player1_sets_1
        request.session['player2_sets.2'] = player1_sets_2


    context = {
        'players': players_list, 
        'player1_name': player1_name,
        'player2_name': player2_name,
        'player1_score': player1_score,
        'player2_score': player2_score,
        'current_set':current_set,
        'player1_sets.0':player1_sets_0,
        'player1_sets.1':player1_sets_1,
        'player1_sets.2':player1_sets_2,
        'player2_sets.0':player1_sets_0,
        'player2_sets.1':player1_sets_1,
        'player2_sets.2':player1_sets_2,
    }

    return render(request, 'court9.html', context)