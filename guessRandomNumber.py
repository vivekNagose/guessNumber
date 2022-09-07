import random
n=100
RandomGuess = int(n*random.random())+1
MyGuess=0
while MyGuess!= RandomGuess:
    MyGuess=int(input("New Number "))
    if MyGuess>0:
        if MyGuess>RandomGuess:
            print("Number is large")
        elif MyGuess<RandomGuess:
            print('Number is small')
    else:
        print('lost')
else:
    print ("Congrats")