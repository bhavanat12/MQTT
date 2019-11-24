import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
	print ("Connected with Code : " + str(rc))
	client.subscribe("myTopic")

def on_message(client, userdata, msg):
	print((msg.payload))

client = mqtt.Client("Python1")
client.on_connect = on_connect
client.on_message = on_message

#client.connect("localhost", 1883, 60)
#client.username_pw_set("sra", "sravanti")

#client.loop_forever()






#client.on_message=on_message
#client.on_publish=on_publish
client.puback_flag=False #use flag in publish ack
client.mid_value=None
#####
print("connecting to broker ",broker)

client.connect("localhost", 1883, 60)
client.username_pw_set("sra", "sravanti")
client.loop_start() #start loop to process received messages
print("subscribing ")
client.on_connect = on_connect#subscribe
time.sleep(2)
start=time.time()
print("publishing ")
send_header(filename)
Run_flag=True
count=0
##hashes
out_hash_md5 = hashlib.md5()
in_hash_md5 = hashlib.md5()

while Run_flag:
   chunk=fo.read(data_block_size) # change if want smaller or larger data blcoks
   if chunk:
      out_hash_md5.update(chunk)
      out_message=chunk
      #print(" length =",type(out_message))
      c_publish(client,topic,out_message,qos)
         
   else:
      #send hash
      out_message=out_hash_md5.hexdigest()
      send_end(filename)
      #print("out Message ",out_message)
      res,mid=client.publish("data/files",out_message,qos=1)#publish
      Run_flag=False
time_taken=time.time()-start
print("took ",time_taken)
time.sleep(4)
client.disconnect() #disconnect
client.loop_stop() #stop loop
fout.close() #close files
fo.close()
