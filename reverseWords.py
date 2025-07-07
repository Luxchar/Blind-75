# array of words in s
# that way we get each word without spaces
# reverse the array and return them concatenated with a space
# to get words we loop on string and reconstruct the word based on spaces around it

class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        current_word = ""
        for element in s:
            if element != " ":
                current_word += element
            else:
                words.append(current_word)
                current_word = ""
            
        reversed_sentence = words.reverse()
        return 
                


        