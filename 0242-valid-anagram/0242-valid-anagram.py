class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t): return False
        seen={}
        for ch in s:
            if ch in seen:
                seen[ch]+=1
            else:
                seen[ch]=1
        for ch in t:
            if ch in seen:
                seen[ch]-=1
                if seen[ch] < 0: return False
            else:
                return False
        return True