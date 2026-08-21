class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=['a','e','i','o','u','A','E','I','O','U']
        string=list(s)
        left=0
        right=len(s)-1
        while left < right:
            while left < right and string[left] not in vowels:
                left+=1
            while left < right and string[right] not in vowels:
                right -=1
            string[left],string[right]=string[right],string[left]
            left +=1
            right -= 1
        return ''.join(string)