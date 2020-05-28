class Solution:
    def countBits(self, num: int) -> List[int]:
        out = [0] * (num + 1)
        for i in range(num+1):
            out[i] = out[i // 2] + (i & 1)
        return out
    
    
