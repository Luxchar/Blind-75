"""Given two integers a and b, return the sum of the two integers without using the operators + and -.

 """

def hammingWeight(n):
    count=0
    for i in n:
        if i == "1":
            count+=1
    print(count)

if __name__ == "__main__":
    hammingWeight("00000000000000000000000000001011")
    hammingWeight("00000000000000000000000010000000") 
    hammingWeight("11111111111111111111111111111101") 