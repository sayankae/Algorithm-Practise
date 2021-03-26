#Check if a given number is prime of not
#With normal approach the time taken will O(n) time
#So, after some observation we can see that n does not need checked till the n-1
#The loop can be run till square root of n because if the any number does not divide the n/2 then it cannot divide n too
#This Algorithm takes O(sqrt(n)) time and O(1) Auxilary Space

#Using math library to find the square root of n
import math

#Function takes one argument i.e the number
def check_Prime(n):
    #If the number is 1 then it is not prime and simply return false
    if n == 1:
        return False
    i = 2
    #Starting the loop from 2 and running till square root of n
    while i<math.sqrt(n):
        #If any number divides n properly then we will say it is not Prime
        if n%i == 0:
            return False
        #Else we keep on checking till square root of n
        else:
            i = i+1
    #If the above loop does not return False then the number must be a Prime Number
    #Returning True
    return True

#main funtion
if __name__ == "__main__":
    num = int(input())
    if (check_Prime(num) == True):
        print("Prime")
    else:
        print("Not Prime")
else:
    print("Error")
