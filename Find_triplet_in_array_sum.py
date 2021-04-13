#Find triplet in an array which gives sum X
#In this question we need to find the triplets let say a,b,c such that a+b+c = X, where x is the target sum
#In this approach we will use, two pointer method. Our first pointer and second pointer will change according 
#to the sum X, such f(sum)<X we will increase the first pointer else decrease the second pointer
#For this approach we first need to sort the array, the we need to fix one element and use two pointer approach
#in the second loop
#Time complexity is O(n*log(n))+O(n^2) when array is not sorted, Auxilary Space required is O(n)

#This function takes one argument i.e arr = array of elements and x = target sum
def triplet(arr,x):
    #arr stores the merged array
    arr = mergesort(arr,0,len(arr)-1)
    print(arr)
    #Iterate through the array
    for i in range(len(arr)):
        #j  = first pointer
        #k = second pointer
        j = i+1
        k = len(arr)-1
        while j<k:
            #s stores the sum of triplets
            s = arr[i]+arr[j]+arr[k]
            #If s is equal to the target sum x
            if s == x:
                #Return the triplets
                return arr[i],arr[j],arr[k]
            #If the sum is bigger than the target sum x
            elif s>x:
                #Move the second pointer
                k = k-1
            #If the sum is smaller than the target sum x
            else:
                #Move the first pointer
                j = j+1
    #If the sum does not exist return False
    return False

#This function takes 3 argument i.e arr = array, l = leftmost index and r = righmost index
def mergesort(arr,l,r):
    #Check if the left most index is smaller than the righmost index
    if l<r:
        #Find the mid or pivot point
        mid = (l+r)//2
        #Recusively call the left part
        mergesort(arr,l,mid)
        #Recursively call the right part
        mergesort(arr,mid+1,r)
        #Join the two part together
        merge(arr,mid)
    #Return the array
    return arr

#THis function takes 2 argument i.e arr = array and mid = pivot point
def merge(arr,mid):
    #Storing the left part of the pivot point in L
    L = arr[:mid]
    #Storing right part of the pivot point in R
    R = arr[mid:]
    #Initialising starting index of left part, right part and orignal array at 0th index
    i = 0
    j = 0
    k = 0
    #Iterating through the array
    while i<len(L) and j<len(R):
        #If element of the right array is smaller
        if L[i]>R[j]:
            #Store it in the orginal array
            arr[k] = R[j]
            #Increment the right pointer
            j = j+1
        #If element of left part is smaller
        else:
            #Store it in the orignal array
            arr[k] = L[i]
            #Increment the left pointer
            i = i+1
        #Increment the index of the original array
        k = k+1
    #Storing the element left in the left array
    while i<len(L):
        arr[k] = L[i]
        i = i+1
        k = k+1
    #Storing the element left in the right array
    while j<len(R):
        arr[k] = R[j]
        j = j+1
        k = k+1
    return

#For input
if __name__ == "__main__":
    arr = [12, 3, 4, 1, 6, 9]
    x = int(input())
    print(triplet(arr,x))
else:
    print("Error")