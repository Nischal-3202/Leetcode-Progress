class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo={}
        ans=False
        def match(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            if j==len(p):
                return i == len(s)
        
            current_match= i<len(s) and (s[i]==p[j] or p[j] == ".")
            if j+1 < len(p) and p[j+1]=="*":
                ans= match(i,j+2) or (current_match and match(i+1,j))
            elif current_match:
                ans=match(i+1,j+1)
            else:
                ans=False
            memo[(i,j)]=ans
            return ans
        return match(0,0)