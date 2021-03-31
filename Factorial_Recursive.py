#Factorial of a number
#In this approach we will use recursion 
#We know that factorial of n is n!*(n-1)!*..*1
#Time complexity is O(N) and Auxilary Space is O(N)

#This funtion takes one argument i.e n = number
def fact(n):
    #Base case
    if n == 1:
        #Fact(1) = 1
        return 1
    else:
        #Fact(n) = n*fact(n-1)
        return n*fact(n-1)

#For input
if __name__ == "__main__":
    n = int(input())
    print(fact(n))
else:
    print("Error")
