/**
 * @file tree.cpp
 * @author yanbingjian1995@163.com
 * @brief 
 * @version 0.1
 * @date 2021-07-29
 * 
 * @copyright Copyright (c) 2021
 * 
 */

#include <iostream>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>


// definition for a binary node
struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x): val(x), left(nullptr), right(nullptr) { }
};

/**
 * @brief 先根遍历：先序遍历(root->left->right)、root->right->left
 *        后根遍历：后序遍历(left->right->root)、right->left->root
 *        中序遍历：(left->root->right)
 *        层序遍历：std::vector<std::vector<int>>, 每一层的节点值存在同一个vector中
 * @brief 三种实现方式：递归、栈和morris
 *        morris遍历方式参考：leetcode-cn.com https://www.cnblogs.com/anniekim/archive/2013/06/15/morristraversal.html
 *        morris遍历的核心在于，在往下走时将前驱节点的right置为当前节点，使得向上回溯时能够通过前驱节点走到当前节点
 * 
 */


// 仅支持完全二叉树
TreeNode* makeTreeV1(std::vector<int>& vec, TreeNode* root) {
    if (vec.empty()) return root;

    root = new TreeNode(vec[0]);
    int index = 1;
    std::vector<TreeNode*> curLayerNodes{root};
    std::vector<TreeNode*> nextLayerNodes;
    while (index < vec.size()) {
        for (auto& node: curLayerNodes) {
            if (index >= vec.size()) return root;
            TreeNode* left = new TreeNode(vec[index++]);
            node->left = left;
            nextLayerNodes.push_back(node->left);

            if (index >= vec.size()) return root;
            TreeNode* right = new TreeNode(vec[index++]);
            node->right = right;
            nextLayerNodes.push_back(node->right);
        }
        curLayerNodes.assign(nextLayerNodes.begin(), nextLayerNodes.end());
        std::vector<TreeNode*>().swap(nextLayerNodes);
    }
    return root;
}

std::string genTreeOutputStrV1(const TreeNode * const root) {
    std::string result = "";
    if (root == nullptr) return result;
    std::vector<const TreeNode*> curLayerNodes{root};
    std::vector<const TreeNode*> nextLayerNodes;
    std::string curLayerStr = "";
    while (!curLayerNodes.empty()) {
        for (auto& node: curLayerNodes) {
            curLayerStr += std::to_string(node->val) + "\t";
            if (node->left != nullptr) nextLayerNodes.push_back(node->left);
            if (node->right != nullptr) nextLayerNodes.push_back(node->right);
        }
        result += curLayerStr + "\n";
        curLayerStr = "";
        curLayerNodes.assign(nextLayerNodes.begin(), nextLayerNodes.end());
        std::vector<const TreeNode*>().swap(nextLayerNodes);
    }
    
    return result;
}

// 支持全部二叉树：印象中『二叉树转序列』和『序列转二叉树』都是原题，等做到的时候再实现下
// vec中包含NULL，表示对应节点是空指针
TreeNode* makeTreeV2(std::vector<int>& vec, TreeNode* root) {
    if (vec.empty()) return root;

    root = new TreeNode(vec[0]);
    int index = 1;
    std::vector<TreeNode*> curLayerNodes{root};
    std::vector<TreeNode*> nextLayerNodes;
    while (index < vec.size()) {
        for (auto& node: curLayerNodes) {
            if (index >= vec.size()) return root;
            TreeNode* left = new TreeNode(vec[index++]);
            node->left = left;
            nextLayerNodes.push_back(node->left);

            if (index >= vec.size()) return root;
            TreeNode* right = new TreeNode(vec[index++]);
            node->right = right;
            nextLayerNodes.push_back(node->right);
        }
        curLayerNodes.assign(nextLayerNodes.begin(), nextLayerNodes.end());
        std::vector<TreeNode*>().swap(nextLayerNodes);
    }
    return root;
}

std::string genTreeOutputStrV2(const TreeNode * const root) {
    std::string result = "";
    if (root == nullptr) return result;
    std::vector<const TreeNode*> curLayerNodes{root};
    std::vector<const TreeNode*> nextLayerNodes;
    std::string curLayerStr = "";
    while (!curLayerNodes.empty()) {
        for (auto& node: curLayerNodes) {
            curLayerStr += std::to_string(node->val) + "\t";
            if (node->left != nullptr) nextLayerNodes.push_back(node->left);
            if (node->right != nullptr) nextLayerNodes.push_back(node->right);
        }
        result += curLayerStr + "\n";
        curLayerStr = "";
        curLayerNodes.assign(nextLayerNodes.begin(), nextLayerNodes.end());
        std::vector<const TreeNode*>().swap(nextLayerNodes);
    }
    
    return result;
}

std::string genVectorOutputStr(std::vector<int> vec) {
    std::string result = "";
    if (vec.empty()) return result;
    for (auto& v: vec) {
        result += std::to_string(v) + " ";
    }
    result += "\n";
    return result;
}

