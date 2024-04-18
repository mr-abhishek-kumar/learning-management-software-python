from django.shortcuts import render
from django.http import HttpResponse

from user.models import * 
from . models import *  

# Create your views here.

def index(request):
    return render(request,'student/index.html')
def index2(request):
    return render(request,'student/index2.html')


def batches(request):
    nbatchdata=newbatches.objects.all().order_by('-id')
    nbdata={"nbd":nbatchdata}
    return render(request,'student/batches.html',nbdata)


def lectures(request):
    cdata=category.objects.all().order_by('-id')
    md={"cdata":cdata}
    return render(request,'student/lectures.html',md)

def liveclasses(request):
    batchid=request.session.get('batchid')
    data=batchtiming.objects.filter(batch=batchid)
    md={"data":data}
    return render(request,'student/liveclasses.html',md)



def logout(request):
    user = request.session.get('user')
    if user:
        del request.session['user']
        del request.session['userpic']
        del request.session['username']
        return HttpResponse(" <script> location.href='/user/signin/' </script> ")

    return render(request,'student/logout.html')



def notes(request):
    bid=request.session.get('batchid')
    # print(bid)
    ndata=enotes.objects.filter(batch=bid)
    md={"ndata":ndata}
    return render(request,'student/notes.html',md)

def softwarekit(request):
    softdata=mysoftware.objects.all()
    softdict={"sdata":softdata}


    return render(request,'student/softwarekit.html',softdict)





def uprofile(request):
    batchid=request.session.get('batchid')
    user=request.session.get('user')
    udata=signup.objects.filter(email=user)
    md={"udata":udata}
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        college=request.POST.get('college')
        course=request.POST.get('course')
        pyear=request.POST.get('pyear')
        picture=request.FILES['fu']
        signup(name=name,mobile=mobile,passwd=passwd,college=college,course=course, profile=picture,pyear=pyear,email=user,batchid=batchid).save()
        return HttpResponse(" <script>alert('Your Profile udated Successfully....');location.href='/student/uprofile'</script> ")

    return render(request,'student/uprofile.html',md)

def lecturesvideo(request):
    batchid=request.session.get('batchid')
    cid=request.GET.get('cid')
    vdata=mylectures.objects.filter(video_category=cid,video_batch=batchid)
    md={"vdata":vdata}
    return render(request,'student/lecturesvideo.html',md)



        # Me Designing database for task records

def tasks(request):
    # bid=request.session.get('batchid')
    # tdata=taskdownload.objects.filter(batch=bid)
    # md={"tdata":tdata}

    # if request.method=="POST":
    #     batchreco=studentbatch.objects.filter(id=bid)
    #     batch=batchreco[0].batch_name
    #     user=request.session.get('username')
    #     pdf=request.FILES['fu']
    #     taskupload(name=user,pdf_task=pdf,batch=batch).save()
    #     print(user,pdf,batch)
    batchid=request.session.get('batchid')
    tdata="";
    user=request.session.get('username')
    if user:
        tdata=mytask.objects.filter(taskbatch=batchid)
        
        data=submittedtask.objects.filter()
        md={"tdata":tdata,"data":data}


    return render(request,'student/tasks.html',md)


def stask(request):
    user=request.session.get('user')
    if request.method=="POST":
        tid=request.POST.get('tid')
        title=request.POST.get('title')
        answer_file=request.FILES['fu']
        x=submittedtask.objects.filter(tid=tid,userid=user).count()
        if x==1:
            return HttpResponse(" <script>alert('This task is already Submitted..!');location.href='/student/tasks'</script> ")
        else:
            submittedtask(title=title,tid=tid,answer_file=answer_file,userid=user).save()
            return HttpResponse(" <script>alert('Task Submitted Successfully.');location.href='/student/tasks'</script> ")

    return render(request,'student/stask.html')


