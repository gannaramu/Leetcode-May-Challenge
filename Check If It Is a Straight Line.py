class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0=coordinates[0][0]
        y0=coordinates[0][1]
        # print(x0,y0)
        if(y0-coordinates[1][1]!=0):
            m=(x0-coordinates[1][0])/(y0-coordinates[1][1])
        else:
            m=-1
        print(m)
        for i in range(2,len(coordinates)-1):
            if(y0-coordinates[i][1]!=0):
            
                if ((x0-coordinates[i][0])/(y0-coordinates[i][1])==m):
                    continue
                else:
                    print(x0,y0,coordinates[i][0],coordinates[i][1])
                    return 0
           
                
        return 1