std::string genVecVecOutputStr(std::vector<std::vector<int>> vecvec) {
    std::string result = "";
    if (vecvec.empty()) return result;
    for (auto& vec: vecvec) {
        for (auto& v: vec) {
            result += std::to_string(v) + " ";
        }
        result += "\n";
    }
    return result;
}

class Solution {
public:
    // preorder tranverse
    std::vector<int> preorderHelper(const TreeNode * const root, std::vector<int>& result) {
        if (root == nullptr) return result;
        result.push_back(root->val);
        preorderHelper(root->left, result);
        preorderHelper(root->right, result);
        return result;
    }

    std::vector<int> preorderTranverseRecurse(const TreeNode * const root) {
        std::vector<int> result;
        preorderHelper(root, result);
        return result;
    }

    std::vector<int> preorderTranverseStack(const TreeNode * const root) {
        std::vector<int> result;
        std::stack<const TreeNode*> s;
        if (root != nullptr) s.push(root);
        while (!s.empty()) {
            auto p = s.top();
            s.pop();
            result.push_back(p->val);
            if (p->right != nullptr) s.push(p->right);
            if (p->left != nullptr) s.push(p->left);
        }
        return result;
    }

    std::vector<int> preorderTranverseMorris(TreeNode *root) {
        std::vector<int> result;
        TreeNode *p = root, *prev = nullptr;
        while (p != nullptr) {
            if (p->left == nullptr) {
                result.push_back(p->val);
                p = p->right;
            } else {
                prev = p->left;
                while (prev->right != nullptr && prev->right != p) {
                    prev = prev->right;
                }
                if (prev->right == nullptr) {
                    prev->right = p;
                    result.push_back(p->val);
                    p = p->left;
                } else {
                    prev->right = nullptr;
                    p = p->right;
                }
            }
        }
        return result;
    }

    // inorder transverse
    std::vector<int> inorderHelper(const TreeNode * const root, std::vector<int>& result) {
        if (root == nullptr) return result;
        inorderHelper(root->left, result);
        result.push_back(root->val);
        inorderHelper(root->right, result);
        return result;
    }

    std::vector<int> inorderTranverseRecurse(const TreeNode * const root) {
        std::vector<int> result;
        inorderHelper(root, result);
        return result;
    }

    std::vector<int> inorderTranverseStack(const TreeNode * const root) {
        std::vector<int> result;
        std::stack<const TreeNode*> s;
        const TreeNode *p = root;
        while (p != nullptr || !s.empty()) {
            while (p != nullptr) {
                s.push(p);
                p = p->left;
            }
            p = s.top();
            s.pop();
            result.push_back(p->val);
            p = p->right;
        }
        return result;
    }

    std::vector<int> inorderTranverseMorris(TreeNode *root) {
        std::vector<int> result;
        TreeNode *p = root, *prev = nullptr;
        while (p != nullptr) {
            if (p->left == nullptr) {
                result.push_back(p->val);
                p = p->right;
            } else {
                prev = p->left;
                while (prev->right != nullptr && prev->right != p) {
                    prev = prev->right;
                }
                if (prev->right == nullptr) {
                    prev->right = p;
                    p = p->left;
                } else {
                    prev->right = nullptr;
                    result.push_back(p->val);
                    p = p->right;
                }
            }
        }
        return result;
    }

    // postorder transverse
    std::vector<int> postorderHelper(const TreeNode * const root, std::vector<int>& result) {
        if (root == nullptr) return result;
        postorderHelper(root->left, result);
        postorderHelper(root->right, result);
        result.push_back(root->val);
        return result;
    }

    std::vector<int> postorderTranverseRecurse(const TreeNode * const root) {
        std::vector<int> result;
        postorderHelper(root, result);
        return result;
    }

    /**
     * @brief 本质上是实现了一种前序遍历的方式，前序遍历是"根左右"，本方案先实现"根右左"，
     * @brief 再通过stack先进后出的性质倒序输出得到后序遍历"左右根""
     * 
     * @param root: root node of the given binary tree
     * @return std::vector<int> 
     */
    std::vector<int> postorderTranverseStackFromPreorder(const TreeNode * const root) {
        std::vector<int> result;
        std::stack<const TreeNode*> s1;
        std::stack<int> s2;
        if (root != nullptr) s1.push(root);
        while (!s1.empty()) {
            auto p = s1.top();
            s1.pop();
            s2.push(p->val);
            if (p->left != nullptr) s1.push(p->left);
            if (p->right != nullptr) s1.push(p->right);
        }
        while (!s2.empty()) {
            auto val = s2.top();
            s2.pop();
            result.push_back(val);
        }
        return result;
    }

    // 后续遍历的标准迭代写法
    std::vector<int> postorderTranverseStack(const TreeNode * const root) {
        std::vector<int> result;
        std::stack<const TreeNode*> s;
        const TreeNode *p = root;
        const TreeNode *prev = nullptr;
        while (p != nullptr || !s.empty()) {
            while (p != nullptr) {
                s.push(p);
                p = p->left;
            }
            p = s.top();
            s.pop();
            if (p->right == nullptr || p->right == prev) {
                result.push_back(p->val);
                prev = p;
                p = nullptr;
            } else {
                s.push(p);
                p = p->right;
            }
        }
        return result;
    }

