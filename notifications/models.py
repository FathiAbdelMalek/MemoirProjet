from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Notification(models.Model):
    TYPE = (
        (1, 'Demand Subscribe'),
        (2, 'Accept Demand'),
        (3, 'Refuse Demand'),
    )

    type = models.IntegerField(choices=TYPE)
    seen = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    conference = models.ForeignKey('conferences.Conference', on_delete=models.CASCADE, related_name='conference')
    demand = models.ForeignKey('conferences.Demand', on_delete=models.CASCADE, related_name='demand')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='from_user')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='to_user')
