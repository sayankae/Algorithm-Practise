#All subset of a set
#In this approach we will use recursion
#We will take an index at a time and choose whether to add it in the current set or not
#Recursing till the end of the length of array will give us our subset 
#Time complexity is 2T(n-1) = O(2^n) and Auxilary space required is O(n)

#This function takes 4 argument i.e arr = orginal set, subarr = current subset, i = index, n = size of the original array
def subset_of_set(arr,subarr,i,n):
    #Base Case
    #If we reach the end of the array that is n, then simply print the subset
    if i == n:
        if len(subarr) != 0:
            print(subarr)
        return
    #If i is smaller then size of original set
    else:
        #Append the ith element of the orignal set inside subarray
        subarr.append(arr[i])
        #Calling subset again but with next index and new subarray
        subset_of_set(arr,subarr,i+1,n)
        #After our subset is generated then remove element from the previous subset
        subarr.pop()
        #Calling the function again but with next index and old subarray
        subset_of_set(arr,subarr,i+1,n)

#For input
if __name__ == "__main__":
    arr = "abc"
    subarr = []
    n = len(arr)
    i = 0
    subset_of_set(arr,subarr,i,n)
