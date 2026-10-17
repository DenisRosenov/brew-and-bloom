
from django.urls import path

from . import views

app_name = "catalog"

urlpatterns = [
    path("coffees/", views.coffee_list, name="coffee_list"),
    path("coffees/add/", views.coffee_create, name="coffee_create"),
    path("coffees/<int:pk>/", views.coffee_detail, name="coffee_detail"),
    path("coffees/<int:pk>/edit/", views.coffee_update, name="coffee_update"),
    path("coffees/<int:pk>/delete/", views.coffee_delete, name="coffee_delete"),

    path("flavors/", views.flavor_list, name="flavor_list"),
    path("flavors/add/", views.flavor_create, name="flavor_create"),
    path("flavors/<int:pk>/edit/", views.flavor_update, name="flavor_update"),
    path("flavors/<int:pk>/delete/", views.flavor_delete, name="flavor_delete"),
]
