from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """  
        给你一个数组 nums 和一个值 val，你需要原地移除所有数值等于val的元素。
        元素的顺序可能发生改变。然后返回 nums中与val不同的元素的数量。
        """

        if not nums:
            return 0

        # slow指针:该位置应该放什么元素
        slow = 0
        # fast指针:该位置元素是否和val相同
        fast = 0
        while fast < len(nums):
            # 不等于val则将该元素存储在slow位置
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            # 等于val则跳过
            fast += 1
        return slow
