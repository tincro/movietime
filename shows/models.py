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

    class Rating(models.TextChoices):
        G = 'G', 'G'
        PG = 'PG', 'PG'
        PG13 = 'PG13', 'PG-13'
        R = 'R', 'R'
        NC17 = 'NC17', 'NC-17'

    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=50, choices=Genre.choices)
    rating = models.CharField(max_length=5, choices=Rating.choices)
    description = models.CharField(max_length=500)
    length = models.DurationField()
    image = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.title}'
    

class Seat(models.Model):
    displayName = models.CharField(max_length=4)

    isOccupied = models.BooleanField(default=False)
    isFunctional = models.BooleanField(default=True)
    isHandicapped = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'Seat {self.displayName}'
    

class Row(models.Model):
    displayName = models.CharField(max_length=4)
    seats = models.ManyToManyField('Seat')

    def __str__(self) -> str:
        return f'Row {self.displayName}'
    

class Room(models.Model):
    theater = models.ForeignKey('Theater', on_delete=models.CASCADE)
    displayName = models.CharField(max_length=20)   
    rows = models.ManyToManyField('Row')

    isAvailable = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f'Room {self.displayName}'
    

class Showing(models.Model):
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
    room = models.ForeignKey('Room', on_delete=models.PROTECT)
    time = models.TimeField()
    premiere_date = models.DateField()
    final_date = models.DateField()

    def __str__(self) -> str:
        return super().__str__()


class Theater(models.Model):
    name = models.CharField(max_length=250)
    phone = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=500, null=True)

    def __str__(self) -> str:
        return f'Theater {self.name}'
    