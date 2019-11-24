from django.shortcuts import render
import paho.mqtt.client as mqttClient
import time
from accounts.models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
# def index(request):
#     return render(request,'message/index.html')
#
# Connected = False
#
#
# broker_address="localhost"
# port = 1883
#
#
# def on_connect(client, userdata, flags, rc):
#
#     if rc == 0:
#
#         print("Connected to broker")
#
#         global Connected                #Use global variable
#         Connected = True                #Signal connection
#
#     else:
#
#         print("Connection failed")
#
#

def sent_messages(request):
     a = Message.objects.all().order_by('userlogid')
     context = {'messages': a,
                 'Topic' : Topic}
     # return redirect('../')
     return render(request, 'message/display.html', context=context)

def result(request):
    print(request.POST)
    fullname = request.POST['fullname']
    global Topic
    x=request.user
    print(x)
    # Topic=request.POST.get('Topic')
    A = fullname.split(',')
    for i in range(0, len(A)-1):
        B = A[i].split(" ")
        hello.objects.create(fullname=B[1],topic=B[0],author=x)

    #Message.objects.create(fullname=fullname,topic=Topic)
    # client = mqttClient.Client("Python")
    #
    # #client.username_pw_set(user, password=password)    #set username and password
    # client.on_connect= on_connect
    # client.connect(broker_address, port=port)                      #attach function to callback
    # client.loop_start()
    #
    # while Connected != True:    #Wait for connection
    #     time.sleep(2)
    #
    # while True:
    #
    #     value = fullname
    #     client.publish(Topic,value)
    #     client.disconnect()
    #     break
    # client.loop_stop()
    return render(request,'message/main.html')
def main(request):
    return render(request, 'message/main.html')
