#!/usr/bin/env python
from socket import *


def userInput(userMsg):
    userMsgStr = "###################\n-------------------\n"+userMsg+"\n-------------------\n###################\n"
    return input(userMsgStr)

if __name__ == '__main__':
    try:
        target = userInput('Enter host to scan: ')
        if target=='exit':
            print("Goodbye")
        else:
            targetIP = gethostbyname(target)
            print('Starting scan on host %s' % targetIP)

            #scan reserved ports
            for i in range(20, 1025):
             s = socket(AF_INET, SOCK_STREAM)

            result = s.connect_ex((targetIP, i))

            #if connection is established
            if(result == 0) :
                print("Port %d: OPEN" % i)
            else:
                print('Port %d: Closed' % i)
            s.close()
    except KeyboardInterrupt:
        print("Goodbye")

