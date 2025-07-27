# Spiral Matrix mostly about code not algorithm
# Key Note:
# 1.init a matrix first
# 2.use n // 2 to calculate how many loops we need to draw
# 3.use n % 2 to calculate whether we need to draw the [mid][mid]
# 4.use count to filled in the number
# 5.use offset to narrow down the range every loop
# 6.dont forget to start another part of loop from the next cell, not the
# one we stopped before.

# First solution:
# draw the first cell and excludes the end cell
# Need to handle the [mid][mid] in the end if n % 2 != 0
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        start_x, start_y = 0, 0
        loop, mid = n // 2, n // 2
        count, offset = 1, 1
        while loop > 0:
            i, j = start_x, start_y # can be delete because define it in for loop
            for j in range(start_y, n - offset):
                nums[start_x][j] = count
                count += 1
            
            for i in range(start_x, n - offset):
                nums[i][n - offset] = count
                count += 1
            
            for j in range(n - offset, start_y, -1):
                nums[n - offset][j] = count
                count += 1
            
            for i in range(n - offset, start_x, -1):
                nums[i][start_y] = count
                count += 1
            
            start_x += 1
            start_y += 1
            loop -= 1
            offset += 1
        if n % 2 != 0:
            nums[mid][mid] = count
        return nums
    
# Second Solution:
# Four bouders
# Draw every cells
# Need to handle [mid][mid] because it works in condition of top == bottom,
# left == right
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []
        
        nums = [[0] * n for _ in range(n)]
        mid = n // 2
        top, bottom, left, right = 0, n - 1, 0, n - 1
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

            for i in range(bottom, top - 1, - 1):
                nums[i][left] = count
                count += 1
            left += 1         
        return nums

# If removes top == bottom, left == right, check n % 2 != 0 in the end
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n <= 0:
            return []
        
        nums = [[0] * n for _ in range(n)]
        mid = n // 2
        top, bottom, left, right = 0, n - 1, 0, n - 1
        count = 1
        while top < bottom and left < right:
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

            for i in range(bottom, top - 1, - 1):
                nums[i][left] = count
                count += 1
            left += 1
        if n % 2 != 0:
            nums[mid][mid] = count
            
        return nums
