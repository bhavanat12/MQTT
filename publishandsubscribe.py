
def publish_n_subscribe()
	print("please select your choice")
	print("1)publish a topic")
	print("2)subscribe to a topic")
	user_choice()
	 switch(user_choice) { 
		case 0: 
		    publish(); 
		case 1: 
		    subscribe();  
		default: 
		    print(""); 
	    }; 
