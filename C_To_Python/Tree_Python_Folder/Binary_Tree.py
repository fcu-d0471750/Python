'''
Binary Tree (二元樹)
'''

#=================================================================================
#class: Node
#=================================================================================
class Node():
    #==============================
    #建構子
    #==============================
    def __init__(self,Value,ID):
        #值
        self.Value = Value
        #左邊子節點
        self.Left = None
        #右邊子節點
        self.Right = None
        #編號
        self.ID = ID

    #==============================
    #方法: 新增Node(根節點，新增的Value , 編號)
    #==============================
    def add_binary_tree_Node(self, New_Value, ID):
        # 如果沒有根節點，則將新增的Value設為根節點的Value
        if (self.Value == None):
            self.Value = New_Value
            self.ID = ID

        #如果ID偶數，則表示此Node是在左邊
        if (ID%2 == 0):
            #如果根節點沒有左子節點
            if (self.Left == None):
                self.Left = Node(New_Value, ID)
            #如果根節點有左子節點
            else:
                self.Left.add_binary_tree_Node(New_Value,ID)

        #如果ID奇數，則表示此Node是在右邊
        else:
            #如果根節點沒有右子節點
            if (self.Right == None):
                self.Right = Node(New_Value, ID)
            #如果根節點有右子節點
            else:
                self.Right.add_binary_tree_Node(New_Value,ID)

    #==============================
    #方法:　印出Binary Tree(中序法)
    #==============================
    def print_binary_tree_inorder_traversal(self):

        if (self.Left != None):
            self.Left.print_binary_tree_inorder_traversal()
        print(self.Value)
        if (self.Right != None):
            self.Right.print_binary_tree_inorder_traversal()
#=================================================================================
#執行
#=================================================================================

#List測試資料
Number_List = [2,3,4,5,6,7,8,9,10]

#設置根節點
Root = Node(Number_List[0] , 1)

#建立二元樹((i+1)是因為編號是從1開始，而List是從0開始)
for i in range(1,len(Number_List)):
    Root.add_binary_tree_Node(Number_List[i] , (i+1))

#印出二元樹
Root.print_binary_tree_inorder_traversal()