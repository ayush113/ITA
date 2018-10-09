from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from . models import Reminders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

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
        send_mail(descript)
        return JsonResponse(result,safe=False)
    return render(request, 'Reminders/reminderCreate.html')


def send_mail(message):

    sendEmail = 'ayush.work113@gmail.com'
    sendPwd =
    rec_name = 'Ayush'
    rec_email = 'ayush.kumar1999@hotmail.com'
    # SENDS VERIFICATION EMAIL, PASSWORD SEND EMAIL, AND REPORTS TO USERS

    msg = MIMEMultipart()

    msg['Subject'] = 'Reminder'
    msg['From'] = "Productive NITK "
    msg['To'] = "%s <%s>" % (rec_name, rec_email)

    msg.attach(MIMEText(message, "html"))


    try:
        smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
        smtp_obj.ehlo()  # CONNECTS WITH HOST
        smtp_obj.starttls()  # TLS --> TRANSPORT LAYER SECURITY
        smtp_obj.ehlo()
        smtp_obj.login(sendEmail, sendPwd)
        smtp_obj.sendmail(sendEmail, rec_email, msg.as_string())
        smtp_obj.close()
        return True  # YAY! MAIL IS SENT!
    except smtplib.SMTPException:
        return False  # NOOO! MAIL IS NOT SENT!
