class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def larger(a,b):
            if len(a)>len(b):
                return a
            else: 
                return b
        left=-1
        right=-1
        max_palindrome=""
        
        for i in range(len(s)):
            o_pal,e_pal="",""
            left,right=i,i
            while left >=0 and right < len(s):
                
                if s[left]!=s[right]:
                    break
                left -=1
                right +=1
            o_pal=s[left+1:right]

            left=i 
            right=i+1
            while left>=0 and right < len(s):
                if s[left] != s[right]:
                    break
                left-=1
                right+=1
            e_pal=s[left+1:right]
            max_palindrome=larger(max_palindrome,larger(o_pal,e_pal))
        return max_palindrome
        
                
                