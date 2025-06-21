# loop through each word in s
# check if word is in hashmap
# if it is in hashmap, check that the letter is the same
# if its not then return false 

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return (len(pattern) == len(words) and 
                len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words))))

if __name__ == "__main__":
    # Example usage
    solution = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(solution.wordPattern(pattern, s))  # Output: True

    pattern2 = "abba"
    s2 = "dog cat cat fish"
    print(solution.wordPattern(pattern2, s2))  # Output: False