class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct={}
        for i in nums:
            if i not in dct:
                dct[i]=1
            else:
                dct[i]+=1
        
        print(dct)
        d = [k for k, v in dct.items() if v >= (len(nums)/2)]
        return d[0]
        
