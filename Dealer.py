import random
from Card import Card
from rule import Pattern
from itertools import combinations

    
class Dealer(object):
    """ 裁判类 """
    def __init__(self):
        # 构造52张的牌堆
        self.__deck = [Card(s, p) for s in Card._suitDict.keys() \
             for p in Card._pointDict.keys()]
        # 已发过牌的数量
        self.__dealtCard = 0
        
    def shuffle(self):
        # 洗牌方法
        random.shuffle(self.__deck)
        self.__dealtCard = 0
        
    def deal(self, cardNum):
        # 发一定数量的牌
        if type(cardNum) is int and cardNum>0:
            dealtCard = self.__dealtCard
            if dealtCard + cardNum <= 52:
                self.__dealtCard += cardNum
                return self.__deck[dealtCard:dealtCard+cardNum]
            else:
                raise(ValueError('剩余牌数量不足，请重新洗牌'))
        else:
            raise(ValueError('发牌数量为正整数'))        
        
    @staticmethod
    def judge(cards7):
        """ 调用rule模块得到牌型和总权重 """
        cards7.sort(reverse=True)
        cmb = combinations(cards7, 5) # 遍历7张牌中所有的5张牌组合
        maxWeight = 0 # 记录最大牌型的权重
        for cards in cmb:
            cards = list(cards)
            patt = Pattern(cards)
            if patt.weight > maxWeight:
                bestPatt = patt 
                maxWeight = patt.weight
        return bestPatt, maxWeight
        
    def new_game(self):
        """ 开始新的一局 """
        # 洗牌
        self.shuffle()
        
        # 发牌
        hole1 = self.deal(2)
        hole2 = self.deal(2)
        river = self.deal(5)
        print('玩家{0}的手牌为[{1}]和[{2}]'.format(1, hole1[0], hole1[1]))
        print('玩家{0}的手牌为[{1}]和[{2}]'.format(2, hole2[0], hole2[1]))
        print('河牌为[{}]'.format(' '.join([str(c) for c in river])))
        
        # 确定牌型
        p1, w1 = self.judge(hole1+river)
        p2, w2 = self.judge(hole2+river)
        print('玩家{0}的最终牌型：{1}[{2}] ({3})' \
                  .format(1, p1.pattern, p1.info, hex(w1)))
        print('玩家{0}的最终牌型：{1}[{2}] ({3})' \
                  .format(2, p2.pattern, p2.info, hex(w2)))
            
        # 判断赢家
        if w1 > w2:
            print('玩家1胜出')
        elif w1 < w2:
            print('玩家2胜出')
        else:
            print('平局')
            
        
if __name__=="__main__":
    # 发确定的牌型用于调试
    d = Dealer()
    hole1 = [Card('H', 14), Card('H',2)]
    hole2 = [Card('H', 7), Card('H',6)]
    river = [Card('H',4), Card('H',3), Card('H',5), Card('H',9), Card('H',8)]
    print('玩家{0}的手牌为[{1}]和[{2}]'.format(1, hole1[0], hole1[1]))
    print('玩家{0}的手牌为[{1}]和[{2}]'.format(2, hole2[0], hole2[1]))
    print('河牌为[{}]'.format(' '.join([str(c) for c in river])))
    
    # 确定牌型
    p1, w1 = d.judge(hole1+river)
    p2, w2 = d.judge(hole2+river)
    print('玩家{0}的最终牌型：{1}[{2}] ({3})' \
              .format(1, p1.pattern, p1.info, hex(w1)))
    print('玩家{0}的最终牌型：{1}[{2}] ({3})' \
              .format(2, p2.pattern, p2.info, hex(w2)))
        
    # 判断赢家
    if w1 > w2:
        print('玩家1胜出')
    elif w1 < w2:
        print('玩家2胜出')
    else:
        print('平局')

    
    

