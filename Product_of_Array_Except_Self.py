"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i]."""

def Product(nums):
    visited = []
    for i in range(len(nums)):
        num = 1
        for j in nums:
            if j != nums[i]:
                num*=j
        visited.append(num)
    print(visited)


if __name__ == "__main__":
    Product([1,2,3,4])
    Product([-1,1,0,-3,3])