from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Game, Award
from .forms import SupportingForm

class GameCreate(LoginRequiredMixin, CreateView):
    model = Game
    fields = ['name', 'company', 'description']

    # This inherited method is called when a
    # valid cat form is being submitted
    def form_valid(self, form):
      # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  # form.instance is the cat
      # Let the CreateView do its job as usual
      return super().form_valid(form)

class GameUpdate(LoginRequiredMixin, UpdateView):
    model = Game
    fields = ['name', 'description']

class GameDelete(LoginRequiredMixin, DeleteView):
    model = Game
    success_url = '/games/'
    
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def games_index(request):
  games = Game.objects.filter(user=request.user)
  return render(request, 'games/index.html', { 'games': games })

@login_required
def games_detail(request, game_id):
  game = Game.objects.get(id=game_id)
  awards_game_doesnt_have = Award.objects.exclude(id__in = game.awards.all().values_list('id'))
  supporting_form = SupportingForm()
  return render(request, 'games/detail.html', {
    # include the cat and feeding_form in the context
    'game': game, 'supporting_form': supporting_form,
    'awards': awards_game_doesnt_have
  })

@login_required
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

@login_required
def assoc_award(request, game_id, award_id):
  Game.objects.get(id=game_id).awards.add(award_id)
  return redirect('games_detail', game_id=game_id)

@login_required
def unassoc_award(request, game_id, award_id):
  Game.objects.get(id=game_id).awards.remove(award_id)
  return redirect('games_detail', game_id=game_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class AwardList(LoginRequiredMixin, ListView):
  model = Award

class AwardDetail(LoginRequiredMixin, DetailView):
  model = Award

class AwardCreate(LoginRequiredMixin, CreateView):
  model = Award
  fields = '__all__'

class AwardUpdate(LoginRequiredMixin, UpdateView):
  model = Award
  fields = ['name', 'color']

class AwardDelete(LoginRequiredMixin, DeleteView):
  model = Award
  success_url = '/awards/'