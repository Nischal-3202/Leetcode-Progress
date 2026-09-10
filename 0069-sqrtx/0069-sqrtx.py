class Solution(object):
    def mySqrt(self, x):
        if x < 2:
            return x
        guess = x
        while True:
            new_guess = (guess + x // guess) // 2
            if new_guess >= guess:
                return guess
            guess = new_guess