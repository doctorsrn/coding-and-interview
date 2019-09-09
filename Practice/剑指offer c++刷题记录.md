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
方法：分为两步，第一步递归遍历树，第二步遍历的同时递归判断是否为子树。递归遍历树可以使用VLR前序遍历。
```c++
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    bool HasSubtree(TreeNode* pRoot1, TreeNode* pRoot2)
    {
        if(pRoot2 == nullptr || pRoot1 == nullptr)
            return false;
        
        if(isEqual(pRoot1, pRoot2))
            return true;
        if(pRoot1->left != nullptr)
        {
            if(HasSubtree(pRoot1->left, pRoot2))
                return true;
        }
            
        if(pRoot1->right != nullptr)
        {
            if(HasSubtree(pRoot1->right, pRoot2))
                return true;
        }
            
        return false;
    }
    bool isEqual(TreeNode* pRoot1, TreeNode* pRoot2)
    {
        if(pRoot2 == nullptr)
            return true;
        if(pRoot1 == nullptr)
            return false;
        
        if(pRoot1->val == pRoot2->val)
            return isEqual(pRoot1->left, pRoot2->left) && isEqual(pRoot1->right, pRoot2->right);
        else
            return false;
    }
};
```

## 18. 二叉树的镜像
方法：VLR递归遍历进行左右交换
```c++
/*
struct TreeNode {
	int val;
	struct TreeNode *left;
	struct TreeNode *right;
	TreeNode(int x) :
			val(x), left(NULL), right(NULL) {
	}
};*/
class Solution {
public:
    void Mirror(TreeNode *pRoot) {
        if(pRoot == nullptr or (pRoot->left == nullptr && pRoot->right == nullptr))
            return;
        
        TreeNode* left = pRoot->left;
        TreeNode* right = pRoot->right;
        pRoot->left = right;
        pRoot->right = left;
        Mirror(pRoot->left);
        Mirror(pRoot->right);

    }
};
```

## 19. 顺时针打印矩阵
注意边界值
```c++
class Solution {
public:
    vector<int> printMatrix(vector<vector<int> > matrix) {
        int row = matrix.size();
        int col = matrix[0].size();
        
        int start = 0;
        vector<int> res;
        while(row > start * 2 && col > start *2)
        {
            Print(matrix, row, col, start, res);
            ++start; 
        }
        return res;
    }
    void Print(const vector<vector<int> > & matrix, int row, int col, int start, vector<int>& res)
    {
        int end_x = col - start - 1;
        int end_y = row - start - 1;
        
        //print row
        for(int i = start; i <= end_x; ++i)
            res.push_back(matrix[start][i]);
        
        if(start < end_y)
        {
            for(int i = start+1; i <= end_y; ++i)
                res.push_back(matrix[i][end_x]);
        }
        
        if(start < end_x && start < end_y)
        {
            for(int i = end_x-1; i >= start; --i)
                res.push_back(matrix[end_y][i]);
        }
        
        if(start < end_y && start < end_x)
        {
            for(int i = end_y-1; i > start; --i)
                res.push_back(matrix[i][start]);
        }
    }
};
```

## 20. 对称二叉树
```c++
/*
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
    TreeNode(int x) :
            val(x), left(NULL), right(NULL) {
    }
};
*/
class Solution {
public:
    bool isSymmetrical(TreeNode* pRoot)
    {
        return isSymmertrical(pRoot, pRoot);
    }
    bool isSymmertrical(TreeNode* left, TreeNode* right)
    {
        if(left == right && left == nullptr)
            return true;
        if(left == nullptr || right == nullptr)
            return false;
        
        if(left->val != right->val)
            return false;
        
        return isSymmertrical(left->left, right->right) && isSymmertrical(left->right, right->left);
    }

};
```

## 21. 包含min函数的栈
使用辅助栈
```c++
class Solution {
public:
    stack<int> m_data;
    stack<int> m_min;
    void push(int value) {
        m_data.push(value);
        if(m_min.empty())
            m_min.push(value);
        else if(value < m_min.top())
            m_min.push(value);
        else
            m_min.push(m_min.top());
    }
    void pop() {
        if(!m_data.empty())
        {
            m_data.pop();
            m_min.pop();
        }
    }
    int top() {
        if(!m_data.empty())
            return m_data.top();
    }
    int min() {
        if(!m_min.empty())
            return m_min.top();
    }
    
};
```

## 22. 栈的压入和弹出序列
```c++
class Solution {
public:
    bool IsPopOrder(vector<int> pushV,vector<int> popV) {
        stack<int> st;
        int i = 1;
        int j = 0;
        st.push(pushV[0]);
        
        while(!st.empty())
        {
            if(st.top() == popV[j])
            {
                st.pop();
                ++j;
            }
            else if(i < pushV.size())
            {
                st.push(pushV[i]);
                ++i;
            }
            else
                return false;

        }
        return true;
    }
};
```
