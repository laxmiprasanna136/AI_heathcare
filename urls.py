"""
URL configuration for DiseasePrediction project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from disease.views import login, adddoctor, adminviewdoctors, deletedoctor, logout, addpatient, viewpatients, \
    deletepatient, updatepatient, updatepatientaction, addpatientaction, viewappointments, addprescription, \
    diseaseprediction, \
    bookappointaction, submitappointment, diseasepredictionaction, addslotaction, addslot, viewslots, \
    addprescriptionaction

urlpatterns = [

    path('admin/', admin.site.urls),

    path('',TemplateView.as_view(template_name = 'index.html')),
    path('login/',TemplateView.as_view(template_name = 'index.html')),
    path('loginaction/',login),

    path('adddoctor/',TemplateView.as_view(template_name = 'adddoctor.html')),
    path('adddoctoraction/',adddoctor),
    path('adminviewdoctors/',adminviewdoctors),
    path('deletedoctor/',deletedoctor),

    path('addpatient/',addpatient),
    path('addpatientaction/',addpatientaction),
    path('viewpatients/',viewpatients),
    path('deletepatient/',deletepatient),

    path('updatepatient/',updatepatient),
    path('updatepatientaction/',updatepatientaction),

    path('viewappointments/',viewappointments),
    path('addprescription/',addprescription),
    path('diseaseprediction/',diseaseprediction),
    path('diseasepredictionaction/',diseasepredictionaction),
    path('bookappointaction/',bookappointaction),
    path('submitappointment/',submitappointment),

    path('addslot/',addslot),
    path('addslotaction/',addslotaction),
    path('viewslots/',viewslots),
    path('addprescriptionaction/', addprescriptionaction),



    path('logout/',logout,name='logout'),

]
