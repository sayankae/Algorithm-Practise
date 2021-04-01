#Rod Cutting 
#In this approach we will use dynamic programming
#First we will check all the prices possible for ith cut and then store the best price for ith index in DP array
#We also maintain a max value we can get from the rod pieces
#Time complexity is O(n^2) and auxilary space required is O(len(arr))

#This function will take 1 argument i.e arr = array
def cutRod(arr):
    #DP array to store the best price
    dpArr = [0]*(len(arr)+1)
    #Max value is 0 before checking
    maxVal = 0
    #Starting index of the array
    i = 1
    #Running a loop will the end of the index of arr
    while i<len(arr)+1:
        #Temp to store current max
        temp  = 0
        #Running a loop to find the best price from 0th index to ith index
        for j in range(i):
            #Checking if the jth + j-ith index best price is greater then normal price of not
            if dpArr[j]+dpArr[i-j]>arr[i-1]:
                #If bigger then put inside temp
                temp = dpArr[j]+dpArr[i-j]
                #If its greater than normal price then break
                break
            else:
                #Else put the normal price in temp
                if i!= 0:
                    temp = arr[i-1]
                else:
                    temp = 0
        #Put the best price of ith index in DP array
        dpArr[i] = temp
        #Check if max value is less than temp or not
        if temp>maxVal:
            #If less than max value is temp 
            maxVal = temp
        i = i+1
    #Return max value
    return maxVal

#For input
if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    print(cutRod(arr))
else:
    print("Error")
