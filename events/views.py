from django.views.generic import ListView, DetailView
from django.utils import timezone

from .models import Event, Organizer, Speaker


class EventListView(ListView):
    model = Event
    context_object_name = 'events'
    paginate_by = 9

    def get_queryset(self):
        queryset = Event.published.filter(
            event_date__gte=timezone.now(),
        )
        return queryset.select_related('place')


class EventDetailView(DetailView):
    model = Event

    def get_queryset(self):
        return Event.published.all()


class OrganizerListView(ListView):
    model = Organizer
    context_object_name = 'organizers'
    paginate_by = 9


class OrganizerDetailView(DetailView):
    model = Organizer


class SpeakerDetailView(DetailView):
    model = Speaker

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = self.get_object().events(manager='published').filter(
            event_date__gte=timezone.now(),
        ).all()[:9]
        context['past_events'] = self.get_object().events(manager='published').filter(
            event_date__lt=timezone.now(),
        ).order_by('-event_date').all()[:9]
        return context
