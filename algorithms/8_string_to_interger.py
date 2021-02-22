INT_MIN = -2**31
INT_MAX = 2**31-1

class Solution:
    def myAtoi(self, s: str) -> int:
        if s.strip() == "":
            return 0
        
        word = [w for w in s.split(' ') if w != ''][0]
        val = ''
        for i, c in enumerate(word):
            if i == 0 and (c == '-' or c == '+'):
                val += c
            elif c.isdigit():
                val += c
            else:
                break
        if val == '' or val == '-' or val == '+':
            return 0
        else:
            val = int(val)

        if val < INT_MIN:
            return INT_MIN
        elif val > INT_MAX:
            return INT_MAX
        else:
            return val
        

if __name__ == '__main__':
    s = Solution()

    inputs = [
        "42",
        "   -42",
        "4193 with words",
        "words and 987",
        "-91283472332",
        "3.14159",
        "  -0012a42",
        "+1",
    ]

    outputs = [
        42,
        -42,
        4193,
        0,
        -2147483648,
        3,
        -12,
        1,
    ]

    for string, output in zip(inputs, outputs):
        res = s.myAtoi(string)
        print(res, output)
        assert res == output
