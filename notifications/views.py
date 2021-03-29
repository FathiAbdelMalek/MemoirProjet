from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from notifications.models import Notification


@login_required()
def show_notifications(request):
    notifications = Notification.objects.filter(receiver=request.user).order_by('-date')
    context = {
        'notifications': notifications
    }
    return render(request, 'notifications/nots.html', context)


def delete_notifications(request, pk):
    Notification.objects.filter(id=pk, receiver=request.user).delete()
    return redirect('notifications')


def count_notifications(request):
    count = 0
    if request.user.is_authenticated:
        count = Notification.objects.filter(receiver=request.user, seen=False).count()

    return {'count_notifications': count}
