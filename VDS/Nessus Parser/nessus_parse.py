import csv
import numpy as np
import sys
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

def parse_nessus(fname):

	f=open(fname,"r")


	reader=csv.reader(f)
	data={}
	fool=0
	ipv4=0
	fmean={}
	cveid={}
	for l in reader:
		if fool!=0:

			if l[3]!="None":
				if l[1]!="":
					cveid[l[1]]=[]
					cveid[l[1]].append(l[3])
					cveid[l[1]].append(float(l[2]))
					cveid[l[1]].append(l[6])
					cveid[l[1]].append(l[5])
					cveid[l[1]].append(l[7])
				if l[3] not in data:
					data[l[3]]={}
					
				if l[0] not in fmean:
					fmean[l[0]]=[]
				if l[0] not in data[l[3]]:
					data[l[3]][l[0]]=[]
				data[l[3]][l[0]].append(float(l[2]))
				
				fmean[l[0]].append(float(l[2]))
				if ipv4==0:
					ipv4=l[4]
		fool=1
	
	fdata={}
	
	for level in data:
		for ids in data[level]:
			if level not in fdata:
				fdata[level]=[]
			fdata[level].append(np.mean(data[level][ids]))
	
	for level in fdata:
		fdata[level]=np.mean(fdata[level])
	final=[]
	print("fdata",fdata)
	for ids in fmean:
		final.append(np.mean(fmean[ids]))

	fdata["final"]=np.mean(final)
	print(fdata)
	return ipv4,fdata,cveid

if __name__ == "__main__":

	try:
		sys.argv[1]
	except:
		print("Please provide valid path name as parameter 1 Example: python3 nessus_parse.py <filename>")
	else:
		macaddr=input("Copy/Paste Mac")
		window=input("Copy/Paste Window")
		print("** Time should be exact copy-paste from file to maintain same format**")
		stime=input("Copy/Paste start time")
		etime=input("Copy/Paste end time")
		ipv4,fdata,cveid=parse_nessus(sys.argv[1])
		metadata=[ipv4,window,stime,etime]
		db = firebase.database()
		db.child("SET").child(macaddr).child("NESSUS").child(stime.strip()+"-"+etime.strip()).child("RESULTS").set(fdata)
		db = firebase.database()
		db.child("SET").child(macaddr).child("NESSUS").child(stime.strip()+"-"+etime.strip()).child("METADATA").set(metadata)
		db = firebase.database()
		db.child("SET").child(macaddr).child("NESSUS").child(stime.strip()+"-"+etime.strip()).child("CVEID").set(cveid)

