from django.db import models
from django.urls import reverse


class Gallery(models.Model):

    title = models.CharField(max_length=255)

    slug = models.SlugField(unique=True)

    description = models.TextField(blank=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'gallery_detail',
            kwargs={'slug': self.slug}
        )


class GalleryImage(models.Model):

    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
        related_name='images'
    )

    image = models.ImageField(
        upload_to='gallery/'
    )

    caption = models.CharField(
        max_length=255,
        blank=True
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.gallery.title