from django.contrib import admin
from django.urls import path, include
from accounts.api import views as api_views

urlpatterns = [
    path('profile/', api_views.ProfileListView.as_view(), name='profile'),
    path('profile/detail/<int:pk>', api_views.ProfileDetailView.as_view(), name='profile_detail'),
]
