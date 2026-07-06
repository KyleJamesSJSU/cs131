#!/bin/bash
#
#


# Git commit and push in a single command
alias 'git commit -m'=gitcp
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

# Test command
echotest () 
{
	if [ -n "$1" ] ; then
		echo $1
	else
		echo "Failure"
	fi

}
