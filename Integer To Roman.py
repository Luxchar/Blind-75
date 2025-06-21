# set a hashmap with integer value to roman char
# go through the hashmap in descending order
# for each Symbol: divide the number by the value in the hashmap and add the corresponding letter to the roman string

class Solution:
    def intToRoman(self, num: int) -> str:
        value_symbols = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]

        roman_string = ""

        for value, symbol in value_symbols:
            if num == 0:
                break
            count = num // value
            num -= value * count
            roman_string += symbol * count

        return roman_string
            