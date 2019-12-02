my_input = [ 1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,19,9,23,1,5,23,27,1,27,9,31,1,6,31,35,2,35,9,39,1,39,6,43,2,9,43,47,1,47,6,51,2,51,9,55,1,5,55,59,2,59,6,63,1,9,63,67,1,67,10,71,1,71,13,75,2,13,75,79,1,6,79,83,2,9,83,87,1,87,6,91,2,10,91,95,2,13,95,99,1,9,99,103,1,5,103,107,2,9,107,111,1,111,5,115,1,115,5,119,1,10,119,123,1,13,123,127,1,2,127,131,1,131,13,0,99,2,14,0,0 ]
example = [ 1,9,10,3,2,3,11,0,99,30,40,50 ]
needle = 19690720

ADD = 1
MULTIPLY = 2
STOP = 99

def day_one( data, noun, verb ):
	data[1] = noun
	data[2] = verb

	i = 0
	while( data[i] != STOP ):
		opCode = data[i]
		p1 = data[i+1]
		p2 = data[i+2]
		p3 = data[i+3]
		#print( i, opCode, data )

		if opCode == ADD:
			data[p3] = data[p1] + data[p2]
		elif opCode == MULTIPLY:
			data[p3] = data[p1] * data[p2]
		# else STOP

		i += 4

	#print( i, data[i], data )
	return data[0]

def day_two( data, needle ):
	for noun in range(100):
		for verb in range(100):
			#print( noun, verb )
			if( day_one( data[:], noun, verb ) == needle ):
				return ( noun, verb, 100 * noun + verb )

	print( "Not found:", needle )
	exit( -1 )

print( 'day_one:', day_one( my_input[:], 12, 2 ) )
#print( 'day_two:', day_two( my_input[:], 3409710 ) )
print( 'day_two:', day_two( my_input, needle ) )
