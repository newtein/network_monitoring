import xml.etree.ElementTree as et
import Table3
import socket
#import netfunctions as nf
def tables(filename):
        print("Table 1")
        print("Macaddr/tIPv4/tStarttime/tEndtime/tTimestamp/tHostname/tFiltered_ports/tUnfilteed ports/tvendor")
        tree=et.parse(filename)
        port_list=[]
        
        i=0
        myset=set([])
        root=tree.findall("host")
        table1={}
        table3,portdetail=Table3.table_3(filename)
        table2={}
        t1=[None]*10
        table4={}
        table5=[None]*3
        t=0
        #print(root)
        for host in root:
                print(host)
                stime=host.get("starttime")
                
                etime=host.get("endtime")
                a=host.findall("address")
                if(a[0].get("addrtype")=="ipv4"):
                          ipv4=a[0].get("addr")
                mac=None
                try:
                        mac=a[1].get("addr")
                        vendor=a[1].get("vendor")
                        if(vendor==None):
                                vendor="null"
                except:
                        pass
                
                

                if mac!=None:
                        table1[mac]=[None]*8
                        
                        #table2[mac]=[None]*10
                        table4[mac]=[None]*4
                
                hostname=host.find("hostnames")
                if(hostname!=None):
                        name=hostname.get("name")
                else:
                        name="null"         
                ports=host.find("ports")        
                extraports=ports.find("extraports")
                filter_count=extraports.get("count")
                if(host.find("distance")!=None):
                        hop=host.find("distance").get("value")
                        if(hop==None):
                                hop=0
                if(int(filter_count)==1000):
                                #All filterred                  
                                for ereasons in extraports.findall("extrareasons"):
                                        reason=ereasons.get("reason")
                                        subcount=ereasons.get("count")
                                        #print(reason,subcount)
                else:
                                for ereasons in extraports.findall("extrareasons"):
                                        reason=ereasons.get("reason")
                                        subcount=ereasons.get("count")
                                        #print(reason,subcount)
                                for port in ports.findall("port"):
                                        protocol=port.get("protocol")
                                        portid=port.get("portid")
                                        state=port.find("state").get("state")
                                        reason= port.find("state").get("reason")
                                        reason_ttl=port.find("state").get("reason_ttl")
                                        s=port.find("service")
                                        service_name=s.get("name")
                                        product=s.get("product")
                                        version=s.get("version")
                                        method=s.get("method")
                                        config=s.get("conf")
                                        #port_list.append(service)
                                        i=i+1
                                        if(mac!=None):
                                                if mac not in table2:
                                                        table2[mac]=[]
                                                #addition
                                                t1=[None]*10
                                                t1[0],t1[1],t1[2],t1[3],t1[4],t1[5],t1[6],t1[7],t1[8],t1[9]=portid,protocol,state,reason,reason_ttl,service_name,product,version,method,config
                                                table2[mac].append(t1)
                                                
                if mac!=None:
                        #addition
                        table1[mac][0],table1[mac][1],table1[mac][2],table1[mac][3],table1[mac][4],table1[mac][5],table1[mac][6],table1[mac][7]=ipv4,stime,etime,int(etime)-int(stime),name,subcount,1000-int(subcount),vendor
                        #table1[mac]=[ipv4,stime,etime,int(etime)-int(stime),name,subcount,1000-int(subcount),vendor,hop]
        #addition
                trace=host.find("trace")
        ip=[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]
        port=trace.get("port")
        
        protocol=trace.get("proto")
        if(trace!=None):
                        for hops in trace.findall("hop"):
                                ttl=hops.get("ttl")
                                ipaddr=hops.get("ipaddr")
                                rtt=hops.get("rtt")
                        if mac!=None:
                                #addition
                                table4[mac][0],table4[mac][1],table4[mac][2],table4[mac][3]=hop,ttl,rtt,ipaddr
        #table 5
        tree=et.parse(filename)
        n=tree.getroot()
        print(n.keys())
        for lp,kky in n.items():
                print(lp,kky)
                if(lp=="startstr"):
                        start=kky
        
        f=tree.find(".//finished")
        end=f.get("timestr")
        elapsed=f.get("elapsed")
        print(end,elapsed)
        table5[0],table5[1],table5[2]=start,end,elapsed
        print(table1)
        print("\n Table 2")
        print(table2)
        print("\n Table 4")
        print("\n MacAdr, hop, time_to_live(ms), RTT, Address")
        print(table4)
        print("\n\n")
        print(table3)
        print("\n table 5")
        print(table5)
        return table1,table2,table3,table4,table5,portdetail


#tables("06_11_17_107.xml")


           
