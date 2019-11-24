import paho.mqtt.client as mqtt #import the client1
import time
############
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")

Connected = False   #global variable for the state of the connection
 
def on_message(client, userdata, message):
    print("message received " ,str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)
########################################
broker_address="localhost"
port = 1883
user = "sra"
password = "sravanti"
#broker_address="iot.eclipse.org"
print("creating new instance")
client = mqtt.Client("P1") #create new instance
client.username_pw_set(user, password=password) 
client.on_connect= on_connect
client.on_message=on_message #attach function to callback

print("connecting to broker")
client.connect(broker_address) #connect to broker

print("Subscribing to topic","house/bulbs/bulb1")
client.subscribe("myTopic")
print("Publishing message to topic","house/bulbs/bulb1")
client.publish("myTopic",input("enter the message"))
#time.sleep(100) # wait
#client.loop_stop() #stop the loop
client.loop_forever()
