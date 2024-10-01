from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Player(models.Model):
    name = models.CharField(max_length=100)
    age_category = models.CharField(max_length=100, choices=[('U19', 'Under 19'), ('Open', 'Open')])  # Add other categories as needed
    country = models.CharField(max_length=100)

    def __str__(self):
        # Return a string that includes the player's name, age category, and country
        return f"{self.name} ({self.age_category}, {self.country})"

