class Solution(object):
    def canConstruct(self, ransom, magazine):
        have = {}
        need = {}

        for ch in magazine:
            if ch in have:
                have[ch] += 1
            else:
                have[ch] = 1

        for ch in ransom:
            if ch in need:
                need[ch] += 1
            else:
                need[ch] = 1
        
        for ch in need:
            if ch not in have:
                return False
            elif need[ch] > have[ch]:
                return False
        return True

        