class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Split string into words, remove extra spaces
        words = s.split()
        # Reverse the list of words
        words.reverse()
        # Join back with a single space
        return " ".join(words)
