"""
You are given an n x n 2D matrix representing an image, 
rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, 
which means you have to modify the input 2D matrix directly. 

DO NOT allocate another 2D matrix and do the rotation.
"""
from typing import List
import numpy as np

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # # cheat but adequate solution with numpy
        # matrix[:] = np.rot90(np.array(matrix), axes=(1, 0)).tolist()
        
        # pain-in-the-ass solution
        n = len(matrix)
        i = 0
        j = n - 1
        while j > i:
            matrix[i], matrix[j] = matrix[j], matrix[i]
            i += 1
            j -= 1
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
    
if __name__ == '__main__':
    s = Solution()
    
    # Test case 1
    matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
    excepted1 = [[7,4,1],[8,5,2],[9,6,3]]
    s.rotate(matrix1)
    assert matrix1 == excepted1, f"Test Case 1 Failed: expected output {excepted1}, but got {matrix1}"
    
    # Test case 2
    matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    excepted2 = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    s.rotate(matrix2)
    assert matrix2 == excepted2, f"Test Case 2 Failed: expected output {excepted2}, but got {matrix2}"
    
    