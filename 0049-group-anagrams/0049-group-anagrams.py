class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen={}
        
        for string in strs:
            sig=[0]*26
            for ch in string:
                sig[ord(ch)-97]+=1
            if tuple(sig) in seen:
                seen[tuple(sig)].append(string)
            else:
                seen[tuple(sig)]=[string]
        return seen.values()