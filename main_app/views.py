from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game
from .forms import SupportingForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class GameList(ListView):
    model = Game
    
    def get_queryset(self):
        return Game.objects.all()

def game_detail(request, pk):
  game = Game.objects.get(id=pk)
  # instantiate FeedingForm to be rendered in the template
  supporting_form = SupportingForm()
  return render(request, 'main_app/game_detail.html', {
    # include the cat and feeding_form in the context
    'game': game, 
    'supporting_form': supporting_form
  })

def add_supporting(request, pk):
  # create the ModelForm using the data in request.POST
  form = SupportingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_supporting = form.save(commit=False)
    new_supporting.game_id = pk
    new_supporting.save()
  return redirect('games_detail', pk=pk)

# def games_detail(request, game_id):
#     game = Game.objects.get(id=game_id)
#     return render(request, 'games/detail.html', {'game': game})

class GameCreate(CreateView):
    model = Game
    fields = '__all__'

class GameUpdate(UpdateView):
    model = Game
    fields = ['name', 'description']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'