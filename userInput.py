#this script gets the coordinates from the user and verifies their quality.

def input():
	print "Welcome to the 3D map simulator.  In a momment, you will be prompted to input 4 latatudinal and longitudinal coordinates.  For this application to function, those coordinates must not form a shape larger than __________ square miles/feet(?).  Also the coordinates that you input MUST(!!!!!!!!) form a square.  If the coordinates do not form a square, then you will be given an error. If you are ready to begin, please press Y."
	if input() == 'Y' | 'y':
		getCoor()
	else:
		input()
		
def getCoor():
	latNW = getlatNW()  #x1
	longNW = getlongNW() #y1
	latNE = getlatNE() #x2
	longNE = getlongNE() #y2
	latSW = getlatSW() #x3
	longSW = getlongSW() #y3
	latSE = getlatSE() #x4
	longSE = getlongSE() #y4
	if (latNE-latNW)-(longNE-longNW) == (
	
#     (x1,y1)-------(x2,y2)
#		|			  |
#		|			  |
#		|			  |
#		|			  |
#		|			  |
#		|			  |
#	  (x3,y3)------(x4,y4)

def getlatNW():
	print "Please input the latitude of the top left (i.e. northwestern most) coordinate."
	latNW = input()
	if 90 >= latNW >= -90:
		print "Valid input"
		return latNW
	else:
		print "Bad input"
		latNW = 0
		getCoor()
		
def getlongNW():
	print "Please input the longitude of the top left (i.e. northwestern most) coordinate."
	longNW = input()
	if 90 >= longNW >= -90:
		print "Valid input"
		return longNW
	else:
		print "Bad input"
		longNW = 0
		getCoor()
		
def getlatNE():
	print "Please input the latitude of the top right (i.e. northeastern most) coordinate."
	latNE = input()
	if 90 >= latNE >= -90:
		print "Valid input"
		return latNE
	else:
		print "Bad input"
		latNE = 0
		getCoor()
		
def getlongNE():
	print "Please input the longitude of the top right (i.e. northeastern most) coordinate."
	longNE = input()
	if 90 >= longNE >= -90:
		print "Valid input"
		return latNE
	else:
		print "Bad input"
		longNE = 0
		getCoor()

def getlatSW():
	print "Please input the latitude of the bottom left (i.e. southwestern most) coordinate."
	latSW = input()
	if 90 >= latSW>= -90:
		print "Valid input"
		return latSW

	else:
		print "Bad input"
		latSW = 0
		getCoor()

def getlongSW():
	print "Please input the longitude of the top left (i.e. southwestern most) coordinate."
	longSW = input()
	if 90 >= longSW >= -90:
		print "Valid input"
		return longSW
	else:
		print "Bad input"
		longSW = 0
		getCoor()
		
def getlatSE():
	print "Please input the latitude of the top left (i.e. southeastern most) coordinate."
	latSE = input()
	if 90 >= latSE >= -90:
		print "Valid input"
		return latSE
	else:
		print "Bad input"
		latSE = 0
		getCoor()

def getlongSE()	:
	print "Please input the longitude of the top left (i.e. northwestern most) coordinate."
	longSE = input()
	if 90 >= longSE >= -90:
		print "Valid input"
		return latSE
	else:
		print "Bad input"
		longSE = 0
		getCoor() 