    void addPath(std::vector<int>& vec, TreeNode *p) {
        int count = 0;
        while (p != nullptr) {
            vec.push_back(p->val);
            p = p->right;
            ++count;
        }
        std::reverse(vec.end()-count, vec.end());
    }

    std::vector<int> postorderTranverseMorris(TreeNode *root) {
        std::vector<int> result;
        TreeNode *p = root, *prev = nullptr;
        while (p != nullptr) {
            if (p->left == nullptr) {
                p = p->right;
            } else {
                prev = p->left;
                while (prev->right != nullptr && prev->right != p) {
                    prev = prev->right;
                }
                if (prev->right == nullptr) {
                    prev->right = p;
                    p = p->left;
                } else {
                    prev->right = nullptr;
                    addPath(result, p->left);
                    p = p->right;
                }
            }
        }
        addPath(result, root);
        return result;
    }

    //layer-wise order
    std::vector<std::vector<int>> layerwiseorderTranverseQueue(TreeNode *root) {
        std::vector<std::vector<int>> result;
        std::queue<TreeNode*> q;
        TreeNode* p = root;
        if (p != nullptr) q.push(root);
        while (!q.empty()) {
            result.push_back(std::vector<int>());
            int length = q.size();
            for (int i = 0; i < length; i++) {
                p = q.front();
                q.pop();
                result.back().push_back(p->val);
                if (p->left) q.push(p->left);
                if (p->right) q.push(p->right);
            }
        }
        return result;
    }

};

int main() {
    std::string outputStr = "";
    std::vector<int> vec = {1, 2, 3, 4, 5, 6, 7};

    // make origin binary tree with vec
    TreeNode *root = nullptr;
    const TreeNode * const const_root = makeTreeV1(vec, root); // const在*左侧，修饰整个*const_root,表示指针指向的是常量
    root = nullptr;
    root = makeTreeV1(vec, root); // morris遍历的中间过程会修改树,因此不能使用const指针
    outputStr = genTreeOutputStrV1(const_root);
    std::cout << "origin binary tree:\n" << outputStr << std::endl;

    Solution sol = Solution();

    // preorder
    std::vector<int> preorderRecurseVec = sol.preorderTranverseRecurse(const_root);
    outputStr = genVectorOutputStr(preorderRecurseVec);
    std::cout << "preorder recurse vector:\n" << outputStr << std::endl;

    std::vector<int> preorderStackVec = sol.preorderTranverseStack(const_root);
    outputStr = genVectorOutputStr(preorderStackVec);
    std::cout << "preorder stack vector:\n" << outputStr << std::endl;

    std::vector<int> preorderMorrisVec = sol.preorderTranverseMorris(root);
    outputStr = genVectorOutputStr(preorderMorrisVec);
    std::cout << "preorder morris vector:\n" << outputStr << std::endl;

    // inorder
    std::vector<int> inorderRecurseVec = sol.inorderTranverseRecurse(const_root);
    outputStr = genVectorOutputStr(inorderRecurseVec);
    std::cout << "inorder recurse vector:\n" << outputStr << std::endl;

    std::vector<int> inorderStackVec = sol.inorderTranverseStack(const_root);
    outputStr = genVectorOutputStr(inorderStackVec);
    std::cout << "inorder stack vector:\n" << outputStr << std::endl;

    std::vector<int> inorderMorrisVec = sol.inorderTranverseMorris(root);
    outputStr = genVectorOutputStr(inorderMorrisVec);
    std::cout << "inorder morris vector:\n" << outputStr << std::endl;

    // postorder
    std::vector<int> postorderRecurseVec = sol.postorderTranverseRecurse(const_root);
    outputStr = genVectorOutputStr(postorderRecurseVec);
    std::cout << "postorder recurse vector:\n" << outputStr << std::endl;

    std::vector<int> postorderStackFromPreorderVec = sol.postorderTranverseStackFromPreorder(const_root);
    outputStr = genVectorOutputStr(postorderStackFromPreorderVec);
    std::cout << "postorder stack from preorder vector:\n" << outputStr << std::endl;

    std::vector<int> postorderStackVec = sol.postorderTranverseStack(const_root);
    outputStr = genVectorOutputStr(postorderStackVec);
    std::cout << "postorder stack vector:\n" << outputStr << std::endl;

    std::vector<int> postorderMorrisVec = sol.postorderTranverseMorris(root);
    outputStr = genVectorOutputStr(postorderMorrisVec);
    std::cout << "postorder morris vector:\n" << outputStr << std::endl;

    std::vector<std::vector<int>> layerwiseorderVec = sol.layerwiseorderTranverseQueue(root);
    outputStr = genVecVecOutputStr(layerwiseorderVec);
    std::cout << "layerwiseorder queue vector:\n" << outputStr << std::endl;
}