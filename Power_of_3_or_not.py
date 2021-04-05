#Check an Integer is power of 3 or not 
#In this approach we wil use this formula to find whether its power of 3 or not:
#i.e (log10(n)/log10(3))%1 == 0 then its a power of 3
#Time complexity is O(1) and Auxilary Space is O(1)

import math
#This Function takes 1 argument i.e the n = number
def checkPow(n):
    #To store the value of (log10(n)/log10(3))%1
    a = (math.log10(n)/math.log10(3))%1
    #Check if the number floor value is 0 or not
    if a == 0:
        return True
    else:
        return False
#For input
if __name__ == "__main__":
    n = int(input())
    print(checkPow(n))
else:
    print("Error")
