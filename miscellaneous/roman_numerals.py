def function(input):  # what's the goal? should name the function that
	if not isinstance(input, int):
		raise TypeError('expected integer, got %s' % type(input))
	if not 0 < input <= 10:
		raise ValueError('argument must be between 1 and 10')
		
	input = int(input)
	integers = (1,2,3,4,5,6,7,8,9,10)
	numerals = ('I','II','III','IV','V','VI','VII','VIII','IX','X')
	result = ''
	
	for i in range(len(integers)):
		count = input / integers[i] # first iteration always resolves to input
		# (string * integer) will replicate the string that many times
		# i.e. 'IV' * 5 = 'IVIVIVIVIV'
		# result += numerals[i] * count # python 2.7
		result += numerals[i] * int(count) # python 2.7/3.4
		input -= integers[i] * count # first iteration always assigns input = 0
		# iterations after first will never produce results
		# due to 0 / x = 0 and 0 * x = 0
	
	return result
	
	
print(function(10)); # IIIIIIIIII
print(function(5));  # IIIII


# here's my best guess at what the above is attempting to accomplish
# it takes an integer between 1 and 10 and returns its roman numeral equivalent
def int_to_roman(number):
	if not isinstance(number, int):
		raise TypeError('expected integer, received %s' % type(number))
	if not 0 < number <= 10:
		raise ValueError('input value must be between 1 and 10')
	
	numerals = ('I','II','III','IV','V','VI','VII','VIII','IX','X')
	
	return numerals[number - 1]


# this prints the index and the roman numeral equivalent
for i in range(1,10): 
	print(i, int_to_roman(i)) 

# these should print 'ValueError caught'
try:
	print(int_to_roman(0))
except ValueError:
	print('ValueError caught')

try:
	print(int_to_roman(11))
except ValueError:
	print('ValueError caught')

# this should print 'TypeError caught'
try:
	print(int_to_roman('butts'))
except TypeError:
	print('TypeError caught')