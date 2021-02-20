class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        mat = [[None for _ in range(1000)] for _ in range(numRows)]
        direction = 'up'
        row = 0
        col = 0
        for c in s:
            mat[row][col] = c
            if direction == 'up' and row == numRows-1:
                direction = 'down'
                row  = row - 1 if row != 0 else 0
                col += 1
            elif direction == 'up':
                row += 1
            elif direction == 'down' and row == 0:
                direction = 'up'
                row  = row + 1 if numRows != 1 else 0
            elif direction == 'down':
                row -= 1
                col += 1

        res = ''
        for row in mat:
            res += ''.join([c for c in row if c is not None])
        return res
                

if __name__ == '__main__':
    s = Solution()
    
    inputs = [
        ["PAYPALISHIRING", 3],
        ["PAYPALISHIRING", 4],
        ["A", 1],
        ["ABC", 1],
    ]

    outputs = [
        "PAHNAPLSIIGYIR",
        "PINALSIGYAHRPI",
        "A",
        "ABC",
    ]

    for vals, output in zip(inputs, outputs):
        string, numRows = vals[0], vals[1]
        res = s.convert(string, numRows)
        print(res)
        assert res == output
