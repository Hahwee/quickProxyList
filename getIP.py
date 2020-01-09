#!/usr/bin/python3

import requests
import re
import urllib.request as sup
import subprocess


def getParam():
    response=requests.get("https://www.us-proxy.org/")
    getIP=re.findall('\d*\.\d*\.\d*\.\d*\s*\d*(?=\s*\w*\s*\w*\s*\w*\s*\w*\s*\w*\s*\w*\s*\w*\s*)',response.text)
    getPort=re.findall('\d*(?=</td><td>\D*</td><td class)',response.text)
    getPort=[x for x in getPort if x != '']
    writeToFile(getIP,getPort)


def writeToFile(getIP,getPort):
    fileCopy=open('./proxychainsCopy','r')
    readWhat=fileCopy.read()
    fileCopy.close()
    
    newFile=open('/etc/proxychains.conf','w')
    #newFile=open('proxychainsNew','w')
    newFile.write(readWhat)
    
    count=0
    
    for i in getIP:
        newFile.write("http  " + str(i) + " " + str(getPort[count]) + "\n")
        count=count+1
    newFile.close()
    

getParam()

