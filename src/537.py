class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = a.split('+')
        b = b.split('+')
        aReal = int(a[0])
        bReal = int(b[0])
        aImaginary = int(a[1][:-1])
        bImaginary = int(b[1][:-1])

        real = aReal * bReal - aImaginary * bImaginary
        imaginary = aReal * bImaginary + bReal * aImaginary

        return str(real) + '+' + str(imaginary) + 'i'
