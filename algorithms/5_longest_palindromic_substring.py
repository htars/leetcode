class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        if len(s) == 2:
            if self._is_palindrome(s):
                return s
            else:
                return s[0]

        max_length = 0
        max_length_paralindrome_substring = ''
        for i in range(len(s)-1):
            for j in range(i+1, len(s)):
                substring = s[i:j+1]
                if self._is_palindrome(substring) and len(substring) > max_length:
                    max_length = len(substring)
                    max_length_paralindrome_substring = substring
            if max_length > len(s[i:]):
                break

        if max_length == 0:
            return s[0]

        return max_length_paralindrome_substring

    def _is_palindrome(self, substring):
        return substring == substring[::-1]


if __name__ == '__main__':
    s = Solution()

    inputs = [
        "babad",
        "cbbd",
        "a",
        "ac",
    ]

    outputs = [
        "bab",
        "bb",
        "a",
        "a",
    ]

    for string, output in zip(inputs, outputs):
        res = s.longestPalindrome(string)
        assert res == output
