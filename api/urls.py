from django.urls import path

from . import views

urlpatterns = [
    path('news', views.News.as_view()),
    path('search/', views.SearchDay.as_view()),
    path('migration/', views.migration),
]
