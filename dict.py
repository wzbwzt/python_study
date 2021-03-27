#字典
'''
可变类型与不可变类型

1. 序列是以连续的整数为索引，与此不同的是，字典以"关键字"为索引，关键字可以是任意不可变类型，通常用字符串
或数值。
2. 字典是 Python 唯一的一个 映射类型，字符串、元组、列表属于序列类型。


那么如何快速判断一个数据类型 X 是不是可变类型的呢？两种方法：
1. 麻烦方法：用 id(X) 函数，对 X 进行某种操作，比较操作前后的 id ，如果不一样，则 X 不可变，如果一样，则
X 可变。
2. 便捷方法：用 hash(X) ，只要不报错，证明 X 可被哈希，即不可变，反过来不可被哈希，即可变
'''
i = 1
print(id(i)) # 140732167000896
i = i + 2
print(id(i)) # 140732167000960
l = [1, 2]
print(id(l)) # 4300825160
l.append('Python')
print(id(l)) # 4300825160


'''
1. 数值、字符和元组 都能被哈希，因此它们是不可变类型。
2. 列表、集合、字典不能被哈希，因此它是可变类型。
'''
print(hash('Name')) # -9215951442099718823
print(hash((1, 2, 'Python'))) # 823362308207799471
# print(hash([1, 2, 'Python']))
# TypeError: unhashable type: 'list'
# print(hash({1, 2, 3}))
# TypeError: unhashable type: 'set'


'''
字典 是无序的 键:值（ key:value ）对集合，键必须是互不相同的（在同一个字典之内）。
1. dict 内部存放的顺序和 key 放入的顺序是没有关系的。
2. dict 查找和插入的速度极快，不会随着 key 的增加而增加，但是需要占用大量的内存

字典 定义语法为 {元素1, 元素2, ..., 元素n}
1. 其中每一个元素是一个「键值对」-- 键:值 ( key:value )
2. 关键点是「大括号 {}」,「逗号 ,」和「冒号 :」
3. 大括号 -- 把所有元素绑在一起
4. 逗号 -- 将每个键值对分开
5. 冒号 -- 将键和值分开
'''

#创建和访问字典

dic1 = {1: 'one', 2: 'two', 3: 'three'}
print(dic1) # {1: 'one', 2: 'two', 3: 'three'}
print(dic1[1]) # one
# print(dic1[4]) # KeyError: 4
dic2 = {'rice': 35, 'wheat': 101, 'corn': 67}
print(dic2) # {'wheat': 101, 'corn': 67, 'rice': 35}
print(dic2['rice']) # 35
12345678

#通过元组作为 key 来创建字典，但一般不这样使用。
dic = {(1, 2, 3): "Tom", "Age": 12, 3: [3, 5, 7]}
print(dic) # {(1, 2, 3): 'Tom', 'Age': 12, 3: [3, 5, 7]}
print(type(dic)) # <class 'dict'>

#dict() -> 创建一个空的字典
dic = dict()
dic['a'] = 1
dic['b'] = 2
dic['c'] = 3
print(dic)
# {'a': 1, 'b': 2, 'c': 3}
dic['a'] = 11
print(dic)
# {'a': 11, 'b': 2, 'c': 3}
dic['d'] = 4
print(dic)
# {'a': 11, 'b': 2, 'c': 3, 'd': 4}

#dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs
dic1 = dict([('apple', 4139), ('peach', 4127), ('cherry', 4098)])
print(dic1) # {'cherry': 4098, 'apple': 4139, 'peach': 4127}
dic2 = dict((('apple', 4139), ('peach', 4127), ('cherry', 4098)))
print(dic2) # {'peach': 4127, 'cherry': 4098, 'apple': 4139}

#dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. 
#For example: dict(one=1, two=2)
#键只能为字符串类型，并且创建的时候字符串不能加引号，加上就会直接报语法错误
dic = dict(name='Tom', age=10)
print(dic) # {'name': 'Tom', 'age': 10}
print(type(dic)) # <class 'dict'>

#字典的内置方法
'''
dict.fromkeys(seq[, value]) 用于创建一个新字典，以序列 seq 中元素做字典的键， value 为字典所有键对
应的初始值。
'''
seq = ('name', 'age', 'sex')
dic1 = dict.fromkeys(seq)
print("新的字典为 : %s" % str(dic1)) 
# 新的字典为 : {'name': None, 'age': None, 'sex': None}
dic2 = dict.fromkeys(seq, 10)
print("新的字典为 : %s" % str(dic2)) 
# 新的字典为 : {'name': 10, 'age': 10, 'sex': 10}
dic3 = dict.fromkeys(seq, ('小马', '8', '男'))
print("新的字典为 : %s" % str(dic3)) 
# 新的字典为 : {'name': ('小马', '8', '男'), 'age': ('小马', '8', '男'), 'sex': ('小马', '8', '男')}

