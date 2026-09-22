from django.db import models
from django.urls import reverse


class ClanCategory(models.Model):
    CATEGORY_CHOICES = (
        ("historical", "Historical Clans"),
        ("political", "Political Clans"),
    )

    name = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, unique=True
    )
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to="clan_categories/", blank=True, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Clan Category"
        verbose_name_plural = "Clan Categories"
        ordering = ["name"]

    def __str__(self):
        return self.get_name_display()

    def get_absolute_url(self):
        return reverse("clan_category_detail", kwargs={"slug": self.slug})


class Clan(models.Model):

    category = models.ForeignKey(
        ClanCategory,
        on_delete=models.CASCADE,
        related_name="clans",
    )

    name = models.CharField(
        max_length=200
    )

    slug = models.SlugField()

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="clans/",
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        verbose_name = "Clan"
        verbose_name_plural = "Clans"
        ordering = ["name"]

        constraints = [
            models.UniqueConstraint(
                fields=["category", "slug"],
                name="unique_clan_slug_per_category"
            )
        ]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "clan_detail",
            kwargs={
                "slug": self.slug
            }
        )

class Ward(models.Model):
    clan = models.ForeignKey(
        Clan, on_delete=models.CASCADE, related_name="wards"
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Ward"
        verbose_name_plural = "Wards"
        ordering = ["name"]
        constraints = [
            models.UniqueConstraint(
                fields=["clan", "slug"], name="unique_ward_slug_per_clan"
            )
        ]

    def __str__(self):
        return f"{self.name} ({self.clan.name})"

    def get_absolute_url(self):
        return reverse(
            "ward_detail",
            kwargs={"clan_slug": self.clan.slug, "slug": self.slug},
        )


class Village(models.Model):

    ward = models.ForeignKey(
        Ward,
        on_delete=models.CASCADE,
        related_name="villages"
    )

    name = models.CharField(max_length=200)

    slug = models.SlugField(
        unique=True
    )

    image = models.ImageField(
        upload_to="villages/",
        blank=True,
        null=True
    )

    # Cultural & Administrative details
    village_head = models.CharField(
        max_length=255,
        blank=True,
        help_text="Name of the Eteidung / Village Head",
    )

    population = models.PositiveIntegerField(
        default=0
    )

    history = models.TextField(
        blank=True
    )

    description = models.TextField(
        blank=True
    )

    # Geo Coordinates
    latitude = models.FloatField(
        blank=True,
        null=True
    )

    longitude = models.FloatField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Village"
        verbose_name_plural = "Villages"
        ordering = ["name"]

    def __str__(self):
        return self.name

    @property
    def clan(self):
        return self.ward.clan if self.ward else None

    def get_absolute_url(self):
        return reverse(
            "village_detail",
            kwargs={
                "ward_slug": self.ward.slug,
                "slug": self.slug,
            }
        )

