#!/usr/bin/env python

import os
import sys
import glob
import time
from datetime import datetime
from termcolor import colored

'''ToDo'''
#Main Arguments
thost = (sys.argv(1)) #target host
tfolder = (sys.argv(2))

#Time check: 
now = datetime.datetime.now()
date_time = now.strftime("%B %d %Y %H:%M:%S")

#Nmap scans used
ipc='nmap -sC -sV -oA nmap-output/ippsec'
all='nmap -Pn -p- -v -v --open -oA nmap-output/allports'
svc='nmap --open -O -sV -T4 -A -v -v -Pn -oA nmap-output/service'
enm='nmap -Pn -T4 -A -v -v --script=*vuln* -oA nmap-output/vulns'
vln='nmap -Pn -T4 -v -v --script=*enum* -oA nmap-output/enum'
udp='nmap -Pn -T4 -sS -sU -v -v -oA nmap-output/udp'
scans = [ipc,all,svc,enm,vln,udp]
snames=["ippsec","allports","services","vulns", "enum", "udp"]
def banner(): #Fancy banner for the tool
    print(colored("\nFuriousRecon - @n1c_Fury", 'yellow', attrs=['bold']))
    print(colored("Usage: ./recon.sh <ip> <name>", 'blue'))
    print(colored("Use '-iL path/file' for multiple hosts", 'blue'))
    print(colored("github.com/n1cfury/FuriousRecon\n", 'yellow'))

def usage(): #Prints usage of the tool
    print ("")
    print (colored("Usage: ./furiousrecon.sh <ip> <name>", 'yellow'))
    print (colored("example: ./furiousrecon 192.168.5.5 targetfolder ",'yellow'))
    print ("")
    sys.exit()

def html_code():    #The HTML page for your report
    with open(tfolder+"-report.html", "w") as file:
        file.write("<!DOCTYPE html>\n")
        file.write("<html>\n")
        file.write("<title>[*] Host Report for "+tfolder+" [*]</title>\n")
        file.write("<body>\n")
        file.write("<h2 align='center''><b>[*]'+tfolder+' - '+thost+' [*]</h></bold>\n")
        file.write("<nav>\n")
        file.write("<h3 align='center'>\n")
        file.write("<a href='nmap-output/ippsec.html' target='iframe_a'>IppSec</a>\n")
        file.write("<a href='nmap-output/allports.html' target='iframe_a'>All Ports</a>\n")
        file.write("<a href='nmap-output/service.html' target='iframe_a'>Services</a>\n")
        file.write("<a href='nmap-output/enum.html' target='iframe_a'>Enum</a\n")
        file.write("<a href='nmap-output/vulns.html' target='iframe_a'>Vulns</a>\n")
        file.write("<a href='nmap-output/udp.html' target='iframe_a'>UDP</a>\n")
        file.write("<p align='left'><iframe height='800px' width='800px' name='iframe_a'></iframe></p>\n")
        file.write("</h3>\n")
        file.write("</nav>\n")
        file.write("</body>\n")
        file.write("</html>\n")
        file.close()

def staging(): #Make target folders and files, and change directory into target folder
    os.mkdir(tfolder)
    os.mkdir(tfolder + '/' + 'nmap-output')
    os.mkdir(tfolder + '/' + 'images')
    os.mkdir(tfolder + '/' + 'tools')
    os.chdir(tfolder)
    print ("[+] Working Directories created")
    print("[+] Current working directory is: " + os.getcwd())
    html_code()
    print ("[+] HTML page created: ")

def recon(): #Runs nmap scans
    for scan in scans:
        os.system(scan + ' ' + thost)
        time.sleep(5)
    for sname in snames:
        os.system(f"xsltproc nmap-output/"+scan+".xml -o nmap-output/"+scan+".html")

def report(): #Writes txt file report of initial findings
    os.system('cat nmap-output/allports.nmap |grep "/" |cut -d " " -f 1 > portlist.txt\n')
    os.system('cat nmap-output/udp.nmap |grep "/" |cut -d " " -f 1 >> portlist.txt') 
    with open("report.txt", "w") as file:
        file.write(tfolder +" - "+ thost)
        file.write("[+] TCP/UDP Ports:\n")        
        os.system("cat portlist.txt |sort -n |uniq >> "+tfolder+"-report.txt\n")
        file.write("[+] Web Recon (directories, robots.txt, etc)\n")
        file.write("[+] Attack Surface (Versions and searchsploit findings)\n")
        file.write("[+] Steps to getting a shell\n")
        file.write("[+] How did you PrivEsc to root\n")
        file.close()
        print(colored("[+] Report scaffolding completed: ", 'green'))

if __name__ == "__main__":
    banner()
    if len(sys.argv) < 3:
        print("")
        print(colored("Not enough arguments. Try again",'red'))
        usage()
    if len(sys.argv) > 3:
        print("")
        print (colored("Too many arguments. Try again",'red'))
        usage()
    else:
        print (colored("Recon has started on: "+ date_time,'green'))
        staging()
        recon()
        report()
        print (colored("Recon completed on : "+ date_time,'green'))
        print (" |) --- Happy Hunting! ---> ")
        sys.exit()
        
# end main