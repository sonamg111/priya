user_input = input("Enter any number")
i = 2
while i < user_input:
	if user_input % i == 0:
		print ("It is not a prime number")
		break
 	else:
		print ("It is a prime number")
		break
	i=i+1