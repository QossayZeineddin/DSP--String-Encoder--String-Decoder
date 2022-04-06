def read_chars():
	chars = {}
	chars_file = open('chars.txt', "r+")
	for i in range(0, 53):
		line = chars_file.readline()
		char = line.split(' ')
		# print(int(char[1]) + int(char[1])+int(char[3]))
		chars[char[0]] = {'char': char[0],'typeOfChar': int(char[1]), 'low': int(char[2]), 'middle': int(char[3]), 'high': int(char[4])}
		#print(char[0] + char[1] +char[2] +  char[3] + char[4])
	chars[' '] = chars.pop('space')
	chars[' ']['char'] = ' '
	return chars
