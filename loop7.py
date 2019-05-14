user = int(raw_input("Enter your number"))
i = 2
while i < user:
	if user % i == 0:
		print "not a prime number"
		break
	i=i+1
else:
		print "prime number hai"