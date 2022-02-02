# Generated by Django 4.0.2 on 2022-02-02 20:25

import os

from django.contrib.auth import get_user_model
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    def generate_superuser(apps, schema_editor):

        superuser = get_user_model().objects.create_superuser(
            username=os.environ.get("SWEETHOME_USER"),
            password=os.environ.get("SWEETHOME_PASSWORD")
        )
        superuser.is_active = True
        superuser.save()

    operations = [
        migrations.RunPython(generate_superuser),
    ]
