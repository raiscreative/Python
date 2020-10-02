for n in range(1, 101):
    
    if n%3 == 0 and n%5 == 0: 
        print('FizzBuzz')
    elif n%3 == 0:
        print('Fizz')
    elif n%5 == 0:
        print('Buzz')
    else:
        if n == 1: print(n)
        else:
            for i in range(2,n):
                if n%i == 0: 
                    print(n)
                    break
            else: print('prime')
                

       
