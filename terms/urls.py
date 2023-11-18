from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="term"),
    path("<int:year>/", views.list, name="year_terms"),
    path("<int:year>/<str:season>/", views.term_view, name="term_detail"),
    path("<int:year>/<str:season>/<int:week>/", views.week_view, name="week_detail")
]