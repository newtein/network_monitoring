
# Config

import pyrebase
import table12 as t
import os
import sys
your_name="Abhinav"
config = {
     "apiKey": "AIzaSyDMbpFGyLizHQ11Su5OnGJ_e4rKHR3mRkY",
    "authDomain": "sal1-5a1a3.firebaseapp.com",
    "databaseURL": "https://sal1-5a1a3.firebaseio.com",
    "projectId": "sal1-5a1a3",
    "storageBucket": "",
    "messagingSenderId": "559686746977"
    }

firebase = pyrebase.initialize_app(config)

# Post

if __name__=="__main__":

    try:
        sys.argv[1]
    except:
        ip_range="172.16.200.83"
        nmap_command="nmap -A "+ip_range+" -oX myfile.xml"
        os.system(nmap_command)
        table1,table2,table3,table4,table5,osportdetail=t.tables("myfile.xml")
        table5.append(nmap_command)
        print(table5)
        db = firebase.database()
        db.child("INFO").child(your_name).push(table5) 
        
    else:

        table1,table2,table3,table4,table5,osportdetail=t.tables(sys.argv[1])

    for t1 in table1:
        db = firebase.database()
        print(t1)
        print(table1[t1])
        print(table1[t1][2])
        db.child("TABLES").child(t1).child("NMAP").child(str(table1[t1][1])+"-"+str(table1[t1][2])).child("TABLE1").set({"ipv4":table1[t1][0],"timestamp":table1[t1][3],"hostname":table1[t1][4],"filtered_ports":table1[t1][5],"unfiltered_ports":table1[t1][6],"vendor":table1[t1][7]})
        db = firebase.database()
        try:
            db.child("TABLES").child(t1).child("NMAP").child(str(table1[t1][1])+"-"+str(table1[t1][2])).child("TABLE2").set(table2[t1])
        except:
            pass
        db = firebase.database()
        try:
            db.child("TABLES").child(t1).child("NMAP").child(str(table1[t1][1])+"-"+str(table1[t1][2])).child("TABLE3").set(table3[t1])
            db = firebase.database()
            db.child("TABLES").child(t1).child("NMAP").child(str(table1[t1][1])+"-"+str(table1[t1][2])).child("TABLE3").child("PORT").set(osportdetail[t1])
        except:
            pass
        db = firebase.database()
        try:
            db.child("TABLES").child(t1).child("NMAP").child(str(table1[t1][1])+"-"+str(table1[t1][2])).child("TABLE4").set(table4[t1])
        except:
            pass
      
    print("ok")                        