'''
dict.keys() 返回一个可迭代对象，可以使用 list() 来转换为列表，列表为字典中的所有键
'''

dic = {'Name': 'lsgogroup', 'Age': 7}
print(dic.keys()) # dict_keys(['Name', 'Age'])
lst = list(dic.keys()) # 转换为列表
print(lst) # ['Name', 'Age']

'''
dict.values() 返回一个迭代器，可以使用 list() 来转换为列表，列表为字典中的所有值。

'''
dic = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print("字典所有值为 : ", list(dic.values())) 
# 字典所有值为 : [7, 'female', 'Zara']

'''
dict.items() 以列表返回可遍历的 (键, 值) 元组数组。
'''
dic = {'Name': 'Lsgogroup', 'Age': 7}
print("Value : %s" % dic.items()) 
# Value : dict_items([('Name', 'Lsgogroup'), ('Age', 7)])
print(tuple(dic.items())) 
# (('Name', 'Lsgogroup'), ('Age', 7))



'''
dict.get(key, default=None) 返回指定键的值，如果值不在字典中返回默认值。

'''
dic = {'Name': 'Lsgogroup', 'Age': 27}
print("Age 值为 : %s" % dic.get('Age')) # Age 值为 : 27
print("Sex 值为 : %s" % dic.get('Sex', "NA")) # Sex 值为 : NA

'''
dict.setdefault(key, default=None) 和 get() 方法 类似, 如果键不存在于字典中，将会添加键并将值设为默
认值。
'''
dic = {'Name': 'Lsgogroup', 'Age': 7}
print("Age 键的值为 : %s" % dic.setdefault('Age', None)) # Age 键的值为 : 7
print("Sex 键的值为 : %s" % dic.setdefault('Sex', None)) # Sex 键的值为 : None
print("新字典为：", dic) 
# 新字典为： {'Age': 7, 'Name': 'Lsgogroup', 'Sex': None}

'''
key in dict in 操作符用于判断键是否存在于字典中，如果键在字典 dict 里返回 true ，
否则返回 false 。 而 not in 操作符刚好相反，如果键在字典 dict 里返回 false ，否则返回 true 。
'''
dic = {'Name': 'Lsgogroup', 'Age': 7}
# in 检测键 Age 是否存在
if 'Age' in dic:
 print("键 Age 存在")
else:
 print("键 Age 不存在")

'''
dict.pop(key[,default]) 删除字典给定键 key 所对应的值，返回值为被删除的值。 key 值必须给出。若 key
不存在，则返回 default 值。
del dict[key] 删除字典给定键 key 所对应的值。
'''
dic1 = {1: "a", 2: [1, 2]}
print(dic1.pop(1), dic1) # a {2: [1, 2]}

# 设置默认值，必须添加，否则报错
print(dic1.pop(3, "nokey"), dic1) # nokey {2: [1, 2]}
del dic1[2]
print(dic1) # {}

'''
dict.popitem() 随机返回并删除字典中的一对键和值，如果字典已经为空，却调用了此方法，就报出KeyError异
'''
dic1 = {1: "a", 2: [1, 2]}
print(dic1.popitem()) # (1, 'a')
print(dic1) # {2: [1, 2]}

'''
dict.clear() 用于删除字典内所有元素。
'''
dic = {'Name': 'Zara', 'Age': 7}
print("字典长度 : %d" % len(dic)) # 字典长度 : 2
dict.clear()
print("字典删除后长度 : %d" % len(dic)) # 字典删除后长度 : 0

'''
dict.copy() 返回一个字典的浅复制
'''
dic1 = {'Name': 'Lsgogroup', 'Age': 7, 'Class': 'First'}
dic2 = dic1.copy()
print("新复制的字典为 : ", dic2) 
# 新复制的字典为 : {'Age': 7, 'Name': 'Lsgogroup', 'Class': 'First'}

#直接赋值和 copy 的区别
dic1 = {'user': 'lsgogroup', 'num': [1, 2, 3]}
# 引用对象
dic2 = dic1 
# 深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
dic3 = dic1.copy() 
print(id(dic1)) # 148635574728
print(id(dic2)) # 148635574728
print(id(dic3)) # 148635574344
# 修改 data 数据
dic1['user'] = 'root'
dic1['num'].remove(1)
# 输出结果
print(dic1) # {'user': 'root', 'num': [2, 3]}
print(dic2) # {'user': 'root', 'num': [2, 3]}
print(dic3) # {'user': 'runoob', 'num': [2, 3]}

'''
dict.update(dict2) 把字典参数 dict2 的 key:value 对 更新到字典 dict 里
'''
dic = {'Name': 'Lsgogroup', 'Age': 7}
dic2 = {'Sex': 'female', 'Age': 8}
dic.update(dic2)
print("更新字典 dict : ", dic) 
# 更新字典 dict : {'Sex': 'female', 'Age': 8, 'Name': 'Lsgogroup'}