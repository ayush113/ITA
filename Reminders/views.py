from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import Reminders

# Create your views here.
def donothing():
    print("AUISJIK")



@csrf_exempt
def createReminder(request):
    if (request.method == "POST"):
        data = request.POST
        title = json.loads(data.get('title'))
        date = json.loads(data.get('date'))
        time = json.loads(data.get('time'))
        priority = json.loads(data.get('priority'))
        descript = json.loads(data.get('description'))
        obj = Reminders(reminderTitle=title,reminderDate=date,reminderDetails=descript,reminderPriority=priority,reminderTime=time)
        obj.save()
        result = 1
        return JsonResponse(result,safe=False)
    return render(request, 'Reminders/reminderCreate.html')
