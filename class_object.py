# 类与对象

'''
对象=属性+方法

对象是类的实例。换句话说，类主要定义对象的结构，然后我们以类为模板创建对象。类不但包含方法定义，而且还包含
所有实例共享的数据。
1.封装：信息隐蔽技术
2.继承：子类自动共享父类之间数据和方法的机制
3.多态：不同对象对同一方法响应不同的行动
'''
# 1


import random


class Turtle:  # Python中的类名约定以大写字母开头
    """关于类的一个简单例子"""
    # 属性
    color = 'green'
    weight = 10
    legs = 4
    shell = True
    mouth = '大嘴'

    # 方法
    def climb(self):
        print('我正在很努力的向前爬...')

    def run(self):
        print('我正在飞快的向前跑...')

    def bite(self):
        print('咬死你咬死你!!')

    def eat(self):
        print('有得吃，真满足...')

    def sleep(self):
        print('困了，睡了，晚安，zzz')


tt = Turtle()
print(tt)
# <__main__.Turtle object at 0x0000007C32D67F98>
print(type(tt))
# <class '__main__.Turtle'>
print(tt.__class__)
# <class '__main__.Turtle'>
print(tt.__class__.__name__)
# Turtle
tt.climb()
# 我正在很努力的向前爬...
tt.run()
# 我正在飞快的向前跑...
tt.bite()
# 咬死你咬死你!!
# Python类也是对象。它们是type的实例
print(type(Turtle))
# <class 'type'>

# 2.


class MyList(list):
    pass


lst = MyList([1, 5, 2, 7, 8])
lst.append(9)
lst.sort()
print(lst)
# [1, 2, 5, 7, 8, 9]

# 3.


class Animal:
    def run(self):
        raise AttributeError('子类必须实现这个方法')


class People(Animal):
    def run(self):
        print('人正在走')


class Pig(Animal):
    def run(self):
        print('pig is walking')


class Dog(Animal):
    def run(self):
        print('dog is running')


def func(animal):
    animal.run()


func(Pig())
# pig is walking


# self
'''
类的方法与普通的函数只有一个特别的区别 —— 它们必须有一个额外的第一个参数名称（对应于该实例，即该对象本
身），按照惯例它的名称是 self 。在调用方法时，我们无需明确提供与参数 self 相对应的参数。
'''


class Ball:
    def setName(self, name):
        self.name = name

    def kick(self):
        print("我叫%s,该死的，谁踢我..." % self.name)


a = Ball()
a.setName("球A")
b = Ball()
b.setName("球B")
a.kick()
# 我叫球A,该死的，谁踢我...
b.kick()
# 我叫球B,该死的，谁踢我...


# 公有与私有
''' 
在 Python 中定义私有变量只需要在变量名或函数名前加上“__”两个下划线，那么这个函数或变量就会为私有的了
'''
# 私有属性实例


class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()  # 1
counter.count()  # 2
print(counter.publicCount)  # 2
print(counter._JustCounter__secretCount)  # 2 Python的私有为伪私有
# print(counter.__secretCount)
# AttributeError: 'JustCounter' object has no attribute '__secretCount'

# 类的私有方法实例


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('Joel', 'https://blog.csdn.net/wzb_wzt')
x.who()
# name : Joel
# url : https://blog.csdn.net/wzb_wzt
x.foo()  # 这是公共方法
# x.__foo()  # 这是私有方法
# AttributeError: 'Site' object has no attribute '__foo'


# 类的继承：派生类
'''
class DerivedClassName(BaseClassName):
 <statement-1>
 .
 .
 .
 <statement-N>


BaseClassName（示例中的基类名）必须与派生类定义在一个作用域内。除了类，还可以用表达式，基类定义在另一个
模块中时这一点非常有用：
'''

# 子类中定义与父类同名的方法或属性，则会自动覆盖父类对应的方法或属性


class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    # 定义构造方法

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

# 单继承示例


class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


s = student('Joel', 10, 60, 3)
s.speak()
# Joel 说: 我 10 岁了，我在读 3 年级


class Fish:
    def __init__(self):
        self.x = random.randint(0, 10)
        self.y = random.randint(0, 10)

    def move(self):
        self.x -= 1
        print("我的位置", self.x, self.y)


class GoldFish(Fish):  # 金鱼
    pass


