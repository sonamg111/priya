tem = int(raw_input("Enter the tempreter"))
if tem < 0:
	print ("Freezing weather")
elif tem <= 10:
	print ("very cold weather")
elif (tem >= 10) and (tem <= 20):
	print ("cold weather")
elif (tem >= 20) and (tem <= 30):
	print ("Normal weather")
elif (tem >= 30) and (tem <= 40):
	print ("it's hot")
else:
	print ("it is very hot")
