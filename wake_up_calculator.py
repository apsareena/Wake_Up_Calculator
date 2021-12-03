#!/usr/bin/env python
# coding: utf-8

# In[6]:



import time
from datetime import datetime      # importing datetime module to get the current time


print("***********************Welcome to Wake-up time Calculator************************")    
now = datetime.now()
Current_time = int(now.strftime("%H%M%S"))     
now=time.time()
local_time = time.ctime(now)# input to ask whether the end user wants to sleep now or want to wake up at specified time 
print(local_time)
choice_1 = input("\nEnter 1 to sleep now or 2 to wake up at specified time:\n")      
choice_2 = input("\nEnter 3 to go with four sleep cycles or enter 4 to go with 5 sleep cycles:\n") # no.of cycles slept today 
cycles_slept = int(input("How many cycles have you slept today?:\n"))

def waking_time(N): #function to print wake time
    sleep_sec =  (N-cycles_slept)*5400 + (N-cycles_slept)*900   
    waking_time = time.localtime(now + sleep_sec)
    waking_time = time.strftime("%H:%M:%S", waking_time)
    print("You should wake up at:",waking_time)
    

def sleeping_time(n):  #function to print sleep time
    time_to_wake_up = input("At what time do you want to wake up?\n\nEnter time in the format of 08:45:30, Aug 24 2019\n")                
    time_to_wake_up = time.strptime(time_to_wake_up,"%H:%M:%S, %b %d %Y")                
    time_to_wake_up = time.mktime(time_to_wake_up)               
    sleep_sec = ((n-cycles_slept)*5400+(n-cycles_slept)*900)                
    sleeping_time = time.localtime(time_to_wake_up - sleep_sec)               
    sleeping_time = time.strftime("%H:%M:%S, %b %d %Y",sleeping_time)                
    print("you should sleep at:",sleeping_time)
    
                    
def wake_time(): # user-defined function to suggest the best time to wake up
    if choice_2 == '3':    # condition for 4 sleep cycles
        if cycles_slept >= 4:
            print("You have slept enough no.of cycles.\n-*-*-*-*-*-Have a nice day!!-*-*-*-*-*-")
        elif cycles_slept >= 0 and cycles_slept<4:
            waking_time(4)
    elif choice_2 == '4':    # condition for 5 sleep cycles
        if cycles_slept >= 5:
            print("You have slept enough no.of cycles.\n-*-*-*-*-*-Have a nice day!!-*-*-*-*-*-")
        elif cycles_slept >= 0 and cycles_slept < 5:
            waking_time(5)
    else:
        print("Invalid input")
        
        
def sleep_time():    # user-defined function to tell the end user the appropriate sleeping time
    if choice_2 == '3':
        if cycles_slept >= 4: # condition for 4 sleep cycles
            print("You have slept enough no.of sleep cycles.\n-*-*-*-*-*-Have a nice day!!-*-*-*-*-*-")
        elif cycles_slept >= 0 and cycles_slept <4 :
            sleeping_time(4)
    elif choice_2 == '4':
        if cycles_slept >= 5:   #condition for 5 sleep cycles
            print("You have slept enough no.of cycles.\n-*-*-*-*-*-Have a nice day!!-*-*-*-*-*-")
        elif cycles_slept >= 0 and cycles_slept < 5 :
            sleeping_time(5)
    else:
        print("Invalid input")  
                   
if choice_1 == '1':
    wake_time()     #calling wake_time function
elif choice_1 == '2':
    sleep_time()    #calling sleep_time function
else:
    print("Invalid input")
enter=input("Enter 1:")
if enter == '1':
    print("********Thank you********")
else:
    print("******Good bye********")

    

