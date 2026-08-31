from django.db import models
from django.urls import reverse


class Event(models.Model):

    EVENT_TYPES = (
        ('Government', 'Government'),
        ('Community', 'Community'),
        ('Festival', 'Festival'),
        ('Youth', 'Youth'),
        ('Women', 'Women'),
        ('Education', 'Education'),
        ('Health', 'Health'),
        ('Sports', 'Sports'),
    )

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    event_type = models.CharField(
        max_length=50,
        choices=EVENT_TYPES
    )

    image = models.ImageField(
        upload_to='events/',
        blank=True,
        null=True
    )

    description = models.TextField()

    venue = models.CharField(max_length=255)

    start_date = models.DateTimeField()

    end_date = models.DateTimeField()

    organizer = models.CharField(
        max_length=255,
        blank=True
    )

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'event_detail',
            kwargs={'slug': self.slug}
        )