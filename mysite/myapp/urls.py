from django.urls import path
from django.contrib.auth import views as adminviews
from . import views


urlpatterns = [
    path('', views.index),
    path('page/<int:year>/<int:num>/', views.page),
    path('suggestions/', views.rest_suggestion),
    path('comment/<int:suggestion_id>/', views.comment_view),
    path('register/', views.register),
    path('login/', adminviews.LoginView.as_view()),
    path('logout/', views.logout_view),
]
