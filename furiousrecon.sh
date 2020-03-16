#!/usr/bin/env bash

RED=$'\e[1;31m' #Colors used for indicators
YLW=$'\e[1;33m'
GRN=$'\e[1;32m'
BLU=$'\e[1;34m'
WTE=$'\e[0m'
echo "";
echo "$YLW  ================================================";	#Line 20-21 creates the working folder
echo "$BLU[*] 	Recon script  @n1c_Fury                  [*]";	#Line 22 changes directory to the working folder
echo "$BLU[*]	Usage: ./recon.sh <ip> <name>	         [*]";	#e.g. ./recon.sh 10.10.10.37 blocky
echo "$BLU[*]	Use '-iL path/file' for multiple hosts   [*]";
echo "$YLW  ================================================";
echo "";
date;
echo "$WTE[*] Target folder is $YLW[!]--> $2 <--[!]";	#This will create the .txt file for posting all of your notes
echo "$WTE[*] Notes are in ${BLU}$2-report.txt";		#The text file and html file are created instantly
echo "$WTE[*] Scans: --> ${BLU}file:///mnt/hgfs/HTB/$2/$2-report.html. If you get a 404, modify Lines 20, 21, 22";
echo "$WTE[*] Check the web page here: ${BLU}http://$1 "; #start manual recon of the web page if available while you wait on scans
mkdir $2;												#1.		WORKING DIRECTORY CREATED HERE
mkdir $2/nmap-output;									#2.		NMAP OUTPUT DIRECTORIES CREATED HERE
cd $2;													#3.		SCRIPT CHANGES TO WORKING DIRECTORY AND STARTS WORKING
echo "$GRN[*] Creating Report Template..."; #Creates Notes file for pasting notes in plaintext
echo "[+] IP/Host: $1 - $2" >> $2-report.txt;
echo "[+] TCP/UDP:" >> $2-report.txt;
echo "	  * TCP: " >> $2-report.txt;
echo " 	  * UDP: " >> $2-report.txt;
echo "[+] MisConfig (misc. configs)" >> $2-report.txt;
echo "[+] SSH Keys" >> $2-report.txt;
echo "[+] Whatweb" >> $2-report.txt;
echo "[+] Nikto" >> $2-report.txt;
echo "[+] Web Dirs (robots.txt, dirb,etc)" >> $2-report.txt;
echo "[+] OS Enumeration" >> $2-report.txt;
echo "[+] Users" >> $2-report.txt;
echo "[+] User Permissions" >> $2-report.txt;
echo "[+] Scheduled Tasks/Cron Jobs" >> $2-report.txt;
echo "[+] Shares" >> $2-report.txt;
echo "[+] Services" >> $2-report.txt;
echo "[+] Directory Permissions" >> $2-report.txt;
echo "[+] Running Processes" >> $2-report.txt;
echo "[+] System Drivers" >> $2-report.txt;
echo "[+] Network Connections" >> $2-report.txt;
echo "[+] Host File" >> $2-report.txt;
echo "[+] Useful Links" >> $2-report.txt;
echo "[+] Attack Surface" >> $2-report.txt;
echo "[+] Possible Vulnerabilties" >> $2-report.txt;
echo "[+] Effective Exploits" >> $2-report.txt;
echo "[+] Low Privilege Shell" >> $2-report.txt;
echo "[+] Root Shell" >> $2-report.txt;
echo "[+] proof.txt" >> $2-report.txt;
echo "[+] Hashes" >> $2-report.txt;
echo "[+] Screenshots:" >> $2-report.txt;
echo "$GRN[*] Creating HTML report file..."; 				#Creates HTML file in the directory you specified
echo "<!DOCTYPE html>" > $2-report.html;
echo "<html>" >> $2-report.html;
echo "<title>[*] Host Report for $1 - $2 [*]</title> " >> $2-report.html;
echo "<body>" >> $2-report.html;
echo "<h2 align="center"><b>[*] $2 - $1 [*]</h></bold>" >> $2-report.html;
echo "<nav>" >> $2-report.html;
echo "<h3 align="center">" >> $2-report.html;
echo "<a href="nmap-output/top1k.html" target="iframe_a">Top 1000</a>" >> $2-report.html;
echo "<a href="nmap-output/allports.html" target="iframe_a">All Ports</a>" >> $2-report.html;
echo "<a href="nmap-output/service.html" target="iframe_a">Services</a>" >> $2-report.html;
echo "<a href="nmap-output/enum.html" target="iframe_a">Enum</a>" >> $2-report.html;
echo "<a href="nmap-output/vulns.html" target="iframe_a">Vulns</a>" >> $2-report.html;
echo "<a href="nmap-output/udp.html" target="iframe_a">UDP</a>" >> $2-report.html;
echo "<p align="left"><iframe height="800px" width="800px" name="iframe_a"></iframe></p>" >> $2-report.html;
echo "</h3>" >> $2-report.html;
echo "</nav>" >> $2-report.html;
echo "</body>" >> $2-report.html;
echo "</html>" >> $2-report.html;
echo "$YLW[*] Starting scans....";  		#Running nmap scans: Output is saved to nmap-output in the sub directory of the working folder
echo "$WTE[1] Scanning top 1000 Ports";
nmap -Pn -F --top-ports 1000 --open -v -v -oA nmap-output/top1k $1 1> /dev/null;
sleep 5;
xsltproc nmap-output/top1k.xml -o nmap-output/top1k.html;

echo "$WTE[2] All ports, shallow scan";
nmap -Pn -p- -v -v --open -oA nmap-output/allports $1 1> /dev/null;
sleep 5;
xsltproc nmap-output/allports.xml -o nmap-output/allports.html;

echo "$WTE[3] Deep Scan (Service Versions) ";
nmap --open -O -sV -T4 -A -v -v -Pn -oA nmap-output/service $1 1> /dev/null;
sleep 5;
xsltproc nmap-output/service.xml -o nmap-output/service.html;

echo "$WTE[4] NMAP Vulnerabiltiy Scan";
nmap -Pn -T4 -A -v -v --script=*vuln* -oA nmap-output/vulns $1 1> /dev/null;
sleep 5;
xsltproc nmap-output/vulns.xml -o nmap-output/vulns.html;

echo "$WTE[5] Running Enum Scripts...";
nmap -Pn -T4 -v -v --script=*enum* -oA nmap-output/enum $1 1> /dev/null;
sleep 5;
xsltproc nmap-output/enum.xml -o nmap-output/enum.html;

echo "$WTE[6] Running UDP Scan...";
nmap -Pn -T4 -sS -sU -v -v -oA nmap-output/udp $1 1> /dev/null;
sleep 5;
xsltproc nmap-output/udp.xml -o nmap-output/udp.html;
echo "$YLW[!] Recon Completed.";
echo "$BLU ";
date;
echo "$RED |) --- Happy Hunting! ---> ";