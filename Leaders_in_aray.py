#Leaders in Array
#In this approach we will use iterative method
#We will check whether the righmost element is currently bigger than its left neighbor or not
#We will append at each step where we will find the next biggest element and store it in an array
#Time complexity is O(n) and Auxilary Space required is O(n)

#This function takes 1 argument i.e arr = array or list of element
def leaders(arr):
    #This empty array or list will store our leaders
    lead = []
    #We assume the biggest element is -1 tho the assumption should be the last value of negative int
    currMax = -1
    #Iterting from right to left
    i = len(arr)-1
    while i>-1:
        #Checking if the current max is smaller then the current element or not
        if currMax<arr[i]:
            #If smaller than our current max is the current index and our new leader
            lead.append(arr[i])
            currMax = arr[i]
        i = i-1
    #Return the leader array 
    return lead[::-1]

#For input
if __name__ == "__main__":
    arr = [16, 17, 4, 3, 5, 2] 
    print(leaders(arr))
else:
    print("Error")


