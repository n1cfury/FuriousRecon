#!/usr/bin/env python
#FuriousRecon (python port)

import os
import nmap
import lxml
import sys
import glob

'''
Furious Recon Todos
    Make working (root) folder e.g. target name
    Nmap scans (lines 45-67)
        foreach [scan,5 sec delay,xsltproc]
    Create Report txt file (lines 68-87)

What are the most important functions
    Create working folders for your target
    Create html page for the report
    create txt file for report notes
    Run multiple nmap scans (output all formats)

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

html_code = """
<!DOCTYPE html>
<html>" 
<title>[*] Host Report for %s - %s [*]</title> % 
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

report= '''
[+] IP/Host:
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
    with open("index.html", "w") as file:
        file.write(html_code)
    with open("report.txt", "w") as file:
        file.write(report)
    if not os.path.exists(tfolder):
        os.makedirs(tfolder)
        for sub in subfolders:
            os.makedirs(sub)
    os.chdir(tfolder)

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

def recon(): #Runs nmap scans
    for scan in scans:
        nmap.PortScanner(thost, arguments=scan)



if __name__ == "__main__":
    banner()
    if len(sys.argv) < 3:
        print("Not enough arguments. Try again")
        print ("")
        usage()
    if len(sys.argv) > 3:
        print ("Too many arguments. Try again")
        print ("")
        usage()
    else:
        staging()
        recon(thost, tfolder)
        
# end main
