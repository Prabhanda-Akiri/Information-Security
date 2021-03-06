import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

dst_ip = "74.125.224.72"
#dst_ip=input('\nEnter the destination ip address:	')
src_port = RandShort()
dst_port=80

tcp_response = sr1(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=20)
tcp_response.show()
#print(tcp_response.proto)
if(str(type(tcp_response))=="<type 'NoneType'>"):
	print("Port is Closed")
elif(tcp_response.haslayer(TCP)):
	
	if(tcp_response.getlayer(TCP).flags == 0x12):
		send_rst = sr(IP(dst=dst_ip)/TCP(sport=src_port,dport=dst_port,flags="R"),timeout=10)
		print("Port is Open")
	elif (tcp_response.getlayer(TCP).flags == 0x14):
		print("Port is Closed")

# pktflags = tcp_response.getlayer(TCP).flags

# if pktflags == SYNACK:
#     # port is open
#     print("Open")
#     pass
# else:
#     # port is not open
#     # ...
#     print("Closed")
#     pass