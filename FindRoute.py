import csv

def getPri(target, no):
　　f1 = open('CSV/Priority/Priority_' + str(no) + '.csv', 'r')
　　read = csv.reader(f1)
　　Pri = [e for e in read]
　　f1.close()
　　return float(Pri[target][0])

def chooseNextPoint(now, prev, no, MAX, save):
　　fvec = open('CSV/Vector.csv', 'r')
　　Rvec = csv.reader(fvec)
　　Lvec = [e for e in Rvec]
　　fvec.close()
　　
　　chooseList = []
　　PriorityList = []
　　　　for a in range(MAX):
　　　　　　if(a != prev):
　　　　　　　　if( Lvec[now][a] == '1' and getPri(a, no) != 0.0):
　　　　　　　　　　chooseList.append(a)
　　　　　　
　　if(len(chooseList) == 1):
　　　　return chooseList[0]
　　elif(len(chooseList) >= 2):
　　　　maxp = chooseList[0]
　　　　maxpri = getPri(chooseList[0], no)
　　　　　　
　　　　for b in range(1, len(chooseList)):
　　　　　　if(maxpri <= getPri(chooseList[b], no)
　　　　　　　　　　and savehistory(chooseList[b], save)):
　　　　　　　　maxp = chooseList[b]
　　　　　　　　maxpri = getPri(chooseList[b], no)
　　　　　　	　　
　　　　return maxp
　　else:
　　　　return now

def savehistory(target, save):
　　if(len(save) <= 1):
　　　　return 1
　　else:
　　　　for a in range(len(save)):
　　　　　　if(save[a] == target):
　　　　　　　　return 0
　　return 1

def FindRoute(MAX, no):
　　#Starting Value
　　now, prev, purpose, cnt = 0, 0, 21, 1
　　#Save Point
　　save = [now]
　　
　　while cnt <= 50:
　　　　now_pri = getPri(now, no)
　　　　
　　　　next = chooseNextPoint(now, prev, no, MAX, save)
　　　　prev = now
　　　　now = next
　　　　save.append(now)
　　　　
　　　　if(purpose == now):
　　　　　　break
　　　　else:
　　　　　　cnt = cnt + 1
　　
　　f2 = open('CSV/FindRoute/FindRoute_' + str(no) + '.csv', 'w')
　　for a in range(len(save)):
　　　　f2.write(str(save[a]) + ',')
　　f2.close()

def FindRouteBack(MAX, no):
　　#Starting Value
　　now, prev, purpose, cnt = 21, 21, 0, 1
　　#Save Point
　　save = [now]

　　while cnt <= 50:
　　　　now_pri = getPri(now, no)
　　　　next = chooseNextPoint(now, prev, no, MAX, save)
　　　　prev = now
　　　　now = next
　　　　save.append(now)
　　　　
　　　　if(purpose == now):
　　　　　　break
　　　　else:
　　　　　　cnt = cnt + 1
　　
　　f2 = open('CSV/FindRoute/FindRoute_' + str(no) + '.csv', 'w')
　　for a in range(len(save)):
　　　　f2.write(str(save[a]) + ',')
　　f2.close()

if __name__ == '__main__':
　　pass
