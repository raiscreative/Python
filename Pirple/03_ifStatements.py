def NumComp(a, b, c):
    
    
    if a == b == c:
        print('All numbers are equal.')
        return True

    elif a == b: 
        print('First and second numbers are equal.')
        return True
    elif a == c:
        print('First and third numbers are equal.')
        return True
    elif b == c:
        print('Second and third numbers are equal')
        return True
    
    else: 
        print('No numbers are equal.')
        return False

try:
    a = int(input('Insert the first number' ))
except:
    print('That is not a number, please try again')
    a = int(input('Insert the first number'))

try:
    b = int(input('Insert the second number' ))
except:
    print('That is not a number, please try again')
    b = int(input('Insert the second number'))

try:
    c = int(input('Insert the third number' ))
except:
    print('That is not a number, please try again')
    c = int(input('Insert the third number'))   


NumComp(a, b, c)
