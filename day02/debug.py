class Solution:
    def generateMatrix(self, n: int):
        top, bottom, left, right = 0, n - 1, 0, n - 1
        nums = [[0] * n for _ in range(n)]
        count = 1
        while top <= bottom and left <= right:
            for j in range(left, right + 1):
                nums[top][j] = count
                count += 1
                top += 1
            
            for i in range(top, bottom + 1):
                nums[i][right] = count
                count += 1
                right -= 1
            
            for j in range(right, left - 1, -1):
                nums[bottom][j] = count
                count += 1
                bottom -= 1

            for i in range(bottom, top - 1, -1):
                nums[i][left] = count
                count += 1
                left += 1
        return nums


solution = Solution()
result = solution.generateMatrix(3)  # 测试n=3的情况
