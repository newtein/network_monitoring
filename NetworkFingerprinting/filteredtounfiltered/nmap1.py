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
f=open("set_data.csv","w")
data=user.val()
f.write("\nmacaddr,filtered_ports,ipv4,timestamp,unfiltered_ports,ratio:fil/unfil ports,vendor")
for i in data:
    print(i)
    try:
        for t in data[i]['NMAP']:
            print(t)
            #print(data[i]['NMAP'][t]['TABLE1']['filtered_ports'])
            fil=data[i]['NMAP'][t]['TABLE1']['filtered_ports']
            #print(fil)
            ip=data[i]['NMAP'][t]['TABLE1']['ipv4']
            #print(ip)
            time=data[i]['NMAP'][t]['TABLE1']['timestamp']
            #print(time)
            u=data[i]['NMAP'][t]['TABLE1']['unfiltered_ports']
            #print(u)
            v=data[i]['NMAP'][t]['TABLE1']['vendor']
            #print(v)
            fil=int(fil)
            u=int(u)
            ratio=fil/u
            print(ratio)
            f.write("\n"+str(i)+","+str(fil)+","+str(i)+","+str(time)+","+str(u)+","+str(ratio)+","+str(v))
    except:
          pass

f.close()
