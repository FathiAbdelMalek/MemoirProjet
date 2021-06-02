from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from conferences.models import Submission

User = get_user_model()


class Notification(models.Model):
    TYPE = (
        (0, 'New Submission'),
        (1, 'Edited Submission'),
        (2, 'Accepted Submission'),
        (3, 'Refused Submission'),
        (4, 'Confirmed Submission'),
    )

    type = models.IntegerField(choices=TYPE)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    conference = models.ForeignKey('conferences.Conference', on_delete=models.CASCADE, related_name='conference')
    submission = models.ForeignKey('conferences.Submission', on_delete=models.CASCADE, related_name='demand')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')


@receiver(post_save, sender=Submission)
def add_submission(instance, created, *args, **kwargs):
    notify = Notification()
    if created:
        notify = Notification(
            type=0,
            submission=instance,
            conference=instance.conference,
            sender=instance.user,
            receiver=instance.conference.organizer,
        )
    else:
        if instance.status == 0:
            notify = Notification(
                type=1,
                submission=instance,
                conference=instance.conference,
                sender=instance.user,
                receiver=instance.conference.organizer
            )
        elif instance.status == 1:
            notify = Notification(
                type=2,
                submission=instance,
                conference=instance.conference,
                sender=instance.conference.organizer,
                receiver=instance.user
            )
        elif instance.status == 2:
            notify = Notification(
                type=3,
                submission=instance,
                conference=instance.conference,
                sender=instance.conference.organizer,
                receiver=instance.user
            )
        elif instance.status == 3:
            notify = Notification(
                type=4,
                submission=instance,
                conference=instance.conference,
                sender=instance.conference.organizer,
                receiver=instance.user
            )
    notify.save()


@receiver(post_delete, sender=Submission)
def delete_submission(instance, *args, **kwargs):
    notify = Notification.objects.filter(conference=instance.conference, sender=instance.user, type=1)
    notify.delete()
