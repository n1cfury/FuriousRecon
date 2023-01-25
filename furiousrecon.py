'''
Furious Recon Todos
    Make a function for the banner (lines 9-14)
    Make a function for the usage
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
python-nmap, os, lxml, glob

'''

def banner():
    print ("================================================")
    print ("[*]	FuriousRecon - @n1c_Fury                 [*]")
    print ("[*]	Usage: ./recon.sh <ip> <name>	         [*]")
    print ("[*]	Use '-iL path/file' for multiple hosts   [*]")
    print ("[*]	github.com/n1cfury/FuriousRecon          [*]")
    print ("================================================")
    
def usage():
    print ("Usage: ./furiousrecon.sh <ip> <name>")
    print ("example: ./furiousrecon 192.168.5.5 targetfolder ")
    
    
banner()
    
    