class Carp(Fish):  # 鲤鱼
    pass


class Salmon(Fish):  # 三文鱼
    pass


class Shark(Fish):  # 鲨鱼
    def __init__(self):
        # 调用未绑定的父类方法 Fish.__init__(self)或者使用super函数 super().__init__()；
        # 从而使该对象可以调用move()
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("吃货的梦想就是天天有得吃！")
            self.hungry = False
        else:
            print("太撑了，吃不下了！")
            self.hungry = True


g = GoldFish()
g.move()  # 我的位置 9 4
s = Shark()
s.eat()  # 吃货的梦想就是天天有得吃！
# s.move()
# AttributeError: 'Shark' object has no attribute 'x'


# 多继承
'''
class DerivedClassName(Base1, Base2, Base3):
 <statement-1>
 .
 .
 .
 <statement-N>

需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，Python 从左至右搜索，即方法在子
类中未找到时，从左到右查找父类中是否包含方法
'''


# 类定义
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class Student(People):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        People.__init__(self, n, a, w)
        self.grade = g
    # 覆写父类的方法

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


# 另一个类，多重继承之前的准备
class Speaker:
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))


# 多重继承
class Sample01(Speaker, Student):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample01("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法
# 我叫 Tim，我是一个演说家，我演讲的主题是 Python


class Sample02(Student, Speaker):
    a = ''

    def __init__(self, n, a, w, g, t):
        Student.__init__(self, n, a, w, g)
        Speaker.__init__(self, n, t)


test = Sample02("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法
# Tim 说: 我 25 岁了，我在读 4 年级


# 组合
class Turtle:
    def __init__(self, x):
        self.num = x


class Fish:
    def __init__(self, x):
        self.num = x


class Pool:
    def __init__(self, x, y):
        self.turtle = Turtle(x)
        self.fish = Fish(y)

    def print_num(self):
        print("水池里面有乌龟%s只，小鱼%s条" % (self.turtle.num, self.fish.num))


p = Pool(2, 3)
p.print_num()
# 水池里面有乌龟2只，小鱼3条


'''
类对象：创建一个类，其实也是一个对象也在内存开辟了一块空间，称为类对象，类对象只有一个。

'''


# 类对象
class A(object):
    pass


'''
实例对象：就是通过实例化类创建的对象，称为实例对象，实例对象可以有多个。
'''
# 实例化对象 a、b、c都属于实例对象。
a = A()
b = A()
c = A()

'''
类属性：类里面方法外面定义的变量称为类属性。类属性所属于类对象并且多个实例对象之间共享同一个类属性，说白了
就是类属性所有的通过该类实例化的对象都能共享。
'''


class A():
    a = xx  # 类属性

    def __init__(self):
        # 类外面，可以通过 实例对象.类属性 和 类名.类属性 进行调用。类里面，通过 self.类属性和 类名.类属性 进行调用。
        A.a = xx  # 使用类属性可以通过 （类名.类属性）调用。


'''
实例属性：实例属性和具体的某个实例对象有关系，并且一个实例对象和另外一个实例对象是不共享属性的，说白了实例
属性只能在自己的对象里面使用，其他的对象不能直接使用，因为 self 是谁调用，它的值就属于该对象。


class 类名():
   __init__(self)
    # 类外面，可以通过 实例对象.实例属性 调用。类里面，通过 self.实例属性 调用。
    self.name = xx  # 实例属性
'''
# 绑定
'''
Python 严格要求方法需要有实例才能被调用，这种限制其实就是 Python 所谓的绑定概念

Python 对象的数据属性通常存储在名为 .__ dict__ 的字典中，我们可以直接访问 __dict__ ，或利用 Python 的内置函
数 vars() 获取 .__ dict__ 。
'''


class CC:
    def setXY(self, x, y):
        self.x = x
        self.y = y

    def printXY(self):
        print(self.x, self.y)


dd = CC()
print(dd.__dict__)
# {}
print(vars(dd))
# {}
print(CC.__dict__)
# {'__module__': '__main__', 'setXY': <function CC.setXY at 0x000000C3473DA048>
# 'printXY':
# <function CC.printXY at 0x000000C3473C4F28>, '__dict__': <attribute '__dict__'
#  of 'CC' objects>,
# '__weakref__': <attribute '__weakref__' of 'CC' objects>, '__doc__': None}

dd.setXY(4, 5)
print(dd.__dict__)
# {'x': 4, 'y': 5}
print(vars(CC))
# {'__module__': '__main__', 'setXY': <function CC.setXY at 0x000000632CA9B048>, 'printXY':
# <function CC.printXY at 0x000000632CA83048>, '__dict__': <attribute '__dict__' of 'CC' objects>,
# '__weakref__': <attribute '__weakref__' of 'CC' objects>, '__doc__': None}
print(CC.__dict__)
# {'__module__': '__main__', 'setXY': <function CC.setXY at 0x000000632CA9B048>, 'printXY':
# <function CC.printXY at 0x000000632CA83048>, '__dict__': <attribute '__dict__' of 'CC' objects>,
# '__weakref__': <attribute '__weakref__' of 'CC' objects>, '__doc__': None}


# 类、属性相关函数
'''
issubclass(class, classinfo) 方法用于判断参数 class 是否是类型参数 classinfo 的子类。
2. 一个类被认为是其自身的子类。
3. classinfo 可以是类对象的元组，只要class是其中任何一个候选类的子类，则返回 True 。

'''


class A:
    pass


class B(A):
    pass


print(issubclass(B, A))  # True
print(issubclass(B, B))  # True
print(issubclass(A, B))  # False
print(issubclass(B, object))  # True

'''
isinstance(object, classinfo) 方法用于判断一个对象是否是一个已知的类型，类似 type() 。
2. type() 不会认为子类是一种父类类型，不考虑继承关系。
3. isinstance() 会认为子类是一种父类类型，考虑继承关系。
4. 如果第一个参数不是对象，则永远返回 False 。
5. 如果第二个参数不是类或者由类对象组成的元组，会抛出一个 TypeError 异常。
'''
a = 2
print(isinstance(a, int))  # True
print(isinstance(a, str))  # False
print(isinstance(a, (str, int, list)))  # True


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # True
print(type(A()) == A)  # True
print(isinstance(B(), A))  # True
print(type(B()) == A)  # False


'''
hasattr(object, name) 用于判断对象是否包含对应的属性
'''


class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()
print(hasattr(point1, 'x'))  # True
print(hasattr(point1, 'y'))  # True
print(hasattr(point1, 'z'))  # True
print(hasattr(point1, 'no'))  # False

'''
getattr(object, name[, default]) 用于返回一个对象属性值。
'''


class A(object):
    bar = 1


a = A()
print(getattr(a, 'bar'))  # 1
print(getattr(a, 'bar2', 3))  # 3
print(getattr(a, 'bar2'))
# AttributeError: 'A' object has no attribute 'bar2'


class A(object):
    def set(self, a, b):
        x = a
        a = b
        b = x
        print(a, b)


a = A()
c = getattr(a, 'set')
c(a='1', b='2')  # 2 1

'''
setattr(object, name, value) 对应函数 getattr() ，用于设置属性值，该属性不一定是存在的
'''


class A(object):
    bar = 1


a = A()
print(getattr(a, 'bar'))  # 1
setattr(a, 'bar', 5)
print(a.bar)  # 5
setattr(a, "age", 28)
print(a.age)  # 28

'''
delattr(object, name) 用于删除属性
'''


class Coordinate:
    x = 10
    y = -5
    z = 0


point1 = Coordinate()
print('x = ', point1.x)  # x = 10
print('y = ', point1.y)  # y = -5
print('z = ', point1.z)  # z = 0
delattr(Coordinate, 'z')
print('--删除 z 属性后--')  # --删除 z 属性后--
print('x = ', point1.x)  # x = 10
print('y = ', point1.y)  # y = -5
# 触发错误
print('z = ', point1.z)
# AttributeError: 'Coordinate' object has no attribute 'z'

'''
class property([fget[, fset[, fdel[, doc]]]]) 用于在新式类中返回属性值。

a. fget -- 获取属性值的函数
b. fset -- 设置属性值的函数
c. fdel -- 删除属性值函数
d. doc -- 属性描述信息
'''


class C(object):
    def __init__(self):
        self.__x = None

    def getx(self):
        return self.__x

    def setx(self, value):
        self.__x = value

    def delx(self):
        del self.__x

    x = property(getx, setx, delx, "I'm the 'x' property.")


cc = C()
cc.x = 2
print(cc.x)  # 2
