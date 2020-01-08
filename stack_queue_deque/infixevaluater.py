from ds import Stack

#order of precedence is - PEMDAS - parantheses, exponential, multiplication and division in left to right order, addition and subraction in left to right order


def infixtoprefixconverter(expression):
#get the expression and evaluate for order of precedence first in infix
#have the order of precedence evaluated on each value as you go through the expression and convert it to prefix accordingly
	open_parantheses = '('
	close_parantheses = ')'
	exponential = '**'
	multiplicaiton = '*'
	division = '/'
	addition = '+'
	subraction = '-'
	index = 0
	operators = ['(',')','**','*','/','+','-']
	infixbuilder = ''
	for i in expression:
		if not i in operators:
			infixbuilder = infixbuilder + '(' + str(i)
			infixbuilder = infixbuilder + str(i)
		



A+B*C -> (A+(B*C))
			
				
		

if __name__ == '__main__':
	print(infixtoprefixconverter("( A + B ) * ( C + D )"))

