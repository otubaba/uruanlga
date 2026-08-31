from django.db import models


class AboutSection(models.Model):

    title = models.CharField(max_length=200)

    slug = models.SlugField(unique=True)

    image = models.ImageField(
        upload_to='about/',
        blank=True,
        null=True
    )

    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
from django.db import models
from django.urls import reverse
from villages.models import Clan, Ward

class ProminentIndigene(models.Model):

    name = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True
    )

    photo = models.ImageField(
        upload_to="prominent_indigenes/",
        blank=True,
        null=True
    )

    title = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g. Professor, Chief, Dr., Hon., etc."
    )

    profession = models.CharField(
        max_length=255,
        blank=True
    )

    position = models.CharField(
        max_length=255,
        blank=True,
        help_text="Current or notable position"
    )

    community = models.CharField(
        max_length=255,
        blank=True
    )

    clan = models.ForeignKey(
        Clan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="prominent_indigenes"
    )

    ward = models.ForeignKey(
        Ward,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="prominent_indigenes"
    )

    short_bio = models.TextField(
        blank=True
    )

    biography = models.TextField(
        blank=True
    )

    achievements = models.TextField(
        blank=True
    )

    featured = models.BooleanField(
        default=True,
        help_text="Show this person on the homepage"
    )

    order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Prominent Indigene"
        verbose_name_plural = "Prominent Indigenes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "prominent_indigene_detail",
            kwargs={"slug": self.slug}
        )



class HomeHero(models.Model):

    # ============================================================
    # HERO CONTENT
    # ============================================================

    background_image = models.ImageField(
        upload_to="home/hero/",
        blank=True,
        null=True,
        help_text="Main background image for the homepage hero section."
    )

    heading = models.CharField(
        max_length=255,
        default="Building a Greater",
        help_text="Main hero heading."
    )

    highlighted_text = models.CharField(
        max_length=100,
        default="Uruan",
        help_text="Text displayed in yellow."
    )

    heading_suffix = models.CharField(
        max_length=100,
        default="Together",
        help_text="Text displayed after the highlighted text."
    )

    description = models.TextField(
        blank=True,
        default="",
        help_text="Hero introductory description."
    )

    # ============================================================
    # PRIMARY BUTTON
    # ============================================================

    primary_button_text = models.CharField(
        max_length=100,
        default="Latest News"
    )

    primary_button_url = models.CharField(
        max_length=255,
        default="/news/"
    )

    # ============================================================
    # SECONDARY BUTTON
    # ============================================================

    secondary_button_text = models.CharField(
        max_length=100,
        default="Our Projects"
    )

    secondary_button_url = models.CharField(
        max_length=255,
        default="/projects/"
    )

    # ============================================================
    # STATISTICS
    # ============================================================

    population = models.CharField(
        max_length=50,
        default="120K+"
    )

    population_label = models.CharField(
        max_length=100,
        default="Population"
    )

    communities = models.CharField(
        max_length=50,
        default="52"
    )

    communities_label = models.CharField(
        max_length=100,
        default="Communities"
    )

    schools = models.CharField(
        max_length=50,
        default="85+"
    )

    schools_label = models.CharField(
        max_length=100,
        default="Schools"
    )

    health_centres = models.CharField(
        max_length=50,
        default="12"
    )

    health_centres_label = models.CharField(
        max_length=100,
        default="Health Centres"
    )

    markets = models.CharField(
        max_length=50,
        default="8"
    )

    markets_label = models.CharField(
        max_length=100,
        default="Markets"
    )

    projects = models.CharField(
        max_length=50,
        default="50+"
    )

    projects_label = models.CharField(
        max_length=100,
        default="Projects"
    )

    # ============================================================
    # STATUS
    # ============================================================

    is_active = models.BooleanField(
        default=True,
        help_text="Only the active hero will appear on the homepage."
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Homepage Hero"
        verbose_name_plural = "Homepage Hero"
        ordering = ["-updated_at"]

    def __str__(self):
        return self.heading

