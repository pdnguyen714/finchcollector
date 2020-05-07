from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Game, Award
from .forms import SupportingForm

class GameCreate(CreateView):
    model = Game
    fields = ['name', 'company', 'description']

class GameUpdate(UpdateView):
    model = Game
    fields = ['name', 'description']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'
    
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def games_index(request):
  games = Game.objects.all()
  return render(request, 'games/index.html', { 'games': games })

def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  awards_game_doesnt_have = Award.objects.exclude(id__in = game.awards.all().values_list('id'))
  supporting_form = SupportingForm()
  return render(request, 'games/detail.html', {
    # include the cat and feeding_form in the context
    'game': game, 'supporting_form': supporting_form,
    'awards': awards_game_doesnt_have
  })

def add_supporting(request, game_id):
  # create the ModelForm using the data in request.POST
  form = SupportingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_supporting = form.save(commit=False)
    new_supporting.game_id = game_id
    new_supporting.save()
  return redirect('games_detail', game_id=game_id)

def assoc_award(request, game_id, award_id):
  Game.objects.get(id=game_id).awards.add(award_id)
  return redirect('games_detail', game_id=game_id)

def unassoc_award(request, game_id, award_id):
  Game.objects.get(id=game_id).awards.remove(award_id)
  return redirect('games_detail', game_id=game_id)

class AwardList(ListView):
  model = Award

class AwardDetail(DetailView):
  model = Award

class AwardCreate(CreateView):
  model = Award
  fields = '__all__'

class AwardUpdate(UpdateView):
  model = Award
  fields = ['name', 'color']

class AwardDelete(DeleteView):
  model = Award
  success_url = '/awards/'