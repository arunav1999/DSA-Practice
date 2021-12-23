# Bruteforce Approach:

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        triangle.append([1])
        for i in range(1,numRows):
            temp = []
            temp.append(1)
            for j in range(len(triangle[i-1])-1):
                s = triangle[i-1][j] + triangle[i-1][j+1]
                temp.append(s)
            temp.append(1)
            triangle.append(temp)
        return triangle

# Optimized Approach

'''

Use the formula r-1Cc-1
For generating a row:
say 5th row, do:
kepp iterating r-1Ci
4C0 4C1 4C2 4C3 4C4

'''