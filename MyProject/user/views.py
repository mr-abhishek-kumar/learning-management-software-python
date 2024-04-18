from django.shortcuts import render
from django.http import HttpResponse

from .models import *
from student.models import *

# Create your views here.

def index(request):
    sdata=sliger.objects.all()[0:3]
    ourinsdata=ourinsrtuctors.objects.all()
    nbdata=newbatches.objects.all().order_by('-id')[0:3]
    lbdata=latestbatches.objects.all()
    mydict={"sd":sdata,"nbd":nbdata,"teachd":ourinsdata,"lbd":lbdata}

    return render(request,'user/index.html',mydict)


def aboutus(request):
    return render(request,'user/aboutus.html')

def contact(request):
    
    if request.method=="POST":
        a=request.POST.get('name')
        b=request.POST.get('email')
        d=request.POST.get('msg')
        c=request.POST.get('number')
        contactus(name=a,email=b,mobile=c,message=d).save()
        return HttpResponse("<script> alert('Thanks for contacting with us....');location.href='/user/contactus/' </script>")

    return render(request,'user/contactus.html')

def feedback(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        clg=request.POST.get('clg')
        msg=request.POST.get('msg')
        city=request.POST.get('city')
        ufeedback(uname=uname,college=clg,message=msg,city=city).save()
        return HttpResponse(" <script> alert('Thanks for contacting us..!'); location.href='/user/feedback/' </script> ")

    return render(request,'user/feedback.html')

def registration(request):
    bdata=studentbatch.objects.all()
    md={"bdata":bdata}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        college=request.POST.get('college')
        course=request.POST.get('course')
        picture=request.FILES['fu']
        pyear=request.POST.get('pyear')
        batch=request.POST.get('batch')

        x=signup.objects.filter(email=email).count()
        if x==0:
            signup(name=name,email=email,mobile=mobile,college=college,course=course,profile=picture,pyear=pyear,passwd=passwd,status='Pending',batchid=batch).save()
            return HttpResponse(" <script>alert('You are Successfully registered....');location.href='/user/signup'</script> ")
        else:
            return HttpResponse(" <script>alert('You are already registered..');location.href='/user/signup'</script> ")

    return render(request,'user/registration.html',md)

# ....................in .py file...........................
#  set Session
# request.session['sessionName]=value
# ex:
# request.session['userid']=email
# request.session['username']=name

# Get session
# request.session.get('sessionName')
# request.session.get('useid')....................rs@gmaol.com
# request.session.get('userName')....................Abhi

# ....................on .html file...........................
# Get Session
# request.session.sessionName
# {{request.session.userid}}
# {{request.session.username}}

# ....................Deletion of session...........................
# del request.session['sessionName']
# del request.session['userid']


def signin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwd=request.POST.get('paswd')
        x=signup.objects.filter(email=email,passwd=passwd,).count()
        if x==1:
            request.session['user']=email
            y=signup.objects.filter(email=email,passwd=passwd)      #1 row
            request.session['userpic']=str(y[0].profile)
            request.session['username']=str(y[0].name)
            request.session['batchid']=str(y[0].batchid)

            return HttpResponse(" <script>location.href='/student/index' </script> ")
        else:
            return HttpResponse(" <script> alert('Your Id or Password is incorrect.!');location.href='/user/signin' </script> ")

    return render(request,'user/login.html')



def mynewbatches(request):
    batchdata=newbatches.objects.all().order_by('-id')
    md={"bdata":batchdata}
    return render(request,'user/newbatches.html',md)

def facility(request):
    return render(request,'user/ourfacility.html')



def sstories(request):
    print(request.method)
    clg=request.GET.get('college')
    year=request.GET.get('year')
    collegedata=college.objects.all().order_by('-id')

    pdata="";
    if clg is not None and year is not None:
        pdata=placement.objects.filter(college=clg,session=year)
    else:
        pdata=placement.objects.all()

    clgdata=college.objects.all().order_by('-id')
    sessdata=session_year.objects.all().order_by('-id')

    cdata={"cd":clgdata,"sd":sessdata,"pd":pdata}
    return render(request,'user/sstories2.html',cdata)
