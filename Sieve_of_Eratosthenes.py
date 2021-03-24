#Sieve of Eratosthenes
#This algorithm finds the list of prime from 1 to N 
#It takes O(N.loglog(N)) unit of time
#Auxilary space is O(N), it is clealy seen that this amount space is not good for large value of N

#Sieve is the main funtion/method which will find all the prime upto N
import math

def Sieve(N):
    #Assuming that all the numbers are prime upto N, so putting bool to True for all the numbers in the list
    prime = [True]*N
    #0 and 1 is not prime number, putting False in at their place
    prime[0] = False
    prime[1] = False
    i = 2

    #Running loop upto square root of N because, it is observed that the number of prime is less than N/2 in any given number
    for i in range(math.floor(math.sqrt(N))):
        #Checking if the bool is True or not
        if prime[i] == True:
            #Loop will run from the square of current prime and upto N
            #Marking False at each multiple of the current prime number
            for j in range(i*i,N,i):
                prime[j] = False
    
    #Running loop till N, iterating through prime list
    for i in range(N):
        #if the current value is True then print the ith value i.e prime number
        if prime[i] == True:
            print(i)

#For input
if __name__ == "__main__":
    N = int(input())
    Sieve(N)
else:
    print("Error")

