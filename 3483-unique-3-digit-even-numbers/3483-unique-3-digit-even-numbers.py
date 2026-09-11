class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        count=[0]*10
        for d in digits:
            count[d]+=1
        ans=0
        for a in range(1,10):
            for b in range(0,10):
                for c in range(0,10,2):
                    used=[0]*10
                    used[a]+=1
                    used[b]+=1
                    used[c]+=1
                    valid=True
                    for d in range(10):
                        if used[d]>count[d]:
                            valid=False
                            break
                    if valid:
                        ans+=1
        return ans