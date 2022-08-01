class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        string=str(x)
        string=string[::-1]
        try:
            if int(string)==x:
                return True
            else:
                return False
        except:
            return False
            
        
        
        