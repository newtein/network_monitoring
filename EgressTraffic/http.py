from scapy.all import *
from operator import *
import sys



def sorting(pcap):
    newerList = list()
        #remove everything not HTTP (anything not TCP or anything TCP and not HTTP (port 80)
    #count = 0 #dont need this it was for testing
    for x in pcap:
        if x.haslayer(TCP) and x.sport == 80 and bin(x[TCP].flags)!="0b10100": 
            newerList.append(x);
    newerList = sorted(newerList, key=itemgetter("IP.src","TCP.dport"))
    wrpcap("sorted.pcap", newerList)
    return newerList


def extract(pcap,num, count):
    listCounter = count
    counter = 0
    #print listCounter

    #Exit if we have reached the end of the the list of packets
    if count >= len(pcap):
        sys.exit()
    #Create a new file and find the packet with the payload containing the beginning HTML code and write it to file
    while listCounter != len(pcap):
        thisFile = "file" + str(num) + ".html"
        file = open(thisFile,"a")
        s = str(pcap[listCounter][TCP].payload)
        #print "S is: ", s
        x,y,z = s.partition("<")
        s = x + y + z #before was y+z
        if s.find("<html") != -1: 
            file.write(s)
            listCounter = listCounter + 1
            break
        listCounter = listCounter + 1

    #Continue to loop through packets and write their contents until we find the close HTML tag and 
    #include that packet as well
    counter = listCounter
    while counter != len(pcap):
        s =  str(pcap[counter][TCP].payload)
        if s.find("</html>") != -1:
            file.write(s)
            file.close
            break
        else:
            file.write(s)
            counter = counter + 1

    #Recursively call the function incrementing the file name by 1
    #and giving it the last spot in the PCAP we were in so we continue
    #at the next PCAP
    extract(pcap, num+1, counter)


if __name__ == "__main__":
    #Read in file from user
    
    pcapFile  = rdpcap("output.pcap")
    print "Filtering Pcap File of non HTTP Packets and then sorting packets"
    #Sort and Filter the PCAP
    pcapFile = sorting(pcapFile)
    print "Sorting Complete"
    print "Extracting Data"
    #Extract the Data
    extract(pcapFile,1,0)
    print "Extracting Complete"
