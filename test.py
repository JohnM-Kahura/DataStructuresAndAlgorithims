import re
import sys
import os

def find_ipaddress(filename):
    result = []
    with open(filename) as f:
        for line in f:
            ips = []
            if 'Up' in line:
                ip = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group()
                result.append(ip)
    return result
def extract_ip_ports(filename):
    ips = find_ipaddress(filename)
    ip_ports = {}
    with open(filename) as f:
        for line in f:
            if any(ip in line for ip in ips) and '/tcp' in line:
                ip = re.search('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', line).group()
                n = re.findall("(\d{1,5})\/\w+.\/tcp", line)
                ip_ports[ip] = n
    return ip_ports

if __name__ == '__main__':


    if (len(sys.argv) < 3):
        sys.exit("Too few arguments")
    elif (len(sys.argv) > 3):
        sys.exit("Too many arguments")
    

    try:
        fn1=sys.argv[1]
        fn2=sys.argv[2]
        if(os.path.exists(fn1) ):
            
            print('Found:'+fn1)
            
        elif(os.path.exists(fn2) ):
            
            print('Found:'+fn2)
        else:
            print("File Not Found")    

        for filename in sys.argv[1:]:
            print(extract_ip_ports(filename))

    except OSError as e:
        sys.exit(e.strerror)

