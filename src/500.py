import re


class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        first = 'qwertyuiop'
        second = 'asdfghjkl'

        answer = []

        for word in words:
            firstChar = word[0].lower()

            if firstChar in first:
                headClassification = 1
            elif firstChar in second:
                headClassification = 2
            else:
                headClassification = 3

            allSameRow = True

            for c in word[1:].lower():
                if c in first:
                    charClassification = 1
                elif c in second:
                    charClassification = 2
                else:
                    charClassification = 3

                if headClassification != charClassification:
                    allSameRow = False
                    break

            if allSameRow:
                answer.append(word)

        return answer

    def findWords_UsingRE(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        answer = []
        for word in words:
            ma = re.match('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$', word)
            if ma is not None:
                answer.append(ma.group(0))

        return answer
