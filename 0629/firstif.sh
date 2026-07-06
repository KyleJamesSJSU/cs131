#!/bin/bash

# First if test

#FILE=$HOME/.bashrc

echo -n "Please enter a filename -> "
read FILE

if [[ -e $FILE ]]; then
	echo "$FILE exists"
else
	echo "$FILE does not exist"
fi
