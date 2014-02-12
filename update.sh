#!/bin/sh
#from http://stackoverflow.com/questions/3497123/run-git-pull-over-all-subdirectories
find . -maxdepth 1 -type d -exec git --git-dir={}/.git --work-tree=$PWD/{} pull origin master \;
