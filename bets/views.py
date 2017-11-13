from .models import Bet, Bettor, Taker
from django.shortcuts import render
from django.views import generic


def index(request):
    """
    View function for homepage of site.
    """

    return render(request, 'index.html')


class BetListView(generic.ListView):
    model = Bet


class BetDetailView(generic.DetailView):
    model = Bet
