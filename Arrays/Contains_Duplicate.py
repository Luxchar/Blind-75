"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""

def Duplicate(nums):
    visited = []
    for i in nums:
        if i in visited:
            print("True")
            return
        else:
            visited.append(i)
    print("False")

if __name__ == "__main__":
    Duplicate([1,2,3,1])
    Duplicate([1,2,3,4])
    Duplicate([1,1,1,3,3,4,3,2,4,2])