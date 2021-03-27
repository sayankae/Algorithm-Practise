#Count Set Bits using simple method
#Right Shifting the bit till log time
#By using & checking if the last bit is 0 or 1
#If its 0 then not a set bit and dont increment the count else increment the count if its a set bit
#Time complexity O(log)

#Function is taking 1 argument i.e n
def count_set_bit(n):
    #Setting count to 0
    count = 0
    #Running loop until n is greater than 0
    while n>0:
        #Checking if n&1 is 0 or not
        if n&1 != 0:
            #If not 0 then increment the count
            count = count+1
        #Right shift the number
        n = n>>1
    #Return the count
    return count

#For input
if __name__ == "__main__":
    n = int(input())
    print(count_set_bit(n))
else:
    print("Error")