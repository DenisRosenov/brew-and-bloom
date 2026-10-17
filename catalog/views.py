
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CoffeeForm, FlavorTagForm
from .models import Coffee, FlavorTag


def coffee_list(request):
    coffees = Coffee.objects.all()

    return render(
        request,
        "catalog/coffee_list.html",
        {"coffees": coffees},
    )


def coffee_detail(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)

    return render(
        request,
        "catalog/coffee_detail.html",
        {"coffee": coffee},
    )


def coffee_create(request):
    if request.method == "POST":
        form = CoffeeForm(request.POST)

        if form.is_valid():
            coffee = form.save()
            messages.success(request, "Coffee created successfully.")
            return redirect(coffee.get_absolute_url())
    else:
        form = CoffeeForm()

    return render(
        request,
        "catalog/coffee_form.html",
        {"form": form, "page_title": "Add a coffee"},
    )


def coffee_update(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)

    if request.method == "POST":
        form = CoffeeForm(request.POST, instance=coffee)

        if form.is_valid():
            form.save()
            messages.success(request, "Coffee updated successfully.")
            return redirect(coffee.get_absolute_url())
    else:
        form = CoffeeForm(instance=coffee)

    return render(
        request,
        "catalog/coffee_form.html",
        {"form": form, "page_title": "Edit coffee"},
    )


def coffee_delete(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)

    if request.method == "POST":
        coffee.delete()
        messages.success(request, "Coffee deleted successfully.")
        return redirect("catalog:coffee_list")

    return render(
        request,
        "catalog/coffee_confirm_delete.html",
        {"coffee": coffee},
    )


def flavor_list(request):
    flavors = FlavorTag.objects.all()

    return render(
        request,
        "catalog/flavor_list.html",
        {"flavors": flavors},
    )


def flavor_create(request):
    if request.method == "POST":
        form = FlavorTagForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Flavor tag created successfully.")
            return redirect("catalog:flavor_list")
    else:
        form = FlavorTagForm()

    return render(
        request,
        "catalog/flavor_form.html",
        {"form": form, "page_title": "Add a flavor"},
    )


def flavor_update(request, pk):
    flavor = get_object_or_404(FlavorTag, pk=pk)

    if request.method == "POST":
        form = FlavorTagForm(request.POST, instance=flavor)

        if form.is_valid():
            form.save()
            messages.success(request, "Flavor tag updated successfully.")
            return redirect("catalog:flavor_list")
    else:
        form = FlavorTagForm(instance=flavor)

    return render(
        request,
        "catalog/flavor_form.html",
        {"form": form, "page_title": "Edit a flavor"},
    )


def flavor_delete(request, pk):
    flavor = get_object_or_404(FlavorTag, pk=pk)

    if request.method == "POST":
        flavor.delete()
        messages.success(request, "Flavor tag deleted successfully.")
        return redirect("catalog:flavor_list")

    return render(
        request,
        "catalog/flavor_confirm_delete.html",
        {"flavor": flavor},
    )

