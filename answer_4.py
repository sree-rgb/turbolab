def getList(a):
	number_of_pairs=0
	for x in range(len(a)-1):
		for y in range(x+1,len(a)):
			if (a[x]+a[y])%30 == 0:
				number_of_pairs+=1
	return number_of_pairs 
if __name__ == '__main__':
	print(getList([15,10,75,50,20]))
	print(getList([30,30,30]))