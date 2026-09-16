class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        integer_val1 = int(a, 2)
        integer_val2 = int(b, 2)
        new_val = integer_val1+integer_val2
        return bin(new_val)[2:]