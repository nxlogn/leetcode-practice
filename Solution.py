class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """  
        在s1中寻找是否有子串包含s2的全部字符
        返回true或者false
        """

        window = {}
        need = {}
        left = 0
        right = 0
        valid = 0
        # 初始化need
        for c in s2:
            need[c] = need.get(c, 0) + 1
        # 扩展滑动窗口，遍历每一个字符    
        while right < len(s1):
            c = s1[right]
            right += 1

            # c出现在need中，更新数据
            if c in need:
                window[c] = window.get(c, 0) + 1
            if window[c] == need[c]:
                valid += 1

            # 收缩滑动窗口，更新数据
            while right - left <= len(need):
                # 当前子串满足条件
                if valid == len(need):
                    return True
                
                # d出现在need中，更新数据
                d = s1[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False
