from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Bet(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    wager = models.CharField(max_length=100)
    bettor = models.ForeignKey(
        'Bettor', 
        help_text="Enter who made the bet", 
        on_delete=models.CASCADE, 
        null=True
    )
    taker = models.ForeignKey(
        'Taker',
        help_text="Enter who accepted the bet",
        on_delete=models.CASCADE,
        null=True
    )
    won = models.NullBooleanField()
    accepted = models.BooleanField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('bet-detail', args=[str(self.id)])

    def get_winner_or_nothing(self):
        if self.won is not None:
            if self.won:
                return '[' + str(self.bettor) + ']'
            else:
                return '[' + str(self.taker) + ']'
        return ''


class Bettor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Taker(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
