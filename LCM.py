#LCM of two given number
#In this algorithm we will first find the gcd of two number
#Then we will use this formula to find the lcm i.e LCM*GCD = a*b => LCM = (a*b)/GCD
#Here a is the first number and b is the second number.
#This Algorithm will take O(log(max(a,b))) time

#To get the floor value of the LCM
import math
#Function takes two argument i.e a = 1st number and b = 2nd number
def GCD(a,b):
    #Checking if the value of value of b is 0 or not
    #If b is 0 then we can say we have reduced the number such that its our GCD
    if b == 0:
        return a
    #If b is not 0 then keep on reducing b and storing the largest value at a postion
    else:
        #Recursing the function and send b in place of a position and sending the remainder in place of b postion
        return GCD(b,a%b)

#For Input
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    #After the execution of given function, we will use this formula LCM = (a*b)/GCD
    print(math.floor((a*b)/GCD(a,b)))
else:
    print("error")
