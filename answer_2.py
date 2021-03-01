def unitCharacterValue(character):
	return ord(character)-65
def stringEvaluate(the_string):
	output_number=unitCharacterValue(the_string[-1])
	the_string=the_string[:-1]
	the_string=the_string[::-1]

	for x in range(len(the_string)):
		placevalue=(len(the_string[x:])*27)*(unitCharacterValue(the_string[x])+1)
		output_number+=placevalue
	return output_number
if __name__ == '__main__':
	print(stringEvaluate('ABA'))

