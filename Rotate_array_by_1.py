#Left Rotation of the array by 1
#In this approach we will use simple iteration
#We will put the first element in a temp variable and then shift all the element to its left index
#Then we will put the temp element in the last index
#Time complexity is O(n) and Auxilary Space required is O(1)

#This function takes one argument i.e arr = array or list of element
def shiftBy1(arr):
    #Temp variable to store the first index
    temp = arr[0]
    #Starting the iteration
    i = 0
    while i<len(arr)-1:
        arr[i] = arr[i+1]
        i = i+1
    #Shifting the first element to the last index
    arr[len(arr)-1] = temp
    #Return the shifted arry
    return arr

#For input
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    print(shiftBy1(arr))
else:
    print("Error")
