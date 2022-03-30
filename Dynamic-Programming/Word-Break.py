def wordBreak(s, WordDict):
    if not s:
        return True
    if not WordDict:
        return False
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in WordDict:
                dp[i] = True
                break
    return dp[-1]

print(wordBreak("leetcode", ["leet", "code"]))
print(wordBreak("applepenapple", ["apple", "pen"]))