from os import walk



def find_duplicates():
	contents={}
	for filenumber in range(0,100):
		file=open(f'data/{filenumber}.txt','r')
		content=file.read()
		try:
		 contents[content].append(filenumber)
		except KeyError:
			contents[content]=[filenumber]

	
	return [contents[x] for x in contents.keys()]
	# return [[0, 2, 7], [1, 5, 9], [3, 6], [4, 8]]

if __name__ == '__main__':
    result = find_duplicates()
    for row in result:
        print(" ".join(str(i) for i in row))
