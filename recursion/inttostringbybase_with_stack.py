from stack import Stack

s = Stack()

def tostrbybase(n, base):
	convstring = '0123456789ABCEDF'
	result = '' 

	while n > 0:
		if n < base:
			s.push(convstring[n])
		else:
			s.push(convstring[n%base])
		n = n//base

	while not s.isEmpty():
		result = result + s.pop()
	return result

if __name__ == '__main__':
	print(tostrbybase(123, 10))
	print(tostrbybase(123, 16))
