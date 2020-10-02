maxW = 80
maxH = 60

def boardFunc(rows, columns):
    if rows <= maxW and columns <= maxH:
        for row in range(rows*2 -1):
            if row % 2 == 0:
                for column in range(1, columns*2):
                    if column % 2 == 1:
                        if column != columns*2 -1:
                            print(' ', end='')
                        else:
                            print('')
                    else:
                        print('|', end='')
            else:
                print('-' * (columns*2 -1))
	
        print('Your board is ready.')
        return True
    else:
    	print('Your board could not be built. Sorry.')
    	return False

	

try:
	rows = int(input('Enter the number of rows: '))
except:
	print('Please enter a valid number.')
	rows = int(input('Enter the number of rows: '))

try:
	columns = int(input('Enter the number of columns: '))
except:
	print('Please enter a valid number.')
	columns = int(input('Enter the number of columns: '))


boardFunc(rows, columns)