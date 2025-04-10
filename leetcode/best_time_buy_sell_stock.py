# /*
# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.
# */

def maxProfit(arr):
    mx = 0
    maxR = [0] * len(arr)
    for i in range(len(arr)-2, -1, -1):
        maxR[i] = max(arr[i+1], maxR[i+1])
        mx = max(mx, maxR[i]-arr[i])
    return mx

arr = [7, 1, 5, 3, 6, 4]
print(maxProfit(arr))

arr = [7, 1, 5, 3, 6, 4]
print(maxProfit(arr))

arr = [7, 6,4,3,1]
print(maxProfit(arr))
