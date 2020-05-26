class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        lena = len(A)
        lenb= len(B)
        # print(lena,lenb)
        dp = [ [ 0 for _ in range(lenb+1) ] for _ in range(lena+1) ]
        # print(dp)
        # dp=List[List[int]]
        for i in range(1,lena+1):
            for j in range(1,lenb+1):
                if i==0 or j==0:
                    dp[i][j]=0;
                
                if A[i-1] == B[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                # pri/nt(dp)
        return dp[lena][lenb]
