
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BrewMethodForm
from .models import BrewMethod


def method_list(request):
    methods = BrewMethod.objects.all()

    return render(
        request,
        "brewing/method_list.html",
        {"methods": methods},
    )


def method_detail(request, pk):
    method = get_object_or_404(BrewMethod, pk=pk)

    return render(
        request,
        "brewing/method_detail.html",
        {"method": method},
    )


def method_create(request):
    if request.method == "POST":
        form = BrewMethodForm(request.POST)

        if form.is_valid():
            method = form.save()
            messages.success(
                request,
                "Brewing method created successfully.",
            )
            return redirect("brewing:method_detail", pk=method.pk)
    else:
        form = BrewMethodForm()

    return render(
        request,
        "brewing/method_form.html",
        {"form": form, "page_title": "Add a brewing method"},
    )


def method_update(request, pk):
    method = get_object_or_404(BrewMethod, pk=pk)

    if request.method == "POST":
        form = BrewMethodForm(request.POST, instance=method)

        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Brewing method updated successfully.",
            )
            return redirect("brewing:method_detail", pk=method.pk)
    else:
        form = BrewMethodForm(instance=method)

    return render(
        request,
        "brewing/method_form.html",
        {"form": form, "page_title": "Edit a brewing method"},
    )


def method_delete(request, pk):
    method = get_object_or_404(BrewMethod, pk=pk)

    if request.method == "POST":
        method.delete()
        messages.success(
            request,
            "Brewing method deleted successfully.",
        )
        return redirect("brewing:method_list")

    return render(
        request,
        "brewing/method_confirm_delete.html",
        {"method": method},
    )
