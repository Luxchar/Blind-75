# use hashmap to map values to nb of occurences

# return top k by creating array and filling up values mapped to index

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {}

        for num in nums:  # can use, count_map = collections.Counter(nums)
            # count_map.get(num, 0) means: "Give me the current count of 'num'.
            # If 'num' isn't in the dictionary yet, just give me 0."
            count_map[num] = count_map.get(num, 0) + 1

        top_k = [[] for _ in range(len(nums)+1)]

        for num, freq in count_map.items():
            top_k[freq].append(num)

        res = []  # array to store solution

        for i in range(len(nums), 0, -1):
            for num in top_k[i]:
                res.append(num)
                if len(res) == k:
                    return res
