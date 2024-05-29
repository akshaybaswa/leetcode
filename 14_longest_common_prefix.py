class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        l_prefix = ''
        sorted_strs = sorted(strs)
        f = sorted_strs[0]
        l = sorted_strs[-1]
        for i in range(min(len(f), len(l))):
            if f[i] != l[i]:
                return l_prefix
            else:
                l_prefix += f[i]
