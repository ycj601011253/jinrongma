from django.urls import path,re_path
from .views import *
urlpatterns = [
    path('index/', index),
    path('email/', email),
    path('login/', login),
    path('logout/', logout),
    path('register/', register),
    path('register_ajax/', register_ajax),
    path('person_step1/', person_step1),
    path('person_step2/', person_step2),
    path('person_step3/', person_step3),
    path('person_step4/', person_step4),
    path('company_public_job/', company_public_job),
    path('company_info/', company_info),
    path('create_company_step1/', create_company_step1),
    path('create_company_step2/', create_company_step2),
    path('create_company_step3/', create_company_step3),
    path('create_company_step4/', create_company_step4),
    path('create_company_step5/', create_company_step5),
    re_path('^$',index),
]
