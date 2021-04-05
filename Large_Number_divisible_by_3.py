#Check if a large number is divisible by 3 or not
#In this approach we will use a property of a number that:
#If we add up every digit of a number together then if that sum divisble by 3 then
#The whole number is divisible by 3
#Time complexity is O(len(string)) and Auxilary Space required is O(1)

#This function takes one argument i.e arr = string of digits
def checkDiv(arr):
    sum = 0
    #Iterating through each element and add up 
    for i in arr:
        sum = sum+int(i)
    #Checking if the sum is divisble by 3 or not
    if sum%3 == 0:
        return True
    else:
        return False
#For input
if __name__ == "__main__":
    arr = "3635883959606670431112222345915"
    print(checkDiv(arr))
else:
    print("Error")
