
class Solution(object):
    def minOperations(self, s):
        n = len(s)

        if s == "".join(sorted(s)):
            return 0

        if n == 2:
            return -1

        mid = s[1:-1]
        lo = min(mid)
        hi = max(mid)

        if s[0] <= min(lo, s[-1]) or max(s[0], hi) <= s[-1]:
            return 1

        if s[-1] < lo and hi < s[0]:
            return 3

        return 2
