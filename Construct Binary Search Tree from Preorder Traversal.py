class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        print(root.val)
        i = 1
        while i<len(preorder) and  preorder[i] < root.val:
            
            i+=1
        print("LEFT",preorder[1:i])
        print("RIGHT",preorder[i:])    
        root.left = self.bstFromPreorder(preorder[1:i])
        root.right = self.bstFromPreorder(preorder[i:])
        return root
