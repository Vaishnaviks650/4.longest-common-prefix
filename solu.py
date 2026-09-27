class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        
        # 1. Sort the words alphabetically
        strs.sort()
        
        first = strs[0]
        last = strs[-1]
        prefix = ""
        
        # 2. Only compare the first and last word
        for i in range(min(len(first), len(last))):
            if first[i] == last[i]:
                prefix += first[i]
            else:
                break
                
        return prefix
