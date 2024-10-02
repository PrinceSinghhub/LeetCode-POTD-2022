class BST:
    def __init__(self,root):
        self.root = root
        self.Lchild = None
        self.Rchild = None

    def insertion(self,data):
        if self.root == None:
            self.root = data

        if self.root == data:
            pass

        if self.root>data:
            if self.Lchild:
                self.Lchild.insertion(data)
            else:
                self.Lchild = BST(data)

        if self.root<data:
            if self.Rchild:
                self.Rchild.insertion(data)

            else:
                self.Rchild = BST(data)

       # todo in order traversal

    def in_order_traversal(self):

        if self.Lchild != None:
            self.Lchild.in_order_traversal()

        print(self.root, end=" ")

        if self.Rchild != None:
            self.Rchild.in_order_traversal()


root=BST(None)
# root1 = [2, 1, 4]
# root2 = [1, 0, 3]

root1 = [1,8]
root2 = [8,1]
for i in root1:
    root.insertion(i)
for j in root2:
    root.insertion(j)
root.in_order_traversal()

