from django.db import models

# Create your models here.

class contactus(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=25,null=True)
    message=models.TextField(null=True)

    def __str__(self):
        return self.name

class sliger(models.Model):
    headlines=models.TextField(null=True)
    slider_dec=models.TextField(null=True)
    slider_picture=models.ImageField(upload_to='static/slider',null=True)
    def __str__(self):
        return self.headlines



class newbatches(models.Model):
    name=models.CharField(max_length=100,null=True)
    batchpic=models.ImageField(upload_to='static/newbatches', null=True)
    starting_date=models.DateTimeField(null=True)

class latestbatches(models.Model):
    bname=models.CharField(max_length=100,null=True)
    batchpic=models.ImageField(upload_to='static/latestbatches', null=True)
    starting_date=models.DateTimeField(null=True)
    more=models.TextField(null=True)


# Table to filter placement records by college name....................
class college(models.Model):
    college_name=models.CharField(max_length=200,null=True)
    college_picture=models.ImageField(upload_to='static/college',null=True)
    def __str__ (self):
        return self.college_name


class session_year(models.Model):
    session=models.CharField(max_length=100,null=True)
    def __str__ (self):
        return self.session


class batch(models.Model):
    batch_name=models.CharField(max_length=50,null=True)
    def __str__(self):
        return self.batch_name


class placement(models.Model):
    student_picture=models.ImageField(upload_to='static/placement',null=True)
    student_name=models.CharField(max_length=100,null=True)
    session=models.ForeignKey(session_year,on_delete=models.CASCADE,null=True)
    batch=models.ForeignKey(batch,on_delete=models.CASCADE,null=True)
    college=models.ForeignKey(college,on_delete=models.CASCADE,null=True)
    company_name=models.CharField(max_length=200,null=True)
    company_picture=models.ImageField(upload_to='static/company',null=True)

class studentbatch(models.Model):
    batch_name=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.batch_name


class signup(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,primary_key=True)
    mobile=models.CharField(max_length=30,null=True)
    profile=models.ImageField(upload_to='static/profile',null=True)
    course=models.CharField(max_length=30,null=True)
    pyear=models.CharField(max_length=30,null=True)
    college=models.CharField(max_length=200,null=True)
    batch=models.ForeignKey(studentbatch,on_delete=models.CASCADE,null=True)
    status=models.CharField(max_length=30,null=True)
    passwd=models.CharField(max_length=100,null=True)
    batchid=models.ImageField(null=True)
    def __str__(self):
        return self.name


class ourinsrtuctors(models.Model):
    name=models.CharField(max_length=100,null=True)
    profile_pic=models.ImageField(upload_to='static/ourinstructors',null=True)
    qualification=models.CharField(max_length=50,null=True)
    company_pic=models.ImageField(upload_to='static/instructorCompanyPic',null=True)
    subject=models.CharField(max_length=100,null=True)

class ufeedback(models.Model):
    uname=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=300,null=True)
    college=models.CharField(max_length=200,null=True)
    message=models.TextField(null=True)
    profile=models.ImageField(upload_to='static/feedbackpic',null=True)

    # From Student models
class category(models.Model):
    category_name=models.CharField(max_length=200,null=True)
    category_picture=models.ImageField(upload_to='static/category',null=True)
    category_date=models.DateField(null=True)
    def __str__(self):
        return self.category_name


class mylectures(models.Model):
    video_category=models.ForeignKey(category,on_delete=models.CASCADE,null=True)
    video_batch=models.ForeignKey(studentbatch,on_delete=models.CASCADE,null=True)
    vlink=models.CharField(max_length=300,null=True)
    thumbnail=models.ImageField(upload_to='static/video',null=True)
    video_description=models.TextField(null=True)
    added_date=models.DateField(null=True)

class batchtiming(models.Model):
    batch=models.ForeignKey(studentbatch,on_delete=models.CASCADE,null=True)
    clink=models.CharField(max_length=300,null=True)
    timing=models.CharField(max_length=50,null=True)
    start_date=models.DateField(null=True)

class enotes(models.Model):
    title=models.CharField(max_length=200,null=True)
    notes_pic=models.ImageField(upload_to='static/enotespic',null=True)
    pdf_notes=models.FileField(upload_to='static/enotespdf',null=True)
    batch=models.ForeignKey(studentbatch,on_delete=models.CASCADE,null=True)
    added_date=models.DateField(null=True)

    # Task tables



class  mytask(models.Model):
    taskbatch=models.ForeignKey(studentbatch,on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=200,null=True)
    task_file=models.FileField(upload_to='static/task',null=True)
    added_date=models.DateField(null=True)

class submittedtask(models.Model):
    title=models.CharField(max_length=200,null=True)
    answer_file=models.FileField(upload_to='static/submittedtask',null=True)
    tid=models.CharField(max_length=100,null=True)
    userid=models.CharField(max_length=200,null=True)
    marks=models.CharField(max_length=200,null=True)


        