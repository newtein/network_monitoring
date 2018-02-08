import xml.etree.ElementTree as ET
import numpy as np
import pyrebase
import sys
import mysql.connector


con=mysql.connector.connect(user='root', password='',
                              host='localhost',
                              database='NVD')
mycur=con.cursor(buffered=True);

config = {
     "apiKey": "AIzaSyDMbpFGyLizHQ11Su5OnGJ_e4rKHR3mRkY",
    "authDomain": "sal1-5a1a3.firebaseapp.com",
    "databaseURL": "https://sal1-5a1a3.firebaseio.com",
    "projectId": "sal1-5a1a3",
    "storageBucket": "",
    "messagingSenderId": "559686746977"
    }

firebase = pyrebase.initialize_app(config)

def parse_oval(filename):
    nvd_data={}
    net_oval={}
    analysis={}
    final_mean=[]
    it = ET.iterparse(filename)
    for _, el in it:
        if '}' in el.tag:
            el.tag = el.tag.split('}', 1)[1] 
    root = it.root
    print("\n\n")
    print (root)
    oval={}
    metadata={}
    cveid={}
    timestamp2=root.find("generator").find("timestamp")
    timedate2=timestamp2.text

    date2=timedate2[:10]
    end_time=timedate2[11:]

    ovalsys=root.find("results").find("system").find("oval_system_characteristics")
    generator=ovalsys.find("generator")
    system_info=ovalsys.find("system_info")
    host_name=system_info.find("primary_host_name").text
    os_name=system_info.find("os_name").text
    os_version=system_info.find("os_version").text
    architecture=system_info.find("architecture").text
    product_name=generator.find("product_name").text
    product_version=generator.find("product_version").text
    schema_version=generator.find("schema_version").text
    timestamp=generator.find("timestamp")
    timedate=timestamp.text
    date=timedate[:10]
    start_time=timedate[11:]
    interfaces=system_info.find("interfaces")
    c=root.find("oval_definitions").find("definitions").findall("definition")
    countvul=0
    countinv=0
    counttrue=0
    countfalse=0
    counterror=0
    counttrueval=0
    for j in c:
        if j!=None:
            a=j.get("class")
            b=j.get("id")
            g=root.find("results").find("system").find("definitions").find("./definition[@definition_id='%s']"%b).get("result")
            if a=="vulnerability" and g=="true":
                counttrueval=counttrueval+1
                d=j.find("metadata").find("title").text
                e=j.find("metadata").find("reference")
                if e!=None:
                    k=e.get("ref_id")
                    
                    t_output=get_NVD_data(k)
                    if t_output[0]!=None and t_output[1]!=None:
                        cveid[k]=t_output
                    if None not in t_output:
                        nvd_data[k]=t_output
                        final_mean.append(t_output[1])
        
        
                b=b.split(":")
                b=b[-1]
           
                oval[b]=[g,a,k,d]
    
    #print(cveid)
    wrapper={}
    for interface in interfaces:
        interface_name=interface.find("interface_name").text
        ip_address=interface.find("ip_address").text
        mac_address=interface.find("mac_address").text
        z=[mac_address,host_name,os_name,os_version,architecture,product_name,product_version,schema_version,date,start_time,date2,end_time]
        net_oval[mac_address]=[[],[]]
        net_oval[mac_address][0].append(z)
        net_oval[mac_address][1].append(oval)
        wrapper[mac_address]=nvd_data
        #print (mac_address)
    s_t=date+" "+start_time
    e_t=date2+" "+end_time
    return net_oval,wrapper,[s_t,e_t],final_mean,cveid



def get_NVD_data(rid):

    sql=("select basescore2 from OVAL where ID=%s")

    mycur.execute(sql,(rid,))
    row=mycur.fetchone()
    basescore=None
    s=None
    if row!=None and row[0]!=None:
        #print(row[0])
        basescore=float(row[0])
        if 0.0<=basescore<=3.9:
            s="Low"
        elif 4.0<=basescore<=6.9:
            s="Medium"
        elif 7.0<=basescore<=8.9:
            s="High"
        elif 9.0<=basescore<=10.0:
            s="Critical"
        else:
            print("odd score","s")

        return [s,basescore]
    else:
        print("Entry not found in DB")
        return [s,basescore]


    
if __name__=="__main__":

    try:
        sys.argv[1]
    except:
        print("Please enter filename")
    else:

        net_oval,wrapper,time_data,final_mean,cveid=parse_oval(sys.argv[1])

        #print(net_oval,wrapper)
        for macaddr in net_oval:
            macadd=macaddr.replace("-",":")
            db = firebase.database()
            stime=time_data[0]
            etime=time_data[1]

            # ALL NVD DATA
            db.child("TABLES").child(str(macadd)).child("NVD").child(stime+"-"+etime).set(wrapper[macaddr])
            db = firebase.database()
            db.child("TABLES").child(macadd).child("OVAL").child(stime+"-"+etime).child("MetaDATA").set(net_oval[macaddr][0][0])
            
            # OVAL vulnerabilities
            for lzp in net_oval[macaddr][1][0]:

                lzzp=lzp.replace(":","")
                lzzp=lzp.replace(".","")
                db = firebase.database()
                db.child("TABLES").child(macadd).child("OVAL").child(stime+"-"+etime).child("Vulnerability").child(lzzp).set(net_oval[macaddr][1][0][lzp])

            # OVAL Analysis 
            analysis={}
            for idz in wrapper[macaddr]:
                if wrapper[macaddr][idz][0] not in analysis:
                       analysis[wrapper[macaddr][idz][0]]=[]
                analysis[wrapper[macaddr][idz][0]].append(wrapper[macaddr][idz][1])
            for levels in analysis:
                analysis[levels]=np.mean(analysis[levels])
            analysis["final"]=np.mean(final_mean)
            print("Analysis",analysis)
            db = firebase.database()
            db.child("SET").child(macadd).child("OVAL").child(stime+"-"+etime).set(analysis)
            db = firebase.database()
            db.child("SET").child(macadd).child("OVAL").child(stime+"-"+etime).child("CVEID").set(cveid)
           
    
