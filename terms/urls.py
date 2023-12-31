from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="term"),
    path("<int:year>/<str:season>/", views.term_view, name="term_detail"),
    path("<int:year>/<str:season>/<int:week>/", views.week_view, name="week_detail"),
    path("class/", views.class_view, name="class"),
    path("stats/", views.my_stats, name="stats"),
    path("stats/<str:username>/", views.user_stats, name="user_stats")
]