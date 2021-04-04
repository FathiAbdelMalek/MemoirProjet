from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save, post_delete

from notifications.models import Notification


User = get_user_model()


class Conference(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(verbose_name='description')
    # image = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField()
    place = models.CharField(max_length=50)
    enabled = models.BooleanField(default=True)
    creator = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self):
        return self.title


class Demand(models.Model):
    note = models.CharField(max_length=500)
    # work = models.FilePathField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    conference = models.ForeignKey(Conference, on_delete=models.CASCADE)

    def add_subscribe(sender, instance, *args, **kwargs):
        demand = instance

        notify = Notification(
            type=1,
            demand=demand,
            conference=demand.conference,
            sender=demand.user,
            receiver=demand.conference.creator,
        )
        notify.save()

    def delete_subscribe(sender, instance, *args, **kwargs):
        demand = instance

        notify = Notification.objects.filter(conference=demand.conference, sender=demand.user, type=1)
        notify.delete()

    # def accept_subscribe(sender, instance, *args, **kwargs):
    #     demand = instance
    #
    #     notify = Notification(
    #         type=2,
    #         conference=demand.conference,
    #         sender=demand.conference.creator,
    #         receiver=demand.user
    #     )
    #     notify.save()
    #
    # def refuse_subscribe(sender, instance, *args, **kwargs):
    #     demand = instance
    #
    #     notify = Notification(
    #         type=2,
    #         conference=demand.conference,
    #         sender=demand.conference.creator,
    #         receiver=demand.user
    #     )
    #     notify.save()


post_save.connect(Demand.add_subscribe, sender=Demand)
post_delete.connect(Demand.delete_subscribe, sender=Demand)
