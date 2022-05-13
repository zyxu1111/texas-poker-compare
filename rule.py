from Card import Card

class Pattern:
    """ 5张牌判断牌的类型 """
    _pattWeightDict = {'皇家同花顺': 10,
                '同花顺': 9,
                '四条': 8,
                '葫芦': 7,
                '同花': 6,
                '顺子': 5,
                '三条': 4,
                '两对': 3,
                '一对': 2,
                '散牌': 1}
    
    def __init__(self, cards):
        cards.sort(reverse=True)
        self.cards = cards
        self.find_pattern()
        self.find_weight()
    
    def __repr__(self):
        return ' '.join([str(c) for c in self.cards])

    def is_same_suit(self):
        """ 判断是相同花色 """
        cards = self.cards
        for c in cards:
            if c.suit != cards[0].suit:
                return False
        return cards[0].real_point
    
    def is_shun(self):
        """ 判断5张牌属于顺 """
        cards = self.cards
        for index, c in enumerate(cards):
            if index != 0 and c.point != cards[index-1].point - 1:
                return False
        return cards[0].real_point
    
    @staticmethod
    def is_same_point(cardsList):
        """ 判断若干张牌的点数相同 """
        for c in cardsList:
            if c.point != cardsList[0].point:
                return False
        return True
    
    def is_royal_flush(self):
        """ 判断是皇家同花顺 """
        cards = self.cards
        if self.is_same_suit() and self.is_shun() and cards[0].point == 14:
            return "AKQJ10"
        else:
            return False
        
    def is_straight_flush(self):
        """ 判断是同花顺 """
        cards = self.cards
        if self.is_same_suit() and self.is_shun() and cards[0].point != 14:
            return cards[0].real_point+'带头'
        else:
            return False
        
    def is_four_of_a_kind(self):
        """ 判断是四条 """
        cards = self.cards
        if self.is_same_point(cards[:4]):
            return cards[0].real_point
        elif self.is_same_point(cards[1:5]):
            cards.append(cards.pop(0)) # 将四条牌移到最前面
            return cards[0].real_point
        else:
            return False
        
    def is_full_house(self):
        """ 判断是葫芦 """
        cards = self.cards
        # 大带小
        if self.is_same_point(cards[:3]) and self.is_same_point(cards[3:]):
            return cards[0].real_point+'带'+cards[3].real_point
        # 小带大
        elif self.is_same_point(cards[:2]) and self.is_same_point(cards[2:]):
            # 把三张的牌移到前面
            self.cards = cards[2:] + cards[:2]
            return self.cards[0].real_point+'带'+self.cards[3].real_point
        else:
            return False
        
    def is_flush(self):
        """ 判断是同花 """
        cards = self.cards
        if self.is_same_suit() and not self.is_shun():
            return cards[0].real_point
        else:
            return False
        
    def is_straight(self):
        """ 判断是顺子 """
        cards = self.cards
        if self.is_shun() and not self.is_same_suit():
            return cards[0].real_point+'带头'
        else:
            return False
    
    def is_three_of_a_kind(self):
        """ 判断是三条 """
        cards = self.cards
        if self.is_same_point(cards[:3]):
            return cards[0].real_point
        elif self.is_same_point(cards[1:4]):
            # 将三条牌移到最前面
            self.cards = cards[1:4] + [cards[0], cards[-1]]
            return self.cards[0].real_point
        else:
            return False
        
    def is_two_pair(self):
        """ 判断是两对 """
        if not self.is_four_of_a_kind() and not self.is_full_house():
            cards = self.cards
            # x x y y z
            if self.is_same_point(cards[:2]) and self.is_same_point(cards[2:4]):
                return cards[0].real_point +'和'+cards[2].real_point
            # x x z y y
            elif self.is_same_point(cards[:2]) and self.is_same_point(cards[-2:]):
                # 将对子牌移到最前面
                self.cards = cards[:2] + cards[-2:] + [cards[2]]
                return self.cards[0].real_point +'和'+self.cards[2].real_point
            # z x x y y
            elif self.is_same_point(cards[1:3]) and self.is_same_point(cards[3:]):
                # 将对子牌移到最前面
                cards.append(cards.pop(0))
                return self.cards[0].real_point +'和'+self.cards[2].real_point
            else:
                return False
        else:
            return False
        
    def is_one_pair(self):
        """ 判断是一对 """
        cards = self.cards
        # x x a b c
        if self.is_same_point(cards[:2]):
            return cards[0].real_point
        # a x x b c
        elif self.is_same_point(cards[1:3]):
            # 将对子牌移到最前面
            self.cards = cards[1:3] + [cards[0], cards[3], cards[4]]
            return cards[0].real_point
        # a b x x c
        elif self.is_same_point(cards[2:4]):
            # 将对子牌移到最前面
            self.cards = cards[2:4] + [cards[0], cards[1], cards[4]]
            return cards[0].real_point
        # a b c x x
        elif self.is_same_point(cards[3:]):
            # 将对子牌移到最前面
            self.cards = cards[3:] + [cards[0], cards[1], cards[2]]
            return cards[0].real_point
        else:
            return False
        
    def find_pattern(self):
        """ 获取牌的类型 """
        if self.is_royal_flush():
            pattern, info = '皇家同花顺', self.is_royal_flush()
        elif self.is_straight_flush():
            pattern, info = '同花顺', self.is_straight_flush()
        elif self.is_four_of_a_kind():
            pattern, info = '四条', self.is_four_of_a_kind()
        elif self.is_full_house():
            pattern, info = '葫芦', self.is_full_house()
        elif self.is_flush():
            pattern, info = '同花', self.is_flush()
        elif self.is_straight():
            pattern, info = '顺子', self.is_straight()
        elif self.is_three_of_a_kind():
            pattern, info = '三条', self.is_three_of_a_kind()
        elif self.is_two_pair():
            pattern, info = '两对', self.is_two_pair()
        elif self.is_one_pair():
            pattern, info = '一对', self.is_one_pair()
        else:
            pattern, info = '散牌', self.cards[0].real_point
        self.__pattern = pattern
        self.__info = info
    
    def find_weight(self):
        """ 获取牌的总权重 """
        pattWeight = Pattern._pattWeightDict[self.__pattern] << 4*5
        subWeight = sum([card.point << 4*(4-index) \
             for index, card in enumerate(self.cards)])
        self.__weight = pattWeight + subWeight
        
    @property
    def pattern(self):
        return self.__pattern
    
    @property
    def info(self):
        return self.__info
    
    @property
    def weight(self):
        return self.__weight
        
    
if __name__ == "__main__":
    patt = Pattern([Card('C',2),
                   Card('H',12),
                   Card('D',12),
                   Card('S',10),
                   Card('H',10)]) 
    print(patt)
    print(patt.is_two_pair())
