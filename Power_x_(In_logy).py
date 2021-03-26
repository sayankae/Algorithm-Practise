#Pow(x,y) in O(log(y)) time
#This is a optimised solution of finding any number after raising its power to y times
#This approach simply takes the power and check if its odd or not
#If the power is odd then simply we can say that x^(y/2).x^(y/2-1) ex: 2^3 = 2^2*2^1
#If the power is even then we can also say say that x^(y/2).x.^(y/2) ex: 2^4 = 2^2*2^2
#This is iterative form of given algorithm
#This algorithm takes O(log(y)) time and takes O(1) Auxilary space

#Funtion will take two argument x = the number y = power of the number
def pow_num(x,y):
    #temp is to store our answer
    temp = 1
    #Running a loop till y is greater than 0
    while y>0:
        #We will check if the power is odd or not,
        #If odd then we will multiply our number to the cuurent solution and store it back in temp
        if y%2 != 0:
            temp = temp*x

        #Reducing the power by dividing it with 2
        #Assuming its the half way of the solution or even and two equal distribution
        y = y>>1
        #Squaring the value of x at each iteration because x^(y/2).x^(y/2) = x^y
        x = x*x
    #returning the answer back to the main function
    return temp

#main function
if __name__ == "__main__":
    x,y = input().split()
    x = int(x)
    y = int(y)
    print(pow_num(x,y))
else:
    print("error")

