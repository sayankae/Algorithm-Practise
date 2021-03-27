#Look up table
#This algorithm is used to count set bits
#In this algorithm, we use a predifined list of number which represent the number of set bit for a number
#We right shift the number by k time, where k is the number of bits that we have already checked
#Increment count by looking into the lookup table
#This method run faster if the look table is large
#Time complexity is O(log(n)/k) and Auxilary Space required is O(2^k)

#This function takes only one argument i.e n = number
def count_set(n):
    #Lookup table that shows number of set bits corresponding to its positon
    table = [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
    #Initialise count as 0
    count = 0
    #Running a loop
    #Checking if n is greater than 0 or not
    while n>0:
        #Finding the number of bits for last four bit of the number and then adding it to count
        count = count+table[n&0xF]
        #Right shifting the n
        n = n>>4
    #Returning the count
    return count

#For input
if __name__ == "__main__":
    n = int(input())
    print(count_set(n))
else:
    print("Error")
