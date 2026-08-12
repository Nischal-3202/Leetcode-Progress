class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        lps=[0]*len(needle)
        i=1
        j=0
        while i< len(needle):
            if needle[i]==needle[j]:
                j+=1
                lps[i]=j
                i+=1
            else:
                if j != 0:
                    j=lps[j-1]
                else:
                    lps[i]=0
                    i+=1
        i=0
        j=0
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                if j==len(needle):
                    return i-j
            else:
                if j != 0 :
                    j=lps[j-1]
                else:
                    i+=1
        return -1
                