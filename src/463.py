class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        perimeter += grid[0].count(1)
        perimeter += grid[-1].count(1)

        for i, row in enumerate(grid):
            prev = 0
            for j, element in enumerate(row):
                if element != prev:
                    perimeter += 1
                    prev = element

                # upper
                if element != grid[max(0, i - 1)][j]:
                    perimeter += 1

            if prev == 1:
                perimeter += 1

        return perimeter

# another solution: 4*island - 2*neighbor
