class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        list1=s.split()
        s= " ".join(list1[::-1])

        return s