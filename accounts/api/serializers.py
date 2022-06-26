from rest_framework import serializers

# Models
from django.contrib.auth.models import User
from accounts.models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Profile 
        fields = '__all__'
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']