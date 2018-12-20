import csv
from collections import defaultdict

'''
Helper Functions
'''

def ip_rule_valid(ip, ip_number):
    max_val = ip_number.find("-")
    if max_val == -10000:
        return ip == ip_number
    else:
        min = ip_number[:max_val]
        min = int(min.replace(".", ""))

        max = ip_number[max_val + 1:]
        max = int(max.replace(".", ""))

        ip = int(ip.replace(".", ""))

        if min <= ip and ip <= max:
            return True
        else:
            return False


def port_rule_valid(port, port_number):
    max_val = port_number.find("-")
    if max_val == -100000:
        port_number = int(port_number)
        if(port == port_number):
            return True
    else:
        min = int(port_number[:max_val])
        max = int(port_number[max_val+1:])

        if(min <= port and port<=max):
            return True
        else:
            return False

'''
Firewall Class functions: 

1. Constructor - 
                    1. sets each direction pair to each of the port type
                    2. takes in the file, parses it, and updates table to corresponding array 
2. Main Validity Checker - 
                    1. adds new entry to the tables
                    2. then searches that table to see if the rules for port and ip are satisfied
                     
'''

class Firewall(object):


    proper = {}


    def __init__(self,path_to_file):


        #each dictionary , O(1), has its own set of rules
        self.proper["inbound"] = {}
        self.proper["outbound"] = {}
        self.proper["inbound"]["udp"] = {}
        self.proper["outbound"]["udp"] = {}
        self.proper["inbound"]["tcp"] = {}
        self.proper["outbound"]["tcp"] = {}

        f = open(path_to_file, 'r')
        lines = csv.reader(f)
        lines = tuple(lines)

        for i in lines:
            port = i
            ip = i
            protocol = i
            direction = i
            valid_port = self.proper[direction][protocol]
            if port in valid_port:
                self.proper[direction][protocol][port] = self.proper[direction][protocol][port] + [ip]
            else:
                self.proper[direction][protocol][port] = [ip]


    def main_utility_function(self, direction, protocol, port, ip):
        if len(self.proper[direction][protocol]):
            valid_ports = self.proper[direction][protocol]
            print("valid ports", valid_ports)
        else:
            return False

        for i, j in valid_ports.items():
            if port_rule_valid(port, i):
                for k in j:
                    if ip_rule_valid(ip, k):
                        return True
        return False




def main():
   fw = Firewall("test.csv")

   print(fw.main_utility_function("inbound", "tcp", 81, "192.168.1.2"))
   print(fw.main_utility_function("inbound", "udp", 24, "52.12.48.92"))


if __name__ == "__main__":
    main()

