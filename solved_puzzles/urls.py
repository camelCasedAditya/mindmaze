from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="solved"),
    path("<int:puzzle_id>/", views.detail, name="solved_detail")
]