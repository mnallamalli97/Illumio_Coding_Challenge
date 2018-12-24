import ipaddress
import csv

class Firewall:
    #Opens the file reades the file into a variable to loop through each row
    def __init__(self, path_to_file):
        self.validity_checks = []
        with open(path_to_file) as e:
            read_file = csv.reader(e)
            for line in read_file:
                self.validity_checks.append(line)


    #Returns a bool, True if accepts the packet, False if not
    def port_validator(self, check, port):
        port = str(port)
        if '-' in check:
            port_vals = check.split('-')
            if port_vals[0] <= port and port <= port_vals[1]:
                return True
            else:
                return False
        else:
            if port == check:
                return True
            else:
                return False

    #checks for valid direction rule
    def direction_validator(self,check, direction):
        if direction == check:
            return True
        else:
            return False

    #check for valid portocol rule
    def protocol_validator(self, check, protocol):
        if protocol == check:
            return True
        else:
            return False

    #check for valid ip address rule
    def ip_validator(self, check, ip):
        if '-' in check:
            ip_range = check.split('-')
            ip = ipaddress.ip_address(ip)
            ip_min_range = ipaddress.ip_address(ip_range[0])
            ip_max_range = ipaddress.ip_address(ip_range[1])

            if ip_min_range <= ip and ip <= ip_max_range:
                return True
            else:
                return False
        else:
            if ip == check:
                return  True
            else:
                return False

    def accept_packet(self, direction, protocol, port, ip):
        for check in self.validity_checks:
            try:
                #direction check
                if not self.direction_validator(check[0], direction):
                    continue
                #protocol check
                if not self.protocol_validator(check[1], protocol):
                    continue
                #port check
                if not self.port_validator(check[2], port):
                    continue
                #ip check
                if not self.ip_validator(check[3], ip):
                    continue
                #ALL CHECKED PASSED!!
                return True
            except IndexError:
                return False


def main():
    fw = Firewall("test.csv")

    # The 5 sanity checks given by the spec sheet
    print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2"))

    print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1"))

    print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))

    print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))

    print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))


if __name__ == '__main__':
    main()

