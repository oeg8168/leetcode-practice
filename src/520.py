import re


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        pattern = '([A-Z]?[a-z]*|[A-Z]*)$'

        if re.match(pattern, word) is None:
            return False
        else:
            return True

    def detectCapitalUse_usingPythonFunc(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word.isupper() or word.islower() or word.istitle()
