# Python知识点学习记录
+ https://www.cnblogs.com/zhaodafa/p/9667045.html#_label0_59
+ https://baijiahao.baidu.com/s?id=1607651363840614527&wfr=spider&for=pc

## 1. Python的垃圾回收处理机制
https://www.jianshu.com/p/1e375fb40506
https://www.jianshu.com/p/b0bc1a162933

引用计数为主（存在循环引用无法清除的问题），标记清除（解决循环引用问题）和分代回收（提高GC效率）为辅。


## 2. 正则表达式re的使用
https://www.runoob.com/python/python-reg-expressions.html
+ re.match函数：从起始位置匹配
+ re.search方法：扫描整个字符串，返回第一个匹配的对象（对象中包含匹配到元素的位置），`print(re.search('com', 'www.runoob.com').span()) `
+ re.sub(pattern, repl, string, count=0, flags=0)：用于替换字符串中的匹配项。
+ re.compile 函数：compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象
+ re.findall:在字符串中找到正则表达式所匹配的所有子串，并返回一个列表
+ re.finditer:和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回
+ re.split:方法按照能够匹配的子串将字符串分割后返回列表

从字符串中提取整数：`re.findall(r"\d+", str)`，从字符串中提取浮点数`re.findall(r"\d+\.?\d*", str)`

## 3. Python 缓存操作
```python
import functools
@functools.lru_cache(None)
```
当有的题内存溢出时，可以使用这个骚操作。
但是当递归函数传入的参数为list时，会报错“TypeError: unhashable type: 'list'”，[报错原因是](https://stackoverflow.com/questions/49210801/python3-pass-lists-to-function-with-functools-lru-cache)list属于可变类型，缓存无法确定对那些值进行缓存。解决这个问题的一种方法是，在将列表传递给缓存函数之前将列表转换为元组。

## 4. Python functools cmp_to_key操作
在使用sorted函数时，可以自定义key，但是自定义cmp函数就无法直接传入，这时可以使用`cmp_to_key`，将自定义的cmp函数转换为key，传入sorted函数中进行排序。

## 5. Python 优先级队列
https://www.cnblogs.com/kumata/p/9201571.html
原始优先级队列：`import heapq`
基于heapq的线程安全优先级队列：`from queue import PriorityQueue`
常用函数：`heapq.heappush(h, num)和heapq.heapify(nums),heapq.heappop（堆）`
Python heapq默认是小顶堆，可以将push(e)改为push(-e)，pop(e)为-pop(e)，利用这个trick得到大顶堆。


# 《Python Cookbook》第三版
## 第一章：数据结构和算法
1. 可迭代对象均可解压赋值给多个变量，部分解压可用`_`占位。
   ```python
   data=[1,2,4]
   _, a, b = data
   ```
2. `*`号表达式可以在解压时得到多个值，也可以配合`_`使用
   ```python
   data = [10,1,2,4,5,3]
   head, *body, tail = data  # body = [1,2,4,5]
   ```
3. python的双端队列：`from collections import deque`
4. python的堆（小顶堆）：`import heapq`，可以基于`heapq`实现优先级队列，如果要用于多线程则需要增加适当的锁和信号量机制
5. 实现字典中的键映射多个值：
   + value部分可以使用列表、集合或者其他容器
   + 使用`defaultdict`容器：`from collections import defaultdict`，在初始化字典时可以更简洁

6. 实现字典在迭代或序列化时元素是顺序的：`from collections import OrderedDict`
7. 求字典中value的最大最小值及对应的key，使用zip函数实现:
   ```python
   prices = {'ACME': 45.23,'AAPL': 612.78,'IBM': 205.55,'HPQ': 37.20,'FB': 10.75}
   min_price = min(zip(prices.values(), prices.keys())) # min_price is (10.75, 'FB')
   max_price = max(zip(prices.values(), prices.keys())) # max_price is (612.78, 'AAPL')
   ```
8. 序列中出现次数最多的元素：`from collections import Counter`
9. 通过某个关键字或多个关键字对字典列表进行排序`from operator import itemgetter`或者lambda表达式实现，但是前者速度更快一些
10. 过滤序列元素，通常可以使用列表推导，但是数据量很大时就会大量占用内存，这时候可以使用生成器表达式：
    ```python
    mylist = [1, 4, -5, 10, -7, 2, 3, -1]
    [n for n in mylist if n > 0]  # 列表推导
    pos = (n for n in mylist if n > 0) # 生成器表达式
    ```
    如果过滤规则比较复杂，则可以使用`filter`函数。
11. 获取一个字典的子集：使用字典推导
12. 映射名称到序列元素，使序列元素的可读性更强，使用了python的工厂方法：`from collections import namedtuple`
13. 生成器比列表推导的效率更高
    ```python
    nums = [1, 2, 3, 4, 5]
    s = sum([x * x for x in nums]) # 列表推导，会先创建一个临时列表
    s = sum((x * x for x in nums)) # 显示的传递一个生成器表达式对象
    s = sum(x * x for x in nums) # 更加优雅的实现方式，省略了括号
    ```
14. 合并多个字典或映射：
    + `from collections import ChainMap`不产生新字典，只是逻辑上合为一个字典，且原字典改变后合并字典也会改变
    + 使用`update()`方法，合并后生成一个独立的新字典


## 第二章：字符串和文本


~~End of file~~