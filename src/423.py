from collections import Counter


class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        def pick(s, numWord, occurrence):
            for c in numWord:
                s = s.replace(c, '', occurrence)
            return s

        ans = ''

        if 'z' in s:
            count0 = s.count('z')
            ans = ans + '0' * count0
            s = pick(s, 'zero', count0)

        if 'x' in s:
            count6 = s.count('x')
            ans = ans + '6' * count6
            s = pick(s, 'six', count6)

        if 'w' in s:
            count2 = s.count('w')
            ans = ans + '2' * count2
            s = pick(s, 'two', count2)

        if 'g' in s:
            count8 = s.count('g')
            ans = ans + '8' * count8
            s = pick(s, 'eight', count8)

        if 'h' in s:
            count3 = s.count('h')
            ans = ans + '3' * count3
            s = pick(s, 'three', count3)

        if 's' in s:
            count7 = s.count('s')
            ans = ans + '7' * count7
            s = pick(s, 'seven', count7)

        if 'r' in s:
            count4 = s.count('r')
            ans = ans + '4' * count4
            s = pick(s, 'four', count4)

        if 'f' in s:
            count5 = s.count('f')
            ans = ans + '5' * count5
            s = pick(s, 'five', count5)

        if 'i' in s:
            count9 = s.count('i')
            ans = ans + '9' * count9
            s = pick(s, 'nine', count9)

        if 'n' in s:
            count1 = s.count('n')
            ans = ans + '1' * count1
            s = pick(s, 'one', count1)

        return ''.join(sorted(ans))

    def originalDigits_anotherSolution(self, s):
        """
        :type s: str
        :rtype: str
        """
        numCount = [0 for i in range(10)]
        wordCount = Counter(s)

        numCount[0] = wordCount['z']
        numCount[2] = wordCount['w']
        numCount[4] = wordCount['u']
        numCount[6] = wordCount['x']
        numCount[8] = wordCount['g']

        numCount[1] = wordCount['o'] - numCount[0] - numCount[2] - numCount[4]
        numCount[3] = wordCount['h'] - numCount[8]
        numCount[5] = wordCount['f'] - numCount[4]
        numCount[7] = wordCount['s'] - numCount[6]
        numCount[9] = wordCount['i'] - numCount[5] - numCount[6] - numCount[8]

        ans = ''
        for num in range(10):
            ans = ans + str(num) * numCount[num]

        return ans
