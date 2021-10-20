from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from .models import extendeduser
import re



def login(request):
    if request.method == 'POST':
        
        user = auth.authenticate( username = request.POST['name'], password=request.POST['password1'])
        if user is not None:
            auth.login(request,user)
            datas = extendeduser.objects.filter(user = request.user)
            return render(request,'clash/result.html',{'data':datas})
            # return render(request,'task3/result.html')
        
        else:
             return render(request, 'rc/login.html',{ 'error': "invalid login credentials"})
    else:
        return render(request,'rc/login.html')


def signup(request):
    if request.method == "POST":
                
                if request.POST['password1'] == request.POST['password2']:
                    try:
                        user = User.objects.get(username=request.POST['username'])
                        
                        return render(request, 'rc/register.html',{'error': "username already exist"})
                        
                        
                    except User.DoesNotExist:
                        # user = User.objects.create_user(username=request.POST['username'],password= request.POST['password1'],email= request.POST['email'])
                        # user = User.objects.create_user(username=request.POST['username'],password= request.POST['password1'])
                        fst=request.POST['firstname']
                        lst=request.POST['lstname']
                        num=request.POST['number']
                        gender=request.POST['gender']
                        email= request.POST['email']
                    if (len(request.POST['password1'])<10):
                        return render(request,'rc/register.html',{'error':"Password too Short, Should Contain ATLEAST 1 Uppercase,1 lowercase,1 special Character and 1 Numeric Value"})

                    elif not re.search(r"[\d]+",request.POST['password1']):
                        return render(request,'rc/register.html',{'error':"Your Password must contain Atleast 1 Numeric value "})
                    elif not re.findall('[A-Z]', request.POST['password1']):   
                        return render(request,'rc/register.html',{'error':"Your Password must contain Atleast 1 UpperCase Letter "})

                    elif not re.findall('[a-z]',request.POST['password1']):
                       return render(request,'rc/register.html',{'error':"Your Password must contain Atleast 1 lowercase Letter "})
                    elif not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', request.POST['password1']):   
                       return render(request,'rc/register.html',{'error':"Your Password must contain Atleast 1 Specail character "})
                    
                    else:
                        if extendeduser.objects.filter(email=email):
                          return render(request, 'rc/register.html',{'error': "email id already exist try using another one"})
                        elif extendeduser.objects.filter(number=num):
                          return render(request, 'rc/register.html',{'error': "phonenumber already exist try using another one"})
                        else:
                             user = User.objects.create_user(username=request.POST['username'],password= request.POST['password1'])   
                             newextendeduser = extendeduser(firstname=fst, lstname=lst,email=email ,number=num,gender=gender,user=user)
                             newextendeduser.save()
                             auth.login(request, user)
                             messages.success(request, f'Your account has been Create!! Login Now')

                             return redirect(login)
                else:
                    return render(request, 'rc/register.html',{'error': "Password doesnot match"})


    else:
         return render(request, "rc/register.html")

def logout(request):
    return render(request, "rc/logout.html")