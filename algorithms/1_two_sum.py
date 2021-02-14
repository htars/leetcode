from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)-1):
            n1 = nums[i]
            for j in range(i+1, len(nums)):
                n2 = nums[j]
                if (n1+n2) == target:
                    return [i, j]


if __name__ == '__main__':
    s = Solution()

    inputs = [
        [2, 7, 11, 15],
        [3, 2, 4],
        [3, 3],
    ]

    targets = [
        9,
        6,
        6,
    ]

    outputs = [
        [0, 1],
        [1, 2],
        [0, 1]
    ]

    for nums, target, output in zip(inputs, targets, outputs):
        result = s.twoSum(nums, target)
        print(result)
        assert result == output
    
