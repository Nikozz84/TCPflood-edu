# TCPflood-edu
Simple TCP flooder

Wellcome to the Doser flood script. First of all you need to choose IP (-d) and
port (-p) of the victim machine.Argument -p is optional , you can leave this
field empty and port will be setted automaticly to http (80).

optional arguments:
  -h, --help            show this help message and exit
  -d DISTANATION, --distanation DISTANATION
                        Victim IP address in format -d x.x.x.x
  -p PORT, --port PORT  Victim port(s) that will be attacked

example: python doser.py -d 192.168.0.1 -p 22
