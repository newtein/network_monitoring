import dpkt
import sys
import socket
import datetime

f = open(sys.argv[1], "r")
pcap = dpkt.pcap.Reader(f)

http_ports = [80, 8080, 443] # Add other ports if you website on non-standard port.
urls = [ ]
ff=open("urls.txt","w")
prefix="https://"
for timestamp, buf in pcap:
	eth = dpkt.ethernet.Ethernet(buf)
	#print(eth)
	ip = eth.data
	#dstip = socket.inet_ntoa(ip.dst)
	#print(dstip)
	try:
		tcp = ip.data
		
		if tcp.__class__.__name__ == 'TCP':
			#print(tcp.dport)
			if tcp.dport in http_ports and len(tcp.data) > 0:
				try:
					http = dpkt.http.Request(tcp.data)
					
					urls.append(http.headers['host'] + http.uri)
					ff.write(socket.inet_ntoa(ip.src)+", "+socket.inet_ntoa(ip.dst)+", "+prefix+http.headers['host'] + http.uri+", "+str(timestamp)+"\n")
					#print(http.headers['host'])
					
				except Exception as e:
					# Just in case we come across some stubborn kid.
					#print ("[-] Some error occured. - %s" % str(e))
					pass
		if tcp.__class__.__name__ == 'UDP':
			try:
				dns = dpkt.dns.DNS(tcp.data)
			except:
				continue
			if dns.qr != dpkt.dns.DNS_R:
				continue
			if dns.opcode != dpkt.dns.DNS_QUERY:
				continue
			if dns.rcode != dpkt.dns.DNS_RCODE_NOERR:
				continue
			if len(dns.an) < 1:
				continue
			
			else:
				for qname in dns.qd:
					print qname.name
					ff.write(socket.inet_ntoa(ip.src)+", "+socket.inet_ntoa(ip.dst)+", "+prefix+qname.name+", "+str(timestamp)+"\n")

					
	except:
		#print tcp
		pass
f.close()
ff.close()
print ("[+] URLs extracted from PCAP file are:\n")

# for url in urls:
# 	print (url)

