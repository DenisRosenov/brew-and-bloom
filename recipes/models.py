
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

from catalog.models import Coffee, FlavorTag
from brewing.models import BrewMethod


class Recipe(models.Model):
    title = models.CharField(
        max_length=120,
        unique=True,
        verbose_name="Recipe title",
        help_text="Give your coffee recipe a descriptive name.",
        error_messages={
            "unique": "A recipe with this title already exists.",
            "blank": "Please enter a recipe title.",
        },
    )
    coffee = models.ForeignKey(
        Coffee,
        on_delete=models.PROTECT,
        related_name="recipes",
        verbose_name="Coffee",
        help_text="Choose the coffee used in this recipe.",
    )
    brew_method = models.ForeignKey(
        BrewMethod,
        on_delete=models.PROTECT,
        related_name="recipes",
        verbose_name="Brewing method",
        help_text="Choose the preparation method.",
    )
    flavors = models.ManyToManyField(
        FlavorTag,
        related_name="recipes",
        blank=True,
        verbose_name="Flavor characteristics",
        help_text="Select one or more flavor notes.",
    )
    ingredients = models.TextField(
        verbose_name="Ingredients",
        help_text="List the ingredients and their quantities.",
    )
    instructions = models.TextField(
        verbose_name="Preparation instructions",
        help_text="Explain the preparation step by step.",
    )
    preparation_time = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(1, "Preparation time must be at least one minute."),
            MaxValueValidator(180, "Preparation time cannot exceed 180 minutes."),
        ],
        verbose_name="Preparation time (minutes)",
    )
    rating = models.PositiveSmallIntegerField(
        default=5,
        validators=[
            MinValueValidator(1, "Rating must be at least 1."),
            MaxValueValidator(5, "Rating cannot exceed 5."),
        ],
        verbose_name="Rating (1–5)",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at", "title"]
        verbose_name = "Recipe"
        verbose_name_plural = "Recipes"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("recipes:recipe_detail", kwargs={"pk": self.pk})

    def clean(self):
        super().clean()

        if self.title:
            self.title = self.title.strip()

        if self.ingredients:
            self.ingredients = self.ingredients.strip()

        if self.instructions:
            self.instructions = self.instructions.strip()
