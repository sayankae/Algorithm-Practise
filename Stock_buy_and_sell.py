#Stock buy and sell
#In this problem we have to find the maximum profit that ccan be earned by buying and selling stock
#An array will be given such that index represents the day and ith element represents the price on that day
#We can buy and sell stock at the same day or buy or sell it after some days but we cannot sell it before we 
#even buy it
#In this approach we will by traversing through array from left to right
#We will find the lowest minimum price before ith day and also find the difference after selling on ith day 
#The maximum difference will be our maximum profit
#Time complexity is O(n) and Auxilary Space required is O(1)

#This function takes one argument i.e arr = array of price
def findProfit(arr):
    #Assume that lowest price is at the first day itself 
    low = arr[0]
    #Assume that profit it 0 initially
    profit = 0
    #Traversing through the array
    for i in arr:
        #If the current price is lower than the lowest price then update the low
        if low>i:
            low = i
        #If the current difference between lowest price and current price is bigger than the profit,then update profit
        if profit<i-low:
            profit = i-low
    #Return profit
    return profit

#For input
if __name__ == "__main__":
    arr = [100, 180, 260, 310, 40, 535, 695]
    print(findProfit(arr))
else:
    print("Error")