
from django.urls import path

from . import views

app_name = "brewing"

urlpatterns = [
    path("methods/", views.method_list, name="method_list"),
    path("methods/add/", views.method_create, name="method_create"),
    path("methods/<int:pk>/", views.method_detail, name="method_detail"),
    path("methods/<int:pk>/edit/", views.method_update, name="method_update"),
    path("methods/<int:pk>/delete/", views.method_delete, name="method_delete"),
]
