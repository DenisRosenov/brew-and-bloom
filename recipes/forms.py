
from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            "title",
            "coffee",
            "brew_method",
            "flavors",
            "ingredients",
            "instructions",
            "preparation_time",
            "rating",
        ]
        labels = {
            "title": "Recipe title",
            "coffee": "Coffee",
            "brew_method": "Brewing method",
            "flavors": "Flavor characteristics",
            "ingredients": "Ingredients",
            "instructions": "Preparation instructions",
            "preparation_time": "Preparation time (minutes)",
            "rating": "Rating (1–5)",
        }
        help_texts = {
            "title": "Give your recipe a descriptive name.",
            "coffee": "Select the coffee used in this recipe.",
            "brew_method": "Choose how the coffee will be prepared.",
            "flavors": "Select any flavors that describe this recipe.",
            "ingredients": "List all ingredients and quantities.",
            "instructions": "Describe the preparation step by step.",
            "preparation_time": "Enter a value between 1 and 180 minutes.",
            "rating": "Choose a rating from 1 to 5.",
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. Vanilla Iced Latte",
                }
            ),
            "coffee": forms.Select(
                attrs={"class": "form-select"}
            ),
            "brew_method": forms.Select(
                attrs={"class": "form-select"}
            ),
            "flavors": forms.SelectMultiple(
                attrs={
                    "class": "form-select",
                    "size": "4",
                }
            ),
            "ingredients": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Milk, coffee, vanilla syrup...",
                }
            ),
            "instructions": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 6,
                    "placeholder": "1. Prepare the coffee...",
                }
            ),
            "preparation_time": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1",
                    "max": "180",
                }
            ),
            "rating": forms.Select(
                choices=[
                    (1, "1 — Needs improvement"),
                    (2, "2 — Fair"),
                    (3, "3 — Good"),
                    (4, "4 — Very good"),
                    (5, "5 — Excellent"),
                ],
                attrs={"class": "form-select"},
            ),
        }

    def clean_title(self):
        title = self.cleaned_data["title"].strip()

        if len(title) < 3:
            raise forms.ValidationError(
                "The recipe title must contain at least 3 characters."
            )

        return title

    def clean_ingredients(self):
        ingredients = self.cleaned_data["ingredients"].strip()

        if len(ingredients) < 5:
            raise forms.ValidationError(
                "Please provide a more detailed list of ingredients."
            )

        return ingredients

    def clean_instructions(self):
        instructions = self.cleaned_data["instructions"].strip()

        if len(instructions) < 10:
            raise forms.ValidationError(
                "Please provide more detailed preparation instructions."
            )

        return instructions
