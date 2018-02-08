import pyrebase

config = {
     "apiKey": "AIzaSyDMbpFGyLizHQ11Su5OnGJ_e4rKHR3mRkY",
    "authDomain": "sal1-5a1a3.firebaseapp.com",
    "databaseURL": "https://sal1-5a1a3.firebaseio.com",
    "projectId": "sal1-5a1a3",
    "storageBucket": "",
    "messagingSenderId": "559686746977"
    }

firebase = pyrebase.initialize_app(config)
port=""
db=firebase.database()
user=db.child("TABLES").get()
f=open("set_dataos.csv","w")
data=user.val()
f.write("\nmacaddr,os,accuracy,bool,osfamily,type,vendor,port")
for i in data:
    print(i)
    try:
        for t in data[i]['NMAP']:
                print(t)
                #print(data[i]['NMAP'][t]['TABLE1']['filtered_ports'])
                if (len(data[i]['NMAP'][t]['TABLE3'])>=2):
                    if (data[i]['NMAP'][t]['TABLE3']['0'][2])==1 or (data[i]['NMAP'][t]['TABLE3']['0'][2])==0 :
                        port=""
                        for k in data[i]['NMAP'][t]['TABLE3']:
                            if(k=='PORT'):
                                print("--",data[i]['NMAP'][t]['TABLE3'][k])
                                for mp in data[i]['NMAP'][t]['TABLE3'][k]:
                                    print(mp)
                                    port1=mp[0]
                                    print(port1)
                                    port2=mp[1]
                                    print(port2)
                                    port3=mp[2]
                                    print(port3)
                                    port+=str(port1)+"_"+str(port2)+"_"+str(port3)+"_"

                        for k in data[i]['NMAP'][t]['TABLE3']:
                            if(k!='PORT'):
                                o=data[i]['NMAP'][t]['TABLE3'][k][0]
                                os=o.split()
                                os1=os[0]+os[1]
                                accuracy=data[i]['NMAP'][t]['TABLE3'][k][1]
                                print(accuracy)
                                bool=data[i]['NMAP'][t]['TABLE3'][k][2]
                                osfamily=data[i]['NMAP'][t]['TABLE3'][k][5]
                                type=data[i]['NMAP'][t]['TABLE3'][k][4]
                                vendor=data[i]['NMAP'][t]['TABLE3'][k][3]
                                f.write("\n"+str(i)+","+str(os1)+","+str(accuracy)+","+str(bool)+","+str(vendor)+","+str(type)+","+str(osfamily)+","+str(port))
                                
                
    except Exception as e:
        print(e)
                       
f.close()
