# This code encapsulates a markov model of a tennis game



def initp(p):

	num = p*p
	denom = 1.0-2.0*p*(1-p)
	tie = num/denom

	ps = [[0 for x in range(0,5)] for y in range(0,5)]
	ps[2][2] = tie
	ps[0][0] = getp(0,0,ps,p)
	return(ps)

def getp(a,b,ps,p):

	# base cases
	if (a == 4):
		return 1.0
	if (b == 4):
		return 0.0

	# check if we've already calculated it
	if (not(ps[a][b] == 0)):
		return ps[a][b]

	# transition cases
	win = 0.0
	lose = 0.0	

	# won the point
	if(checkTie(a+1,b)):
		win = ps[2][2]
	else:
		ps[a+1][b] = getp(a+1,b,ps,p)
		win = ps[a+1][b]
	
	# lost the point
	if(checkTie(a,b+1)):
		lose = ps[2][2]
	else:
		ps[a][b+1] = getp(a,b+1,ps,p)
		lose = ps[a][b+1]

	return(p*win+(1-p)*lose)

def checkTie(a,b):
	if (a==2 and b==2):
		return 1
	if (a==3 and b==3):
		return 1
	else:
		return 0
