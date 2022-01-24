"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""
    
def twosum(nums,target):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]+nums[j] == target:
                print('['+str(i)+","+str(j)+"]")


if __name__ == "__main__":
    twosum([2,7,11,15],9)
    twosum([3,2,4],6)
    twosum([3,3],6)