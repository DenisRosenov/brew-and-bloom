
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class BrewMethod(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True,
        verbose_name="Method name",
        help_text="For example, Espresso, French Press, or V60.",
        error_messages={
            "unique": "A brewing method with this name already exists.",
            "blank": "Please enter a method name.",
        },
    )
    description = models.TextField(
        verbose_name="Description",
        help_text="Explain how this brewing method works.",
    )
    recommended_temperature = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, "Temperature must be above zero."),
            MaxValueValidator(100, "Temperature cannot exceed 100°C."),
        ],
        verbose_name="Recommended water temperature (°C)",
    )
    recommended_brew_time = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, "Brew time must be at least one second."),
            MaxValueValidator(3600, "Brew time cannot exceed one hour."),
        ],
        verbose_name="Recommended brew time (seconds)",
        help_text="Enter the brewing time in seconds.",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Brewing method"
        verbose_name_plural = "Brewing methods"

    def __str__(self):
        return self.name

    def clean(self):
        super().clean()

        if self.name:
            self.name = self.name.strip()

        if self.description:
            self.description = self.description.strip()
