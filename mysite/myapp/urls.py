from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('page/<int:year>/<int:num>/', views.page),
]
