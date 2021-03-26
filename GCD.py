#GCD of Two given number
#In this approach we will simply divide the number let say a by b until the bigger number becomes 0
#The logic behind this approach that we know any gcd between two number will be less than or equal to the smallest one
#We are keeping the remainder in the smallest position

#Function takes two argument i.e a = 1st number and b = 2nd number
def GCD(a,b):
    #Checking if the value of value of b is 0 or not
    #If b is 0 then we can say we have reduced the number such that its our GCD
    if b == 0:
        return a
    #If b is not 0 then keep on reducing b and storing the largest value at a postion
    else:
        #Recursing the function and send b in place of a position and sending the remainder in place of b postion
        return GCD(b,a%b)

#For Input
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(GCD(a,b))
else:
    print("error")



