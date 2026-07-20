class Solution(object):
    def maxNumberOfBalloons(self, text):
        x = "balloon"
        balloon = {}
        have = {}

        for ch in x:
            if ch in balloon:
                balloon[ch] += 1
            else:
                balloon[ch] = 1

        for ch in text:
            if ch in have:
                have[ch] += 1
            else:
                have[ch] = 1

        count = float('inf')

        for ch in balloon:
            if ch not in have:
                return 0

            possible = have[ch] // balloon[ch]
            count = min(count, possible)

        return count