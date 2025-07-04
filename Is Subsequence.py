## loop through array until first char is found
## then do another loop on the rest of the string and try to add the characters in order
## if it doesnt work, keep going in the loop 

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        
        s_index = 0
        
        for i in range(len(t)):
            if t[i] == s[s_index]:
                s_index += 1
                if s_index == len(s):
                    return True
                
        return False