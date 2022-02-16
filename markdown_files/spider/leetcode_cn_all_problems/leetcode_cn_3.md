# 301.删除无效的括号
[https://leetcode-cn.com/problems/remove-invalid-parentheses](https://leetcode-cn.com/problems/remove-invalid-parentheses) 
## 原题
给你一个由若干括号和字母组成的字符串 `s` ，删除最小数量的无效括号，使得输入的字符串有效。

返回所有可能的结果。答案可以按 **任意顺序** 返回。

 

 **示例 1：** 

```

输入：s = "()())()"
输出：["(())()","()()()"]

```
 **示例 2：** 

```

输入：s = "(a)())()"
输出：["(a())()","(a)()()"]

```
 **示例 3：** 

```

输入：s = ")("
输出：[""]

```
 

 **提示：** 
-  `1 <= s.length <= 25` 
-  `s` 由小写英文字母以及括号 `'('` 和 `')'` 组成
-  `s` 中至多含 `20` 个括号
 
**标签**
`广度优先搜索` `字符串` `回溯` 


## 
```python

```
>
# 302.包含全部黑色像素的最小矩形
[https://leetcode-cn.com/problems/smallest-rectangle-enclosing-black-pixels](https://leetcode-cn.com/problems/smallest-rectangle-enclosing-black-pixels) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `二分查找` `矩阵` 


## 
```python

```
>
# 303.区域和检索 - 数组不可变
[https://leetcode-cn.com/problems/range-sum-query-immutable](https://leetcode-cn.com/problems/range-sum-query-immutable) 
## 原题
给定一个整数数组 `nums` ，处理以下类型的多个查询:
- 计算索引 `left` 和 `right` （包含 `left` 和 `right` ）之间的 `nums` 元素的 **和** ，其中 `left <= right` 
实现 `NumArray` 类：
-  `NumArray(int[] nums)` 使用数组 `nums` 初始化对象
-  `int sumRange(int i, int j)` 返回数组 `nums` 中索引 `left` 和 `right` 之间的元素的 **总和** ，包含 `left` 和 `right` 两点（也就是 `nums[left] + nums[left + 1] + ... + nums[right]` )
 

 **示例 1：** 

```

输入：
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
输出：
[null, 1, -1, -3]

解释：
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))

```
 

 **提示：** 
-  `0 <= nums.length <= 10^4` 
-  `-10^5 <= nums[i] <= 10^5` 
-  `0 <= i <= j < nums.length` 
- 最多调用 `10^4` 次 `sumRange` **** 方法
 
**标签**
`设计` `数组` `前缀和` 


## 
```python

```
>
# 304.二维区域和检索 - 矩阵不可变
[https://leetcode-cn.com/problems/range-sum-query-2d-immutable](https://leetcode-cn.com/problems/range-sum-query-2d-immutable) 
## 原题
<big><small>给定一个二维矩阵 `matrix` ，</small></big>以下类型的多个请求：
- <big><small>计算其子矩形范围内元素的总和，该子矩阵的 **左上角** 为 `(row1, col1)` ， **右下角** 为 `(row2, col2)` 。</small></big>
实现 `NumMatrix` 类：
-  `NumMatrix(int[][] matrix)` 给定整数矩阵 `matrix` 进行初始化
-  `int sumRegion(int row1, int col1, int row2, int col2)` 返回<big><small> **左上角** </small></big><big><small> `(row1, col1)` 、 **右下角** `(row2, col2)` </small></big> 所描述的子矩阵的元素 **总和** 。
 

 **示例 1：** 

<img src="https://pic.leetcode-cn.com/1626332422-wUpUHT-image.png" style="width: 200px;" />

```

输入: 
["NumMatrix","sumRegion","sumRegion","sumRegion"]
[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]
输出: 
[null, 8, 11, 12]

解释:
NumMatrix numMatrix = new NumMatrix([[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (红色矩形框的元素总和)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (绿色矩形框的元素总和)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (蓝色矩形框的元素总和)

```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m, n <= 200` <meta charset="UTF-8" />
-  `-10^5 <= matrix[i][j] <= 10^5` 
-  `0 <= row1 <= row2 < m` 
-  `0 <= col1 <= col2 < n` 
- <meta charset="UTF-8" />最多调用 `10^4` 次 `sumRegion` 方法
 
**标签**
`设计` `数组` `矩阵` `前缀和` 


## 
```python

```
>
# 305.岛屿数量 II
[https://leetcode-cn.com/problems/number-of-islands-ii](https://leetcode-cn.com/problems/number-of-islands-ii) 
## 原题

 
**标签**
`并查集` `数组` 


## 
```python

```
>
# 306.累加数
[https://leetcode-cn.com/problems/additive-number](https://leetcode-cn.com/problems/additive-number) 
## 原题
 **累加数** 是一个字符串，组成它的数字可以形成累加序列。

一个有效的 **累加序列** 必须 **至少** 包含 3 个数。除了最开始的两个数以外，序列中的每个后续数字必须是它之前两个数字之和。

给你一个只包含数字 `'0'-'9'` 的字符串，编写一个算法来判断给定输入是否是 **累加数** 。如果是，返回 `true` ；否则，返回 `false` 。

 **说明：** 累加序列里的数，除数字 0 之外， **不会** 以 0 开头，所以不会出现 `1, 2, 03` 或者 `1, 02, 3` 的情况。

 

 **示例 1：** 

```

输入："112358"
输出：true 
解释：累加序列为: 1, 1, 2, 3, 5, 8 。1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

```
 **示例 2：** 

```

输入："199100199"
输出：true 
解释：累加序列为: 1, 99, 100, 199。1 + 99 = 100, 99 + 100 = 199
```
 

 **提示：** 
-  `1 <= num.length <= 35` 
-  `num` 仅由数字（ `0` - `9` ）组成
 

 **进阶：** 你计划如何处理由过大的整数输入导致的溢出?

 
**标签**
`字符串` `回溯` 


## 
```python

```
>
# 307.区域和检索 - 数组可修改
[https://leetcode-cn.com/problems/range-sum-query-mutable](https://leetcode-cn.com/problems/range-sum-query-mutable) 
## 原题
给你一个数组 `nums` ，请你完成两类查询。
- 其中一类查询要求 **更新** 数组 `nums` 下标对应的值
- 另一类查询要求返回数组 `nums` 中索引 `left` 和索引 `right` 之间（ **包含** ）的nums元素的 **和** ，其中 `left <= right` 
实现 `NumArray` 类：
-  `NumArray(int[] nums)` 用整数数组 `nums` 初始化对象
-  `void update(int index, int val)` 将 `nums[index]` 的值 **更新** 为 `val` 
-  `int sumRange(int left, int right)` 返回数组 `nums` 中索引 `left` 和索引 `right` 之间（ **包含** ）的nums元素的 **和** （即， `nums[left] + nums[left + 1], ..., nums[right]` ）
 

 **示例 1：** 

```

输入：
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
输出：
[null, 9, null, 8]

解释：
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // 返回 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1,2,5]
numArray.sumRange(0, 2); // 返回 1 + 2 + 5 = 8

```
 

 **提示：** 
-  `1 <= nums.length <= 3 * 10^4` 
-  `-100 <= nums[i] <= 100` 
-  `0 <= index < nums.length` 
-  `-100 <= val <= 100` 
-  `0 <= left <= right < nums.length` 
- 调用 `pdate` 和 `sumRange` 方法次数不大于 `3 * 10^4` 
 
**标签**
`设计` `树状数组` `线段树` `数组` 


## 
```python

```
>
# 308.二维区域和检索 - 可变
[https://leetcode-cn.com/problems/range-sum-query-2d-mutable](https://leetcode-cn.com/problems/range-sum-query-2d-mutable) 
## 原题

 
**标签**
`设计` `树状数组` `线段树` `数组` `矩阵` 


## 
```python

```
>
# 309.最佳买卖股票时机含冷冻期
[https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown) 
## 原题
给定一个整数数组<meta charset="UTF-8" /> `prices` ，其中第  `prices[i]` 表示第 ` *i* ` 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:
- 卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
 **注意：** 你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

 **示例 1:** 

```

输入: prices = [1,2,3,0,2]
输出: 3 
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]
```
 **示例 2:** 

```

输入: prices = [1]
输出: 0

```
 

 **提示：** 
-  `1 <= prices.length <= 5000` 
-  `0 <= prices[i] <= 1000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 310.最小高度树
[https://leetcode-cn.com/problems/minimum-height-trees](https://leetcode-cn.com/problems/minimum-height-trees) 
## 原题
树是一个无向图，其中任何两个顶点只通过一条路径连接。 换句话说，一个任何没有简单环路的连通图都是一棵树。

给你一棵包含 `n` 个节点的树，标记为 `0` 到 `n - 1` 。给定数字 `n` 和一个有 `n - 1` 条无向边的 `edges` 列表（每一个边都是一对标签），其中 `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` 表示树中节点 `a<sub>i</sub>` 和 `b<sub>i</sub>` 之间存在一条无向边。

可选择树中任何一个节点作为根。当选择节点 `x` 作为根节点时，设结果树的高度为 `h` 。在所有可能的树中，具有最小高度的树（即， `min(h)` ）被称为 **最小高度树** 。

请你找到所有的 **最小高度树** 并按 **任意顺序** 返回它们的根节点标签列表。
树的 **高度** 是指根节点和叶子节点之间最长向下路径上边的数量。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/e1.jpg" style="height: 213px; width: 800px;" />
```

输入：n = 4, edges = [[1,0],[1,2],[1,3]]
输出：[1]
解释：如图所示，当根是标签为 1 的节点时，树的高度是 1 ，这是唯一的最小高度树。
```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/e2.jpg" style="height: 321px; width: 800px;" />
```

输入：n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
输出：[3,4]

```
 
 **提示：** 
-  `1 <= n <= 2 * 10^4` 
-  `edges.length == n - 1` 
-  `0 <= a<sub>i</sub>, b<sub>i</sub> < n` 
-  `a<sub>i</sub> != b<sub>i</sub>` 
- 所有 `(a<sub>i</sub>, b<sub>i</sub>)` 互不相同
- 给定的输入 **保证** 是一棵树，并且 **不会有重复的边** 
 
**标签**
`深度优先搜索` `广度优先搜索` `图` `拓扑排序` 


## 
```python

```
>
# 311.稀疏矩阵的乘法
[https://leetcode-cn.com/problems/sparse-matrix-multiplication](https://leetcode-cn.com/problems/sparse-matrix-multiplication) 
## 原题

 
**标签**
`数组` `哈希表` `矩阵` 


## 
```python

```
>
# 312.戳气球
[https://leetcode-cn.com/problems/burst-balloons](https://leetcode-cn.com/problems/burst-balloons) 
## 原题
有 `n` 个气球，编号为 `0` 到 `n - 1` ，每个气球上都标有一个数字，这些数字存在数组  `nums`  中。

现在要求你戳破所有的气球。戳破第 `i` 个气球，你可以获得  `nums[i - 1] * nums[i] * nums[i + 1]` 枚硬币。 这里的 `i - 1` 和 `i + 1` 代表和  `i`  相邻的两个气球的序号。如果 `i - 1` 或 `i + 1` 超出了数组的边界，那么就当它是一个数字为 `1` 的气球。

求所能获得硬币的最大数量。

 
 **示例 1：** 

```

输入：nums = [3,1,5,8]
输出：167
解释：
nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
```
 **示例 2：** 

```

输入：nums = [1,5]
输出：10

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 500` 
-  `0 <= nums[i] <= 100` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 313.超级丑数
[https://leetcode-cn.com/problems/super-ugly-number](https://leetcode-cn.com/problems/super-ugly-number) 
## 原题
 **超级丑数** 是一个正整数，并满足其所有质因数都出现在质数数组 `primes` 中。

给你一个整数 `n` 和一个整数数组 `primes` ，返回第 `n` 个 **超级丑数** 。

题目数据保证第 `n` 个 **超级丑数** 在 **32-bit** 带符号整数范围内。

 

 **示例 1：** 

```

输入：n = 12, primes = [2,7,13,19]
输出：32 
解释：给定长度为 4 的质数数组 primes = [2,7,13,19]，前 12 个超级丑数序列为：[1,2,4,7,8,13,14,16,19,26,28,32] 。
```
 **示例 2：** 

```

输入：n = 1, primes = [2,3,5]
输出：1
解释：1 不含质因数，因此它的所有质因数都在质数数组 primes = [2,3,5] 中。

```

 
 **提示：** 
-  `1 <= n <= 10^6` 
-  `1 <= primes.length <= 100` 
-  `2 <= primes[i] <= 1000` 
- 题目数据 **保证** `primes[i]` 是一个质数
-  `primes` 中的所有值都 **互不相同** ，且按 **递增顺序** 排列
 
**标签**
`数组` `哈希表` `数学` `动态规划` `堆（优先队列）` 


## 
```python

```
>
# 314.二叉树的垂直遍历
[https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal](https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `哈希表` `二叉树` 


## 
```python

```
>
# 315.计算右侧小于当前元素的个数
[https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self](https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self) 
## 原题
给你一个整数数组 `nums` ，按要求返回一个新数组 `counts` 。数组 `counts` 有该性质： `counts[i]` 的值是 `nums[i]` 右侧小于 `nums[i]` 的元素的数量。

 

 **示例 1：** 

```

输入：nums = [5,2,6,1]
输出：[2,1,1,0] 
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素

```
 **示例 2：** 

```

输入：nums = [-1]
输出：[0]

```
 **示例 3：** 

```

输入：nums = [-1,-1]
输出：[0,0]

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-10^4 <= nums[i] <= 10^4` 
 
**标签**
`树状数组` `线段树` `数组` `二分查找` `分治` `有序集合` `归并排序` 


## 
```python

```
>
# 316.去除重复字母
[https://leetcode-cn.com/problems/remove-duplicate-letters](https://leetcode-cn.com/problems/remove-duplicate-letters) 
## 原题
给你一个字符串 `s` ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 **返回结果的字典序最小** （要求不能打乱其他字符的相对位置）。

 

 **示例 1：** 

```

输入：s = "bcabc"
输出："abc"

```
 **示例 2：** 

```

输入：s = "cbacdcbc"
输出："acdb"
```
 

 **提示：** 
-  `1 <= s.length <= 10^4` 
-  `s` 由小写英文字母组成
 

 **注意：** 该题与 1081 <a href="https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters">https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters</a> 相同

 
**标签**
`栈` `贪心` `字符串` `单调栈` 


## 
```python

```
>
# 317.离建筑物最近的距离
[https://leetcode-cn.com/problems/shortest-distance-from-all-buildings](https://leetcode-cn.com/problems/shortest-distance-from-all-buildings) 
## 原题

 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 318.最大单词长度乘积
[https://leetcode-cn.com/problems/maximum-product-of-word-lengths](https://leetcode-cn.com/problems/maximum-product-of-word-lengths) 
## 原题
给你一个字符串数组 `words` ，找出并返回 `length(words[i]) * length(words[j])` 的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 `0` 。

 

 **示例 1：** 

```

输入：words = ["abcw","baz","foo","bar","xtfn","abcdef"]
输出：16 
解释：这两个单词为 "abcw", "xtfn"。
```
 **示例 2：** 

```

输入：words = ["a","ab","abc","d","cd","bcd","abcd"]
输出：4 
解释：这两个单词为 "ab", "cd"。
```
 **示例 3：** 

```

输入：words = ["a","aa","aaa","aaaa"]
输出：0 
解释：不存在这样的两个单词。

```
 

 **提示：** 
-  `2 <= words.length <= 1000` 
-  `1 <= words[i].length <= 1000` 
-  `words[i]` 仅包含小写字母
 
**标签**
`位运算` `数组` `字符串` 


## 
```python

```
>
# 319.灯泡开关
[https://leetcode-cn.com/problems/bulb-switcher](https://leetcode-cn.com/problems/bulb-switcher) 
## 原题
初始时有 `n` 个灯泡处于关闭状态。第一轮，你将会打开所有灯泡。接下来的第二轮，你将会每两个灯泡关闭第二个。

第三轮，你每三个灯泡就切换第三个灯泡的开关（即，打开变关闭，关闭变打开）。第 `i` 轮，你每 `i` 个灯泡就切换第 `i` 个灯泡的开关。直到第 `n` 轮，你只需要切换最后一个灯泡的开关。

找出并返回 `n` 轮后有多少个亮着的灯泡。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bulb.jpg" style="width: 421px; height: 321px;" />

```

输入：n = 3
输出：1 
解释：
初始时, 灯泡状态 [关闭, 关闭, 关闭].
第一轮后, 灯泡状态 [开启, 开启, 开启].
第二轮后, 灯泡状态 [开启, 关闭, 开启].
第三轮后, 灯泡状态 [开启, 关闭, 关闭]. 

你应该返回 1，因为只有一个灯泡还亮着。

```
 **示例 2：** 

```

输入：n = 0
输出：0

```
 **示例 3：** 

```

输入：n = 1
输出：1

```
 

 **提示：** 
-  `0 <= n <= 10^9` 
 
**标签**
`脑筋急转弯` `数学` 


## 
```python

```
>
# 320.列举单词的全部缩写
[https://leetcode-cn.com/problems/generalized-abbreviation](https://leetcode-cn.com/problems/generalized-abbreviation) 
## 原题

 
**标签**
`位运算` `字符串` `回溯` 


## 
```python

```
>
# 321.拼接最大数
[https://leetcode-cn.com/problems/create-maximum-number](https://leetcode-cn.com/problems/create-maximum-number) 
## 原题
给定长度分别为 `m` 和 `n` 的两个数组，其元素由 `0-9` 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 `k (k <= m + n)` 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 `k` 的数组。

 **说明:** 请尽可能地优化你算法的时间和空间复杂度。

 **示例 1:** 

```
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
```
 **示例 2:** 

```
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
```
 **示例 3:** 

```
输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
```
 
**标签**
`栈` `贪心` `单调栈` 


## 
```python

```
>
# 322.零钱兑换
[https://leetcode-cn.com/problems/coin-change](https://leetcode-cn.com/problems/coin-change) 
## 原题
给你一个整数数组 `coins` ，表示不同面额的硬币；以及一个整数 `amount` ，表示总金额。

计算并返回可以凑成总金额所需的 **最少的硬币个数** 。如果没有任何一种硬币组合能组成总金额，返回 `-1` 。

你可以认为每种硬币的数量是无限的。

 

 **示例 1：** 

```

输入：coins = [1, 2, 5], amount = 11
输出：3 
解释：11 = 5 + 5 + 1
```
 **示例 2：** 

```

输入：coins = [2], amount = 3
输出：-1
```
 **示例 3：** 

```

输入：coins = [1], amount = 0
输出：0

```
 

 **提示：** 
-  `1 <= coins.length <= 12` 
-  `1 <= coins[i] <= 2^31 - 1` 
-  `0 <= amount <= 10^4` 
 
**标签**
`广度优先搜索` `数组` `动态规划` 


## 
```python

```
>
# 323.无向图中连通分量的数目
[https://leetcode-cn.com/problems/number-of-connected-components-in-an-undirected-graph](https://leetcode-cn.com/problems/number-of-connected-components-in-an-undirected-graph) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `图` 


## 
```python

```
>
# 324.摆动排序 II
[https://leetcode-cn.com/problems/wiggle-sort-ii](https://leetcode-cn.com/problems/wiggle-sort-ii) 
## 原题
给你一个整数数组  `nums` ，将它重新排列成  `nums[0] < nums[1] > nums[2] < nums[3]...`  的顺序。

你可以假设所有输入数组都可以得到满足题目要求的结果。

 

 **示例 1：** 

```

输入：nums = [1,5,1,1,6,4]
输出：[1,6,1,5,1,4]
解释：[1,4,1,5,1,6] 同样是符合题目要求的结果，可以被判题程序接受。

```
 **示例 2：** 

```

输入：nums = [1,3,2,2,3,1]
输出：[2,3,1,3,1,2]

```
 

 **提示：** 
-  `1 <= nums.length <= 5 * 10^4` 
-  `0 <= nums[i] <= 5000` 
- 题目数据保证，对于给定的输入 `nums` ，总能产生满足题目要求的结果
 

 **进阶：** 你能用 O(n) 时间复杂度和 / 或原地 O(1) 额外空间来实现吗？

 
**标签**
`数组` `分治` `快速选择` `排序` 


## 
```python

```
>
# 325.和等于 k 的最长子数组长度
[https://leetcode-cn.com/problems/maximum-size-subarray-sum-equals-k](https://leetcode-cn.com/problems/maximum-size-subarray-sum-equals-k) 
## 原题

 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 326.3 的幂
[https://leetcode-cn.com/problems/power-of-three](https://leetcode-cn.com/problems/power-of-three) 
## 原题
给定一个整数，写一个函数来判断它是否是 3 的幂次方。如果是，返回 `true` ；否则，返回 `false` 。

整数 `n` 是 3 的幂次方需满足：存在整数 `x` 使得 `n == 3^x` 

 

 **示例 1：** 

```

输入：n = 27
输出：true

```
 **示例 2：** 

```

输入：n = 0
输出：false

```
 **示例 3：** 

```

输入：n = 9
输出：true

```
 **示例 4：** 

```

输入：n = 45
输出：false

```
 

 **提示：** 
-  `-2^31 <= n <= 2^31 - 1` 
 

 **进阶：** 你能不使用循环或者递归来完成本题吗？

 
**标签**
`递归` `数学` 


## 
```python

```
>
# 327.区间和的个数
[https://leetcode-cn.com/problems/count-of-range-sum](https://leetcode-cn.com/problems/count-of-range-sum) 
## 原题
给你一个整数数组  `nums` 以及两个整数  `lower` 和 `upper` 。求数组中，值位于范围 `[lower, upper]` （包含  `lower`  和  `upper` ）之内的 **区间和的个数** 。

 **区间和**   `S(i, j)`  表示在  `nums`  中，位置从  `i`  到  `j`  的元素之和，包含  `i`  和  `j`  ( `i` ≤ `j` )。

 
 **示例 1：** 

```

输入：nums = [-2,5,-1], lower = -2, upper = 2
输出：3
解释：存在三个区间：[0,0]、[2,2] 和 [0,2] ，对应的区间和分别是：-2 、-1 、2 。

```
 **示例 2：** 

```

输入：nums = [0], lower = 0, upper = 0
输出：1

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
-  `-10^5 <= lower <= upper <= 10^5` 
- 题目数据保证答案是一个 **32 位** 的整数
 
**标签**
`树状数组` `线段树` `数组` `二分查找` `分治` `有序集合` `归并排序` 


## 
```python

```
>
# 328.奇偶链表
[https://leetcode-cn.com/problems/odd-even-linked-list](https://leetcode-cn.com/problems/odd-even-linked-list) 
## 原题
给定单链表的头节点 `head` ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。

 **第一个** 节点的索引被认为是 **奇数** ， **第二个** 节点的索引为 **偶数** ，以此类推。

请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。

你必须在 `O(1)` 的额外空间复杂度和 `O(n)` 的时间复杂度下解决这个问题。

 

 **示例 1:** 

<img src="https://assets.leetcode.com/uploads/2021/03/10/oddeven-linked-list.jpg" style="height: 123px; width: 300px;" />

```

输入: head = [1,2,3,4,5]
输出: [1,3,5,2,4]
```
 **示例 2:** 

<img src="https://assets.leetcode.com/uploads/2021/03/10/oddeven2-linked-list.jpg" style="height: 142px; width: 500px;" />

```

输入: head = [2,1,3,5,6,4,7]
输出: [2,3,6,7,1,5,4]
```
 

 **提示:** 
-  `n ==` 链表中的节点数
-  `0 <= n <= 10^4` 
-  `-10^6 <= Node.val <= 10^6` 
 
**标签**
`链表` 


## 
```python

```
>
# 329.矩阵中的最长递增路径
[https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix](https://leetcode-cn.com/problems/longest-increasing-path-in-a-matrix) 
## 原题
给定一个  `m x n` 整数矩阵  `matrix` ，找出其中 **最长递增路径** 的长度。

对于每个单元格，你可以往上，下，左，右四个方向移动。 你 **不能** 在 **对角线** 方向上移动或移动到 **边界外** （即不允许环绕）。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/05/grid1.jpg" style="width: 242px; height: 242px;" />
```

输入：matrix = [[9,9,4],[6,6,8],[2,1,1]]
输出：4 
解释：最长递增路径为 [1, 2, 6, 9]。
```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/27/tmp-grid.jpg" style="width: 253px; height: 253px;" />
```

输入：matrix = [[3,4,5],[3,2,6],[2,2,1]]
输出：4 
解释：最长递增路径是 [3, 4, 5, 6]。注意不允许在对角线方向上移动。

```
 **示例 3：** 

```

输入：matrix = [[1]]
输出：1

```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m, n <= 200` 
-  `0 <= matrix[i][j] <= 2^31 - 1` 
 
**标签**
`深度优先搜索` `广度优先搜索` `图` `拓扑排序` `记忆化搜索` `动态规划` 


## 
```python

```
>
# 330.按要求补齐数组
[https://leetcode-cn.com/problems/patching-array](https://leetcode-cn.com/problems/patching-array) 
## 原题
给定一个已排序的正整数数组 `nums` *，* 和一个正整数 `n` *。* 从 `[1, n]` 区间内选取任意个数字补充到 nums 中，使得 `[1, n]` 区间内的任何数字都可以用 nums 中某几个数字的和来表示。

请返回 *满足上述要求的最少需要补充的数字个数* 。

 

 **示例 1:** 

```

输入: nums = [1,3], n = 6
输出: 1 
解释:
根据 nums 里现有的组合 [1], [3], [1,3]，可以得出 1, 3, 4。
现在如果我们将 2 添加到 nums 中， 组合变为: [1], [2], [3], [1,3], [2,3], [1,2,3]。
其和可以表示数字 1, 2, 3, 4, 5, 6，能够覆盖 [1, 6] 区间里所有的数。
所以我们最少需要添加一个数字。
```
 **示例 2:** 

```

输入: nums = [1,5,10], n = 20
输出: 2
解释: 我们需要添加 [2,4]。

```
 **示例 3:** 

```

输入: nums = [1,2,2], n = 5
输出: 0

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `1 <= nums[i] <= 10^4` 
-  `nums` 按 **升序排列** 
-  `1 <= n <= 2^31 - 1` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 331.验证二叉树的前序序列化
[https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree](https://leetcode-cn.com/problems/verify-preorder-serialization-of-a-binary-tree) 
## 原题
序列化二叉树的一种方法是使用前序遍历。当我们遇到一个非空节点时，我们可以记录下这个节点的值。如果它是一个空节点，我们可以使用一个标记值记录，例如 `#` 。

```
     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #

```
例如，上面的二叉树可以被序列化为字符串 `"9,3,4,#,#,1,#,#,2,#,6,#,#"` ，其中 `#` 代表一个空节点。

给定一串以逗号分隔的序列，验证它是否是正确的二叉树的前序序列化。编写一个在不重构树的条件下的可行算法。

每个以逗号分隔的字符或为一个整数或为一个表示 `null` 指针的 `';#';` 。

你可以认为输入格式总是有效的，例如它永远不会包含两个连续的逗号，比如 `"1,,3"` 。

 **示例 1:** 

```
输入: "9,3,4,#,#,1,#,#,2,#,6,#,#"
输出: true
```
 **示例 2:** 

```
输入: "1,#"
输出: false

```
 **示例 3:** 

```
输入: "9,#,#,1"
输出: false
```
 
**标签**
`栈` `树` `字符串` `二叉树` 


## 
```python

```
>
# 332.重新安排行程
[https://leetcode-cn.com/problems/reconstruct-itinerary](https://leetcode-cn.com/problems/reconstruct-itinerary) 
## 原题
给你一份航线列表 `tickets` ，其中 `tickets[i] = [from<sub>i</sub>, to<sub>i</sub>]` 表示飞机出发和降落的机场地点。请你对该行程进行重新规划排序。

所有这些机票都属于一个从 `JFK` （肯尼迪国际机场）出发的先生，所以该行程必须从 `JFK` 开始。如果存在多种有效的行程，请你按字典排序返回最小的行程组合。
- 例如，行程 `["JFK", "LGA"]` 与 `["JFK", "LGB"]` 相比就更小，排序更靠前。
假定所有机票至少存在一种合理的行程。且所有的机票 必须都用一次 且 只能用一次。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/itinerary1-graph.jpg" style="width: 382px; height: 222px;" />
```

输入：tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
输出：["JFK","MUC","LHR","SFO","SJC"]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/itinerary2-graph.jpg" style="width: 222px; height: 230px;" />
```

输入：tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
输出：["JFK","ATL","JFK","SFO","ATL","SFO"]
解释：另一种有效的行程是 ["JFK","SFO","ATL","JFK","ATL","SFO"] ，但是它字典排序更大更靠后。

```
 

 **提示：** 
-  `1 <= tickets.length <= 300` 
-  `tickets[i].length == 2` 
-  `from<sub>i</sub>.length == 3` 
-  `to<sub>i</sub>.length == 3` 
-  `from<sub>i</sub>` 和 `to<sub>i</sub>` 由大写英文字母组成
-  `from<sub>i</sub> != to<sub>i</sub>` 
 
**标签**
`深度优先搜索` `图` `欧拉回路` 


## 
```python

```
>
# 333.最大 BST 子树
[https://leetcode-cn.com/problems/largest-bst-subtree](https://leetcode-cn.com/problems/largest-bst-subtree) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉搜索树` `动态规划` `二叉树` 


## 
```python

```
>
# 334.递增的三元子序列
[https://leetcode-cn.com/problems/increasing-triplet-subsequence](https://leetcode-cn.com/problems/increasing-triplet-subsequence) 
## 原题
给你一个整数数组 `nums` ，判断这个数组中是否存在长度为 `3` 的递增子序列。

如果存在这样的三元组下标 `(i, j, k)` 且满足 `i < j < k` ，使得 `nums[i] < nums[j] < nums[k]` ，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：nums = [1,2,3,4,5]
输出：true
解释：任何 i < j < k 的三元组都满足题意

```
 **示例 2：** 

```

输入：nums = [5,4,3,2,1]
输出：false
解释：不存在满足题意的三元组
```
 **示例 3：** 

```

输入：nums = [2,1,5,0,4,6]
输出：true
解释：三元组 (3, 4, 5) 满足题意，因为 nums[3] == 0 < nums[4] == 4 < nums[5] == 6

```
 

 **提示：** 
-  `1 <= nums.length <= 5 * 10^5` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
 

 **进阶：** 你能实现时间复杂度为 `O(n)` ，空间复杂度为 `O(1)` 的解决方案吗？

 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 335.路径交叉
[https://leetcode-cn.com/problems/self-crossing](https://leetcode-cn.com/problems/self-crossing) 
## 原题
给你一个整数数组 `distance` 。

从 **X-Y** 平面上的点 `(0,0)` 开始，先向北移动 `distance[0]` 米，然后向西移动 `distance[1]` 米，向南移动 `distance[2]` 米，向东移动 `distance[3]` 米，持续移动。也就是说，每次移动后你的方位会发生逆时针变化。

判断你所经过的路径是否相交。如果相交，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/selfcross1-plane.jpg" style="width: 400px; height: 435px;" />
```

输入：distance = [2,1,1,2]
输出：true

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/selfcross2-plane.jpg" style="width: 400px; height: 435px;" />
```

输入：distance = [1,2,3,4]
输出：false

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/selfcross3-plane.jpg" style="width: 400px; height: 435px;" />
```

输入：distance = [1,1,1,1]
输出：true
```
 

 **提示：** 
-  `1 <= distance.length <= 10^5` 
-  `1 <= distance[i] <= 10^5` 
 
**标签**
`几何` `数组` `数学` 


## 
```python

```
>
# 336.回文对
[https://leetcode-cn.com/problems/palindrome-pairs](https://leetcode-cn.com/problems/palindrome-pairs) 
## 原题
给定一组 **互不相同** 的单词， 找出所有 **不同 * * ** 的索引对 `(i, j)` ，使得列表中的两个单词，  `words[i] + words[j]`  ，可拼接成回文串。

 

 **示例 1：** 

```

输入：words = ["abcd","dcba","lls","s","sssll"]
输出：[[0,1],[1,0],[3,2],[2,4]] 
解释：可拼接成的回文串为 ["dcbaabcd","abcddcba","slls","llssssll"]

```
 **示例 2：** 

```

输入：words = ["bat","tab","cat"]
输出：[[0,1],[1,0]] 
解释：可拼接成的回文串为 ["battab","tabbat"]
```
 **示例 3：** 

```

输入：words = ["a",""]
输出：[[0,1],[1,0]]

```

 

 **提示：** 
-  `1 <= words.length <= 5000` 
-  `0 <= words[i].length <= 300` 
-  `words[i]` 由小写英文字母组成
 
**标签**
`字典树` `数组` `哈希表` `字符串` 


## 
```python

```
>
# 337.打家劫舍 III
[https://leetcode-cn.com/problems/house-robber-iii](https://leetcode-cn.com/problems/house-robber-iii) 
## 原题
小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为<meta charset="UTF-8" /> `root` 。

除了<meta charset="UTF-8" /> `root` 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 **两个直接相连的房子在同一天晚上被打劫** ，房屋将自动报警。

给定二叉树的 `root` 。返回 ***在不触动警报的情况下** ，小偷能够盗取的最高金额* 。

 

 **示例 1:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob1-tree.jpg" />

```

输入: root = [3,2,3,null,3,null,1]
输出: 7 
解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
```
 **示例 2:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/10/rob2-tree.jpg" />

```

输入: root = [3,4,5,1,3,null,1]
输出: 9
解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9

```
 

 **提示：** 

<meta charset="UTF-8" />
- 树的节点数在 `[1, 10^4]` 范围内
-  `0 <= Node.val <= 10^4` 
 
**标签**
`树` `深度优先搜索` `动态规划` `二叉树` 


## 
```python

```
>
# 338.比特位计数
[https://leetcode-cn.com/problems/counting-bits](https://leetcode-cn.com/problems/counting-bits) 
## 原题
给你一个整数 `n` ，对于 `0 <= i <= n` 中的每个 `i` ，计算其二进制表示中 ** `1` 的个数** ，返回一个长度为 `n + 1` 的数组 `ans` 作为答案。

 
 **示例 1：** 

```

输入：n = 2
输出：[0,1,1]
解释：
0 --> 0
1 --> 1
2 --> 10

```
 **示例 2：** 

```

输入：n = 5
输出：[0,1,1,2,1,2]
解释：
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

```
 

 **提示：** 
-  `0 <= n <= 10^5` 
 

 **进阶：** 
- 很容易就能实现时间复杂度为 `O(n log n)` 的解决方案，你可以在线性时间复杂度 `O(n)` 内用一趟扫描解决此问题吗？
- 你能不使用任何内置函数解决此问题吗？（如，C++ 中的 `__builtin_popcount` ）
 
**标签**
`位运算` `动态规划` 


## 
```python

```
>
# 339.嵌套列表权重和
[https://leetcode-cn.com/problems/nested-list-weight-sum](https://leetcode-cn.com/problems/nested-list-weight-sum) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` 


## 
```python

```
>
# 340.至多包含 K 个不同字符的最长子串
[https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters](https://leetcode-cn.com/problems/longest-substring-with-at-most-k-distinct-characters) 
## 原题

 
**标签**
`哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
# 341.扁平化嵌套列表迭代器
[https://leetcode-cn.com/problems/flatten-nested-list-iterator](https://leetcode-cn.com/problems/flatten-nested-list-iterator) 
## 原题
给你一个嵌套的整数列表 `nestedList` 。每个元素要么是一个整数，要么是一个列表；该列表的元素也可能是整数或者是其他列表。请你实现一个迭代器将其扁平化，使之能够遍历这个列表中的所有整数。

实现扁平迭代器类 `NestedIterator` ：
-  `NestedIterator(List<NestedInteger> nestedList)` 用嵌套列表 `nestedList` 初始化迭代器。
-  `int next()` 返回嵌套列表的下一个整数。
-  `boolean hasNext()` 如果仍然存在待迭代的整数，返回 `true` ；否则，返回 `false` 。
你的代码将会用下述伪代码检测：

```

initialize iterator with nestedList
res = []
while iterator.hasNext()
    append iterator.next() to the end of res
return res
```
如果 `res` 与预期的扁平化列表匹配，那么你的代码将会被判为正确。

 

 **示例 1：** 

```

输入：nestedList = [[1,1],2,[1,1]]
输出：[1,1,2,1,1]
解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,1,2,1,1]。
```
 **示例 2：** 

```

输入：nestedList = [1,[4,[6]]]
输出：[1,4,6]
解释：通过重复调用 next 直到 hasNext 返回 false，next 返回的元素的顺序应该是: [1,4,6]。

```
 

 **提示：** 
-  `1 <= nestedList.length <= 500` 
- 嵌套列表中的整数值在范围 `[-10^6, 10^6]` 内
 
**标签**
`栈` `树` `深度优先搜索` `设计` `队列` `迭代器` 


## 
```python

```
>
# 342.4的幂
[https://leetcode-cn.com/problems/power-of-four](https://leetcode-cn.com/problems/power-of-four) 
## 原题
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 `true` ；否则，返回 `false` 。

整数 `n` 是 4 的幂次方需满足：存在整数 `x` 使得 `n == 4^x` 

 

 **示例 1：** 

```

输入：n = 16
输出：true

```
 **示例 2：** 

```

输入：n = 5
输出：false

```
 **示例 3：** 

```

输入：n = 1
输出：true

```
 

 **提示：** 
-  `-2^31 <= n <= 2^31 - 1` 
 

 **进阶：** 你能不使用循环或者递归来完成本题吗？

 
**标签**
`位运算` `递归` `数学` 


## 
```python

```
>
# 343.整数拆分
[https://leetcode-cn.com/problems/integer-break](https://leetcode-cn.com/problems/integer-break) 
## 原题
给定一个正整数 `n` ，将其拆分为 `k` 个 **正整数** 的和（ `k >= 2` ），并使这些整数的乘积最大化。

返回 *你可以获得的最大乘积* 。

 

 **示例 1:** 

```

输入: n = 2
输出: 1
解释: 2 = 1 + 1, 1 × 1 = 1。
```
 **示例 2:** 

```

输入: n = 10
输出: 36
解释: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36。
```
 

 **提示:** 
-  `2 <= n <= 58` 
 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 344.反转字符串
[https://leetcode-cn.com/problems/reverse-string](https://leetcode-cn.com/problems/reverse-string) 
## 原题
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 `s` 的形式给出。

不要给另外的数组分配额外的空间，你必须 **<a href="https://baike.baidu.com/item/原地算法" target="_blank">原地</a>修改输入数组** 、使用 O(1) 的额外空间解决这一问题。

 

 **示例 1：** 

```

输入：s = ["h","e","l","l","o"]
输出：["o","l","l","e","h"]

```
 **示例 2：** 

```

输入：s = ["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s[i]` 都是 <a href="https://baike.baidu.com/item/ASCII" target="_blank">ASCII</a> 码表中的可打印字符
 
**标签**
`递归` `双指针` `字符串` 


## 
```python

```
>
# 345.反转字符串中的元音字母
[https://leetcode-cn.com/problems/reverse-vowels-of-a-string](https://leetcode-cn.com/problems/reverse-vowels-of-a-string) 
## 原题
给你一个字符串 `s` ，仅反转字符串中的所有元音字母，并返回结果字符串。

元音字母包括 `'a'` 、 `'e'` 、 `'i'` 、 `'o'` 、 `'u'` ，且可能以大小写两种形式出现。

 

 **示例 1：** 

```

输入：s = "hello"
输出："holle"

```
 **示例 2：** 

```

输入：s = "leetcode"
输出："leotcede"
```
 

 **提示：** 
-  `1 <= s.length <= 3 * 10^5` 
-  `s` 由 **可打印的 ASCII** 字符组成
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 346.数据流中的移动平均值
[https://leetcode-cn.com/problems/moving-average-from-data-stream](https://leetcode-cn.com/problems/moving-average-from-data-stream) 
## 原题

 
**标签**
`设计` `队列` `数组` `数据流` 


## 
```python

```
>
# 347.前 K 个高频元素
[https://leetcode-cn.com/problems/top-k-frequent-elements](https://leetcode-cn.com/problems/top-k-frequent-elements) 
## 原题
给你一个整数数组 `nums` 和一个整数 `k` ，请你返回其中出现频率前 `k` 高的元素。你可以按 **任意顺序** 返回答案。

 

 **示例 1:** 

```

输入: nums = [1,1,1,2,2,3], k = 2
输出: [1,2]

```
 **示例 2:** 

```

输入: nums = [1], k = 1
输出: [1]
```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `k` 的取值范围是 `[1, 数组中不相同的元素的个数]` 
- 题目数据保证答案唯一，换句话说，数组中前 `k` 个高频元素的集合是唯一的
 

 **进阶：** 你所设计算法的时间复杂度 **必须** 优于 `O(n log n)` ，其中 `n` * * 是数组大小。

 
**标签**
`数组` `哈希表` `分治` `桶排序` `计数` `快速选择` `排序` `堆（优先队列）` 


## 
```python

```
>
# 348.设计井字棋
[https://leetcode-cn.com/problems/design-tic-tac-toe](https://leetcode-cn.com/problems/design-tic-tac-toe) 
## 原题

 
**标签**
`设计` `数组` `哈希表` `矩阵` 


## 
```python

```
>
# 349.两个数组的交集
[https://leetcode-cn.com/problems/intersection-of-two-arrays](https://leetcode-cn.com/problems/intersection-of-two-arrays) 
## 原题
给定两个数组 `nums1` 和 `nums2` ，返回 *它们的交集* 。输出结果中的每个元素一定是 **唯一** 的。我们可以 **不考虑输出结果的顺序** 。

 

 **示例 1：** 

```

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]

```
 **示例 2：** 

```

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的

```
 

 **提示：** 
-  `1 <= nums1.length, nums2.length <= 1000` 
-  `0 <= nums1[i], nums2[i] <= 1000` 
 
**标签**
`数组` `哈希表` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 350.两个数组的交集 II
[https://leetcode-cn.com/problems/intersection-of-two-arrays-ii](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii) 
## 原题
给你两个整数数组 `nums1` 和 `nums2` ，请你以数组形式返回两数组的交集。返回结果中每个元素出现的次数，应与元素在两个数组中都出现的次数一致（如果出现次数不一致，则考虑取较小值）。可以不考虑输出结果的顺序。

 

 **示例 1：** 

```

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]

```
 **示例 2:** 

```

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
```
 

 **提示：** 
-  `1 <= nums1.length, nums2.length <= 1000` 
-  `0 <= nums1[i], nums2[i] <= 1000` 
 

 ** **进阶** ：** 
- 如果给定的数组已经排好序呢？你将如何优化你的算法？
- 如果 `nums1` 的大小比 `nums2` 小，哪种方法更优？
- 如果 `nums2` 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？
 
**标签**
`数组` `哈希表` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 351.安卓系统手势解锁
[https://leetcode-cn.com/problems/android-unlock-patterns](https://leetcode-cn.com/problems/android-unlock-patterns) 
## 原题

 
**标签**
`动态规划` `回溯` 


## 
```python

```
>
# 352.将数据流变为多个不相交区间
[https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals](https://leetcode-cn.com/problems/data-stream-as-disjoint-intervals) 
## 原题
 给你一个由非负整数 `a<sub>1</sub>, a<sub>2</sub>, ..., a<sub>n</sub>` 组成的数据流输入，请你将到目前为止看到的数字总结为不相交的区间列表。

实现 `SummaryRanges` 类：
-  `SummaryRanges()` 使用一个空数据流初始化对象。
-  `void addNum(int val)` 向数据流中加入整数 `val` 。
-  `int[][] getIntervals()` 以不相交区间 `[start<sub>i</sub>, end<sub>i</sub>]` 的列表形式返回对数据流中整数的总结。
 

 **示例：** 

```

输入：
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
输出：
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

解释：
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // 返回 [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // 返回 [[1, 3], [6, 7]]

```
 

 **提示：** 
-  `0 <= val <= 10^4` 
- 最多调用 `addNum` 和 `getIntervals` 方法 `3 * 10^4` 次
 

 **进阶：** 如果存在大量合并，并且与数据流的大小相比，不相交区间的数量很小，该怎么办?

 
**标签**
`设计` `二分查找` `有序集合` 


## 
```python

```
>
# 353.贪吃蛇
[https://leetcode-cn.com/problems/design-snake-game](https://leetcode-cn.com/problems/design-snake-game) 
## 原题

 
**标签**
`设计` `队列` `数组` `矩阵` 


## 
```python

```
>
# 354.俄罗斯套娃信封问题
[https://leetcode-cn.com/problems/russian-doll-envelopes](https://leetcode-cn.com/problems/russian-doll-envelopes) 
## 原题
给你一个二维整数数组 `envelopes` ，其中 `envelopes[i] = [w<sub>i</sub>, h<sub>i</sub>]` ，表示第 `i` 个信封的宽度和高度。

当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。

请计算 **最多能有多少个** 信封能组成一组“俄罗斯套娃”信封（即可以把一个信封放到另一个信封里面）。

 **注意** ：不允许旋转信封。
 

 **示例 1：** 

```

输入：envelopes = [[5,4],[6,4],[6,7],[2,3]]
输出：3
解释：最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。
```
 **示例 2：** 

```

输入：envelopes = [[1,1],[1,1],[1,1]]
输出：1

```
 

 **提示：** 
-  `1 <= envelopes.length <= 10^5` 
-  `envelopes[i].length == 2` 
-  `1 <= w<sub>i</sub>, h<sub>i</sub> <= 10^5` 
 
**标签**
`数组` `二分查找` `动态规划` `排序` 


## 
```python

```
>
# 355.设计推特
[https://leetcode-cn.com/problems/design-twitter](https://leetcode-cn.com/problems/design-twitter) 
## 原题
设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近 `10` 条推文。

实现 `Twitter` 类：
-  `Twitter()` 初始化简易版推特对象
-  `void postTweet(int userId, int tweetId)` 根据给定的 `tweetId` 和 `userId` 创建一条新推文。每次调用此函数都会使用一个不同的 `tweetId` 。
-  `List<Integer> getNewsFeed(int userId)` 检索当前用户新闻推送中最近 `10` 条推文的 ID 。新闻推送中的每一项都必须是由用户关注的人或者是用户自己发布的推文。推文必须 **按照时间顺序由最近到最远排序** 。
-  `void follow(int followerId, int followeeId)` ID 为 `followerId` 的用户开始关注 ID 为 `followeeId` 的用户。
-  `void unfollow(int followerId, int followeeId)` ID 为 `followerId` 的用户不再关注 ID 为 `followeeId` 的用户。
 

 **示例：** 

```

输入
["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
[[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
输出
[null, null, [5], null, null, [6, 5], null, [5]]

解释
Twitter twitter = new Twitter();
twitter.postTweet(1, 5); // 用户 1 发送了一条新推文 (用户 id = 1, 推文 id = 5)
twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含一个 id 为 5 的推文
twitter.follow(1, 2);    // 用户 1 关注了用户 2
twitter.postTweet(2, 6); // 用户 2 发送了一个新推文 (推文 id = 6)
twitter.getNewsFeed(1);  // 用户 1 的获取推文应当返回一个列表，其中包含两个推文，id 分别为 -> [6, 5] 。推文 id 6 应当在推文 id 5 之前，因为它是在 5 之后发送的
twitter.unfollow(1, 2);  // 用户 1 取消关注了用户 2
twitter.getNewsFeed(1);  // 用户 1 获取推文应当返回一个列表，其中包含一个 id 为 5 的推文。因为用户 1 已经不再关注用户 2
```
 

 **提示：** 
-  `1 <= userId, followerId, followeeId <= 500` 
-  `0 <= tweetId <= 10^4` 
- 所有推特的 ID 都互不相同
-  `postTweet` 、 `getNewsFeed` 、 `follow` 和 `unfollow` 方法最多调用 `3 * 10^4` 次
 
**标签**
`设计` `哈希表` `链表` `堆（优先队列）` 


## 
```python

```
>
# 356.直线镜像
[https://leetcode-cn.com/problems/line-reflection](https://leetcode-cn.com/problems/line-reflection) 
## 原题

 
**标签**
`数组` `哈希表` `数学` 


## 
```python

```
>
# 357.计算各个位数不同的数字个数
[https://leetcode-cn.com/problems/count-numbers-with-unique-digits](https://leetcode-cn.com/problems/count-numbers-with-unique-digits) 
## 原题
给定一个 **非负** 整数 n，计算各位数字都不同的数字 x 的个数，其中 0 ≤ x < 10^n 。

 **示例:** 

```
输入: 2
输出: 91 
解释: 答案应为除去 11,22,33,44,55,66,77,88,99 外，在 [0,100) 区间内的所有数字。

```
 
**标签**
`数学` `动态规划` `回溯` 


## 
```python

```
>
# 358.K 距离间隔重排字符串
[https://leetcode-cn.com/problems/rearrange-string-k-distance-apart](https://leetcode-cn.com/problems/rearrange-string-k-distance-apart) 
## 原题

 
**标签**
`贪心` `哈希表` `字符串` `计数` `排序` `堆（优先队列）` 


## 
```python

```
>
# 359.日志速率限制器
[https://leetcode-cn.com/problems/logger-rate-limiter](https://leetcode-cn.com/problems/logger-rate-limiter) 
## 原题

 
**标签**
`设计` `哈希表` 


## 
```python

```
>
# 360.有序转化数组
[https://leetcode-cn.com/problems/sort-transformed-array](https://leetcode-cn.com/problems/sort-transformed-array) 
## 原题

 
**标签**
`数组` `数学` `双指针` `排序` 


## 
```python

```
>
# 361.轰炸敌人
[https://leetcode-cn.com/problems/bomb-enemy](https://leetcode-cn.com/problems/bomb-enemy) 
## 原题

 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 362.敲击计数器
[https://leetcode-cn.com/problems/design-hit-counter](https://leetcode-cn.com/problems/design-hit-counter) 
## 原题

 
**标签**
`设计` `队列` `数组` `哈希表` `二分查找` 


## 
```python

```
>
# 363.矩形区域不超过 K 的最大数值和
[https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k](https://leetcode-cn.com/problems/max-sum-of-rectangle-no-larger-than-k) 
## 原题
给你一个 `m x n` 的矩阵 `matrix` 和一个整数 `k` ，找出并返回矩阵内部矩形区域的不超过 `k` 的最大数值和。

题目数据保证总会存在一个数值和不超过 `k` 的矩形区域。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/18/sum-grid.jpg" style="width: 255px; height: 176px;" />
```

输入：matrix = [[1,0,1],[0,-2,3]], k = 2
输出：2
解释：蓝色边框圈出来的矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。

```
 **示例 2：** 

```

输入：matrix = [[2,2,-1]], k = 3
输出：3

```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m, n <= 100` 
-  `-100 <= matrix[i][j] <= 100` 
-  `-10^5 <= k <= 10^5` 
 

 **进阶：** 如果行数远大于列数，该如何设计解决方案？

 
**标签**
`数组` `二分查找` `动态规划` `矩阵` `有序集合` 


## 
```python

```
>
# 364.加权嵌套序列和 II
[https://leetcode-cn.com/problems/nested-list-weight-sum-ii](https://leetcode-cn.com/problems/nested-list-weight-sum-ii) 
## 原题

 
**标签**
`栈` `深度优先搜索` `广度优先搜索` 


## 
```python

```
>
# 365.水壶问题
[https://leetcode-cn.com/problems/water-and-jug-problem](https://leetcode-cn.com/problems/water-and-jug-problem) 
## 原题
有两个水壶，容量分别为 `jug1Capacity` 和 `jug2Capacity` 升。水的供应是无限的。确定是否有可能使用这两个壶准确得到 `targetCapacity` 升。

如果可以得到 `targetCapacity` 升水，最后请用以上水壶中的一或两个来盛放取得的 `targetCapacity` 升水。

你可以：
- 装满任意一个水壶
- 清空任意一个水壶
- 从一个水壶向另外一个水壶倒水，直到装满或者倒空
 

 **示例 1:** 

```

输入: jug1Capacity = 3, jug2Capacity = 5, targetCapacity = 4
输出: true
解释：来自著名的 <a href="https://www.youtube.com/watch?v=BVtQNK_ZUJg">"Die Hard"
```
 **示例 2:** 

```

输入: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
输出: false

```
 **示例 3:** 

```

输入: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
输出: true

```
 

 **提示:** 
-  `1 <= jug1Capacity, jug2Capacity, targetCapacity <= 10^6` 
 
**标签**
`深度优先搜索` `广度优先搜索` `数学` 


## 
```python

```
>
# 366.寻找二叉树的叶子节点
[https://leetcode-cn.com/problems/find-leaves-of-binary-tree](https://leetcode-cn.com/problems/find-leaves-of-binary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 367.有效的完全平方数
[https://leetcode-cn.com/problems/valid-perfect-square](https://leetcode-cn.com/problems/valid-perfect-square) 
## 原题
给定一个 **正整数** `num` ，编写一个函数，如果 `num` 是一个完全平方数，则返回 `true` ，否则返回 `false` 。

 **进阶：不要** 使用任何内置的库函数，如  `sqrt` 。

 

 **示例 1：** 

```

输入：num = 16
输出：true

```
 **示例 2：** 

```

输入：num = 14
输出：false

```
 

 **提示：** 
-  `1 <= num <= 2^31 - 1` 
 
**标签**
`数学` `二分查找` 


## 
```python

```
>
# 368.最大整除子集
[https://leetcode-cn.com/problems/largest-divisible-subset](https://leetcode-cn.com/problems/largest-divisible-subset) 
## 原题
给你一个由 **无重复** 正整数组成的集合 `nums` ，请你找出并返回其中最大的整除子集 `answer` ，子集中每一元素对 `(answer[i], answer[j])` 都应当满足：

-  `answer[i] % answer[j] == 0` ，或
-  `answer[j] % answer[i] == 0` 
如果存在多个有效解子集，返回其中任何一个均可。

 

 **示例 1：** 

```

输入：nums = [1,2,3]
输出：[1,2]
解释：[1,3] 也会被视为正确答案。

```
 **示例 2：** 

```

输入：nums = [1,2,4,8]
输出：[1,2,4,8]

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `1 <= nums[i] <= 2 * 10^9` 
-  `nums` 中的所有整数 **互不相同** 
 
**标签**
`数组` `数学` `动态规划` `排序` 


## 
```python

```
>
# 369.给单链表加一
[https://leetcode-cn.com/problems/plus-one-linked-list](https://leetcode-cn.com/problems/plus-one-linked-list) 
## 原题

 
**标签**
`链表` `数学` 


## 
```python

```
>
# 370.区间加法
[https://leetcode-cn.com/problems/range-addition](https://leetcode-cn.com/problems/range-addition) 
## 原题

 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 371.两整数之和
[https://leetcode-cn.com/problems/sum-of-two-integers](https://leetcode-cn.com/problems/sum-of-two-integers) 
## 原题
给你两个整数 `a` 和 `b` ， **不使用** 运算符 `+` 和 `-` ​​​​​​​，计算并返回两整数之和。

 

 **示例 1：** 

```

输入：a = 1, b = 2
输出：3

```
 **示例 2：** 

```

输入：a = 2, b = 3
输出：5

```
 

 **提示：** 
-  `-1000 <= a, b <= 1000` 
 
**标签**
`位运算` `数学` 


## 
```python

```
>
# 372.超级次方
[https://leetcode-cn.com/problems/super-pow](https://leetcode-cn.com/problems/super-pow) 
## 原题
你的任务是计算  `a^b`  对  `1337` 取模， `a` 是一个正整数， `b` 是一个非常大的正整数且会以数组形式给出。

 

 **示例 1：** 

```

输入：a = 2, b = [3]
输出：8

```
 **示例 2：** 

```

输入：a = 2, b = [1,0]
输出：1024

```
 **示例 3：** 

```

输入：a = 1, b = [4,3,3,8,5,2]
输出：1

```
 **示例 4：** 

```

输入：a = 2147483647, b = [2,0,0]
输出：1198

```
 

 **提示：** 
-  `1 <= a <= 2^31 - 1` 
-  `1 <= b.length <= 2000` 
-  `0 <= b[i] <= 9` 
-  `b` 不含前导 0
 
**标签**
`数学` `分治` 


## 
```python

```
>
# 373.查找和最小的 K 对数字
[https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums](https://leetcode-cn.com/problems/find-k-pairs-with-smallest-sums) 
## 原题
给定两个以 **升序排列** 的整数数组 `nums1` 和 **** `nums2` **** , 以及一个整数 `k` **** 。

定义一对值 `(u,v)` ，其中第一个元素来自 `nums1` ，第二个元素来自 `nums2` **** 。

请找到和最小的 `k` 个数对 `(u<sub>1</sub>,v<sub>1</sub>)` , `(u<sub>2</sub>,v<sub>2</sub>)` ... `(u<sub>k</sub>,v<sub>k</sub>)` 。

 

 **示例 1:** 

```

输入: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
输出: [1,2],[1,4],[1,6]
解释: 返回序列中的前 3 对数：
     [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

```
 **示例 2:** 

```

输入: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
输出: [1,1],[1,1]
解释: 返回序列中的前 2 对数：
     [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

```
 **示例 3:** 

```

输入: nums1 = [1,2], nums2 = [3], k = 3 
输出: [1,3],[2,3]
解释: 也可能序列中所有的数对都被返回:[1,3],[2,3]

```
 

 **提示:** 
-  `1 <= nums1.length, nums2.length <= 10^5` 
-  `-10^9 <= nums1[i], nums2[i] <= 10^9` 
-  `nums1` 和 `nums2` 均为升序排列
-  `1 <= k <= 1000` 
 
**标签**
`数组` `堆（优先队列）` 


## 
```python

```
>
# 374.猜数字大小
[https://leetcode-cn.com/problems/guess-number-higher-or-lower](https://leetcode-cn.com/problems/guess-number-higher-or-lower) 
## 原题
猜数字游戏的规则如下：
- 每轮游戏，我都会从  **1**  到  ***n*** 随机选择一个数字。 请你猜选出的是哪个数字。
- 如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 `int guess(int num)` 来获取猜测结果，返回值一共有 3 种可能的情况（ `-1` ， `1`  或 `0` ）：
- -1：我选出的数字比你猜的数字小 `pick < num` 
- 1：我选出的数字比你猜的数字大 `pick > num` 
- 0：我选出的数字和你猜的数字一样。恭喜！你猜对了！ `pick == num` 
返回我选出的数字。

 

 **示例 1：** 

```

输入：n = 10, pick = 6
输出：6

```
 **示例 2：** 

```

输入：n = 1, pick = 1
输出：1

```
 **示例 3：** 

```

输入：n = 2, pick = 1
输出：1

```
 **示例 4：** 

```

输入：n = 2, pick = 2
输出：2

```
 

 **提示：** 
-  `1 <= n <= 2^31 - 1` 
-  `1 <= pick <= n` 
 
**标签**
`二分查找` `交互` 


## 
```python

```
>
# 375.猜数字大小 II
[https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii](https://leetcode-cn.com/problems/guess-number-higher-or-lower-ii) 
## 原题
我们正在玩一个猜数游戏，游戏规则如下：
- 我从 `1` **** 到 `n` 之间选择一个数字。
- 你来猜我选了哪个数字。
- 如果你猜到正确的数字，就会 **赢得游戏** 。
- 如果你猜错了，那么我会告诉你，我选的数字比你的 **更大或者更小** ，并且你需要继续猜数。
- 每当你猜了数字 `x` 并且猜错了的时候，你需要支付金额为 `x` 的现金。如果你花光了钱，就会 **输掉游戏** 。
给你一个特定的数字 `n` ，返回能够 **确保你获胜** 的最小现金数， **不管我选择那个数字** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/10/graph.png" style="width: 505px; height: 388px;" />
```

输入：n = 10
输出：16
解释：制胜策略如下：
- 数字范围是 [1,10] 。你先猜测数字为 7 。
    - 如果这是我选中的数字，你的总费用为 $0 。否则，你需要支付 $7 。
    - 如果我的数字更大，则下一步需要猜测的数字范围是 [8,10] 。你可以猜测数字为 9 。
        - 如果这是我选中的数字，你的总费用为 $7 。否则，你需要支付 $9 。
        - 如果我的数字更大，那么这个数字一定是 10 。你猜测数字为 10 并赢得游戏，总费用为 $7 + $9 = $16 。
        - 如果我的数字更小，那么这个数字一定是 8 。你猜测数字为 8 并赢得游戏，总费用为 $7 + $9 = $16 。
    - 如果我的数字更小，则下一步需要猜测的数字范围是 [1,6] 。你可以猜测数字为 3 。
        - 如果这是我选中的数字，你的总费用为 $7 。否则，你需要支付 $3 。
        - 如果我的数字更大，则下一步需要猜测的数字范围是 [4,6] 。你可以猜测数字为 5 。
            - 如果这是我选中的数字，你的总费用为 $7 + $3 = $10 。否则，你需要支付 $5 。
            - 如果我的数字更大，那么这个数字一定是 6 。你猜测数字为 6 并赢得游戏，总费用为 $7 + $3 + $5 = $15 。
            - 如果我的数字更小，那么这个数字一定是 4 。你猜测数字为 4 并赢得游戏，总费用为 $7 + $3 + $5 = $15 。
        - 如果我的数字更小，则下一步需要猜测的数字范围是 [1,2] 。你可以猜测数字为 1 。
            - 如果这是我选中的数字，你的总费用为 $7 + $3 = $10 。否则，你需要支付 $1 。
            - 如果我的数字更大，那么这个数字一定是 2 。你猜测数字为 2 并赢得游戏，总费用为 $7 + $3 + $1 = $11 。
在最糟糕的情况下，你需要支付 $16 。因此，你只需要 $16 就可以确保自己赢得游戏。

```
 **示例 2：** 

```

输入：n = 1
输出：0
解释：只有一个可能的数字，所以你可以直接猜 1 并赢得游戏，无需支付任何费用。

```
 **示例 3：** 

```

输入：n = 2
输出：1
解释：有两个可能的数字 1 和 2 。
- 你可以先猜 1 。
    - 如果这是我选中的数字，你的总费用为 $0 。否则，你需要支付 $1 。
    - 如果我的数字更大，那么这个数字一定是 2 。你猜测数字为 2 并赢得游戏，总费用为 $1 。
最糟糕的情况下，你需要支付 $1 。

```
 

 **提示：** 
-  `1 <= n <= 200` 
 
**标签**
`数学` `动态规划` `博弈` 


## 
```python

```
>
# 376.摆动序列
[https://leetcode-cn.com/problems/wiggle-subsequence](https://leetcode-cn.com/problems/wiggle-subsequence) 
## 原题
如果连续数字之间的差严格地在正数和负数之间交替，则数字序列称为 **摆动序列 。** 第一个差（如果存在的话）可能是正数或负数。仅有一个元素或者含两个不等元素的序列也视作摆动序列。
- 
	例如，  `[1, 7, 4, 9, 2, 5]` 是一个 **摆动序列** ，因为差值 `(6, -3, 5, -7, 3)`  是正负交替出现的。
	
- 相反， `[1, 4, 7, 2, 5]`  和  `[1, 7, 4, 5, 5]` 不是摆动序列，第一个序列是因为它的前两个差值都是正数，第二个序列是因为它的最后一个差值为零。
 **子序列** 可以通过从原始序列中删除一些（也可以不删除）元素来获得，剩下的元素保持其原始顺序。

给你一个整数数组 `nums` ，返回 `nums` 中作为 **摆动序列** 的 **最长子序列的长度** 。

 

 **示例 1：** 

```

输入：nums = [1,7,4,9,2,5]
输出：6
解释：整个序列均为摆动序列，各元素之间的差值为 (6, -3, 5, -7, 3) 。

```
 **示例 2：** 

```

输入：nums = [1,17,5,10,13,15,10,5,16,8]
输出：7
解释：这个序列包含几个长度为 7 摆动序列。
其中一个是 [1, 17, 10, 13, 10, 16, 8] ，各元素之间的差值为 (16, -7, 3, -3, 6, -8) 。

```
 **示例 3：** 

```

输入：nums = [1,2,3,4,5,6,7,8,9]
输出：2

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `0 <= nums[i] <= 1000` 
 

 **进阶：** 你能否用  `O(n)` 时间复杂度完成此题?

 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 377.组合总和 Ⅳ
[https://leetcode-cn.com/problems/combination-sum-iv](https://leetcode-cn.com/problems/combination-sum-iv) 
## 原题
给你一个由 **不同** 整数组成的数组 `nums` ，和一个目标整数 `target` 。请你从 `nums` 中找出并返回总和为 `target` 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

 

 **示例 1：** 

```

输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。

```
 **示例 2：** 

```

输入：nums = [9], target = 3
输出：0

```
 

 **提示：** 
-  `1 <= nums.length <= 200` 
-  `1 <= nums[i] <= 1000` 
-  `nums` 中的所有元素 **互不相同** 
-  `1 <= target <= 1000` 
 

 **进阶：** 如果给定的数组中含有负数会发生什么？问题会产生何种变化？如果允许负数出现，需要向题目中添加哪些限制条件？

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 378.有序矩阵中第 K 小的元素
[https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix](https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix) 
## 原题
给你一个 `n x n` 矩阵 `matrix` ，其中每行和每列元素均按升序排序，找到矩阵中第 `k` 小的元素。<br />
请注意，它是 **排序后** 的第 `k` 小元素，而不是第 `k` 个 **不同** 的元素。

你必须找到一个内存复杂度优于 `O(n^2)` 的解决方案。

 

 **示例 1：** 

```

输入：matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
输出：13
解释：矩阵中的元素为 [1,5,9,10,11,12,13,13,15]，第 8 小元素是 13

```
 **示例 2：** 

```

输入：matrix = [[-5]], k = 1
输出：-5

```
 

 **提示：** 
-  `n == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= n <= 300` 
-  `-10^9 <= matrix[i][j] <= 10^9` 
- 题目数据 **保证** `matrix` 中的所有行和列都按 **非递减顺序** 排列
-  `1 <= k <= n^2` 
 

 **进阶：** 
- 你能否用一个恒定的内存(即 `O(1)` 内存复杂度)来解决这个问题?
- 你能在 `O(n)` 的时间复杂度下解决这个问题吗?这个方法对于面试来说可能太超前了，但是你会发现阅读这篇文章（ <a href="http://www.cse.yorku.ca/~andy/pubs/X+Y.pdf" target="_blank">this paper</a> ）很有趣。
 
**标签**
`数组` `二分查找` `矩阵` `排序` `堆（优先队列）` 


## 
```python

```
>
# 379.电话目录管理系统
[https://leetcode-cn.com/problems/design-phone-directory](https://leetcode-cn.com/problems/design-phone-directory) 
## 原题

 
**标签**
`设计` `队列` `数组` `哈希表` `链表` 


## 
```python

```
>
# 380.O(1) 时间插入、删除和获取随机元素
[https://leetcode-cn.com/problems/insert-delete-getrandom-o1](https://leetcode-cn.com/problems/insert-delete-getrandom-o1) 
## 原题
实现 `RandomizedSet` 类：
-  `RandomizedSet()` 初始化 `RandomizedSet` 对象
-  `bool insert(int val)` 当元素 `val` 不存在时，向集合中插入该项，并返回 `true` ；否则，返回 `false` 。
-  `bool remove(int val)` 当元素 `val` 存在时，从集合中移除该项，并返回 `true` ；否则，返回 `false` 。
-  `int getRandom()` 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 **相同的概率** 被返回。
你必须实现类的所有函数，并满足每个函数的 **平均** 时间复杂度为 `O(1)` 。

 

 **示例：** 

```

输入
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
输出
[null, true, false, true, 2, true, false, 2]

解释
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // 向集合中插入 1 。返回 true 表示 1 被成功地插入。
randomizedSet.remove(2); // 返回 false ，表示集合中不存在 2 。
randomizedSet.insert(2); // 向集合中插入 2 。返回 true 。集合现在包含 [1,2] 。
randomizedSet.getRandom(); // getRandom 应随机返回 1 或 2 。
randomizedSet.remove(1); // 从集合中移除 1 ，返回 true 。集合现在包含 [2] 。
randomizedSet.insert(2); // 2 已在集合中，所以返回 false 。
randomizedSet.getRandom(); // 由于 2 是集合中唯一的数字，getRandom 总是返回 2 。

```
 

 **提示：** 
-  `-2^31 <= val <= 2^31 - 1` 
- 最多调用 `insert` 、 `remove` 和 `getRandom` 函数 `2 *` `10^5` 次
- 在调用 `getRandom` 方法时，数据结构中 **至少存在一个** 元素。
 
**标签**
`设计` `数组` `哈希表` `数学` `随机化` 


## 
```python

```
>
# 381.O(1) 时间插入、删除和获取随机元素 - 允许重复
[https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed](https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed) 
## 原题
 `RandomizedCollection` 是一种包含数字集合(可能是重复的)的数据结构。它应该支持插入和删除特定元素，以及删除随机元素。

实现 `RandomizedCollection` 类:
-  `RandomizedCollection()` 初始化空的 `RandomizedCollection` 对象。
-  `bool insert(int val)` 将一个 `val` 项插入到集合中，即使该项已经存在。如果该项不存在，则返回 `true` ，否则返回 `false` 。
-  `bool remove(int val)` 如果存在，从集合中移除一个 `val` 项。如果该项存在，则返回 `true` ，否则返回 `false` 。注意，如果 `val` 在集合中出现多次，我们只删除其中一个。
-  `int getRandom()` 从当前的多个元素集合中返回一个随机元素。每个元素被返回的概率与集合中包含的相同值的数量 **线性相关** 。
您必须实现类的函数，使每个函数的 **平均** 时间复杂度为 `O(1)` 。

 **注意：** 生成测试用例时，只有在 `RandomizedCollection` 中 **至少有一项** 时，才会调用 `getRandom` 。

 

 **示例 1:** 

```

输入
["RandomizedCollection", "insert", "insert", "insert", "getRandom", "remove", "getRandom"]
[[], [1], [1], [2], [], [1], []]
输出
[null, true, false, true, 2, true, 1]

解释
RandomizedCollection collection = new RandomizedCollection();// 初始化一个空的集合。
collection.insert(1);// 向集合中插入 1 。返回 true 表示集合不包含 1 。
collection.insert(1);// 向集合中插入另一个 1 。返回 false 表示集合包含 1 。集合现在包含 [1,1] 。
collection.insert(2);// 向集合中插入 2 ，返回 true 。集合现在包含 [1,1,2] 。
collection.getRandom();// getRandom 应当有 2/3 的概率返回 1 ，1/3 的概率返回 2 。
collection.remove(1);// 从集合中删除 1 ，返回 true 。集合现在包含 [1,2] 。
collection.getRandom();// getRandom 应有相同概率返回 1 和 2 。

```
 

 **提示:** 
-  `-2^31 <= val <= 2^31 - 1` 
-  `insert` , `remove` 和 `getRandom` 最多 **总共** 被调用 `2 * 10^5` 次
- 当调用 `getRandom` 时，数据结构中 **至少有一个** 元素
 
**标签**
`设计` `数组` `哈希表` `数学` `随机化` 


## 
```python

```
>
# 382.链表随机节点
[https://leetcode-cn.com/problems/linked-list-random-node](https://leetcode-cn.com/problems/linked-list-random-node) 
## 原题
给你一个单链表，随机选择链表的一个节点，并返回相应的节点值。每个节点 **被选中的概率一样** 。

实现 `Solution` 类：
-  `Solution(ListNode head)` 使用整数数组初始化对象。
-  `int getRandom()` 从链表中随机选择一个节点并返回该节点的值。链表中所有节点被选中的概率相等。
 

 **示例：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/16/getrand-linked-list.jpg" style="width: 302px; height: 62px;" />
```

输入
["Solution", "getRandom", "getRandom", "getRandom", "getRandom", "getRandom"]
[[[1, 2, 3]], [], [], [], [], []]
输出
[null, 1, 3, 2, 2, 3]

解释
Solution solution = new Solution([1, 2, 3]);
solution.getRandom(); // 返回 1
solution.getRandom(); // 返回 3
solution.getRandom(); // 返回 2
solution.getRandom(); // 返回 2
solution.getRandom(); // 返回 3
// getRandom() 方法应随机返回 1、2、3中的一个，每个元素被返回的概率相等。
```
 

 **提示：** 
- 链表中的节点数在范围 `[1, 10^4]` 内
-  `-10^4 <= Node.val <= 10^4` 
- 至多调用 `getRandom` 方法 `10^4` 次
 

 **进阶：** 
- 如果链表非常大且长度未知，该怎么处理？
- 你能否在不使用额外空间的情况下解决此问题？
 
**标签**
`水塘抽样` `链表` `数学` `随机化` 


## 
```python

```
>
# 383.赎金信
[https://leetcode-cn.com/problems/ransom-note](https://leetcode-cn.com/problems/ransom-note) 
## 原题
给你两个字符串： `ransomNote` 和 `magazine` ，判断 `ransomNote` 能不能由 `magazine` 里面的字符构成。

如果可以，返回 `true` ；否则返回 `false` 。

 `magazine` 中的每个字符只能在 `ransomNote` 中使用一次。

 

 **示例 1：** 

```

输入：ransomNote = "a", magazine = "b"
输出：false

```
 **示例 2：** 

```

输入：ransomNote = "aa", magazine = "ab"
输出：false

```
 **示例 3：** 

```

输入：ransomNote = "aa", magazine = "aab"
输出：true

```
 

 **提示：** 
-  `1 <= ransomNote.length, magazine.length <= 10^5` 
-  `ransomNote` 和 `magazine` 由小写英文字母组成
 
**标签**
`哈希表` `字符串` `计数` 


## 
```python

```
>
# 384.打乱数组
[https://leetcode-cn.com/problems/shuffle-an-array](https://leetcode-cn.com/problems/shuffle-an-array) 
## 原题
给你一个整数数组 `nums` ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是 **等可能** 的。

实现 `Solution` class:
-  `Solution(int[] nums)` 使用整数数组 `nums` 初始化对象
-  `int[] reset()` 重设数组到它的初始状态并返回
-  `int[] shuffle()` 返回数组随机打乱后的结果
 

 **示例 1：** 

```

输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]

```
 

 **提示：** 
-  `1 <= nums.length <= 200` 
-  `-10^6 <= nums[i] <= 10^6` 
-  `nums` 中的所有元素都是 **唯一的** 
- 最多可以调用 `5 * 10^4` 次 `reset` 和 `shuffle` 
 
**标签**
`数组` `数学` `随机化` 


## 
```python

```
>
# 385.迷你语法分析器
[https://leetcode-cn.com/problems/mini-parser](https://leetcode-cn.com/problems/mini-parser) 
## 原题
给定一个字符串 s 表示一个整数嵌套列表，实现一个解析它的语法分析器并返回解析的结果 `NestedInteger` 。

列表中的每个元素只可能是整数或整数嵌套列表

 

 **示例 1：** 

```

输入：s = "324",
输出：324
解释：你应该返回一个 NestedInteger 对象，其中只包含整数值 324。

```
 **示例 2：** 

```

输入：s = "[123,[456,[789]]]",
输出：[123,[456,[789]]]
解释：返回一个 NestedInteger 对象包含一个有两个元素的嵌套列表：
1. 一个 integer 包含值 123
2. 一个包含两个元素的嵌套列表：
    i.  一个 integer 包含值 456
    ii. 一个包含一个元素的嵌套列表
         a. 一个 integer 包含值 789

```
 

 **提示：** 
-  `1 <= s.length <= 5 * 10^4` 
-  `s` 由数字、方括号 `"[]"` 、负号 `'-'` 、逗号 `','` 组成
- 用例保证 `s` 是可解析的 `NestedInteger` 
- 输入中的所有值的范围是 `[-10^6, 10^6]` 
 
**标签**
`栈` `深度优先搜索` `字符串` 


## 
```python

```
>
# 386.字典序排数
[https://leetcode-cn.com/problems/lexicographical-numbers](https://leetcode-cn.com/problems/lexicographical-numbers) 
## 原题
给你一个整数 `n` ，按字典序返回范围 `[1, n]` 内所有整数。

你必须设计一个时间复杂度为 `O(n)` 且使用 `O(1)` 额外空间的算法。

 

 **示例 1：** 

```

输入：n = 13
输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]

```
 **示例 2：** 

```

输入：n = 2
输出：[1,2]

```
 

 **提示：** 
-  `1 <= n <= 5 * 10^4` 
 
**标签**
`深度优先搜索` `字典树` 


## 
```python

```
>
# 387.字符串中的第一个唯一字符
[https://leetcode-cn.com/problems/first-unique-character-in-a-string](https://leetcode-cn.com/problems/first-unique-character-in-a-string) 
## 原题
给定一个字符串 `s` ，找到 *它的第一个不重复的字符，并返回它的索引* 。如果不存在，则返回 `-1` 。

 

 **示例 1：** 

```

输入: s = "leetcode"
输出: 0

```
 **示例 2:** 

```

输入: s = "loveleetcode"
输出: 2

```
 **示例 3:** 

```

输入: s = "aabb"
输出: -1

```
 

 **提示:** 
-  `1 <= s.length <= 10^5` 
-  `s` 只包含小写字母
 
**标签**
`队列` `哈希表` `字符串` `计数` 


## 
```python

```
>
# 388.文件的最长绝对路径
[https://leetcode-cn.com/problems/longest-absolute-file-path](https://leetcode-cn.com/problems/longest-absolute-file-path) 
## 原题
假设有一个同时存储文件和目录的文件系统。下图展示了文件系统的一个示例：

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mdir.jpg" style="height: 142px; width: 300px;" />

这里将 `dir` 作为根目录中的唯一目录。 `dir` 包含两个子目录 `subdir1` 和 `subdir2` 。 `subdir1` 包含文件 `file1.ext` 和子目录 `subsubdir1` ； `subdir2` 包含子目录 `subsubdir2` ，该子目录下包含文件 `file2.ext` 。

在文本格式中，如下所示(⟶表示制表符)：

```

dir
⟶ subdir1
⟶ ⟶ file1.ext
⟶ ⟶ subsubdir1
⟶ subdir2
⟶ ⟶ subsubdir2
⟶ ⟶ ⟶ file2.ext

```
如果是代码表示，上面的文件系统可以写为 `"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"` 。 `'\n'` 和 `'\t'` 分别是换行符和制表符。

文件系统中的每个文件和文件夹都有一个唯一的 **绝对路径** ，即必须打开才能到达文件/目录所在位置的目录顺序，所有路径用 `'/'` 连接。上面例子中，指向 `file2.ext` 的 **绝对路径** 是 `"dir/subdir2/subsubdir2/file2.ext"` 。每个目录名由字母、数字和/或空格组成，每个文件名遵循 `name.extension` 的格式，其中<meta charset="UTF-8" /> `name` 和<meta charset="UTF-8" /> `extension` 由字母、数字和/或空格组成。

给定一个以上述格式表示文件系统的字符串 `input` ，返回文件系统中 *指向 **文件** 的 **最长绝对路径** 的长度* 。 如果系统中没有文件，返回 `0` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/dir1.jpg" style="height: 101px; width: 200px;" />
```

输入：input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
输出：20
解释：只有一个文件，绝对路径为 "dir/subdir2/file.ext" ，路径长度 20

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/dir2.jpg" style="height: 151px; width: 300px;" />
```

输入：input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
输出：32
解释：存在两个文件：
"dir/subdir1/file1.ext" ，路径长度 21
"dir/subdir2/subsubdir2/file2.ext" ，路径长度 32
返回 32 ，因为这是最长的路径
```
 **示例 3：** 

```

输入：input = "a"
输出：0
解释：不存在任何文件
```
 **示例 4：** 

```

输入：input = "file1.txt\nfile2.txt\nlongfile.txt"
输出：12
解释：根目录下有 3 个文件。
因为根目录中任何东西的绝对路径只是名称本身，所以答案是 "longfile.txt" ，路径长度为 12

```
 

 **提示：** 
-  `1 <= input.length <= 10^4` 
-  `input` 可能包含小写或大写的英文字母，一个换行符 `'\n'` ，一个制表符 `'\t'` ，一个点 `'.'` ，一个空格 `' '` ，和数字。
 
**标签**
`栈` `深度优先搜索` `字符串` 


## 
```python

```
>
# 389.找不同
[https://leetcode-cn.com/problems/find-the-difference](https://leetcode-cn.com/problems/find-the-difference) 
## 原题
给定两个字符串 `s` 和 `t` ，它们只包含小写字母。

字符串 `t` 由字符串 `s` 随机重排，然后在随机位置添加一个字母。

请找出在 `t` 中被添加的字母。

 

 **示例 1：** 

```

输入：s = "abcd", t = "abcde"
输出："e"
解释：'e' 是那个被添加的字母。

```
 **示例 2：** 

```

输入：s = "", t = "y"
输出："y"

```
 

 **提示：** 
-  `0 <= s.length <= 1000` 
-  `t.length == s.length + 1` 
-  `s` 和 `t` 只包含小写字母
 
**标签**
`位运算` `哈希表` `字符串` `排序` 


## 
```python

```
>
# 390.消除游戏
[https://leetcode-cn.com/problems/elimination-game](https://leetcode-cn.com/problems/elimination-game) 
## 原题
列表 `arr` 由在范围 `[1, n]` 中的所有整数组成，并按严格递增排序。请你对 `arr` 应用下述算法：
- 从左到右，删除第一个数字，然后每隔一个数字删除一个，直到到达列表末尾。
- 重复上面的步骤，但这次是从右到左。也就是，删除最右侧的数字，然后剩下的数字每隔一个删除一个。
- 不断重复这两步，从左到右和从右到左交替进行，直到只剩下一个数字。
给你整数 `n` ，返回 `arr` 最后剩下的数字。

 

 **示例 1：** 

```

输入：n = 9
输出：6
解释：
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = [2, 4, 6, 8]
arr = [2, 6]
arr = [6]

```
 **示例 2：** 

```

输入：n = 1
输出：1

```
 

 **提示：** 
-  `1 <= n <= 10^9` 
 
**标签**
`数学` 


## 
```python

```
>
# 391.完美矩形
[https://leetcode-cn.com/problems/perfect-rectangle](https://leetcode-cn.com/problems/perfect-rectangle) 
## 原题
给你一个数组 `rectangles` ，其中 `rectangles[i] = [x<sub>i</sub>, y<sub>i</sub>, a<sub>i</sub>, b<sub>i</sub>]` 表示一个坐标轴平行的矩形。这个矩形的左下顶点是 `(x<sub>i</sub>, y<sub>i</sub>)` ，右上顶点是 `(a<sub>i</sub>, b<sub>i</sub>)` 。

如果所有矩形一起精确覆盖了某个矩形区域，则返回 `true` ；否则，返回 `false` 。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/perectrec1-plane.jpg" style="width: 300px; height: 294px;" />
```

输入：rectangles = [[1,1,3,3],[3,1,4,2],[3,2,4,4],[1,3,2,4],[2,3,3,4]]
输出：true
解释：5 个矩形一起可以精确地覆盖一个矩形区域。 

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/perfectrec2-plane.jpg" style="width: 300px; height: 294px;" />
```

输入：rectangles = [[1,1,2,3],[1,3,2,4],[3,1,4,2],[3,2,4,4]]
输出：false
解释：两个矩形之间有间隔，无法覆盖成一个矩形。
```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/perfectrec3-plane.jpg" style="width: 300px; height: 294px;" />
```

输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[3,2,4,4]]
输出：false
解释：图形顶端留有空缺，无法覆盖成一个矩形。
```
 **示例 4：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/27/perfecrrec4-plane.jpg" style="width: 300px; height: 294px;" />
```

输入：rectangles = [[1,1,3,3],[3,1,4,2],[1,3,2,4],[2,2,4,4]]
输出：false
解释：因为中间有相交区域，虽然形成了矩形，但不是精确覆盖。
```
 

 **提示：** 
-  `1 <= rectangles.length <= 2 * 10^4` 
-  `rectangles[i].length == 4` 
-  `-10^5 <= x<sub>i</sub>, y<sub>i</sub>, a<sub>i</sub>, b<sub>i</sub> <= 10^5` 
 
**标签**
`数组` `扫描线` 


## 
```python

```
>
# 392.判断子序列
[https://leetcode-cn.com/problems/is-subsequence](https://leetcode-cn.com/problems/is-subsequence) 
## 原题
给定字符串 **s** 和 **t** ，判断 **s** 是否为 **t** 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如， `"ace"` 是 `"abcde"` 的一个子序列，而 `"aec"` 不是）。

 **进阶：** 

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

 **致谢：** 

特别感谢 **** <a href="https://leetcode.com/pbrother/">@pbrother </a>添加此问题并且创建所有测试用例。

 

 **示例 1：** 

```

输入：s = "abc", t = "ahbgdc"
输出：true

```
 **示例 2：** 

```

输入：s = "axc", t = "ahbgdc"
输出：false

```
 

 **提示：** 
-  `0 <= s.length <= 100` 
-  `0 <= t.length <= 10^4` 
- 两个字符串都只由小写字符组成。
 
**标签**
`双指针` `字符串` `动态规划` 


## 
```python

```
>
# 393.UTF-8 编码验证
[https://leetcode-cn.com/problems/utf-8-validation](https://leetcode-cn.com/problems/utf-8-validation) 
## 原题
给定一个表示数据的整数数组 `data` ，返回它是否为有效的 **UTF-8** 编码。

 **UTF-8** 中的一个字符可能的长度为 **1 到 4 字节** ，遵循以下的规则：
- 对于 **1 字节** 的字符，字节的第一位设为 0 ，后面 7 位为这个符号的 unicode 码。
- 对于 **n 字节** 的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为 0 ，后面字节的前两位一律设为 10 。剩下的没有提及的二进制位，全部为这个符号的 unicode 码。
这是 UTF-8 编码的工作方式：

```

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

```
 **注意：** 输入是整数数组。只有每个整数的 **最低 8 个有效位** 用来存储数据。这意味着每个整数只表示 1 字节的数据。

 

 **示例 1：** 

```

输入：data = [197,130,1]
输出：true
解释：数据表示字节序列:11000101 10000010 00000001。
这是有效的 utf-8 编码，为一个 2 字节字符，跟着一个 1 字节字符。

```
 **示例 2：** 

```

输入：data = [235,140,4]
输出：false
解释：数据表示 8 位的序列: 11101011 10001100 00000100.
前 3 位都是 1 ，第 4 位为 0 表示它是一个 3 字节字符。
下一个字节是开头为 10 的延续字节，这是正确的。
但第二个延续字节不以 10 开头，所以是不符合规则的。

```
 

 **提示:** 
-  `1 <= data.length <= 2 * 10^4` 
-  `0 <= data[i] <= 255` 
 
**标签**
`位运算` `数组` 


## 
```python

```
>
# 394.字符串解码
[https://leetcode-cn.com/problems/decode-string](https://leetcode-cn.com/problems/decode-string) 
## 原题
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: `k[encoded_string]` ，表示其中方括号内部的 `encoded_string` 正好重复 `k` 次。注意 `k` 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 `k` ，例如不会出现像 `3a` 或 `2[4]` 的输入。

 

 **示例 1：** 

```

输入：s = "3[a]2[bc]"
输出："aaabcbc"

```
 **示例 2：** 

```

输入：s = "3[a2[c]]"
输出："accaccacc"

```
 **示例 3：** 

```

输入：s = "2[abc]3[cd]ef"
输出："abcabccdcdcdef"

```
 **示例 4：** 

```

输入：s = "abc3[cd]xyz"
输出："abccdcdcdxyz"

```
 

 **提示：** 
-  `1 <= s.length <= 30` 
- <meta charset="UTF-8" /> `s` 由小写英文字母、数字和方括号<meta charset="UTF-8" /> `'[]'` 组成
-  `s` 保证是一个 **有效** 的输入。
-  `s` 中所有整数的取值范围为<meta charset="UTF-8" /> `[1, 300]` 
 
**标签**
`栈` `递归` `字符串` 


## 
```python

```
>
# 395.至少有 K 个重复字符的最长子串
[https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters](https://leetcode-cn.com/problems/longest-substring-with-at-least-k-repeating-characters) 
## 原题
给你一个字符串 `s` 和一个整数 `k` ，请你找出 `s` 中的最长子串， 要求该子串中的每一字符出现次数都不少于 `k` 。返回这一子串的长度。

 

 **示例 1：** 

```

输入：s = "aaabb", k = 3
输出：3
解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。

```
 **示例 2：** 

```

输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
```
 

 **提示：** 
-  `1 <= s.length <= 10^4` 
-  `s` 仅由小写英文字母组成
-  `1 <= k <= 10^5` 
 
**标签**
`哈希表` `字符串` `分治` `滑动窗口` 


## 
```python

```
>
# 396.旋转函数
[https://leetcode-cn.com/problems/rotate-function](https://leetcode-cn.com/problems/rotate-function) 
## 原题
给定一个长度为 `n` 的整数数组 `nums` 。

假设 `arr<sub>k</sub>` 是数组 `nums` 顺时针旋转 `k` 个位置后的数组，我们定义 `nums` 的 **旋转函数** `F` 为：
-  `F(k) = 0 * arr<sub>k</sub>[0] + 1 * arr<sub>k</sub>[1] + ... + (n - 1) * arr<sub>k</sub>[n - 1]` 
返回 *`F(0), F(1), ..., F(n-1)` 中的最大值* 。

生成的测试用例让答案符合 **32 位** 整数。

 

 **示例 1:** 

```

输入: nums = [4,3,2,6]
输出: 26
解释:
F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26
所以 F(0), F(1), F(2), F(3) 中的最大值是 F(3) = 26 。

```
 **示例 2:** 

```

输入: nums = [100]
输出: 0

```
 

 **提示:** 
-  `n == nums.length` 
-  `1 <= n <= 10^5` 
-  `-100 <= nums[i] <= 100` 
 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 397.整数替换
[https://leetcode-cn.com/problems/integer-replacement](https://leetcode-cn.com/problems/integer-replacement) 
## 原题
给定一个正整数 `n` ，你可以做如下操作：
- 如果 `n` 是偶数，则用 `n / 2` 替换 `n` 。
- 如果 `n` 是奇数，则可以用 `n + 1` 或 `n - 1` 替换 `n` 。
返回 `n` 变为 `1` 所需的 *最小替换次数* 。

 

 **示例 1：** 

```

输入：n = 8
输出：3
解释：8 -> 4 -> 2 -> 1

```
 **示例 2：** 

```

输入：n = 7
输出：4
解释：7 -> 8 -> 4 -> 2 -> 1
或 7 -> 6 -> 3 -> 2 -> 1

```
 **示例 3：** 

```

输入：n = 4
输出：2

```
 

 **提示：** 
-  `1 <= n <= 2^31 - 1` 
 
**标签**
`贪心` `位运算` `记忆化搜索` `动态规划` 


## 
```python

```
>
# 398.随机数索引
[https://leetcode-cn.com/problems/random-pick-index](https://leetcode-cn.com/problems/random-pick-index) 
## 原题
给定一个可能含有重复元素的整数数组，要求随机输出给定的数字的索引。 您可以假设给定的数字一定存在于数组中。

 **注意：** <br />
数组大小可能非常大。 使用太多额外空间的解决方案将不会通过测试。

 **示例:** 

```

int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) 应该返回索引 2,3 或者 4。每个索引的返回概率应该相等。
solution.pick(3);

// pick(1) 应该返回 0。因为只有nums[0]等于1。
solution.pick(1);

```
 
**标签**
`水塘抽样` `哈希表` `数学` `随机化` 


## 
```python

```
>
# 399.除法求值
[https://leetcode-cn.com/problems/evaluate-division](https://leetcode-cn.com/problems/evaluate-division) 
## 原题
给你一个变量对数组 `equations` 和一个实数值数组 `values` 作为已知条件，其中 `equations[i] = [A<sub>i</sub>, B<sub>i</sub>]` 和 `values[i]` 共同表示等式 `A<sub>i</sub> / B<sub>i</sub> = values[i]` 。每个 `A<sub>i</sub>` 或 `B<sub>i</sub>` 是一个表示单个变量的字符串。

另有一些以数组 `queries` 表示的问题，其中 `queries[j] = [C<sub>j</sub>, D<sub>j</sub>]` 表示第 `j` 个问题，请你根据已知条件找出 `C<sub>j</sub> / D<sub>j</sub> = ?` 的结果作为答案。

返回 **所有问题的答案** 。如果存在某个无法确定的答案，则用 `-1.0` 替代这个答案。如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 `-1.0` 替代这个答案。

 **注意：** 输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。

 

 **示例 1：** 

```

输入：equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
输出：[6.00000,0.50000,-1.00000,1.00000,-1.00000]
解释：
条件：a / b = 2.0, b / c = 3.0
问题：a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
结果：[6.0, 0.5, -1.0, 1.0, -1.0 ]

```
 **示例 2：** 

```

输入：equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
输出：[3.75000,0.40000,5.00000,0.20000]

```
 **示例 3：** 

```

输入：equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
输出：[0.50000,2.00000,-1.00000,-1.00000]

```
 

 **提示：** 
-  `1 <= equations.length <= 20` 
-  `equations[i].length == 2` 
-  `1 <= A<sub>i</sub>.length, B<sub>i</sub>.length <= 5` 
-  `values.length == equations.length` 
-  `0.0 < values[i] <= 20.0` 
-  `1 <= queries.length <= 20` 
-  `queries[i].length == 2` 
-  `1 <= C<sub>j</sub>.length, D<sub>j</sub>.length <= 5` 
-  `A<sub>i</sub>, B<sub>i</sub>, C<sub>j</sub>, D<sub>j</sub>` 由小写英文字母与数字组成
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `图` `数组` `最短路` 


## 
```python

```
>
# 400.第 N 位数字
[https://leetcode-cn.com/problems/nth-digit](https://leetcode-cn.com/problems/nth-digit) 
## 原题
给你一个整数 `n` ，请你在无限的整数序列 `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...]` 中找出并返回第 `n` 位上的数字。

 

 **示例 1：** 

```

输入：n = 3
输出：3

```
 **示例 2：** 

```

输入：n = 11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。

```
 

 **提示：** 
-  `1 <= n <= 2^31 - 1` 
 
**标签**
`数学` `二分查找` 


## 
```python

```
>
