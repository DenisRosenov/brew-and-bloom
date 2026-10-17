
from django import forms

from .models import Coffee, FlavorTag


class CoffeeForm(forms.ModelForm):
    form_notice = forms.CharField(
        label="Information",
        initial="Please provide accurate information about this coffee.",
        required=False,
        disabled=True,
    )

    class Meta:
        model = Coffee
        fields = [
            "name",
            "origin",
            "description",
            "roast_level",
            "price_per_kg",
        ]
        labels = {
            "name": "Coffee name",
            "origin": "Country of origin",
            "description": "About this coffee",
            "roast_level": "Roast level",
            "price_per_kg": "Price per kilogram",
        }
        help_texts = {
            "name": "Use a unique name.",
            "origin": "Enter the country where the coffee originates.",
            "description": "Describe the flavor and character.",
            "price_per_kg": "Enter a positive price.",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g. Ethiopian Yirgacheffe"}
            ),
            "origin": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g. Ethiopia"}
            ),
            "description": forms.Textarea(
                attrs={"class": "form-control", "rows": 4, "placeholder": "Describe the coffee..."}
            ),
            "roast_level": forms.Select(
                attrs={"class": "form-select"}
            ),
            "price_per_kg": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "e.g. 24.50", "step": "0.01", "min": "0.01"}
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                "The coffee name must contain at least 2 characters."
            )

        return name

    def clean_origin(self):
        origin = self.cleaned_data["origin"].strip()

        if len(origin) < 2:
            raise forms.ValidationError(
                "Please enter a valid country of origin."
            )

        return origin


class FlavorTagForm(forms.ModelForm):
    class Meta:
        model = FlavorTag
        fields = ["name", "description"]
        labels = {
            "name": "Flavor name",
            "description": "Description",
        }
        help_texts = {
            "name": "Enter a short, unique flavor name.",
            "description": "Optionally describe this flavor.",
        }
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "e.g. Chocolate"}
            ),
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "A short flavor description"}
            ),
        }

    def clean_name(self):
        name = self.cleaned_data["name"].strip()

        if len(name) < 2:
            raise forms.ValidationError(
                "The flavor name must contain at least 2 characters."
            )

        return name
