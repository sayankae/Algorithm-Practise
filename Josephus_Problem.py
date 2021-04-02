#Josephus Problem
#In this game, we need to find the last survivor after killing kth person each time
#The approach is to use recursion
#Time complexity is O(n) and Auxilary Space required is O(n)

#This function takes 2 argument i.e n = number of people and k = kth person to kill
def jos(n,k):
    #Base Case
    #If only one person remains then return 0 i.e the person survin=ving is at 0th position
    if n == 1:
        return 0
    #Else reduce the person after killing at kth postion
    else:
        #Previous location of the person for n remaining person
        x = jos(n-1,k)
        #Shift the previous location of the person to the current n number of people
        y = (x+k)%n
        #Return y, the current position of the person
        return y

#For input
if __name__ == "__main__":
    n = int(input())
    k = int(input())
    print(jos(n,k)+1)
else:
    print("Error")
