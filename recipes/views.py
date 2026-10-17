
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecipeForm
from .models import Recipe


def recipe_list(request):
    recipes = Recipe.objects.select_related(
        "coffee",
        "brew_method",
    ).prefetch_related("flavors")

    return render(
        request,
        "recipes/recipe_list.html",
        {"recipes": recipes},
    )


def recipe_detail(request, pk):
    recipe = get_object_or_404(
        Recipe.objects.select_related(
            "coffee",
            "brew_method",
        ).prefetch_related("flavors"),
        pk=pk,
    )

    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe},
    )


def recipe_create(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)

        if form.is_valid():
            recipe = form.save()
            messages.success(
                request,
                "Recipe created successfully.",
            )
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeForm()

    return render(
        request,
        "recipes/recipe_form.html",
        {"form": form, "page_title": "Create a recipe"},
    )


def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Recipe updated successfully.",
            )
            return redirect(recipe.get_absolute_url())
    else:
        form = RecipeForm(instance=recipe)

    return render(
        request,
        "recipes/recipe_form.html",
        {"form": form, "page_title": "Edit a recipe"},
    )


def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        recipe.delete()
        messages.success(
            request,
            "Recipe deleted successfully.",
        )
        return redirect("recipes:recipe_list")

    return render(
        request,
        "recipes/recipe_confirm_delete.html",
        {"recipe": recipe},
    )
