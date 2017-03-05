from django.db import models
from django.conf import settings

from model_utils.models import TimeStampedModel


class Event(TimeStampedModel):
    EVENT_TYPE_LECTURE = 1
    EVENT_TYPE_MASTER_CLASS = 2
    EVENT_TYPE_EXCURSION = 3
    EVENT_TYPE_SHOW = 4
    EVENT_TYPE_ROUND_TABLE = 5
    EVENT_TYPE_CONFERENCE = 6
    EVENT_TYPE_MEETING = 7
    EVENT_TYPE_DEBATE = 8
    EVENT_TYPES = (
        (EVENT_TYPE_LECTURE, 'Lecture'),
        (EVENT_TYPE_MASTER_CLASS, 'Master class'),
        (EVENT_TYPE_EXCURSION, 'Excursion'),
        (EVENT_TYPE_SHOW, 'Show'),
        (EVENT_TYPE_ROUND_TABLE, 'Round table'),
        (EVENT_TYPE_CONFERENCE, 'Conference'),
        (EVENT_TYPE_MEETING, 'Meeting'),
        (EVENT_TYPE_DEBATE, 'Debate'),
    )

    EVENT_TOPIC_DESIGN = 1
    EVENT_TOPIC_CITY = 2
    EVENT_TOPIC_SCIENCE = 3
    EVENT_TOPIC_ART = 4
    EVENT_TOPIC_BUSINESS = 5
    EVENT_TOPIC_SOCIETY = 6
    EVENT_TOPIC_TECHNOLOGY = 7
    EVENT_TOPIC_MEDIA = 8
    EVENT_TOPIC_CULTURE = 9
    EVENT_TOPIC_PHOTOGRAPHY = 10
    EVENT_TOPIC_CINEMA = 11
    EVENT_TOPICS = (
        (EVENT_TOPIC_DESIGN, 'Design'),
        (EVENT_TOPIC_CITY, 'City'),
        (EVENT_TOPIC_SCIENCE, 'Science'),
        (EVENT_TOPIC_ART, 'Art'),
        (EVENT_TOPIC_BUSINESS, 'Business'),
        (EVENT_TOPIC_SOCIETY, 'Society'),
        (EVENT_TOPIC_TECHNOLOGY, 'Technology'),
        (EVENT_TOPIC_MEDIA, 'Media'),
        (EVENT_TOPIC_CULTURE, 'Culture'),
        (EVENT_TOPIC_PHOTOGRAPHY, 'Photography'),
        (EVENT_TOPIC_CINEMA, 'Cinema'),
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    event_type = models.PositiveSmallIntegerField(choices=EVENT_TYPES)
    topic = models.PositiveSmallIntegerField(choices=EVENT_TOPICS)
    event_date = models.DateTimeField()
    event_end_date = models.DateTimeField(null=True, blank=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=9)
    image = models.ImageField(blank=True, null=True)
    organizer = models.CharField(max_length=255)
    place = models.ForeignKey('places.Place')
    is_published = models.BooleanField(default=False)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.title
