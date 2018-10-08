from django.shortcuts import render,HttpResponseRedirect,reverse
from django.views.decorators.csrf import csrf_exempt
from . models import Users
import json
from django.http import JsonResponse
# Create your views here.

def signup(request):
    return render(request,'ProductiveNITK/signup.html')

def home(request):
    return render(request,'ProductiveNITK/home.html')

@csrf_exempt
def login(request):
    if(request.method == "POST"):
        data = request.POST
        print(data)
        uname = data.get('uname')
        uname = json.loads(uname)
        password = data.get('pass')
        password = json.loads(password)
        data1 = Users.objects.all().filter(username=uname)
        for e in data1:
            if(password == e.password):
                result = 1
                return JsonResponse(result,safe=False)
    else:
        return render(request, 'ProductiveNITK/login.html')


