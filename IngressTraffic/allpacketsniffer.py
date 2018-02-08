import socket, sys
from struct import *
import netifaces as ni
import unicodedata
import binascii
import os
systemip=unicodedata.normalize('NFKD',  ni.ifaddresses('wlp3s0')[2][0]['addr']).encode('ascii','ignore')
trustedip=[]
nontrustedip=[]
cnt=0
flags=[]
blockedip=[] 
#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
  b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
  return b
 
#create a AF_PACKET type raw socket (thats basically packet level)
#define ETH_P_ALL    0x0003          /* Every packet (be careful!!!) */
try:
    s = socket.socket( socket.AF_PACKET , socket.SOCK_RAW , socket.ntohs(0x0003))
except socket.error , msg:
    print 'Socket could not be created. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
 
# receive a packet
while True:
    packet = s.recvfrom(65565)
     
    #packet string from tuple
    packet = packet[0]
     
    #parse ethernet header
    eth_length = 14
     
    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])
    #network byte order to host byte order
    #print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)
 
    #Parse IP packets, IP Protocol number = 8
    if eth_protocol == 8 :
        #Parse IP header
        #take first 20 characters for the ip header
        ip_header = packet[eth_length:20+eth_length]
         
        #now unpack them :)
        iph = unpack('!BBHHHBBH4s4s' , ip_header)
        #print str(iph)
 
        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF
 
        iph_length = ihl * 4
 
        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8]);
        d_addr = socket.inet_ntoa(iph[9]);
        if ((s_addr==systemip or d_addr==systemip) and s_addr!=d_addr):
        #if ((s_addr=='192.168.43.59' and d_addr=='192.168.43.238') or (s_addr=='192.168.43.238' and d_addr=='192.168.43.59')):
        #if ((s_addr==systemip or d_addr==systemip)):

            print ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
            if s_addr==systemip and d_addr not in trustedip and d_addr not in nontrustedip:
            #if s_addr==systemip and d_addr not in trustedip and d_addr!=systemip:
                trustedip.append(d_addr)
            elif d_addr==systemip and s_addr not in trustedip and s_addr not in nontrustedip:
                nontrustedip.append(s_addr)
                #print "\n\n PROTECT YOUR COMPUTER\n\n"
                #break
            
 
        #TCP protocol
            if protocol == 6 :
                t = iph_length + eth_length
                tcp_header = packet[t:t+20]
 
            #now unpack them :)
            # tcph = unpack('!HHLLBBHHH' , tcp_header)
             
            # source_port = tcph[0]
            # dest_port = tcph[1]
            # sequence = tcph[2]
            # acknowledgement = tcph[3]
            # doff_reserved = tcph[4]
            # tcph_length = doff_reserved >> 4
            # print str(tcph)
             
            #print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)
                tcp_hdr =unpack("!HH9ss6s", tcp_header)
                print "---------- TCP Header -----------"
                print "Source Port:", tcp_hdr[0]
                print "Destination Port:", tcp_hdr[1]
                print "Flags:", binascii.hexlify(tcp_hdr[3])
                k=binascii.hexlify(tcp_hdr[3])
                dec = int(k, 16)
                #print dec 
                if s_addr in nontrustedip and dec not in flags:
                    flags.append(dec)
                    if 41 in flags:
                        print "\n\n PROTECT YOUR COMPUTER------OS Scanninig \n\n"
                        command="iptables -A INPUT -s "+s_addr+" -j DROP"
                        os.system(command)
                        print "IP BLOCKED"
                        blockedip.append(s_addr)
                        #break;
                        


            if len(nontrustedip)!=0:
                print"-----------------------------------------------------------------------------------------"
                print " Untrusted IP's : "+str(nontrustedip)
                print "Packets coming from these IP's are being checked"
            if len(blockedip)!=0:
                print "----------------------------------------------------------------------------------------"
                print "Blocked IP's : "+ str(blockedip)
                print "These IP's are blocked as these are trying to perform OS scanning"
            os.system("clear")


        #     h_size = eth_length + iph_length + tcph_length * 4
        #     data_size = len(packet) - h_size
             
        #     #get data from the packet
        #     data = packet[h_size:]
             
        #     #print 'Data : ' + data
 
        # #ICMP Packets
        # elif protocol == 1 :
        #     u = iph_length + eth_length
        #     icmph_length = 4
        #     icmp_header = packet[u:u+4]
 
        #     #now unpack them :)
        #     icmph = unpack('!BBH' , icmp_header)
             
        #     icmp_type = icmph[0]
        #     code = icmph[1]
        #     checksum = icmph[2]
             
        #     #print 'Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum)
             
        #     h_size = eth_length + iph_length + icmph_length
        #     data_size = len(packet) - h_size
             
        #     #get data from the packet
        #     data = packet[h_size:]
             
        #     #print 'Data : ' + data
 
        # #UDP packets
        # elif protocol == 17 :
        #     u = iph_length + eth_length
        #     udph_length = 8
        #     udp_header = packet[u:u+8]
 
        #     #now unpack them :)
        #     udph = unpack('!HHHH' , udp_header)
             
        #     source_port = udph[0]
        #     dest_port = udph[1]
        #     length = udph[2]
        #     checksum = udph[3]
             
        #     #print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum)
             
        #     h_size = eth_length + iph_length + udph_length
        #     data_size = len(packet) - h_size
             
        #     #get data from the packet
        #     data = packet[h_size:]
             
        #     #print 'Data : ' + data
 
        # #some other IP packet like IGMP
    # else :
    #     print ''
             
        
