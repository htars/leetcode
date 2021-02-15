class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        for i in range(len(s)):
            alphabets = [s[i]]
            length = 1
            for j in range(i+1, len(s)):
                if s[j] not in alphabets:
                    alphabets.append(s[j])
                    length += 1
                else:
                    break
            if length > max_length:
                max_length = length
        return max_length


if __name__ == '__main__':
    s = Solution()

    inputs = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "",
    ]

    outputs = [
        3,
        1,
        3,
        0,
    ]

    for string, output in zip(inputs, outputs):
        res = s.lengthOfLongestSubstring(string)
        print(res)
        assert res == output
