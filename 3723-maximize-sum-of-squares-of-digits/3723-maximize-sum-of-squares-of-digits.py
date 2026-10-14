class Solution:
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        full_nines = sum // 9
        remainder = sum % 9

        if full_nines == num:
            return "9" * num

        if remainder:
            return "9" * full_nines + str(remainder) + "0" * (num - full_nines - 1)

        return "9" * full_nines + "0" * (num - full_nines)