from django.contrib import admin

# Register your models here.

from . models import *      #Importing Classes or we can say tables



class mysoftwareAdmin(admin.ModelAdmin):
    list_display=('id','software_title','software_description','software_picture','software_link','software_date')
admin.site.register(mysoftware,mysoftwareAdmin)

# class categoryAdmin(admin.ModelAdmin):
#     list_display=('id','category_name','category_picture','category_date')
# admin.site.register(category,categoryAdmin)

# class studentbatchAdmin(admin.ModelAdmin):
#     list_display=('id','batch_name')
# admin.site.register(studentbatch,studentbatchAdmin)

# class mylecturesAdmin(admin.ModelAdmin):
#     list_display=('id','video_category','video_batch','vlink','thumbnail','video_description','added_date')
# admin.site.register(mylectures,mylecturesAdmin)

# class batchtimingAdmin(admin.ModelAdmin):
#     list_display=('id','batch','clink','timing','start_date')
# admin.site.register(batchtiming,batchtimingAdmin)