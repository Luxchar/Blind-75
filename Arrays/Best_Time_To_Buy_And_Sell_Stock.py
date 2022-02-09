"""You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0."""

def Stock(nums):
    mini = nums[0]
    maxi=0
    for i in range(len(nums)):
        mini = min(nums[i],mini)
        maxi = max(maxi,nums[i]-mini)
    print(maxi)

if __name__ == "__main__":
    Stock([7,1,5,3,6,4])
    Stock([7,6,4,3,1])