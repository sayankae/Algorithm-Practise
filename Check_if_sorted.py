#Check if Sorted
#In this approach we will use simple iteration
#We will compare the element to its next next element whether it is smaller or not
#If all the element are smaller than its right neighbor then sorted
#Else its not sorted
#Time complexity is O(n) and Auxilary Space required is O(1)

def checkarr(arr):
    #Starting iteration from first index to the second last index
    i = 0
    while i<len(arr)-2:
        #Checking if the neighbor is smaller or not
        if arr[i]>arr[i+1]:
            #If smaller then its not sorted, return False
            return False
        i = i+1
    #If it does not return false then its sorted
    return True

#For input
if __name__ == "__main__":
    arr = [1,2,3,7,5,6]
    print(checkarr(arr))
else:
    print("Error")
