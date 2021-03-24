#Segmented Sieve
#If range is somewhere between 1 to N such that N can be a large number i.e 10^9, then this method is useful
#It does not reduce the time complexity of the Normal Sieve Algo but it does reduce the space complexity if the value of N is big
#Auxilary Space Required here is sqrt(h) and time complexity is O(h.loglog(h)) here h = upper range
import math

#It is a good practise to find all the prime number upto root of 10^9, so later one do not have to calculate prime over and over

#to find the reference prime number upto square root of h
def normalSieve(h):
    size = math.sqrt(h)
    size = math.floor(size)
    #suppose all the number upto square root of h is prime so we put all the value as True
    prime = [True]*(size+1)
    i = 2
    #new list to put all the prime number upto square root of h
    new_prime = []
    while i<size+1:
        if prime[i] == True:
            new_prime.append(i)
            #loop from square of prime till the square root of h and mark all the multiples of prime as False
            for j in range(i*i,size+1,i):
                prime[j] = False
        i = i+1
    
    #return of prime list back to segmented sieve function/method
    return new_prime

#main Sieve function//method which will find all the primes between the given Range
def segSieve(h,l):
    #determinig the size of the list where we will store our bool value of prime and non prime numbers
    size = h-l+1
    #Assuming that all the numbers are prime, so we mark them as True
    prime = [True]*size
    #calling Sieve function to fetch the list of primes upto the square root of h
    ref_prime = normalSieve(h)

    #Running the loop till the end of the prime list
    for i in ref_prime:
        #determing the base or starting point of the list prime
        #l = lower range, i is the chosen or selected prime at this instance
        low = math.floor(l/i)*i
        #we will compare with floor value of base with the lower range, if its lower than l, we will increment the base with the current prime
        if low<l:
            low = low+i
        #changing low to integer because it may contain float value and then storing it in base
        base = low

        #this loop will mark every multiple of current prime to False but between given range
        for j in range(base,h+1,i):
            prime[j-l] = False

        #if the base value is equal to current prime then we will revert the change back to True
        if base == i:
            prime[base-l] = True
    
    #checking all the bool values of number between given range and if the value found to be true at ith position then storing the value in
    #an empty set or list
    new_prime = set()
    for i in range(len(prime)):
        if prime[i] == True:
            new_prime.add(i+l)

    #if the list or set contains 1 then remove it 
    if 1 in new_prime:
        new_prime.remove(1)
    
    #return the list of prime between l to h
    return new_prime

#for input
if __name__ == "__main__":
    h,l = input().split(" ")
    h = int(h)
    l = int(l)
    print(segSieve(h,l))
else:
    print("Not Found")