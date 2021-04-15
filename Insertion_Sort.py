#Insertion Sort
#A very famous sort algorithm which is a part of the comparision sort problems
#In this algorithm, we will compare the next index element with the previously sorted list
#If the element fits into the sorted array then we will swap there places with each comparision
#Swap the elements until the chosen element is not in the right place i.e bigger than the previous one
#Time complexity of insertion sort is O(n*n) and Auxilary Space required is O(1)

#This function takes 1 argument i.e arr = array
def insertionSort(arr):
    #We will select our element from the second index and start iterating
    #We assumed that first element itself is sorted
    for i in range(1,len(arr)):
        #We will check if the selected element can be inserted inside the sorted part
        for j in range(i-1,-1,-1):
            #If the selected element is smaller then insert the element in the position
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = swap(arr[j],arr[j+1])
            #If the selected element is bigger then dont need to check further
            else:
                break
    return arr


#This function takes 2 argument i.e a = first element and b = second element 
def swap(a,b):
    #Basic Swap opertion 
    temp = a
    a = b
    b = temp
    return a,b

#For input
if __name__ == "__main__":
    arr = [1,5,3,7,8,9,4]
    print(insertionSort(arr))
else:
    print("Error")