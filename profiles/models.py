from django.contrib.auth import get_user_model
from django.db import models
from django_countries.fields import CountryField


User = get_user_model()


class Profile(models.Model):
    SEX = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    DEGREE = (
        ('Student', 'Student'),
        ('MBB', 'MBB'),
        ('MBA', 'MBA'),
        ('MCB', 'MCB'),
        ('MCA', 'MCA'),
        ('Professor', 'Professor'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True, upload_to='images')
    birth_date = models.DateField(verbose_name="birth date", null=True, blank=True)
    sex = models.CharField(max_length=6, choices=SEX, null=True, blank=True)
    country = CountryField(null=True, blank=True)
    work_place = models.CharField(max_length=30, null=True, blank=True)
    degree = models.CharField(max_length=9, choices=DEGREE, null=True, blank=True)
    speciality = models.CharField(max_length=50, null=True, blank=True)
    web_site = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name
