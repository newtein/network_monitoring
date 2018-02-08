import xml.etree.ElementTree as et
import numpy as np
def tables(filename):
        print ("Table 4")
        tree=et.parse(filename)
        root=tree.findall("host")
        table4={}
        table={}
        t1={}
        #f=open("rtt_daily.csv","a")
        f=open("rtt_sd.csv","a")
        #f.write("\nfilename,rtt")
        for host in root:
                stime=host.get("starttime")
                etime=host.get("endtime")
                timestamp=int(etime)-int(stime)
                print(timestamp)
                a=host.findall("address")
                if(a[0].get("addrtype")=="ipv4"):
                        ipv4=a[0].get("addr")
                #table4[ipv4]=[None]*4
                hop=host.find("distance").get("value")
                print(hop)
                if(hop==None):
                    hop=0
                trace=host.find("trace")
                if(trace!=None):
                    for hops in trace.findall("hop"):
                        ttl=hops.get("ttl")
                        print(ttl)
                        ipaddr=hops.get("ipaddr")
                        print(ipaddr)
                        rtt=hops.get("rtt")
                        print(rtt)
                        if ipv4 not in table4:
                                table4[ipv4]=[]
                        t1=[None]*4
                        t1[0],t1[1],t1[2],t1[3]=hop,ttl,rtt,ipaddr
                        table4[ipv4].append(t1)
                                
                        #table4[ipv4][0],table4[ipv4][1],table4[ipv4][2],table4[ipv4][3]=hop,ttl,rtt,ipaddr
        print(table4)
        d={}
        for t in table4:
                print(t)
                x=[]
                for p in table4[t]:
                        print(p[2])
                        x.append(float(p[2]))
                q=np.mean(x)
                print(q)
                d[t]=q
        print(d)
        y=np.std([ d[i] for i in d])
        f.write("\n"+str(filename)+","+str(y))
        f.close()
                
tables("11nov.xml")              
        
                

       
 
