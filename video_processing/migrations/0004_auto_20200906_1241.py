# Generated by Django 3.1.1 on 2020-09-06 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_processing', '0003_auto_20200906_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]