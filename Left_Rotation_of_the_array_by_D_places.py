#Left Rotation of the array by D places
#In this approach we will reverse of an array alogrithm
#First we will reverse the array from 0 to d-1 position and then we will reverse the array from d to n-1 position
#Where n is the size of the array
#And then reverse the whole array from 0 to n-1
#Time complexity is O(n) and Auxilary Space required is O(1)

#This function takes 1 input i.e arr = array or list of elememt
def rotate(arr,d):
    #Checking if number of roation is 0 or not
    if d == 0:
        #If 0 then simply return arr
        return arr
    else:
        #If d is bigger than n then we can simply find the d value by using mod
        d = d%len(arr)
        #Finding the reverse from 0 to d-1 position
        arr = reverse(arr,0,d-1)
        #Finding the reverse from d to n-1 position
        arr =  reverse(arr,d,len(arr)-1)
        #Finding the reverse from 0 to n-1 position
        arr = reverse(arr,0,len(arr)-1)
        #Return the rotated array
        return arr

#This function takes 3 argument i.e arr = array, l = starting index and r = ending index
def reverse(arr,l,r):
    #Using temp variable to store the value at arr[l] index
    temp = 0
    while l<r:
        temp = arr[l]
        #Moving the last index to the first index
        arr[l] = arr[r]
        #Moving First index to the last index
        arr[r] = temp
        #Incrementing the first index
        l = l+1
        #Decrementing the last index
        r = r-1
    #Returning the array
    return arr

#For input
if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    d = int(input())
    print(rotate(arr,d))
else:
    print("Error")