
'''
package 包

包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
Python中的包是一个包含多个模块文件的目录，按包来组织模块。
创建包分为三个步骤：
1. 创建一个文件夹，用于存放相关的模块，文件夹的名字即包的名字。
2. 在文件夹中创建一个 __init__.py 的模块文件，内容可以为空。
目录只有包含一个叫做 __init__.py 的文件才会被认作是一个包，最简单的情况，放一个空的 __init__.py 就可以
了。
3. 将相关的模块放入文件夹中。

十二分注意：

不要将自己的模块文件名与Python自带的模块名冲突。

不要将自己的模块文件名与Python自带的模块名冲突。

不要将自己的模块文件名与Python自带的模块名冲突。

例如：内置的time模块，你自己创建的py文件就不要命名成time.py，否则就不能正常使用内置的time模块了。
'''
