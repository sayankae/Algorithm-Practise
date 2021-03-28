#Check whether the number is power of 2 or not
#In this algorithm, we will use bitwise property
#We will check each bit of the number whether its 0 or not at places except at last position
#If no bit found at other places except the last postion then its a power of 2
#Time complexity is O(log(n)) and auxilary space required is O(1)

#This Function takes one argumment i.e n = number
def check_pow(n):
    #Running a loop
    #Checking if n is greater than 1 or not
    while n>1:
        #Checking if bit is set bit or not
        if n&1 != 0:
            #If setbit then return False
            return False
        #Right shift the bits of n by 1 position
        n = n>>1
    #If the entire loop executed then its clear that no set bit present at other places except the last one
    #Return True
    return True

#For input
if __name__ == "__main__":
    n = int(input())
    print(check_pow(n))
else:
    print("Error")
