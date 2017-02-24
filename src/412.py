class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        answer = []

        for num in range(1, n + 1):
            if num % 15 == 0:
                answer.append('FizzBuzz')
            elif num % 3 == 0:
                answer.append('Fizz')
            elif num % 5 == 0:
                answer.append('Buzz')
            else:
                answer.append(str(num))

        return answer

    def fizzBuzz_anotherSolution(self, n):
        return [str(i) if (i % 3 != 0 and i % 5 != 0) else ('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0)) for i in range(1, n + 1)]
