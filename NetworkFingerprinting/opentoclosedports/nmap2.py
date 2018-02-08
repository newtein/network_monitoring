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

db=firebase.database()
user=db.child("TABLES").get()
f=open("set_data2.csv","w")
data=user.val()
f.write("\n macaadr, portid,protocol ,state,reason,reason_ttl,sevice_name,product,version,method,config")
for i in data:
    print(i)
    try:
        for t in data[i]['NMAP']:
                print(t)
                #print(data[i]['NMAP'][t]['TABLE1']['filtered_ports'])
                for l in data[i]['NMAP'][t]['TABLE2']:
                    portid=l[0]
                    print(portid)
                    protocol=l[1]
                    state=l[2]
                    reason=l[3]
                    reason_ttl=l[4]
                    service=l[5]
                    product=l[6]
                    version=l[7]
                    method=l[8]
                    config=l[9]
                    f.write("\n" +str(i)+","+str(portid)+","+str(protocol)+","+str(state)+","+str(reason)+","+str(reason_ttl)+","+str(service)+","+str(product)+","+str(version)+","+str(method)+","+str(config))
    except:
           pass    
f.close()
