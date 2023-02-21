![Banner](https://github.com/n1cfury/FuriousRecon/blob/master/images/banner.png)
                                                                  
##A Bash recon script using nmap and xsltproc to create some easy to read HTML reports

###What does this do?
#### This bash script does runs some nmap scans, creates a web page to easily view them from, and creates a folder to organize your findings. I used this to help with the recon portion of attacking boxes in labs (e.g. HackTheBox, OSCP)

###How does this work?

##Usage: ./furiousrecon <target> <foldername>

###Requirements: 
  - nmap
  - xsltproc
  - Any web browser
  - Linux/Mac OS
  - Sudo (in some cases)
  
####This will also work on subnets, but will take longer.
####Most effective against single boxes (typically =< 60 min)

###Organizes my notes, how so?
###Creates a folder for all the command output consisting of: 

- Target name
- The output from the nmap commands
- A txt file to document findings.
- HTML files to view nmap results from each scan
- Organizes findings: images (for screenshots), tools used, nmap scans



###Running the script, and what to expect.

Running with user privileges
![Running as a low priv user](https://github.com/n1cfury/FuriousRecon/blob/master/images/asuser.png)

Running with root privileges
![Running as Root](https://github.com/n1cfury/FuriousRecon/blob/master/images/asroot.png)

The results folder
![The Results Folder](https://github.com/n1cfury/FuriousRecon/blob/master/images/mortyfolder.png)

The HTML page
![The HTML page](https://github.com/n1cfury/FuriousRecon/blob/master/images/htmlpage.png)

The txt file
![The text file](https://github.com/n1cfury/FuriousRecon/blob/master/images/textfile.png)

###ToDo's
- Test the -iL argument
- Add an additional argument for the full path.
- Figure out threading and get the script to run multiple windows for other tools (nikto, dirb, etc)
- Port over to Python
