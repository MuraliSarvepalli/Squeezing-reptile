import random
count=0
num=random.randint(0,100)
#print(num)
lst=[]
while True:
    guesss=input("Guess it")
    guess=int(guesss)
    count=count+1
    if guess==num:
            print('Congrats!!!The guess is correct')
            print('The number of guesses is {}'.format(count))
            break
    if guess<1 and guess>100:
        print('OUT OF BOUNDS')
    while count==1:
        if guess-num in range(-10,10):
            print('WARM')
        else :
            print('COLD')
        break
    lst.append(guess)
    if len(lst)>1:
        if abs(num-lst[-1])<abs(num-lst[-2]):
                     print("WARMER")
        else:
                     print("COLDER")
