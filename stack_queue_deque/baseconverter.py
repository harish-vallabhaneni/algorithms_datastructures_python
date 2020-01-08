from ds import Stack

def baseconverter(number, base):
	s = Stack()
	number_string = '0123456789ABCDEF'

	while number > 0:
		remainder = number%base
		s.push(remainder)
		number = number//base

	base_builder = ''
	while not s.isEmpty():
		base_builder = base_builder + str(number_string[s.pop()])

	return base_builder

if __name__ == '__main__':
	print(baseconverter(233, 2))
	print(baseconverter(25,8))
	print(baseconverter(256,16))
	print(baseconverter(26,26))	
