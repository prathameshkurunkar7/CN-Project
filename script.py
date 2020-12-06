#-------------------------------------------------------------------------------------------------------------------------#
#                                                 all subdomain
#=========================================================================================================================#
import os
import requests
import IP2Location
import nmap

def subdomain(modurl):
    modurl = modurl.split('://',1)[1]
    if '/' in modurl:
        modurl = modurl.split('/',1)[0]
    os.system("start cmd /k python ./Sublist3r/sublist3r.py -d {} -t 50".format(modurl))

def portScanner(ip_addr):
    scanner = nmap.PortScanner()
    # Regular Scan
    ip_addr = str(ip_addr)
    print('Regular Scan Ongoing...')
    scanner.scan(ip_addr)
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

    # OS Detection
    print('OS detection...')
    print(scanner.scan(ip_addr, arguments="-O")['scan'][ip_addr]['osmatch'][1])

    # Multiple IP inputs 
    print('Multiple IP inputs...')
    scanner.scan(ip_addr,'1-1024', '-v -sS')
    print(scanner.scaninfo())
    # state() tells if target is up or down
    print("Ip Status: ", scanner[ip_addr].state())
    # all_protocols() tells which protocols are enabled like TCP UDP etc
    print("protocols:",scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())

    # Ping Scan
    print('Ping Scan...')
    scanner.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, scanner[x]['status']['state']) for x in scanner.all_hosts()]
    for host, status in hosts_list:
        print('{0}:{1}'.format(host, status))

def IpTracker(ip):
    # ip="115.112.67.196"
    database = IP2Location.IP2Location(os.path.join("data", "IP2LOCATION-LITE-DB11.BIN"))
    rec = database.get_all(str(ip))

    return rec

def hopCounter(ip):
    os.system("start cmd /k tracert {}".format(ip))

def ipDns(ip):
    os.system("start cmd /k nslookup {}".format(ip))

def pinger(ip):
    os.system('start cmd /k ping {}'.format(ip))

def arp(ip):
    os.system('start cmd /k arp -a {}'.format(ip))
#-------------------------------------------------------------------------------------------------------------------------#
#                                                 all subdomain
#=========================================================================================================================#
# import dnspython as dns
# import dns.resolver

# result = dns.resolver.query('tutorialspoint.com', 'A')

# for ipval in result:
#     print('IP', ipval.to_text())
# os.system("start cmd /k ping domain")