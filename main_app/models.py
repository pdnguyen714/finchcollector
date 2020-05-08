from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

SUPPORTED = (
    ('P', 'Playstation'),
    ('N', 'Nintendo'),
    ('X', 'Xbox')
)

class Award(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('awards_detail', kwargs={'pk': self.id})

class Game(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    awards = models.ManyToManyField(Award)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games_detail', kwargs={ 'game_id': self.id })

class Supporting(models.Model):
    date = models.DateField('supported date')
    support = models.CharField(
        max_length=1,
        choices=SUPPORTED,
        default=SUPPORTED[0][0]
    )

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_support_display()} on {self.date}"

    class Meta:
        ordering = ['-date']