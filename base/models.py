from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Player(models.Model):
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
) # Add other categories as needed
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
        ('XK', 'Kosovo'),  # Note: Kosovo is not universally recognized
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
        # Additional Balkan countries (if not included above)
        ('BG', 'Bulgaria'),
        ('HR', 'Croatia'),
        ('XK', 'Kosovo'),
        ('ME', 'Montenegro'),
        ('RS', 'Serbia'),
        ('AL', 'Albania'),
        ('MK', 'North Macedonia'),  # Formerly FYROM
    ]
)

    def __str__(self):
        # Return a string that includes the player's name, age category, and country
        return f"{self.name} ({self.age_category}, {self.country})"

