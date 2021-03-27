#Check kth bit set ot not using left shift
#Create a pesudo bit 1 and shift the pesudo bit upto k-1 position to left using left shift
#Peform an AND position with n 
#If the bit at kth position is set then the kth bit will remain 1 after AND operation or it will be 0 if not set bit
#Time complexity is O(1)

#Function will take 2 argument, n = number and k = kth postion
def check_bit(n,k):
    #temp is pseduo bit
    temp = 1
    #Shifting the 1 to k-1 postion
    temp = temp<<k-1
    #Checking if the AND operation gives 0 or not
    #If after AND operation its not 0 then its a set bit at kth postion
    if n&temp != 0:
        return "Set Bit"
    #Else not set bit at kth position
    else:
        return "Not Set Bit"

#For input
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(check_bit(n,k))
else:
    print("Error")
