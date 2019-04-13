from django.shortcuts import render,redirect
import hashlib
# Create your views here.
from .models import *


def pwd_encypt(pwd):
    '''密码加密'''
    md5=hashlib.md5()
    md5.update(pwd.encode())
    return md5.hexdigest()


def index(request):
    return render(request,"buyer/index.html")

def email(request):
    return render(request,'buyer/email.html')

def login(request):
    return render(request,'buyer/login.html')

def register(request):
    data={}
    email=request.GET.get("email")
    print(email)
    if Buyer.objects.filter(email=email):
        print("Ss")
        data["error"]="用户名已存在"
    if request.method=="POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        password=pwd_encypt(password)
        buyer_obj=Buyer()
        buyer_obj.email=email
        buyer_obj.password=password
        buyer_obj.save()
        return redirect('/buyer/index/')
    return render(request,'buyer/register.html',locals())

def person_step1(request):
    return render(request,'buyer/个人信息注册_个人信息填写.html')

def person_step2(request):
    return render(request,'buyer/个人信息注册_招聘信息.html')

def person_step3(request):
    return render(request,'buyer/个人信息注册_收藏职位.html')

def person_step4(request):
    return render(request,'buyer/个人信息注册_社交.html')

def company_public_job(request):
    return render(request,'buyer/企业发布职位招聘.html')

def company_info(request):
    return render(request,'buyer/企业基本信息.html')

def create_company_step1(request):
    return render(request,'buyer/创建新公司step1.html')

def create_company_step2(request):
    return render(request,'buyer/创建新公司step2.html')

def create_company_step3(request):
    return render(request,'buyer/创建新公司step3.html')

def create_company_step4(request):
    return render(request,'buyer/创建新公司step4.html')

def create_company_step5(request):
    return render(request,'buyer/创建新公司step5.html')

