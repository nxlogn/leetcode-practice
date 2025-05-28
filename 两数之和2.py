from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """  
        固定一个元素num，在剩下的元素中找到target-nums的另一个元素
        """
        # 左右指针
        left = 0
        right = len(numbers) - 1

        # left和right从两边往内部靠
        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            # sum较小,移动left
            elif sum < target:
                left += 1
            # sum较大,移动right
            elif sum > target:
                right -= 1
