# holds functions for probability of winning tennis match

def match_breaker(p):
	
	# create array for probabilities
	ps = [[0 for x in range(0,4)] for y in range(0,4)]

	ps[0][0] = get_p_breaker(0,0,ps,p)

	return(ps)

def match_no_breaker(p):
	
	# different because fifth set is no longer identical


def get_p_breaker(a,b,ps,p):

	# base cases
	if (a == 3):
		return 1.0
	if (b == 3):
		return 0.0

	# see if we've already calculated it
	if (not(ps[a][b] == 0)):
		return ps[a][b]

	# transition step
	win = get_p_breaker(a+1,b,ps,p)
	lose = get_p_breaker(a,b+1,ps,p)

	ps[a][b] = p*win+(1-p)*lose

	return(ps[a][b])

	
