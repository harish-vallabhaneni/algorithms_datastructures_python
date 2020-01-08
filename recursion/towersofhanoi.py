def towers(height, frm, to, spare):
	if height == 1:
		movedisk(frm,to)
	else:
		towers(height-1,frm, spare, to)
		towers(1, frm, to, spare)
		towers(height-1, spare, to, frm)

def movedisk(frm, to):
	print('moving disk from '+frm+' to '+to)

if __name__ == '__main__':
	towers(3,'a', 'b', 'c')
