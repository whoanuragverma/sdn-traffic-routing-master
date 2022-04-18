#!/bin/sh
echo "Initializing POX and Mininet"
echo "POX: Using POX version 0.5.0-eel"
echo "Mininet: Using Mininet version 2.2.1"
echo "Using 100 flows and 100 hosts with 10 Mbps bandwidth with proposed solution"
python2 pox/pox.py sway.startup & python2 mininet/topology.py --topo=topo_100_100_10 &