# Generated by Django 3.1.1 on 2020-09-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_processing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='email',
            field=models.CharField(default='null', max_length=50),
        ),
    ]