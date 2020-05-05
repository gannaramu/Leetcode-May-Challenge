class Solution:
    def firstUniqChar(self, s: str) -> int:
        dct={}
        if not s:
            return -1
        for c in s:
            if c not in dct:
                dct[c]=1
            else:
                dct[c]+=1
            
            # if(sum(dct.values())==1):
                
     
        # print(dct.popitem())
        for i in range(len(s)):
            if(dct[s[i]]==1):
                return i
        
        return -1
            
