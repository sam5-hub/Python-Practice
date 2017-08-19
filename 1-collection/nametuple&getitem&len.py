import collections
from random import choice

Card = collections.namedtuple("Card", ['rank', 'suit'])

#实现len跟getitem
#序列类
class FrenchDeck:
	ranks = [str(n) for n in  range(2,11)] + list('JQKA') #字符串
	suits = 'spades diamonds clubs hearts'.split() #数组
	
	def __init__(self):
		#_cards是私人变量
		self._cards = [Card(rank, suit) for suit in self.suits
										for rank in self.ranks]
		self.ca = self._cards

	def __len__(self):
		return len(self._cards)
		
#	1.因为 __getitem__ 方法把 [] 操作交给了 self._cards 列表
#	2.所以我们的 deck 类自动支持切片（slicing）操作。
	def __getitem__(self, position):
		return self._cards[position]
		

deck = FrenchDeck()
print(choice(deck))

#倒数三个
print(deck[:3])
