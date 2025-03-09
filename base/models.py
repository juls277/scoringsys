from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Player(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]


    name = models.CharField(max_length=100)
    age_categories = models.ManyToManyField(Category, related_name="players")

    country = models.CharField(
        max_length=100,
        choices=[
            # European Countries
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
            ('GB-ENG', 'England'),
            ('GB-SCT', 'Scotland'),
            ('GB-WLS', 'Wales'),
            ('IE', 'Ireland'),
            ('VA', 'Vatican City'),
            ('MK', 'North Macedonia'),

            # Asian Countries
            ('AF', 'Afghanistan'),
            ('AM', 'Armenia'),
            ('AZ', 'Azerbaijan'),
            ('BH', 'Bahrain'),
            ('BD', 'Bangladesh'),
            ('BT', 'Bhutan'),
            ('BN', 'Brunei'),
            ('KH', 'Cambodia'),
            ('CN', 'China'),
            ('CY', 'Cyprus'),
            ('GE', 'Georgia'),
            ('IN', 'India'),
            ('ID', 'Indonesia'),
            ('IR', 'Iran'),
            ('IQ', 'Iraq'),
            ('IL', 'Israel'),
            ('JP', 'Japan'),
            ('JO', 'Jordan'),
            ('KZ', 'Kazakhstan'),
            ('KW', 'Kuwait'),
            ('KG', 'Kyrgyzstan'),
            ('LA', 'Laos'),
            ('LB', 'Lebanon'),
            ('MY', 'Malaysia'),
            ('MV', 'Maldives'),
            ('MN', 'Mongolia'),
            ('MM', 'Myanmar'),
            ('NP', 'Nepal'),
            ('OM', 'Oman'),
            ('PK', 'Pakistan'),
            ('PH', 'Philippines'),
            ('QA', 'Qatar'),
            ('SA', 'Saudi Arabia'),
            ('SG', 'Singapore'),
            ('KR', 'South Korea'),
            ('LK', 'Sri Lanka'),
            ('SY', 'Syria'),
            ('TJ', 'Tajikistan'),
            ('TH', 'Thailand'),
            ('TR', 'Turkey'),
            ('TM', 'Turkmenistan'),
            ('AE', 'United Arab Emirates'),
            ('UZ', 'Uzbekistan'),
            ('VN', 'Vietnam'),
            ('YE', 'Yemen'),
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
