from ds import Stack

def balancedsymbols(symbol_string):
	s = Stack()
	balanced = True
	index = 0
	lastopensymbol = ''
	while index < len(symbol_string) and balanced:
		symbol = symbol_string[index]
		lastopensymbol = s.peek()
		if symbol in "({[":
			s.push(symbol)
		elif s.isEmpty():
			balanced = False
		else:
			balanced = symbolchecker(lastopensymbol, symbol)
			if balanced:
				s.pop()

		index += 1

	if balanced and s.isEmpty():
		return True
	else:
		return False

def symbolchecker(opensymbol, closesymbol):
	startsymbols = "({["
	closesymbols = ")}]"
	if startsymbols.index(opensymbol) == closesymbols.index(closesymbol):
		return True
	else:
		return False

if __name__ == '__main__':
	print(balancedsymbols("({[]})"))
	print(balancedsymbols("({[})"))
