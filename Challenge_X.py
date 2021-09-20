# Challenge X - Integer Fizz Buzz

x = int(input("Enter a number: "))

if (x%3==0):
    print("{} is divisible by 3 >> Fizz".format(x))
else:
    print("{} is not divisible by 3".format(x))

# Integer is multiple of 5
def isMultipleof5(x):

    while ( x > 0 ):
        x = x - 5

    if ( x == 0 ):
        return 1
    return 0

if (isMultipleof5(x) == 1 ):
    print (x, "is multiple of 5 >> Buzz")
else:
    print (x, "is not a multiple of 5")

if (x%3==0) and (isMultipleof5(x) == 1 ):
    print ("FizzBuzz!")
else:
    print("X")
