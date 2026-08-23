class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        res=[]
        for char in s:
            if char == '(' or char == '{' or char == '[':
                res.append(char)
            elif char == ')' and res and res[-1]=='(':
                res.pop()
            elif char == '}' and res and res[-1]=='{':
                res.pop()
            elif char == ']' and res and res[-1]=='[':
                res.pop()
            else:
                return False
        return len(res)==0