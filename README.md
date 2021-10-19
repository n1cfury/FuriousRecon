# FurousRecon

![Banner](https://github.com/n1cfury/FuriousRecon/blob/master/images/banner.png)

## Scan a box, organize your findings, save time on reporting.

## **Disclaimer** 
I have used this to help with the recon and reporting portion of attacking boxes in labs on various platforms. This can be used in production environments under the caveat you are very comfortable with nmap and modify the scans as needed.

## What does this do?
When applying the arguments, this script runs multiple nmap scans, creates a web page to easily view them from, and creates multiple folders to organize your findings. 

## Why did I make this?
* I wanted to get more comfortable with scripting and make a useful tool
* I have a tendency to want to organize my notes in a particular fashion
* Coming back to a box later is much easier to follow what I've done
* This makes reporting easier

### How does this work?

## Usage: ./furiousrecon <target> <foldername>

## Requirements 
* nmap
* xsltproc
* A web browser
* A non-Windows Operating System
* bash shell
* sudo

## Features
* Using the -iL switch for the argument will let you scan a list of hosts
* This will also work on subnets, but will take longer.
* Most effective against single hosts (typically =< 60 min)
* Creates individual subfolders to organize work on the target host
* Creates a notes.txt file to outline important findings

## Running the script, and what to expect.

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

# ToDo
* Port over to another language (e.g. python)
* Figure out threading to run additional tools
* Screenshots for ports allowing http
