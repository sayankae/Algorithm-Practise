#Check if divisible by 4
#In this approach we will see if the number's last 2 digit is divisble by 4 
#If its divisible by 4 then the whole number is divisible by 4
#Time complexity is O(1) and Auxilary Space required is O(1)

#This function takes 1 argument i.e arr = string of digits
def checkDiv(arr):
    #Checking if the length of the string is greater than 2 or not
    if len(arr)<3:
        #If the integer form of the string is divisible by 4 or not
        if int(arr)%4 == 0:
            return True
        else:
            return False
    else:
        #Forming a 2 digit number from the second last digit and last digit
        num = int(arr[-2])*10+int(arr[-1])
        if num%4 == 0:
            return True
        else:
            return False
#For input
if __name__ == "__main__":
    arr = "363588395960667043875487"
    print(checkDiv(arr))
else:
    print("Error")
