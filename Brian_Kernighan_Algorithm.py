#Brian Kernighan’s Algorithm
#This algorithm is used for counting set bits in a number
#In observation, it can be seen that n-1 of a number unset the rightmost setbit
#By repeatedly unsetting the right most set bit and then performing a AND operating to flip the bits
#In each time we will increase the count 
#Eventually it will make n = 0
#Time complexity is O(log(n)) 

#Function takes one argument i.e n = number
def count_set(n):
    #Putting count as 0
    count = 0
    #Running a loop
    #Checking if the n is greater than 0 or not
    while n>0:
        #First unsetting the set bit by using "-" operator then performing AND with the old value
        n = n&n-1
        #Increasing the count
        count = count+1
    #Returning the count
    return count

#For input
if __name__ == "__main__":
    n = int(input())
    print(count_set(n))
else:
    print("error")