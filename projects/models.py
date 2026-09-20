from django.db import models

from django.urls import reverse
from django.utils.text import slugify


class Project(models.Model):

    STATUS_CHOICES = (
        ('Planning', 'Planning'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Suspended', 'Suspended'),
    )

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )

    description = models.TextField()

    location = models.CharField(
        max_length=200
    )

    contractor = models.CharField(
        max_length=200,
        blank=True
    )

    budget = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=0
    )

    progress = models.PositiveIntegerField(
        default=0
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Planning'
    )

    start_date = models.DateField()

    expected_completion = models.DateField()

    featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        # Prevent progress from exceeding 100
        if self.progress > 100:
            self.progress = 100

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            'project_detail',
            kwargs={'slug': self.slug}
        )
    
