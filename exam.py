a=int(raw_input("Enter the number"))
b=int(raw_input("Enter the number"))
c=int(raw_input("Enter the number"))
if a > b:
	if a < c:
	    print a
	elif b > a:
	    print b	
	else:
	    print c
else:
	if a > c:
	    print a
	elif b < c:
	    print b
	else:
	    print c
	
print c

 