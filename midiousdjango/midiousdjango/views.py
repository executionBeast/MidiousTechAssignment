from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.core.mail import EmailMessage
import os
emailParams = {
  "sender":"raos92249@gmail.com",
  "recievers":['ashokag67570@gmail.com'],
  "subject":"Python (Selenium) Assignment - Sujit Kumar",
  "message":'''Approach: Open Google Form in any browser and insppect the dom elements
  and select and copy the id or class of the input or textarea elements
   then using javascript in same browser get those elements using document.getElementsByClassName()
    and try to set values for that element, if succeed then do the same in python code with selenium,
     I created list that keeps data to be filled and iterated over dom input elements
    array passed the keys then usign execute javascript the submit button is clicked to submit form       ''',
  "bcc":['ashokag67570@gmail.com','raos92249@gmail.com',],
  # "cc":['ashokag67570@gmail.com','raos92249@gmail.com','hr@themedius.ai'],
  "cc":['ashokag67570@gmail.com','raos92249@gmail.com'],

  "connection":None,
  "myResume":['/home/sujit/Downloads/Sujit Resume.pdf','/home/sujit/Pictures/Screenshots/SeleniumAutomate.png','/home/sujit/Pictures/Screenshots/SeleniumSuccesScreenShot.png']

}
emailAttachment = ['/home/sujit/Downloads/Sujit Resume.pdf','/home/sujit/Pictures/Screenshots/SeleniumAutomate.png','/home/sujit/Pictures/Screenshots/SeleniumSuccesScreenShot.png']


def sendEmail(request):
  print('Email Sent :', emailParams)
  Email = EmailMessage(
        emailParams["subject"],

        emailParams["message"],
        emailParams["sender"],

        emailParams["recievers"],
        emailParams["bcc"],
        cc=emailParams["cc"]
    )
  Email.attach_file(emailAttachment[0])
  Email.attach_file(emailAttachment[1])
  Email.attach_file(emailAttachment[2])

  Email.send()

  # return HttpResponseRedirect('')
  return HttpResponse(emailParams)



def HomePage(request):
  return HttpResponse("<a href='email'> <button>Send Email</button> </a>")
