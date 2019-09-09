## 23. 从上到下打印二叉树
方法：层次遍历，利用辅助队列存储子节点，依次弹出并将子节点的子节点压栈继续打印。层次遍历也是广度优先遍历。

使用双端队列。
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
    vector<int> PrintFromTopToBottom(TreeNode* root) {
        deque<TreeNode*> assist;
        vector<int> res;
        if(root != nullptr)
        {
            assist.push_back(root);
            while(!assist.empty())
            {
                TreeNode* tmp = assist.front();
                assist.pop_front();
                res.push_back(tmp->val);
                if(tmp->left != nullptr)
                    assist.push_back(tmp->left);
                if(tmp->right != nullptr)
                    assist.push_back(tmp->right);
            }
        }
        return res;
    }
};
```

使用普通队列：
```c++
class Solution {
public:
    vector<int> PrintFromTopToBottom(TreeNode* root) {
        queue<TreeNode*> assist;
        vector<int> res;
        if(root != nullptr)
        {
            assist.push(root);
            while(!assist.empty())
            {
                TreeNode* tmp = assist.front();
                assist.pop();
                res.push_back(tmp->val);
                if(tmp->left != nullptr)
                    assist.push(tmp->left);
                if(tmp->right != nullptr)
                    assist.push(tmp->right);
            }
        }
        return res;
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
