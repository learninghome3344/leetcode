# 101.对称二叉树
[https://leetcode-cn.com/problems/symmetric-tree](https://leetcode-cn.com/problems/symmetric-tree) 
## 原题
给你一个二叉树的根节点 `root` ， 检查它是否轴对称。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree1.jpg" style="width: 354px; height: 291px;" />
```

输入：root = [1,2,2,3,4,4,3]
输出：true

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/symtree2.jpg" style="width: 308px; height: 258px;" />
```

输入：root = [1,2,2,null,3,null,3]
输出：false

```
 

 **提示：** 
- 树中节点数目在范围 `[1, 1000]` 内
-  `-100 <= Node.val <= 100` 
 

 **进阶：** 你可以运用递归和迭代两种方法解决这个问题吗？

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 102.二叉树的层序遍历
[https://leetcode-cn.com/problems/binary-tree-level-order-traversal](https://leetcode-cn.com/problems/binary-tree-level-order-traversal) 
## 原题
给你二叉树的根节点 `root` ，返回其节点值的 **层序遍历** 。 （即逐层地，从左到右访问所有节点）。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
```

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]

```
 **示例 2：** 

```

输入：root = [1]
输出：[[1]]

```
 **示例 3：** 

```

输入：root = []
输出：[]

```
 

 **提示：** 
- 树中节点数目在范围 `[0, 2000]` 内
-  `-1000 <= Node.val <= 1000` 
 
**标签**
`树` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 103.二叉树的锯齿形层序遍历
[https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal) 
## 原题
给你二叉树的根节点 `root` ，返回其节点值的 **锯齿形层序遍历** 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
```

输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]

```
 **示例 2：** 

```

输入：root = [1]
输出：[[1]]

```
 **示例 3：** 

```

输入：root = []
输出：[]

```
 

 **提示：** 
- 树中节点数目在范围 `[0, 2000]` 内
-  `-100 <= Node.val <= 100` 
 
**标签**
`树` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 104.二叉树的最大深度
[https://leetcode-cn.com/problems/maximum-depth-of-binary-tree](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree) 
## 原题
给定一个二叉树，找出其最大深度。

二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。

 **说明:** 叶子节点是指没有子节点的节点。

 **示例：** <br>
给定二叉树 `[3,9,20,null,null,15,7]` ，

```
    3
   / \
  9  20
    /  \
   15   7
```
返回它的最大深度 3 。

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 105.从前序与中序遍历序列构造二叉树
[https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal) 
## 原题
给定两个整数数组 `preorder` 和 `inorder` ，其中 `preorder` 是二叉树的 **先序遍历** ， `inorder` 是同一棵树的 **中序遍历** ，请构造二叉树并返回其根节点。

 

 **示例 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" style="height: 302px; width: 277px;" />
```

输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

```
 **示例 2:** 

```

输入: preorder = [-1], inorder = [-1]
输出: [-1]

```
 

 **提示:** 
-  `1 <= preorder.length <= 3000` 
-  `inorder.length == preorder.length` 
-  `-3000 <= preorder[i], inorder[i] <= 3000` 
-  `preorder` 和 `inorder` 均 **无重复** 元素
-  `inorder` 均出现在 `preorder` 
-  `preorder` **保证** 为二叉树的前序遍历序列
-  `inorder` **保证** 为二叉树的中序遍历序列
 
**标签**
`树` `数组` `哈希表` `分治` `二叉树` 


## 
```python

```
>
# 106.从中序与后序遍历序列构造二叉树
[https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal) 
## 原题
给定两个整数数组 `inorder` 和 `postorder` ，其中 `inorder` 是二叉树的中序遍历， `postorder` 是同一棵树的后序遍历，请你构造并返回这颗 *二叉树* 。

 

 **示例 1:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree.jpg" />
```

输入：inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
输出：[3,9,20,null,null,15,7]

```
 **示例 2:** 

```

输入：inorder = [-1], postorder = [-1]
输出：[-1]

```
 

 **提示:** 
-  `1 <= inorder.length <= 3000` 
-  `postorder.length == inorder.length` 
-  `-3000 <= inorder[i], postorder[i] <= 3000` 
-  `inorder` 和 `postorder` 都由 **不同** 的值组成
-  `postorder` 中每一个值都在 `inorder` 中
-  `inorder` **保证** 是树的中序遍历
-  `postorder` **保证** 是树的后序遍历
 
**标签**
`树` `数组` `哈希表` `分治` `二叉树` 


## 
```python

```
>
# 107.二叉树的层序遍历 II
[https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii) 
## 原题
给你二叉树的根节点 `root` ，返回其节点值 **自底向上的层序遍历** 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/tree1.jpg" style="width: 277px; height: 302px;" />
```

输入：root = [3,9,20,null,null,15,7]
输出：[[15,7],[9,20],[3]]

```
 **示例 2：** 

```

输入：root = [1]
输出：[[1]]

```
 **示例 3：** 

```

输入：root = []
输出：[]

```
 

 **提示：** 
- 树中节点数目在范围 `[0, 2000]` 内
-  `-1000 <= Node.val <= 1000` 
 
**标签**
`树` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 108.将有序数组转换为二叉搜索树
[https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree) 
## 原题
给你一个整数数组 `nums` ，其中元素已经按 **升序** 排列，请你将其转换为一棵 **高度平衡** 二叉搜索树。

 **高度平衡** 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree1.jpg" style="width: 302px; height: 222px;" />
```

输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]
解释：[0,-10,5,null,-3,null,9] 也将被视为正确答案：
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree2.jpg" style="width: 302px; height: 222px;" />

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/btree.jpg" style="width: 342px; height: 142px;" />
```

输入：nums = [1,3]
输出：[3,1]
解释：[1,3] 和 [3,1] 都是高度平衡二叉搜索树。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `-10^4 <= nums[i] <= 10^4` 
-  `nums` 按 **严格递增** 顺序排列
 
**标签**
`树` `二叉搜索树` `数组` `分治` `二叉树` 


## 
```python

```
>
# 109.有序链表转换二叉搜索树
[https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree) 
## 原题
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树 *每个节点* 的左右两个子树的高度差的绝对值不超过 1。

 **示例:** 

```
给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5

```
 
**标签**
`树` `二叉搜索树` `链表` `分治` `二叉树` 


## 
```python

```
>
# 110.平衡二叉树
[https://leetcode-cn.com/problems/balanced-binary-tree](https://leetcode-cn.com/problems/balanced-binary-tree) 
## 原题
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

<blockquote>
一个二叉树 *每个节点 * 的左右两个子树的高度差的绝对值不超过 1 。
</blockquote>

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_1.jpg" style="width: 342px; height: 221px;" />
```

输入：root = [3,9,20,null,null,15,7]
输出：true

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/06/balance_2.jpg" style="width: 452px; height: 301px;" />
```

输入：root = [1,2,2,3,3,null,null,4,4]
输出：false

```
 **示例 3：** 

```

输入：root = []
输出：true

```
 

 **提示：** 
