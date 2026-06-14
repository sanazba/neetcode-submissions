class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # both nodes are null
        if not p and not q:
            return True
        
        # one is null OR values do not match
        if not p or not q or p.val != q.val:
            return False
        
        # recursively check left and right
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)