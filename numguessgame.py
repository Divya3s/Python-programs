import random
import math

lower = int(input("Set smallest number:- "))
upper = int(input("Set biggest number:- "))

# generating random number between the lower and upper
x = random.randint(lower, upper)

print( "\n\tYou have only", round(math.log(upper - lower + 1, 2)), "chances to guess the number!\n" )


count = 0
while count < math.log(upper - lower + 1, 2):
    count += 1
    
    guess = int(input("Guess a number:- "))
    
    if x == guess:
        print("congratulations you guessed the number correctly in", count , " try")
        break
    elif x > guess:
        print("you guessed smaller number.")
        
    elif x < guess:
        print("you guessed larger number.")
        
        
if count >= math.log(upper - lower + 1, 2):
    print("\nThe number is %d" % x)
    print("\tBetter luck next time!")
    
    
