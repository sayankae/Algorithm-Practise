#Longest Even Odd Subarray
#In this problem we need to find the longet sequence of subarray with odd even or even odd arrangement
#In this approach we will use simple iterative method
#We will check for thr starting element, if its odd then we will check for the next element if its opposite or not
#If its opposite then we will increase the count and if they are same i.e odd-odd or even-even then we will reset 
#the count
#Time  complexity is O(n) and Auxilary Space required is O(1)

#This function takes 1 argument i.e arr = array
def longOddEven(arr):
    #Initialise the count as 1 because we already considered the starting index
    count = 1
    #Maximum size of the subarrat is 0 before checking
    ans = 0
    #Starting the loop from the next in index
    for i in range(1,len(arr)):
        #Check if the current element is odd and left elment is even
        if arr[i]%2 != 0 and arr[i-1]%2 == 0:
            #Increase the counter
            count = count+1
        #Check if the current element is even and left element is odd
        elif arr[i]%2 == 0 and arr[i-1]%2 != 0:
            #Increase the count
            count = count+1
        #Check if the current element and the last element both are odd or even
        elif arr[i]%2 == arr[i-1]%2:
            #Counter resets
            count = 1
        #Check if the current length of the subarray is greater than the maximum size
        if count>ans:
            #Update the ans
            ans = count
    #Return ans
    return ans
        
#For input
if __name__ == "__main__":
    arr = [1,0,1,1,0,1,0,1,1,0,1]
    print(longOddEven(arr))
else:
    print("Error")
