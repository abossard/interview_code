class BinaryTree(object):
    
    root = None
    
    class Node(object):
        parent = None
        data = None
        left = None
        right = None
        def __init__(self, parent, data):
            self.parent = parent
            self.data = data
        def __str__(self):
            output = ''
            if self.left:
                output += "%s < "%(self.left,)
            if self.data:
                output += "%s (P:%s)"%(self.data,self.parent.data)
            if self.right:
                output += " <= %s"%(self.right,)
            return output
                
            
    def insert(self, data):
        if not self.root:
            self.root = self.Node(None, data)
        else:
            self._insert_below(self.root, data)
            
    def _insert_below(self, node, data):
        if data < node.data:
            if node.left:
                self._insert_below(node.left, data)
            else:
                node.left = self.Node(node, data)
        else:
            if node.right:
                self._insert_below(node.right, data)
            else:
                node.right = self.Node(node, data)

    def find(self, data):
        if not self.root:
            return None
        else:
            return self._find_below(self.root, data)
            
    def _find_below(self, node, data):
        if data == node.data:
            return node
        elif data < node.data:
            return self._find_below(node.left, data) if node.left else None
        else:
            return self._find_below(node.right, data) if node.right else None
            
    
    def remove(self, data):
        node = self.find(data)
        if not node:
            return None
        parent = node.parent
        promoted_node = None
        if parent and data < parent.data:
            if node.right:
                promoted_node = node.right
            if node.left:
                if promoted_node:
                    promoted_node.left = node.left
                else:
                    promoted_node = node.left
        else:
            if node.left:
                promoted_node = node.left
            if node.right:
                if promoted_node:
                    promoted_node.right = node.right
                else:
                    promoted_node = node.right
        if parent:
            promoted_node.parent = parent
        else:
            self.root = promoted_node
        return node, promoted_node
    
    def __str__(self):
        return "BinaryTree: %s"%(self.root,) 
        
tree = BinaryTree()
import random
numbers = [x for x in range(1,99)]
random.shuffle(numbers)
for x in numbers:
    tree.insert(x)
#print tree.find(7)
tree = BinaryTree()
tree.insert(0)
tree.insert(1)
tree.insert(2)
tree.insert(3)
oldnode, newnode = tree.remove(0)
print "%s - %s"% (oldnode,newnode,)