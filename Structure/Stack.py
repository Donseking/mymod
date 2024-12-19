class Stack( object ) :
    # > 數據結構 [ 棧 ]
    def __init__(self):
        self.items = []

    # FUN 判斷 棧 是否為空
    def is_empty( self ) :
        return self.items == []
    
    # FUN 彈出 棧
    def pop ( self ) :
        if self.is_empty() :
            raise IndexError("棧內無物") 
        return self.items.pop()
    
    # FUN 加入棧
    def push( self, item) :
        return self.items.append(item)
    
    # FUN 棧頂元素
    def peek( self ) :
        if self.is_empty() :
            raise IndexError("棧內無物") 
        return self.items[len(self.items)-1]
    
    # FUN 棧的大小
    def size( self ) :
        return len(self.items)
    
    # FUN 轉換成字符串
    def __restr__(self):
        return "".join(self.items)