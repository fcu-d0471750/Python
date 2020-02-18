'''
Binary_Search_Tree (二元搜尋樹)
'''

#=================================================================================
#class: Node
#=================================================================================
class Node():
    #==============================
    #建構子
    #==============================
    def __init__(self,Value):
        #值
        self.Value = Value
        #左邊子節點
        self.Left = None
        #右邊子節點
        self.Right = None


    #==============================
    #方法: 新增Node(根節點，新增的Node)
    #==============================
    def add_binary_search_tree_Node(self, New_Value):
        #如果沒有根節點，則將新增的Node設為根節點
        if(self.Value == None):
            self.Value = New_Value

        #如果有根節點
        else:
            #如果Root的Value > New_Value
            if(self.Value > New_Value):
                #如果根節點沒有左子節點
                if(self.Left == None):
                   self.Left = Node(New_Value)
                #如果根節點有左子節點
                else:
                    self.Left.add_binary_search_tree_Node(New_Value)

            #如果Root的Value < New_Value
            else:
                #如果根節點沒有右子節點
                if (self.Right == None):
                    self.Right = Node(New_Value)
                #如果根節點有右子節點
                else:
                    self.Right.add_binary_search_tree_Node(New_Value)


    #==============================
    #方法:印出Binary Tree(中序法)
    #==============================
    def print_binary_search_tree_inorder_traversal(self):

        if(self.Left != None):
            self.Left.print_binary_search_tree_inorder_traversal()
        print(self.Value)
        if (self.Right != None):
            self.Right.print_binary_search_tree_inorder_traversal()

    #==============================
    #方法:印出Binary Tree(前序法)
    #==============================

    def print_binary_search_tree_preorder_traversal(self):

        print(self.Value)
        if (self.Left != None):
            self.Left.print_binary_search_tree_preorder_traversal()
        if (self.Right != None):
            self.Right.print_binary_search_tree_preorder_traversal()

    #==============================
    #方法:印出Binary Tree(後序法)
    #==============================
    def print_binary_search_tree_postorder_traversal(self):

        if (self.Left != None):
            self.Left.print_binary_search_tree_postorder_traversal()
        if (self.Right != None):
            self.Right.print_binary_search_tree_postorder_traversal()
        print(self.Value)

#=================================================================================
#執行
#=================================================================================

#List測試資料
Nubmer_List = [1,2,3,4,5,6,7,8,9,10]

#設置根節點
Root = Node(Nubmer_List[0])

#建立二元搜尋樹
for i in range(1,len(Nubmer_List)):
    Root.add_binary_search_tree_Node(Nubmer_List[i])

#印出二元搜尋樹
Root.print_binary_search_tree_inorder_traversal()