from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


class Band(models.Model):

    class Genre(models.TextChoices):
            HIP_HOP = 'HH'
            SYNTH_POP = 'SP'
            ALTERNATIV_ROCK = 'AR'

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50, choices=Genre.choices)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2021)] #permet de définir min et max pour le champ
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
    #like_new = models.fields.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}'


class Listing(models.Model):

    class ListingTypes(models.TextChoices):
        RECORDS = 'R'
        CLOTHING = 'C'
        POSTER = 'P'
        MISC = 'M'

    title = models.fields.CharField(max_length=180)
    description = models.fields.CharField(max_length=2000)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(
        null = True,
        validators = [MinValueValidator(1990), MaxValueValidator(2021)]
    )
    type = models.fields.CharField(max_length=5, choices=ListingTypes.choices)
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{self.title}'