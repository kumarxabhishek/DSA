class Solution(object):
    def longestPalindrome(self, s):
        pali = {}

        for ch in s:
            if ch in pali:
                pali[ch] += 1
            else:
                pali[ch] = 1
        
        has_odd = 0
        res = 0

        for ch in pali:
            res += (pali[ch] // 2)*2
            if has_odd == 0:
                has_odd = pali[ch]%2
        
        return res+has_odd

        