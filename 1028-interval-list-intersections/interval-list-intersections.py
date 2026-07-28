class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        ans =[]
        i=0
        j=0
        while i < len(firstList) and j < len(secondList):
            s1 = firstList[i][0]
            e1 = firstList[i][1]
            s2 = secondList[j][0]
            e2 = secondList[j][1]
            start = max(s1, s2)
            end = min(e1, e2)
            if start <= end:
                ans.append([start,end])

            if e1 > e2:
                j+=1
            elif e2>e1:
                i+=1
            else:
                i+=1
                j+=1
        return ans
                    
        