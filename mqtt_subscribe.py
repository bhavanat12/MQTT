import paho.mqtt.client as mqtt

print("\n######################### Client subscribing ###############################\n")
def on_connect(client, userdata, flags, rc):
	print ("Connected with Code : " + str(rc))
	client.subscribe("esp8266")

def on_message(client, userdata, msg):
	print((msg.payload))

client = mqtt.Client("Python1")
client.on_connect = on_connect
client.on_message = on_message
client.connect("10.42.0.69", 1883, 60)
client.username_pw_set("ryqrjgdp", "_W2goEn3fSUP")

client.loop_forever()
