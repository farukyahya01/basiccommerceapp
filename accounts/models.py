from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.

class Profile(models.Model):

    class StatusChoices(models.TextChoices):
        ACTIVE = 'active', _('AKTİF')
        PASSIVE = 'passive', _('PASİF')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='profile_photo/%Y/%m/')
    UserCity = models.CharField(max_length=50, null=True, blank=True)
    UserState = models.CharField(max_length=50,null=True, blank=True)
    UserPhone = models.CharField(max_length=11, null=True, blank=True)
    UserAdress = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.ACTIVE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = 'Profiller'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            if img.height > 600 or img.width > 600:
                output_size = (600,600)
                img.thumbnail(output_size)
                img.save(self.photo.path)


