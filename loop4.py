x=1
while x<=100:
	if x%3==0:
		print "Nav"
	if x%7==0:
		print "Gurukul"
	if (x%3==0) and (x%7==0):
			print "Navgurukul"
	else:
			print x
             x=x+1