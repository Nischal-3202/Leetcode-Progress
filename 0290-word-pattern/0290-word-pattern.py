class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        words = s.split()
        if len(pattern) != len(words):
            return False
        mapping = {}
        used = set()
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            if char in mapping:
                if mapping[char] != word:
                    return False
            else:
                if word in used:
                    return False
                mapping[char] = word
                used.add(word)
        return True