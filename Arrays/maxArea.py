"""You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container."""

def maxArea(heights):
    score = 0
    imin = 0
    imax=len(heights)-1
    while imin<=imax :
        score = max(score,min(heights[imin],heights[imax])*(imax-imin))
        imin+=1
        score = max(score,min(heights[imin],heights[imax])*(imax-imin)) #check all combinations
        imax-=1
    print(score)
    
if __name__ == "__main__":
    maxArea([1,8,6,2,5,4,8,3,7])
    maxArea([1,1])    