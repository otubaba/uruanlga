from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from villages.models import Clan, Ward


class CouncilLeadership(models.Model):

    COUNCIL_TYPE_CHOICES = (
        ("Executive", "Executive Council"),
        ("Legislative", "Legislative Council"),
    )

    # ==========================================================
    # BASIC INFORMATION
    # ==========================================================

    full_name = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    photo = models.ImageField(
        upload_to="council_leadership/",
        blank=True,
        null=True
    )

    title = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g. Hon., Barr., Engr., Dr., Chief, etc."
    )

    # ==========================================================
    # COUNCIL INFORMATION
    # ==========================================================

    council_type = models.CharField(
        max_length=20,
        choices=COUNCIL_TYPE_CHOICES
    )

    designation = models.CharField(
        max_length=100
    )

    custom_designation = models.CharField(
        max_length=255,
        blank=True,
        help_text="Use this if the designation is not covered above."
    )

    ward = models.CharField(
        max_length=255,
        blank=True
    )

    community = models.CharField(
        max_length=255,
        blank=True
    )

    political_party = models.CharField(
        max_length=100,
        blank=True
    )

    # ==========================================================
    # PERSONAL / PROFESSIONAL INFORMATION
    # ==========================================================

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    profession = models.CharField(
        max_length=255,
        blank=True
    )

    qualification = models.CharField(
        max_length=500,
        blank=True
    )

    biography = models.TextField(
        blank=True
    )

    achievements = models.TextField(
        blank=True
    )

    # ==========================================================
    # CHAIRMAN'S MESSAGE
    # ==========================================================

    chairman_message = models.TextField(
        blank=True,
        help_text=(
            "Official message from the Executive Chairman. "
            "This field is primarily used for the Chairman's profile."
        )
    )

    message_title = models.CharField(
        max_length=255,
        blank=True,
        default="Chairman's Message"
    )

    # ==========================================================
    # TENURE
    # ==========================================================

    date_assumed_office = models.DateField(
        blank=True,
        null=True
    )

    date_left_office = models.DateField(
        blank=True,
        null=True
    )

    current = models.BooleanField(
        default=True,
        help_text="Is this person currently serving?"
    )

    # ==========================================================
    # CONTACT INFORMATION
    # ==========================================================

    email = models.EmailField(
        blank=True
    )

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    office_address = models.TextField(
        blank=True
    )

    # ==========================================================
    # WEBSITE DISPLAY
    # ==========================================================

    featured = models.BooleanField(
        default=True,
        help_text="Display this person on the leadership page."
    )

    show_on_homepage = models.BooleanField(
        default=False,
        help_text="Display this leader on the homepage."
    )

    show_chairman_message = models.BooleanField(
        default=False,
        help_text="Display this person's message as Chairman's Message."
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls the display order."
    )

    # ==========================================================
    # TIMESTAMPS
    # ==========================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # ==========================================================
    # META
    # ==========================================================

    class Meta:

        ordering = [
            "council_type",
            "order",
            "full_name"
        ]

        verbose_name = "Council Leadership"
        verbose_name_plural = "Council Leadership"

    # ==========================================================
    # STRING
    # ==========================================================

    def __str__(self):
        return f"{self.full_name} - {self.display_designation}"

    # ==========================================================
    # SAVE
    # ==========================================================

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(self.full_name)
            slug = base_slug
            counter = 1

            while CouncilLeadership.objects.filter(
                slug=slug
            ).exclude(pk=self.pk).exists():

                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    # ==========================================================
    # ABSOLUTE URL
    # ==========================================================

    def get_absolute_url(self):

        return reverse(
            "leadership_detail",
            kwargs={
                "slug": self.slug
            }
        )

    # ==========================================================
    # DISPLAY DESIGNATION
    # ==========================================================

    @property
    def display_designation(self):

        if self.custom_designation:
            return self.custom_designation

        return self.designation
    

