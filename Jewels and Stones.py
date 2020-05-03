class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count =0
        for char in S:
            for j in J:
                if(char== j):
                    count=count+1;
        return count
