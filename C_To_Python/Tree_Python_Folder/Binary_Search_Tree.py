'''
Binary Search Tree (二元搜尋樹)
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
    #方法: 新增Node(根節點，新增的Value)
    #==============================
    def add_binary_search_tree_Node(self, New_Value):
        #如果沒有根節點，則將新增的Value設為根節點的Value
        if(self.Value == None):
            self.Value = New_Value

        #如果有根節點
        else:
            #如果根節點的Value > New_Value
            if(self.Value > New_Value):
                #如果根節點沒有左子節點
                if(self.Left == None):
                   self.Left = Node(New_Value)
                #如果根節點有左子節點
                else:
                    self.Left.add_binary_search_tree_Node(New_Value)

            #如果根節點的Value < New_Value
            else:
                #如果根節點沒有右子節點
                if (self.Right == None):
                    self.Right = Node(New_Value)
                #如果根節點有右子節點
                else:
                    self.Right.add_binary_search_tree_Node(New_Value)


    #==============================
    #方法:印出Binary Search Tree(中序法)
    #==============================
    def print_binary_search_tree_inorder_traversal(self):

        if(self.Left != None):
            self.Left.print_binary_search_tree_inorder_traversal()
        print(self.Value)
        if (self.Right != None):
            self.Right.print_binary_search_tree_inorder_traversal()

    #==============================
    #方法:印出Binary Search Tree(前序法)
    #==============================

    def print_binary_search_tree_preorder_traversal(self):

        print(self.Value)
        if (self.Left != None):
            self.Left.print_binary_search_tree_preorder_traversal()
        if (self.Right != None):
            self.Right.print_binary_search_tree_preorder_traversal()

    #==============================
    #方法:印出Binary Search Tree(後序法)
    #==============================
    def print_binary_search_tree_postorder_traversal(self):

        if (self.Left != None):
            self.Left.print_binary_search_tree_postorder_traversal()
        if (self.Right != None):
            self.Right.print_binary_search_tree_postorder_traversal()
        print(self.Value)

    #==============================
    #方法: 搜尋Binary Search Tree的Value(Value:要搜尋的值)
    #==============================
    def findvalue(self , Value):
        #如果沒有根節點，表示沒有任何value存在
        if (self.Value == None):
            return print(Value , 'was not found')
        if(self.Value == Value):
            return print(Value, 'was found')

        #如果有根節點
        else:
            #如果根節點的Value > Value
            if (self.Value > Value):
                #如果根節點沒有左子節點，表示沒有更小的Value
                if (self.Left == None):
                    return print(Value , 'was not found')
                #如果根節點有左子節點
                else:
                    self.Left.findvalue(Value)

            #如果根節點的Value < Value
            else:
                #如果根節點沒有右子節點，表示沒有更大的Value
                if (self.Right == None):
                    return print(Value , 'was not found')
                #如果根節點有右子節點
                else:
                    self.Right.findvalue(Value)

    #==============================
    #方法: 找出要刪除的Node的右子樹中，最小的Node
    #==============================
    def minValueNode(self):
        #要刪除的Node
        Temp = self

        #如果還有左子樹，代表還不是右子樹中，最小的Node
        while (Temp.Left != None):
            Temp = Temp.Left

        return Temp

    #==============================
    #方法: 刪除Binary Search Tree的Value(Value:要刪除的值)
    #Case1：欲刪除之node沒有child pointer。
    #Case2：欲刪除之node只有一個child pointer(不論是leftchild或rightchild)。
    #Case3：欲刪除之node有兩個child pointer。
    #==============================
    def deletevalue(self , Value):

        if(self.Value > Value):
            #如果根節點沒有左子節點，表示沒有更小的Value，也就是沒有存在要刪除的值
            if(self.Left==None):
                print(Value, 'was not found')
                #回傳沒改變的Tree
                return self
            #如果根節點有左子節點
            else:
                self.Left = self.Left.deletevalue(Value)

        elif(self.Value < Value):
            #如果根節點沒有右子節點，表示沒有更大的Value，也就是沒有存在要刪除的值
            if(self.Right==None):
                print(Value, 'was not found')
                #回傳沒改變的Tree
                return self
            #如果根節點有右子節點
            else:
                self.Right = self.Right.deletevalue(Value)

        #self.Value == Value
        else:
            #Case1、2
            if(self.Left == None):
                Temp = self.Right
                self = None
                return Temp
            elif(self.Right == None):
                Temp = self.Left
                self = None
                return Temp

            #Case3
            #找出右子樹中，最小的Node
            Temp = self.Right.minValueNode()

            #將要刪除的Node的Value改成右子樹中，最小的Node的Value
            self.Value = Temp.Value

            #從右子樹開始找出，最小的Node，將其刪除
            #因為self.Value = Temp.Value已經將要刪除的Node的Value交替成，符合二元搜尋樹的Value
            self.Right = self.Right.deletevalue(Temp.Value)

        return self
#=================================================================================
#執行
#=================================================================================

#List測試資料
Nubmer_List = [2,1,3,4,5,6,7,8,9,10]

#設置根節點
Root = Node(Nubmer_List[0])

#建立二元搜尋樹
for i in range(1,len(Nubmer_List)):
    Root.add_binary_search_tree_Node(Nubmer_List[i])

#印出二元搜尋樹
Root.print_binary_search_tree_inorder_traversal()
#換行
print()
#刪除
Root = Root.deletevalue(1)

#印出二元搜尋樹
Root.print_binary_search_tree_inorder_traversal()