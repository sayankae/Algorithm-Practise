#Bitonic array
#Array which is strictly increasing upto ith position but after that its strictly dereasing
#In this array we need to find an element with modified binary search
#We will check if the left part is strictly increasing or not and right part is strictly decreasing or not
#Then will shift our pivot accordingly to that 
#If the element is found in any of the part we will return the index
#Else we will return -1
#Time complexity is O(log(n)) and Auxilary Space required is (1)

#This function will take 2 input i.e arr = array and k = target element
def bitonicSearch(arr,k):
    #Left most index as 0
    l = 0
    #Right most index as length of the array -1
    r = len(arr)-1
    #Iterating through the array
    while l<=r:
        #Finding the mid or pivot
        mid = (l+r)//2
        #Checking if the mid is equal to key or not
        if arr[mid] == k:
            #If key is at mid index then return index
            return mid
        #Checking if the mid is greater then the leftmost element or not
        elif arr[mid]>arr[l]:
            #Checking if the key is smaller than mid and bigger than leftmost element
            if arr[mid]>=k and k>=arr[l]:
                #If yes then move to the left part of the array
                r = mid-1
            else:
                #Else move to the right part
                l = mid+1
        #If the mid is smaller then
        else:
            #Checking if the key is smaller than the mid element or not and key is bigger than the right most element
            if arr[mid]>=k and k>=arr[r]:
                #Then move to the right part of the array
                l = mid+1
            else:
                #Move to the left part
                r = mid-1
    #If during iteration the index is not returned then return -1
    return -1

#For input
if __name__ == "__main__":
    arr = [1,2,3,4,9,7,6,5]
    k  = int(input())
    print(bitonicSearch(arr,k))
else:
    print("Error")
