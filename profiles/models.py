from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField


User = get_user_model()


class Profile(models.Model):
    SEXE = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
    )

    DEGREE = (
        (0, 'UNKNOWN'),
        (1, 'Student'),
        (2, 'MAB'),
        (3, 'MAA'),
        (4, 'MCB'),
        (5, 'MCA'),
        (6, 'Professor'),
    )

    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20, default="", null=True, blank=True)
    last_name = models.CharField(max_length=20, default="", null=True, blank=True)
    birth_date = models.DateField(verbose_name="birth date", null=True, blank=True)
    sexe = models.CharField(max_length=7, choices=SEXE, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    country = CountryField(null=True, blank=True)
    work_place = models.CharField(max_length=30, null=True, blank=True)
    degree = models.IntegerField(choices=DEGREE, default=0)
    speciality = models.CharField(max_length=50, null=True, blank=True)
    site = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
