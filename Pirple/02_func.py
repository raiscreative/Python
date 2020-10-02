'''
This is about a song,
 but is also about learning variables.
'''

Genre = 'Psychedelic rock' #String
Artist = 'The Doors'
Album = 'Strange Days'
ReleaseYear = 1967 #Integer
Released = 'September'  
Recorded = 'May-August'
BillboardPosition = 12
DurationInSeconds = 132.0 #Float
Songwriter1, Songwriter2 = 'Jim Morrison', 'Robbie Krieger'

'''
And now we get to functions
'''

def GenreFunction():
    print(Genre)
    return Genre

def ArtistFunction():
    print(Artist)
    return Artist

def Year():
    print(ReleaseYear)
    return ReleaseYear

def Fav():
    print(True)
    return True

GenreFunction()

ArtistFunction()

Year()

Fav()