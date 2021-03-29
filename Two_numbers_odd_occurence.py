#Two numbers having odd occurrences in an array
#In this method we will use XOR operation and AND operation
#We will peform a XOR in the entire array, then again iterate through the same array by checking,
#If the resultant XOR rightmost bit matches the current element bit or not,
#If its matches then we will perform a XOR operation until one number remaining
#Same for non-matching bit number 
#Time complexity is O(n), Auxilary space required is O(1)

#This function take only one argument i.e arr = array
def find_two(arr):
    #To store total xor after iterating
    xorTotal = 0
    #Iterating through the array while perforimg XOR operation
    for i in arr:
        xorTotal = xorTotal^i
    #To store the first number and second number respectively
    first,second = 0,0
    #Iterating through the array again
    for i in arr:
        #If the rightmost set bit is same in the element or not
        if i&(i-1) != 0:
            #Performing XOR with each element with same setbit at that position
            first = first^i
        else:
            #Performing XOR with each element with non same setbit at that position
            second = second^i
    #Return the numbers
    return first,second

#For input
if __name__ == "__main__":
    arr = [1,2,2,3,1,4,5,5,8,4]
    print(find_two(arr))
else:
    print("Error")