#Majority Element
#In this problem we need to find an element which is more than n/2 in arrray 
#In this approach we will use Moore's Voting Algorithm
#We will assume the first element is the potential answer and create a count of the element
#If the element occurs again then we will increase the count else dercrease the count
#If the count becomes 0 then we will assume that current element is our new potential answer
#We will check if the potential answer occurs more than n/2 times in array
#Time complexity is O(n) and Space Complexity is O(1)

#This function takes 1 argument i.e arr = array
def maj(arr):
    #Assume that first element is our potential answer
    ans = arr[0]
    #Set the counter at 1
    count  = 1
    #Iterate through the array
    for i in range(1,len(arr)):
        #If the element occurs again then increase the counter
        if ans == arr[i]:
            count = count+1
        #Else decrease the counter
        else:
            count = count-1
        #If the counter becomes 0 then our new potential answer is current element
        if count == 0:
            ans = arr[i]
            count = 1
    #Iterate through the array again and check if the element occurs more than n/2 time or not
    count = 0
    for i in arr:
        if i == ans:
            count = count+1
    #If it occurs more then n/2 times then return ans
    if count>=len(arr)//2:
        return ans
    #Else return -1
    else:
        return -1

#For input
if __name__ == "__main__":
    arr = [1,0,1,1,0,2,2,3,2,2,2,2]
    print(maj(arr))
else:
    print("Error")