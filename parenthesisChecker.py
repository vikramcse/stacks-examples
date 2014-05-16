from stack import Stack

def parenChecker(sequence):
	s = Stack()
	balenced = True
	index = 0

	while index < len(sequence) and balenced:
		symbol  = sequence[index]

		if symbol in "{[(":
			s.push(symbol)
		else:
			if s.isEmpty():
				balenced = False
			else:
				top = s.pop()
				if not matches(symbol, top):
					balenced = False
		index = index + 1

	if balenced and s.isEmpty():
		return True
	else:
		return False


def matches(symbol, top):
	opens = "({["
	closes = ")}]"
	return opens.index(top) == closes.index(symbol)
		

print (parenChecker('{[]}'))
print (parenChecker('{{([][])}()}'))
