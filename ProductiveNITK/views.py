from django.shortcuts import render, HttpResponseRedirect, reverse,redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Users
import json
from django.http import JsonResponse
from django.contrib.auth.models import User as authuser
from django.contrib.auth import authenticate
from django.contrib.auth import login as logs
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
def signup(request):
    if (request.method == "POST"):
        data = request.POST
        uname = data.get('username')
        password = data.get('password')
        email = data.get('email')
        uname = json.loads(uname)
        password = json.loads(password)
        email = json.loads(email)
        obj = Users(username=uname, password=password, email=email)
        obj.save()
        someuser = authuser.objects.create_user(uname,email,password)
        someuser.save()
        #results = '1'
        return redirect(reverse('login'))
        #return JsonResponse(results, safe=False)
    else:
        return render(request, 'ProductiveNITK/signup.html')

@login_required
def home(request):
    return render(request, 'ProductiveNITK/home.html')


def landing(request):
    return render(request, 'ProductiveNITK/landingPage.html')


@csrf_exempt
def login(request):
    if (request.method == "POST"):
        data = request.POST
        uname = data.get('uname')
        uname = json.loads(uname)
        password = data.get('pass')
        password = json.loads(password)
        user = authenticate(username=uname,password=password)
        if user is not None:
            logs(request,user)
            return redirect('home')
            '''result = 1
            print (result)
            return JsonResponse(result,safe=False)'''
        else:
            print("ASDSAD")
            print("sdfs")
            return redirect('signup')
    else:
        return render(request, 'ProductiveNITK/login.html')