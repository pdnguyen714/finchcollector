from django.shortcuts import render
from .models import Game

from django.http import HttpResponse

# class Game:  # Note that parens are optional if not inheriting from another class
#   def __init__(self, name, company, description):
#     self.name = name
#     self.company = company
#     self.description = description

# games = [
#   Game('League Of Legends', 'Riot Games', 'Mobile Online Battle Arena that pins two teams of five against each other.'),
#   Game('Call Of Duty Warzone', 'Activision Blizzard', 'First Person Shooter that pins up to 100+ players against each other in different modes of play.'),
#   Game('Mobile Legends', 'Moonton', 'Mobile Online Battle Arena that pins two teams together - identical to LoL.')
# ]

def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', { 'game': game})