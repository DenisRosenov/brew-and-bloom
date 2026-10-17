
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Coffee(models.Model):
    class RoastLevel(models.TextChoices):
        LIGHT = "light", "Light"
        MEDIUM = "medium", "Medium"
        DARK = "dark", "Dark"

    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name="Coffee name",
        help_text="Enter a unique name for this coffee.",
        error_messages={
            "unique": "A coffee with this name already exists.",
            "blank": "Please enter a coffee name.",
        },
    )
    origin = models.CharField(
        max_length=100,
        verbose_name="Country of origin",
        help_text="For example, Ethiopia or Colombia.",
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Describe the coffee's flavor and character.",
    )
    roast_level = models.CharField(
        max_length=10,
        choices=RoastLevel.choices,
        default=RoastLevel.MEDIUM,
        verbose_name="Roast level",
    )
    price_per_kg = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        validators=[
            MinValueValidator(0.01, "Price must be greater than zero."),
            MaxValueValidator(99999.99, "Price is too high."),
        ],
        verbose_name="Price per kilogram",
        help_text="Enter the price in your local currency.",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Coffee"
        verbose_name_plural = "Coffees"

    def __str__(self):
        return f"{self.name} ({self.origin})"

    def get_absolute_url(self):
        return reverse("catalog:coffee_detail", kwargs={"pk": self.pk})

    def clean(self):
        super().clean()

        if self.name:
            self.name = self.name.strip()

        if self.origin:
            self.origin = self.origin.strip()

        if self.description:
            self.description = self.description.strip()

class FlavorTag(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name="Flavor name",
        help_text="For example, chocolate, caramel, or citrus.",
        error_messages={
            "unique": "This flavor tag already exists.",
            "blank": "Please enter a flavor name.",
        },
    )
    description = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Description",
        help_text="Optional short description of this flavor.",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Flavor tag"
        verbose_name_plural = "Flavor tags"

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

        if self.name:
            self.name = self.name.strip()

        if self.description:
            self.description = self.description.strip()
