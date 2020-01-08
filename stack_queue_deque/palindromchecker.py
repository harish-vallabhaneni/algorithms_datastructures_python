from ds import Deque

def palindromechecker(palindromestring):
	deque = Deque()
	
	for ch in palindromestring:
		deque.addRear(ch)

	while deque.size() > 1:
		size = len(palindromestring)
		if deque.removeFront() == deque.removeRear():
			continue
		else:
			return "{} is not a palindrome".format(palindromestring)
	if deque.size() <= 1:
		return "{} is a palindrome".format(palindromestring)

if __name__ == '__main__':
	print(palindromechecker('radar'))
	print(palindromechecker('hello'))
