# Generated by Django 4.2.3 on 2023-11-01 14:11

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('cmsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('category_id', models.UUIDField(default=uuid.UUID('191fbe2a-0ee4-40fd-a348-c5615be6c10d'), editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='post_id',
            field=models.UUIDField(default=uuid.UUID('f670a742-7fa8-4e28-beff-a4f9ef427286'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cmsapp.category'),
        ),
    ]
