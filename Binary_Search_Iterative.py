#Binary Search
#Very popular and faster way to find elements in an sorted list or array. It takes logarithmic time
#The Principle it is based in is divide and conquerer. It divides the list in two different list and
#look for the element whether its in the right part of left part of the list 
#In every single iteration or run it again divides the list into smaller list and narrrows down to the 
#target element
#Time complexity is O(log(n)) and Auxilary Space required is O(1) in iterative approach

#This function takes 4 argument i.e arr = array or list and k = target
def binarySearch(arr,k):
    #l is the leftmost index
    l = 0
    #r is the rightmost index
    r = len(arr)-1
    #Iterating through the lust
    while l<=r:
        #mid is the pivot index
        mid = (l+r)//2
        #Check if the middle element is the target
        if arr[mid] == k:
            #Return thr index
            return mid
        #Check if target element is bigger than the middle element
        elif k>arr[mid]:
            #Shift to the right part
            l = mid+1
        else:
            #Shift to the left part
            r = mid-1
    #If the above iteration returns nothing then the target element is not present in the list
    return -1

#For input
if __name__ == "__main__":
    arr = [1,3,4,6,7,8,9,13,20]
    k = int(input())
    print(binarySearch(arr,k))
else:
    print("Error")

