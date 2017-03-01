'''Write a Python program to print numbers from 1 to 100 except for multiples of 3 for which you should print "fuzz" instead, for multiples of 5 you should print 'buzz' instead and for multiples of both 3 and 5, you should print 'fuzzbuzz' instead.'''

for i in range(1,101):
    if (i%3 == 0):
        print ("Fuzz")
    elif (i%5 ==0):
        print ("Buzz")
    elif (i%3 ==0 and i%5 == 0):
        print ("FizzBuzz")
    else:
        print (i)
