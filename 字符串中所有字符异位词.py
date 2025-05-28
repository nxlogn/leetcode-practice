from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """  
        对于子串问题，常使用滑动窗口来解决
        需要哪些数据结构？
        哪些数据结构在遍历的过程中对结果有影响，在什么地方会被改变？
        """
        if not s:
            return []
        
        # window：存储窗口中每个字符出现的次数
        window = {}
        # need：存储p中每个字符出现的次数
        need = {}
        # res:答案数组
        res = []
        # right,left:控制左右边界的指针
        right = 0
        left = 0

        for c in p:
            need[c] = need.get(c, 0) + 1
        
        # valid:符合p中字符出现次数的个数
        valid = 0

        # while:遍历s中的每个字符
        while right < len(s):
            c = s[right]
            right += 1
            # 当前字符是否出现在need中
            if c in need:
                # 加入window中
                window[c] = window.get(c, 0) + 1
                # 加入之后是否满足个数条件
                if window[c] == need[c]:
                    valid += 1
            # 窗口超出或等于时考虑收缩
            while right - left >= len(p):
                # 符合要求
                if valid == len(need):
                    res.append(left)
                d = s[left]
                left += 1
                # 当前字符是否出现在need中
                if d in need:
                    # 删除之前考虑valid
                    if window[d] == need[d]:
                        valid -= 1
                    # 删除
                    window[d] -= 1
        return res