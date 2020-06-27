#plasma is a terimal or a  shell which is in progress

#pakages
import os
import datetime
import socket
import  platform
import requests
#functons
#vaiables
i=1   #start  a wile loop
#programs

print("\nwelocome to plasma [version 0.1]")
while(i==1):
    user=input(">> ")


  #help----------------------------------------------------------------------------
    if user in["help"] :
        print("shutdown :shut down your pc")
        print("time : get time")
        print("for claculations : add , mul ,div , power")
        print("ip :shows host na,e and ip address")
        print("system info : shows system information")

    #brouse

    if user in ["web"] :
        url=input('ENTER URL')
        r=requests.get(url)
        print(r)

    #------------------------------------------------------------------------------


 #accessblity----------------------------------------------------------


#shutdown


    if user in ["shutdown"] :
        user=input("WARNING!!!!ARE U SURE U WANT TO SHUTDOWN(y/n)??")
        if user in ["Y","y"] :
            os.system("shutdown/s /t 1")
        if user in ["n",'N'] :
            pass
        else :
            print("invalid command")
            pass



#time

    if user in ["time"] :
        show=datetime.datetime.now()
        print(show)



 # arthimetic calicualtions-------------------------------------------------------



 #add
    if user in["add"] :
        var1=int(input("enter first number : "))
        var2= int(input("enter second number : "))
        print(var1+var2)

#subtract

    if user in["sub","subtract"] :
        var1=int(input("enter first number : "))
        var2= int(input("enter second number : "))
        print(var1-var2)

#multply

    if user in["mul"] :
        var1=int(input("enter first number : "))
        var2= int(input("enter second number : "))
        print(var1*var2)
#div

    if user in["div"] :
        var1=int(input("enter first number : "))
        var2= int(input("enter second number : "))
        print(var1/var2)

#raise to

    if user in["power"] :
        var1=int(input("enter first number : "))
        var2= int(input("enter second number : "))
        print(var1**var2)


#-----------------------------------------------------------------------------------



#networking -----------------------------------------------------------------------



                                      #ip address

    if user in["ip"] :
        var1=socket.gethostname()
        var2=socket.gethostbyname(var1)
        print("host name : ",var1)
        print("ip address : ",var2)

#-----------------------------------------------------------------------------------


#hardware-----------------------------------------------------------

    #system info

    if user in ["system info"] :
        print("=" * 40, "System Information", "=" * 40)
        uname = platform.uname()
        print(f"System: {uname.system}")
        print(f"Node Name: {uname.node}")
        print(f"Release: {uname.release}")
        print(f"Version: {uname.version}")
        print(f"Machine: {uname.machine}")
        print(f"Processor: {uname.processor}")




