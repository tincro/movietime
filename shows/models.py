from django.db import models

# Create your models here.
class Movie(models.Model):
    class Genre(models.TextChoices):
        ACTION = 'ACT', 'Action'
        ADVENTURE = 'ADV', 'Adventure'
        ANIMATION = 'ANM', 'Animation'
        COMEDY = 'CMD', 'Comedy'
        CRIME = 'CRM', 'Crime'
        DOCUMENTARY = 'DOC', 'Documentary'
        DRAMA = 'DRM', 'Drama'
        FANTASY ='FNT', 'Fantasy'
        HORROR = 'HOR', 'Horror'
        MUSICAL = 'MSC', 'Musical'
        MYSTERY = 'MST', 'Mystery'
        ROMANCE = 'RMC', 'Romance'
        SCIFI = 'SFY', 'Science-Fiction'
        SPORTS = 'SPT', 'Sports'
        THRILLER = 'TRL', 'Thriller'
        WAR = 'WAR', 'War'
        WESTERN = 'WST', 'Western'

    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, choices=Genre.choices)
    description = models.CharField(max_length=500)
    length = models.DurationField()
    image = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.title}'