class Solution:
    def reverse(self, x: int) -> int:
        n = str(int(str(abs(x))[::-1]))
        if self._is_negative(x):
            n = '-' + n
        n = int(n)
        if not self._is_range(n):
            n = 0
        return n

    def _is_range(self, x):
        x_min = - 2 ** 31
        x_max = 2 ** 31 -1
        return x_min <= x and x <= x_max

    def _is_negative(self, x):
        return x < 0


if __name__ == '__main__':
    s = Solution()

    inputs = [
        123,
        -123,
        120,
        0,
        1534236469,
    ]

    outputs = [
        321,
        -321,
        21,
        0,
        0,
    ]

    for x, output in zip(inputs, outputs):
        res = s.reverse(x)
        print(res, output)
        assert res == output
