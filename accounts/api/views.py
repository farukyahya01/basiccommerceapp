from django.shortcuts import render, redirect
from requests import request

# DRF
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from accounts.api.serializers import ProfileSerializer
# Models
from django.contrib.auth.models import User
from accounts.models import Profile
# Permissions
from rest_framework import permissions
from accounts.api.permissions import IsProfileRecordOwner
from rest_framework.authentication import TokenAuthentication

class ProfileListView(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminUser]

    # def get_queryset(self):
    #     return Profile.objects.filter(user=self.request.user.id)
    

class ProfileDetailView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsProfileRecordOwner]
