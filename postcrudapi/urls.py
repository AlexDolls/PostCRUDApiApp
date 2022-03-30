from django.urls import path

from . import views



app_name = "postcrud_api"

urlpatterns = [
        path("", views.index, name="index"),
        ]

