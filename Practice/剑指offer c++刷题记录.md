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

## 23.链表中环节点的检测
```c++
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if(head == nullptr)
            return nullptr;
        
        ListNode *slow = head->next;
        if(slow == nullptr)
            return nullptr;
        
        ListNode *fast = slow->next;
        if(fast == nullptr)
            return nullptr;
        //countCycleNodes(slow);
        int cycle_nodes_count = 0;
        while(fast != nullptr && slow != nullptr)
        {
            if(fast == slow)
            {
                cycle_nodes_count = countCycleNodes(slow);
                break;
            }
                
            
            slow = slow->next;
            fast = fast->next;
            if(fast != nullptr)
                fast = fast->next;
        }
        if(cycle_nodes_count == 0)
            return nullptr;
        
        slow = head;
        fast = head;
        while(cycle_nodes_count > 0)
        {
            fast = fast->next;
            --cycle_nodes_count;
        }
        while(slow != fast)
        {
            slow = slow->next;
            fast = fast->next;
        }
        return slow;
    }
    
    // 统计环中节点的个数
    int countCycleNodes(const ListNode *node_in_cycle) {
        ListNode *slow = node_in_cycle->next;
        ListNode *fast = slow->next;
        int count = 1;
        while(slow != fast)
        {
            fast = fast->next;
            ++count;
        }
        return count;
    }
};
```

## 3. 从尾到头打印链表
使用栈记录链表，然后从尾到头打印
```c++
/**
*  struct ListNode {
*        int val;
*        struct ListNode *next;
*        ListNode(int x) :
*              val(x), next(NULL) {
*        }
*  };
*/
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        std::vector<int> res;
        if(head != nullptr)
        {
            std::stack<ListNode*> nodes;
            ListNode* node = head;
            while(node != nullptr)
            {
                nodes.push(node);
                node = node->next;
            }
            while(!nodes.empty())
            {
                node = nodes.top();
                res.push_back(node->val);
                nodes.pop();
            }
        }
        return res;
    }
};
```

顺序遍历并将值存入数组，然后倒序输出数组
```c++
class Solution {
public:
    vector<int> printListFromTailToHead(ListNode* head) {
        std::vector<int> res;
        if(head != nullptr)
        {
            std::stack<ListNode*> nodes;
            ListNode* node = head;
            while(node != nullptr)
            {
                res.push_back(node->val);
                node = node->next;
            }
            
        }
        return vector<int>(res.rbegin(), res.rend());  // 倒序迭代器
    }
};
```
