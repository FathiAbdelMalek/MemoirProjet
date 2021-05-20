import django_filters
from .models import Conference


class ConferenceFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='contains')
    place = django_filters.CharFilter(field_name='place', lookup_expr='contains')
    date = django_filters.DateFilter(field_name='date', lookup_expr='gte')

    class Meta:
        model = Conference
        fields = ['title', 'place', 'date', 'organizer']
