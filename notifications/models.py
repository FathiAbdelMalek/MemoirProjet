from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Notification(models.Model):
    TYPE = (
        (1, 'Demand Subscribe'),
        (2, 'Accept Demand'),
        (3, 'Refuse Demand'),
    )

    date = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    type = models.IntegerField(choices=TYPE)
    text = models.CharField(max_length=90, blank=True)
    demand = models.ForeignKey('conferences.Demand', on_delete=models.CASCADE, related_name='demand', blank=True, null=True)
    conference = models.ForeignKey('conferences.Conference', on_delete=models.CASCADE, related_name='conference', blank=True, null=True)
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
