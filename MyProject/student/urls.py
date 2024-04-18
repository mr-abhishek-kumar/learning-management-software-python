from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.index),
    # path('index2/',views.index2),
    path('batches/',views.batches),
    path('lectures/',views.lectures),
    path('liveclasses/',views.liveclasses),
    path('logout/',views.logout),
    path('notes/',views.notes),
    path('softwarekit/',views.softwarekit),
    path('tasks/',views.tasks),
    path('stask/',views.stask),
    path('uprofile/',views.uprofile),
    path('lecturesvideo/',views.lecturesvideo),
    path('',views.index),
]