import math
import csv

def MakePri(INDEX,pd,speed,no):

	al, be, g, d = 0.01*pd, 0.001, 0.99, 0.1	#The constant value
	
	f1 = open('csv_file/Danger_v2.csv')
	read = csv.reader(f1)
	dang = [ e for e in read ]
	f1.close()
	
	f2 = open('csv_file/User/User'+str(no)+'.csv')
	read = csv.reader(f2)
	User = [ e for e in read ]
	f2.close()
	
	f3 = open('csv_file/Distance_v2.csv')
	read = csv.reader(f3)
	Dist = [ e for e in read ]
	f3.close()
	
	f4 = open('csv_file/Priority/Priority'+str(no)+'.csv','w')
	
	for a in range(INDEX):
		for b in range(INDEX):
			D = dang[a][b]
			Us = User[a][b]
			Dp = Dist[a][b]
			BlockA = math.floor(float(Dp)*pd)*al
			BlockB = be*BlockA/speed/60
			BlockC = g*float(Us)
			BlockD = d*float(D)
			if(float(Us)==0):
				priority = 0.000
			elif(float(D)==1):
				priority = 1.000
			else:
				priority = math.floor((BlockA+BlockB+BlockC+BlockD)*1000)/1000
				if(priority>1.000):
					priority=1.000
			print("["+str(a)+"]["+str(b)+"] Dp:"+str(math.floor(float(Dp)*pd*100)/100)+"\tD:"+D+"\tUs:"+Us+"\tPri:"+str(priority))
			f4.write(str(priority))
			if(b==(INDEX-1)):
				break
			else:
				f4.write(",")
		f4.write("\n")
	f4.close()

if __name__=='__main__':
	#pass
	#INDEX,pd,speed,no
	MakePri(5,5,4,5)