class PastChairman(models.Model):

    # ==========================================================
    # PERSONAL INFORMATION
    # ==========================================================

    full_name = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    title = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g. Hon., Barr., Engr., Dr., Chief, etc."
    )

    photo = models.ImageField(
        upload_to="past_chairmen/",
        blank=True,
        null=True
    )

    # ==========================================================
    # TENURE
    # ==========================================================

    tenure_start = models.DateField(
        blank=True,
        null=True
    )

    tenure_end = models.DateField(
        blank=True,
        null=True
    )

    tenure_description = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g. 2015 - 2018"
    )

    # ==========================================================
    # BACKGROUND
    # ==========================================================

    profession = models.CharField(
        max_length=255,
        blank=True
    )

    qualification = models.CharField(
        max_length=500,
        blank=True
    )

    community = models.CharField(
        max_length=255,
        blank=True
    )

    clan = models.CharField(
        max_length=255,
        blank=True
    )

    biography = models.TextField(
        blank=True
    )

    # ==========================================================
    # SERVICE RECORD
    # ==========================================================

    service_summary = models.TextField(
        blank=True,
        help_text="Summary of the chairman's administration."
    )

    achievements = models.TextField(
        blank=True,
        help_text=(
            "Major projects, policies and accomplishments "
            "recorded during the administration."
        )
    )

    legacy = models.TextField(
        blank=True,
        help_text="Describe the lasting impact of the administration."
    )

    challenges = models.TextField(
        blank=True,
        help_text="Major challenges encountered during the tenure."
    )

    # ==========================================================
    # NOTABLE PROJECTS
    # ==========================================================

    major_projects = models.TextField(
        blank=True,
        help_text=(
            "List major infrastructure, education, health, "
            "roads, water or other projects undertaken."
        )
    )

    # ==========================================================
    # RECOGNITION
    # ==========================================================

    awards = models.TextField(
        blank=True,
        help_text="Awards, honours and recognitions received."
    )

    # ==========================================================
    # WEBSITE DISPLAY
    # ==========================================================

    featured = models.BooleanField(
        default=True,
        help_text="Display this former chairman on the website."
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls display order."
    )

    # ==========================================================
    # TIMESTAMPS
    # ==========================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # ==========================================================
    # META
    # ==========================================================

    class Meta:

        ordering = [
            "-tenure_end",
            "order",
            "full_name",
        ]

        verbose_name = "Past Chairman"
        verbose_name_plural = "Past Chairmen"

    # ==========================================================
    # STRING
    # ==========================================================

    def __str__(self):
        return self.full_name

    # ==========================================================
    # SAVE
    # ==========================================================

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(self.full_name)

            slug = base_slug
            counter = 1

            while PastChairman.objects.filter(
                slug=slug
            ).exclude(pk=self.pk).exists():

                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    # ==========================================================
    # ABSOLUTE URL
    # ==========================================================

    def get_absolute_url(self):

        return reverse(
            "past_chairman_detail",
            kwargs={
                "slug": self.slug
            }
        )

    # ==========================================================
    # TENURE DISPLAY
    # ==========================================================

    @property
    def tenure(self):

        if self.tenure_description:
            return self.tenure_description

        if self.tenure_start and self.tenure_end:
            return (
                f"{self.tenure_start.year} - "
                f"{self.tenure_end.year}"
            )

        if self.tenure_start:
            return f"From {self.tenure_start.year}"

        return "Tenure information unavailable"


