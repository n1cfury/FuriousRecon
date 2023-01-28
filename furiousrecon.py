#!/usr/bin/env python

import os
import sys
import glob
import time
from datetime import datetime
from termcolor import colored

''' Details
    Debugging ToDos
        
    Order of Operations (from the bash script)
        Print the banner
        Announce start date/time
        Make the target folder(arg 2)
        Create subfolders in target folder (tools, images, nmap-output)
        change directory into target folder
        Create HTML file
        Run 6 Nmap scans (output all formats)
        Create notes file
            include target/ip name in the first line
            Grab tcp ports from allports, sort in order and append to TCP line
            Grab udp ports from udp scan, sort in order and append to UDP line
            Create rest of the text file
        Announce date/time (finish)      
'''

thost = (sys.argv(1)) #target host
tfolder = (sys.argv(2))

#Time check: 
now = datetime.datetime.now()
date_time = now.strftime("%B %d %Y %H:%M:%S")

#Nmap scans
ipc='nmap -sC -sV -oA nmap-output/ippsec'
all='nmap -Pn -p- -v -v --open -oA nmap-output/allports'
svc='nmap --open -O -sV -T4 -A -v -v -Pn -oA nmap-output/service'
enm='nmap -Pn -T4 -A -v -v --script=*vuln* -oA nmap-output/vulns'
vln='nmap -Pn -T4 -v -v --script=*enum* -oA nmap-output/enum'
udp='nmap -Pn -T4 -sS -sU -v -v -oA nmap-output/udp'
scans = [ipc,all,svc,enm,vln,udp]

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

reportnotes= '''
[+] TCP/UDP Ports:
[+] Web Recon (directories, robots.txt, etc)
[+] User Creds discovered (did you find users and/or passwords
[+] Network Connections (e.g. netstat output)
[+] Attack Surface (what's in the box and what versions)
[+] Possible Vulnerabilties (these might work)
[+] Effective Exploits (these did work)
[+] Gaining a Foothold (how you found a way in)
[+] Foothold to Shell (reproduce steps for your shell)
[+] Host Enumeration (what's on the box)
[+] Priv Esc to Root (how you got from shell to root)
[+] proof.txt
user: 
root: 
[+] Post Exploitation
'''

def banner(): #Fancy banner for the tool
    print(colored("\nFuriousRecon - @n1c_Fury", 'yellow', attrs=['bold']))
    print(colored("Usage: ./recon.sh <ip> <name>", 'blue'))
    print(colored("Use '-iL path/file' for multiple hosts", 'blue'))
    print(colored("github.com/n1cfury/FuriousRecon\n", 'yellow'))

def usage(): #Prints usage of the tool
    print (colored("Usage: ./furiousrecon.sh <ip> <name>", 'yellow'))
    print (colored("example: ./furiousrecon 192.168.5.5 targetfolder ",'yellow'))
    sys.exit()

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
        os.system(f"xsltproc nmap-output/"+scan+".xml -o nmap-output/"+scan+".html")

def report(): #Writes txt file report of initial findings
    os.system('cat nmap-output/allports.nmap |grep "/" |cut -d " " -f 1 > portlist.txt')
    os.system('\n')
    os.system('cat nmap-output/udp.nmap |grep "/" |cut -d " " -f 1 >> portlist.txt') 
    with open("report.txt", "w") as file:
        file.write(tfolder +" - "+ thost )
        file.write("\n")
        os.system("cat portlist.txt |sort -n |uniq >> "+tfolder+"-report.txt")
    with open("report.txt", "a") as report:
        for line in reportnotes:
            file.write(line)
            file.write("\n")

if __name__ == "__main__":
    banner()
    if len(sys.argv) < 3:
        print("")
        print(colored("Not enough arguments. Try again",'red'))
        usage()
    if len(sys.argv) > 3:
        print("")
        print (colored("Too many arguments. Try again", 'red'))
        usage()
    else:
        print (colored("Recon has started on: "+ date_time, 'green'))
        staging()
        recon()
        print("")
        print (colored("Scan has completed on : "+ date_time,'green'))
        print (" |) --- Happy Hunting! ---> ")
        sys.exit()
        
# end main