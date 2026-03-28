from scapy.all import *
import socket


def port_scan(ip):
    ports = [21, 22, 23, 53, 80, 443, 3389, 8080]
    print("Scanning ports...", ip)
    for port in ports:
        packet = IP(dst=ip) / TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)

        if not response:
            pass
        elif response.haslayer(TCP):
            if response[TCP].flags == 0x12:
                sr(IP(dst=ip) / TCP(dport=port, flags="R"), timeout=1, verbose=0)
                print("Port opened: ", port)
            elif response[TCP].flags == 0x14:
                pass


def get_os(ip):
    try:
        ans = sr1(IP(dst=ip) / ICMP(), timeout=2, verbose=0)
        if ans:
            ttl = ans.ttl
            if ttl <= 64:
                return "Linux/Unix (Android/iOS/Mac)"
            elif ttl <= 128:
                return "Windows"
            elif ttl <= 255:
                return "Network Device"
            else:
                return "Unknown TTL"
        else:
            return "Firewall/No Response"
    except:
        return "Error"

def scan(ip):
    packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip+"/24")
    sendp(packet)
    answer, unanswer = srp(packet, verbose=0, timeout=1)
    for snd, rcvd in answer:
        try:
            hostname = socket.gethostbyaddr(rcvd.psrc)[0]
        except:
            try:
                hostname = conf.manufdb._get_manuf(rcvd.hwsrc)
                if hostname == rcvd.hwsrc or hostname == None:
                    hostname = "?"
            except:
                hostname = "?"
        print(rcvd.psrc, "->", rcvd.hwsrc, "->", hostname, "->", get_os(ip))
def spam(ip, string, number):
    text = IP(dst=ip) / UDP(dport=12345) / Raw(load=string)
    send(text, count=number)


while True:
    print("scan loc: 1      spam: 2     scan port: 3")
    try :
        number = int(input())
        if number == 1 or number == 2 or number == 3:
            break
        else:
            continue
    except ValueError:
        continue
if number == 1:
    ip_addr = str(input("IP address: "))
    scan(ip_addr)
elif number == 2:
    ip_addr = str(input("IP address: "))
    phrase = str(input("Phrase: "))
    num = int(input("Number: "))
    spam(ip_addr, phrase, num)
elif number == 3:
    ip_addr = str(input("IP address: "))
    port_scan(ip_addr)
