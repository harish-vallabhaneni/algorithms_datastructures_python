from ds import Stack

def balancedparantheses(parantheses_string):
	s = Stack()
	balanced = True
	index = 0
	while index < len(parantheses_string) and balanced:
		symbol = parantheses_string[index]
		if symbol == "(":
			s.push(symbol)
		elif s.isEmpty():
			balanced = False
		else:
			s.pop()
		index += 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

if __name__ == '__main__':
	print(balancedparantheses("((()))"))
	print(balancedparantheses("{{{}}}}"))
