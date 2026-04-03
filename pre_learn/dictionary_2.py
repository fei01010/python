#7.3.2删除为特定值的所有列表元素
pets = ['gouliang', 'tianrun', 'xiiugou']
while 'gouliang' in pets:
    pets.remove('gouliang')

print(pets)
#tips:-1指的是插入到列表的最后一个元素之前
if 'gouliang' not in pets:
    pets.insert(0, 'guijie')
    pets.insert(-1, 'booya')
print(pets)