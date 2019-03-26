import socket
import sys
import dpkt
import pcapkit

# s = socket.socket()
# s.bind(('',9999))
# s.listen(10) # Acepta hasta 10 conexiones entrantes.

# i = 1
# while True:
# 	sc, address = s.accept()

# 	print(address)
# 	f = open('file_'+ str(i)+".txt",'wb') #open in binary
# 	i=i+1
# 	while (True):
# 		# recibimos y escribimos en el fichero
# 		l = sc.recv(1024)
# 		f.write(l)
# 		if not l:
# 			break

# 	f.close()
# 	sc.close()
# 	print('copied the file.')
# s.close()

# f=open('../ipv4frags.pcap', encoding='latin-1')
# pcap=dpkt.pcap.Reader(f)

# for ts, buf in pcap:
# 	eth = dpkt.ethernet.Ethernet(buf)

# print(eth)
# ip = eth.data
# tcp = ip.data

extraction = pcapkit.extract(fin='../packets/pkt2.pcap', nofile=True)
#print(extraction.frame[0])
frame0 = extraction.frame[0]
flag = pcapkit.IP in frame0
tcp = frame0[pcapkit.IP] if flag else None

cipher_text_bytes=tcp.payload.payload._read_packet()
cipher_text=int(cipher_text_bytes)


# for packet in extraction.reassembly.tcp:
#     for reassembly in packet.packets:
#         if pcapkit.HTTP in reassembly.protochain:
#             print(reassembly.info)