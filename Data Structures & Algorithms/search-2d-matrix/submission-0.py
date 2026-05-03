class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nrow, ncol = len(matrix), len(matrix[0])
        top, bot = 0, nrow - 1
        while top <= bot:
            row = (top + bot) // 2
            if target > matrix[row][-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bot = row - 1
            else:
                break
        finalRow = (top + bot) // 2
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[finalRow][m]:
                l = m + 1
            elif target < matrix[finalRow][m]:
                r = m - 1
            else:
                return True
        return False