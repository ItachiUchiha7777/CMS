# Generated by Django 4.2.3 on 2023-11-05 06:30

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_userprofile_about_alter_userprofile_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_id',
            field=models.UUIDField(default=uuid.UUID('fc699a3f-47ab-427f-a9e0-7695431687f4'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]
