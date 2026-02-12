#!/usr/bin/env bash
RED=$'\e[1;31m' #Colors used for indicators
YLW=$'\e[1;33m'
GRN=$'\e[1;32m'
BLU=$'\e[1;34m'
WTE=$'\e[0m'
echo ""; #Fancy Banner
echo "$YLW  ======================================================";
echo "$BLU[*]	  FuriousRecon - @n1c_Fury  v.20260214         [*]";
echo "$BLU[*]	  Usage: ./recon.sh <ip> <name> <user>         [*]";
#echo "$BLU[*]	Use '-iL path/file' for multiple hosts         [*]";
echo "$BLU[*]	  https://github.com/n1cfury/FuriousRecon      [*]";
echo "$YLW  ======================================================";
echo "";
date;
echo "$WTE[*] ------- Seek and Destroy $3 --------->  "
echo "$WTE[*] Target folder is $YLW[!]--> $2 <--[!]";
echo "$WTE[*] Notes are in ${BLU}$2-report.txt";
echo "$WTE[*] Access the $2-report.html to review the report";
echo "$WTE[*] Check the web page here: ${BLU}http://$1 ";
mkdir $2;
mkdir $2/{nmap-output,tools,images,loot}; #Additional subfolders for your target
cd $2;
echo "$GRN[*] Creating HTML report..."; #Creation of HTML page
echo "<!DOCTYPE html>" > $2-report.html;
echo "<html>" >> $2-report.html;
echo "<title>[*] Host Report for $1 - $2 [*]</title> " >> $2-report.html;
echo "<body>" >> $2-report.html;
echo "<h2 align="center"><b>[*] $2 - $1 [*]</h></bold>" >> $2-report.html;
echo "<nav>" >> $2-report.html;
echo "<h3 align="center">" >> $2-report.html;
echo "<a href="nmap-output/ippsec.html" target="iframe_a">IppSec</a>" >> $2-report.html;
echo "<a href="nmap-output/allports.html" target="iframe_a">All Ports</a>" >> $2-report.html;
echo "<a href="nmap-output/service.html" target="iframe_a">Services</a>" >> $2-report.html;
echo "<a href="nmap-output/enum.html" target="iframe_a">Enum</a>" >> $2-report.html;
echo "<a href="nmap-output/vulns.html" target="iframe_a">Vulns</a>" >> $2-report.html;
echo "<a href="nmap-output/web.html" target="iframe_a">HTTP</a>" >> $2-report.html;
echo "<p align="left"><iframe height="800px" width="800px" name="iframe_a"></iframe></p>" >> $2-report.html;
echo "</h3>" >> $2-report.html;
echo "</nav>" >> $2-report.html;
echo "</body>" >> $2-report.html;
echo "</html>" >> $2-report.html;
echo "$YLW[*] Starting scans...."; #nmap scans ran here. Adjust accordingly
echo "$WTE[1] IppSec Initial Scan";
nmap -sC -sV -oA nmap-output/ippsec $1 1> /dev/null; #nmap for ippsec scan
sleep 5;
xsltproc nmap-output/ippsec.xml -o nmap-output/ippsec.html;
echo "$WTE[2] All ports, shallow scan";
nmap -Pn -p- -v -v --open -oA nmap-output/allports $1 1> /dev/null; #nmap for all ports
sleep 5;
xsltproc nmap-output/allports.xml -o nmap-output/allports.html;
echo "$WTE[3] Deep Scan (Service Versions) ";
nmap --open -O -sV -T4 -A -v -v -Pn -oA nmap-output/service $1 1> /dev/null; #nmap for service versions
sleep 5;
xsltproc nmap-output/service.xml -o nmap-output/service.html;
echo "$WTE[4] NMAP Vulnerabiltiy Scan";
nmap -Pn -T4 -A -v -v --script=*cve* -oA nmap-output/vulns $1 1> /dev/null; #nmap for vuln scans
sleep 5;
xsltproc nmap-output/vulns.xml -o nmap-output/vulns.html;
echo "$WTE[5] Running Enum Scripts...";
nmap -Pn -T4 -v -v --script=*enum* -oA nmap-output/enum $1 1> /dev/null; #nmap for enumeration scans
sleep 5;
xsltproc nmap-output/enum.xml -o nmap-output/enum.html;
echo "$WTE[6] Running HTTP Scan...";
nmap -Pn -T4 -p- --script=*http* -v -v -oA nmap-output/web $1 1> /dev/null; #nmap for udp scans
sleep 5;
xsltproc nmap-output/web.xml -o nmap-output/web.html;
echo "$GRN[*] Creating Report Note file..."; #Creates txt file for findings
echo "[+] IP/Host: $1 - $2" >> $2-report.txt;
echo "[+] TCP/UDP Ports:" >> $2-report.txt;
echo "$YLW[*] Grabbing Ports...";
cat nmap-output/allports.nmap |grep "/" |cut -d " " -f 1 > portlist.txt;
cat nmap-output/web.nmap |grep "/" |cut -d " " -f 1 >> portlist.txt;
cat portlist.txt |sort -n |uniq >> $2-report.txt;
echo "[+] Web Recon (directories, robots.txt, etc)" >> $2-report.txt;
echo "[+] User Creds discovered (did you find users and/or passwords" >> $2-report.txt;
echo "[+] Network Connections (e.g. netstat output)" >> $2-report.txt;
echo "[+] Attack Surface (what's in the box and what versions)" >> $2-report.txt;
echo "[+] Possible Vulnerabilties (these might work)" >> $2-report.txt;
echo "[+] Effective Exploits (these did work)" >> $2-report.txt;
echo "[+] Gaining a Foothold (how you found a way in)" >> $2-report.txt;
echo "[+] Foothold to Shell (reproduce steps for your shell)" >> $2-report.txt;
echo "[+] Host Enumeration (what's on the box)" >> $2-report.txt;
echo "[+] Priv Esc to Root (how you got from shell to root)" >> $2-report.txt;
echo "[+] proof.txt" >> $2-report.txt;
echo "user: " >> $2-report.txt;
echo "root: " >> $2-report.txt;
echo "[+] Post Exploitation" >> $2-report.txt;
echo "$YLW[*] Fixing working folder ownership: $2 -> $3";
sudo chown -R "$3:$3" "$2";
echo "$YLW[!] Recon Completed.  |) --- Happy Hunting $3! --->";
echo "$YLW[!] Here is your folder layout  ";
echo "$YLW[!]	$2 Main target folder.";
echo "$YLW[!] 		$2/nmap-output The nmap scans.";
echo "$YLW[!] 		$2/tools Exploits used.";
echo "$YLW[!] 		$2/images Screenshots.";
echo "$YLW[!] 		$2/loot What you find";
echo "$RED ";
date;