# 使用C++二刷《剑指offer》
之前使用Python刷过一遍[《剑指offer》](https://nbviewer.jupyter.org/github/doctorsrn/coding-and-interview/blob/master/CodingInterviewChinese2.ipynb)，这次再使用C++刷一遍，复习复习C++。

主要使用[牛客网](https://www.nowcoder.com/ta/coding-interviews)和[AcWing](https://www.acwing.com/problem/)这两个网站进行评测，AcWing在线调试比较方便。


## 1. 二维数组的查找
```c++
class Solution {
public:
    bool Find(int target, vector<vector<int> > array) {
        if(!array.empty() && array[0].size() > 0) //array[0].size() > 0这个条件判断必须要添加
        {
            int row = 0;
            int col = array.size()-1;
            while(row < array.size() && col >= 0)
            {
                if(array[row][col] == target)
                {
                    return true;
                }
                else if(array[row][col] > target)
                {
                    --col;
                }
                else
                {
                    ++row;
                }
            }
        }
        
        return false;
    }
};

```

## 2. 替换空格
Python写多了忘记区分C++中字符和字符串的表示方法了，字符是单引号，字符串是双引号，所以使用`*(str+i) != " "`程序就会编译不成功。
```c++
class Solution {
public:
    // length表示原始有效字符的长度
	void replaceSpace(char *str,int length) {
        if(str != nullptr)
        {
            int count = 0;
            for(int i = 0; i < length; ++i)
            {
                if(*(str+i) == ' ')
                    ++count;
            }
            
            for(int i = length-1; i >= 0; --i)
            {
                if(*(str+i) != ' ')
                {
                    *(str+2*count+i) = *(str+i);
                }
                else
                {
                    --count;
                    *(str+2*count+i) = '%';
                    *(str+2*count+i+1) = '2';
                    *(str+2*count+i+2) = '0';
                }
            }
        }
        return ;
	}
};
```
