from django.urls import path
from . import views

urlpatterns = [
    # path with no additional argument and visit views.py -> function index, name for this path for easier reference later
    path("", views.index, name="index"),
    path("daniel", views.daniel, name="daniel")
]
