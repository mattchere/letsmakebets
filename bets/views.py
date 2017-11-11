from .models import Bet, Bettor, Taker
from django.shortcuts import render
from django.views import generic

# Create your views here.
class BetDetailView(generic.DetailView):
    model = Bet
