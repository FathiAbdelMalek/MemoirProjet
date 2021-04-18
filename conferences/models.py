from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(verbose_name="email", max_length=254, unique=False)

    def __str__(self):
        return self.last_name + " " + self.first_name


class Conference(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(verbose_name='description')
    place = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    last_date_for_submit = models.DateField()
    last_date_for_confirm = models.DateField(null=True, blank=True)
    last_date_for_pay = models.DateField(null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title

    def can_demand(self):
        if timezone.now().date() > self.last_date_for_submit:
            return False
        return True

    def can_confirm(self):
        if timezone.now().date() <= self.last_date_for_submit or timezone.now().date() > self.last_date_for_confirm:
            return False
        return True


class Demand(models.Model):
    STATUS = (
        (0, 'waiting'),
        (1, 'accepted'),
        (2, 'refused'),
        (3, 'confirmed'),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(verbose_name="email", max_length=254, unique=False)
    abstract = models.TextField(verbose_name='abstract')
    article = models.FileField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author, related_name='article_authors')
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    demand_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user + " -> " + self.conference
