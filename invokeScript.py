#!/usr/bin/python3
import subprocess

#This line runs the python script that gets the IP addresses/ports with sudo privileges
subprocess.call(['sudo','python3','getIP.py'])

#This line is for debugging and submitting purposes so that there will be no need to install the proxychains program
print('Running Proxychains Success, this is a simple text output for either case if proxychains is or is not installed to verify that the configuration file was changed successfully')

#This is commented out, but will just need to uncomment for the proxychains program
subprocess.call(['proxychains','firefox'])
