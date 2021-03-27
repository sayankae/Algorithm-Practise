#Set the bit at kth postion
#In this approach we will simply shift our psuedo bit to kth-1 position
#Then we will perfrom a OR operation with n, to set bit we perform OR operation with 1
#Time complexity is O(1)

#This function takes 2 argument, n = number and k = position to set bit at
def set_bit(n,k):
    #temp is our pesudo 1 bit
    temp = 1
    #Changing the postion of 1 to the kth bit
    temp = temp<<k-1
    #Perform the OR operation with n 
    n = n|temp
    #Returning the temp
    return n

#For input
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(set_bit(n,k))
else:
    print("Error")
