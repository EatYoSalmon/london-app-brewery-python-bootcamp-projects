#Write your code below this line 👇

def prime_checker(number):

    primeIs = True
    loopOver = False

    while loopOver == False:

        for i in range(2, number):
            if number % i == 0:
                primeIs = False
                loopOver = True

        loopOver = True
    
    if primeIs:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
