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

## 4. 重建二叉树
```c++
/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* reConstructBinaryTree(vector<int> pre,vector<int> vin) {
        //TreeNode* root;
        if((pre.size() == vin.size()) && (pre.size() > 0))
        {
            //root->val = *pre.begin();
            //return recursion_construct(pre, vin);
            auto len = pre.size();
            return dfs(pre, 0, len - 1, vin, 0, len - 1);
                
        }
        return nullptr;
    }

    TreeNode* dfs(vector<int>& preorder, int plo, int phi, vector<int>& inorder, int ilo, int ihi) {
        if(phi < plo) return nullptr;
        TreeNode *ans = new TreeNode(preorder[plo]);
        if(plo == phi) return ans;
        int lsize = 0;

        for(auto i = inorder.begin() + ilo ; i != inorder.end(); ++i) {
            if(*i == preorder[plo]) break;
            lsize++;
        }

        ans->left = dfs(preorder, plo + 1, plo + lsize, inorder, ilo, ilo + lsize - 1);
        ans->right = dfs(preorder, plo + lsize + 1, phi, inorder, ilo + lsize + 1, ihi);
        return ans;
    }
};
```

## 5.两个栈实现队列的push和pop操作
```c++
class Solution
{
public:
    void push(int node) {
        stack1.push(node);
    }

    int pop() {
        if(stack2.empty())
        {
            if(!stack1.empty())
            {
                while(!stack1.empty())
                {
                    stack2.push(stack1.top());
                    stack1.pop();
                }
            }
            else
                return 0;
        }
        
        int res = stack2.top();
        stack2.pop();
        return res;
    }

private:
    stack<int> stack1;
    stack<int> stack2;
};
```

## 6.旋转数组最小数字
```c++
class Solution {
public:
    int minNumberInRotateArray(vector<int> rotateArray) {
        if(rotateArray.empty())
            return 0;
        
        int index1 = 0;
        int index2 = rotateArray.size()-1;
        int mid_index = index1;
        while(rotateArray[index1] >= rotateArray[index2])
        {
            if((index2 - index1) == 1)
            {
                mid_index = index2;
                break;
            }
            mid_index = (index1 + index2) / 2;
            if(rotateArray[mid_index] >= rotateArray[index1])
                index1 = mid_index;
            else //if(rotateArray[mid_index] <= rotateArray[index2])
                index2 = mid_index;
        }
        return rotateArray[mid_index];
    }
};
```

## 7.斐波那契数列
```c++
class Solution {
public:
    int Fibonacci(int n) {
        int preNum=1;
        int prePreNum=0;
        int result=0;
        if(n==0)
            return 0;
        if(n==1)
            return 1;
        for(int i=2;i<=n;i++){
            result=preNum+prePreNum;
            prePreNum=preNum;
            preNum=result;
        }
        return result;
    }
};
```

## 8.跳台阶
```c++
class Solution {
public:
    int jumpFloor(int number) {
        if(number <= 2){
            return number;
        }
        int pre2 = 1, pre1 = 2;
        for (int i = 3; i <= number; i++){
            int cur = pre2 + pre1;
            pre2 = pre1;
            pre1 = cur;
        }
        return pre1;
    }
};
```

## 9.变态跳台阶
定义$f(n)$表示跳上第n个台阶的跳法，则有$f(0)=0,f(1)=1,f(2)=2,f(n)=1+f(n-1)+f(n-2)+\cdots+f(1)$，推出$f(n-1)=1+f(n-2)+f(n-2)+\cdots+f(1)$,两式相减的$f(n)-f(n-1)=f(n-1)$，则有$f(n)=2f(n-1)$，即$f(n)$为等比数列满足$f(n)=2^{n-1}$，进一步可求$f(n)=1++f(n-1)+f(n-2)+\cdots+f(1)=2^{n-1}$.
```c++
class Solution {
public:
    int jumpFloorII(int number) {
        if(number < 1)
            return number;
        int res = 1;
        for(int i=1; i<number;++i)
        {
            res *= 2;
        }
        return res;
    }
};
```

## 10.矩形覆盖问题
```c++
class Solution {
public:
    int rectCover(int number) {
        if(number<3)
            return number;
        int pre=2, prepre=1;
        int res = 0;
        for(int i=2;i<number;++i)
        {
            res = pre+prepre;
            prepre = pre;
            pre = res;
        }
        return res;
    }
};
```

## 11.二进制中1的个数
方法一：暴力法
```c++
class Solution {
public:
     int  NumberOf1(int n) {
         int count = 0;
         int flag = 1;
         while(flag)
         {
             if(n & flag)
                 count += 1;
             flag <<= 1;
         }
         
         return count;
     }
};
```

方法二：取巧法，n&(n-1)
```c++
class Solution {
public:
     int  NumberOf1(int n) {
         int count = 0;
         int flag = 1;
         while(n)
         {
             ++count;
             n = n & (n-1);
         }
         
         return count;
     }
};
```

## 12.数值的整数次方
方法一: 暴力法
```c++
class Solution {
public:
    double Power(double base, int exponent) {
        if(equal(base, 0.0))
            return 0;
        if(exponent == 0)
            return 1;
        
        if(exponent > 0)
            return power_core(base, exponent);
        else
            return 1 / power_core(base, exponent);
    }
    
    
    int equal(double a, double b, double epision = 0.00000000001)
    {
        if(abs(a-b) < epision)
            return 1;
        else
            return 0;
    }
    
    double power_core(double b, int e)
    {
        double res = 1.0;
        while(e!=0)
        {
            res *= b;
            --e;
        }
        return res;
    }
};
```

