from django.db import models
from django.utils.text import slugify


class Attraction(models.Model):

    CATEGORY_CHOICES = (
        ('Beach', 'Beach'),
        ('Historical Site', 'Historical Site'),
        ('Festival', 'Festival'),
        ('Cultural Centre', 'Cultural Centre'),
        ('Nature', 'Nature'),
        ('Hotel', 'Hotel'),
        ('Restaurant', 'Restaurant'),
    )

    name = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    image = models.ImageField(
        upload_to='tourism/',
        blank=True,
        null=True
    )

    location = models.CharField(
        max_length=255
    )

    description = models.TextField()

    featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name