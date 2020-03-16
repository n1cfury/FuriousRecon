
8888888888               d8b                            8888888b.                                    
888                      Y8P                            888   Y88b                                   
888                                                     888    888                                   
8888888 888  888 888d888 888  .d88b.  888  888 .d8888b  888   d88P .d88b.   .d8888b .d88b.  88888b.  
888     888  888 888P"   888 d88""88b 888  888 88K      8888888P" d8P  Y8b d88P"   d88""88b 888 "88b 
888     888  888 888     888 888  888 888  888 "Y8888b. 888 T88b  88888888 888     888  888 888  888 
888     Y88b 888 888     888 Y88..88P Y88b 888      X88 888  T88b Y8b.     Y88b.   Y88..88P 888  888 
888      "Y88888 888     888  "Y88P"   "Y88888  88888P' 888   T88b "Y8888   "Y8888P "Y88P"  888  888 



##A Bash recon script using nmap and xsltproc to create some easy to read HTML reports

###What does this do?
#### This bash script does some of the initial recon of a given target and creates a folder to organize your notes and findings. I used this to help with the recon portion of attacking boxes in labs (e.g. HackTheBox, OSCP, )

###How does this work?

## Usage: ./furiousrecon <ip address> <foldername>
#### Requirements: nmap, xsltproc, a browser, and any OS with bash.	
#### This will also work on subnets, but will take longer.
#### Most effective against single boxes (typically =< 60 min)



###Organize my notes, how so?
####In addition to running the nmap commands, this also creates a folder for all the command output consisting of: 

####The folder you specified based on your target
####The output from the nmap commands
####A notes txt file you can add info on your findings to.
####The script creates an HTML file with links to the various nmap scans ran.

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
####	Test the -iL argument
####	Add comments from the script to this README. 
####	Add an addiitonal argument for the full path.
####	Add additional features: (gobuster, nikto, etc).
