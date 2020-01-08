
def tostrbybase(n, base):
	convstring = '0123456789ABCEDF'

	if n < base:
		return convstring[n]
	else:
		return tostrbybase(n//base, base) + convstring[n%base]

if __name__ == '__main__':
	print(tostrbybase(123, 10))
	print(tostrbybase(123, 16))
