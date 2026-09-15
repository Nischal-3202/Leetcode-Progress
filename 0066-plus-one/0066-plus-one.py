class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        number="".join(str(d) for d in digits)
        number=str(int(number)+1)
        return [int(char) for char in number]
