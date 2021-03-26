#Check if a number is Palindrome or not
#Approach will be first storing the reverse of the mumber in variable and then compare with the orginal number
#If they are same then its Palindrome
#Time complexity is O(log(N)) and Auxilary Space required is O(1)

#To get the floor value of the number in loop
import math

#Function takes one argument that is number
def check_Palindrome(n):
    #Temporary variable to store the reversed number
    sum = 0
    #Stores the orginal number
    original = n
    #Running loop till n is greater than 0
    while n>0:
        #Multpilying the sum with n to create 0 at the end of sum and adding the mod of n in sum
        sum = (sum*10) + (n%10)
        #Decreasing the tenth place of the n and storing the value in n
        n = math.floor(n/10)
    #If sum is equal to original number then it is palindrome
    if sum == original:
        return "Palindrome"
    else:
        return "Not Palindrome"

#For input
if __name__ == "__main__":
    num = int(input())
    print(check_Palindrome(num))
else:
    print("error")
