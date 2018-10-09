from django.urls import path

from . import views
from django.contrib.auth import views as adminviews

urlpatterns = [
    path('', views.index),
    path('page/<int:year>/<int:num>/', views.page),
    path('suggestions/', views.rest_suggestion),
    path('register/', views.register),
    path('login/', adminviews.LoginView.as_view()),
]
