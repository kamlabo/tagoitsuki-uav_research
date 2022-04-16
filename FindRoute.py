#Choose Value Sort
import csv

def getPri( x , y , no):
	f1 = open('csv_file/Priority/Priority'+str(no)+'.csv','r')
	read = csv.reader( f1 )
	Pri = [ e for e in read ]
	f1.close()
	return float( Pri[ x ][ y ] )

def getUpPos( a ):
	if (a != 0):
		a = a - 1
	return a

def getDownPos( a, INDEX ):
	if ( a != ( INDEX - 1 )):
		a = a + 1
	return a

def getRightPos( b , INDEX):
	if ( b != INDEX -1 ):
		b = b + 1
	return b

def getLeftPos( b ):
	if ( b != 0):
		b = b - 1
	return b

def savehistory(cnt, target_x, target_y, save_x, save_y):
	if(cnt==1):
		return 1
	else:
		for a in range(cnt):
			for b in range(cnt):
				if(save_x[a]==target_x and save_y[b]==target_y):
					return 0
	return 1
	
def FindRoute( INDEX, no ):
	
	#Starting Value
	now_a, now_b, pre_a, pre_b, cnt = 0, 0, 4, 4, 1
	#Save Point
	save_a, save_b = [now_a], [now_b]

	while cnt<=50:
		now_pri = getPri(now_a, now_b, no)
		print('cnt:'+str(cnt),end='')
		print('['+str(now_a)+','+str(now_b)+']')
		#Chooser List
		up, down, right, left = getUpPos(now_a), getDownPos(now_a,INDEX), getRightPos(now_b,INDEX), getLeftPos(now_b)
		upp, downp, rightp, leftp = getPri(up, now_b, no), getPri(down, now_b, no), getPri(now_a,right, no), getPri(now_a,left, no)
		savP = [upp, downp, rightp, leftp]
		savP.sort()
		i = 3
		max=now_pri
		mark=0
		while 1:
			if(savP[i]==1.0):
				i-=1
			elif(savP[i]==now_pri):
				i-=1
			else:
				if(savP[i]==rightp and right!=pre_b and now_b!=INDEX-1 and savehistory(cnt,now_a,right,save_a,save_b)):
					save_a.append(now_a)
					save_b.append(right)
					pre_a, pre_b = now_a, now_b
					now_b = right
					cnt = cnt + 1
					break
				if(savP[i]==downp and down!=pre_a and now_a!=INDEX-1 and savehistory(cnt,down,now_b,save_a,save_b)):
					save_a.append(down)
					save_b.append(now_b)
					pre_a, pre_b = now_a, now_b
					now_a = down
					cnt = cnt + 1
					break
				if(savP[i]==leftp and left!=pre_b and savehistory(cnt,now_a,left,save_a,save_b)):
					save_a.append(now_a)
					save_b.append(left)
					pre_a, pre_b = now_a, now_b
					now_b = left
					cnt = cnt + 1
					break
				if(savP[i]==upp and up!=pre_a and savehistory(cnt,up,now_b,save_a,save_b)):
					save_a.append(up)
					save_b.append(now_b)
					pre_a, pre_b = now_a, now_b
					now_a = up
					cnt = cnt + 1
					break
			i-=1
			
			if(i < 0):
				mark=1
				break
			
			if (((now_a == 4) and (now_b == 4)) or ( cnt > 50 )):
				mark = 1
				break
			
		if(mark==1):
			break
		
	f2 = open('csv_file/FindRoute/FindRoute'+str(no)+'.csv','w')
	for a in range(cnt):
		f2.write(str(save_a[a])+',')
	f2.write('\n')
	for a in range(cnt):
		f2.write(str(save_b[a])+',')
	f2.close()

