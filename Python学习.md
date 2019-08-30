# Python知识点学习记录

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

