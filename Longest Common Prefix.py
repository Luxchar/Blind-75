# create new string
# get the shortest word length and range over every word in the array for that length
# if the key is common between all the words, append it to the string

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        length = min(len(element) for element in strs)

        if len(strs) == 1:
            return strs[0]

        for i in range(length):
            firstChar = strs[0][i]

            for word in strs:
                if firstChar != word[i]:
                    return res

            res += firstChar

        return res