
from django import forms

from .models import BrewMethod


class BrewMethodForm(forms.ModelForm):
    class Meta:
        model = BrewMethod
        fields = [
            "name",
            "description",
            "recommended_temperature",
            "recommended_brew_time",
        ]
        labels = {
            "name": "Method name",
            "description": "Description",
            "recommended_temperature": "Water temperature (°C)",
            "recommended_brew_time": "Brewing time (seconds)",
        }
        help_texts = {
            "name": "For example, French Press or V60.",
            "description": "Explain how this brewing method works.",
            "recommended_temperature": "Enter a temperature between 1 and 100°C.",
            "recommended_brew_time": "Enter the brewing time in seconds.",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "e.g. French Press",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Describe the brewing method...",
                }
            ),
            "recommended_temperature": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1",
                    "max": "100",
                }
            ),
            "recommended_brew_time": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "min": "1",
                    "max": "3600",
                }
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                "The method name must contain at least 2 characters."
            )

        return name
