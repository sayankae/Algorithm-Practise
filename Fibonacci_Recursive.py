#Fibonacci Number
#In this approach we will use the property of recurssion,
#We know that nth fibonacci number is (n-1)th + (n-2)th term
#Time complexity is O(2^N) and auxilary space required is O(N)

#This function takes one argument i.e n = nth number in fibo series
def fibo(n):
    #Base case
    if n == 0:
        #Fibo(0) = 0
        return 0
    elif n == 2 or n == 1:
        #Fibo(1) = Fibo(2) = 1
        return 1
    else:
        #Recursive call fibo(n-1) and fibo(n-2) then add them
        return fibo(n-1) + fibo(n-2)

#For input
if __name__ == "__main__":
    n = int(input())
    print(fibo(n))
else:
    print("Error")