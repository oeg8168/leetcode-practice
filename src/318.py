class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def shareSameChar(str_1, str_2):
            for c in str_1:
                if c in str_2:
                    return True
            return False

        ans = 0
        words = [(len(word), set(word)) for word in words]

        for word_1 in words:
            for word_2 in words:
                if not shareSameChar(word_1[1], word_2[1]):
                    ans = max(ans, word_1[0] * word_2[0])

        return ans
