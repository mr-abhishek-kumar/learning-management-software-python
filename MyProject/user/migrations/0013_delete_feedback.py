# Generated by Django 3.2.4 on 2023-09-23 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_rename_name_feedback_uname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='feedback',
        ),
    ]
