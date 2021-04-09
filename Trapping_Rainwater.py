#Trapping Rainwater Problem
#In this problem we have to calculate how much rainwater trapped in between the region
#We will be given one array, each element in the array represents the height of the region
#In this approach we will we will use array preproccesing
#First we will store the highest point traversing from the left to right of the array 
#Then we will store the highest poinit while traversing from right to left of the array
#Then we will compare the highest point and whichever is the lowest among them such that its higher than the current place
#We will simply find the difference of the lower highest place and the current place
#We will add it to the total of the array

#This function will take 1 argument i.e arr = array of heights 
def trappedWater(arr):
    #Create a two temporary list to store the leftmost highest and rightmost highest point
    left = [0]*len(arr)
    right = [0]*len(arr)
    #Assuming 0 is the highest peak in the array
    high = 0
    #Iterating from left index to right index
    for i in range(1,len(arr)-1,1):
        if high<arr[i-1]:
            high = arr[i-1]
        left[i] = high
    high = 0
    #Iterating from righ index to the leftmost index
    for i in range(len(arr)-2,-1,-1):
        if high<arr[i+1]:
            high = arr[i+1]
        right[i] = high
    #Assuming that there is no raiwater stored
    total = 0
    #Iterating from left to right again to store the total rainwater
    for i in range(len(arr)):
        #To find the lower highest peak at the current position
        if left[i]>right[i]:
            #To check if the highest peak is greater than the current peak
            if right[i]>arr[i]:
                #Add the difference of lower hghest peak and current peak to total
                total = total+right[i]-arr[i]
        else:
            #To check if the lower highest peak is greater than the current peak
            if left[i]>arr[i]:
                #Add the difference of lower highest peak and current peak to  the total
                total = total+left[i]-arr[i]
    #Return Total
    return total

#For input
if __name__ == "__main__":
    arr = [3,2,0,4,0,5,7,1,0,1]
    print(trappedWater(arr))
else:
    print("Error")