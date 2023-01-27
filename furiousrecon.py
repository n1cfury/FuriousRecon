#!/usr/bin/env python

import os
import sys
import glob
import datetime
import time
from termcolor import colored

'''
    Furious Recon Todos
            foreach [scan,5 sec delay,xsltproc]
            xsltproc nmap-output/udp.xml -o nmap-output/udp.html
        Create Report txt file (lines 68-87)
            List ports in TCP ports secion (sorted by order)

    What are the most important functions
        Create working folders for your target
        Create html page for the report
        create txt file for report notes (appending ports and name/ip of target)
        Run multiple nmap scans (output all formats)
        
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

#Arguments
thost = (sys.argv(1))
tfolder = (sys.argv(2))

#Nmap scans
ipc='nmap -sC -sV -oA nmap-output/ippsec'
all='nmap -Pn -p- -v -v --open -oA nmap-output/allports'
svc='nmap --open -O -sV -T4 -A -v -v -Pn -oA nmap-output/service'
enm='nmap -Pn -T4 -A -v -v --script=*vuln* -oA nmap-output/vulns'
vln='nmap -Pn -T4 -v -v --script=*enum* -oA nmap-output/enum'
udp='nmap -Pn -T4 -sS -sU -v -v -oA nmap-output/udp'
scans = [ipc,all,svc,enm,vln,udp]

html_code = """
<!DOCTYPE html>
<html>" 
<title>[*] Host Report for  -  [*]</title> 
<body>
<h2 align="center"><b>[*] $2 - $1 [*]</h></bold>
<nav>
<h3 align="center">
<a href="nmap-output/ippsec.html" target="iframe_a">IppSec</a>
<a href="nmap-output/allports.html" target="iframe_a">All Ports</a>
<a href="nmap-output/service.html" target="iframe_a">Services</a>
<a href="nmap-output/enum.html" target="iframe_a">Enum</a>
<a href="nmap-output/vulns.html" target="iframe_a">Vulns</a>
<a href="nmap-output/udp.html" target="iframe_a">UDP</a>
<p align="left"><iframe height="800px" width="800px" name="iframe_a"></iframe></p>
</h3>
</nav>
</body>
</html>
"""

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

def staging(): #Make target folders and files, and change directory into target folder
    os.mkdir(tfolder)
    os.mkdir(tfolder + '/' + 'nmap-output')
    os.mkdir(tfolder + '/' + 'images')
    os.mkdir(tfolder + '/' + 'tools')
    os.chdir(tfolder)
    file = open(tfolder + '/' + "index.html", "w")
    file.write(html_code)
    file.close()
    print ("[+] HTML page created: ")
    print("[+] Current working directory is: " + os.getcwd())

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
    
    # Declare a variable with the text you want to add to the file
text_to_add = "This is the text that will be added to the file."



def timetracker(): #Announces date/time at the start and finish of this script
    now = datetime.datetime.now()
    date_time = now.strftime("%d%m%y %H:%M:%S")
    print("Date/Time is: " + date_time)

def banner(): #Fancy banner for the tool
    print(colored("\nFuriousRecon - @n1c_Fury", 'yellow', attrs=['bold']))
    print(colored("Usage: ./recon.sh <ip> <name>", 'blue'))
    print(colored("Use '-iL path/file' for multiple hosts", 'blue'))
    print(colored("github.com/n1cfury/FuriousRecon\n", 'yellow'))

def usage(): #Prints usage of the tool
    print (colored("Usage: ./furiousrecon.sh <ip> <name>", 'yellow'))
    print (colored("example: ./furiousrecon 192.168.5.5 targetfolder ",'yellow'))
    sys.exit()



if __name__ == "__main__":
    banner()
    if len(sys.argv) < 3:
        print(colored("Not enough arguments. Try again",'red'))
        usage()
    if len(sys.argv) > 3:
        print (colored("Too many arguments. Try again", 'red'))
        usage()
    else:
        timetracker()
        staging()
        recon()
        print("")
        print (colored("Scans completed",'green'))
        timetracker()
        print (" |) --- Happy Hunting! ---> ")
        sys.exit()
        
# end main
