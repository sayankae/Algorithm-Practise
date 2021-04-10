#Maximum Consecutive 1s
#In this problem we have to find the size of biggest conseccutive 1s sequence
#We will use simple iterative approach
#Every time we get 1 we will icrease the count but when we enocunter a 0 then we will reset the count
#After every count we will compare it to the current max
#Return the max value
#Time complexity is O(n) and Auxilary Space required is O(1)

#This function takes 1 argument i.e arr = array of 1s and 0s
def max1(arr):
    #Before the iteration start, Assume count is 0 and length of maximum sequence is 0
    count = 0
    ans = 0
    #Iterating through the array
    for i in arr:
        #If 1 shows up then increase the counter
        if i == 1:
            count = count+1
            #First check if the current sequence length is bigger than current maximum length
            if count>ans:
                #Update the maximum
                ans = count
        #If 0 shows up
        else:
            #Reset the count
            count = 0
    #Return the ans
    return ans

#For input
if __name__ == "__main__":
    arr = [1,1,1,0,1,0,0,0,1,1,1,1,1]
    print(max1(arr))
else:
    print("Error")
