# Generated by Django 3.2.4 on 2023-09-19 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_batchtiming_mylectures_studentbatch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mylectures',
            name='video_batch',
        ),
        migrations.RemoveField(
            model_name='mylectures',
            name='video_category',
        ),
        migrations.DeleteModel(
            name='batchtiming',
        ),
        migrations.DeleteModel(
            name='mylectures',
        ),
        migrations.DeleteModel(
            name='studentbatch',
        ),
    ]
