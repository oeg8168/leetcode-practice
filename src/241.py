import re


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        digits = re.split('[\+\-\*]', input)
        operators = re.findall('[\+\-\*]', input)

        expressions = ['N']
        currentDigitCount = 1
        totalDigitCount = len(digits)

        while currentDigitCount < totalDigitCount:
            newExpressions = []
            for expr in expressions:
                posN = [i for i, x in enumerate(expr) if x == 'N']
                replaced = [expr[:i] + '(NopN)' + expr[i + 1:] for i in posN]
                newExpressions = newExpressions + replaced

            currentDigitCount += 1
            expressions = set(newExpressions)

        ans = []
        for expr in expressions:
            for d in digits:
                expr = expr.replace('N', d, 1)
            for op in operators:
                expr = expr.replace('op', op, 1)
            ans.append(expr)

        return [eval(expr) for expr in ans]
