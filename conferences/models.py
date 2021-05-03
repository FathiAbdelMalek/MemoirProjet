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
    created_date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField()
    submission_deadline = models.DateField()
    confirmation_deadline = models.DateField(null=True, blank=True)
    payment_deadline = models.DateField(null=True, blank=True)
    price = models.CharField(max_length=20, null=True, blank=True)
    organizer = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title

    def can_submit(self):
        if timezone.now().date() > self.submission_deadline:
            return False
        return True

    def can_confirm(self):
        if timezone.now().date() <= self.submission_deadline or timezone.now().date() > self.confirmation_deadline:
            return False
        return True

    def can_pay(self):
        if timezone.now().date() <= self.payment_deadline or timezone.now().date() > self.confirmation_deadline:
            return False
        return True


class Submission(models.Model):
    STATUS = (
        (0, 'waiting'),
        (1, 'accepted'),
        (2, 'refused'),
        (3, 'confirmed'),
    )

    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(verbose_name="email", max_length=254, unique=False)
    article_name = models.CharField(max_length=100)
    abstract = models.TextField(verbose_name='abstract')
    article = models.FileField(null=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='article_authors', null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    demand_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    def __str__(self):
        return self.user + " submission in " + self.conference
