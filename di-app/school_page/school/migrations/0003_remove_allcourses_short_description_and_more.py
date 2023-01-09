# Generated by Django 4.0.6 on 2022-09-16 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_allcourses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allcourses',
            name='short_description',
        ),
        migrations.AddField(
            model_name='allcourses',
            name='description',
            field=models.TextField(blank=True, verbose_name='Описание'),
        ),
    ]