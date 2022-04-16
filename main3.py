import MakePri as MP
#import MakeRate as MR 
#import MainThread as MT
#import LoadMap as LM
import FindRoute as FR
import HelpCount as HC

INDEX = 5					#Area point include point A and B in rows
point_distance = 5 		#Between A and B (km)
speed = 50 					#UAV flight speed between each point(km/h)
AREA_MAX = 2000		#Max evacuers in Area
#Amount = 2000
#starting value
no = 1
while no <= 10:
	MP.MakePri(INDEX,point_distance,speed,no)
	FR.FindRoute(INDEX, no)
	HC.HelpCount(INDEX, AREA_MAX, no)
	no = no + 1
#MT.MThread(INDEX,AREA_MAX)
#LM.LoadMap(INDEX)
