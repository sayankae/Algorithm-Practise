#Sum of two arrays
#In this problem, digits has been stored inside the array
#We will use a iterative approach, we will start adding from the last index of the arrays
#If the sum is greater than 9 then we ill keep a carry and add to the next index sum
#We will append each sum last digit to the new array to the same index at which we did the sum
#If carry still exist then we will put the carry at 0th position and shift the array
#Time complexity is O(n) and Auxilary space required is O(max(a,b)) here a and b is the size of the array

#Note some edge can create problem i.e if the staring index have 0 or any index have negative numbers

#This function takes 2 argument, i.e a = first array and b = second array
def sumArray(a,b):
    #Auxilary list will be the size of the bigger array
    if len(a)>len(b):
        k = len(a)
    else:
        k = len(b)
    #Creating an empty list of size k
    arr = [0]*k
    #We will store the last index of each array in i,j and k
    i = len(a)-1
    j = len(b)-1
    k = k-1
    #Assume the carry is 0 at initial
    carry = 0
    #We will iterate through the array until the Auxilary list is fully traversed
    while k>-1:
        #When both of the array is not fully traversed
        if i>-1 and j>-1:
            #Adding both the digit and carry
            sum = a[i]+b[j]+carry
            #Storing the first digit at the carry
            carry = sum//10
            #Modulous of 10 to store the last digit in the current index
            arr[k] = sum%10
        #If the first array is fully traversed
        elif i<0:
            #Adding both the digit and carry
            sum = b[j]+carry
            #Storing the first digit at the carry
            carry = sum//10
            #Modulous of 10 to store the last digit in the current index
            arr[k] = sum%10
        #If the second array is fully traversed
        elif j<0:
            #Adding both the digit and carry
            sum = a[i]+carry
            #Storing the first digit at the carry
            carry = sum//10
            #Modulous of 10 to store the last digit in the current index
            arr[k] = sum%10
        #Moving to the next index
        k = k-1
        j = j-1
        i = i-1
    #If carry still exist
    if carry != 0:
        #We will insert the carry at the first position of the list and shift all the element to the next index
        arr.insert(0,carry)
        carry = 0
    #Return the result
    return arr

#For input
if __name__ == "__main__":
    a = [9,9,9,9]
    b = [1]
    print(sumArray(a,b))
else:
    print("Error")
