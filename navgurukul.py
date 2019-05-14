i = 0
while(i <= 100):
    if (i % 3 == 0) and (i % 7 == 0):
        print("Navgurukul")
    elif i % 3 == 0:
        print("Nav")
    elif i % 7 == 0:
        print("gurukul")
    else:
        print(i)
    i=i+1
print ("Done!")