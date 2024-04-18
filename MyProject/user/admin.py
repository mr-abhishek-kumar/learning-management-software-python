from django.contrib import admin

# Register your models here.

from .models import *

class contactusAdmin(admin.ModelAdmin):
    list_display=('id','name','email','mobile','message')

admin.site.register(contactus,contactusAdmin)



class sliderAdmin(admin.ModelAdmin):
    list_display=('headlines','slider_dec','slider_picture')
admin.site.register(sliger,sliderAdmin)


# rest tables are to be regestered

class newbatchesAdmin(admin.ModelAdmin):
    list_display=('id','name','batchpic','starting_date')
admin.site.register(newbatches,newbatchesAdmin)

class latestbatchesAdmin(admin.ModelAdmin):
    list_display=('id','bname','batchpic','starting_date')
admin.site.register(latestbatches,latestbatchesAdmin)


class collegeAdmin(admin.ModelAdmin):
    list_display=('college_name','college_picture')
admin.site.register(college,collegeAdmin)


class session_yearAdmin(admin.ModelAdmin):
    list_display=('id','session',)
admin.site.register(session_year,session_yearAdmin)

class batchadmin(admin.ModelAdmin):
    list_display=('batch_name',)
admin.site.register(batch,batchadmin)

class placementAdmin(admin.ModelAdmin):
    list_display=('student_picture','student_name','session','batch','college','company_name','company_picture')
admin.site.register(placement,placementAdmin)


class signupAdmin(admin.ModelAdmin):
    list_display=('name','email','passwd','mobile','profile','course','pyear','college','batch','status','batchid')
admin.site.register(signup,signupAdmin)

class ourinsrtuctorsAdmin(admin.ModelAdmin):
    list_display=('id','name','profile_pic','qualification','company_pic','subject')
admin.site.register(ourinsrtuctors,ourinsrtuctorsAdmin)


# class ufeedbackAdmin(admin.ModelAdmin):
#     list_display=('id','uname','city','college','message')
# admin.site.register(ufeedback,ufeedbackAdmin)


# Registering fro student
class categoryAdmin(admin.ModelAdmin):
    list_display=('id','category_name','category_picture','category_date')
admin.site.register(category,categoryAdmin)

class studentbatchAdmin(admin.ModelAdmin):
    list_display=('id','batch_name')
admin.site.register(studentbatch,studentbatchAdmin)

class mylecturesAdmin(admin.ModelAdmin):
    list_display=('id','video_category','video_batch','vlink','thumbnail','video_description','added_date')
admin.site.register(mylectures,mylecturesAdmin)

class batchtimingAdmin(admin.ModelAdmin):
    list_display=('id','batch','clink','timing','start_date')
admin.site.register(batchtiming,batchtimingAdmin)

class enotesAdmin(admin.ModelAdmin):
    list_display=('title','notes_pic','pdf_notes','batch','added_date')
admin.site.register(enotes,enotesAdmin)

# Registering task tables

class mytaskAdmin(admin.ModelAdmin):
    list_display=('id','taskbatch','title','task_file','added_date')
admin.site.register(mytask,mytaskAdmin)

class submittedtaskAdmin(admin.ModelAdmin):
    list_display=('id','title','tid','userid','answer_file','marks')
admin.site.register(submittedtask,submittedtaskAdmin)

class ufeedbackAdmin(admin.ModelAdmin):
    list_display=('id','uname','city','college','message','profile')
admin.site.register(ufeedback,ufeedbackAdmin)