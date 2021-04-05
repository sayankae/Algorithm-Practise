#Product of given N fractions in reduced form
#Given the Numerator and Denominator of N fractions. The task is to find the
#product of N fraction and output the answer in reduced form.
#In this approach we will use recursion
#First we will multiply all the numerator given and then we will multiply all the denominator
#Then to reduce their form we will find the gcd of the two products and then divide it by the two products 
#Time complexity is O(n) and Auxilary Space required is O(1)

import math
#This function takes two argument i.e num = array of numerator and den = array of denominator
def reduceForm(num,den):
    numProd = 1
    denProd = 1
    #Finding product of the numerator
    for i in num:
        numProd = numProd*i
    #Finding product of the denominator
    for i in den:
        denProd = denProd*i
    #Finding gcd of the two product
    gcdProd = gcd(numProd,denProd)
    #Finding the reduced form by divding the product by obtained gcd
    return (numProd/gcdProd),(denProd/gcdProd)

#This function takes 2 argument i.e a = product of all the numerator and b = product of all the denominator
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

#For input
if __name__ == "__main__":
    num = [1, 2, 5, 30, 17]
    den = [2, 1, 6, 20, 17]
    a,b = reduceForm(num,den)
    a = str(math.floor(a))
    b = str(math.floor(b))
    print(a+"/"+b)
else:
    print("Error")


