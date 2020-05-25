class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        if matrix is None or len(matrix) == 0:
            return 0
        result =0
        cell =0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==1:
                    if i==0 or j==0:
                        result+=1

                    else:
                        cell= min(matrix[i][j-1],matrix[i-1][j-1],matrix[i-1][j])+  matrix[i][j]
                        result += cell
                        matrix[i][j] = cell

        return result
