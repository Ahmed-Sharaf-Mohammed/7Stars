from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
import os
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


def image_upload(instance, filename):
    name, extension = os.path.splitext(filename)
    return f"profile/{instance.id}/{extension}"


def user_directory_path(instance, filename):
    return f'user_{instance.user.id}/{filename}'


class Profile(models.Model):
    image = models.ImageField(default='user.png', upload_to=image_upload, verbose_name=_("Profile Image"))
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_("User"))
    slug = models.SlugField(null=True, blank=True, verbose_name=_("Slug"))
    email = models.EmailField(max_length=50, default='', blank=True, verbose_name=_("Email"))
    phone_number = models.CharField(max_length=15, default='', blank=True, verbose_name=_("Phone Number"))
    city = models.CharField(max_length=30, default='', blank=True, verbose_name=_("City"))
    gender = models.CharField(max_length=15, default='', blank=True, verbose_name=_("Gender"))
    dob = models.DateField(blank=True, null=True, verbose_name=_("Date of Birth"))
    file = models.FileField(upload_to=user_directory_path, max_length=40, default='none', blank=True, verbose_name=_("File"))
    course = models.CharField(max_length=50, blank=True, null=True, verbose_name=_("Certification"))

    def __str__(self):
        return str(self.user)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        try:
            user_profile = Profile.objects.create(user=kwargs['instance'])
        except Exception as e:
            print(f"Error saving profile: {str(e)}")


post_save.connect(create_profile, sender=User)
