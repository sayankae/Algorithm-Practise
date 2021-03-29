#Generate power set using bitwise operators.
#In this method we will use AND property of the number
#First we will generate size of set by using Power Set formula i.e P(len(arr)) = 2^len(array)
#If we run see the number in binary form from 0 to the size of Power set then
#We can see that each makes a forms a combination
#We can simply compare each bit postion with postion of elements in the array and then print the element
#Time comlexity is O(2^n)

#This function take one argument i.e arr = array
def power_set(arr):
    #Power set size is 2 raise to the power of total number of elements in array
    set_size = 2**len(arr)
    #Iterating through each number of the powerset
    for i in range(set_size):
        #Creating an empty list to store the subset
        word = []
        #Iterating through our array
        for j in range(len(arr)):
            #Performing AND opeation with the number and the postion of the element in array
            if i&(1<<j) != 0:
                #If the set bit matches then add the element to the subset
                word.append(arr[j])
        #Print the subset
        print(word)
        #Delete the subset after each iteration
        del(word)

#For input
if __name__ == "__main__":
    arr = "abcde"
    power_set(arr)
else:
    print("Error")
