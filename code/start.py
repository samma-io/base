import subprocess
import os
import json



#Get the values we want to start the scanner
target = os.getenv('TARGET', 'samma.io')

#Start the scanner 
def start_scan():
	'''
	Start the domain analyser
	'''
	process = subprocess.Popen('/opt/domain_analyzer-master/domain_analyzer.py  -d {0} -o '.format(target) , shell=True, stdout=subprocess.PIPE)
	process.wait()

start_scan()