from django.shortcuts import render, redirect
import hashlib
# Create your views here.
from .models import *
from django.http import JsonResponse


def buyer_decorater(func):
    def inner(request):
        email = request.session.get("email")
        user_id = request.COOKIES.get("user_id")
        if email and user_id:
            return func(request)
        else:
            return redirect('/buyer/login/')

    return inner


def pwd_encypt(pwd):
    '''密码加密'''
    md5 = hashlib.md5()
    md5.update(pwd.encode())
    return md5.hexdigest()


def index(request):
    return render(request, "buyer/index.html")


def email(request):
    return render(request, 'buyer/email.html')


def login(request):
    data = {"error": ""}
    if request.session.get("email"):
        return redirect("/buyer/index/")
    if request.method == "POST":
        email = request.POST.get("email")
        buyer_obj = Buyer.objects.filter(email=email)
        if buyer_obj:
            password = request.POST.get("password")
            pwd = pwd_encypt(password)
            if buyer_obj[0].password == pwd:
                response = redirect("/buyer/index/")
                response.set_cookie("user_id", buyer_obj[0].id)
                request.session["email"] = email
                return response
            else:
                data["error"] = "密码错误"
        else:
            data["error"] = "用户名不存在"
    return render(request, 'buyer/login.html', locals())


def logout(request):
    response = redirect('/buyer/index/')
    response.delete_cookie('id')
    del request.session['email']
    return response


def register_ajax(request):
    data = {}
    email = request.GET.get("email")
    type = request.GET.get("type")
    if int(type) == 1:
        if Buyer.objects.filter(email=email):
            data["result"] = "true"
    else:
        if Company.objects.filter(email=email):
            data["result"] = "true"
    return JsonResponse(data=data)


def register(request):
    if request.method == "POST":
        if request.POST.get("ok") == "ok":
            type2 = request.POST.get("type2")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password = pwd_encypt(password)
            if int(type2) == 1:
                buyer_obj = Buyer()
            else:
                buyer_obj = Company()
            buyer_obj.email = email
            buyer_obj.password = password
            buyer_obj.save()
            return redirect('/buyer/index/')
        else:
            data = {"error": "注册失败，请重新输入"}
            return render(request, 'buyer/register.html', {"data": data})
    return render(request, 'buyer/register.html')


@buyer_decorater
def person_step1(request):
    person_obj = Person_step1.objects.filter(buyer_id=request.COOKIES.get("user_id")).first()
    email = request.session.get("email")
    if request.method == "POST":
        nickname = request.POST.get("nickname")
        sex = request.POST.get("sex")
        province = request.POST.get("province")
        city = request.POST.get("city")
        circle = request.POST.get("circle")
        username = request.POST.get("username")
        topDegree = request.POST.get("topDegree")
        workyear = request.POST.get("workyear")
        tel = request.POST.get("tel")
        person_step1 = Person_step1()
        person_step1.name = nickname
        person_step1.sex = sex
        person_step1.province = province
        person_step1.city = city
        person_step1.circle = circle
        person_step1.username = username
        person_step1.topDegree = topDegree
        person_step1.tel = tel
        person_step1.workyear = workyear
        person_step1.buyer_id = request.COOKIES.get("user_id")
        person_step1.save()
        person_obj.delete()
        return redirect("/buyer/person_step2/")

    return render(request, 'buyer/个人信息注册_个人信息填写.html', locals())


def person_step2(request):
    return render(request, 'buyer/个人信息注册_招聘信息.html')


def person_step3(request):
    return render(request, 'buyer/个人信息注册_收藏职位.html')


def person_step4(request):
    return render(request, 'buyer/个人信息注册_社交.html')


def company_public_job(request):
    return render(request, 'buyer/企业发布职位招聘.html')


def company_info(request):
    return render(request, 'buyer/企业基本信息.html')


def create_company_step1(request):
    return render(request, 'buyer/创建新公司step1.html')


def create_company_step2(request):
    return render(request, 'buyer/创建新公司step2.html')


def create_company_step3(request):
    return render(request, 'buyer/创建新公司step3.html')


def create_company_step4(request):
    return render(request, 'buyer/创建新公司step4.html')


def create_company_step5(request):
    return render(request, 'buyer/创建新公司step5.html')
