# Generated by Django 3.2.4 on 2023-09-21 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200, null=True)),
                ('category_picture', models.ImageField(null=True, upload_to='static/category')),
                ('category_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='college',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=200, null=True)),
                ('college_picture', models.ImageField(null=True, upload_to='static/college')),
            ],
        ),
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('mobile', models.CharField(max_length=25, null=True)),
                ('message', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='latestbatches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bname', models.CharField(max_length=100, null=True)),
                ('batchpic', models.ImageField(null=True, upload_to='static/latestbatches')),
                ('starting_date', models.DateTimeField(null=True)),
                ('more', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='newbatches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('batchpic', models.ImageField(null=True, upload_to='static/newbatches')),
                ('starting_date', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ourinsrtuctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('profile_pic', models.ImageField(null=True, upload_to='static/ourinstructors')),
                ('qualification', models.CharField(max_length=50, null=True)),
                ('company_pic', models.ImageField(null=True, upload_to='static/instructorCompanyPic')),
                ('subject', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='session_year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sliger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headlines', models.TextField(null=True)),
                ('slider_dec', models.TextField(null=True)),
                ('slider_picture', models.ImageField(null=True, upload_to='static/slider')),
            ],
        ),
        migrations.CreateModel(
            name='studentbatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('mobile', models.CharField(max_length=30, null=True)),
                ('profile', models.ImageField(null=True, upload_to='static/profile')),
                ('course', models.CharField(max_length=30, null=True)),
                ('pyear', models.CharField(max_length=30, null=True)),
                ('college', models.CharField(max_length=200, null=True)),
                ('status', models.CharField(max_length=30, null=True)),
                ('passwd', models.CharField(max_length=100, null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.studentbatch')),
            ],
        ),
        migrations.CreateModel(
            name='placement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_picture', models.ImageField(null=True, upload_to='static/placement')),
                ('student_name', models.CharField(max_length=100, null=True)),
                ('company_name', models.CharField(max_length=200, null=True)),
                ('company_picture', models.ImageField(null=True, upload_to='static/company')),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.batch')),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.college')),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.session_year')),
            ],
        ),
        migrations.CreateModel(
            name='mylectures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vlink', models.CharField(max_length=300, null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='static/video')),
                ('video_description', models.TextField(null=True)),
                ('added_date', models.DateField(null=True)),
                ('video_batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.studentbatch')),
                ('video_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.category')),
            ],
        ),
        migrations.CreateModel(
            name='batchtiming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clink', models.CharField(max_length=300, null=True)),
                ('timing', models.CharField(max_length=50, null=True)),
                ('start_date', models.DateField(null=True)),
                ('batch', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.studentbatch')),
            ],
        ),
    ]
