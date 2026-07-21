class Solution(object):
    def merge(self, intervals):
        intervals.sort(key = lambda i : i[0])
        output = [intervals[0]]

        for start,end in intervals[1:]:
            lastend = output[-1][1]
            if start <= lastend:
                output[-1][1] = max(end,lastend)
            else:
                output.append([start,end])

        return output