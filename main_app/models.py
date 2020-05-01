from django.db import models
from django.urls import reverse

SUPPORTED = (
    ('P', 'Playstation'),
    ('N', 'Nintendo'),
    ('X', 'Xbox')
)

class Game(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('games_detail', kwargs={ 'pk': self.id })

class Supporting(models.Model):
    date = models.DateField('supporting date')
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