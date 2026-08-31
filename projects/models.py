from django.db import models


class Project(models.Model):

    STATUS_CHOICES = (
        ('Planning', 'Planning'),
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
        ('Suspended', 'Suspended'),
    )

    title = models.CharField(max_length=200)

    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )

    description = models.TextField()

    location = models.CharField(max_length=200)

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

    featured = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title