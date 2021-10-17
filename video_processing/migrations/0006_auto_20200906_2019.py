# Generated by Django 3.1.1 on 2020-09-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_processing', '0005_video_percentage_compression'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videogray',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
        migrations.RenameModel(
            old_name='Video',
            new_name='Videocompress',
        ),
    ]