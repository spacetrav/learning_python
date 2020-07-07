from random import randint
import math

def truncate(n):
    return int(n*1)/1

ones = []
twos = []
rolls = 1000000

for n in range(1,rolls+1):
    x = randint(1,2)

    if x == 1:
        ones.append(x)
    else:
        twos.append(x)

rand_stat_error = truncate(math.sqrt(rolls))
difference = abs(len(ones) - rolls/2)

print("Number of heads flipped: " + str(len(ones)))
print("Number of tails flipped: " + str(len(twos)))

if difference > rand_stat_error:
    print("The difference is: " + str(difference) + ", which deviates outside of the standard error of " + str(rand_stat_error))
else:
    print("The difference is: " + str(difference) + ", which is inside the standard error of " + str(rand_stat_error))
