#Check Palindrome
#In this approach we will use recursion,
#We will check the left index of the array and the right index of the array,
#If its same then increment the left side and decrement the right side until it reaches mid
#If it reaches mid then its a palindrome else its not
#Time complexity is O(len(arr)/2) and Space required is O(1)

#Function takes 3 argument i.e l = left index, r = right index and arr = string
def checkPalindrome(l,r,arr):
    #Base case
    #Check if left index reaches right index
    if l>=r:
        #If left index reaches right index then its palindorme
        return "Palindrome"
    else:
        #Check if the word at left index and right index are same or not
        if arr[l] == arr[r]:
            l = l+1
            r = r-1
            #If same then check the next index
            return checkPalindrome(l,r,arr)
        else:
            #The word do not matches at left index and right index so its not a palindrome
            return "Not Palindrome"
#For input
if __name__ == "__main__":
    arr = "issassi"
    arr1 = "iamnotpalindrome"
    print(checkPalindrome(0,len(arr)-1,arr))
    print(checkPalindrome(0,len(arr1)-1,arr1))
else:
    print("Error")

