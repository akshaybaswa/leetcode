class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: #since reverse of negative cannot be same
            return False
        
        return str(x) == str(x)[::-1]

