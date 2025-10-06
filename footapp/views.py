from django.shortcuts import render, redirect
from .models import Players, Clubs, positions
from .forms import PlayerForm, ClubForm

def home(request):
    return render(request, 'footapp/home.html')

def player_list(request):
    players = Players.objects.all()
    clubs = Clubs.objects.all()

    country = request.GET.get('country')
    club_id = request.GET.get('club')
    position = request.GET.get('position')

    if country:
        players = players.filter(player_country=country)
    if club_id:
        players = players.filter(player_club_id=club_id)
    if position:
        players = players.filter(player_position=position)

    context = {
        'players': players,
        'clubs': clubs,
        'selected_country': country or '',
        'selected_club': club_id or '',
        'selected_position': position or '',
    }

    return render(request, 'footapp/player_list.html', context)


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