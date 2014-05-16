from stack import Stack

def infix_to_postfix(infixexpr):
	precedence_values = {
		"*" : 3,
		"/" : 3,
		"+" : 2,
		"-" : 2,
		"(" : 1
	}

	output_stack = Stack()
	tokenList = infixexpr.split()
	postfix_expr = []
	
	for token in tokenList:
		if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
			postfix_expr.append(token)

		elif token == "(":
			output_stack.push(token)

		elif token == ")":
			top_token = output_stack.pop()

			while top_token != "(":
				postfix_expr.append(top_token)
				top_token = output_stack.pop()
		else:
			# if the precedence of top operator in stack is greater than current token then remove 
			# the element from stack and add into postfix array
			while (not output_stack.isEmpty()) and (precedence_values[output_stack.peek()] >= precedence_values[token]):
				postfix_expr.append(output_stack.pop())
			output_stack.push(token)
			
	while not output_stack.isEmpty():
		postfix_expr.append(output_stack.pop())

	return " " .join(postfix_expr)   


print(infix_to_postfix( "( A + B ) * ( ( C * D ) / ( K - M ) + ( T * G ) )" ))