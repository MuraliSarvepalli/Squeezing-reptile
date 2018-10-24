#COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

def prime(a):
    count=0
    flag=0
    for i in range(3,a):
        if (a%i==0):
            pass
        else:
            count=count+1
        return count

a=int(input('Enter the number upto which no of primes need to be known'))
r=prime(a)
print(r)

