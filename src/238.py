class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 1:
            return [1]
        if len(nums) == 2:
            return [nums[1], nums[0]]

        if nums.count(0) > 1:
            return [0] * len(nums)

        allProduct = 1
        for num in nums:
            if num == 0:
                allProduct *= 1
            else:
                allProduct *= num

        if nums.count(0) == 1:
            ans = [0] * len(nums)
            ans[nums.index(0)] = allProduct
        else:
            ans = [allProduct // i for i in nums]

        return ans

    def productExceptSelf_withoutDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        product = 1
        for num in nums:
            ans.append(product)
            product *= num

        product = 1
        for i, num in enumerate(nums[::-1]):
            ans[len(nums) - i - 1] *= product
            product *= num

        return ans
