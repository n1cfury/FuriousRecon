#!/usr/bin/env python

import os
import nmap
import lxml
from sys import argv

'''
Furious Recon Todos
    Make working (root) folder e.g. target name
    Make subfolders (images, tools, nmap-output) 
    Create HTML page inside working folder (lines 25-42)
    Nmap scans (lines 45-67)
        foreach [scan,5 sec delay,xsltproc]
    Create Report txt file (lines 68-87)

What are the most important functions
    Create working folders for your target
    Create html page for the report
    create txt file for report notes
    Run multiple nmap scans (output all formats)

Modules needed
nmap, os, lxml, glob
'''
#Variables
thost = (sys.argv(1))
tfolder = (sys.argv(2))

#Subdirectories
sub1='nmap-output'
sub2='images'
sub3='tools'
subfolders = [sub1,sub2,sub3]

#Nmap scan arguments
ipc='-sC -sV -oA nmap-output/ippsec'
all='-Pn -p- -v -v --open -oA nmap-output/allports'
svc='--open -O -sV -T4 -A -v -v -Pn -oA nmap-output/service'
enm='-Pn -T4 -A -v -v --script=*vuln* -oA nmap-output/vulns'
vln='-Pn -T4 -v -v --script=*enum* -oA nmap-output/enum'
udp='-Pn -T4 -sS -sU -v -v -oA nmap-output/udp'
scans = [ipc,all,svc,enm,vln]

def banner(): #Fancy banner for the tool
    print ("")
    print ("[*] ================================================[*]")
    print ("[*]	FuriousRecon - @n1c_Fury                 [*]")
    print ("[*]	Usage: ./recon.sh <ip> <name>	         [*]")
    print ("[*]	Use '-iL path/file' for multiple hosts   [*]")
    print ("[*]	github.com/n1cfury/FuriousRecon          [*]")
    print ("[*] ================================================[*]")
    print ("")
    
def usage(): #Prints usage of the tool
    print ("Usage: ./furiousrecon.sh <ip> <name>")
    print ("example: ./furiousrecon 192.168.5.5 targetfolder ")
    sys.exit()
    
def recon() #Runs nmap scans
    for scan in scans:
        nmap.PortScanner(thost, arguments=scan)

def staging() #Make target directory and subdirectories
    if not os.path.exists(folder):
        os.makedirs(folder)
        for sub in subfolders:
            os.makedirs(sub)

if __name__ == "__main__":
    banner()
    if len(sys.argv) < 3:
        usage()
    else:
        staging()
        scans(target, folder)
        
# end main
