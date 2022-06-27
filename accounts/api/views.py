from django.shortcuts import render, redirect
from requests import request

# DRF
from rest_framework import generics, status, mixins
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
# from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.viewsets import GenericViewSet
from accounts.api.serializers import ProfileSerializer

# Models
from django.contrib.auth.models import User
from accounts.models import Profile
# Permissions
from rest_framework import permissions
from accounts.api.permissions import IsProfileRecordOwner
from rest_framework.authentication import TokenAuthentication

class ProfileViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated, IsProfileRecordOwner]

    # def get_queryset(self):
    #     return 
    

# class ProfileDetailView(generics.RetrieveUpdateAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     permission_classes = [permissions.IsAuthenticated, IsProfileRecordOwner]
