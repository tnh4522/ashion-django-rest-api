from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('offers/', views.OfferList.as_view()),
    path('offers/<int:pk>/', views.OfferDetails.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetails.as_view()),
]