class TraditionalLeader(models.Model):

    # ==========================================================
    # LEADERSHIP TYPE
    # ==========================================================

    LEADERSHIP_TYPE_CHOICES = (
        ("Paramount Ruler", "Paramount Ruler"),
        ("Clan Head", "Clan Head"),
        ("Village Head", "Village Head"),
        ("Chief", "Chief"),
        ("Regent", "Regent"),
        ("Traditional Council", "Traditional Council"),
        ("Other", "Other"),
    )

    # ==========================================================
    # BASIC INFORMATION
    # ==========================================================

    full_name = models.CharField(
        max_length=255
    )

    slug = models.SlugField(
        unique=True,
        blank=True
    )

    title = models.CharField(
        max_length=150,
        blank=True,
        help_text="e.g. His Royal Majesty, HRM, Chief, Prince, etc."
    )

    photo = models.ImageField(
        upload_to="traditional_leaders/",
        blank=True,
        null=True
    )

    # ==========================================================
    # TRADITIONAL OFFICE
    # ==========================================================

    leadership_type = models.CharField(
        max_length=50,
        choices=LEADERSHIP_TYPE_CHOICES,
        default="Other"
    )

    traditional_title = models.CharField(
        max_length=255,
        help_text="e.g. Paramount Ruler of Uruan, Clan Head of ..., Village Head of ..."
    )

    custom_designation = models.CharField(
        max_length=255,
        blank=True,
        help_text="Use this where the standard leadership type does not apply."
    )

    # ==========================================================
    # JURISDICTION
    # ==========================================================

    clan = models.ForeignKey(
        Clan,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="traditional_leaders"
    )

    ward = models.ForeignKey(
        Ward,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="traditional_leaders"
    )

    community = models.CharField(
        max_length=255,
        blank=True
    )

    village = models.CharField(
        max_length=255,
        blank=True
    )

    traditional_council = models.CharField(
        max_length=255,
        blank=True,
        help_text="Name of the Traditional Council, where applicable."
    )

    # ==========================================================
    # PERSONAL / PROFESSIONAL INFORMATION
    # ==========================================================

    date_of_birth = models.DateField(
        blank=True,
        null=True
    )

    profession = models.CharField(
        max_length=255,
        blank=True
    )

    qualification = models.CharField(
        max_length=500,
        blank=True
    )

    biography = models.TextField(
        blank=True
    )

    # ==========================================================
    # TRADITIONAL SERVICE
    # ==========================================================

    date_of_ascension = models.DateField(
        blank=True,
        null=True,
        help_text="Date the leader assumed the traditional office."
    )

    date_left_office = models.DateField(
        blank=True,
        null=True
    )

    current = models.BooleanField(
        default=True,
        help_text="Is this person currently holding the traditional office?"
    )

    reign_description = models.CharField(
        max_length=255,
        blank=True,
        help_text="e.g. 2018 - Present"
    )

    # ==========================================================
    # ACHIEVEMENTS & LEGACY
    # ==========================================================

    achievements = models.TextField(
        blank=True,
        help_text="Major achievements and contributions to the community."
    )

    community_development = models.TextField(
        blank=True,
        help_text="Community development initiatives and contributions."
    )

    cultural_contributions = models.TextField(
        blank=True,
        help_text="Contributions to culture, traditions and heritage."
    )

    legacy = models.TextField(
        blank=True,
        help_text="Describe the leader's lasting traditional or community legacy."
    )

    # ==========================================================
    # CONTACT / OFFICIAL INFORMATION
    # ==========================================================

    palace_address = models.TextField(
        blank=True,
        help_text="Palace or official traditional council address."
    )

    phone = models.CharField(
        max_length=50,
        blank=True
    )

    email = models.EmailField(
        blank=True
    )

    # ==========================================================
    # WEBSITE DISPLAY
    # ==========================================================

    featured = models.BooleanField(
        default=True,
        help_text="Display this traditional leader on the website."
    )

    show_on_homepage = models.BooleanField(
        default=False,
        help_text="Display this traditional leader on the homepage."
    )

    order = models.PositiveIntegerField(
        default=0,
        help_text="Controls the display order."
    )

    # ==========================================================
    # TIMESTAMPS
    # ==========================================================

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    # ==========================================================
    # META
    # ==========================================================

    class Meta:

        ordering = [
            "-current",
            "order",
            "full_name",
        ]

        verbose_name = "Traditional Leader"
        verbose_name_plural = "Traditional Leaders"

    # ==========================================================
    # STRING
    # ==========================================================

    def __str__(self):
        return f"{self.full_name} - {self.display_designation}"

    # ==========================================================
    # SAVE
    # ==========================================================

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(self.full_name)

            slug = base_slug
            counter = 1

            while TraditionalLeader.objects.filter(
                slug=slug
            ).exclude(pk=self.pk).exists():

                slug = f"{base_slug}-{counter}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    # ==========================================================
    # ABSOLUTE URL
    # ==========================================================

    def get_absolute_url(self):

        return reverse(
            "traditional_leader_detail",
            kwargs={
                "slug": self.slug
            }
        )

    # ==========================================================
    # DISPLAY DESIGNATION
    # ==========================================================

    @property
    def display_designation(self):

        if self.custom_designation:
            return self.custom_designation

        return self.traditional_title

    # ==========================================================
    # REIGN / SERVICE PERIOD
    # ==========================================================

    @property
    def reign_period(self):

        if self.reign_description:
            return self.reign_description

        if self.date_of_ascension and self.date_left_office:
            return (
                f"{self.date_of_ascension.year} - "
                f"{self.date_left_office.year}"
            )

        if self.date_of_ascension:
            return f"{self.date_of_ascension.year} - Present"

        return "Reign period unavailable"


