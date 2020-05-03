# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        i=n
        a =0
        left =0
        right=n
        print(left,right)
        while(i>=0 or i==n):    
            if(right==left+1 or right+1==left):
                if(isBadVersion(right) and not isBadVersion(left)):
                    return right
                else:
                    return left
                
            i=(right+left)>>1
            a = isBadVersion(i)
            print(a)
            if(a):
                right=i
                
            else:
                left=i
            print(left,right)
