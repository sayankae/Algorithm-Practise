#Maximum Circular Sum Subarray
#In this problem we need to find the maximum sum of the subarray such that it can wrap around
#In this approach we will use Kadane's Algorithm 
#We will first find the biggest sum subarray in the 1 to n array
#Then we will find the total sum of the array and then change the sign of each element
#Then we will perform Kadane's Algorithm again on the new array and find the biggest sum
#Then we will check if the new sum and the sum of array is equal to 0 then our biggest sum is the old sum subarray
#If the sum is greater than 0 then we will check if the old sum subarray is greater than the sum 
#Whichever is bigger we will return that
#Time complexity is O(n) and Auxilary Space required is O(1)

#This function takes 1 argument i.e arr = array
def maxSum(arr):
    #First the find the biggest sum in normal array without wrap
    first = kadane(arr)
    #Second find the sum of all the element and also make the element negative after sum
    second = 0
    for i in range(0,len(arr)):
        #Adding sum 
        second = second+arr[i]
        #Making the element ngative if postive and postive if negative vice versa
        arr[i] = -1*arr[i]
    #Third find the biggest sum of subarray in new array
    third = kadane(arr)
    #Check if the sum of second and third is equal to 0
    if second+third == 0:
        #Return First
        return first
    else:
        #If first is bigger than the sum of the second and third
        if first>second+third:
            #Return First
            return first
        else:
            return second+third

#This function takes 1 argument i.e arr = array
def kadane(arr):
    ans = arr[0]
    #We will asume that our current sum is 0
    count = 0
    #We will run the loop from the second element
    for i in range(len(arr)):
        #Check if the current sum is positive
        if count+arr[i]<0:
            #Check if the count was already negative or not
            if count<0:
                #Check if the current negative sum is bigger than the old sum
                if count+arr[i]>count:
                    #Update the count
                    count = count+arr[i]
                    #Check if the current max is smaller then the current sum
                    if count>ans:
                    #Check if the current max is smaller then the current sum
                        ans = count
                else:
                    #Reset the count to 0
                    count = 0
            else:
                #Reset the count 
                count = 0
        else:
            #Add the current element with the old sum
            count = count+arr[i]
            #Check if the current max is smaller then the current sum
            if count>ans:
            #Check if the current max is smaller then the current sum
                ans = count
    #Return 
    return ans

#For input
if __name__ == "__main__":
    arr = [8, -8, 9, -9, 10, -11, 12]
    print(maxSum(arr))
else:
    print("Error")