


Song = {'Genre': 'Psychedelic rock', 'Artist': 'The Doors', 'Album': 'Strange Days', 'Release Year': '1967', 'Released': 'September', 'Recorded': 'May-August', 'BillboardPosition': '12', 'DurationInSeconds': '132', 'Songwriter1': 'Jim Morrison', 'Songwriter2': 'Robbie Krieger'}

for element in Song:
	print(element, ': ', Song[element])


def guessingFunc():
	key = input('What will you try to guess?\n')
	if key not in Song:
		print("Sorry. There's nothing to guess there.")
		return False
	else:
		value = Song[key]
		guess = input('What is your guess?\n')
		if guess == value:
			print('Good work. You guessed correctly.')
			return True
		else: 
			print('Sorry. You did not guess correctly.')
			return False


guessingFunc()




