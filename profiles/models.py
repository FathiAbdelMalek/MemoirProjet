from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField


User = get_user_model()


class Profile(models.Model):
    SEXE = (
        (1, "MALE"),
        (2, "FEMALE"),
    )

    DEGREE = (
        (0, 'Student'),
        (1, 'MBB'),
        (2, 'MBA'),
        (3, 'MAB'),
        (4, 'MAA'),
        (5, 'Professor'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name="birth date", null=True, blank=True)
    sexe = models.IntegerField(choices=SEXE, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    work_place = models.CharField(max_length=30, null=True, blank=True)
    degree = models.IntegerField(choices=DEGREE, null=True, blank=True)
    speciality = models.CharField(max_length=50, null=True, blank=True)
    web_site = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
