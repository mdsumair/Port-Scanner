import socket
import re

# regular Expression Pattern to recognise IPv4 addresses.
ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
#initializing port numbers
min_port = 0
max_port = 65535
#name header
print(r"""       .__ .__                                                       .__          
___  __|__||  |    ____    ____        ______ __ __   _____  _____   |__|_______  
\  \/ /|  ||  |  _/ __ \  /    \      /  ___/|  |  \ /     \ \__  \  |  |\_  __ \ 
 \   / |  ||  |__\  ___/ |   |  \     \___ \ |  |  /|  Y Y  \ / __ \_|  | |  | \/ 
  \_/  |__||____/ \___  >|___|  /    /____  >|____/ |__|_|  /(____  /|__| |__|    
                      \/      \/          \/              \/      \/              
                                                                                  """)
print("\n****************************************************************")

#ask user to input the ip address
open_ports = []
while True:
    ip_add_entered = input("\nEnter the ip address to scan:")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break
    else:
        print("\nThe ip address you entered is invalid")
while True:
    print("\nPlease entered the range of ports you want to scan in format:example 60-120")
    port_range = input("Enter port range:")
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))

    #coverting string into integer with seperating groups
    if port_range_valid:
        min_port = int(port_range_valid.group(1))
        max_port = int(port_range_valid.group(2))
        break

#Basic socket connection
for port in range(min_port, max_port + 1):
    try:
        # With socket.AF_INET you can enter either a domain name or an ip address
        with socket.socket(socket.AF_INET,socket.SOCK_STREAM ) as s:
            s.settimeout(0.5)   #take time to scan each port
            s.connect((ip_add_entered, port))
            open_ports.append(port)
    except: 
     pass    # Ignore timeouts or connection errors

#printing open ports
while True:
    if open_ports:
        for port in open_ports:
            print(f"Port {port} is open on {ip_add_entered}.")
        break
    else:
        print("No open ports found in the given range.")
        break