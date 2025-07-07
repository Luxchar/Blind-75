# loop through ransomNote
# if element is in magazine
# add it to the hashmap
# if its not available then return false
#~if out of the range then return true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return (Counter(ransomNote) - Counter(magazine)) == {}