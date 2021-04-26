from tkinter import *
import threading
import socket
import math
import time

NUM_OF_PORTS = 100
HOST = 'www.hackthissite.org'
ports_scanned = [False] * NUM_OF_PORTS
portFound = ''
startScan = 0
#===================================================================================================================================
def scan_port(port):
    """This function tries to connect to the given port.
    It returns True if can, False otherwise."""
    global ports_scanned
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.3)

    if port <= 0 or port > NUM_OF_PORTS:
        return False
    try:
        s.connect((HOST, port))
        return True
    except:
        return False
#===================================================================================================================================
def scan_range(start, end):
    """Scans a range of ports."""
    global portFound
    for port in range(start, end):
        ports_scanned[port] = False
        if scan_port(port):
            
            portFound = "Port", port, "is open!"
            print("Port", port, "is open!")    
        ports_scanned[port] = True    
#===================================================================================================================================            
def threaded_scan(num_of_threads):
    """This functions scans all NUM_OF_PORTS ports using the given number of threads.
    Each thread scans almost the same number of ports."""
    port = 0
    portSpread = NUM_OF_PORTS/ num_of_threads
    portSpreadRemainder = math.ceil(portSpread)
    threads_list = []
    for x in range(1,num_of_threads+1):
        endport = port + portSpreadRemainder  
        if endport >= NUM_OF_PORTS:
            endport = NUM_OF_PORTS
        thread = threading.Thread(target=scan_range, args=(port, endport))
        print("thread",x," scans ",port,"to",endport)
        port = endport          

        threads_list.append(thread)
    for thread in threads_list:
        thread.start()

    for thread in threads_list:
        thread.join()
#===================================================================================================================================
def send():
 
  global NUM_OF_PORTS
  global HOST
  global ports_scanned
  global startScan
  global portFound
  try: 
      HOST = 'www.hackthissite.org'
      NUM_OF_PORTS = int(number1.get())
      threads =   int(number2.get())
      if (number3.get()!= ""):
       HOST = number3.get()     
  except:
      OPEN_PORT['text'] = "invalid input"
  NUM_OF_PORTS = int(number1.get())
  threads = int(number2.get())
  HOST = number3.get()
  ports_scanned = [False] * NUM_OF_PORTS
  print("Starting to scan ", NUM_OF_PORTS, "ports with", threads, "thread(s) please wait")
  startScan = time.time()
  threaded_scan(threads)
  finishScan = time.time()
  scanTime = float("%0.2f" % (finishScan - startScan))
  print( scanTime, "seconds was taken during the scan")
  OPEN_PORT['text'] = portFound
  print("PortStatus = ", end=" ")
  print(*ports_scanned, sep = ", ")  
 
#===================================================================================================================================

master = Tk()
master.title("Port Scanner")
master.resizable(width= False, height= False)
master.geometry("300x300")

#===================================================================================================================================

number1 = StringVar()  
number2 = StringVar()
number3 = StringVar() 

#=====================================================================================================================================
 
master.geometry("400x250")  
  
Port = Label(master, text = "Port").place(x = 30,y = 50)    
Threads = Label(master, text = "Threads").place(x = 30, y = 90)    
Host = Label(master, text = "Host").place(x = 30, y = 130)
OPEN_PORT = Label(master, text = "")
OPEN_PORT.place(x = 150, y = 190)
  
e1 = Entry(master,textvariable=number1).place(x = 95, y = 50)    
e2 = Entry(master,textvariable=number2).place(x = 95, y = 90)   
e3 = Entry(master,textvariable=number3)
e3.place(x = 95, y = 130)
e3.insert(0, "www.hackthissite.org")


start = Button(master, text = "start",command=send,activebackground = "pink", activeforeground = "blue").place(x = 30, y = 170)

#======================================================================================================================================
master.mainloop()
