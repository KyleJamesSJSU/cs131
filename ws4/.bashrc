#!/bin/bash
#
# Written by Kyle James
# also added source ~/cs131/ws4/.bashrc to ~/.bashrc, didn't want to modify 
# that file too much


# Git commit and push in a single command
gitcp () 
{
	# check if a message was provided, if not print an error message
	if [ -n "$1" ] ; then
		# commit and push
		git commit -m "$1"
		git push
	else
		# print error message with echo
		echo 'Error: no commit message provided'
	fi
}

# Alias to go to home/cs131 directory quickly
alias home='cd ~/cs131/'

# Taken from example bashrc, makes a file executable
alias mx='chmod a+x'

# Inspired by the phpconfig command in the example bashrc, opens this file in a 
# text editor and then runs source to update the environment
bashrc () 
{
	vim ~/cs131/ws4/.bashrc
	source ~/cs131/ws4/.bashrc
}

# Edit the .gitignore file
gitignore () 
{
	vim ~/cs131/.gitignore
}

# Test command
echotest () 
{
	if [ -n "$1" ] ; then
		echo $1
	else
		echo "Failure"
	fi
}


