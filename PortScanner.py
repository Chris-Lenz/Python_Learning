"""1. On execution of program system should prompt “Enter a host to scan”. User will provide a host name
2. System should look for all the ports between the range of 1 to 1025
3. If the Ports is open it should create a file and add an entry for port number
4. In case of any exception for instance “host is not available”, “host name could not be resolved” or due to any other error you need to write that exception into same file
5. You also need to record starting and ending date and time at the beginning and ending of file accordingly. It should also show the total time it took in port scanning process"""





import socket
import time
from datetime import datetime
import threading

from queue import Queue
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

# input hostname or IP, try again on error
while True:
    try:
        target = input('Enter the host to be scanned: ')
        target_file = str(target + ".txt")
        t_IP = socket.gethostbyname(target)
        break
    except:
        bad_target = ("bad_target" + target_file)
        with open(bad_target, 'w') as file:
            file.write(str(target) + "does not exist\n")
        print(str(target) + " does not exist, please try again")

with open(target_file, "a") as file:
    file.write("Scanning: " + target + "\n\n")
print ('Starting scan on host: ', t_IP)

def portscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((t_IP, port))
            with print_lock:
                with open(target_file, "a") as file:
                    print(port, 'is open')
                    file.write("Port " + str(port) + " is open\n")
                    con.close()
        except:
            pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()
startTime = time.time()
date = str(datetime.now())


for x in range(100):
    t = threading.Thread(target = threader)
    t.daemon = True
    t.start()
for worker in range(1, 1025):
    q.put(worker)
q.join()

endtime = str(datetime.now())




print(target + " scan complete")
start_time = ("Start time: {:.19}".format(date))
end_time = ("End time:   {:.19}".format(endtime))
elapsed_time = ('Time taken: {:.2f} seconds'.format(time.time() - startTime))

print(start_time)
print(end_time)
print(elapsed_time)

with open(target_file, "a") as file:
    file.write("\n" + start_time)
    file.write("\n" + end_time)
    file.write("\n" + elapsed_time + "\n\n")




