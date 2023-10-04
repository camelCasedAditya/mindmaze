from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="puzzle"),
    path("<int:puzzle_id_detail>/", views.detail, name="detail"),
]