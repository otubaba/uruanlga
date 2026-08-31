from django.db import models


class Location(models.Model):

    LOCATION_TYPES = (
        ('Village', 'Village'),
        ('Ward', 'Ward'),
        ('School', 'School'),
        ('Health Centre', 'Health Centre'),
        ('Tourist Site', 'Tourist Site'),
        ('Project', 'Project'),
    )

    name = models.CharField(max_length=255)

    location_type = models.CharField(
        max_length=50,
        choices=LOCATION_TYPES
    )

    description = models.TextField(blank=True)

    latitude = models.FloatField()

    longitude = models.FloatField()

    image = models.ImageField(
        upload_to='locations/',
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name