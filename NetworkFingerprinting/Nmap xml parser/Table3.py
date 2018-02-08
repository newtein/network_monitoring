import xml.etree.ElementTree as et


def table_3(filename):
        tree=et.parse(filename)
        port_list=[]
        i=0
        myset=set([])
        root=tree.findall("host")
        table3={}
        portzzz={}
        z=0
        t=0;
     
        for host in root:
                
                
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
                        os=host.find("os")
                        if(os!=None):
                                port=os.findall("portused")
                                flagopen=0
                                flagclosed=0
                                bo=0
                                if mac not in portzzz:
                                        portzzz[mac]=[]
                                
                                for pt in port:
                                        plist=[None]*3
                                        if pt!=None:
                                                if pt.get("state")=="open":
                                                        flagopen=1
                                                elif pt.get("state")=="closed":
                                                        flagclosed=1
                                                plist[2]=pt.get("state")
                                                plist[1]=pt.get("proto")
                                                plist[0]=pt.get("portid")
                                                portzzz[mac].append(plist)
                                        
                               # print (portzzz)                
                                                
                                if flagopen==1 and flagclosed==1:
                                        bo=1
                                osm=os.findall("osmatch")
                                
                                if mac not in table3:
                                        tlist=[None]*6
                                        table3[mac]=[]
                                        if len(osm)==0:
                                                table3[mac].append(tlist)
                                for om in osm:
                                        tlist=[None]*6
                                        if om!=None:
                                                qw=om.find("osclass")
                                                if qw!=None:
                                                        vendor=qw.get("vendor")
                                                        typ=qw.get("type")
                                                        os_family=qw.get("osfamily")
                                                        
                                                name=om.get("name")
                                                acc=om.get("accuracy")
                                        tlist[0]=name
                                        tlist[1]=acc
                                        tlist[2]=bo
                                        tlist[3]=vendor
                                        tlist[4]=typ
                                        tlist[5]=os_family
                                        table3[mac].append(tlist)
                                #print table3[mac]
                                        #print tlist
        #print table3

        return table3,portzzz
                                




#table_3("SampleAxml.xml")
           
