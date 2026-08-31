from django.db import models


class ContactMessage(models.Model):

    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Reviewed', 'Reviewed'),
        ('Resolved', 'Resolved'),
    )

    name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(
        max_length=20,
        blank=True
    )

    subject = models.CharField(max_length=255)

    message = models.TextField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name
    

class Department(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField()

    phone = models.CharField(max_length=50)

    office_location = models.CharField(
        max_length=255
    )

    description = models.TextField(
        blank=True
    )

    def __str__(self):
        return self.name