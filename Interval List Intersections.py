class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        result = []
        for i,j in A:
            for m,n in B:
                # print(i,j,m,n)
                if (j>=m and n>=i):
                    result.append([max(i,m),min(j,n)])
        return result
