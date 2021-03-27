#Check kth bit set or not using right shift
#First we will right shift the n to kth postion
#Then we will perform AND operation with 1 
#If the kth postion is set bit then it will return a non zero number else if its not set bit then it will return 0
#Time complexity is O(1)

#Function takes 2 argument i.e n = number and k = kth position
def check_bit(n,k):
    #Shifting the n to kth postion using right shift
    n = n>>k-1
    #Checking if the AND operation will give a 0 at set bit postion or not
    #If its a set bit then it will return a non zero number
    if n&1 != 0:
        return "Set Bit"
    #Else it will return 0
    else:
        return "Not Set Bit"

#For input
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(check_bit(n,k))
else:
    print("Error")
