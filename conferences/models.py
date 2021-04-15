from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


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
        if timezone.now().date() < self.last_date_for_submit:
            return True
        return False


class Demand(models.Model):

    STATUS = (
        (0, 'waiting'),
        (1, 'accepted'),
        (2, 'refused'),
    )

    note = models.CharField(max_length=500)
    # work = models.FilePathField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)
    demand_date = models.DateTimeField(auto_now_add=True)
