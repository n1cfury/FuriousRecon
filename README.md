  ______          _                 _____                      
 |  ____|        (_)               |  __ \                     
 | |__ _   _ _ __ _  ___  _   _ ___| |__) |___  ___ ___  _ __  
 |  __| | | | '__| |/ _ \| | | / __|  _  // _ \/ __/ _ \| '_ \ 
 | |  | |_| | |  | | (_) | |_| \__ | | \ |  __| (_| (_) | | | |
 |_|   \__,_|_|  |_|\___/ \__,_|___|_|  \_\___|\___\___/|_| |_|


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

####Running with user privileges

####Running with root privileges

####The results folder

####The HTML page

####The txt file


###ToDo's
####	Link screenshots you uploaded in this repo.
####	Test the -iL argument
####	Add comments from the script to this README. 
####	Add an addiitonal argument for the full path.
####	Add additional features: (gobuster, nikto, etc).
