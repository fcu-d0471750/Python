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
    def __init__(self,Value):
        #值
        self.Value = Value
        #左邊子節點
        self.Left = None
        #右邊子節點
        self.Right = None


    #==============================
    #方法: 新增左子節點(根節點，新增的Node)
    #==============================
    def add_binary_tree_left_Node(self, New_Value):
        #如果根節點沒有左子節點
        if(self.Left == None):
            self.Left = Node(New_Value)
        else:
            self.Left.add_binary_tree_left_Node(New_Value)

    #==============================
    #方法:新增右子節點(根節點，新增的Node)
    #==============================
    def add_binary_tree_right_Node(self, New_Value):
        #如果根節點沒有右子節點
        if(self.Right == None):
            self.Right = Node(New_Value)
        else:
            self.Right.add_binary_tree_right_Node(New_Value)


#=================================================================================
#執行
#=================================================================================

#List測試資料
Nubmer_List = [1,2,3,4,5,6,7,8,9,10]

#設置根節點
Root = Node(Nubmer_List[0])

#建立二元樹


