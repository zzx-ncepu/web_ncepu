from django.shortcuts import render
from django.shortcuts import HttpResponse
from exam import models
# Create your views here.
user_list = [
    {"name":"zzx","user":"15156","pwd":"abc","sex":"男","school":"华北电力大学","phone":"156486132"},
]
user_list_chazhao = []
def index(request):
    user_list = models.UserInfo.objects.all()
    return render(request,"index.html",{"data":user_list})#第一个参数确定，第二个文件
#render就是相当于打包
#增加成员
def zengjia(request):
    if request.method == "POST":
        name = request.POST.get("name",None)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        sex = request.POST.get("sex",None)
        school = request.POST.get("school",None)
        phone = request.POST.get("phone",None)
        models.UserInfo.objects.create(name = name,user=username, pwd=password,
                                       sex=sex,school=school,phone=phone)
    user_list = models.UserInfo.objects.all()  # 读取数据库中的所有行
    return render(request, "zengjia.html", {"data": user_list})  # 第一个参数确定，第二个文件
#删除成员
def shanchu(request):
    if request.method == "POST":
        name = request.POST.get("name", None)
        username = request.POST.get("username", None)
        models.UserInfo.objects.filter(name=name).delete()
    user_list = models.UserInfo.objects.all()  # 读取数据库中的所有行
    return render(request, "shanchu.html", {"data": user_list})  # 第一个参数确定，第二个文件
#修改成员信息
def xiugai(request):
    if request.method == "POST":
        name = request.POST.get("name",None)
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        sex = request.POST.get("sex",None)
        school = request.POST.get("school",None)
        phone = request.POST.get("phone",None)
        models.UserInfo.objects.filter(name=name).update(user=username, pwd=password,
                                       sex=sex,school=school,phone=phone)
    user_list = models.UserInfo.objects.all()  # 读取数据库中的所有行
    return render(request, "xiugai.html", {"data": user_list})  # 第一个参数确定，第二个文件
#查找成员
def chazhao(request):
    if request.method == "POST":
        name = request.POST.get("name",None)
        global user_list_chazhao
        user_list_chazhao = models.UserInfo.objects.filter(name__exact=name)
    return render(request, "chazhao.html", {"data": user_list_chazhao})  # 第一个参数确定，第二个文件