- 树中的节点数在范围 `[0, 5000]` 内
-  `-10^4 <= Node.val <= 10^4` 
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 111.二叉树的最小深度
[https://leetcode-cn.com/problems/minimum-depth-of-binary-tree](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) 
## 原题
给定一个二叉树，找出其最小深度。

最小深度是从根节点到最近叶子节点的最短路径上的节点数量。

 **说明：** 叶子节点是指没有子节点的节点。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg" style="width: 432px; height: 302px;" />
```

输入：root = [3,9,20,null,null,15,7]
输出：2

```
 **示例 2：** 

```

输入：root = [2,null,3,null,4,null,5,null,6]
输出：5

```
 

 **提示：** 
- 树中节点数的范围在 `[0, 10^5]` 内
-  `-1000 <= Node.val <= 1000` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 112.路径总和
[https://leetcode-cn.com/problems/path-sum](https://leetcode-cn.com/problems/path-sum) 
## 原题
给你二叉树的根节点 `root` 和一个表示目标和的整数 `targetSum` 。判断该树中是否存在 **根节点到叶子节点** 的路径，这条路径上所有节点值相加等于目标和 `targetSum` 。如果存在，返回 `true` ；否则，返回 `false` 。

 **叶子节点** 是指没有子节点的节点。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;" />
```

输入：root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
输出：true
解释：等于目标和的根节点到叶节点路径如上图所示。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" />
```

输入：root = [1,2,3], targetSum = 5
输出：false
解释：树中存在两条根节点到叶子节点的路径：
(1 --> 2): 和为 3
(1 --> 3): 和为 4
不存在 sum = 5 的根节点到叶子节点的路径。
```
 **示例 3：** 

```

输入：root = [], targetSum = 0
输出：false
解释：由于树是空的，所以不存在根节点到叶子节点的路径。

```
 

 **提示：** 
- 树中节点的数目在范围 `[0, 5000]` 内
-  `-1000 <= Node.val <= 1000` 
-  `-1000 <= targetSum <= 1000` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 113.路径总和 II
[https://leetcode-cn.com/problems/path-sum-ii](https://leetcode-cn.com/problems/path-sum-ii) 
## 原题
给你二叉树的根节点 `root` 和一个整数目标和 `targetSum` ，找出所有 **从根节点到叶子节点** 路径总和等于给定目标和的路径。

 **叶子节点** 是指没有子节点的节点。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsumii1.jpg" style="width: 500px; height: 356px;" />
```

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：[[5,4,11,2],[5,8,4,5]]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg" style="width: 212px; height: 181px;" />
```

输入：root = [1,2,3], targetSum = 5
输出：[]

```
 **示例 3：** 

```

输入：root = [1,2], targetSum = 0
输出：[]

```
 

 **提示：** 
- 树中节点总数在范围 `[0, 5000]` 内
-  `-1000 <= Node.val <= 1000` 
-  `-1000 <= targetSum <= 1000` 
 
**标签**
`树` `深度优先搜索` `回溯` `二叉树` 


## 
```python

```
>
# 114.二叉树展开为链表
[https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list) 
## 原题
给你二叉树的根结点 `root` ，请你将它展开为一个单链表：
- 展开后的单链表应该同样使用 `TreeNode` ，其中 `right` 子指针指向链表中下一个结点，而左子指针始终为 `null` 。
- 展开后的单链表应该与二叉树 <a href="https://baike.baidu.com/item/%E5%85%88%E5%BA%8F%E9%81%8D%E5%8E%86/6442839?fr=aladdin" target="_blank"> **先序遍历** </a> 顺序相同。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/flaten.jpg" style="width: 500px; height: 226px;" />
```

输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]

```
 **示例 2：** 

```

输入：root = []
输出：[]

```
 **示例 3：** 

```

输入：root = [0]
输出：[0]

```
 

 **提示：** 
- 树中结点数在范围 `[0, 2000]` 内
-  `-100 <= Node.val <= 100` 
 

 **进阶：** 你可以使用原地算法（ `O(1)` 额外空间）展开这棵树吗？

 
**标签**
`栈` `树` `深度优先搜索` `链表` `二叉树` 


## 
```python

```
>
# 115.不同的子序列
[https://leetcode-cn.com/problems/distinct-subsequences](https://leetcode-cn.com/problems/distinct-subsequences) 
## 原题
给定一个字符串 `s` **** 和一个字符串 `t` ，计算在 `s` 的子序列中 `t` 出现的个数。

字符串的一个 **子序列** 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如， `"ACE"`  是  `"ABCDE"`  的一个子序列，而  `"AEC"`  不是）

题目数据保证答案符合 32 位带符号整数范围。

 

 **示例 1：** 

```

输入：s = "rabbbit", t = "rabbit"
输出：3
解释：
如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
rabbbit
rabbbit
rabbbit
```
 **示例 2：** 

```

输入：s = "babgbag", t = "bag"
输出：5
解释：
如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
babgbag
babgbag
babgbag
babgbag
babgbag

```
 

 **提示：** 
-  `0 <= s.length, t.length <= 1000` 
-  `s` 和 `t` 由英文字母组成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 116.填充每个节点的下一个右侧节点指针
[https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node) 
## 原题
给定一个 **完美二叉树** ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

```

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 `NULL` 。

初始状态下，所有 next 指针都被设置为 `NULL` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2019/02/14/116_sample.png" style="height: 171px; width: 500px;" />

```

输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。

```
<meta charset="UTF-8" />

 **示例 2:** 

```

输入：root = []
输出：[]

```
 

 **提示：** 
- 树中节点的数量在<meta charset="UTF-8" /> `[0, 2^12 - 1]` 范围内
-  `-1000 <= node.val <= 1000` 
 

 **进阶：** 
- 你只能使用常量级额外空间。
- 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `链表` `二叉树` 


## 
```python

```
>
# 117.填充每个节点的下一个右侧节点指针 II
[https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii) 
## 原题
给定一个二叉树

```

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
```
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 `NULL` 。

初始状态下，所有 next 指针都被设置为 `NULL` 。

 

 **进阶：** 
- 你只能使用常量级额外空间。
- 使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 

 **示例：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/117_sample.png" style="height: 218px; width: 640px;" />

```

输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。
```
 

 **提示：** 
- 树中的节点数小于 `6000` 
-  `-100 <= node.val <= 100` 
 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `链表` `二叉树` 


## 
```python

```
>
# 118.杨辉三角
[https://leetcode-cn.com/problems/pascals-triangle](https://leetcode-cn.com/problems/pascals-triangle) 
## 原题
给定一个非负整数  *`numRows` ，* 生成「杨辉三角」的前  *`numRows`  * 行。

<small>在「杨辉三角」中，每个数是它左上方和右上方的数的和。</small>

<img alt="" src="https://pic.leetcode-cn.com/1626927345-DZmfxB-PascalTriangleAnimated2.gif" />

 

 **示例 1:** 

```

输入: numRows = 5
输出: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

```
 **示例 2:** 

```

输入: numRows = 1
输出: [[1]]

```
 

 **提示:** 
-  `1 <= numRows <= 30` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 119.杨辉三角 II
[https://leetcode-cn.com/problems/pascals-triangle-ii](https://leetcode-cn.com/problems/pascals-triangle-ii) 
## 原题
给定一个非负索引 `rowIndex` ，返回「杨辉三角」的第 `rowIndex` * * 行。

<small>在「杨辉三角」中，每个数是它左上方和右上方的数的和。</small>

<img alt="" src="https://pic.leetcode-cn.com/1626927345-DZmfxB-PascalTriangleAnimated2.gif" />

 

 **示例 1:** 

```

输入: rowIndex = 3
输出: [1,3,3,1]

```
 **示例 2:** 

```

输入: rowIndex = 0
输出: [1]

```
 **示例 3:** 

```

输入: rowIndex = 1
输出: [1,1]

```
 

 **提示:** 
-  `0 <= rowIndex <= 33` 
 

 **进阶：** 

你可以优化你的算法到 ` *O* (<i>rowIndex</i>)` 空间复杂度吗？

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 120.三角形最小路径和
[https://leetcode-cn.com/problems/triangle](https://leetcode-cn.com/problems/triangle) 
## 原题
给定一个三角形 `triangle` ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。 **相邻的结点** 在这里指的是 **下标** 与 **上一层结点下标** 相同或者等于 **上一层结点下标 + 1** 的两个结点。也就是说，如果正位于当前行的下标 `i` ，那么下一步可以移动到下一行的下标 `i` 或 `i + 1` 。

 

 **示例 1：** 

```

输入：triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
输出：11
解释：如下面简图所示：
   2
  3 4
 6 5 7
4 1 8 3
自顶向下的最小路径和为 11（即，2 + 3 + 5 + 1 = 11）。

```
 **示例 2：** 

```

输入：triangle = [[-10]]
输出：-10

```
 

 **提示：** 
-  `1 <= triangle.length <= 200` 
-  `triangle[0].length == 1` 
-  `triangle[i].length == triangle[i - 1].length + 1` 
-  `-10^4 <= triangle[i][j] <= 10^4` 
 

 **进阶：** 
- 你可以只使用 `O(n)`  的额外空间（ `n` 为三角形的总行数）来解决这个问题吗？
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 121.买卖股票的最佳时机
[https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock) 
## 原题
给定一个数组 `prices` ，它的第  `i` 个元素  `prices[i]` 表示一支给定股票第 `i` 天的价格。

你只能选择 **某一天** 买入这只股票，并选择在 **未来的某一个不同的日子** 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 `0` 。

 

 **示例 1：** 

```

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

```
 **示例 2：** 

```

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。

```
 

 **提示：** 
-  `1 <= prices.length <= 10^5` 
-  `0 <= prices[i] <= 10^4` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 122.买卖股票的最佳时机 II
[https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii) 
## 原题
给定一个数组 `prices` ，其中 `prices[i]` 表示股票第 `i` 天的价格。

在每一天，你可能会决定购买和/或出售股票。你在任何时候 **最多** 只能持有 **一股** 股票。你也可以购买它，然后在 **同一天** 出售。<br />
返回 *你能获得的 **最大** 利润* 。

 

 **示例 1:** 

```

输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

```
 **示例 2:** 

```

输入: prices = [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

```
 **示例 3:** 

```

输入: prices = [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
```
 

 **提示：** 
-  `1 <= prices.length <= 3 * 10^4` 
-  `0 <= prices[i] <= 10^4` 
 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 123.买卖股票的最佳时机 III
[https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii) 
## 原题
给定一个数组，它的第 `i` 个元素是一支给定的股票在第 `i` 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成  **两笔 ** 交易。

 **注意：** 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

 **示例 1:** 

```

输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
```
 **示例 2：** 

```

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。

```
 **示例 3：** 

```

输入：prices = [7,6,4,3,1] 
输出：0 
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
```
 **示例 4：** 

```

输入：prices = [1]
输出：0

```
 

 **提示：** 
-  `1 <= prices.length <= 10^5` 
-  `0 <= prices[i] <= 10^5` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 124.二叉树中的最大路径和
[https://leetcode-cn.com/problems/binary-tree-maximum-path-sum](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum) 
## 原题
 **路径** 被定义为一条从树中任意节点出发，沿父节点-子节点连接，达到任意节点的序列。同一个节点在一条路径序列中 **至多出现一次** 。该路径 **至少包含一个** 节点，且不一定经过根节点。

 **路径和** 是路径中各节点值的总和。

给你一个二叉树的根节点 `root` ，返回其 **最大路径和** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx1.jpg" style="width: 322px; height: 182px;" />
```

输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6
```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/exx2.jpg" />
```

输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

```
 

 **提示：** 
- 树中节点数目范围是 `[1, 3 * 10^4]` 
-  `-1000 <= Node.val <= 1000` 
 
**标签**
`树` `深度优先搜索` `动态规划` `二叉树` 


## 
```python

```
>
# 125.验证回文串
[https://leetcode-cn.com/problems/valid-palindrome](https://leetcode-cn.com/problems/valid-palindrome) 
## 原题
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

 **说明：** 本题中，我们将空字符串定义为有效的回文串。

 

 **示例 1:** 

```

输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串

```
 **示例 2:** 

```

输入: "race a car"
输出: false
解释："raceacar" 不是回文串

```
 

 **提示：** 
-  `1 <= s.length <= 2 * 10^5` 
- 字符串 `s` 由 ASCII 字符组成
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 126.单词接龙 II
[https://leetcode-cn.com/problems/word-ladder-ii](https://leetcode-cn.com/problems/word-ladder-ii) 
## 原题
按字典 `wordList` 完成从单词 `beginWord` 到单词 `endWord` 转化，一个表示此过程的 **转换序列** 是形式上像 `beginWord -> s<sub>1</sub> -> s<sub>2</sub> -> ... -> s<sub>k</sub>` 这样的单词序列，并满足：
- 每对相邻的单词之间仅有单个字母不同。
- 转换过程中的每个单词 `s<sub>i</sub>` （ `1 <= i <= k` ）必须是字典 `wordList` 中的单词。注意， `beginWord` 不必是字典 `wordList` 中的单词。
-  `s<sub>k</sub> == endWord` 
给你两个单词 `beginWord` 和 `endWord` ，以及一个字典 `wordList` 。请你找出并返回所有从 `beginWord` 到 `endWord` 的 **最短转换序列** ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 `[beginWord, s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>k</sub>]` 的形式返回。

 

 **示例 1：** 

```

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
解释：存在 2 种最短的转换序列：
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"

```
 **示例 2：** 

```

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：[]
解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。

```
 

 **提示：** 
-  `1 <= beginWord.length <= 5` 
-  `endWord.length == beginWord.length` 
-  `1 <= wordList.length <= 5000` 
-  `wordList[i].length == beginWord.length` 
-  `beginWord` 、 `endWord` 和 `wordList[i]` 由小写英文字母组成
-  `beginWord != endWord` 
-  `wordList` 中的所有单词 **互不相同** 
 
**标签**
`广度优先搜索` `哈希表` `字符串` `回溯` 


## 
```python

```
>
# 127.单词接龙
[https://leetcode-cn.com/problems/word-ladder](https://leetcode-cn.com/problems/word-ladder) 
## 原题
字典 `wordList` 中从单词 `beginWord` 和 `endWord` 的 **转换序列** 是一个按下述规格形成的序列<meta charset="UTF-8" /> `beginWord -> s<sub>1</sub> -> s<sub>2</sub> -> ... -> s<sub>k</sub>` ：
- 每一对相邻的单词只差一个字母。
- <meta charset="UTF-8" /> 对于 `1 <= i <= k` 时，每个<meta charset="UTF-8" /> `s<sub>i</sub>` 都在<meta charset="UTF-8" /> `wordList` 中。注意， `beginWord` 不需要在<meta charset="UTF-8" /> `wordList` 中。<meta charset="UTF-8" />
-  `s<sub>k</sub> == endWord` 
给你两个单词 `beginWord` 和 `endWord` 和一个字典 `wordList` ，返回 *从 `beginWord` 到 `endWord` 的 **最短转换序列** 中的 **单词数目*** 。如果不存在这样的转换序列，返回 `0` 。
 

 **示例 1：** 

```

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：5
解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。

```
 **示例 2：** 

```

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：0
解释：endWord "cog" 不在字典中，所以无法进行转换。
```
 

 **提示：** 
-  `1 <= beginWord.length <= 10` 
-  `endWord.length == beginWord.length` 
-  `1 <= wordList.length <= 5000` 
-  `wordList[i].length == beginWord.length` 
-  `beginWord` 、 `endWord` 和 `wordList[i]` 由小写英文字母组成
-  `beginWord != endWord` 
-  `wordList` 中的所有字符串 **互不相同** 
 
**标签**
`广度优先搜索` `哈希表` `字符串` 


## 
```python

```
>
# 128.最长连续序列
[https://leetcode-cn.com/problems/longest-consecutive-sequence](https://leetcode-cn.com/problems/longest-consecutive-sequence) 
## 原题
给定一个未排序的整数数组 `nums` ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为  `O(n)` 的算法解决此问题。

 

 **示例 1：** 

```

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
```
 **示例 2：** 

```

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9

```
 

 **提示：** 
-  `0 <= nums.length <= 10^5` 
-  `-10^9 <= nums[i] <= 10^9` 
 
**标签**
`并查集` `数组` `哈希表` 


## 
```python

```
>
# 129.求根节点到叶节点数字之和
[https://leetcode-cn.com/problems/sum-root-to-leaf-numbers](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers) 
## 原题
给你一个二叉树的根节点 `root` ，树中每个节点都存放有一个 `0` 到 `9` 之间的数字。
每条从根节点到叶节点的路径都代表一个数字：
- 例如，从根节点到叶节点的路径 `1 -> 2 -> 3` 表示数字 `123` 。
计算从根节点到叶节点生成的 **所有数字之和** 。

 **叶节点** 是指没有子节点的节点。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/num1tree.jpg" style="width: 212px; height: 182px;" />
```

输入：root = [1,2,3]
输出：25
解释：
从根到叶子节点路径 1->2 代表数字 12
从根到叶子节点路径 1->3 代表数字 13
因此，数字总和 = 12 + 13 = 25
```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/num2tree.jpg" style="width: 292px; height: 302px;" />
```

输入：root = [4,9,0,5,1]
输出：1026
解释：
从根到叶子节点路径 4->9->5 代表数字 495
从根到叶子节点路径 4->9->1 代表数字 491
从根到叶子节点路径 4->0 代表数字 40
因此，数字总和 = 495 + 491 + 40 = 1026

```
 

 **提示：** 
- 树中节点的数目在范围 `[1, 1000]` 内
-  `0 <= Node.val <= 9` 
- 树的深度不超过 `10` 
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 130.被围绕的区域
[https://leetcode-cn.com/problems/surrounded-regions](https://leetcode-cn.com/problems/surrounded-regions) 
## 原题
给你一个 `m x n` 的矩阵 `board` ，由若干字符 `'X'` 和 `'O'` ，找到所有被 `'X'` 围绕的区域，并将这些区域里所有的  `'O'` 用 `'X'` 填充。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/xogrid.jpg" style="width: 550px; height: 237px;" />
```

输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

```
 **示例 2：** 

```

输入：board = [["X"]]
输出：[["X"]]

```
 

 **提示：** 
-  `m == board.length` 
-  `n == board[i].length` 
-  `1 <= m, n <= 200` 
-  `board[i][j]` 为 `'X'` 或 `'O'` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` 


## 
```python

```
>
# 131.分割回文串
[https://leetcode-cn.com/problems/palindrome-partitioning](https://leetcode-cn.com/problems/palindrome-partitioning) 
## 原题
给你一个字符串 `s` ，请你将 `s` 分割成一些子串，使每个子串都是 **回文串** 。返回 `s` 所有可能的分割方案。

 **回文串** 是正着读和反着读都一样的字符串。

 

 **示例 1：** 

```

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]

```
 **示例 2：** 

```

输入：s = "a"
输出：[["a"]]

```
 

 **提示：** 
-  `1 <= s.length <= 16` 
-  `s` 仅由小写英文字母组成
 
**标签**
`字符串` `动态规划` `回溯` 


## 
```python

```
>
# 132.分割回文串 II
[https://leetcode-cn.com/problems/palindrome-partitioning-ii](https://leetcode-cn.com/problems/palindrome-partitioning-ii) 
## 原题
给你一个字符串 `s` ，请你将 `s` 分割成一些子串，使每个子串都是回文。

返回符合要求的 **最少分割次数** 。
 

 **示例 1：** 

```

输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

```
 **示例 2：** 

```

输入：s = "a"
输出：0

```
 **示例 3：** 

```

输入：s = "ab"
输出：1

```
 

 **提示：** 
-  `1 <= s.length <= 2000` 
-  `s` 仅由小写英文字母组成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 133.克隆图
[https://leetcode-cn.com/problems/clone-graph](https://leetcode-cn.com/problems/clone-graph) 
## 原题
给你无向 **<a href="https://baike.baidu.com/item/连通图/6460995?fr=aladdin" target="_blank">连通</a>** 图中一个节点的引用，请你返回该图的 <a href="https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin" target="_blank"> **深拷贝** </a>（克隆）。

图中的每个节点都包含它的值 `val` （ `int` ） 和其邻居的列表（ `list[Node]` ）。

```
class Node {
    public int val;
    public List<Node> neighbors;
}
```
 

 **测试用例格式：** 

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（ `val = 1` ），第二个节点值为 2（ `val = 2` ），以此类推。该图在测试用例中使用邻接列表表示。

 **邻接列表** 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 **给定节点的拷贝** 作为对克隆图的引用返回。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/01/133_clone_graph_question.png" style="height: 500px; width: 500px;">

```
输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
输出：[[2,4],[1,3],[2,4],[1,3]]
解释：
图中有 4 个节点。
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/01/graph.png" style="height: 148px; width: 163px;">

```
输入：adjList = [[]]
输出：[[]]
解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。

```
 **示例 3：** 

```
输入：adjList = []
输出：[]
解释：这个图是空的，它不含任何节点。

```
 **示例 4：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/01/graph-1.png" style="height: 133px; width: 272px;">

```
输入：adjList = [[2],[1]]
输出：[[2],[1]]
```
 

 **提示：** 
- 节点数不超过 100 。
- 每个节点值 `Node.val` 都是唯一的， `1 <= Node.val <= 100` 。
- 无向图是一个<a href="https://baike.baidu.com/item/简单图/1680528?fr=aladdin" target="_blank">简单图</a>，这意味着图中没有重复的边，也没有自环。
- 由于图是无向的，如果节点 *p* 是节点 *q* 的邻居，那么节点 *q* 也必须是节点 *p* 的邻居。
- 图是连通图，你可以从给定节点访问到所有节点。
 
**标签**
`深度优先搜索` `广度优先搜索` `图` `哈希表` 


## 
```python

```
>
# 134.加油站
[https://leetcode-cn.com/problems/gas-station](https://leetcode-cn.com/problems/gas-station) 
## 原题
在一条环路上有 `n` 个加油站，其中第 `i` 个加油站有汽油 `gas[i]` 升。

你有一辆油箱容量无限的的汽车，从第 `i` 个加油站开往第 `i+1` 个加油站需要消耗汽油 `cost[i]` 升。你从其中的一个加油站出发，开始时油箱为空。

给定两个整数数组 `gas` 和 `cost` ，如果你可以绕环路行驶一周，则返回出发时加油站的编号，否则返回 `-1` 。如果存在解，则 **保证** 它是 **唯一** 的。

 

 **示例 1:** 

```

输入: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
输出: 3
解释:
从 3 号加油站(索引为 3 处)出发，可获得 4 升汽油。此时油箱有 = 0 + 4 = 4 升汽油
开往 4 号加油站，此时油箱有 4 - 1 + 5 = 8 升汽油
开往 0 号加油站，此时油箱有 8 - 2 + 1 = 7 升汽油
开往 1 号加油站，此时油箱有 7 - 3 + 2 = 6 升汽油
开往 2 号加油站，此时油箱有 6 - 4 + 3 = 5 升汽油
开往 3 号加油站，你需要消耗 5 升汽油，正好足够你返回到 3 号加油站。
因此，3 可为起始索引。
```
 **示例 2:** 

```

输入: gas = [2,3,4], cost = [3,4,3]
输出: -1
解释:
你不能从 0 号或 1 号加油站出发，因为没有足够的汽油可以让你行驶到下一个加油站。
我们从 2 号加油站出发，可以获得 4 升汽油。 此时油箱有 = 0 + 4 = 4 升汽油
开往 0 号加油站，此时油箱有 4 - 3 + 2 = 3 升汽油
开往 1 号加油站，此时油箱有 3 - 3 + 3 = 3 升汽油
你无法返回 2 号加油站，因为返程需要消耗 4 升汽油，但是你的油箱只有 3 升汽油。
因此，无论怎样，你都不可能绕环路行驶一周。
```
 

 **提示:** 
-  `gas.length == n` 
-  `cost.length == n` 
-  `1 <= n <= 10^5` 
-  `0 <= gas[i], cost[i] <= 10^4` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 135.分发糖果
[https://leetcode-cn.com/problems/candy](https://leetcode-cn.com/problems/candy) 
## 原题
 `n` 个孩子站成一排。给你一个整数数组 `ratings` 表示每个孩子的评分。

你需要按照以下要求，给这些孩子分发糖果：
- 每个孩子至少分配到 `1` 个糖果。
- 相邻两个孩子评分更高的孩子会获得更多的糖果。
请你给每个孩子分发糖果，计算并返回需要准备的 **最少糖果数目** 。

 

 **示例 1：** 

```

输入：ratings = [1,0,2]
输出：5
解释：你可以分别给第一个、第二个、第三个孩子分发 2、1、2 颗糖果。

```
 **示例 2：** 

```

输入：ratings = [1,2,2]
输出：4
解释：你可以分别给第一个、第二个、第三个孩子分发 1、2、1 颗糖果。
     第三个孩子只得到 1 颗糖果，这满足题面中的两个条件。
```
 

 **提示：** 
-  `n == ratings.length` 
-  `1 <= n <= 2 * 10^4` 
-  `0 <= ratings[i] <= 2 * 10^4` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 136.只出现一次的数字
[https://leetcode-cn.com/problems/single-number](https://leetcode-cn.com/problems/single-number) 
## 原题
给定一个 **非空** 整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

 **说明：** 

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

 **示例 1:** 

```
输入: [2,2,1]
输出: 1

```
 **示例 2:** 

```
输入: [4,1,2,1,2]
输出: 4
```
 
**标签**
`位运算` `数组` 


## 
```python

```
>
# 137.只出现一次的数字 II
[https://leetcode-cn.com/problems/single-number-ii](https://leetcode-cn.com/problems/single-number-ii) 
## 原题
给你一个整数数组  `nums` ，除某个元素仅出现 **一次** 外，其余每个元素都恰出现 **三次 。** 请你找出并返回那个只出现了一次的元素。

 

 **示例 1：** 

```

输入：nums = [2,2,3,2]
输出：3

```
 **示例 2：** 

```

输入：nums = [0,1,0,1,0,1,99]
输出：99

```
 

 **提示：** 
-  `1 <= nums.length <= 3 * 10^4` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
-  `nums` 中，除某个元素仅出现 **一次** 外，其余每个元素都恰出现 **三次** 
 

 **进阶：** 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

 
**标签**
`位运算` `数组` 


## 
```python

```
>
# 138.复制带随机指针的链表
[https://leetcode-cn.com/problems/copy-list-with-random-pointer](https://leetcode-cn.com/problems/copy-list-with-random-pointer) 
## 原题
给你一个长度为 `n` 的链表，每个节点包含一个额外增加的随机指针 `random` ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 **<a href="https://baike.baidu.com/item/深拷贝/22785317?fr=aladdin" target="_blank">深拷贝</a>** 。 深拷贝应该正好由 `n` 个 **全新** 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 `next` 指针和 `random` 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。 **复制链表中的指针都不应指向原链表中的节点** 。

例如，如果原链表中有 `X` 和 `Y` 两个节点，其中 `X.random --> Y` 。那么在复制链表中对应的两个节点 `x` 和 `y` ，同样有 `x.random --> y` 。

返回复制链表的头节点。

用一个由 `n` 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 `[val, random_index]` 表示：
-  `val` ：一个表示 `Node.val` 的整数。
-  `random_index` ：随机指针指向的节点索引（范围从 `0` 到 `n-1` ）；如果不指向任何节点，则为 `null` 。
你的代码 **只** 接受原链表的头节点 `head` 作为传入参数。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e1.png" style="height: 142px; width: 700px;" />

```

输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e2.png" style="height: 114px; width: 700px;" />

```

输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e3.png" style="height: 122px; width: 700px;" />** 

```

输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]

```
 

 **提示：** 
-  `0 <= n <= 1000` <meta charset="UTF-8" />
-  `-10^4 <= Node.val <= 10^4` 
-  `Node.random` 为 `null` 或指向链表中的节点。
 
**标签**
`哈希表` `链表` 


## 
```python

```
>
# 139.单词拆分
[https://leetcode-cn.com/problems/word-break](https://leetcode-cn.com/problems/word-break) 
## 原题
给你一个字符串 `s` 和一个字符串列表 `wordDict` 作为字典。请你判断是否可以利用字典中出现的单词拼接出 `s` 。

 **注意：** 不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

 **示例 1：** 

```

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。

```
 **示例 2：** 

```

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。

```
 **示例 3：** 

```

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false

```
 

 **提示：** 
-  `1 <= s.length <= 300` 
-  `1 <= wordDict.length <= 1000` 
-  `1 <= wordDict[i].length <= 20` 
-  `s` 和 `wordDict[i]` 仅有小写英文字母组成
-  `wordDict` 中的所有字符串 **互不相同** 
 
**标签**
`字典树` `记忆化搜索` `哈希表` `字符串` `动态规划` 


## 
```python

```
>
# 140.单词拆分 II
[https://leetcode-cn.com/problems/word-break-ii](https://leetcode-cn.com/problems/word-break-ii) 
## 原题
给定一个字符串 `s` 和一个字符串字典<meta charset="UTF-8" /> `wordDict` ，在字符串<meta charset="UTF-8" /> `s` 中增加空格来构建一个句子，使得句子中所有的单词都在词典中。 **以任意顺序** 返回所有这些可能的句子。

 **注意：** 词典中的同一个单词可能在分段中被重复使用多次。

 

 **示例 1：** 

```

输入:s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
输出:["cats and dog","cat sand dog"]

```
 **示例 2：** 

```

输入:s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
输出:["pine apple pen apple","pineapple pen apple","pine applepen apple"]
解释: 注意你可以重复使用字典中的单词。

```
 **示例 3：** 

```

输入:s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
输出:[]

```
 

 **提示：** 

<meta charset="UTF-8" />
-  `1 <= s.length <= 20` 
-  `1 <= wordDict.length <= 1000` 
-  `1 <= wordDict[i].length <= 10` 
-  `s` 和 `wordDict[i]` 仅有小写英文字母组成
-  `wordDict` 中所有字符串都 **不同** 
 
**标签**
`字典树` `记忆化搜索` `哈希表` `字符串` `动态规划` `回溯` 


## 
```python

```
>
# 141.环形链表
[https://leetcode-cn.com/problems/linked-list-cycle](https://leetcode-cn.com/problems/linked-list-cycle) 
## 原题
给你一个链表的头节点 `head` ，判断链表中是否有环。

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（索引从 0 开始）。 **注意： `pos` 不作为参数进行传递** 。仅仅是为了标识链表的实际情况。

 *如果链表中存在环* ，则返回 `true` 。 否则，返回 `false` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png" />

```

输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png" />

```

输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png" />

```

输入：head = [1], pos = -1
输出：false
解释：链表中没有环。

```
 

 **提示：** 
- 链表中节点的数目范围是 `[0, 10^4]` 
-  `-10^5 <= Node.val <= 10^5` 
-  `pos` 为 `-1` 或者链表中的一个 **有效索引** 。
 

 **进阶：** 你能用 `O(1)` （即，常量）内存解决此问题吗？

 
**标签**
`哈希表` `链表` `双指针` 


## 
```python

```
>
# 142.环形链表 II
[https://leetcode-cn.com/problems/linked-list-cycle-ii](https://leetcode-cn.com/problems/linked-list-cycle-ii) 
## 原题
给定一个链表的头节点 `head` ，返回链表开始入环的第一个节点。 *如果链表无环，则返回 `null` 。* 

如果链表中有某个节点，可以通过连续跟踪 `next` 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 `pos` 来表示链表尾连接到链表中的位置（ **索引从 0 开始** ）。如果 `pos` 是 `-1` ，则在该链表中没有环。 **注意： `pos` 不作为参数进行传递** ，仅仅是为了标识链表的实际情况。

 **不允许修改** 链表。
 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2018/12/07/circularlinkedlist.png" />

```

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png" />

```

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png" />

```

输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。

```
 

 **提示：** 
- 链表中节点的数目范围在范围 `[0, 10^4]` 内
-  `-10^5 <= Node.val <= 10^5` 
-  `pos` 的值为 `-1` 或者链表中的一个有效索引
 

 **进阶：** 你是否可以使用 `O(1)` 空间解决此题？

 
**标签**
`哈希表` `链表` `双指针` 


## 
```python

```
>
# 143.重排链表
[https://leetcode-cn.com/problems/reorder-list](https://leetcode-cn.com/problems/reorder-list) 
## 原题
给定一个单链表 `L` 的头节点 `head` ，单链表 `L` 表示为：

```

L0 → L1 → … → Ln - 1 → Ln

```
请将其重新排列后变为：

```

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

 **示例 1：** 

<img alt="" src="https://pic.leetcode-cn.com/1626420311-PkUiGI-image.png" style="width: 240px; " />

```

输入：head = [1,2,3,4]
输出：[1,4,2,3]
```
 **示例 2：** 

<img alt="" src="https://pic.leetcode-cn.com/1626420320-YUiulT-image.png" style="width: 320px; " />

```

输入：head = [1,2,3,4,5]
输出：[1,5,2,4,3]
```
 

 **提示：** 
- 链表的长度范围为 `[1, 5 * 10^4]` 
-  `1 <= node.val <= 1000` 
 
**标签**
`栈` `递归` `链表` `双指针` 


## 
```python

```
>
# 144.二叉树的前序遍历
[https://leetcode-cn.com/problems/binary-tree-preorder-traversal](https://leetcode-cn.com/problems/binary-tree-preorder-traversal) 
## 原题
给你二叉树的根节点 `root` ，返回它节点值的  **前序** * * 遍历。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 202px; height: 324px;" />
```

输入：root = [1,null,2,3]
输出：[1,2,3]

```
 **示例 2：** 

```

输入：root = []
输出：[]

```
 **示例 3：** 

```

输入：root = [1]
输出：[1]

```
 **示例 4：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg" style="width: 202px; height: 202px;" />
```

输入：root = [1,2]
输出：[1,2]

```
 **示例 5：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg" style="width: 202px; height: 202px;" />
```

输入：root = [1,null,2]
输出：[1,2]

```
 

 **提示：** 
- 树中节点数目在范围 `[0, 100]` 内
-  `-100 <= Node.val <= 100` 
 

 **进阶：** 递归算法很简单，你可以通过迭代算法完成吗？

 
**标签**
`栈` `树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 145.二叉树的后序遍历
[https://leetcode-cn.com/problems/binary-tree-postorder-traversal](https://leetcode-cn.com/problems/binary-tree-postorder-traversal) 
## 原题
给你一棵二叉树的根节点 `root` ，返回其节点值的 **后序遍历** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/pre1.jpg" style="width: 127px; height: 200px;" />
```

输入：root = [1,null,2,3]
输出：[3,2,1]

```
 **示例 2：** 

```

输入：root = []
输出：[]

```
 **示例 3：** 

```

输入：root = [1]
输出：[1]

```
 

 **提示：** 
- 树中节点的数目在范围 `[0, 100]` 内
-  `-100 <= Node.val <= 100` 
 

 **进阶：** 递归算法很简单，你可以通过迭代算法完成吗？

 
**标签**
`栈` `树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 146.LRU 缓存
[https://leetcode-cn.com/problems/lru-cache](https://leetcode-cn.com/problems/lru-cache) 
## 原题
请你设计并实现一个满足  <a href="https://baike.baidu.com/item/LRU" target="_blank">LRU (最近最少使用) 缓存</a> 约束的数据结构。

实现 `LRUCache` 类：
-  `LRUCache(int capacity)` 以 **正整数** 作为容量 `capacity` 初始化 LRU 缓存
-  `int get(int key)` 如果关键字 `key` 存在于缓存中，则返回关键字的值，否则返回 `-1` 。
-  `void put(int key, int value)` 如果关键字 `key` 已经存在，则变更其数据值 `value` ；如果不存在，则向缓存中插入该组 `key-value` 。如果插入操作导致关键字数量超过 `capacity` ，则应该 **逐出** 最久未使用的关键字。
函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。
 

 **示例：** 

```

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4

```
 

 **提示：** 
-  `1 <= capacity <= 3000` 
-  `0 <= key <= 10000` 
-  `0 <= value <= 10^5` 
- 最多调用 `2 * 10^5` 次 `get` 和 `put` 
 
**标签**
`设计` `哈希表` `链表` `双向链表` 


## 
```python

```
>
# 147.对链表进行插入排序
[https://leetcode-cn.com/problems/insertion-sort-list](https://leetcode-cn.com/problems/insertion-sort-list) 
## 原题
给定单个链表的头<meta charset="UTF-8" /> `head` ，使用 **插入排序** 对链表进行排序，并返回 *排序后链表的头* 。

 **插入排序** 算法的步骤:
- 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
- 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
- 重复直到所有输入数据插入完为止。
下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。

对链表进行插入排序。

<img alt="" src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif" />

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/sort1linked-list.jpg" />

```

输入: head = [4,2,1,3]
输出: [1,2,3,4]
```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/sort2linked-list.jpg" />

```

输入: head = [-1,5,3,4,0]
输出: [-1,0,3,4,5]
```
 

 **提示：** 

<meta charset="UTF-8" />
- 列表中的节点数在 `[1, 5000]` 范围内
-  `-5000 <= Node.val <= 5000` 
 
**标签**
`链表` `排序` 


## 
```python

```
>
# 148.排序链表
[https://leetcode-cn.com/problems/sort-list](https://leetcode-cn.com/problems/sort-list) 
## 原题
给你链表的头结点 `head` ，请将其按 **升序** 排列并返回 **排序后的链表** 。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg" style="width: 450px;" />
```

输入：head = [4,2,1,3]
输出：[1,2,3,4]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg" style="width: 550px;" />
```

输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]

```
 **示例 3：** 

```

输入：head = []
输出：[]

```
 

<b>提示：</b>
- 链表中节点的数目在范围 `[0, 5 * 10^4]` 内
-  `-10^5 <= Node.val <= 10^5` 
 

<b>进阶：</b>你可以在 `O(n log n)` 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

 
**标签**
`链表` `双指针` `分治` `排序` `归并排序` 


## 
```python

```
>
# 149.直线上最多的点数
[https://leetcode-cn.com/problems/max-points-on-a-line](https://leetcode-cn.com/problems/max-points-on-a-line) 
## 原题
给你一个数组 `points` ，其中 `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` 表示 **X-Y** 平面上的一个点。求最多有多少个点在同一条直线上。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane1.jpg" style="width: 300px; height: 294px;" />
```

输入：points = [[1,1],[2,2],[3,3]]
输出：3

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/plane2.jpg" style="width: 300px; height: 294px;" />
```

输入：points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
输出：4

```
 

 **提示：** 
-  `1 <= points.length <= 300` 
-  `points[i].length == 2` 
-  `-10^4 <= x<sub>i</sub>, y<sub>i</sub> <= 10^4` 
-  `points` 中的所有点 **互不相同** 
 
**标签**
`几何` `数组` `哈希表` `数学` 


## 
```python

```
>
# 150.逆波兰表达式求值
[https://leetcode-cn.com/problems/evaluate-reverse-polish-notation](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation) 
## 原题
根据<a href="https://baike.baidu.com/item/%E9%80%86%E6%B3%A2%E5%85%B0%E5%BC%8F/128437" target="_blank"> 逆波兰表示法</a>，求表达式的值。

有效的算符包括 `+` 、 `-` 、 `*` 、 `/` 。每个运算对象可以是整数，也可以是另一个逆波兰表达式。

<b>注意 </b>两个整数之间的除法只保留整数部分。

可以保证给定的逆波兰表达式总是有效的。换句话说，表达式总会得出有效数值且不存在除数为 0 的情况。

 

 **示例 1：** 

```

输入：tokens = ["2","1","+","3","*"]
输出：9
解释：该算式转化为常见的中缀算术表达式为：((2 + 1) * 3) = 9

```
 **示例 2：** 

```

输入：tokens = ["4","13","5","/","+"]
输出：6
解释：该算式转化为常见的中缀算术表达式为：(4 + (13 / 5)) = 6

```
 **示例 3：** 

```

输入：tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
输出：22
解释：该算式转化为常见的中缀算术表达式为：
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
```
 

 **提示：** 
-  `1 <= tokens.length <= 10^4` 
-  `tokens[i]` 是一个算符（ `"+"` 、 `"-"` 、 `"*"` 或 `"/"` ），或是在范围 `[-200, 200]` 内的一个整数
 

 **逆波兰表达式：** 

逆波兰表达式是一种后缀表达式，所谓后缀就是指算符写在后面。
- 平常使用的算式则是一种中缀表达式，如 `( 1 + 2 ) * ( 3 + 4 )` 。
- 该算式的逆波兰表达式写法为 `( ( 1 2 + ) ( 3 4 + ) * )` 。
逆波兰表达式主要有以下两个优点：
- 去掉括号后表达式无歧义，上式即便写成 `1 2 + 3 4 + *` 也可以依据次序计算出正确结果。
- 适合用栈操作运算：遇到数字则入栈；遇到算符则取出栈顶两个数字进行计算，并将结果压入栈中
 
**标签**
`栈` `数组` `数学` 


## 
```python

```
>
# 151.翻转字符串里的单词
[https://leetcode-cn.com/problems/reverse-words-in-a-string](https://leetcode-cn.com/problems/reverse-words-in-a-string) 
## 原题
给你一个字符串 `s` ，逐个翻转字符串中的所有 **单词** 。

 **单词** 是由非空格字符组成的字符串。 `s` 中使用至少一个空格将字符串中的 **单词** 分隔开。

请你返回一个翻转 `s` 中单词顺序并用单个空格相连的字符串。

 **说明：** 
- 输入字符串 `s` 可以在前面、后面或者单词间包含多余的空格。
- 翻转后单词间应当仅用一个空格分隔。
- 翻转后的字符串中不应包含额外的空格。
 

 **示例 1：** 

```

输入：s = "the sky is blue"
输出："blue is sky the"

```
 **示例 2：** 

```

输入：s = "  hello world  "
输出："world hello"
解释：输入字符串可以在前面或者后面包含多余的空格，但是翻转后的字符不能包括。

```
 **示例 3：** 

```

输入：s = "a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，将翻转后单词间的空格减少到只含一个。

```
 **示例 4：** 

```

输入：s = "  Bob    Loves  Alice   "
输出："Alice Loves Bob"

```
 **示例 5：** 

```

输入：s = "Alice does not even like bob"
输出："bob like even not does Alice"

```
 

 **提示：** 
-  `1 <= s.length <= 10^4` 
-  `s` 包含英文大小写字母、数字和空格 `' '` 
-  `s` 中 **至少存在一个** 单词
 

 **进阶：** 
- 请尝试使用  ` *O* (1)` 额外空间复杂度的原地解法。
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 152.乘积最大子数组
[https://leetcode-cn.com/problems/maximum-product-subarray](https://leetcode-cn.com/problems/maximum-product-subarray) 
## 原题
给你一个整数数组 `nums` ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 **32-位** 整数。

 **子数组** 是数组的连续子序列。

 

 **示例 1:** 

```

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。

```
 **示例 2:** 

```

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
```
 

 **提示:** 
-  `1 <= nums.length <= 2 * 10^4` 
-  `-10 <= nums[i] <= 10` 
-  `nums` 的任何前缀或后缀的乘积都 **保证** 是一个 **32-位** 整数
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 153.寻找旋转排序数组中的最小值
[https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array) 
## 原题
已知一个长度为 `n` 的数组，预先按照升序排列，经由 `1` 到 `n` 次 **旋转** 后，得到输入数组。例如，原数组 `nums = [0,1,2,4,5,6,7]` 在变化后可能得到：

- 若旋转 `4` 次，则可以得到 `[4,5,6,7,0,1,2]` 
- 若旋转 `7` 次，则可以得到 `[0,1,2,4,5,6,7]` 
注意，数组 `[a[0], a[1], a[2], ..., a[n-1]]` **旋转一次** 的结果为数组 `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]` 。

给你一个元素值 **互不相同** 的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 **最小元素** 。

 

 **示例 1：** 

```

输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

```
 **示例 2：** 

```

输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。

```
 **示例 3：** 

```

输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 5000` 
-  `-5000 <= nums[i] <= 5000` 
-  `nums` 中的所有整数 **互不相同** 
-  `nums` 原来是一个升序排序的数组，并进行了 `1` 至 `n` 次旋转
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 154.寻找旋转排序数组中的最小值 II
[https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii) 
## 原题
已知一个长度为 `n` 的数组，预先按照升序排列，经由 `1` 到 `n` 次 **旋转** 后，得到输入数组。例如，原数组 `nums = [0,1,4,4,5,6,7]` 在变化后可能得到：

- 若旋转 `4` 次，则可以得到 `[4,5,6,7,0,1,4]` 
- 若旋转 `7` 次，则可以得到 `[0,1,4,4,5,6,7]` 
注意，数组 `[a[0], a[1], a[2], ..., a[n-1]]` **旋转一次** 的结果为数组 `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]` 。

给你一个可能存在 **重复** 元素值的数组 `nums` ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 **最小元素** 。

 

 **示例 1：** 

```

输入：nums = [1,3,5]
输出：1

```
 **示例 2：** 

```

输入：nums = [2,2,2,0,1]
输出：0

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 5000` 
-  `-5000 <= nums[i] <= 5000` 
-  `nums` 原来是一个升序排序的数组，并进行了 `1` 至 `n` 次旋转
 

 **进阶：** 
- 这道题是 <a href="https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/">寻找旋转排序数组中的最小值</a> 的延伸题目。
- 允许重复会影响算法的时间复杂度吗？会如何影响，为什么？
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 155.最小栈
[https://leetcode-cn.com/problems/min-stack](https://leetcode-cn.com/problems/min-stack) 
## 原题
设计一个支持 `push` ， `pop` ， `top` 操作，并能在常数时间内检索到最小元素的栈。
-  `push(x)` &mdash;&mdash; 将元素 x 推入栈中。
-  `pop()` &mdash;&mdash; 删除栈顶的元素。
-  `top()` &mdash;&mdash; 获取栈顶元素。
-  `getMin()` &mdash;&mdash; 检索栈中的最小元素。
 

 **示例:** 

```
输入：
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

输出：
[null,null,null,null,-3,null,0,-2]

解释：
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

```
 

 **提示：** 
-  `pop` 、 `top` 和 `getMin` 操作总是在 **非空栈** 上调用。
 
**标签**
`栈` `设计` 


## 
```python

```
>
# 156.上下翻转二叉树
[https://leetcode-cn.com/problems/binary-tree-upside-down](https://leetcode-cn.com/problems/binary-tree-upside-down) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 157.用 Read4 读取 N 个字符
[https://leetcode-cn.com/problems/read-n-characters-given-read4](https://leetcode-cn.com/problems/read-n-characters-given-read4) 
## 原题

 
**标签**
`字符串` `交互` `模拟` 


## 
```python

```
>
# 158.用 Read4 读取 N 个字符 II
[https://leetcode-cn.com/problems/read-n-characters-given-read4-ii-call-multiple-times](https://leetcode-cn.com/problems/read-n-characters-given-read4-ii-call-multiple-times) 
## 原题

 
**标签**
`字符串` `交互` `模拟` 


## 
```python

```
>
# 159.至多包含两个不同字符的最长子串
[https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters](https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters) 
## 原题

 
**标签**
`哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
# 160.相交链表
[https://leetcode-cn.com/problems/intersection-of-two-linked-lists](https://leetcode-cn.com/problems/intersection-of-two-linked-lists) 
## 原题
给你两个单链表的头节点 `headA` 和 `headB` ，请你找出并返回两个单链表相交的起始节点。如果两个链表不存在相交节点，返回 `null` 。

图示两个链表在节点 `c1` 开始相交 **：** 

<a href="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png" target="_blank"><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png" style="height: 130px; width: 400px;" /></a>

题目数据 **保证** 整个链式结构中不存在环。

 **注意** ，函数返回结果后，链表必须 **保持其原始结构** 。

 **自定义评测：** 

 **评测系统** 的输入如下（你设计的程序 **不适用** 此输入）：
-  `intersectVal` - 相交的起始节点的值。如果不存在相交节点，这一值为 `0` 
-  `listA` - 第一个链表
-  `listB` - 第二个链表
-  `skipA` - 在 `listA` 中（从头节点开始）跳到交叉节点的节点数
-  `skipB` - 在 `listB` 中（从头节点开始）跳到交叉节点的节点数
评测系统将根据这些输入创建链式数据结构，并将两个头节点 `headA` 和 `headB` 传递给你的程序。如果程序能够正确返回相交节点，那么你的解决方案将被 **视作正确答案** 。

 

 **示例 1：** 

<a href="https://assets.leetcode.com/uploads/2018/12/13/160_example_1.png" target="_blank"><img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_1_1.png" style="height: 130px; width: 400px;" /></a>

```

输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,6,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。

```
 **示例 2：** 

<a href="https://assets.leetcode.com/uploads/2018/12/13/160_example_2.png" target="_blank"><img alt="" src="https://assets.leetcode.com/uploads/2021/03/05/160_example_2.png" style="height: 136px; width: 350px;" /></a>

```

输入：intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [1,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。

```
 **示例 3：** 

<a href="https://assets.leetcode.com/uploads/2018/12/13/160_example_3.png" target="_blank"><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png" style="height: 126px; width: 200px;" /></a>

```

输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。

```
 

 **提示：** 
-  `listA` 中节点数目为 `m` 
-  `listB` 中节点数目为 `n` 
-  `1 <= m, n <= 3 * 10^4` 
-  `1 <= Node.val <= 10^5` 
-  `0 <= skipA <= m` 
-  `0 <= skipB <= n` 
- 如果 `listA` 和 `listB` 没有交点， `intersectVal` 为 `0` 
- 如果 `listA` 和 `listB` 有交点， `intersectVal == listA[skipA] == listB[skipB]` 
 

 **进阶：** 你能否设计一个时间复杂度 `O(m + n)` 、仅用 `O(1)` 内存的解决方案？

 
**标签**
`哈希表` `链表` `双指针` 


## 
```python

```
>
# 161.相隔为 1 的编辑距离
[https://leetcode-cn.com/problems/one-edit-distance](https://leetcode-cn.com/problems/one-edit-distance) 
## 原题

 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 162.寻找峰值
[https://leetcode-cn.com/problems/find-peak-element](https://leetcode-cn.com/problems/find-peak-element) 
## 原题
峰值元素是指其值严格大于左右相邻值的元素。

给你一个整数数组 `nums` ，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 **任何一个峰值** 所在位置即可。

你可以假设 `nums[-1] = nums[n] = -∞` 。

你必须实现时间复杂度为 `O(log n)` 的算法来解决此问题。

 

 **示例 1：** 

```

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
```
 **示例 2：** 

```

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
- 对于所有有效的 `i` 都有 `nums[i] != nums[i + 1]` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 163.缺失的区间
[https://leetcode-cn.com/problems/missing-ranges](https://leetcode-cn.com/problems/missing-ranges) 
## 原题

 
**标签**
`数组` 


## 
```python

```
>
# 164.最大间距
[https://leetcode-cn.com/problems/maximum-gap](https://leetcode-cn.com/problems/maximum-gap) 
## 原题
给定一个无序的数组 `nums` ，返回 *数组在排序之后，相邻元素之间最大的差值* 。如果数组元素个数小于 2，则返回 `0` 。

您必须编写一个在「线性时间」内运行并使用「线性额外空间」的算法。

 

 **示例 1:** 

```

输入: nums = [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
```
 **示例 2:** 

```

输入: nums = [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
```
 

 **提示:** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^9` 
 
**标签**
`数组` `桶排序` `基数排序` `排序` 


## 
```python

```
>
# 165.比较版本号
[https://leetcode-cn.com/problems/compare-version-numbers](https://leetcode-cn.com/problems/compare-version-numbers) 
## 原题
给你两个版本号 `version1` 和 `version2` ，请你比较它们。

版本号由一个或多个修订号组成，各修订号由一个 `'.'` 连接。每个修订号由 **多位数字** 组成，可能包含 **前导零** 。每个版本号至少包含一个字符。修订号从左到右编号，下标从 0 开始，最左边的修订号下标为 0 ，下一个修订号下标为 1 ，以此类推。例如， `2.5.33` 和 `0.1` 都是有效的版本号。

比较版本号时，请按从左到右的顺序依次比较它们的修订号。比较修订号时，只需比较 **忽略任何前导零后的整数值** 。也就是说，修订号 `1` 和修订号 `001` **相等** 。如果版本号没有指定某个下标处的修订号，则该修订号视为 `0` 。例如，版本 `1.0` 小于版本 `1.1` ，因为它们下标为 `0` 的修订号相同，而下标为 `1` 的修订号分别为 `0` 和 `1` ， `0 < 1` 。

返回规则如下：
- 如果 ` *version1* > *version2* ` 返回 `1` ，
- 如果 ` *version1* < *version2* ` 返回 `-1` ，
- 除此之外返回 `0` 。
 

 **示例 1：** 

```

输入：version1 = "1.01", version2 = "1.001"
输出：0
解释：忽略前导零，"01" 和 "001" 都表示相同的整数 "1"

```
 **示例 2：** 

```

输入：version1 = "1.0", version2 = "1.0.0"
输出：0
解释：version1 没有指定下标为 2 的修订号，即视为 "0"

```
 **示例 3：** 

```

输入：version1 = "0.1", version2 = "1.1"
输出：-1
解释：version1 中下标为 0 的修订号是 "0"，version2 中下标为 0 的修订号是 "1" 。0 < 1，所以 version1 < version2

```
 

 **提示：** 
-  `1 <= version1.length, version2.length <= 500` 
-  `version1` 和 `version2` 仅包含数字和 `'.'` 
-  `version1` 和 `version2` 都是 **有效版本号** 
-  `version1` 和 `version2` 的所有修订号都可以存储在 **32 位整数** 中
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 166.分数到小数
[https://leetcode-cn.com/problems/fraction-to-recurring-decimal](https://leetcode-cn.com/problems/fraction-to-recurring-decimal) 
## 原题
给定两个整数，分别表示分数的分子  `numerator` 和分母 `denominator` ，以 **字符串形式返回小数** 。

如果小数部分为循环小数，则将循环的部分括在括号内。

<p class="MachineTrans-lang-zh-CN">如果存在多个答案，只需返回 **任意一个** 。

<p class="MachineTrans-lang-zh-CN">对于所有给定的输入， **保证** 答案字符串的长度小于 `10^4` 。

 

 **示例 1：** 

```

输入：numerator = 1, denominator = 2
输出："0.5"

```
 **示例 2：** 

```

输入：numerator = 2, denominator = 1
输出："2"

```
 **示例 3：** 

```

输入：numerator = 2, denominator = 3
输出："0.(6)"

```
 **示例 4：** 

```

输入：numerator = 4, denominator = 333
输出："0.(012)"

```
 **示例 5：** 

```

输入：numerator = 1, denominator = 5
输出："0.2"

```
 

 **提示：** 
-  `-2^31 <= numerator, denominator <= 2^31 - 1` 
-  `denominator != 0` 
 
**标签**
`哈希表` `数学` `字符串` 


## 
```python

```
>
# 167.两数之和 II - 输入有序数组
[https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted](https://leetcode-cn.com/problems/two-sum-ii-input-array-is-sorted) 
## 原题
给你一个下标从 **1** 开始的整数数组 `numbers` ，该数组已按 **非递减顺序排列** ，请你从数组中找出满足相加之和等于目标数 `target` 的两个数。如果设这两个数分别是 `numbers[index<sub>1</sub>]` 和 `numbers[index<sub>2</sub>]` ，则 `1 <= index<sub>1</sub> < index<sub>2</sub> <= numbers.length` 。

以长度为 2 的整数数组 `[index<sub>1</sub>, index<sub>2</sub>]` 的形式返回这两个整数的下标 `index<sub>1</sub>` 和 `index<sub>2</sub>` 。

你可以假设每个输入 **只对应唯一的答案** ，而且你 **不可以** 重复使用相同的元素。

你所设计的解决方案必须只使用常量级的额外空间。
 

 **示例 1：** 

```

输入：numbers = [2,7,11,15], target = 9
输出：[1,2]
解释：2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。
```
 **示例 2：** 

```

输入：numbers = [2,3,4], target = 6
输出：[1,3]
解释：2 与 4 之和等于目标数 6 。因此 index1 = 1, index2 = 3 。返回 [1, 3] 。
```
 **示例 3：** 

```

输入：numbers = [-1,0], target = -1
输出：[1,2]
解释：-1 与 0 之和等于目标数 -1 。因此 index1 = 1, index2 = 2 。返回 [1, 2] 。

```
 

 **提示：** 
-  `2 <= numbers.length <= 3 * 10^4` 
-  `-1000 <= numbers[i] <= 1000` 
-  `numbers` 按 **非递减顺序** 排列
-  `-1000 <= target <= 1000` 
-  **仅存在一个有效答案** 
 
**标签**
`数组` `双指针` `二分查找` 


## 
```python

```
>
# 168.Excel表列名称
[https://leetcode-cn.com/problems/excel-sheet-column-title](https://leetcode-cn.com/problems/excel-sheet-column-title) 
## 原题
给你一个整数  `columnNumber` ，返回它在 Excel 表中相对应的列名称。

例如：

```

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...

```
 

 **示例 1：** 

```

输入：columnNumber = 1
输出："A"

```
 **示例 2：** 

```

输入：columnNumber = 28
输出："AB"

```
 **示例 3：** 

```

输入：columnNumber = 701
输出："ZY"

```
 **示例 4：** 

```

输入：columnNumber = 2147483647
输出："FXSHRXW"

```
 

 **提示：** 
-  `1 <= columnNumber <= 2^31 - 1` 
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 169.多数元素
[https://leetcode-cn.com/problems/majority-element](https://leetcode-cn.com/problems/majority-element) 
## 原题
给定一个大小为 *n* 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 **大于**   `⌊ n/2 ⌋`  的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

 **示例 1：** 

```

输入：[3,2,3]
输出：3
```
 **示例 2：** 

```

输入：[2,2,1,1,1,2,2]
输出：2

```
 

 **进阶：** 
- 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。
 
**标签**
`数组` `哈希表` `分治` `计数` `排序` 


## 
```python

```
>
# 170.两数之和 III - 数据结构设计
[https://leetcode-cn.com/problems/two-sum-iii-data-structure-design](https://leetcode-cn.com/problems/two-sum-iii-data-structure-design) 
## 原题

 
**标签**
`设计` `数组` `哈希表` `双指针` `数据流` 


## 
```python

```
>
# 171.Excel 表列序号
[https://leetcode-cn.com/problems/excel-sheet-column-number](https://leetcode-cn.com/problems/excel-sheet-column-number) 
## 原题
给你一个字符串 `columnTitle` ，表示 Excel 表格中的列名称。返回 *该列名称对应的列序号* 。

例如：

```

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
```
 

 **示例 1:** 

```

输入: columnTitle = "A"
输出: 1

```
 **示例 2:** 

```

输入: columnTitle = "AB"
输出: 28

```
 **示例 3:** 

```

输入: columnTitle = "ZY"
输出: 701
```
 

 **提示：** 
-  `1 <= columnTitle.length <= 7` 
-  `columnTitle` 仅由大写英文组成
-  `columnTitle` 在范围 `["A", "FXSHRXW"]` 内
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 172.阶乘后的零
[https://leetcode-cn.com/problems/factorial-trailing-zeroes](https://leetcode-cn.com/problems/factorial-trailing-zeroes) 
## 原题
给定一个整数 `n` ，返回 `n!` 结果中尾随零的数量。

提示 `n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1` 

 

 **示例 1：** 

```

输入：n = 3
输出：0
解释：3! = 6 ，不含尾随 0

```
 **示例 2：** 

```

输入：n = 5
输出：1
解释：5! = 120 ，有一个尾随 0

```
 **示例 3：** 

```

输入：n = 0
输出：0

```
 

 **提示：** 
-  `0 <= n <= 10^4` 
 

<b>进阶：</b>你可以设计并实现对数时间复杂度的算法来解决此问题吗？

 
**标签**
`数学` 


## 
```python

```
>
# 173.二叉搜索树迭代器
[https://leetcode-cn.com/problems/binary-search-tree-iterator](https://leetcode-cn.com/problems/binary-search-tree-iterator) 
## 原题
实现一个二叉搜索树迭代器类 `BSTIterator` ，表示一个按中序遍历二叉搜索树（BST）的迭代器：
-  `BSTIterator(TreeNode root)` 初始化 `BSTIterator` 类的一个对象。BST 的根节点 `root` 会作为构造函数的一部分给出。指针应初始化为一个不存在于 BST 中的数字，且该数字小于 BST 中的任何元素。
-  `boolean hasNext()` 如果向指针右侧遍历存在数字，则返回 `true` ；否则返回 `false` 。
-  `int next()` 将指针向右移动，然后返回指针处的数字。
注意，指针初始化为一个不存在于 BST 中的数字，所以对 `next()` 的首次调用将返回 BST 中的最小元素。
你可以假设  `next()`  调用总是有效的，也就是说，当调用 `next()`  时，BST 的中序遍历中至少存在一个下一个数字。

 

 **示例：** 
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png" style="width: 189px; height: 178px;" />
```

输入
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
输出
[null, 3, 7, true, 9, true, 15, true, 20, false]

解释
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
bSTIterator.next();    // 返回 3
bSTIterator.next();    // 返回 7
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 9
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 15
bSTIterator.hasNext(); // 返回 True
bSTIterator.next();    // 返回 20
bSTIterator.hasNext(); // 返回 False

```
 

 **提示：** 
- 树中节点的数目在范围 `[1, 10^5]` 内
-  `0 <= Node.val <= 10^6` 
- 最多调用 `10^5` 次 `hasNext` 和 `next` 操作
 

 **进阶：** 
- 你可以设计一个满足下述条件的解决方案吗？ `next()` 和 `hasNext()` 操作均摊时间复杂度为 `O(1)` ，并使用 `O(h)` 内存。其中 `h` 是树的高度。
 
**标签**
`栈` `树` `设计` `二叉搜索树` `二叉树` `迭代器` 


## 
```python

```
>
# 174.地下城游戏
[https://leetcode-cn.com/problems/dungeon-game](https://leetcode-cn.com/problems/dungeon-game) 
## 原题
<style>
table.dungeon, .dungeon th, .dungeon td {
  border:3px solid black;
}

 .dungeon th, .dungeon td {
    text-align: center;
    height: 70px;
    width: 70px;
}
</style>

一些恶魔抓住了公主（ **P** ）并将她关在了地下城的右下角。地下城是由 M x N 个房间组成的二维网格。我们英勇的骑士（ **K** ）最初被安置在左上角的房间里，他必须穿过地下城并通过对抗恶魔来拯救公主。

骑士的初始健康点数为一个正整数。如果他的健康点数在某一时刻降至 0 或以下，他会立即死亡。

有些房间由恶魔守卫，因此骑士在进入这些房间时会失去健康点数（若房间里的值为 *负整数* ，则表示骑士将损失健康点数）；其他房间要么是空的（房间里的值为 *0* ），要么包含增加骑士健康点数的魔法球（若房间里的值为 *正整数* ，则表示骑士将增加健康点数）。

为了尽快到达公主，骑士决定每次只向右或向下移动一步。

 

 **编写一个函数来计算确保骑士能够拯救到公主所需的最低初始健康点数。** 

例如，考虑到如下布局的地下城，如果骑士遵循最佳路径 `右 -> 右 -> 下 -> 下` ，则骑士的初始健康点数至少为 **7** 。

<table class="dungeon">
<tr> 
<td>-2 (K)</td> 
<td>-3</td> 
<td>3</td> 
</tr> 
<tr> 
<td>-5</td> 
<td>-10</td> 
<td>1</td> 
</tr> 
<tr> 
<td>10</td> 
<td>30</td> 
<td>-5 (P)</td> 
</tr> 
</table>
<!---2K   -3  3
-5   -10   1
10 30   5P-->

 

 **说明:** 


- 
	骑士的健康点数没有上限。
	
- 任何房间都可能对骑士的健康点数造成威胁，也可能增加骑士的健康点数，包括骑士进入的左上角房间以及公主被监禁的右下角房间。

 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 175.组合两个表
[https://leetcode-cn.com/problems/combine-two-tables](https://leetcode-cn.com/problems/combine-two-tables) 
## 原题
表1: `Person` 

```
+-------------+---------+
| 列名         | 类型     |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
PersonId 是上表主键

```
表2: `Address` 

```
+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
AddressId 是上表主键

```
 

编写一个 SQL 查询，满足条件：无论 person 是否有地址信息，都需要基于上述两表提供 person 的以下信息：

 

```
FirstName, LastName, City, State

```
 
**标签**
`数据库` 


## 
```python

```
>
# 176.第二高的薪水
[https://leetcode-cn.com/problems/second-highest-salary](https://leetcode-cn.com/problems/second-highest-salary) 
## 原题
 `Employee` 表：
```

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id 是这个表的主键。
表的每一行包含员工的工资信息。

```
 

编写一个 SQL 查询，获取并返回 `Employee` 表中第二高的薪水 。如果不存在第二高的薪水，查询应该返回 `null` 。

查询结果如下例所示。

 

 **示例 1：** 

```

输入：
Employee 表：
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
输出：
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

```
 **示例 2：** 

```

输入：
Employee 表：
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
输出：
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+

```
 
**标签**
`数据库` 


## 
```python

```
>
# 177.第N高的薪水
[https://leetcode-cn.com/problems/nth-highest-salary](https://leetcode-cn.com/problems/nth-highest-salary) 
## 原题
表: `Employee` 

```

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
Id是该表的主键列。
该表的每一行都包含有关员工工资的信息。

```
 

编写一个SQL查询来报告 `Employee` 表中第 `n` 高的工资。如果没有第 `n` 个最高工资，查询应该报告为 `null` 。

查询结果格式如下所示。

 

 **示例 1:** 

```

输入: 
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
n = 2
输出: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| 200                    |
+------------------------+

```
 **示例 2:** 

```

输入: 
Employee 表:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
n = 2
输出: 
+------------------------+
| getNthHighestSalary(2) |
+------------------------+
| null                   |
+------------------------+
```
 
**标签**
`数据库` 


## 
```python

```
>
# 178.分数排名
[https://leetcode-cn.com/problems/rank-scores](https://leetcode-cn.com/problems/rank-scores) 
## 原题
表: `Scores` 

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
Id是该表的主键。
该表的每一行都包含了一场比赛的分数。Score是一个有两位小数点的浮点值。

```
 

编写 SQL 查询对分数进行排序。排名按以下规则计算:
- 分数应按从高到低排列。
- 如果两个分数相等，那么两个分数的排名应该相同。
- 在排名相同的分数后，排名数应该是下一个连续的整数。换句话说，排名之间不应该有空缺的数字。
按 `score` 降序返回结果表。

查询结果格式如下所示。

 

 **示例 1:** 

```

输入: 
Scores 表:
+----+-------+
| id | score |
+----+-------+
| 1  | 3.50  |
| 2  | 3.65  |
| 3  | 4.00  |
| 4  | 3.85  |
| 5  | 4.00  |
| 6  | 3.65  |
+----+-------+
输出: 
+-------+------+
| score | rank |
+-------+------+
| 4.00  | 1    |
| 4.00  | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.50  | 4    |
+-------+------+
```
 
**标签**
`数据库` 


## 
```python

```
>
# 179.最大数
[https://leetcode-cn.com/problems/largest-number](https://leetcode-cn.com/problems/largest-number) 
## 原题
给定一组非负整数 `nums` ，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。

 **注意：** 输出结果可能非常大，所以你需要返回一个字符串而不是整数。

 

 **示例 1：** 

```

输入：nums = [10,2]
输出："210"
```
 **示例 2：** 

```

输入：nums = [3,30,34,5,9]
输出："9534330"

```
 **示例 3：** 

```

输入：nums = [1]
输出："1"

```
 **示例 4：** 

```

输入：nums = [10]
输出："10"

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `0 <= nums[i] <= 10^9` 
 
**标签**
`贪心` `字符串` `排序` 


## 
```python

```
>
# 180.连续出现的数字
[https://leetcode-cn.com/problems/consecutive-numbers](https://leetcode-cn.com/problems/consecutive-numbers) 
## 原题
表： `Logs` 

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
id 是这个表的主键。
```
 

编写一个 SQL 查询，查找所有至少连续出现三次的数字。

返回的结果表中的数据可以按 **任意顺序** 排列。

查询结果格式如下面的例子所示：

 

 **示例 1:** 

```

输入：
Logs 表：
+----+-----+
| Id | Num |
+----+-----+
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
+----+-----+
输出：
Result 表：
+-----------------+
| ConsecutiveNums |
+-----------------+
| 1               |
+-----------------+
解释：1 是唯一连续出现至少三次的数字。
```
 
**标签**
`数据库` 


## 
```python

```
>
# 181.超过经理收入的员工
[https://leetcode-cn.com/problems/employees-earning-more-than-their-managers](https://leetcode-cn.com/problems/employees-earning-more-than-their-managers) 
## 原题
表： `Employee` 

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
Id是该表的主键。
该表的每一行都表示雇员的ID、姓名、工资和经理的ID。

```
 

编写一个SQL查询来查找收入比经理高的员工。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。

 

 **示例 1:** 

```

输入: 
Employee 表:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
输出: 
+----------+
| Employee |
+----------+
| Joe      |
+----------+
解释: Joe 是唯一挣得比经理多的雇员。
```
 
**标签**
`数据库` 


## 
```python

```
>
# 182.查找重复的电子邮箱
[https://leetcode-cn.com/problems/duplicate-emails](https://leetcode-cn.com/problems/duplicate-emails) 
## 原题
编写一个 SQL 查询，查找 `Person` 表中所有重复的电子邮箱。

 **示例：** 

```
+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+

```
根据以上输入，你的查询应返回以下结果：

```
+---------+
| Email   |
+---------+
| a@b.com |
+---------+

```
 **说明：** 所有电子邮箱都是小写字母。

 
**标签**
`数据库` 


## 
```python

```
>
# 183.从不订购的客户
[https://leetcode-cn.com/problems/customers-who-never-order](https://leetcode-cn.com/problems/customers-who-never-order) 
## 原题
某网站包含两个表， `Customers` 表和 `Orders` 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。

 `Customers` 表：

```
+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

```
 `Orders` 表：

```
+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

```
例如给定上述表格，你的查询应返回：

```
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

```
 
**标签**
`数据库` 


## 
```python

```
>
# 184.部门工资最高的员工
[https://leetcode-cn.com/problems/department-highest-salary](https://leetcode-cn.com/problems/department-highest-salary) 
## 原题
表： `Employee` 

```

+--------------+---------+
| 列名          | 类型    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id是此表的主键列。
departmentId是Department表中ID的外键。
此表的每一行都表示员工的ID、姓名和工资。它还包含他们所在部门的ID。

```
 

表： `Department` 

```

+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id是此表的主键列。
此表的每一行都表示一个部门的ID及其名称。

```
 

编写SQL查询以查找每个部门中薪资最高的员工。<br />
按 **任意顺序** 返回结果表。<br />
查询结果格式如下例所示。

 

 **示例 1:** 

```

输入：
Employee 表:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 70000  | 1            |
| 2  | Jim   | 90000  | 1            |
| 3  | Henry | 80000  | 2            |
| 4  | Sam   | 60000  | 2            |
| 5  | Max   | 90000  | 1            |
+----+-------+--------+--------------+
Department 表:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
输出：
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Jim      | 90000  |
| Sales      | Henry    | 80000  |
| IT         | Max      | 90000  |
+------------+----------+--------+
解释：Max 和 Jim 在 IT 部门的工资都是最高的，Henry 在销售部的工资最高。
```
 
**标签**
`数据库` 


## 
```python

```
>
# 185.部门工资前三高的所有员工
[https://leetcode-cn.com/problems/department-top-three-salaries](https://leetcode-cn.com/problems/department-top-three-salaries) 
## 原题
表: `Employee` 

```

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
Id是该表的主键列。
departmentId是Department表中ID的外键。
该表的每一行都表示员工的ID、姓名和工资。它还包含了他们部门的ID。

```
 

表: `Department` 

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
Id是该表的主键列。
该表的每一行表示部门ID和部门名。

```
 

公司的主管们感兴趣的是公司每个部门中谁赚的钱最多。一个部门的 **高收入者** 是指一个员工的工资在该部门的 **不同** 工资中 **排名前三** 。

编写一个SQL查询，找出每个部门中 **收入高的员工** 。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。

 

 **示例 1:** 

```

输入: 
Employee 表:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
Department  表:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
输出: 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
解释:
在IT部门:
- Max的工资最高
- 兰迪和乔都赚取第二高的独特的薪水
- 威尔的薪水是第三高的

在销售部:
- 亨利的工资最高
- 山姆的薪水第二高
- 没有第三高的工资，因为只有两名员工
```
 
**标签**
`数据库` 


## 
```python

```
>
# 186.翻转字符串里的单词 II
[https://leetcode-cn.com/problems/reverse-words-in-a-string-ii](https://leetcode-cn.com/problems/reverse-words-in-a-string-ii) 
## 原题

 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 187.重复的DNA序列
[https://leetcode-cn.com/problems/repeated-dna-sequences](https://leetcode-cn.com/problems/repeated-dna-sequences) 
## 原题
 **DNA序列** 由一系列核苷酸组成，缩写为<meta charset="UTF-8" /> `'A'` , `'C'` , `'G'` 和<meta charset="UTF-8" /> `'T'` .。
- 例如，<meta charset="UTF-8" /> `"ACGAATTCCG"` 是一个 **DNA序列** 。
在研究 **DNA** 时，识别 DNA 中的重复序列非常有用。

给定一个表示 **DNA序列** 的字符串 `s` ，返回所有在 DNA 分子中出现不止一次的 **长度为 `10` ** 的序列(子字符串)。你可以按 **任意顺序** 返回答案。

 

 **示例 1：** 

```

输入：s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
输出：["AAAAACCCCC","CCCCCAAAAA"]

```
 **示例 2：** 

```

输入：s = "AAAAAAAAAAAAA"
输出：["AAAAAAAAAA"]

```
 

 **提示：** 
-  `0 <= s.length <= 10^5` 
-  `s[i]` `==` `'A'` 、 `'C'` 、 `'G'` or `'T'` 
 
**标签**
`位运算` `哈希表` `字符串` `滑动窗口` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 188.买卖股票的最佳时机 IV
[https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv) 
## 原题
给定一个整数数组  `prices` ，它的第 `i` 个元素  `prices[i]` 是一支给定的股票在第 `i` 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 **k** 笔交易。

 **注意：** 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

 **示例 1：** 

```

输入：k = 2, prices = [2,4,1]
输出：2
解释：在第 1 天 (股票价格 = 2) 的时候买入，在第 2 天 (股票价格 = 4) 的时候卖出，这笔交易所能获得利润 = 4-2 = 2 。
```
 **示例 2：** 

```

输入：k = 2, prices = [3,2,6,5,0,3]
输出：7
解释：在第 2 天 (股票价格 = 2) 的时候买入，在第 3 天 (股票价格 = 6) 的时候卖出, 这笔交易所能获得利润 = 6-2 = 4 。
     随后，在第 5 天 (股票价格 = 0) 的时候买入，在第 6 天 (股票价格 = 3) 的时候卖出, 这笔交易所能获得利润 = 3-0 = 3 。
```
 

 **提示：** 
-  `0 <= k <= 100` 
-  `0 <= prices.length <= 1000` 
-  `0 <= prices[i] <= 1000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 189.轮转数组
[https://leetcode-cn.com/problems/rotate-array](https://leetcode-cn.com/problems/rotate-array) 
## 原题
给你一个数组，将数组中的元素向右轮转 `k` 个位置，其中 `k` 是非负数。

 

 **示例 1:** 

```

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

```
 **示例 2:** 

```

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
-  `0 <= k <= 10^5` 
 

 **进阶：** 
- 尽可能想出更多的解决方案，至少有 **三种** 不同的方法可以解决这个问题。
- 你可以使用空间复杂度为 `O(1)` 的 **原地** 算法解决这个问题吗？
 
**标签**
`数组` `数学` `双指针` 


## 
```python

```
>
# 190.颠倒二进制位
[https://leetcode-cn.com/problems/reverse-bits](https://leetcode-cn.com/problems/reverse-bits) 
## 原题
颠倒给定的 32 位无符号整数的二进制位。

 **提示：** 
- 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
- 在 Java 中，编译器使用<a href="https://baike.baidu.com/item/二进制补码/5295284" target="_blank">二进制补码</a>记法来表示有符号整数。因此，在 **示例 2** 中，输入表示有符号整数 `-3` ，输出表示有符号整数 `-1073741825` 。
 

 **示例 1：** 

```

输入：n = 00000010100101000001111010011100
输出：964176192 (00111001011110000010100101000000)
解释：输入的二进制串 00000010100101000001111010011100 表示无符号整数 43261596，
     因此返回 964176192，其二进制表示形式为 00111001011110000010100101000000。
```
 **示例 2：** 

```

输入：n = 11111111111111111111111111111101
输出：3221225471 (10111111111111111111111111111111)
解释：输入的二进制串 11111111111111111111111111111101 表示无符号整数 4294967293，
     因此返回 3221225471 其二进制表示形式为 10111111111111111111111111111111 。
```
 

 **提示：** 
- 输入是一个长度为 `32` 的二进制字符串
 

 **进阶** : 如果多次调用这个函数，你将如何优化你的算法？

 
**标签**
`位运算` `分治` 


## 
```python

```
>
# 191.位1的个数
[https://leetcode-cn.com/problems/number-of-1-bits](https://leetcode-cn.com/problems/number-of-1-bits) 
## 原题
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为<a href="https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E9%87%8D%E9%87%8F" target="_blank">汉明重量</a>）。

 

 **提示：** 
- 请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
- 在 Java 中，编译器使用<a href="https://baike.baidu.com/item/二进制补码/5295284" target="_blank">二进制补码</a>记法来表示有符号整数。因此，在上面的  **示例 3**  中，输入表示有符号整数 `-3` 。
 

 **示例 1：** 

```

输入：00000000000000000000000000001011
输出：3
解释：输入的二进制串 00000000000000000000000000001011 中，共有三位为 '1'。

```
 **示例 2：** 

```

输入：00000000000000000000000010000000
输出：1
解释：输入的二进制串 00000000000000000000000010000000 中，共有一位为 '1'。

```
 **示例 3：** 

```

输入：11111111111111111111111111111101
输出：31
解释：输入的二进制串 11111111111111111111111111111101 中，共有 31 位为 '1'。
```
 

 **提示：** 
- 输入必须是长度为 `32` 的 **二进制串** 。
 

 **进阶** ：
- 如果多次调用这个函数，你将如何优化你的算法？
 
**标签**
`位运算` 


## 
```python

```
>
# 192.统计词频
[https://leetcode-cn.com/problems/word-frequency](https://leetcode-cn.com/problems/word-frequency) 
## 原题
写一个 bash 脚本以统计一个文本文件 `words.txt` 中每个单词出现的频率。

为了简单起见，你可以假设：
-  `words.txt` 只包括小写字母和 `'; ';` 。
- 每个单词只由小写字母组成。
- 单词间由一个或多个空格字符分隔。
 **示例:** 

假设 `words.txt` 内容如下：

```
the day is sunny the the
the sunny is is

```
你的脚本应当输出（以词频降序排列）：

```
the 4
is 3
sunny 2
day 1

```
 **说明:** 
- 不要担心词频相同的单词的排序问题，每个单词出现的频率都是唯一的。
- 你可以使用一行 <a href="http://tldp.org/HOWTO/Bash-Prog-Intro-HOWTO-4.html">Unix pipes</a> 实现吗？
 
**标签**
`Shell` 


## 
```python

```
>
# 193.有效电话号码
[https://leetcode-cn.com/problems/valid-phone-numbers](https://leetcode-cn.com/problems/valid-phone-numbers) 
## 原题
给定一个包含电话号码列表（一行一个电话号码）的文本文件 `file.txt` ，写一个单行 bash 脚本输出所有有效的电话号码。

你可以假设一个有效的电话号码必须满足以下两种格式： (xxx) xxx-xxxx 或 xxx-xxx-xxxx。（x 表示一个数字）

你也可以假设每行前后没有多余的空格字符。

 

 **示例：** 

假设  `file.txt`  内容如下：

```

987-123-4567
123 456 7890
(123) 456-7890

```
你的脚本应当输出下列有效的电话号码：

```

987-123-4567
(123) 456-7890

```
 
**标签**
`Shell` 


## 
```python

```
>
# 194.转置文件
[https://leetcode-cn.com/problems/transpose-file](https://leetcode-cn.com/problems/transpose-file) 
## 原题
给定一个文件  `file.txt` ，转置它的内容。

你可以假设每行列数相同，并且每个字段由  `' '` 分隔。

 

 **示例：** 

假设  `file.txt`  文件内容如下：

```

name age
alice 21
ryan 30

```
应当输出：

```

name alice ryan
age 21 30

```
 
**标签**
`Shell` 


## 
```python

```
>
# 195.第十行
[https://leetcode-cn.com/problems/tenth-line](https://leetcode-cn.com/problems/tenth-line) 
## 原题
给定一个文本文件 `file.txt` ，请只打印这个文件中的第十行。

 **示例:** 

假设 `file.txt` 有如下内容：

```
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10

```
你的脚本应当显示第十行：

```
Line 10

```
 **说明:** <br>
1. 如果文件少于十行，你应当输出什么？<br>
2. 至少有三种不同的解法，请尝试尽可能多的方法来解题。

 
**标签**
`Shell` 


## 
```python

```
>
# 196.删除重复的电子邮箱
[https://leetcode-cn.com/problems/delete-duplicate-emails](https://leetcode-cn.com/problems/delete-duplicate-emails) 
## 原题
编写一个 SQL 查询，来删除 `Person` 表中所有重复的电子邮箱，重复的邮箱里只保留 **Id** *最小* 的那个。

```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id 是这个表的主键。

```
例如，在运行你的查询语句之后，上面的 `Person` 表应返回以下几行:

```
+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

```
 

 **提示：** 
- 执行 SQL 之后，输出是整个 `Person` 表。
- 使用 `delete` 语句。
 
**标签**
`数据库` 


## 
```python

```
>
# 197.上升的温度
[https://leetcode-cn.com/problems/rising-temperature](https://leetcode-cn.com/problems/rising-temperature) 
## 原题


表： `Weather` 

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id 是这个表的主键
该表包含特定日期的温度信息
```
 

编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 `id` 。

返回结果 **不要求顺序** 。

查询结果格式如下例。

 

 **示例 1：** 

```

输入：
Weather 表：
+----+------------+-------------+
| id | recordDate | Temperature |
+----+------------+-------------+
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |
+----+------------+-------------+
输出：
+----+
| id |
+----+
| 2  |
| 4  |
+----+
解释：
2015-01-02 的温度比前一天高（10 -> 25）
2015-01-04 的温度比前一天高（20 -> 30）
```
 
**标签**
`数据库` 


## 
```python

```
>
# 198.打家劫舍
[https://leetcode-cn.com/problems/house-robber](https://leetcode-cn.com/problems/house-robber) 
## 原题
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统， **如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警** 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 **不触动警报装置的情况下** ，一夜之内能够偷窃到的最高金额。

 

 **示例 1：** 

```

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
```
 **示例 2：** 

```

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `0 <= nums[i] <= 400` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 199.二叉树的右视图
[https://leetcode-cn.com/problems/binary-tree-right-side-view](https://leetcode-cn.com/problems/binary-tree-right-side-view) 
## 原题
给定一个二叉树的 **根节点** `root` ，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

 

 **示例 1:** 

<img src="https://assets.leetcode.com/uploads/2021/02/14/tree.jpg" style="width: 270px; " />

```

输入: [1,2,3,null,5,null,4]
输出: [1,3,4]

```
 **示例 2:** 

```

输入: [1,null,3]
输出: [1,3]

```
 **示例 3:** 

```

输入: []
输出: []

```
 

 **提示:** 
- 二叉树的节点个数的范围是 `[0,100]` 
- <meta charset="UTF-8" /> `-100 <= Node.val <= 100`  
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 200.岛屿数量
[https://leetcode-cn.com/problems/number-of-islands](https://leetcode-cn.com/problems/number-of-islands) 
## 原题
给你一个由  `'1'` （陆地）和 `'0'` （水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

 **示例 1：** 

```

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

```
 **示例 2：** 

```

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 300` 
-  `grid[i][j]` 的值为 `'0'` 或 `'1'` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` 


## 
```python

```
>
