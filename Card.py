class Card:
    back = "蓝色方格花纹"
    _suitDict = {'C':'梅花', 'D':'方块', 'H':'红桃', 'S':'黑桃'}
    _pointDict = {2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7',\
                 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K', 14:'A'}
    
    def __init__(self, suit, point):
        self.__suit = suit
        self.__point = point
        
    def __repr__(self):
        return Card._suitDict[self.__suit]+Card._pointDict[self.__point]
    
    def desc(self):
        print("这是一张花色为{0}，点数为{1}，牌背为{2}的扑克牌~"\
              .format(Card._suitDict[self.__suit], \
                      Card._pointDict[self.__point], \
                      self.back))
            
    def change_back(self, new_back):
        self.back = new_back
    
    def __eq__(self, other):
        # 定义 == 运算
        if self.__point == other.point and self.__suit == other.suit:
            return True
        else:
            return False
    
    def __lt__(self, other):
        # 定义 < 运算
        return (self.__point < other.point)
        
    def __gt__(self, other):
        # 定义 > 运算
        return (self.__point > other.point)
        
    @property
    def suit(self):
        return self.__suit
    
    @property
    def point(self):
        # 数字形式的点数2~14
        return self.__point
    
    @property
    def real_point(self):
        # 字符串形式的点数
        return Card._pointDict[self.__point]
    
            

