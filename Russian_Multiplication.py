#Russian Multiplication 
#In this method of multiplication, we half the first number until it reaches 1 and double the second number
#We add the second number before doubling and after doubling
#Time complexity O(log(a,b)) and Auxilary Space = 1

#This function takes 2 argument i.e a = first number and b = second sunmber
def russian_multiplication(a,b):
    #To store the result
    res = 0
    #Loop until a is greater than 0
    while a>0:
        #Checking if the number is odd 
        if a&1:
            #If odd then add second number to the current result
            res = res+b
        #Double the b by using the left shift
        b = b<<1
        #Half the a using the right shift
        a = a>>1
    #Return the answer
    return res

#For input
if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(russian_multiplication(a,b))
else:
    print("Error")
