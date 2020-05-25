class Solution:
    def frequencySort(self, s: str) -> str:
        dct={}
        for c in s:
            if c not in dct:
                dct[c]=1
            else:
                dct[c]+=1
        print(dct)
        a={k: v for k, v in sorted(dct.items(), key=lambda item: item[1])}
        print(a)
        answer=""
        
        while(a):
            k,v = a.popitem()
            for i in range(v):
                answer =answer + k
                
        return answer
                
