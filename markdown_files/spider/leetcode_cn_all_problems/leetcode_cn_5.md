# 501.二叉搜索树中的众数
[https://leetcode-cn.com/problems/find-mode-in-binary-search-tree](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree) 
## 原题
给你一个含重复值的二叉搜索树（BST）的根节点 `root` ，找出并返回 BST 中的所有 <a href="https://baike.baidu.com/item/%E4%BC%97%E6%95%B0/44796" target="_blank">众数</a>（即，出现频率最高的元素）。

如果树中有不止一个众数，可以按 **任意顺序** 返回。

假定 BST 满足如下定义：
- 结点左子树中所含节点的值 **小于等于** 当前节点的值
- 结点右子树中所含节点的值 **大于等于** 当前节点的值
- 左子树和右子树都是二叉搜索树
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg" style="width: 142px; height: 222px;" />
```

输入：root = [1,null,2,2]
输出：[2]

```
 **示例 2：** 

```

输入：root = [0]
输出：[0]

```
 

 **提示：** 
- 树中节点的数目在范围 `[1, 10^4]` 内
-  `-10^5 <= Node.val <= 10^5` 
 

 **进阶：** 你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）

 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 502.IPO
[https://leetcode-cn.com/problems/ipo](https://leetcode-cn.com/problems/ipo) 
## 原题
假设 力扣（LeetCode）即将开始 **IPO** 。为了以更高的价格将股票卖给风险投资公司，力扣 希望在 IPO 之前开展一些项目以增加其资本。 由于资源有限，它只能在 IPO 之前完成最多 `k` 个不同的项目。帮助 力扣 设计完成最多 `k` 个不同项目后得到最大总资本的方式。

给你 `n` 个项目。对于每个项目 `i` **** ，它都有一个纯利润 `profits[i]` ，和启动该项目需要的最小资本 `capital[i]` 。

最初，你的资本为 `w` 。当你完成一个项目时，你将获得纯利润，且利润将被添加到你的总资本中。

总而言之，从给定项目中选择 **最多** `k` 个不同项目的列表，以 **最大化最终资本** ，并输出最终可获得的最多资本。

答案保证在 32 位有符号整数范围内。

 

 **示例 1：** 

```

输入：k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
输出：4
解释：
由于你的初始资本为 0，你仅可以从 0 号项目开始。
在完成后，你将获得 1 的利润，你的总资本将变为 1。
此时你可以选择开始 1 号或 2 号项目。
由于你最多可以选择两个项目，所以你需要完成 2 号项目以获得最大的资本。
因此，输出最后最大化的资本，为 0 + 1 + 3 = 4。

```
 **示例 2：** 

```

输入：k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
输出：6

```
 

 **提示：** 
-  `1 <= k <= 10^5` 
-  `0 <= w <= 10^9` 
-  `n == profits.length` 
-  `n == capital.length` 
-  `1 <= n <= 10^5` 
-  `0 <= profits[i] <= 10^4` 
-  `0 <= capital[i] <= 10^9` 
 
**标签**
`贪心` `数组` `排序` `堆（优先队列）` 


## 
```python

```
>
# 503.下一个更大元素 II
[https://leetcode-cn.com/problems/next-greater-element-ii](https://leetcode-cn.com/problems/next-greater-element-ii) 
## 原题
给定一个循环数组 `nums` （ `nums[nums.length - 1]` 的下一个元素是 `nums[0]` ），返回 *`nums` 中每个元素的 **下一个更大元素*** 。

数字 `x` 的 **下一个更大的元素** 是按数组遍历顺序，这个数字之后的第一个比它更大的数，这意味着你应该循环地搜索它的下一个更大的数。如果不存在，则输出 `-1` 。

 

 **示例 1:** 

```

输入: nums = [1,2,1]
输出: [2,-1,2]
解释: 第一个 1 的下一个更大的数是 2；
数字 2 找不到下一个更大的数； 
第二个 1 的下一个最大的数需要循环搜索，结果也是 2。

```
 **示例 2:** 

```

输入: nums = [1,2,3,4,3]
输出: [2,3,4,-1,4]

```
 

 **提示:** 
-  `1 <= nums.length <= 10^4` 
-  `-10^9 <= nums[i] <= 10^9` 
 
**标签**
`栈` `数组` `单调栈` 


## 
```python

```
>
# 504.七进制数
[https://leetcode-cn.com/problems/base-7](https://leetcode-cn.com/problems/base-7) 
## 原题
给定一个整数 `num` ，将其转化为 **7 进制** ，并以字符串形式输出。

 

 **示例 1:** 

```

输入: num = 100
输出: "202"

```
 **示例 2:** 

```

输入: num = -7
输出: "-10"

```
 

 **提示：** 
-  `-10^7 <= num <= 10^7` 
 
**标签**
`数学` 


## 
```python

```
>
# 505.迷宫 II
[https://leetcode-cn.com/problems/the-maze-ii](https://leetcode-cn.com/problems/the-maze-ii) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `图` `最短路` `堆（优先队列）` 


## 
```python

```
>
# 506.相对名次
[https://leetcode-cn.com/problems/relative-ranks](https://leetcode-cn.com/problems/relative-ranks) 
## 原题
给你一个长度为 `n` 的整数数组 `score` ，其中 `score[i]` 是第 `i` 位运动员在比赛中的得分。所有得分都 **互不相同** 。

运动员将根据得分 **决定名次** ，其中名次第 `1` 的运动员得分最高，名次第 `2` 的运动员得分第 `2` 高，依此类推。运动员的名次决定了他们的获奖情况：
- 名次第 `1` 的运动员获金牌 `"Gold Medal"` 。
- 名次第 `2` 的运动员获银牌 `"Silver Medal"` 。
- 名次第 `3` 的运动员获铜牌 `"Bronze Medal"` 。
- 从名次第 `4` 到第 `n` 的运动员，只能获得他们的名次编号（即，名次第 `x` 的运动员获得编号 `"x"` ）。
使用长度为 `n` 的数组 `answer` 返回获奖，其中 `answer[i]` 是第 `i` 位运动员的获奖情况。

 

 **示例 1：** 

```

输入：score = [5,4,3,2,1]
输出：["Gold Medal","Silver Medal","Bronze Medal","4","5"]
解释：名次为 [1^st, 2^nd, 3^rd, 4^th, 5^th] 。
```
 **示例 2：** 

```

输入：score = [10,3,8,9,4]
输出：["Gold Medal","5","Bronze Medal","Silver Medal","4"]
解释：名次为 [1^st, 5^th, 3^rd, 2^nd, 4^th] 。

```
 

 **提示：** 
-  `n == score.length` 
-  `1 <= n <= 10^4` 
-  `0 <= score[i] <= 10^6` 
-  `score` 中的所有值 **互不相同** 
 
**标签**
`数组` `排序` `堆（优先队列）` 


## 
```python

```
>
# 507.完美数
[https://leetcode-cn.com/problems/perfect-number](https://leetcode-cn.com/problems/perfect-number) 
## 原题
对于一个 **正整数** ，如果它和除了它自身以外的所有 **正因子** 之和相等，我们称它为 **「完美数」** 。

给定一个 **整数** `n` ， 如果是完美数，返回 `true` ；否则返回 `false` 。

 

 **示例 1：** 

```

输入：num = 28
输出：true
解释：28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 和 14 是 28 的所有正因子。
```
 **示例 2：** 

```

输入：num = 7
输出：true

```
 

 **提示：** 
-  `1 <= num <= 10^8` 
 
**标签**
`数学` 


## 
```python

```
>
# 508.出现次数最多的子树元素和
[https://leetcode-cn.com/problems/most-frequent-subtree-sum](https://leetcode-cn.com/problems/most-frequent-subtree-sum) 
## 原题
给你一个二叉树的根结点 `root` ，请返回出现次数最多的子树元素和。如果有多个元素出现的次数相同，返回所有出现次数最多的子树元素和（不限顺序）。

一个结点的 **「子树元素和」** 定义为以该结点为根的二叉树上所有结点的元素之和（包括结点本身）。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/04/24/freq1-tree.jpg" />

```

输入: root = [5,2,-3]
输出: [2,-3,4]

```
 **示例 2：** 

<img src="https://assets.leetcode.com/uploads/2021/04/24/freq2-tree.jpg" />

```

输入: root = [5,2,-5]
输出: [2]

```
 

 **提示:** 
- 节点数在 `[1, 10^4]` 范围内
-  `-10^5 <= Node.val <= 10^5` 
 
**标签**
`树` `深度优先搜索` `哈希表` `二叉树` 


## 
```python

```
>
# 509.斐波那契数
[https://leetcode-cn.com/problems/fibonacci-number](https://leetcode-cn.com/problems/fibonacci-number) 
## 原题
 **斐波那契数** （通常用 `F(n)` 表示）形成的序列称为 **斐波那契数列** 。该数列由 `0` 和 `1` 开始，后面的每一项数字都是前面两项数字的和。也就是：

```

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1

```
给定 `n` ，请计算 `F(n)` 。

 

 **示例 1：** 

```

输入：n = 2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1

```
 **示例 2：** 

```

输入：n = 3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2

```
 **示例 3：** 

```

输入：n = 4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3

```
 

 **提示：** 
-  `0 <= n <= 30` 
 
**标签**
`递归` `记忆化搜索` `数学` `动态规划` 


## 
```python

```
>
# 510.二叉搜索树中的中序后继 II
[https://leetcode-cn.com/problems/inorder-successor-in-bst-ii](https://leetcode-cn.com/problems/inorder-successor-in-bst-ii) 
## 原题

 
**标签**
`树` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 511.游戏玩法分析 I
[https://leetcode-cn.com/problems/game-play-analysis-i](https://leetcode-cn.com/problems/game-play-analysis-i) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 512.游戏玩法分析 II
[https://leetcode-cn.com/problems/game-play-analysis-ii](https://leetcode-cn.com/problems/game-play-analysis-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 513.找树左下角的值
[https://leetcode-cn.com/problems/find-bottom-left-tree-value](https://leetcode-cn.com/problems/find-bottom-left-tree-value) 
## 原题
给定一个二叉树的 **根节点** `root` ，请找出该二叉树的  **最底层 最左边 ** 节点的值。

假设二叉树中至少有一个节点。

 

 **示例 1:** 

<img src="https://assets.leetcode.com/uploads/2020/12/14/tree1.jpg" style="width: 182px; " />

```

输入: root = [2,1,3]
输出: 1

```
 **示例 2:** 

<img src="https://assets.leetcode.com/uploads/2020/12/14/tree2.jpg" style="width: 242px; " /> **** 

```

输入: [1,2,3,4,null,5,6,null,null,7]
输出: 7

```
 

 **提示:** 
- 二叉树的节点个数的范围是 `[1,10^4]` 
- <meta charset="UTF-8" /> `-2^31 <= Node.val <= 2^31 - 1`  
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 514.自由之路
[https://leetcode-cn.com/problems/freedom-trail](https://leetcode-cn.com/problems/freedom-trail) 
## 原题
电子游戏“辐射4”中，任务 **“通向自由”** 要求玩家到达名为 “ **Freedom Trail Ring”** 的金属表盘，并使用表盘拼写特定关键词才能开门。

给定一个字符串 `ring` ，表示刻在外环上的编码；给定另一个字符串 `key` ，表示需要拼写的关键词。您需要算出能够拼写关键词中所有字符的 **最少** 步数。

最初， **ring** 的第一个字符与 `12:00` 方向对齐。您需要顺时针或逆时针旋转 `ring` 以使 **key** 的一个字符在 `12:00` 方向对齐，然后按下中心按钮，以此逐个拼写完 ** `key` ** 中的所有字符。

旋转 `ring` **** 拼出 key 字符 `key[i]` **** 的阶段中：
- 您可以将 **ring** 顺时针或逆时针旋转 **一个位置** ，计为1步。旋转的最终目的是将字符串 ** `ring` ** 的一个字符与 `12:00` 方向对齐，并且这个字符必须等于字符 ** `key[i]` 。** 
- 如果字符 ** `key[i]` ** 已经对齐到12:00方向，您需要按下中心按钮进行拼写，这也将算作 **1 步** 。按完之后，您可以开始拼写 **key** 的下一个字符（下一阶段）, 直至完成所有拼写。
 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2018/10/22/ring.jpg" style="height: 450px; width: 450px;" />

<center> </center>

```

输入: ring = "godding", key = "gd"
输出: 4
解释:
 对于 key 的第一个字符 'g'，已经在正确的位置, 我们只需要1步来拼写这个字符。 
 对于 key 的第二个字符 'd'，我们需要逆时针旋转 ring "godding" 2步使它变成 "ddinggo"。
 当然, 我们还需要1步进行拼写。
 因此最终的输出是 4。

```
 **示例 2:** 

```

输入: ring = "godding", key = "godding"
输出: 13

```
 

 **提示：** 
-  `1 <= ring.length, key.length <= 100` 
-  `ring` 和 `key` 只包含小写英文字母
-  **保证** 字符串 `key` 一定可以由字符串 `ring` 旋转拼出
 
**标签**
`深度优先搜索` `广度优先搜索` `字符串` `动态规划` 


## 
```python

```
>
# 515.在每个树行中找最大值
[https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row) 
## 原题
给定一棵二叉树的根节点 `root` ，请找出该二叉树中每一层的最大值。

 

 **示例1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/21/largest_e1.jpg" style="height: 172px; width: 300px;" />

```

输入: root = [1,3,2,5,3,null,9]
输出: [1,3,9]

```
 **示例2：** 

```

输入: root = [1,2,3]
输出: [1,3]

```
 

 **提示：** 
- 二叉树的节点个数的范围是 `[0,10^4]` 
- <meta charset="UTF-8" /> `-2^31 <= Node.val <= 2^31 - 1` 
 

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 516.最长回文子序列
[https://leetcode-cn.com/problems/longest-palindromic-subsequence](https://leetcode-cn.com/problems/longest-palindromic-subsequence) 
## 原题
给你一个字符串 `s` ，找出其中最长的回文子序列，并返回该序列的长度。

子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。

 

 **示例 1：** 

```

输入：s = "bbbab"
输出：4
解释：一个可能的最长回文子序列为 "bbbb" 。

```
 **示例 2：** 

```

输入：s = "cbbd"
输出：2
解释：一个可能的最长回文子序列为 "bb" 。

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s` 仅由小写英文字母组成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 517.超级洗衣机
[https://leetcode-cn.com/problems/super-washing-machines](https://leetcode-cn.com/problems/super-washing-machines) 
## 原题
假设有 `n` **** 台超级洗衣机放在同一排上。开始的时候，每台洗衣机内可能有一定量的衣服，也可能是空的。

在每一步操作中，你可以选择任意 `m` ( `1 <= m <= n` ) 台洗衣机，与此同时将每台洗衣机的一件衣服送到相邻的一台洗衣机。

给定一个整数数组 `machines` 代表从左至右每台洗衣机中的衣物数量，请给出能让所有洗衣机中剩下的衣物的数量相等的 **最少的操作步数** 。如果不能使每台洗衣机中衣物的数量相等，则返回 `-1` 。

 

 **示例 1：** 

```

输入：machines = [1,0,5]
输出：3
解释：
第一步:    1     0 <-- 5    =>    1     1     4
第二步:    1 <-- 1 <-- 4    =>    2     1     3    
第三步:    2     1 <-- 3    =>    2     2     2   

```
 **示例 2：** 

```

输入：machines = [0,3,0]
输出：2
解释：
第一步:    0 <-- 3     0    =>    1     2     0    
第二步:    1     2 --> 0    =>    1     1     1     

```
 **示例 3：** 

```

输入：machines = [0,2,0]
输出：-1
解释：
不可能让所有三个洗衣机同时剩下相同数量的衣物。

```
 

 **提示：** 
-  `n == machines.length` 
-  `1 <= n <= 10^4` 
-  `0 <= machines[i] <= 10^5` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 518.零钱兑换 II
[https://leetcode-cn.com/problems/coin-change-2](https://leetcode-cn.com/problems/coin-change-2) 
## 原题
给你一个整数数组 `coins` 表示不同面额的硬币，另给一个整数 `amount` 表示总金额。

请你计算并返回可以凑成总金额的硬币组合数。如果任何硬币组合都无法凑出总金额，返回 `0` 。

假设每一种面额的硬币有无限个。 

题目数据保证结果符合 32 位带符号整数。

 
 **示例 1：** 

```

输入：amount = 5, coins = [1, 2, 5]
输出：4
解释：有四种方式可以凑成总金额：
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

```
 **示例 2：** 

```

输入：amount = 3, coins = [2]
输出：0
解释：只用面额 2 的硬币不能凑成总金额 3 。

```
 **示例 3：** 

```

输入：amount = 10, coins = [10] 
输出：1

```
 

 **提示：** 
-  `1 <= coins.length <= 300` 
-  `1 <= coins[i] <= 5000` 
-  `coins` 中的所有值 **互不相同** 
-  `0 <= amount <= 5000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 519.随机翻转矩阵
[https://leetcode-cn.com/problems/random-flip-matrix](https://leetcode-cn.com/problems/random-flip-matrix) 
## 原题
给你一个 `m x n` 的二元矩阵 `matrix` ，且所有值被初始化为 `0` 。请你设计一个算法，随机选取一个满足 `matrix[i][j] == 0` 的下标 `(i, j)` ，并将它的值变为 `1` 。所有满足 `matrix[i][j] == 0` 的下标 `(i, j)` 被选取的概率应当均等。

尽量最少调用内置的随机函数，并且优化时间和空间复杂度。

实现 `Solution` 类：
-  `Solution(int m, int n)` 使用二元矩阵的大小 `m` 和 `n` 初始化该对象
-  `int[] flip()` 返回一个满足 `matrix[i][j] == 0` 的随机下标 `[i, j]` ，并将其对应格子中的值变为 `1` 
-  `void reset()` 将矩阵中所有的值重置为 `0` 
 

 **示例：** 

```

输入
["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]
输出
[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

解释
Solution solution = new Solution(3, 1);
solution.flip();  // 返回 [1, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
solution.flip();  // 返回 [2, 0]，因为 [1,0] 已经返回过了，此时返回 [2,0] 和 [0,0] 的概率应当相同
solution.flip();  // 返回 [0, 0]，根据前面已经返回过的下标，此时只能返回 [0,0]
solution.reset(); // 所有值都重置为 0 ，并可以再次选择下标返回
solution.flip();  // 返回 [2, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
```
 

 **提示：** 
-  `1 <= m, n <= 10^4` 
- 每次调用 `flip` 时，矩阵中至少存在一个值为 0 的格子。
- 最多调用 `1000` 次 `flip` 和 `reset` 方法。
 
**标签**
`水塘抽样` `哈希表` `数学` `随机化` 


## 
```python

```
>
# 520.检测大写字母
[https://leetcode-cn.com/problems/detect-capital](https://leetcode-cn.com/problems/detect-capital) 
## 原题
我们定义，在以下情况时，单词的大写用法是正确的：
- 全部字母都是大写，比如 `"USA"` 。
- 单词中所有字母都不是大写，比如 `"leetcode"` 。
- 如果单词不只含有一个字母，只有首字母大写， 比如 `"Google"` 。
给你一个字符串 `word` 。如果大写用法正确，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：word = "USA"
输出：true

```
 **示例 2：** 

```

输入：word = "FlaG"
输出：false

```
 

 **提示：** 
-  `1 <= word.length <= 100` 
-  `word` 由小写和大写英文字母组成
 
**标签**
`字符串` 


## 
```python

```
>
# 521.最长特殊序列 Ⅰ
[https://leetcode-cn.com/problems/longest-uncommon-subsequence-i](https://leetcode-cn.com/problems/longest-uncommon-subsequence-i) 
## 原题
给你两个字符串 `a` 和 `b` ，请返回 *这两个字符串中 **最长的特殊序列*** 。如果不存在，则返回 `-1` 。

 **「最长特殊序列」** 定义如下：该序列为 **某字符串独有的最长子序列（即不能是其他字符串的子序列）** 。

字符串 `s` 的子序列是在从 `s` 中删除任意数量的字符后可以获得的字符串。
- 例如， `“abc”` 是 `“aebdc”` 的子序列，因为您可以删除 `“aebdc”` 中的下划线字符来得到 `“abc”` 。 `“aebdc”` 的子序列还包括 `“aebdc”` 、 `“aeb”` 和 `“”` (空字符串)。
 

 **示例 1：** 

```

输入: a = "aba", b = "cdc"
输出: 3
解释: 最长特殊序列可为 "aba" (或 "cdc")，两者均为自身的子序列且不是对方的子序列。
```
 **示例 2：** 

```

输入：a = "aaa", b = "bbb"
输出：3
解释: 最长特殊序列是“aaa”和“bbb”。

```
 **示例 3：** 

```

输入：a = "aaa", b = "aaa"
输出：-1
解释: 字符串a的每个子序列也是字符串b的每个子序列。同样，字符串b的每个子序列也是字符串a的子序列。

```
 

 **提示：** 
-  `1 <= a.length, b.length <= 100` 
-  `a` 和 `b` 由小写英文字母组成
 
**标签**
`字符串` 


## 
```python

```
>
# 522.最长特殊序列 II
[https://leetcode-cn.com/problems/longest-uncommon-subsequence-ii](https://leetcode-cn.com/problems/longest-uncommon-subsequence-ii) 
## 原题
给定字符串列表，你需要从它们中找出最长的特殊序列。最长特殊序列定义如下：该序列为某字符串独有的最长子序列（即不能是其他字符串的子序列）。

 **子序列** 可以通过删去字符串中的某些字符实现，但不能改变剩余字符的相对顺序。空序列为所有字符串的子序列，任何字符串为其自身的子序列。

输入将是一个字符串列表，输出是最长特殊序列的长度。如果最长特殊序列不存在，返回 -1 。

 

 **示例：** 

```
输入: "aba", "cdc", "eae"
输出: 3

```
 

 **提示：** 
- 所有给定的字符串长度不会超过 10 。
- 给定字符串列表的长度将在 [2, 50 ] 之间。
 

 
**标签**
`数组` `哈希表` `双指针` `字符串` `排序` 


## 
```python

```
>
# 523.连续的子数组和
[https://leetcode-cn.com/problems/continuous-subarray-sum](https://leetcode-cn.com/problems/continuous-subarray-sum) 
## 原题
给你一个整数数组 `nums` 和一个整数  `k` ，编写一个函数来判断该数组是否含有同时满足下述条件的连续子数组：
- 子数组大小 **至少为 2** ，且
- 子数组元素总和为 `k` 的倍数。
如果存在，返回 `true` ；否则，返回 `false` 。

如果存在一个整数 `n` ，令整数 `x` 符合 `x = n * k` ，则称 `x` 是 `k` 的一个倍数。 `0` 始终视为 `k` 的一个倍数。

 

 **示例 1：** 

```

输入：nums = [23,2,4,6,7], k = 6
输出：true
解释：[2,4] 是一个大小为 2 的子数组，并且和为 6 。
```
 **示例 2：** 

```

输入：nums = [23,2,6,4,7], k = 6
输出：true
解释：[23, 2, 6, 4, 7] 是大小为 5 的子数组，并且和为 42 。 
42 是 6 的倍数，因为 42 = 7 * 6 且 7 是一个整数。

```
 **示例 3：** 

```

输入：nums = [23,2,6,4,7], k = 13
输出：false

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^9` 
-  `0 <= sum(nums[i]) <= 2^31 - 1` 
-  `1 <= k <= 2^31 - 1` 
 
**标签**
`数组` `哈希表` `数学` `前缀和` 


## 
```python

```
>
# 524.通过删除字母匹配到字典里最长单词
[https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting](https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting) 
## 原题
给你一个字符串 `s` 和一个字符串数组 `dictionary` ，找出并返回 `dictionary` 中最长的字符串，该字符串可以通过删除 `s` 中的某些字符得到。

如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。

 

 **示例 1：** 

```

输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
输出："apple"

```
 **示例 2：** 

```

输入：s = "abpcplea", dictionary = ["a","b","c"]
输出："a"

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `1 <= dictionary.length <= 1000` 
-  `1 <= dictionary[i].length <= 1000` 
-  `s` 和 `dictionary[i]` 仅由小写英文字母组成
 
**标签**
`数组` `双指针` `字符串` `排序` 


## 
```python

```
>
# 525.连续数组
[https://leetcode-cn.com/problems/contiguous-array](https://leetcode-cn.com/problems/contiguous-array) 
## 原题
给定一个二进制数组 `nums` , 找到含有相同数量的 `0` 和 `1` 的最长连续子数组，并返回该子数组的长度。

 

 **示例 1:** 

```

输入: nums = [0,1]
输出: 2
说明: [0, 1] 是具有相同数量 0 和 1 的最长连续子数组。
```
 **示例 2:** 

```

输入: nums = [0,1,0]
输出: 2
说明: [0, 1] (或 [1, 0]) 是具有相同数量0和1的最长连续子数组。
```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `nums[i]` 不是 `0` 就是 `1` 
 
**标签**
`数组` `哈希表` `前缀和` 


## 
```python

```
>
# 526.优美的排列
[https://leetcode-cn.com/problems/beautiful-arrangement](https://leetcode-cn.com/problems/beautiful-arrangement) 
## 原题
假设有从 1 到 n 的 n 个整数。用这些整数构造一个数组 `perm` （ **下标从 1 开始** ），只要满足下述条件 **之一** ，该数组就是一个 **优美的排列** ：
-  `perm[i]` 能够被 `i` 整除
-  `i` 能够被 `perm[i]` 整除
给你一个整数 `n` ，返回可以构造的 **优美排列** 的 **数量** 。

 

 **示例 1：** 

```

输入：n = 2
输出：2
解释：
第 1 个优美的排列是 [1,2]：
    - perm[1] = 1 能被 i = 1 整除
    - perm[2] = 2 能被 i = 2 整除
第 2 个优美的排列是 [2,1]:
    - perm[1] = 2 能被 i = 1 整除
    - i = 2 能被 perm[2] = 1 整除

```
 **示例 2：** 

```

输入：n = 1
输出：1

```
 

 **提示：** 
-  `1 <= n <= 15` 
 
**标签**
`位运算` `数组` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 527.单词缩写
[https://leetcode-cn.com/problems/word-abbreviation](https://leetcode-cn.com/problems/word-abbreviation) 
## 原题

 
**标签**
`贪心` `字典树` `数组` `字符串` `排序` 


## 
```python

```
>
# 528.按权重随机选择
[https://leetcode-cn.com/problems/random-pick-with-weight](https://leetcode-cn.com/problems/random-pick-with-weight) 
## 原题
给你一个 **下标从 0 开始** 的正整数数组 `w` ，其中 `w[i]` 代表第 `i` 个下标的权重。

请你实现一个函数 `pickIndex` ，它可以 **随机地** 从范围 `[0, w.length - 1]` 内（含 `0` 和 `w.length - 1` ）选出并返回一个下标。选取下标 `i` 的 **概率** 为 `w[i] / sum(w)` 。
- 例如，对于 `w = [1, 3]` ，挑选下标 `0` 的概率为 `1 / (1 + 3) = 0.25` （即，25%），而选取下标 `1` 的概率为 `3 / (1 + 3) = 0.75` （即， `75%` ）。
 

 **示例 1：** 

```

输入：
["Solution","pickIndex"]
[[[1]],[]]
输出：
[null,0]
解释：
Solution solution = new Solution([1]);
solution.pickIndex(); // 返回 0，因为数组中只有一个元素，所以唯一的选择是返回下标 0。
```
 **示例 2：** 

```

输入：
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
输出：
[null,1,1,1,1,0]
解释：
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // 返回 1，返回下标 1，返回该下标概率为 3/4 。
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 1
solution.pickIndex(); // 返回 0，返回下标 0，返回该下标概率为 1/4 。

由于这是一个随机问题，允许多个答案，因此下列输出都可以被认为是正确的:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
诸若此类。

```
 

 **提示：** 
-  `1 <= w.length <= 10^4` 
-  `1 <= w[i] <= 10^5` 
-  `pickIndex` 将被调用不超过 `10^4` 次
 
**标签**
`数学` `二分查找` `前缀和` `随机化` 


## 
```python

```
>
# 529.扫雷游戏
[https://leetcode-cn.com/problems/minesweeper](https://leetcode-cn.com/problems/minesweeper) 
## 原题
让我们一起来玩扫雷游戏！

给你一个大小为 `m x n` 二维字符矩阵 `board` ，表示扫雷游戏的盘面，其中：
-  `'M'` 代表一个 **未挖出的** 地雷，
-  `'E'` 代表一个 **未挖出的** 空方块，
-  `'B'` **** 代表没有相邻（上，下，左，右，和所有4个对角线）地雷的 **已挖出的** 空白方块，
-  **数字** （ `'1'` 到 `'8'` ）表示有多少地雷与这块 **已挖出的** 方块相邻，
-  `'X'` 则表示一个 **已挖出的** 地雷。
给你一个整数数组 `click` ，其中 `click = [click<sub>r</sub>, click<sub>c</sub>]` 表示在所有 **未挖出的** 方块（ `'M'` 或者 `'E'` ）中的下一个点击位置（ `click<sub>r</sub>` 是行下标， `click<sub>c</sub>` 是列下标）。

根据以下规则，返回相应位置被点击后对应的盘面：
- 如果一个地雷（ `'M'` ）被挖出，游戏就结束了- 把它改为 `'X'` 。
- 如果一个 **没有相邻地雷** 的空方块（ `'E'` ）被挖出，修改它为（ `'B'` ），并且所有和其相邻的 **未挖出** 方块都应该被递归地揭露。
- 如果一个 **至少与一个地雷相邻** 的空方块（ `'E'` ）被挖出，修改它为数字（ `'1'` 到 `'8'` ），表示相邻地雷的数量。
- 如果在此次点击中，若无更多方块可被揭露，则返回盘面。
 

 **示例 1：** 
<img src="https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_1.png" style="width: 500px; max-width: 400px; height: 269px;" />
```

输入：board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]
输出：[["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

```
 **示例 2：** 
<img src="https://assets.leetcode.com/uploads/2018/10/12/minesweeper_example_2.png" style="width: 500px; max-width: 400px; height: 275px;" />
```

输入：board = [["B","1","E","1","B"],["B","1","M","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]], click = [1,2]
输出：[["B","1","E","1","B"],["B","1","X","1","B"],["B","1","1","1","B"],["B","B","B","B","B"]]

```
 

 **提示：** 
-  `m == board.length` 
-  `n == board[i].length` 
-  `1 <= m, n <= 50` 
-  `board[i][j]` 为 `'M'` 、 `'E'` 、 `'B'` 或数字 `'1'` 到 `'8'` 中的一个
-  `click.length == 2` 
-  `0 <= click<sub>r</sub> < m` 
-  `0 <= click<sub>c</sub> < n` 
-  `board[click<sub>r</sub>][click<sub>c</sub>]` 为 `'M'` 或 `'E'` 
 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 530.二叉搜索树的最小绝对差
[https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst](https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst) 
## 原题
给你一个二叉搜索树的根节点 `root` ，返回 **树中任意两不同节点值之间的最小差值** 。

差值是一个正数，其数值等于两值之差的绝对值。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg" style="width: 292px; height: 301px;" />
```

输入：root = [4,2,6,1,3]
输出：1

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg" style="width: 282px; height: 301px;" />
```

输入：root = [1,0,48,null,null,12,49]
输出：1

```
 

 **提示：** 
- 树中节点的数目范围是 `[2, 10^4]` 
-  `0 <= Node.val <= 10^5` 
 

 **注意：** 本题与 783 <a href="https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/">https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes/</a> 相同

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 531.孤独像素 I
[https://leetcode-cn.com/problems/lonely-pixel-i](https://leetcode-cn.com/problems/lonely-pixel-i) 
## 原题

 
**标签**
`数组` `哈希表` `矩阵` 


## 
```python

```
>
# 532.数组中的 k-diff 数对
[https://leetcode-cn.com/problems/k-diff-pairs-in-an-array](https://leetcode-cn.com/problems/k-diff-pairs-in-an-array) 
## 原题
给定一个整数数组和一个整数 `**k**` ，你需要在数组里找到 **不同的** k-diff 数对，并返回不同的 **k-diff 数对** 的数目。

这里将 **k-diff** 数对定义为一个整数对 `(nums[i], nums[j])` ，并满足下述全部条件：
-  `0 <= i < j < nums.length` 
-  `|nums[i] - nums[j]| == k` 
 **注意** ， `|val|` 表示 `val` 的绝对值。

 

 **示例 1：** 

```

输入：nums = [3, 1, 4, 1, 5], k = 2
输出：2
解释：数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
尽管数组中有两个1，但我们只应返回不同的数对的数量。

```
 **示例 2：** 

```

输入：nums = [1, 2, 3, 4, 5], k = 1
输出：4
解释：数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。

```
 **示例 3：** 

```

输入：nums = [1, 3, 1, 5, 4], k = 0
输出：1
解释：数组中只有一个 0-diff 数对，(1, 1)。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `-10^7 <= nums[i] <= 10^7` 
-  `0 <= k <= 10^7` 
 
**标签**
`数组` `哈希表` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 533.孤独像素 II
[https://leetcode-cn.com/problems/lonely-pixel-ii](https://leetcode-cn.com/problems/lonely-pixel-ii) 
## 原题

 
**标签**
`数组` `哈希表` `矩阵` 


## 
```python

```
>
# 534.游戏玩法分析 III
[https://leetcode-cn.com/problems/game-play-analysis-iii](https://leetcode-cn.com/problems/game-play-analysis-iii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 535.TinyURL 的加密与解密
[https://leetcode-cn.com/problems/encode-and-decode-tinyurl](https://leetcode-cn.com/problems/encode-and-decode-tinyurl) 
## 原题
TinyURL是一种URL简化服务， 比如：当你输入一个URL `https://leetcode.com/problems/design-tinyurl` 时，它将返回一个简化的URL `http://tinyurl.com/4e9iAk` .

要求：设计一个 TinyURL 的加密 `encode` 和解密 `decode` 的方法。你的加密和解密算法如何设计和运作是没有限制的，你只需要保证一个URL可以被加密成一个TinyURL，并且这个TinyURL可以用解密方法恢复成原本的URL。

 
**标签**
`设计` `哈希表` `字符串` `哈希函数` 


## 
```python

```
>
# 536.从字符串生成二叉树
[https://leetcode-cn.com/problems/construct-binary-tree-from-string](https://leetcode-cn.com/problems/construct-binary-tree-from-string) 
## 原题

 
**标签**
`树` `深度优先搜索` `字符串` `二叉树` 


## 
```python

```
>
# 537.复数乘法
[https://leetcode-cn.com/problems/complex-number-multiplication](https://leetcode-cn.com/problems/complex-number-multiplication) 
## 原题
<a href="https://baike.baidu.com/item/%E5%A4%8D%E6%95%B0/254365?fr=aladdin" target="_blank">复数</a> 可以用字符串表示，遵循 `" **实部** + **虚部** i"` 的形式，并满足下述条件：
-  `实部` 是一个整数，取值范围是 `[-100, 100]` 
-  `虚部` 也是一个整数，取值范围是 `[-100, 100]` 
-  `i^2 == -1` 
给你两个字符串表示的复数 `num1` 和 `num2` ，请你遵循复数表示形式，返回表示它们乘积的字符串。

 

 **示例 1：** 

```

输入：num1 = "1+1i", num2 = "1+1i"
输出："0+2i"
解释：(1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i ，你需要将它转换为 0+2i 的形式。

```
 **示例 2：** 

```

输入：num1 = "1+-1i", num2 = "1+-1i"
输出："0+-2i"
解释：(1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i ，你需要将它转换为 0+-2i 的形式。 

```
 

 **提示：** 
-  `num1` 和 `num2` 都是有效的复数表示。
 
**标签**
`数学` `字符串` `模拟` 


## 
```python

```
>
# 538.把二叉搜索树转换为累加树
[https://leetcode-cn.com/problems/convert-bst-to-greater-tree](https://leetcode-cn.com/problems/convert-bst-to-greater-tree) 
## 原题
给出二叉 **搜索** 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 `node` 的新值等于原树中大于或等于 `node.val` 的值之和。

提醒一下，二叉搜索树满足下列约束条件：
- 节点的左子树仅包含键 **小于** 节点键的节点。
- 节点的右子树仅包含键 **大于** 节点键的节点。
- 左右子树也必须是二叉搜索树。
 **注意：** 本题和 1038: <a href="https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/">https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree/</a> 相同

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/05/03/tree.png" style="height: 364px; width: 534px;">** 

```
输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

```
 **示例 2：** 

```
输入：root = [0,null,1]
输出：[1,null,1]

```
 **示例 3：** 

```
输入：root = [1,0,2]
输出：[3,3,2]

```
 **示例 4：** 

```
输入：root = [3,2,4,1]
输出：[7,9,4,10]

```
 

 **提示：** 
- 树中的节点数介于 `0` 和 `10^4` ^ 之间。
- 每个节点的值介于 `-10^4` 和 `10^4` 之间。
- 树中的所有值 **互不相同** 。
- 给定的树为二叉搜索树。
 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 539.最小时间差
[https://leetcode-cn.com/problems/minimum-time-difference](https://leetcode-cn.com/problems/minimum-time-difference) 
## 原题
给定一个 24 小时制（小时:分钟 **"HH:MM"** ）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。

 

 **示例 1：** 

```

输入：timePoints = ["23:59","00:00"]
输出：1

```
 **示例 2：** 

```

输入：timePoints = ["00:00","23:59","00:00"]
输出：0

```
 

 **提示：** 
-  `2 <= timePoints.length <= 2 * 10^4` 
-  `timePoints[i]` 格式为 **"HH:MM"** 
 
**标签**
`数组` `数学` `字符串` `排序` 


## 
```python

```
>
# 540.有序数组中的单一元素
[https://leetcode-cn.com/problems/single-element-in-a-sorted-array](https://leetcode-cn.com/problems/single-element-in-a-sorted-array) 
## 原题
给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。

请你找出并返回只出现一次的那个数。

你设计的解决方案必须满足 `O(log n)` 时间复杂度和 `O(1)` 空间复杂度。

 

 **示例 1:** 

```

输入: nums = [1,1,2,3,3,4,4,8,8]
输出: 2

```
 **示例 2:** 

```

输入: nums =  [3,3,7,7,10,11,11]
输出: 10

```
 

<meta charset="UTF-8" />

 **提示:** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^5` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 541.反转字符串 II
[https://leetcode-cn.com/problems/reverse-string-ii](https://leetcode-cn.com/problems/reverse-string-ii) 
## 原题
给定一个字符串 `s` 和一个整数 `k` ，从字符串开头算起，每计数至 `2k` 个字符，就反转这 `2k` 字符中的前 `k` 个字符。
- 如果剩余字符少于 `k` 个，则将剩余字符全部反转。
- 如果剩余字符小于 `2k` 但大于或等于 `k` 个，则反转前 `k` 个字符，其余字符保持原样。
 

 **示例 1：** 

```

输入：s = "abcdefg", k = 2
输出："bacdfeg"

```
 **示例 2：** 

```

输入：s = "abcd", k = 2
输出："bacd"

```
 

 **提示：** 
-  `1 <= s.length <= 10^4` 
-  `s` 仅由小写英文组成
-  `1 <= k <= 10^4` 
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 542.01 矩阵
[https://leetcode-cn.com/problems/01-matrix](https://leetcode-cn.com/problems/01-matrix) 
## 原题
给定一个由 `0` 和 `1` 组成的矩阵 `mat`  ，请输出一个大小相同的矩阵，其中每一个格子是 `mat` 中对应位置元素到最近的 `0` 的距离。

两个相邻元素间的距离为 `1` 。

 

<b>示例 1：</b>

<img alt="" src="https://pic.leetcode-cn.com/1626667201-NCWmuP-image.png" style="width: 150px; " />

```

输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]

```
<b>示例 2：</b>

<img alt="" src="https://pic.leetcode-cn.com/1626667205-xFxIeK-image.png" style="width: 150px; " />

```

输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat[i].length` 
-  `1 <= m, n <= 10^4` 
-  `1 <= m * n <= 10^4` 
-  `mat[i][j] is either 0 or 1.` 
-  `mat` 中至少有一个 `0 ` 
 
**标签**
`广度优先搜索` `数组` `动态规划` `矩阵` 


## 
```python

```
>
# 543.二叉树的直径
[https://leetcode-cn.com/problems/diameter-of-binary-tree](https://leetcode-cn.com/problems/diameter-of-binary-tree) 
## 原题
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

 

 **示例 :** <br>
给定二叉树

```
          1
         / \
        2   3
       / \     
      4   5    

```
返回 **3** , 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。

 

 **注意：** 两结点之间的路径长度是以它们之间边的数目表示。

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 544.输出比赛匹配对
[https://leetcode-cn.com/problems/output-contest-matches](https://leetcode-cn.com/problems/output-contest-matches) 
## 原题

 
**标签**
`递归` `字符串` `模拟` 


## 
```python

```
>
# 545.二叉树的边界
[https://leetcode-cn.com/problems/boundary-of-binary-tree](https://leetcode-cn.com/problems/boundary-of-binary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 546.移除盒子
[https://leetcode-cn.com/problems/remove-boxes](https://leetcode-cn.com/problems/remove-boxes) 
## 原题
给出一些不同颜色的盒子<meta charset="UTF-8" /> `boxes` ，盒子的颜色由不同的正数表示。

你将经过若干轮操作去去掉盒子，直到所有的盒子都去掉为止。每一轮你可以移除具有相同颜色的连续 `k` 个盒子（ `k >= 1` ），这样一轮之后你将得到 `k * k` 个积分。

返回 *你能获得的最大积分和* 。

 

 **示例 1：** 

```

输入：boxes = [1,3,2,2,2,3,4,3,1]
输出：23
解释：
[1, 3, 2, 2, 2, 3, 4, 3, 1] 
----> [1, 3, 3, 4, 3, 1] (3*3=9 分) 
----> [1, 3, 3, 3, 1] (1*1=1 分) 
----> [1, 1] (3*3=9 分) 
----> [] (2*2=4 分)

```
 **示例 2：** 

```

输入：boxes = [1,1,1]
输出：9

```
 **示例 3：** 

```

输入：boxes = [1]
输出：1

```
 

 **提示：** 
-  `1 <= boxes.length <= 100` 
-  `1 <= boxes[i] <= 100` 
 
**标签**
`记忆化搜索` `数组` `动态规划` 


## 
```python

```
>
# 547.省份数量
[https://leetcode-cn.com/problems/number-of-provinces](https://leetcode-cn.com/problems/number-of-provinces) 
## 原题


有 `n` 个城市，其中一些彼此相连，另一些没有相连。如果城市 `a` 与城市 `b` 直接相连，且城市 `b` 与城市 `c` 直接相连，那么城市 `a` 与城市 `c` 间接相连。

 **省份** 是一组直接或间接相连的城市，组内不含其他没有相连的城市。

给你一个 `n x n` 的矩阵 `isConnected` ，其中 `isConnected[i][j] = 1` 表示第 `i` 个城市和第 `j` 个城市直接相连，而 `isConnected[i][j] = 0` 表示二者不直接相连。

返回矩阵中 **省份** 的数量。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg" style="width: 222px; height: 142px;" />
```

输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/graph2.jpg" style="width: 222px; height: 142px;" />
```

输入：isConnected = [[1,0,0],[0,1,0],[0,0,1]]
输出：3

```
 

 **提示：** 
-  `1 <= n <= 200` 
-  `n == isConnected.length` 
-  `n == isConnected[i].length` 
-  `isConnected[i][j]` 为 `1` 或 `0` 
-  `isConnected[i][i] == 1` 
-  `isConnected[i][j] == isConnected[j][i]` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `图` 


## 
```python

```
>
# 548.将数组分割成和相等的子数组
[https://leetcode-cn.com/problems/split-array-with-equal-sum](https://leetcode-cn.com/problems/split-array-with-equal-sum) 
## 原题

 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 549.二叉树中最长的连续序列
[https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence-ii](https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence-ii) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 550.游戏玩法分析 IV
[https://leetcode-cn.com/problems/game-play-analysis-iv](https://leetcode-cn.com/problems/game-play-analysis-iv) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 551.学生出勤记录 I
[https://leetcode-cn.com/problems/student-attendance-record-i](https://leetcode-cn.com/problems/student-attendance-record-i) 
## 原题
给你一个字符串 `s` 表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：
-  `'A'` ：Absent，缺勤
-  `'L'` ：Late，迟到
-  `'P'` ：Present，到场
如果学生能够 **同时** 满足下面两个条件，则可以获得出勤奖励：
- 按 **总出勤** 计，学生缺勤（ `'A'` ） **严格** 少于两天。
- 学生 **不会** 存在 **连续** 3 天或 **连续** 3 天以上的迟到（ `'L'` ）记录。
如果学生可以获得出勤奖励，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：s = "PPALLP"
输出：true
解释：学生缺勤次数少于 2 次，且不存在 3 天或以上的连续迟到记录。

```
 **示例 2：** 

```

输入：s = "PPALLL"
输出：false
解释：学生最后三天连续迟到，所以不满足出勤奖励的条件。

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s[i]` 为 `'A'` 、 `'L'` 或 `'P'` 
 
**标签**
`字符串` 


## 
```python

```
>
# 552.学生出勤记录 II
[https://leetcode-cn.com/problems/student-attendance-record-ii](https://leetcode-cn.com/problems/student-attendance-record-ii) 
## 原题
可以用字符串表示一个学生的出勤记录，其中的每个字符用来标记当天的出勤情况（缺勤、迟到、到场）。记录中只含下面三种字符：

-  `'A'` ：Absent，缺勤
-  `'L'` ：Late，迟到
-  `'P'` ：Present，到场
如果学生能够 **同时** 满足下面两个条件，则可以获得出勤奖励：
- 按 **总出勤** 计，学生缺勤（ `'A'` ） **严格** 少于两天。
- 学生 **不会** 存在 **连续** 3 天或 **连续** 3 天以上的迟到（ `'L'` ）记录。
给你一个整数 `n` ，表示出勤记录的长度（次数）。请你返回记录长度为 `n` 时，可能获得出勤奖励的记录情况 **数量** 。答案可能很大，所以返回对 `10^9 + 7` **取余** 的结果。

 

 **示例 1：** 

```

输入：n = 2
输出：8
解释：
有 8 种长度为 2 的记录将被视为可奖励：
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL" 
只有"AA"不会被视为可奖励，因为缺勤次数为 2 次（需要少于 2 次）。

```
 **示例 2：** 

```

输入：n = 1
输出：3

```
 **示例 3：** 

```

输入：n = 10101
输出：183236316

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 553.最优除法
[https://leetcode-cn.com/problems/optimal-division](https://leetcode-cn.com/problems/optimal-division) 
## 原题
给定一组 **正整数，** 相邻的整数之间将会进行浮点除法操作。例如， [2,3,4] -> 2 / 3 / 4 。

但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，才能得到 **最大的** 结果，并且返回相应的字符串格式的表达式。 **你的表达式不应该含有冗余的括号。** 

 **示例：** 

```

输入: [1000,100,10,2]
输出: "1000/(100/10/2)"
解释:
1000/(100/10/2) = 1000/((100/10)/2) = 200
但是，以下加粗的括号 "1000/((100/10)/2)" 是冗余的，
因为他们并不影响操作的优先级，所以你需要返回 "1000/(100/10/2)"。

其他用例:
1000/(100/10)/2 = 50
1000/(100/(10/2)) = 50
1000/100/10/2 = 0.5
1000/100/(10/2) = 2

```
 **说明:** 
- 输入数组的长度在 [1, 10] 之间。
- 数组中每个元素的大小都在 [2, 1000] 之间。
- 每个测试用例只有一个最优除法解。
 
**标签**
`数组` `数学` `动态规划` 


## 
```python

```
>
# 554.砖墙
[https://leetcode-cn.com/problems/brick-wall](https://leetcode-cn.com/problems/brick-wall) 
## 原题
你的面前有一堵矩形的、由 `n` 行砖块组成的砖墙。这些砖块高度相同（也就是一个单位高）但是宽度不同。每一行砖块的宽度之和相等。

你现在要画一条 **自顶向下** 的、穿过 **最少** 砖块的垂线。如果你画的线只是从砖块的边缘经过，就不算穿过这块砖。 **你不能沿着墙的两个垂直边缘之一画线，这样显然是没有穿过一块砖的。** 

给你一个二维数组 `wall` ，该数组包含这堵墙的相关信息。其中， `wall[i]` 是一个代表从左至右每块砖的宽度的数组。你需要找出怎样画才能使这条线 **穿过的砖块数量最少** ，并且返回 **穿过的砖块数量** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/cutwall-grid.jpg" style="width: 493px; height: 577px;" />
```

输入：wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]]
输出：2

```
 **示例 2：** 

```

输入：wall = [[1],[1],[1]]
输出：3

```

 

 **提示：** 
-  `n == wall.length` 
-  `1 <= n <= 10^4` 
-  `1 <= wall[i].length <= 10^4` 
-  `1 <= sum(wall[i].length) <= 2 * 10^4` 
- 对于每一行 `i` ， `sum(wall[i])` 是相同的
-  `1 <= wall[i][j] <= 2^31 - 1` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 555.分割连接字符串
[https://leetcode-cn.com/problems/split-concatenated-strings](https://leetcode-cn.com/problems/split-concatenated-strings) 
## 原题

 
**标签**
`贪心` `数组` `字符串` 


## 
```python

```
>
# 556.下一个更大元素 III
[https://leetcode-cn.com/problems/next-greater-element-iii](https://leetcode-cn.com/problems/next-greater-element-iii) 
## 原题
给你一个正整数  `n` ，请你找出符合条件的最小整数，其由重新排列 `n` ** ** 中存在的每位数字组成，并且其值大于 `n` 。如果不存在这样的正整数，则返回 `-1` 。

 **注意** ，返回的整数应当是一个 **32 位整数** ，如果存在满足题意的答案，但不是 **32 位整数** ，同样返回 `-1` 。

 

 **示例 1：** 

```

输入：n = 12
输出：21

```
 **示例 2：** 

```

输入：n = 21
输出：-1

```
 

 **提示：** 
-  `1 <= n <= 2^31 - 1` 
 
**标签**
`数学` `双指针` `字符串` 


## 
```python

```
>
# 557.反转字符串中的单词 III
[https://leetcode-cn.com/problems/reverse-words-in-a-string-iii](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii) 
## 原题
给定一个字符串<meta charset="UTF-8" /> `s` ，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

 

 **示例 1：** 

```

输入：s = "Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"

```
 **示例 2:** 

```

输入： s = "God Ding"
输出："doG gniD"

```
 

 ** ** ** **提示：** ** ** ** 
-  `1 <= s.length <= 5 * 10^4` 
- <meta charset="UTF-8" /> `s` 包含可打印的 **ASCII** 字符。
- <meta charset="UTF-8" /> `s` 不包含任何开头或结尾空格。
- <meta charset="UTF-8" /> `s` 里 **至少** 有一个词。
- <meta charset="UTF-8" /> `s` 中的所有单词都用一个空格隔开。
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 558.四叉树交集
[https://leetcode-cn.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees](https://leetcode-cn.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees) 
## 原题
二进制矩阵中的所有元素不是 **0** 就是 **1** 。

给你两个四叉树， `quadTree1` 和 `quadTree2` 。其中 `quadTree1` 表示一个 `n * n` 二进制矩阵，而 `quadTree2` 表示另一个 `n * n` 二进制矩阵。

请你返回一个表示 `n * n` 二进制矩阵的四叉树，它是 `quadTree1` 和 `quadTree2` 所表示的两个二进制矩阵进行 **按位逻辑或运算** 的结果。

注意，当 `isLeaf` 为 **False** 时，你可以把 **True** 或者 **False** 赋值给节点，两种值都会被判题机制 **接受** 。

四叉树数据结构中，每个内部节点只有四个子节点。此外，每个节点都有两个属性：
-  `val` ：储存叶子结点所代表的区域的值。1 对应 **True** ，0 对应 **False** ；
-  `isLeaf` : 当这个节点是一个叶子结点时为 **True** ，如果它有 4 个子节点则为 **False** 。
```

class Node {
    public boolean val;
    public boolean isLeaf;
    public Node topLeft;
    public Node topRight;
    public Node bottomLeft;
    public Node bottomRight;
}
```
我们可以按以下步骤为二维区域构建四叉树：
- 如果当前网格的值相同（即，全为 `0` 或者全为 `1` ），将 `isLeaf` 设为 True ，将 `val` 设为网格相应的值，并将四个子节点都设为 Null 然后停止。
- 如果当前网格的值不同，将 `isLeaf` 设为 False， 将 `val` 设为任意值，然后如下图所示，将当前网格划分为四个子网格。
- 使用适当的子网格递归每个子节点。
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/new_top.png" style="height: 181px; width: 777px;" />

如果你想了解更多关于四叉树的内容，可以参考 <a href="https://en.wikipedia.org/wiki/Quadtree">wiki</a> 。

 **四叉树格式：** 

输出为使用层序遍历后四叉树的序列化形式，其中 `null` 表示路径终止符，其下面不存在节点。

它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 `[isLeaf, val]` 。

如果 `isLeaf` 或者 `val` 的值为 True ，则表示它在列表  `[isLeaf, val]` 中的值为 **1** ；如果 `isLeaf` 或者 `val` 的值为 False ，则表示值为 **0** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/qt1.png" style="height: 196px; width: 550px;" /> <img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/qt2.png" style="height: 278px; width: 550px;" />

```

输入：quadTree1 = [[0,1],[1,1],[1,1],[1,0],[1,0]]
, quadTree2 = [[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
输出：[[0,0],[1,1],[1,1],[1,1],[1,0]]
解释：quadTree1 和 quadTree2 如上所示。由四叉树所表示的二进制矩阵也已经给出。
如果我们对这两个矩阵进行按位逻辑或运算，则可以得到下面的二进制矩阵，由一个作为结果的四叉树表示。
注意，我们展示的二进制矩阵仅仅是为了更好地说明题意，你无需构造二进制矩阵来获得结果四叉树。
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/qtr.png" style="height: 222px; width: 777px;" />

```
 **示例 2：** 

```

输入：quadTree1 = [[1,0]]
, quadTree2 = [[1,0]]
输出：[[1,0]]
解释：两个数所表示的矩阵大小都为 1*1，值全为 0 
结果矩阵大小为 1*1，值全为 0 。

```
 **示例 3：** 

```

输入：quadTree1 = [[0,0],[1,0],[1,0],[1,1],[1,1]]
, quadTree2 = [[0,0],[1,1],[1,1],[1,0],[1,1]]
输出：[[1,1]]

```
 **示例 4：** 

```

输入：quadTree1 = [[0,0],[1,1],[1,0],[1,1],[1,1]]
, quadTree2 = [[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[1,1]]
输出：[[0,0],[1,1],[0,1],[1,1],[1,1],null,null,null,null,[1,1],[1,0],[1,0],[1,1]]

```
 **示例 5：** 

```

输入：quadTree1 = [[0,1],[1,0],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
, quadTree2 = [[0,1],[0,1],[1,0],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1]]
输出：[[0,0],[0,1],[0,1],[1,1],[1,0],[1,0],[1,0],[1,1],[1,1],[1,0],[1,0],[1,1],[1,1]]

```
 

 **提示：** 
-  `quadTree1` 和 `quadTree2` 都是符合题目要求的四叉树，每个都代表一个 `n * n` 的矩阵。
-  `n == 2^x` ，其中 `0 <= x <= 9` .
 
**标签**
`树` `分治` 


## 
```python

```
>
# 559.N 叉树的最大深度
[https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree](https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree) 
## 原题
给定一个 N 叉树，找到其最大深度。

<p class="MachineTrans-lang-zh-CN">最大深度是指从根节点到最远叶子节点的最长路径上的节点总数。

<p class="MachineTrans-lang-zh-CN">N 叉树输入按层序遍历序列化表示，每组子节点由空值分隔（请参见示例）。

<p class="MachineTrans-lang-zh-CN"> 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" />

```

输入：root = [1,null,3,2,4,null,5,6]
输出：3

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 296px; height: 241px;" />

```

输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：5

```
 

 **提示：** 
- 树的深度不会超过  `1000` 。
- 树的节点数目位于 `[0, 10^4]` 之间。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` 


## 
```python

```
>
# 560.和为 K 的子数组
[https://leetcode-cn.com/problems/subarray-sum-equals-k](https://leetcode-cn.com/problems/subarray-sum-equals-k) 
## 原题
给你一个整数数组 `nums` 和一个整数 `k` ，请你统计并返回该数组中和为 `k` **** 的连续子数组的个数。

 

 **示例 1：** 

```

输入：nums = [1,1,1], k = 2
输出：2

```
 **示例 2：** 

```

输入：nums = [1,2,3], k = 3
输出：2

```
 

 **提示：** 
-  `1 <= nums.length <= 2 * 10^4` 
-  `-1000 <= nums[i] <= 1000` 
-  `-10^7 <= k <= 10^7` 
 
**标签**
`数组` `哈希表` `前缀和` 


## 
```python

```
>
# 561.数组拆分 I
[https://leetcode-cn.com/problems/array-partition-i](https://leetcode-cn.com/problems/array-partition-i) 
## 原题
给定长度为  `2n` ** ** 的整数数组 `nums` ，你的任务是将这些数分成  `n` **** 对, 例如 `(a<sub>1</sub>, b<sub>1</sub>), (a<sub>2</sub>, b<sub>2</sub>), ..., (a<sub>n</sub>, b<sub>n</sub>)` ，使得从 `1` 到  `n` 的 `min(a<sub>i</sub>, b<sub>i</sub>)` 总和最大。

返回该 **最大总和** 。

 

 **示例 1：** 

```

输入：nums = [1,4,3,2]
输出：4
解释：所有可能的分法（忽略元素顺序）为：
1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
所以最大总和为 4
```
 **示例 2：** 

```

输入：nums = [6,2,6,5,1,2]
输出：9
解释：最优的分法为 (2, 1), (2, 5), (6, 6). min(2, 1) + min(2, 5) + min(6, 6) = 1 + 2 + 6 = 9

```
 

 **提示：** 
-  `1 <= n <= 10^4` 
-  `nums.length == 2 * n` 
-  `-10^4 <= nums[i] <= 10^4` 
 
**标签**
`贪心` `数组` `计数排序` `排序` 


## 
```python

```
>
# 562.矩阵中最长的连续1线段
[https://leetcode-cn.com/problems/longest-line-of-consecutive-one-in-matrix](https://leetcode-cn.com/problems/longest-line-of-consecutive-one-in-matrix) 
## 原题

 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 563.二叉树的坡度
[https://leetcode-cn.com/problems/binary-tree-tilt](https://leetcode-cn.com/problems/binary-tree-tilt) 
## 原题
给你一个二叉树的根节点 `root` ，计算并返回 **整个树** 的坡度 。

一个树的 **节点的坡度** 定义即为，该节点左子树的节点之和和右子树节点之和的 **差的绝对值** 。如果没有左子树的话，左子树的节点之和为 0 ；没有右子树的话也是一样。空结点的坡度是 0 。

 **整个树** 的坡度就是其所有节点的坡度之和。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/20/tilt1.jpg" style="width: 712px; height: 182px;" />
```

输入：root = [1,2,3]
输出：1
解释：
节点 2 的坡度：|0-0| = 0（没有子节点）
节点 3 的坡度：|0-0| = 0（没有子节点）
节点 1 的坡度：|2-3| = 1（左子树就是左子节点，所以和是 2 ；右子树就是右子节点，所以和是 3 ）
坡度总和：0 + 0 + 1 = 1

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/20/tilt2.jpg" style="width: 800px; height: 203px;" />
```

输入：root = [4,2,9,3,5,null,7]
输出：15
解释：
节点 3 的坡度：|0-0| = 0（没有子节点）
节点 5 的坡度：|0-0| = 0（没有子节点）
节点 7 的坡度：|0-0| = 0（没有子节点）
节点 2 的坡度：|3-5| = 2（左子树就是左子节点，所以和是 3 ；右子树就是右子节点，所以和是 5 ）
节点 9 的坡度：|0-7| = 7（没有左子树，所以和是 0 ；右子树正好是右子节点，所以和是 7 ）
节点 4 的坡度：|(3+5+2)-(9+7)| = |10-16| = 6（左子树值为 3、5 和 2 ，和是 10 ；右子树值为 9 和 7 ，和是 16 ）
坡度总和：0 + 0 + 0 + 2 + 7 + 6 = 15

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/20/tilt3.jpg" style="width: 800px; height: 293px;" />
```

输入：root = [21,7,14,1,1,2,2,3,3]
输出：9

```
 

 **提示：** 
- 树中节点数目的范围在 `[0, 10^4]` 内
-  `-1000 <= Node.val <= 1000` 
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 564.寻找最近的回文数
[https://leetcode-cn.com/problems/find-the-closest-palindrome](https://leetcode-cn.com/problems/find-the-closest-palindrome) 
## 原题
给定一个表示整数的字符串 `n` ，返回与它最近的回文整数（不包括自身）。如果不止一个，退回小的那个。

“最近的”定义为两个整数 **差的绝对值** 最小。

 

 **示例 1:** 

```

输入: n = "123"
输出: "121"

```
 **示例 2:** 

```

输入: n = "1"
输出: "0"
解释: 0 和 2是最近的回文，但我们返回最小的，也就是 0。

```
 

 **提示:** 
-  `1 <= n.length <= 18` 
-  `n` 只由数字组成
-  `n` 不含前导 0
-  `n` 代表在 `[1, 10^18 - 1]` 范围内的整数
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 565.数组嵌套
[https://leetcode-cn.com/problems/array-nesting](https://leetcode-cn.com/problems/array-nesting) 
## 原题
索引从 `0` 开始长度为 `N` 的数组 `A` ，包含 `0` 到 `N - 1` 的所有整数。找到最大的集合 `S` 并返回其大小，其中 `S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }` 且遵守以下的规则。

假设选择索引为 `i` 的元素 `A[i]` 为 `S` 的第一个元素， `S` 的下一个元素应该是 `A[A[i]]` ，之后是 `A[A[A[i]]]...` 以此类推，不断添加直到 `S` 出现重复的元素。

 

 **示例 1:** 

```
输入: A = [5,4,0,3,1,6,2]
输出: 4
解释: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}

```
 

 **提示：** 
-  `N` 是 `[1, 20,000]` 之间的整数。
-  `A` 中不含有重复的元素。
-  `A` 中的元素大小在 `[0, N-1]` 之间。
 
**标签**
`深度优先搜索` `数组` 


## 
```python

```
>
# 566.重塑矩阵
[https://leetcode-cn.com/problems/reshape-the-matrix](https://leetcode-cn.com/problems/reshape-the-matrix) 
## 原题
在 MATLAB 中，有一个非常有用的函数 `reshape` ，它可以将一个 `m x n` 矩阵重塑为另一个大小不同（ `r x c` ）的新矩阵，但保留其原始数据。

给你一个由二维数组 `mat` 表示的 `m x n` 矩阵，以及两个正整数 `r` 和 `c` ，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的 **行遍历顺序** 填充。

如果具有给定参数的 `reshape` 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/reshape1-grid.jpg" style="width: 613px; height: 173px;" />
```

输入：mat = [[1,2],[3,4]], r = 1, c = 4
输出：[[1,2,3,4]]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/24/reshape2-grid.jpg" style="width: 453px; height: 173px;" />
```

输入：mat = [[1,2],[3,4]], r = 2, c = 4
输出：[[1,2],[3,4]]

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat[i].length` 
-  `1 <= m, n <= 100` 
-  `-1000 <= mat[i][j] <= 1000` 
-  `1 <= r, c <= 300` 
 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 567.字符串的排列
[https://leetcode-cn.com/problems/permutation-in-string](https://leetcode-cn.com/problems/permutation-in-string) 
## 原题
给你两个字符串 `s1` 和 `s2` ，写一个函数来判断 `s2` 是否包含 `s1` **** 的排列。如果是，返回 `true` ；否则，返回 `false` 。

换句话说， `s1` 的排列之一是 `s2` 的 **子串** 。

 

 **示例 1：** 

```

输入：s1 = "ab" s2 = "eidbaooo"
输出：true
解释：s2 包含 s1 的排列之一 ("ba").

```
 **示例 2：** 

```

输入：s1= "ab" s2 = "eidboaoo"
输出：false

```
 

 **提示：** 
-  `1 <= s1.length, s2.length <= 10^4` 
-  `s1` 和 `s2` 仅包含小写字母
 
**标签**
`哈希表` `双指针` `字符串` `滑动窗口` 


## 
```python

```
>
# 568.最大休假天数
[https://leetcode-cn.com/problems/maximum-vacation-days](https://leetcode-cn.com/problems/maximum-vacation-days) 
## 原题

 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 569.员工薪水中位数
[https://leetcode-cn.com/problems/median-employee-salary](https://leetcode-cn.com/problems/median-employee-salary) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 570.至少有5名直接下属的经理
[https://leetcode-cn.com/problems/managers-with-at-least-5-direct-reports](https://leetcode-cn.com/problems/managers-with-at-least-5-direct-reports) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 571.给定数字的频率查询中位数
[https://leetcode-cn.com/problems/find-median-given-frequency-of-numbers](https://leetcode-cn.com/problems/find-median-given-frequency-of-numbers) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 572.另一棵树的子树
[https://leetcode-cn.com/problems/subtree-of-another-tree](https://leetcode-cn.com/problems/subtree-of-another-tree) 
## 原题


给你两棵二叉树 `root` 和 `subRoot` 。检验 `root` 中是否包含和 `subRoot` 具有相同结构和节点值的子树。如果存在，返回 `true` ；否则，返回 `false` 。

二叉树 `tree` 的一棵子树包括 `tree` 的某个节点和这个节点的所有后代节点。 `tree` 也可以看做它自身的一棵子树。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree1-tree.jpg" style="width: 532px; height: 400px;" />
```

输入：root = [3,4,5,1,2], subRoot = [4,1,2]
输出：true

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/subtree2-tree.jpg" style="width: 502px; height: 458px;" />
```

输入：root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
输出：false

```
 

 **提示：** 
-  `root` 树上的节点数量范围是 `[1, 2000]` 
-  `subRoot` 树上的节点数量范围是 `[1, 1000]` 
-  `-10^4 <= root.val <= 10^4` 
-  `-10^4 <= subRoot.val <= 10^4` 
 
**标签**
`树` `深度优先搜索` `二叉树` `字符串匹配` `哈希函数` 


## 
```python

```
>
# 573.松鼠模拟
[https://leetcode-cn.com/problems/squirrel-simulation](https://leetcode-cn.com/problems/squirrel-simulation) 
## 原题

 
**标签**
`数组` `数学` 


## 
```python

```
>
# 574.当选者
[https://leetcode-cn.com/problems/winning-candidate](https://leetcode-cn.com/problems/winning-candidate) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 575.分糖果
[https://leetcode-cn.com/problems/distribute-candies](https://leetcode-cn.com/problems/distribute-candies) 
## 原题
Alice 有 `n` 枚糖，其中第 `i` 枚糖的类型为 `candyType[i]` 。Alice 注意到她的体重正在增长，所以前去拜访了一位医生。

医生建议 Alice 要少摄入糖分，只吃掉她所有糖的 `n / 2` 即可（ `n` 是一个偶数）。Alice 非常喜欢这些糖，她想要在遵循医生建议的情况下，尽可能吃到最多不同种类的糖。

给你一个长度为 `n` 的整数数组 `candyType` ，返回： Alice *在仅吃掉 `n / 2` 枚糖的情况下，可以吃到糖的 **最多** 种类数* 。

 

 **示例 1：** 

```

输入：candyType = [1,1,2,2,3,3]
输出：3
解释：Alice 只能吃 6 / 2 = 3 枚糖，由于只有 3 种糖，她可以每种吃一枚。

```
 **示例 2：** 

```

输入：candyType = [1,1,2,3]
输出：2
解释：Alice 只能吃 4 / 2 = 2 枚糖，不管她选择吃的种类是 [1,2]、[1,3] 还是 [2,3]，她只能吃到两种不同类的糖。

```
 **示例 3：** 

```

输入：candyType = [6,6,6,6]
输出：1
解释：Alice 只能吃 4 / 2 = 2 枚糖，尽管她能吃 2 枚，但只能吃到 1 种糖。

```
 

 **提示：** 
-  `n == candyType.length` 
-  `2 <= n <= 10^4` 
-  `n` 是一个偶数
-  `-10^5 <= candyType[i] <= 10^5` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 576.出界的路径数
[https://leetcode-cn.com/problems/out-of-boundary-paths](https://leetcode-cn.com/problems/out-of-boundary-paths) 
## 原题
给你一个大小为 `m x n` 的网格和一个球。球的起始坐标为 `[startRow, startColumn]` 。你可以将球移到在四个方向上相邻的单元格内（可以穿过网格边界到达网格之外）。你 **最多** 可以移动 `maxMove` 次球。

给你五个整数 `m` 、 `n` 、 `maxMove` 、 `startRow` 以及 `startColumn` ，找出并返回可以将球移出边界的路径数量。因为答案可能非常大，返回对 `10^9 + 7` **取余** 后的结果。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_1.png" style="width: 500px; height: 296px;" />
```

输入：m = 2, n = 2, maxMove = 2, startRow = 0, startColumn = 0
输出：6

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/28/out_of_boundary_paths_2.png" style="width: 500px; height: 293px;" />
```

输入：m = 1, n = 3, maxMove = 3, startRow = 0, startColumn = 1
输出：12

```
 

 **提示：** 
-  `1 <= m, n <= 50` 
-  `0 <= maxMove <= 50` 
-  `0 <= startRow < m` 
-  `0 <= startColumn < n` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 577.员工奖金
[https://leetcode-cn.com/problems/employee-bonus](https://leetcode-cn.com/problems/employee-bonus) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 578.查询回答率最高的问题
[https://leetcode-cn.com/problems/get-highest-answer-rate-question](https://leetcode-cn.com/problems/get-highest-answer-rate-question) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 579.查询员工的累计薪水
[https://leetcode-cn.com/problems/find-cumulative-salary-of-an-employee](https://leetcode-cn.com/problems/find-cumulative-salary-of-an-employee) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 580.统计各专业学生人数
[https://leetcode-cn.com/problems/count-student-number-in-departments](https://leetcode-cn.com/problems/count-student-number-in-departments) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 581.最短无序连续子数组
[https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray) 
## 原题
给你一个整数数组 `nums` ，你需要找出一个 **连续子数组** ，如果对这个子数组进行升序排序，那么整个数组都会变为升序排序。

请你找出符合题意的 **最短** 子数组，并输出它的长度。

 
 **示例 1：** 

```

输入：nums = [2,6,4,8,10,9,15]
输出：5
解释：你只需要对 [6, 4, 8, 10, 9] 进行升序排序，那么整个表都会变为升序排序。

```
 **示例 2：** 

```

输入：nums = [1,2,3,4]
输出：0

```
 **示例 3：** 

```

输入：nums = [1]
输出：0

```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `-10^5 <= nums[i] <= 10^5` 
 

 **进阶：** 你可以设计一个时间复杂度为 `O(n)` 的解决方案吗？
 
**标签**
`栈` `贪心` `数组` `双指针` `排序` `单调栈` 


## 
```python

```
>
# 582.杀掉进程
[https://leetcode-cn.com/problems/kill-process](https://leetcode-cn.com/problems/kill-process) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `数组` `哈希表` 


## 
```python

```
>
# 583.两个字符串的删除操作
[https://leetcode-cn.com/problems/delete-operation-for-two-strings](https://leetcode-cn.com/problems/delete-operation-for-two-strings) 
## 原题
给定两个单词 `word1` 和<meta charset="UTF-8" /> `word2` ，返回使得<meta charset="UTF-8" /> `word1` 和 <meta charset="UTF-8" /> `word2`  **相同** 所需的 **最小步数** 。

 **每步** 可以删除任意一个字符串中的一个字符。

 

 **示例 1：** 

```

输入: word1 = "sea", word2 = "eat"
输出: 2
解释: 第一步将 "sea" 变为 "ea" ，第二步将 "eat "变为 "ea"

```
 **示例  2:** 

```

输入：word1 = "leetcode", word2 = "etco"
输出：4

```
 

 **提示：** 
<meta charset="UTF-8" />
-  `1 <= word1.length, word2.length <= 500` 
-  `word1` 和 `word2` 只包含小写英文字母
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 584.寻找用户推荐人
[https://leetcode-cn.com/problems/find-customer-referee](https://leetcode-cn.com/problems/find-customer-referee) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 585.2016年的投资
[https://leetcode-cn.com/problems/investments-in-2016](https://leetcode-cn.com/problems/investments-in-2016) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 586.订单最多的客户
[https://leetcode-cn.com/problems/customer-placing-the-largest-number-of-orders](https://leetcode-cn.com/problems/customer-placing-the-largest-number-of-orders) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 587.安装栅栏
[https://leetcode-cn.com/problems/erect-the-fence](https://leetcode-cn.com/problems/erect-the-fence) 
## 原题
在一个二维的花园中，有一些用 (x, y) 坐标表示的树。由于安装费用十分昂贵，你的任务是先用 **最短** 的绳子围起所有的树。只有当所有的树都被绳子包围时，花园才能围好栅栏。你需要找到正好位于栅栏边界上的树的坐标。

 

 **示例 1:** 

```
输入: [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
输出: [[1,1],[2,0],[4,2],[3,3],[2,4]]
解释:
<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/erect_the_fence_1.png" style="width: 100%; max-width: 320px">

```


 **示例 2:** 

```
输入: [[1,2],[2,2],[4,2]]
输出: [[1,2],[2,2],[4,2]]
解释:
<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/erect_the_fence_2.png" style="width: 100%; max-width: 320px">
即使树都在一条直线上，你也需要先用绳子包围它们。

```


 

 **注意:** 


- 所有的树应当被围在一起。你不能剪断绳子来包围树或者把树分成一组以上。
- 输入的整数在 0 到 100 之间。
- 花园至少有一棵树。
- 所有树的坐标都是不同的。
- 输入的点 **没有** 顺序。输出顺序也没有要求。

 
**标签**
`几何` `数组` `数学` 


## 
```python

```
>
# 588.设计内存文件系统
[https://leetcode-cn.com/problems/design-in-memory-file-system](https://leetcode-cn.com/problems/design-in-memory-file-system) 
## 原题

 
**标签**
`设计` `字典树` `哈希表` `字符串` 


## 
```python

```
>
# 589.N 叉树的前序遍历
[https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal](https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal) 
## 原题
给定一个 n 叉树的根节点 <meta charset="UTF-8" /> `root` ，返回 *其节点值的 **前序遍历*** 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 `null` 分隔（请参见示例）。

<br />
 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="height: 193px; width: 300px;" />

```

输入：root = [1,null,3,2,4,null,5,6]
输出：[1,3,5,6,2,4]

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="height: 272px; width: 300px;" />

```

输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[1,2,3,6,7,11,14,4,8,12,5,9,13,10]

```
 

 **提示：** 
- 节点总数在范围<meta charset="UTF-8" /> `[0, 10^4]` 内
-  `0 <= Node.val <= 10^4` 
- n 叉树的高度小于或等于 `1000` 
 

 **进阶：** 递归法很简单，你可以使用迭代法完成此题吗?

 
**标签**
`栈` `树` `深度优先搜索` 


## 
```python

```
>
# 590.N 叉树的后序遍历
[https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal) 
## 原题
给定一个 n 叉树的根节点<meta charset="UTF-8" /> `root` ，返回 *其节点值的 **后序遍历*** 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 `null` 分隔（请参见示例）。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="height: 193px; width: 300px;" />

```

输入：root = [1,null,3,2,4,null,5,6]
输出：[5,6,3,2,4,1]

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="height: 269px; width: 296px;" />

```

输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[2,6,14,11,7,3,12,8,4,13,9,10,5,1]

```
 

 **提示：** 
- 节点总数在范围 `[0, 10^4]` 内
-  `0 <= Node.val <= 10^4` 
- n 叉树的高度小于或等于 `1000` 
 

 **进阶：** 递归法很简单，你可以使用迭代法完成此题吗?

 
**标签**
`栈` `树` `深度优先搜索` 


## 
```python

```
>
# 591.标签验证器
[https://leetcode-cn.com/problems/tag-validator](https://leetcode-cn.com/problems/tag-validator) 
## 原题
给定一个表示代码片段的字符串，你需要实现一个验证器来解析这段代码，并返回它是否合法。合法的代码片段需要遵守以下的所有规则：
- 代码必须被 **合法的闭合标签** 包围。否则，代码是无效的。
-  **闭合标签** （不一定合法）要严格符合格式： `<TAG_NAME>TAG_CONTENT</TAG_NAME>` 。其中， `<TAG_NAME>` 是起始标签， `</TAG_NAME>` 是结束标签。起始和结束标签中的 TAG_NAME 应当相同。当且仅当 TAG_NAME 和 TAG_CONTENT 都是合法的，闭合标签才是 **合法的** 。
-  **合法的** `TAG_NAME` 仅含有 **大写字母** ，长度在范围 [1,9] 之间。否则，该 `TAG_NAME` 是 **不合法的** 。
-  **合法的** `TAG_CONTENT` 可以包含其他 **合法的闭合标签** ， **cdata** （请参考规则7）和任意字符（注意参考规则1） **除了** 不匹配的 `<` 、不匹配的起始和结束标签、不匹配的或带有不合法 TAG_NAME 的闭合标签。否则， `TAG_CONTENT` 是 **不合法的** 。
- 一个起始标签，如果没有具有相同 TAG_NAME 的结束标签与之匹配，是不合法的。反之亦然。不过，你也需要考虑标签嵌套的问题。
- 一个 `<` ，如果你找不到一个后续的 `>` 与之匹配，是不合法的。并且当你找到一个 `<` 或 `</` 时，所有直到下一个 `>` 的前的字符，都应当被解析为 TAG_NAME（不一定合法）。
- cdata 有如下格式： `<![CDATA[CDATA_CONTENT]]>` 。 `CDATA_CONTENT` 的范围被定义成 `<![CDATA[` 和 **后续的第一个** `]]>` 之间的字符。
-  `CDATA_CONTENT` 可以包含 **任意字符** 。cdata 的功能是阻止验证器解析 `CDATA_CONTENT` ，所以即使其中有一些字符可以被解析为标签（无论合法还是不合法），也应该将它们视为 **常规字符** 。
 **合法代码的例子:** 

```

输入: "<DIV>This is the first line <![CDATA[]]></DIV>"

输出: True

解释: 

代码被包含在了闭合的标签内： <DIV> 和 </DIV> 。

TAG_NAME 是合法的，TAG_CONTENT 包含了一些字符和 cdata 。 

即使 CDATA_CONTENT 含有不匹配的起始标签和不合法的 TAG_NAME，它应该被视为普通的文本，而不是标签。

所以 TAG_CONTENT 是合法的，因此代码是合法的。最终返回True。
输入: "<DIV>>>  ![cdata[]] <![CDATA[]>]]>]]>>]</DIV>"

输出: True

解释:

我们首先将代码分割为： start_tag|tag_content|end_tag 。

start_tag -> "<DIV>"

end_tag -> "</DIV>"

tag_content 也可被分割为： text1|cdata|text2 。

text1 -> ">>  ![cdata[]] "

cdata -> "<![CDATA[]>]]>" ，其中 CDATA_CONTENT 为 "]>"

text2 -> "]]>>]"
start_tag 不是 "<DIV>>>" 的原因参照规则 6 。
cdata 不是 "<![CDATA[]>]]>]]>" 的原因参照规则 7 。

```
 **不合法代码的例子:** 

```

输入: "<A>  <B> </A>   </B>"
输出: False
解释: 不合法。如果 "<A>" 是闭合的，那么 "<B>" 一定是不匹配的，反之亦然。

输入: "<DIV>  div tag is not closed  <DIV>"
输出: False

输入: "<DIV>  unmatched <  </DIV>"
输出: False

输入: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
输出: False

输入: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
输出: False

输入: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
输出: False

```
 **注意:** 
- 为简明起见，你可以假设输入的代码（包括提到的 **任意字符** ）只包含 `数字` , <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="background-color:#f9f2f4; font-size:12.6px">字母</span></font>, `';<';` , `';>';` , `';/';` , `';!';` , `';[';` , `';]';` 和 `'; ';` 。
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 592.分数加减运算
[https://leetcode-cn.com/problems/fraction-addition-and-subtraction](https://leetcode-cn.com/problems/fraction-addition-and-subtraction) 
## 原题
给定一个表示分数加减运算的字符串 `expression` ，你需要返回一个字符串形式的计算结果。 

这个结果应该是不可约分的分数，即<a href="https://baike.baidu.com/item/%E6%9C%80%E7%AE%80%E5%88%86%E6%95%B0" target="_blank">最简分数</a>。 如果最终结果是一个整数，例如 `2` ，你需要将它转换成分数形式，其分母为 `1` 。所以在上述例子中, `2` 应该被转换为 `2/1` 。

 

 **示例 1:** 

```

输入: expression = "-1/2+1/2"
输出: "0/1"

```
 **示例 2:** 

```

输入: expression = "-1/2+1/2+1/3"
输出: "1/3"

```
 **示例 3:** 

```

输入: expression = "1/3-1/2"
输出: "-1/6"

```
 

 **提示:** 
- 输入和输出字符串只包含 `'0'` 到 `'9'` 的数字，以及 `'/'` , `'+'` 和 `'-'` 。 
- 输入和输出分数格式均为 `±分子/分母` 。如果输入的第一个分数或者输出的分数是正数，则 `'+'` 会被省略掉。
- 输入只包含合法的 **最简分数** ，每个分数的 **分子** 与 **分母** 的范围是  [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
- 输入的分数个数范围是 [1,10]。
-  **最终结果** 的分子与分母保证是 32 位整数范围内的有效整数。
 
**标签**
`数学` `字符串` `模拟` 


## 
```python

```
>
# 593.有效的正方形
[https://leetcode-cn.com/problems/valid-square](https://leetcode-cn.com/problems/valid-square) 
## 原题
给定2D空间中四个点的坐标 `p1` , `p2` , `p3` 和 `p4` ，如果这四个点构成一个正方形，则返回 `true` 。

点的坐标 `p<sub>i</sub>` 表示为 `[xi, yi]` 。输入 **不是** 按任何顺序给出的。

一个 **有效的正方形** 有四条等边和四个等角(90度角)。

 

 **示例 1:** 

```

输入: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
输出: True

```
 **示例 2:** 

```

输入：p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,12]
输出：false

```
 **示例 3:** 

```

输入：p1 = [1,0], p2 = [-1,0], p3 = [0,1], p4 = [0,-1]
输出：true

```
 

 **提示:** 
-  `p1.length == p2.length == p3.length == p4.length == 2` 
-  `-10^4 <= x<sub>i</sub>, y<sub>i</sub> <= 10^4` 
 
**标签**
`几何` `数学` 


## 
```python

```
>
# 594.最长和谐子序列
[https://leetcode-cn.com/problems/longest-harmonious-subsequence](https://leetcode-cn.com/problems/longest-harmonious-subsequence) 
## 原题
和谐数组是指一个数组里元素的最大值和最小值之间的差别 **正好是 `1` ** 。

现在，给你一个整数数组 `nums` ，请你在所有可能的子序列中找到最长的和谐子序列的长度。

数组的子序列是一个由数组派生出来的序列，它可以通过删除一些元素或不删除元素、且不改变其余元素的顺序而得到。

 

 **示例 1：** 

```

输入：nums = [1,3,2,2,5,2,3,7]
输出：5
解释：最长的和谐子序列是 [3,2,2,2,3]

```
 **示例 2：** 

```

输入：nums = [1,2,3,4]
输出：2

```
 **示例 3：** 

```

输入：nums = [1,1,1,1]
输出：0

```
 

 **提示：** 
-  `1 <= nums.length <= 2 * 10^4` 
-  `-10^9 <= nums[i] <= 10^9` 
 
**标签**
`数组` `哈希表` `排序` 


## 
```python

```
>
# 595.大的国家
[https://leetcode-cn.com/problems/big-countries](https://leetcode-cn.com/problems/big-countries) 
## 原题
 `World` 表：
```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | int     |
+-------------+---------+
name 是这张表的主键。
这张表的每一行提供：国家名称、所属大陆、面积、人口和 GDP 值。

```
 

如果一个国家满足下述两个条件之一，则认为该国是 **大国** ：
- 面积至少为 300 平方公里（即， `3000000 km^2` ），或者
- 人口至少为 2500 万（即 `25000000` ）
编写一个 SQL 查询以报告 **大国** 的国家名称、人口和面积。

按 **任意顺序** 返回结果表。

查询结果格式如下例所示。

 

 **示例：** 

```

输入：
World 表：
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
输出：
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+

```
 
**标签**
`数据库` 


## 
```python

```
>
# 596.超过5名学生的课
[https://leetcode-cn.com/problems/classes-more-than-5-students](https://leetcode-cn.com/problems/classes-more-than-5-students) 
## 原题
表: `Courses` 

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class)是该表的主键列。
该表的每一行表示学生的名字和他们注册的班级。

```
 

编写一个SQL查询来报告 **至少有5个学生** 的所有类。

以 **任意顺序** 返回结果表。

查询结果格式如下所示。

 

 **示例 1:** 

```

输入: 
Courses table:
+---------+----------+
| student | class    |
+---------+----------+
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
+---------+----------+
输出: 
+---------+ 
| class   | 
+---------+ 
| Math    | 
+---------+
解释: 
-数学课有6个学生，所以我们包括它。
-英语课有1名学生，所以我们不包括它。
-生物课有1名学生，所以我们不包括它。
-计算机课有1个学生，所以我们不包括它。
```
 
**标签**
`数据库` 


## 
```python

```
>
# 597.好友申请 I：总体通过率
[https://leetcode-cn.com/problems/friend-requests-i-overall-acceptance-rate](https://leetcode-cn.com/problems/friend-requests-i-overall-acceptance-rate) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 598.范围求和 II
[https://leetcode-cn.com/problems/range-addition-ii](https://leetcode-cn.com/problems/range-addition-ii) 
## 原题
给你一个 `m x n` 的矩阵 `M` **** ，初始化时所有的 `0` 和一个操作数组 `op` ，其中 `ops[i] = [ai, bi]` 意味着当所有的 `0 <= x < ai` 和 `0 <= y < bi` 时， `M[x][y]` 应该加 1。

在 *执行完所有操作后* ，计算并返回 *矩阵中最大整数的个数* 。

 

 **示例 1:** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/02/ex1.jpg" style="height: 176px; width: 750px;" />

```

输入: m = 3, n = 3，ops = [[2,2],[3,3]]
输出: 4
解释: M 中最大的整数是 2, 而且 M 中有4个值为2的元素。因此返回 4。

```
 **示例 2:** 

```

输入: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
输出: 4

```
 **示例 3:** 

```

输入: m = 3, n = 3, ops = []
输出: 9

```
 

 **提示:** 

<meta charset="UTF-8" />
-  `1 <= m, n <= 4 * 10^4` 
-  `0 <= ops.length <= 10^4` 
-  `ops[i].length == 2` 
-  `1 <= a<sub>i</sub> <= m` 
-  `1 <= b<sub>i</sub> <= n` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 599.两个列表的最小索引总和
[https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists](https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists) 
## 原题
假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用 **最少的索引和** 找出他们 **共同喜爱的餐厅** 。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。

 

 **示例 1:** 

```

输入: list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
输出: ["Shogun"]
解释: 他们唯一共同喜爱的餐厅是“Shogun”。

```
 **示例 2:** 

```

输入:list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]，list2 = ["KFC", "Shogun", "Burger King"]
输出: ["Shogun"]
解释: 他们共同喜爱且具有最小索引和的餐厅是“Shogun”，它有最小的索引和1(0+1)。

```
 

 **提示:** 
-  `1 <= list1.length, list2.length <= 1000` 
-  `1 <= list1[i].length, list2[i].length <= 30` 
-  `list1[i]` 和 `list2[i]` 由空格<meta charset="UTF-8" /> `' '` 和英文字母组成。
-  `list1` 的所有字符串都是 **唯一** 的。
-  `list2` 中的所有字符串都是 **唯一** 的。
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 600.不含连续1的非负整数
[https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones](https://leetcode-cn.com/problems/non-negative-integers-without-consecutive-ones) 
## 原题
给定一个正整数 `n` ，返回范围在 `[0, n]` 都非负整数中，其二进制表示不包含 **连续的 1** 的个数。

 

 **示例 1:** 

```

输入: n = 5
输出: 5
解释: 
下面是带有相应二进制表示的非负整数<= 5：
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
```
 **示例 2:** 

```

输入: n = 1
输出: 2

```
 **示例 3:** 

```

输入: n = 2
输出: 3

```
 

 **提示:** 
-  `1 <= n <= 10^9` 
 
**标签**
`动态规划` 


## 
```python

```
>
