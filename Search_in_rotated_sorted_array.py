#Search in a Rotated Array
#In this algorithm, we will find the given element index by using binary serach
#This binary search is modified around the property of the rotated array
#We know that in sorted array the max element stays at the mid+1 or greater index
#Where as the min stays at the mid-1 or lower index
#So here our mid is the pivot point, in this algorithm we will check the pivot point
#Then we will compare that pivot point with the lowest index element and the highest index element
#Also we will compare it with the key location and decide which part we should move our pivot too
#Time complexity is O(log(n)) and Auxilary space required is O(1)

#This function takes 4 argument i.e A = list of elements, l = lowest index, h = highest index and key = key element
def search(A, l, h, key):
    low = l
    high = h
    #Iterating through the list or array
    while low<=high:
        #Finding the pivot or mid of the array
        mid = int((low+high)/2)
        #If the mid element itself is our key then return the index of the mid
        if A[mid] == key:
            return mid
        #If the mid element is bigger than the lower element
        elif A[mid]>=A[low]:
            #Checking if the key is lower than the mid element and bigger than the lower element
            if key<=A[mid] and key>=A[low]:
                #Then move higher index to mid -1 position
                high = mid-1
            else:
                #Else move the lowest index to mid+1 position
                low = mid+1
        #If the mid element is lower then the lower element
        else:
            #Checking if the key is greater than mid element and smaller than the highest element
            if key>=A[mid] and key<=A[high]:
                #Then move the lower index to mid+1 position
                low = mid+1
            else:
                #Else move the hghest index to mid-1 position
                high = mid-1
    #If the above loop return no index then element not found in the list     
    return -1

#For input
if __name__ == "__main__":
    n = int(input())
    A = []
    for i in range(n):
        temp = int(input())
        A.append(temp)
    key = int(input())
    print(search(A,0,len(A)-1,key))
else:
    print("Error")