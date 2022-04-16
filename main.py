import MakePri as MP
import FindRoute as FR
import HelpCount as HC
import FinalResult as FinR

MAX_AREA_POINT = 22	#Count of Area points in the map
point_distance = 5	#Between S1 and S2 (km)
speed = 50		#(km/h)
AREA_MAX = 50		#Max evacuers in 1 AREA_POINT

#starting value
no = 1
while no <= 10:
　　print("# UAV-1 CONTROLL STEP." + str(no) + " #")
　　MP.MakePri2(MAX_AREA_POINT, speed, no)
　　if(no % 2 == 0):
　　　　FR.FindRouteBack(MAX_AREA_POINT, no)
　　　　HC.HelpCount2(MAX_AREA_POINT, AREA_MAX, no)
　　else:
　　　　FR.FindRoute(MAX_AREA_POINT, no)
　　　　HC.HelpCount(MAX_AREA_POINT, AREA_MAX, no)
　　no = no + 1

FinR.FinalResult(MAX_AREA_POINT, no - 1, AREA_MAX)
