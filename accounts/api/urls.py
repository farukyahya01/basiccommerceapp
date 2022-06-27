from django.contrib import admin
from django.urls import path, include
from accounts.api.views import ProfileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
