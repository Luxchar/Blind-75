"""Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i."""

def countBits(n):
    out = []
    for i in range(0,n+1):
        binary = ("{0:b}".format(int(i))) 
        if binary.count("1") == 0:
            out.append(0)
        else:
            out.append(binary.count("1"))
    print(out)

if __name__ == "__main__":
    countBits(2)
    countBits(5)