from stack import Stack

def decimal_to_binary(number):
	remainder = Stack()

	while number > 0:
		rem = number % 2
		remainder.push(rem)
		number = number // 2

	binary_string = ""	
	while not remainder.isEmpty():
		binary_string = binary_string + str(remainder.pop())	

	return binary_string

print(decimal_to_binary(223))
