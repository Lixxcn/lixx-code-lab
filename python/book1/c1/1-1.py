import collections  # 导入collections模块，它包含了一些有用的容器类型

# 使用collections.namedtuple创建一个名为Card的命名元组，它有两个字段：rank和suit
Card = collections.namedtuple("Card", ["rank", "suit"])

# 定义一个名为FrenchDeck的类，代表一副法式扑克牌
class FrenchDeck:
    # 初始化扑克牌的等级列表，这里用列表推导式创建了从2到10的字符串表示，然后使用+操作符拼接了"JQKA"
    ranks = [str(n) for n in range(2, 11)] + list("JQKA")
    # 初始化扑克牌的花色列表，使用split()方法从字符串中分割出各个花色
    suits = "spades diamonds clubs hearts".split()

    # 构造器，当创建FrenchDeck的实例时，会自动调用这个方法
    def __init__(self):
        # 使用列表推导式创建所有的牌，它是一个嵌套循环，外层循环遍历所有的花色，内层循环遍历所有的等级
        # 每个循环的迭代产生一张牌，它是Card命名元组的实例
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    # 定义一个方法，用于获取牌堆的大小，这里实现了特殊方法__len__
    def __len__(self):
        # 返回_cards列表的长度，即牌堆中牌的数量
        return len(self._cards)

    # 定义一个方法，用于通过索引获取牌堆中的牌，这里实现了特殊方法__getitem__
    def __getitem__(self, position):
        # 返回_cards列表中指定位置position的牌
        return self._cards[position]
