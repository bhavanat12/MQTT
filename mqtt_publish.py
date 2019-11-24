import paho.mqtt.client as mqttClient
import time

print("\n######################### Client publishing ###############################\n")
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
 
        print("Connected to broker")
 
        global Connected                #Use global variable
        Connected = True                #Signal connection 
 
    else:
 
        print("Connection failed")

Connected = False   #global variable for the state of the connection
 
broker_address= "localhost"
port = 1883
user = "sra"
password = "sravanti"
 
client = mqttClient.Client("Python4")               #create new instance
#client.username_pw_set(user, password=password) 
   #set username and password
client.username_pw_set("ryqrjgdp", "_W2goEn3fSUP")
client.on_connect= on_connect                      #attach function to callback

#client.connect(broker_address, port=port)          #connect to broker
client.connect("m16.cloudmqtt.com", 16755, 60)

client.loop_start()        #start the loop
 
while Connected != True:    #Wait for connection
    time.sleep(2)
 
try:
    while True:
 
        value = input("Enter message: ")
        client.publish("esp8266",value)
 
except KeyboardInterrupt:
 
    client.disconnect()
    client.loop_stop()
