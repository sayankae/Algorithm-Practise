#Tower of Hanoi
#In this approach we will use recursion 
#Time complexity is O(2^n) and Auxilary space required is O(n)

#This function takes 4 argument i.e n = number of disc, a = source, b = destination and c = auxiliary pole
def hanoi(n,a,b,c):
    #If n is equal to 1
    #Base Case
    if n == 1:
        #Printing that one disk will move from source to destination
        print(1,a,b,c)
        return 
    else:
        #Moving n-1 disk from source to the auxiliary pole
        hanoi(n-1,a,c,b)
        #Print the step taken
        print(n,a,b,c)
        #Moving nth disk from source to the destination pole
        hanoi(n-1,c,b,a)

#For input
if __name__ == "__main__":
    n = int(input())
    hanoi(n,"A","B","C")
else:
    print("Error")