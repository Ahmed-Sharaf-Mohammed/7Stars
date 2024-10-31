# Generated by Django 4.1.7 on 2024-10-31 01:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='user.png', upload_to=profiles.models.image_upload, verbose_name='Profile Image')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Slug')),
                ('email', models.EmailField(blank=True, default='', max_length=50, verbose_name='Email')),
                ('phone_number', models.CharField(blank=True, default='', max_length=15, verbose_name='Phone Number')),
                ('city', models.CharField(blank=True, default='', max_length=30, verbose_name='City')),
                ('gender', models.CharField(blank=True, default='', max_length=15, verbose_name='Gender')),
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('file', models.FileField(blank=True, default='none', max_length=40, upload_to=profiles.models.user_directory_path, verbose_name='File')),
                ('course', models.CharField(blank=True, max_length=50, null=True, verbose_name='Certification')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]