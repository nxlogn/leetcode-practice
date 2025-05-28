from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        fast指针走前面探路，slow指针位置暂存前一个元素，当fast指针找到
        不重复元素时，slow指针加一并存储新元素
        """

        if len(nums) == 0:
            return 0
        
        fast = 1
        slow = 0

        while fast <= len(nums) - 1:
            # 遍历fast，当fast指针指向的元素和nums指针指向的元素不同
            if nums[fast] != nums[slow]:
                slow += 1
                # 维护nums[0...slow]不重复
                nums[slow] = nums[fast]
            fast += 1

        return slow + 1
        
            