class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    
    def insert(self,root,data):
        if not root:
            root = Node(data)
        else:
            current = root
            if data<current.data:
                if not current.left:
                    current.left = Node(data)
                else:
                    self.insert(current.left,data)
            elif data>current.data:
                if not current.right:
                    current.right = Node(data)
                else:
                    self.insert(current.right,data)
        return root
    
    def preorder(self,root):
        if root.left:
            self.preorder(root.left)
        if root.right:
            self.preorder(root.right)
        print root.data,
    
    def postorder(self,root):
        print root.data,
        if root.left:
            self.postorder(root.left)
        if root.right:
            self.postorder(root.right)
    
    def inorder(self,root):
        if root.left:
            self.inorder(root.left)
        print root.data,
        if root.right:
            self.inorder(root.right)
    
    def find(self,root,data):
        if root.data==data:
            print "Node is present"
        elif data<root.data and root.left:
            self.find(root.left,data)
        elif data>root.data and root.right:
            self.find(root.right,data)
        else:
            print "Node is not present"
    
    def delete(self,root,data,offset=0,before=None):
        if root.data==data:
            if root.left and root.right:
                temp = root.left
                if temp.right:
                    while temp.right:
                        prev = temp
                        temp = temp.right
                        child = temp.left
                    prev.right = child
                temp.right = root.right
                root = temp
                
                
            elif root.right and not root.left:
                root = root.right
            elif root.left and not root.right:
                root = root.left
            else:
                if before and offset == 1:
                    before.right = None
                elif before and offset == 2:
                    before.left = None
                else:
                    root = None
        elif root.left or root.right:
            current = root
            if data>root.data:
                self.delete(current.right,data,offset = 1,before = current)
            elif data<root.data:
                self.delete(current.left,data,offset = 2,before = current)
        else:
            print "Node not found"
        return root
    
    def height(self,root):
        if not root:
            return -1
        return 1+max(self.height(root.left),self.height(root.right))
