#!/usr/bin/env python3

"""1. On execution of program system should prompt “Enter a host to scan”. User will provide a host name
2. System should look for all the ports between the range of 1 to 1025
3. If the Ports is open it should create a file and add an entry for port number
4. In case of any exception for instance “host is not available”, “host name could not be resolved” or due to any other error you need to write that exception into same file
5. You also need to record starting and ending date and time at the beginning and ending of file accordingly. It should also show the total time it took in port scanning process"""



#Import modules and declare variables

import socket
import time
from datetime import datetime
import threading
from queue import Queue
import sys
socket.setdefaulttimeout(0.25)
print_lock = threading.Lock()

target = ""
target_file = "results.csv"

#create CSV file with 1st line titles
with open(target_file, "a") as file:
    file.write("Host Name,Scanned,Open Ports,Start Time,End Time,Elapsed Time, \n")


def port_scanner1():
# input hostname or IP, try again on error, write errors to csv file
    while True:
        try:
            target = input('Enter the host to be scanned (type quit to exit): ')
            t_IP = socket.gethostbyname(target)
            break
        except:
            if target.lower() == "quit":
                sys.exit("exiting")
            with open(target_file, 'a') as file:
                file.write(target + "," + "NO\n")
            print(str(target) + " does not exist, please try again")

    #write target name and Yes to file
    with open(target_file, "a") as file:
        file.write(target + ",YES,")
    print ('Starting scan on host: ', t_IP)

    #Scan open ports and write to file
    def portscan(port):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                con = s.connect((t_IP, port))
                with print_lock:
                    with open(target_file, "a") as file:
                        print(port, 'is open')
                        file.write("Port " + str(port) + " ")
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
    start_time = ("{:.19}".format(date))
    end_time = ("{:.19}".format(endtime))
    elapsed_time = ("{:.2f} seconds".format(time.time() - startTime))

    print(start_time)
    print(end_time)
    print(elapsed_time)

    with open(target_file, "a") as file:
        file.write("," + start_time)
        file.write("," + end_time)
        file.write("," + elapsed_time + "\n")
    return port_scanner1()
port_scanner1()



