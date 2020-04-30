from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class GameList(ListView):
    model = Game
    
    def get_queryset(self):
        return Game.objects.all()

class GameDetail(DetailView):
    model = Game

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    return render(request, 'games/detail.html', {'game': game})

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = ['name', 'description']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'