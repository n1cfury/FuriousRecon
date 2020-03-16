
    
    ______           _                  ____                      
   / ____/_  _______(_)___  __  _______/ __ \___  _________  ____ 
  / /_  / / / / ___/ / __ \/ / / / ___/ /_/ / _ \/ ___/ __ \/ __ \
 / __/ / /_/ / /  / / /_/ / /_/ (__  ) _, _/  __/ /__/ /_/ / / / /
/_/    \__,_/_/  /_/\____/\__,_/____/_/ |_|\___/\___/\____/_/ /_/ 
                                                                  
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
