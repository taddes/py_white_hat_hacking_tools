import scapy.all as scapy


def scan(ip):
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    # Set broadcast mac
    broadcast = scapy.Ether(sdt='ff:ff:ff:ff:ff:ff')
    broadcast.show()
    # scapy.ls(scapy.Ether())
    # arp_request.pdst = ip
    print(arp_request.summary())
    print(broadcast.summary())
    scapy.ls(scapy.ARP())
    arp_request_broadcast = broadcast/arp_request
    arp_request_broadcast.show()

scan('10.0.2.1/24')

# Ethernet Frame - data in networks send using mac address, a physical address engraved on each network card, and source mac and dest mac set in ethernet part of each packet.

# Append ARP  request to Ethernet frame

# Create a packet
# Get ARP to ask who has target ip
# Send request destination mac to broadcase MAC