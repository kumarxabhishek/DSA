class Solution(object):
    def firstUniqChar(self, s):
        mp = {}

        for ch in s:
            if ch in mp:
                mp[ch] += 1
            else:
                mp[ch] = 1

        for i in range(len(s)):
            if mp[s[i]] == 1:
                return i
        
        return -1
        