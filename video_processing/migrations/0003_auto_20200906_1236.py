# Generated by Django 3.1.1 on 2020-09-06 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_processing', '0002_video_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]