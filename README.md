# README

### 简介

实现德州扑克的两人对战

### 功能

运行主模块Poker.py，程序随机洗混 52 张牌、给两名玩家发 5 张公共牌和代表两个玩家的各 2 张底牌后，以德州扑克 (Poker) 规则判断赢家。

### 模块

+ Dealer.py：Dealer裁判类
+ Card.py：Card扑克牌类
+ rule.py：Pattern牌型类

### 实现思路

#### Card

有花色和点数两个属性，通过定义< 和 > 运算实现点数比较

#### Pattern

cards属性是5张Card构成的列表，初始化时调用判断牌型方法和计算总权重方法

有一系列判断牌型的方法，`find_pattern()` 对这些方法依次调用

获取权重方法 `find_weight()` ：由6位16进制数构成：最高位表示牌型，与数字的对照见_pattWeightDict，其余5位表示五张牌，对牌大小决定性更强的牌排在前面。如 两对 【Q Q J 7 7】 的总权重为 【0x3cc77b】

#### Dealer

+ 构造函数中生成牌堆
+ shuffle方法洗牌，从第一张开始发牌
+ deal方法按顺序发牌，已发过的牌不再发出
+ judge方法构造Pattern类得到牌型和总权重
+ new_game方法新开一局，执行以上三个方法，输出结果信息