def FindRouteBack( INDEX, no ):	
	#Starting Value
	now_a, now_b, pre_a, pre_b, cnt = 4, 4, 5, 5, 1
	#Save Point
	save_a, save_b = [now_a], [now_b]

	while cnt <= 50:
		print('cnt:'+str(cnt),end='')
		print('['+str(now_a)+','+str(now_b)+']')
		#Chooser List
		up, down, right, left = getUpPos(now_a), getDownPos(now_a,INDEX), getRightPos(now_b,INDEX), getLeftPos(now_b)
		upp, downp, rightp, leftp = getPri(up, now_b, no), getPri(down, now_b, no), getPri(now_a,right, no), getPri(now_a,left, no)
		savP = [upp, downp, rightp, leftp]
		now_pri = getPri(now_a, now_b, no)
		savP.sort()
		i = 3
		max=now_pri
		mark=0
		while 1:
			if(savP[i]==1.0):
				i-=1
			elif(savP[i]==now_pri):
				i-=1
			else:
				if(savP[i]==rightp and right!=pre_b and now_b!=INDEX-1 and savehistory(cnt,now_a,right,save_a,save_b)):
					save_a.append(now_a)
					save_b.append(right)
					pre_a, pre_b = now_a, now_b
					now_b = right
					cnt = cnt + 1
					break
				if(savP[i]==downp and down!=pre_a and now_a!=INDEX-1 and savehistory(cnt,down,now_b,save_a,save_b)):
					save_a.append(down)
					save_b.append(now_b)
					pre_a, pre_b = now_a, now_b
					now_a = down
					cnt = cnt + 1
					break
				if(savP[i]==leftp and left!=pre_b and savehistory(cnt,now_a,left,save_a,save_b)):
					save_a.append(now_a)
					save_b.append(left)
					pre_a, pre_b = now_a, now_b
					now_b = left
					cnt = cnt + 1
					break
				if(savP[i]==upp and up!=pre_a and savehistory(cnt,up,now_b,save_a,save_b)):
					save_a.append(up)
					save_b.append(now_b)
					pre_a, pre_b = now_a, now_b
					now_a = up
					cnt = cnt + 1
					break
				i = i - 1
			if(i < 0):
				mark=1
				break
			
			if (((now_a == 0) and (now_b == 0)) or ( cnt > 50 )):
				mark = 1
				break
		if(mark==1):
			break
	
	f2 = open('csv_file/FindRoute/FindRoute'+str(no)+'.csv','w')
	for a in range(cnt):
		f2.write(str(save_a[a])+',')
	f2.write('\n')
	for a in range(cnt):
		f2.write(str(save_b[a])+',')
	f2.close()
	
def FindRouteBack2( INDEX, no ):	
	#Starting Value
	now_a, now_b, pre_a, pre_b, cnt = 4, 4, 5, 5, 1
	now_pri = getPri(now_a, now_b)
	#Save Point
	save_a, save_b, save_pri = [now_a], [now_b], [now_pri]

	while cnt <= 50:
		print('cnt:'+str(cnt),end='')
		print('['+str(now_a)+','+str(now_b)+']')
		#Chooser List
		up, down, right, left = getUpPos(now_a), getDownPos(now_a,INDEX), getRightPos(now_b,INDEX), getLeftPos(now_b)
		upp, downp, rightp, leftp = getPri(up, now_b), getPri(down, now_b), getPri(now_a,right), getPri(now_a,left)
		savP = [upp, downp, rightp, leftp]
		savP.sort()
		i = 3
		max=now_pri
		mark=0
		while 1:
			if(savP[i]==rightp and right!=pre_b and now_b!=INDEX-1 and savehistory(cnt,now_a,right,save_a,save_b)):
				save_pri.append(rightp)
				save_a.append(now_a)
				save_b.append(right)
				pre_a, pre_b = now_a, now_b
				now_b = right
				cnt = cnt + 1
				break
			if(savP[i]==downp and down!=pre_a and now_a!=INDEX-1 and savehistory(cnt,down,now_b,save_a,save_b)):
				save_pri.append(downp)
				save_a.append(down)
				save_b.append(now_b)
				pre_a, pre_b = now_a, now_b
				now_a = down
				cnt = cnt + 1
				break
			if(savP[i]==leftp and left!=pre_b and savehistory(cnt,now_a,left,save_a,save_b)):
				save_pri.append(leftp)
				save_a.append(now_a)
				save_b.append(left)
				pre_a, pre_b = now_a, now_b
				now_b = left
				cnt = cnt + 1
				break
			if(savP[i]==upp and up!=pre_a and savehistory(cnt,up,now_b,save_a,save_b)):
				save_pri.append(upp)
				save_a.append(up)
				save_b.append(now_b)
				pre_a, pre_b = now_a, now_b
				now_a = up
				cnt = cnt + 1
				break
			i = i - 1
			if(i < 0):
				mark=1
				break
			
			if (((now_a == 0) and (now_b == 0)) or ( cnt > 50 )):
				mark = 1
				break
		if(mark==1):
			break
	
	f2 = open('csv_file/FindRoute/FindRoute'+str(no)+'.csv','w')
	for a in range(cnt):
		f2.write(str(save_a[a])+',')
	f2.write('\n')
	for a in range(cnt):
		f2.write(str(save_b[a])+',')
	f2.close()
	
if __name__=='__main__':
	no = 5
	FindRoute(5,no)
	#FindRouteBack(5,no)
	#FindRouteBack2(5,3)
