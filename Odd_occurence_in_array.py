#Odd occrences in the array
#In this algorithm we will find the element which exist odd number of times in an array
#We will use the property of XOR i.e a^0 = a or a^a = 0
#We will iterate through all the elements while performing a XOR operation
#In the end all the even number of times occurring element will be removed and needed number will remain
#Time comlexity is O(n) and Auxilary Space required is O(1)

#This function takes one argument i.e arr = array of elements
def find_ele(arr):
    #Creating a temp to store our result
    temp = 0
    #Iterating through our array
    for i in arr:
        #Performing xor operation with elements in arrat
        temp = temp^i
    #Returning the result
    return temp

#For input
if __name__ == "__main__":
    arr = [1,1,2,4,3,4,2]
    print(find_ele(arr))
else:
    print("Error")