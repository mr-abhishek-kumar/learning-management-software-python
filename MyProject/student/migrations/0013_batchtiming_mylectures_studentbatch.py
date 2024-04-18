# Generated by Django 3.2.4 on 2023-09-19 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_auto_20230919_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentbatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='mylectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlink', models.CharField(max_length=300, null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='static/video')),
                ('video_description', models.TextField(null=True)),
                ('added_date', models.DateField()),
                ('video_batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.studentbatch')),
                ('video_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.category')),
            ],
        ),
        migrations.CreateModel(
            name='batchtiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clink', models.CharField(max_length=300, null=True)),
                ('timing', models.CharField(max_length=50, null=True)),
                ('start_date', models.DateField()),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='student.studentbatch')),
            ],
        ),
    ]
