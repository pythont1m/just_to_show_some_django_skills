from django.shortcuts import render, redirect
from .models import Players, Clubs
from .forms import PlayerForm, ClubForm

def home(request):
    return render(request, 'footapp/home.html')

def player_list(request):
    return render(request, 'footapp/player_list.html', {'players': Players.objects.all()})

def club_list(request):
    return render(request, 'footapp/clubs_list.html', {'clubs': Clubs.objects.all()})

def add_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'footapp/add_player.html', {'form': form})

def add_club(request):
    if request.method == 'POST':
        form = ClubForm(request.POST, request.FILES)
        if form .is_valid():
            form.save()
            return redirect('club_list')
    else:
        form = ClubForm()
    return render(request, 'footapp/add_club.html', {'form': form})