import ftplib
import sys
import threading
from threading import Thread
import time
import traceback

semaphore = 0

def threaded_function(ia):
        print "thread created "+str(ia) 
        while semaphore == 0 :
                time.sleep(10)
                # Try again
        
	exit();

def monitor_thread():
        
        while True :
                print "Enter 1 to start data sessions\n"
                input_value = str(raw_input())
                if input_value == "1" :
                        global semaphore
                        semaphore = 1
                        break
        print "Bye from monitor"


threads = []

if __name__ == "__main__":
	
        threading.stack_size(1024*1024)

        thread = Thread(target = monitor_thread);
        thread.start()
        # Create a monitor thread
        # ACTIVE FTP
	for i in range(1,int(sys.argv[1])+1):
		time.sleep(0.01);
                thread = Thread(target = threaded_function, args = (i,))
		thread.start()
		threads.append(thread)
    	
	for i in threads:
		i.join()
    	print "All threads finished...exiting"	
