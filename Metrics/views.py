from django.db import models
from django.http import  HttpResponse
from django.conf import settings
from django.contrib import messages
from django.shortcuts import render,redirect
from Metrics.forms import userForm
from Metrics.models import user




def index(request):
    return render(request,'index.html')

def adminpage(request):
    return render(request,'admin/adminpage.html')

def editor(request):
    return render(request,'user/editor.html')

def userpage(request):
    print("hello gudmng")
    return render(request,"user/userpage.html")

def adminlogin(request):
    return render(request, "admin/adminlogin.html")

def adminloginentered(request):
    if request.method == 'POST':
        uname=request.POST['uname']
        passwd=request.POST['upass']
        if uname == 'admin' and passwd=='sadaf':
            return render(request,"admin/adminloginentered.html")
        else:
            
            return render(request, "admin/adminlogin.html")


def logoutuser(request):
    return render(request,'user/userlogin.html')

def logoutadmin(request):
    return render(request, 'admin/adminlogin.html')


def userlogin(request):
    return render(request,"user/userlogin.html")

def userregister(request):
    if request.method=='POST':
        form1=userForm(request.POST)
        if form1.is_valid():
            form1.save()
            return render(request, "user/userlogin.html")
            #return HttpResponse("registration succesfully completed")
        else:
            print("form not valid")
            return HttpResponse("form not valid")
    else:
        form=userForm()
        return render(request,"user/userregister.html",{"form":form})

def viewuserdata(request):
    s=user.objects.all()
    return render(request,"admin/viewuserdata.html",{"qs":s})

def activateuser(request):
    if request.method == 'GET':
        uname=request.GET.get('pid')
        print(uname)
        status='Activated'
        print("pid=",uname,"status=",status)
        user.objects.filter(id=uname).update(status=status)
        qs=user.objects.all()
        return render(request,"admin/viewuserdata.html",{"qs":qs})


def userlogincheck1(request):
    if request.method == 'POST':
        uname = request.POST.get('umail')
        print(uname)
        upasswd = request.POST.get('upasswd')
        print(upasswd)
        try:
            check = user.objects.get(mail=uname, passwd=upasswd)
            # print('usid',usid,'pswd',pswd)
            print(check)
            # request.session['name'] = check.name
            # print("name",check.name)
            status = check.status
            print('status',status)
            if status == "Activated":
                request.session['mail'] = check.mail
                return render(request, 'user/userpage.html')
            else:
                messages.success(request, 'user is not activated')
                return render(request, 'user/userlogin.html')
        except Exception as e:
            print('Exception is ',str(e))
            pass
        messages.success(request,'Invalid Email id and password')
        return render(request,'user/userlogin.html')