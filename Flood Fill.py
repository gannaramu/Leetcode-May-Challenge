class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
                
        def helper(image,x,y,newColor,color):
            # print(x,y)
            if(x<0 or x>=len(image) or y<0 or y>=len(image[0])):        
                return 
            if(image[x][y]==color):
                image[x][y]=newColor
                helper(image,x,y+1,newColor,color)
                helper(image,x,y-1,newColor,color)
                helper(image,x+1,y,newColor,color)
                helper(image,x-1,y,newColor,color)
            else:
                return
          
        color = image[sr][sc]
        if color==newColor:
            return image
        else:
            helper(image,sr,sc,newColor,color)
        return image

    
