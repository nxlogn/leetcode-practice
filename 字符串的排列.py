class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """  
        判断字符串s1的排列之一是否为s2的子串
        返回true或者false
        """
        
        window = {}
        need = {}
        left = 0
        right = 0
        valid = 0
        
        # 初始化need
        for c in s1:
            need[c] = need.get(c, 0) + 1
            
        # 扩展滑动窗口，遍历每一个字符    
        while right < len(s2):
            c = s2[right]
            right += 1
            
            # c出现在need中，更新数据
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1
            
            # 当窗口长度大于s1长度时，需要收缩
            while right - left >= len(s1):
                # 当前子串满足条件
                if valid == len(need):
                    return True
                
                # 移除左边的字符
                d = s2[left]
                left += 1
                
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    
        return False
