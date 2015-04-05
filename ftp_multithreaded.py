import ftplib
import sys
import threading
from threading import Thread
import time
import traceback


semaphore = 0

def threaded_function(file_name,host,passive,local_ip):
	user = "user"
	passw = "freebsd";
	
	ftp = None;
	while True:
		try:
			ftp = ftplib.FTP( host, user, passw, timeout=60*60 )
			print "Control connection for "+str(file_name)+"\n"
			break
		except Exception:
			print traceback.format_exc()
			print "Continuing\n"
			continue
        
	#Active
	ftp.set_pasv(False);
        while semaphore == 0 :
                time.sleep(10)
                # Try again
        
        
        print "Data connection for "+str(file_name)

	filee = open(file_name, 'w')
	
	while True:
		try:
			ftp.retrbinary_mod('RETR '+file_name, filee.write, local_ip, 0)
			break
		except Exception:
			print traceback.format_exc()
			print "Cant initiatte data connection from client 1 for  "+file_name
			time.sleep(2)
			continue
	#ftp.quit()
	
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
	
	############ ARGS ##############
	# 1) file count to be fetched (active)
	# 2) host name
	# 3) file name
        # 4) Start file number
        # 5) Connection rate
	################################
        #threading.stack_size(1024*1024)
	if( len(sys.argv) != 7 ):
		print "Wrong number of args\n"
                print "Usage: python ftp_multithreaded.py <no_of_connections> <host_ip> <file_name> <start_file_no> <connection_rate>\n"
		exit();

	# Arguments are number of files to be fetched
	file_count = int(sys.argv[4]);
        ip = sys.argv[6]
        thread = Thread(target = monitor_thread)
        thread.start()
        print "Monitor created!\n"
        
        host = sys.argv[2];

        sleep_time = 1/float(sys.argv[5])
        print "Sleep time is "+str(sleep_time)
        time.sleep(5)
        # Create a monitor thread
        # ACTIVE FTP
	for i in range(1,int(sys.argv[1])+1):
		time.sleep(sleep_time);
                thread = Thread(target = threaded_function, args = (sys.argv[3]+str(file_count),host,False,ip))
		thread.start()
		threads.append(thread)
		file_count+=1
    	
	for i in threads:
		i.join()
    	print "All threads finished...exiting"	
