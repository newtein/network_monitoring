import dpkt
import sys
f=file("output.pcap","rb")
pcap=dpkt.pcap.Reader(f)
for ts, buf in pcap:
  eth=dpkt.ethernet.Ethernet(buf)
  ip=eth.data
  try:

	  tcp=ip.data
	  try:
	  	if tcp.dport==80 and len(tcp.data)>0:
	  		try:
	  			http=dpkt.http.Request(tcp.data)
	          		print http.uri
      
          
	  		except:
		  		print 'issue'
		  		continue
	  except:
		  pass
  except:
  	pass


f.close()

