from django.urls import path

from . import views
urlpatterns = [
    path('index/',views.index),
    path('aboutus/', views.aboutus),
    path('contactus/', views.contact),
    path('feedback/', views.feedback),
    path('signup/', views.registration),
    path('signin/', views.signin),
    path('batches/', views.mynewbatches),
    path('facility/', views.facility),
    path('successtories/', views.sstories),
    path('', views.index),
]