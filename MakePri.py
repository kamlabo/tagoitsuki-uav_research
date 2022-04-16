import math
import csv

def DistCal(Lati, Long, Lati0, Long0, LatiEnd, LongEnd):
　　SET_A = math.sqrt(pow((Lati0 - Lati) / 0.0111, 2)
　　　　　　　　　　+ pow((Long0 - Long) / 0.0091, 2))
　　SET_B = math.sqrt(pow((LatiEnd - Lati) / 0.0111, 2)
　　　　　　　　　　+ pow((LongEnd - Long) / 0.0091, 2))
　　if(SET_A < SET_B):
　　　　return SET_A
　　return SET_B

def MakePri2(MAX, speed, no):
　　f1 = open('CSV/Danger/Danger_' + str(no) + '.csv')
　　read = csv.reader(f1)
　　dang = [e for e in read]
　　f1.close()
　　
　　f2 = open('CSV/User/User_' + str(no) + '.csv')
　　read = csv.reader(f2)
　　User = [e for e in read]
　　f2.close()
　　
　　f3 = open('CSV/Map.csv')
　　read = csv.reader(f3)
　　Dist = [e for e in read]
　　f3.close()
　　
　　pd = math.sqrt(
　　　　　　　　pow((float(Dist[0][1]) - float(Dist[MAX - 1][1])) / 0.0111, 2)+
　　　　　　　　pow((float(Dist[0][2]) - float(Dist[MAX - 1][2])) / 0.0091, 2))
　　
　　#The constant value
　　al, be, g, d = 0.0001 * pd, 0.001, 0.99, 0.1
　　f4 = open('CSV/Priority/Priority_' + str(no) + '.csv', 'w')
　　
　　for a in range(MAX):
　　　　D = dang[a][1]
　　　　Us = User[a][1]
　　　　Dp = DistCal(float(Dist[a][1]), float(Dist[a][2]), 
　　　　　　　　　　float(Dist[0][1]), float(Dist[0][2]),
　　　　　　　　　　float(Dist[MAX - 1][1]), float(Dist[MAX - 1][2]))
　　　　
　　　　Bl_A = math.floor(float(Dp)) * al
　　　　Bl_B = be * BlockA / speed / 60
　　　　Bl_C = g * float(Us)
　　　　Bl_D = d * float(D)
　　　　
　　　　if(float(Us) == 0):
　　　　　　priority = 0.000
　　　　elif(float(D) == 1 or a == 0 or a == MAX - 1):
　　　　　　priority = 1.000
　　　　else:
　　　　　　priority = math.floor((Bl_A + Bl_B + Bl_C + Bl_D) * 1000) / 1000
　　　　　　if(priority > 1.000):
　　　　　　　　priority = 1.000
　　　　
　　　　f4.write(str(priority))
　　　　f4.write('\n')
　　f4.close()
　　
　　#ParamSaves
　　f5 = open('CSV/Priority/PriParams.csv', 'a')
　　f5.write(str(no) + ',' + str(al) + ',' + str(be) + ',' + str(g) + ','
　　　　　　　　+ str(d) + '\n') 
　　f5.close()

if __name__=='__main__':
　　pass
