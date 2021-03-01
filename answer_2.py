def unitCharacterValue(character):
	return ord(character)-65
def stringEvaluate(the_string):
	output_number=unitCharacterValue(the_string[-1])
	the_string=the_string[:-1]
	the_string=the_string[::-1]

	for x in range(len(the_string)):
		output_number+=(len(the_string[x:])*27)+unitCharacterValue(the_string[x])
		print(len(the_string[x:])*26,unitCharacterValue(the_string[x]))
	return output_number
if __name__ == '__main__':
	print(stringEvaluate('AAA'))

