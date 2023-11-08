# Generated by Django 4.2.3 on 2023-11-05 06:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0003_alter_category_category_id_alter_post_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_id',
            field=models.UUIDField(default=uuid.UUID('08242c70-09a1-4870-b28a-647127c5641a'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.UUIDField(default=uuid.UUID('8c70ee70-2507-4db8-876e-08246b4918b0'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]