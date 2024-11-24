from django.db import models


class Player(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    name = models.CharField(max_length=100)
    age_category = models.CharField(
        max_length=100,
        choices=[
            ('U9', 'Under 9'),
            ('U11', 'Under 11'),
            ('U13', 'Under 13'),
            ('U15', 'Under 15'),
            ('U17', 'Under 17'),
            ('U19', 'Under 19'),
            ('Open', 'Open'),
        ]
    )
    country = models.CharField(
        max_length=100,
        choices=[
            ('AL', 'Albania'),
            ('AD', 'Andorra'),
            ('AT', 'Austria'),
            ('BY', 'Belarus'),
            ('BE', 'Belgium'),
            ('BA', 'Bosnia and Herzegovina'),
            ('BG', 'Bulgaria'),
            ('HR', 'Croatia'),
            ('CY', 'Cyprus'),
            ('CZ', 'Czech Republic'),
            ('DK', 'Denmark'),
            ('EE', 'Estonia'),
            ('FI', 'Finland'),
            ('FR', 'France'),
            ('DE', 'Germany'),
            ('GR', 'Greece'),
            ('HU', 'Hungary'),
            ('IS', 'Iceland'),
            ('IE', 'Ireland'),
            ('IT', 'Italy'),
            ('XK', 'Kosovo'),
            ('LV', 'Latvia'),
            ('LT', 'Lithuania'),
            ('LU', 'Luxembourg'),
            ('MT', 'Malta'),
            ('MD', 'Moldova'),
            ('MC', 'Monaco'),
            ('ME', 'Montenegro'),
            ('NL', 'Netherlands'),
            ('NO', 'Norway'),
            ('PL', 'Poland'),
            ('PT', 'Portugal'),
            ('RO', 'Romania'),
            ('RU', 'Russia'),
            ('SM', 'San Marino'),
            ('RS', 'Serbia'),
            ('SK', 'Slovakia'),
            ('SI', 'Slovenia'),
            ('ES', 'Spain'),
            ('SE', 'Sweden'),
            ('CH', 'Switzerland'),
            ('UA', 'Ukraine'),
            ('GB', 'United Kingdom'),
            ('VA', 'Vatican City'),
            ('MK', 'North Macedonia'),
        ]
    )
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
    )

    def __str__(self):
        return f"{self.name} ({self.country})"


# Proxy models for separating men and women
class MalePlayer(Player):
    objects = models.Manager()

    class Meta:
        proxy = True
        verbose_name = "Male Player"
        verbose_name_plural = "Male Players"


class FemalePlayer(Player):
    objects = models.Manager()

    class Meta:
        proxy = True
        verbose_name = "Female Player"
        verbose_name_plural = "Female Players"
