#!/bin/bash
#
# start up script 
#
cd /output


echo "Starting the scanner"
python /code/start.py


echo "export the result "
python /code/parsefile.py



echo "All done die"