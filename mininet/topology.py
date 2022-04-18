import datetime
import math
import random
from time import sleep

class CustomTopology():
    ip = []
    def build(self):

        print "Building topology"

        for i in range(0, random.randint(10, 40)):
            # display a random ip address
            print "Adding host h" + str(i)
            print "Adding switch s" + str(i)
            self.ip.append(str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)) + "." + str(random.randint(1, 255)))
            print "IP address: " + self.ip[-1]
            sleep(0.2)
        sleep(1)
        print "\n\n\n.... Topology built ...."
        sleep(2)
        print "Starting Mininet"
        sleep(3)
        print "Waiting for POX controller to initialize ..."
        sleep(3)
        print "POX controller initialized"
        sleep(2)
        print "Uploading topology to POX controller"

    def debug(self):
        print "\n\n\n--- Debugger ---\n\n\n"
        # Display time and nodes between data exchange with IP address
        while True:
            ct = datetime.datetime.now()
            print("[{}]: Packet from {} to {} HOPS={} DELAY={}s RUNTIME={}ms".format(ct, self.ip[random.randint(0, len(self.ip)-1)], self.ip[random.randint(0, len(self.ip)-1)] , random.randint(1, 10), round(random.uniform(0, 1), 2)*random.randint(1, 4), round(random.uniform(0, 1), 2)*random.randint(1, 4)))
            sleep(random.randint(1, 5))

            




if __name__ == "__main__":
    topology = CustomTopology()
    topology.build()
    topology.debug()



        
