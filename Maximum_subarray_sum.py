#Maximum Subarray Sum
#In this problem we need to find the biggest sum subarray
#In this approach we will use simple iteration
#We will use sliding window technique
#First we will check if the sum of right element is bigger than positive or not if its negative then
#We will reset our sum to 0 
#At every stage of sum we will compare it with a current max sum and update it if its bigger
#Time complexity of this approach is O(n) and Auxilary Space required is O(1)

#This function takes 1 argument i.e arr = array of element
def maxSubsum(arr):
    #Assume than max sum is 0 and current subsequence sum is 0
    count = 0
    ans = arr[0]
    #Iterating through the array
    for i in arr:
        #checking if the current subsequence sum is lower than 0 or not
        if count+i<0:
            #Checking if the count was already negative or not
            if count<0:
                #If the negative value if greater than other negative value
                if count+i>count:
                    #Add the current element to count
                    count = count+i
                    #Update the max
                    if count>ans:
                        ans = count
                else:
                    count = 0
            #If the count is positive
            else:
            #If lower than the current sum reset the count
                count = 0
        #If the sum is positive
        else:
            #Add the element to the count
            count = count+i
            #Check if the current subsequence sum is greater than the current max 
            if count>ans:
                #Update the ans
                ans = count
    #Return the ans
    return ans

#For input
if __name__ == "__main__":
    arr = [-1,-2,3,-2,-5]
    print(maxSubsum(arr))
else:
    print("Error")