方法二：递归高效法
```c++
class Solution {
public:
    double Power(double base, int exponent) {
        if(equal(base, 0.0))
            return 0;
        if(exponent == 0)
            return 1;
        
        if(exponent > 0)
            return power_core_recursion(base, exponent);
        else
            return 1 / power_core_recursion(base, -exponent);
    }
    
    
    int equal(double a, double b, double epision = 0.0000001)
    {
        if(abs(a-b) < epision)
            return 1;
        else
            return 0;
    }
    
    double power_core(double b, int e)
    {
        double res = 1.0;
        while(e!=0)
        {
            res *= b;
            --e;
        }
        return res;
    }
    double power_core_recursion(double b, int e)
    {
        if(e == 0)
            return 1;
        if(e == 1)
            return b;
        double res = power_core_recursion(b, e>>1);
        if((e&0x1) == 0)
        {
            return res*res;
        }
        else
            return res*res*b;
    }
};
```

## 13.调整数组顺序使奇数位于偶数前面
方法：借助额外的空间实现，空间复杂度$O(n)$
```c++
class Solution {
public:
    void reOrderArray(vector<int> &array) {
        if(!array.empty())
        {
            vector<int> odd;
            vector<int> even;
            for(auto n : array)
            {
                if((n&0x1) == 1)
                    odd.push_back(n);
                else
                    even.push_back(n);
            }
            odd.insert(odd.end(), even.begin(), even.end());
            
            array.swap(odd); //array = odd;
        }
    }
};
```

## 14. 链表中的第k个节点
方法：快慢指针法
```c++
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* FindKthToTail(ListNode* pListHead, unsigned int k) {
        ListNode* fast = pListHead;
        ListNode* slow = pListHead;
        int count = 0;
        while(fast != NULL)
        {
            fast = fast->next;
            ++count;
            if(count == k)
                break;
        }
        //判断K是否大于链表长度
        if(count != k)
            return NULL;
        
        while(fast != NULL)
        {
            fast = fast->next;
            slow = slow->next;
        }
        return slow;
    }
};
```

## 15. 翻转链表
方法：递归法或基于栈的迭代法
```c++
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* ReverseList(ListNode* pHead) {
        if(pHead != nullptr)
            return recursion_core(pHead);
        else
            return nullptr;
    }
    ListNode* recursion_core(ListNode* pHead)
    {
        if(pHead->next == nullptr)
            return pHead;
        
        ListNode* temp = pHead->next;
        ListNode* new_pHead = recursion_core(pHead->next);  # 递归得到尾节点
        pHead->next = nullptr; # 记得将每个节点next指针置为nullptr，否则链表将成为一个环
        temp->next = pHead;
        
        return new_pHead;
    }   
};
```

## 16. 合并两个有序链表
方法1：递归法pHead->next = min(pHead->next, pHead1)
方法2：将一个链表插入至另一个链表
```c++
//递归法
/*
struct ListNode {
	int val;
	struct ListNode *next;
	ListNode(int x) :
			val(x), next(NULL) {
	}
};*/
class Solution {
public:
    ListNode* Merge(ListNode* pHead1, ListNode* pHead2)
    {
        if(pHead1 == nullptr)
            return pHead2;
        if(pHead2 == nullptr)
            return pHead1;
        
        if(pHead1->val < pHead2->val)
        {
            pHead1->next = Merge(pHead1->next, pHead2);
            return pHead1;
        }
            
        else
        {
            pHead2->next = Merge(pHead2->next, pHead1);
            return pHead2;
        }
    }
    
};
```

## 17. 树的子结构



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



## 7.约瑟夫环问题
$$
f(i,m) = \left\{\begin{matrix}
0, & i=1\\ 
(f(i-1,m)+m)\%i, & i>1
\end{matrix}\right.
$$


## 24.数组中的逆序对
方法一：暴力法时间复杂度太大，无法通过。
```c++
class Solution {
public:
    int InversePairs(vector<int> data) {
        if(!data.empty())
        {
            int counter = 0;
            for(int i = 0; i < data.size()-1; ++i)
                for(int j = i+1; j < data.size(); ++j)
                {
                    if(data[j] < data[i]) counter += 1;
                }
            return counter%1000000007;
        }
    }
};
```

方法二：基于归并思想的解法$O(nlogn)$
```c++
class Solution {
public:
    int InversePairs(vector<int> data) {
        if(data.size() > 1)
        {
            vector<int> copy;
            for(auto i : data)
                copy.push_back(i);
            long long count = InversePairsCore(data, copy, 0, data.size()-1);
            return count%1000000007;
        }
        else
            return 0;
    }

    long long InversePairsCore(vector<int> &data, vector<int> &copy, int start, int end)
    {
        if(start == end)
        {
            copy[start] = data[start];
            return 0;
        }
        int length = (end - start) / 2;
        long long count_left = InversePairsCore(copy, data, start, start+length);
        long long count_right = InversePairsCore(copy, data, start+length+1, end);

        //初始化双指针
        int i = start+length;
        int j = end;
        int indexcopy=end;
        long long count=0;
        while(i >= start && j >= start+length+1)
        {
            if(data[i] > data[j])
            {
                copy[indexcopy--] = data[i--];
                count += j - (start + length);
            }
            else
                copy[indexcopy--] = data[j--];
        }

        //将剩余元素追加至copy
       for(;i>=start;i--)
           copy[indexcopy--]=data[i];
       for(;j>=start+length+1;j--)
           copy[indexcopy--]=data[j];
        return count_left + count_right + count;
    }
};
```
