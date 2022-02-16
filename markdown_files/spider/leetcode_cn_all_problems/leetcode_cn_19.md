# 1901.找出顶峰元素 II
[https://leetcode-cn.com/problems/find-a-peak-element-ii](https://leetcode-cn.com/problems/find-a-peak-element-ii) 
## 原题
一个 2D 网格中的 **顶峰元素** 是指那些 **严格大于** 其相邻格子(上、下、左、右)的元素。

给你一个 **从 0 开始编号** 的 `m x n` 矩阵 `mat` ，其中任意两个相邻格子的值都 **不相同** 。找出 **任意一个** 顶峰元素 `mat[i][j]` 并 **返回其位置** `[i,j]` 。

你可以假设整个矩阵周边环绕着一圈值为 `-1` 的格子。

要求必须写出时间复杂度为 `O(m log(n))` 或 `O(n log(m))` 的算法

 

 

 **示例 1:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/1.png" style="width: 206px; height: 209px;" />

```

输入: mat = [[1,4],[3,2]]
输出: [0,1]
解释: 3和4都是顶峰元素，所以[1,0]和[0,1]都是可接受的答案。

```
 **示例 2:** 

 **<img alt="" src="https://assets.leetcode.com/uploads/2021/06/07/3.png" style="width: 254px; height: 257px;" />** 

```

输入: mat = [[10,20,15],[21,30,14],[7,16,32]]
输出: [1,1]
解释: 30和32都是顶峰元素，所以[1,1]和[2,2]都是可接受的答案。

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat[i].length` 
-  `1 <= m, n <= 500` 
-  `1 <= mat[i][j] <= 10^5` 
- 任意两个相邻元素均不相等.
 
**标签**
`数组` `二分查找` `分治` `矩阵` 


## 
```python

```
>
# 1902.给定二叉搜索树的插入顺序求深度
[https://leetcode-cn.com/problems/depth-of-bst-given-insertion-order](https://leetcode-cn.com/problems/depth-of-bst-given-insertion-order) 
## 原题

 
**标签**
`树` `二叉搜索树` `二叉树` `有序集合` 


## 
```python

```
>
# 1903.字符串中的最大奇数
[https://leetcode-cn.com/problems/largest-odd-number-in-string](https://leetcode-cn.com/problems/largest-odd-number-in-string) 
## 原题
给你一个字符串 `num` ，表示一个大整数。请你在字符串 `num` 的所有  **非空子字符串** 中找出 **值最大的奇数** ，并以字符串形式返回。如果不存在奇数，则返回一个空字符串 `""` 。

 **子字符串** 是字符串中的一个连续的字符序列。

 

 **示例 1：** 

```

输入：num = "52"
输出："5"
解释：非空子字符串仅有 "5"、"2" 和 "52" 。"5" 是其中唯一的奇数。

```
 **示例 2：** 

```

输入：num = "4206"
输出：""
解释：在 "4206" 中不存在奇数。

```
 **示例 3：** 

```

输入：num = "35427"
输出："35427"
解释："35427" 本身就是一个奇数。

```
 

 **提示：** 
-  `1 <= num.length <= 10^5` 
-  `num` 仅由数字组成且不含前导零
 
**标签**
`贪心` `数学` `字符串` 


## 
```python

```
>
# 1904.你完成的完整对局数
[https://leetcode-cn.com/problems/the-number-of-full-rounds-you-have-played](https://leetcode-cn.com/problems/the-number-of-full-rounds-you-have-played) 
## 原题
一款新的在线电子游戏在近期发布，在该电子游戏中，以 **刻钟** 为周期规划若干时长为 **15 分钟** 的游戏对局。这意味着，在 `HH:00` 、 `HH:15` 、 `HH:30` 和 `HH:45` ，将会开始一个新的对局，其中 `HH` 用一个从 `00` 到 `23` 的整数表示。游戏中使用 **24 小时制的时钟** ，所以一天中最早的时间是 `00:00`  ，最晚的时间是 `23:59` 。

给你两个字符串 `startTime` 和 `finishTime` ，均符合 `"HH:MM"` 格式，分别表示你 **进入** 和 **退出** 游戏的确切时间，请计算在整个游戏会话期间，你完成的 **完整对局的对局数** 。
- 例如，如果 `startTime = "05:20"` 且 `finishTime = "05:59"` ，这意味着你仅仅完成从 `05:30` 到 `05:45` 这一个完整对局。而你没有完成从 `05:15` 到 `05:30` 的完整对局，因为你是在对局开始后进入的游戏；同时，你也没有完成从 `05:45` 到 `06:00` 的完整对局，因为你是在对局结束前退出的游戏。
如果 `finishTime` **早于** `startTime` ，这表示你玩了个通宵（也就是从 `startTime` 到午夜，再从午夜到 `finishTime` ）。

假设你是从  `startTime` 进入游戏，并在  `finishTime` 退出游戏，请计算并返回你完成的 **完整对局的对局数** 。

 

 **示例 1：** 

```

输入：startTime = "12:01", finishTime = "12:44"
输出：1
解释：你完成了从 12:15 到 12:30 的一个完整对局。
你没有完成从 12:00 到 12:15 的完整对局，因为你是在对局开始后的 12:01 进入的游戏。
你没有完成从 12:30 到 12:45 的完整对局，因为你是在对局结束前的 12:44 退出的游戏。

```
 **示例 2：** 

```

输入：startTime = "20:00", finishTime = "06:00"
输出：40
解释：你完成了从 20:00 到 00:00 的 16 个完整的对局，以及从 00:00 到 06:00 的 24 个完整的对局。
16 + 24 = 40

```
 **示例 3：** 

```

输入：startTime = "00:00", finishTime = "23:59"
输出：95
解释：除最后一个小时你只完成了 3 个完整对局外，其余每个小时均完成了 4 场完整对局。

```
 

 **提示：** 
-  `startTime` 和 `finishTime` 的格式为 `HH:MM` 
-  `00 <= HH <= 23` 
-  `00 <= MM <= 59` 
-  `startTime` 和 `finishTime` 不相等
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 1905.统计子岛屿
[https://leetcode-cn.com/problems/count-sub-islands](https://leetcode-cn.com/problems/count-sub-islands) 
## 原题
给你两个  `m x n`  的二进制矩阵  `grid1` 和  `grid2`  ，它们只包含  `0`  （表示水域）和 `1`  （表示陆地）。一个 **岛屿**  是由 **四个方向**  （水平或者竖直）上相邻的  `1`  组成的区域。任何矩阵以外的区域都视为水域。

如果 `grid2`  的一个岛屿，被 `grid1`  的一个岛屿  **完全** 包含，也就是说 `grid2`  中该岛屿的每一个格子都被 `grid1`  中同一个岛屿完全包含，那么我们称 `grid2`  中的这个岛屿为 **子岛屿**  。

请你返回 `grid2`  中 **子岛屿**  的 **数目**  。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/test1.png" style="width: 493px; height: 205px;">
```
输入：grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
输出：3
解释：如上图所示，左边为 grid1 ，右边为 grid2 。
grid2 中标红的 1 区域是子岛屿，总共有 3 个子岛屿。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/03/testcasex2.png" style="width: 491px; height: 201px;">
```
输入：grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
输出：2 
解释：如上图所示，左边为 grid1 ，右边为 grid2 。
grid2 中标红的 1 区域是子岛屿，总共有 2 个子岛屿。

```
 

 **提示：** 
-  `m == grid1.length == grid2.length` 
-  `n == grid1[i].length == grid2[i].length` 
-  `1 <= m, n <= 500` 
-  `grid1[i][j]` 和  `grid2[i][j]`  都要么是  `0`  要么是  `1`  。
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` 


## 
```python

```
>
# 1906.查询差绝对值的最小值
[https://leetcode-cn.com/problems/minimum-absolute-difference-queries](https://leetcode-cn.com/problems/minimum-absolute-difference-queries) 
## 原题
一个数组 `a`  的 **差绝对值的最小值**  定义为： `0 <= i < j < a.length`  且 `a[i] != a[j]`  的 **** `<span style="">|a[i] - a[j]|</span>` 的 **最小值** 。如果 `a`  中所有元素都 **相同**  ，那么差绝对值的最小值为 `-1`  。
- 比方说，数组  `[5, **2** , **3** ,7,2]`  差绝对值的最小值是  `|2 - 3| = 1`  。注意答案不为 `0`  ，因为  `a[i]` 和  `a[j]`  必须不相等。
给你一个整数数组  `nums`  和查询数组  `queries`  ，其中  `queries[i] = [l<sub>i</sub>, r<sub>i</sub>]`  。对于每个查询  `i`  ，计算  **子数组**   `nums[l<sub>i</sub>...r<sub>i</sub>]`  中 **差绝对值的最小值** ，子数组  `nums[l<sub>i</sub>...r<sub>i</sub>]` 包含 `nums`  数组（下标从 **0**  开始）中下标在 `l<sub>i</sub>` 和  `r<sub>i</sub>` 之间的所有元素（包含  `l<sub>i</sub>` 和  `r<sub>i</sub>` 在内）。

请你返回  `ans`   **数组** ，其中 `ans[i]`  是第 `i`  个查询的答案。

 **子数组**  是一个数组中连续的一段元素。

 `|x|`  的值定义为：
- 如果  `x >= 0`  ，那么值为  `x`  。
- 如果  `x < 0`  ，那么值为  `-x`  。
 

 **示例 1：** 

```

输入：nums = [1,3,4,8], queries = [[0,1],[1,2],[2,3],[0,3]]
输出：[2,1,4,1]
解释：查询结果如下：
- queries[0] = [0,1]：子数组是 [1,3] ，差绝对值的最小值为 |1-3| = 2 。
- queries[1] = [1,2]：子数组是 [3,4] ，差绝对值的最小值为 |3-4| = 1 。
- queries[2] = [2,3]：子数组是 [4,8] ，差绝对值的最小值为 |4-8| = 4 。
- queries[3] = [0,3]：子数组是 [1,3,4,8] ，差的绝对值的最小值为 |3-4| = 1 。

```
 **示例 2：** 

```

输入：nums = [4,5,2,2,7,10], queries = [[2,3],[0,2],[0,5],[3,5]]
输出：[-1,1,1,3]
解释：查询结果如下：
- queries[0] = [2,3]：子数组是 [2,2] ，差绝对值的最小值为 -1 ，因为所有元素相等。
- queries[1] = [0,2]：子数组是 [4,5,2] ，差绝对值的最小值为 |4-5| = 1 。
- queries[2] = [0,5]：子数组是 [4,5,2,2,7,10] ，差绝对值的最小值为 |4-5| = 1 。
- queries[3] = [3,5]：子数组是 [2,7,10] ，差绝对值的最小值为 |7-10| = 3 。

```
 

 **提示：** 
-  `2 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 100` 
-  `1 <= queries.length <= 2 * 10^4` 
-  `0 <= l<sub>i</sub> < r<sub>i</sub> < nums.length` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1907.按分类统计薪水
[https://leetcode-cn.com/problems/count-salary-categories](https://leetcode-cn.com/problems/count-salary-categories) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1908.Nim 游戏 II
[https://leetcode-cn.com/problems/game-of-nim](https://leetcode-cn.com/problems/game-of-nim) 
## 原题

 
**标签**
`位运算` `脑筋急转弯` `数组` `数学` `动态规划` `博弈` 


## 
```python

```
>
# 1909.删除一个元素使数组严格递增
[https://leetcode-cn.com/problems/remove-one-element-to-make-the-array-strictly-increasing](https://leetcode-cn.com/problems/remove-one-element-to-make-the-array-strictly-increasing) 
## 原题
给你一个下标从 **0**  开始的整数数组  `nums`  ，如果  **恰好**  删除  **一个**  元素后，数组  **严格递增**  ，那么请你返回  `true`  ，否则返回  `false`  。如果数组本身已经是严格递增的，请你也返回  `true`  。

数组  `nums`  是 **严格递增**  的定义为：对于任意下标的  `1 <= i < nums.length`  都满足  `nums[i - 1] < nums[i]`  。

 

 **示例 1：** 

```
输入：nums = [1,2,10,5,7]
输出：true
解释：从 nums 中删除下标 2 处的 10 ，得到 [1,2,5,7] 。
[1,2,5,7] 是严格递增的，所以返回 true 。

```
 **示例 2：** 

```
输入：nums = [2,3,1,2]
输出：false
解释：
[3,1,2] 是删除下标 0 处元素后得到的结果。
[2,1,2] 是删除下标 1 处元素后得到的结果。
[2,3,2] 是删除下标 2 处元素后得到的结果。
[2,3,1] 是删除下标 3 处元素后得到的结果。
没有任何结果数组是严格递增的，所以返回 false 。
```
 **示例 3：** 

```
输入：nums = [1,1,1]
输出：false
解释：删除任意元素后的结果都是 [1,1] 。
[1,1] 不是严格递增的，所以返回 false 。

```
 **示例 4：** 

```
输入：nums = [1,2,3]
输出：true
解释：[1,2,3] 已经是严格递增的，所以返回 true 。

```
 

 **提示：** 
-  `2 <= nums.length <= 1000` 
-  `1 <= nums[i] <= 1000` 
 
**标签**
`数组` 


## 
```python

```
>
# 1910.删除一个字符串中所有出现的给定子字符串
[https://leetcode-cn.com/problems/remove-all-occurrences-of-a-substring](https://leetcode-cn.com/problems/remove-all-occurrences-of-a-substring) 
## 原题
给你两个字符串  `s`  和  `part`  ，请你对  `s`  反复执行以下操作直到 <b>所有</b> 子字符串  `part`  都被删除：
- 找到 `s`  中 **最左边**  的子字符串 `part`  ，并将它从 `s`  中删除。
请你返回从 `s`  中删除所有 `part`  子字符串以后得到的剩余字符串。

一个 **子字符串**  是一个字符串中连续的字符序列。

 

 **示例 1：** 

```
输入：s = "daabcbaabcbc", part = "abc"
输出："dab"
解释：以下操作按顺序执行：
- s = "daabcbaabcbc" ，删除下标从 2 开始的 "abc" ，得到 s = "dabaabcbc" 。
- s = "dabaabcbc" ，删除下标从 4 开始的 "abc" ，得到 s = "dababc" 。
- s = "dababc" ，删除下标从 3 开始的 "abc" ，得到 s = "dab" 。
此时 s 中不再含有子字符串 "abc" 。

```
 **示例 2：** 

```
输入：s = "axxxxyyyyb", part = "xy"
输出："ab"
解释：以下操作按顺序执行：
- s = "axxxxyyyyb" ，删除下标从 4 开始的 "xy" ，得到 s = "axxxyyyb" 。
- s = "axxxyyyb" ，删除下标从 3 开始的 "xy" ，得到 s = "axxyyb" 。
- s = "axxyyb" ，删除下标从 2 开始的 "xy" ，得到 s = "axyb" 。
- s = "axyb" ，删除下标从 1 开始的 "xy" ，得到 s = "ab" 。
此时 s 中不再含有子字符串 "xy" 。

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `1 <= part.length <= 1000` 
-  `s` ​​​​​​ 和  `part`  只包小写英文字母。
 
**标签**
`字符串` 


## 
```python

```
>
# 1911.最大子序列交替和
[https://leetcode-cn.com/problems/maximum-alternating-subsequence-sum](https://leetcode-cn.com/problems/maximum-alternating-subsequence-sum) 
## 原题
一个下标从 **0**  开始的数组的 **交替和**  定义为 **偶数**  下标处元素之 **和**  减去 **奇数**  下标处元素之 **和**  。
- 比方说，数组  `[4,2,5,3]`  的交替和为  `(4 + 5) - (2 + 3) = 4`  。
给你一个数组  `nums`  ，请你返回  `nums`  中任意子序列的  **最大交替和**  （子序列的下标 **重新**  从 0 开始编号）。
一个数组的 **子序列**  是从原数组中删除一些元素后（也可能一个也不删除）剩余元素不改变顺序组成的数组。比方说， `[2,7,4]`  是  `[4, **2** ,3, **7** ,2,1, **4** ]`  的一个子序列（加粗元素），但是  `[2,4,2]` 不是。

 

<b>示例 1：</b>

```
输入：nums = [4,2,5,3]
输出：7
解释：最优子序列为 [4,2,5] ，交替和为 (4 + 5) - 2 = 7 。

```
 **示例 2：** 

```
输入：nums = [5,6,7,8]
输出：8
解释：最优子序列为 [8] ，交替和为 8 。

```
 **示例 3：** 

```
输入：nums = [6,2,1,2,4,5]
输出：10
解释：最优子序列为 [6,1,5] ，交替和为 (6 + 5) - 1 = 10 。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^5` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1912.设计电影租借系统
[https://leetcode-cn.com/problems/design-movie-rental-system](https://leetcode-cn.com/problems/design-movie-rental-system) 
## 原题
你有一个电影租借公司和 `n`  个电影商店。你想要实现一个电影租借系统，它支持查询、预订和返还电影的操作。同时系统还能生成一份当前被借出电影的报告。

所有电影用二维整数数组  `entries`  表示，其中  `entries[i] = [shop<sub>i</sub>, movie<sub>i</sub>, price<sub>i</sub>]`  表示商店 `shop<sub>i</sub>`  有一份电影  `movie<sub>i</sub>`  的拷贝，租借价格为  `price<sub>i</sub>`  。每个商店有  **至多一份**  编号为  `movie<sub>i</sub>`  的电影拷贝。

系统需要支持以下操作：
-  **Search：** 找到拥有指定电影且 **未借出**  的商店中  **最便宜的 5 个**  。商店需要按照  **价格**  升序排序，如果价格相同，则  `shop<sub>i</sub>`   **较小**  的商店排在前面。如果查询结果少于 5 个商店，则将它们全部返回。如果查询结果没有任何商店，则返回空列表。
-  **Rent：** 从指定商店借出指定电影，题目保证指定电影在指定商店 **未借出**  。
-  **Drop：** 在指定商店返还 **之前已借出**  的指定电影。
-  **Report：** 返回 **最便宜的 5 部已借出电影**  （可能有重复的电影 ID），将结果用二维列表  `res`  返回，其中 `res[j] = [shop<sub>j</sub>, movie<sub>j</sub>]`  表示第  `j`  便宜的已借出电影是从商店  `shop<sub>j</sub>`  借出的电影  `movie<sub>j</sub>`  。 `res`  中的电影需要按 **价格**  升序排序；如果价格相同，则 ** ** `shop<sub>j</sub>` **较小**  的排在前面；如果仍然相同，则 `movie<sub>j</sub>` **较小** 的排在前面。如果当前借出的电影小于 5 部，则将它们全部返回。如果当前没有借出电影，则返回一个空的列表。
请你实现  `MovieRentingSystem`  类：
-  `MovieRentingSystem(int n, int[][] entries)`  将  `MovieRentingSystem`  对象用  `n`  个商店和  `entries`  表示的电影列表初始化。
-  `List<Integer> search(int movie)` 如上所述，返回 **未借出**  指定 `movie`  的商店列表。
-  `void rent(int shop, int movie)`  从指定商店 `shop`  借出指定电影  `movie`  。
-  `void drop(int shop, int movie)`  在指定商店 `shop`  返还之前借出的电影  `movie`  。
-  `List<List<Integer>> report()` 如上所述，返回最便宜的 **已借出**  电影列表。
 **注意：** 测试数据保证  `rent`  操作中指定商店拥有 **未借出** 的指定电影，且  `drop`  操作指定的商店 **之前已借出**  指定电影。

 

 **示例 1：** 

```

输入：
["MovieRentingSystem", "search", "rent", "rent", "report", "drop", "search"]
[[3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]], [1], [0, 1], [1, 2], [], [1, 2], [2]]
输出：
[null, [1, 0, 2], null, null, [[0, 1], [1, 2]], null, [0, 1]]

解释：
MovieRentingSystem movieRentingSystem = new MovieRentingSystem(3, [[0, 1, 5], [0, 2, 6], [0, 3, 7], [1, 1, 4], [1, 2, 7], [2, 1, 5]]);
movieRentingSystem.search(1);  // 返回 [1, 0, 2] ，商店 1，0 和 2 有未借出的 ID 为 1 的电影。商店 1 最便宜，商店 0 和 2 价格相同，所以按商店编号排序。
movieRentingSystem.rent(0, 1); // 从商店 0 借出电影 1 。现在商店 0 未借出电影编号为 [2,3] 。
movieRentingSystem.rent(1, 2); // 从商店 1 借出电影 2 。现在商店 1 未借出的电影编号为 [1] 。
movieRentingSystem.report();   // 返回 [[0, 1], [1, 2]] 。商店 0 借出的电影 1 最便宜，然后是商店 1 借出的电影 2 。
movieRentingSystem.drop(1, 2); // 在商店 1 返还电影 2 。现在商店 1 未借出的电影编号为 [1,2] 。
movieRentingSystem.search(2);  // 返回 [0, 1] 。商店 0 和 1 有未借出的 ID 为 2 的电影。商店 0 最便宜，然后是商店 1 。

```
 

 **提示：** 
-  `1 <= n <= 3 * 10^5` 
-  `1 <= entries.length <= 10^5` 
-  `0 <= shop<sub>i</sub> < n` 
-  `1 <= movie<sub>i</sub>, price<sub>i</sub> <= 10^4` 
- 每个商店 **至多**  有一份电影  `movie<sub>i</sub>`  的拷贝。
-  `search` ， `rent` ， `drop` 和  `report`  的调用  **总共**  不超过  `10^5`  次。
 
**标签**
`设计` `数组` `哈希表` `有序集合` `堆（优先队列）` 


## 
```python

```
>
# 1913.两个数对之间的最大乘积差
[https://leetcode-cn.com/problems/maximum-product-difference-between-two-pairs](https://leetcode-cn.com/problems/maximum-product-difference-between-two-pairs) 
## 原题
两个数对  `(a, b)` 和 `(c, d)` 之间的 **乘积差** 定义为 `(a * b) - (c * d)` 。
- 例如， `(5, 6)` 和 `(2, 7)` 之间的乘积差是 `(5 * 6) - (2 * 7) = 16` 。
给你一个整数数组 `nums` ，选出四个 **不同的** 下标 `w` 、 `x` 、 `y` 和 `z` ，使数对 `(nums[w], nums[x])` 和 `(nums[y], nums[z])` 之间的 **乘积差** 取到 **最大值** 。

返回以这种方式取得的乘积差中的 **最大值** 。

 

 **示例 1：** 

```
输入：nums = [5,6,2,7,4]
输出：34
解释：可以选出下标为 1 和 3 的元素构成第一个数对 (6, 7) 以及下标 2 和 4 构成第二个数对 (2, 4)
乘积差是 (6 * 7) - (2 * 4) = 34

```
 **示例 2：** 

```
输入：nums = [4,2,5,9,7,4,8]
输出：64
解释：可以选出下标为 3 和 6 的元素构成第一个数对 (9, 8) 以及下标 1 和 5 构成第二个数对 (2, 4)
乘积差是 (9 * 8) - (2 * 4) = 64

```
 

 **提示：** 
-  `4 <= nums.length <= 10^4` 
-  `1 <= nums[i] <= 10^4` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 1914.循环轮转矩阵
[https://leetcode-cn.com/problems/cyclically-rotating-a-grid](https://leetcode-cn.com/problems/cyclically-rotating-a-grid) 
## 原题
给你一个大小为 `m x n` 的整数矩阵 `grid` ​​​ ，其中 `m` 和 `n` 都是 **偶数** ；另给你一个整数 `k` 。

矩阵由若干层组成，如下图所示，每种颜色代表一层：

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid.png" style="width: 231px; height: 258px;">

矩阵的循环轮转是通过分别循环轮转矩阵中的每一层完成的。在对某一层进行一次循环旋转操作时，层中的每一个元素将会取代其  **逆时针** 方向的相邻元素。轮转示例如下：
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/explanation_grid.jpg" style="width: 500px; height: 268px;">
返回执行 `k` 次循环轮转操作后的矩阵。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/19/rod2.png" style="width: 421px; height: 191px;">
```
输入：grid = [[40,10],[30,20]], k = 1
输出：[[10,20],[40,30]]
解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。
```
 **示例 2：** 
 **<img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid5.png" style="width: 231px; height: 262px;">** **<img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid6.png" style="width: 231px; height: 262px;">** **<img alt="" src="https://assets.leetcode.com/uploads/2021/06/10/ringofgrid7.png" style="width: 231px; height: 262px;">** 

```
输入：grid = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], k = 2
输出：[[3,4,8,12],[2,11,10,16],[1,7,6,15],[5,9,13,14]]
解释：上图展示了矩阵在执行循环轮转操作时每一步的状态。

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `2 <= m, n <= 50` 
-  `m` 和 `n` 都是 **偶数** 
-  `1 <= grid[i][j] <=^ 5000` 
-  `1 <= k <= 10^9` 
 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 1915.最美子字符串的数目
[https://leetcode-cn.com/problems/number-of-wonderful-substrings](https://leetcode-cn.com/problems/number-of-wonderful-substrings) 
## 原题
如果某个字符串中 **至多一个** 字母出现 **奇数** 次，则称其为 **最美** 字符串。
- 例如， `"ccjjc"` 和 `"abab"` 都是最美字符串，但 `"ab"` 不是。
给你一个字符串 `word` ，该字符串由前十个小写英文字母组成（ `'a'` 到 `'j'` ）。请你返回 `word` 中 **最美非空子字符串** 的数目 *。* 如果同样的子字符串在 `word` 中出现多次，那么应当对 **每次出现** 分别计数 *。* 

 **子字符串** 是字符串中的一个连续字符序列。

 

 **示例 1：** 

```

输入：word = "aba"
输出：4
解释：4 个最美子字符串如下所示：
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"

```
 **示例 2：** 

```

输入：word = "aabb"
输出：9
解释：9 个最美子字符串如下所示：
- "aabb" -> "a"
- "aabb" -> "aa"
- "aabb" -> "aab"
- "aabb" -> "aabb"
- "aabb" -> "a"
- "aabb" -> "abb"
- "aabb" -> "b"
- "aabb" -> "bb"
- "aabb" -> "b"

```
 **示例 3：** 

```

输入：word = "he"
输出：2
解释：2 个最美子字符串如下所示：
- "he" -> "h"
- "he" -> "e"

```
 

 **提示：** 
-  `1 <= word.length <= 10^5` 
-  `word` 由从 `'a'` 到 `'j'` 的小写英文字母组成
 
**标签**
`位运算` `哈希表` `字符串` `前缀和` 


## 
```python

```
>
# 1916.统计为蚁群构筑房间的不同顺序
[https://leetcode-cn.com/problems/count-ways-to-build-rooms-in-an-ant-colony](https://leetcode-cn.com/problems/count-ways-to-build-rooms-in-an-ant-colony) 
## 原题
你是一只蚂蚁，负责为蚁群构筑 `n` 间编号从 `0` 到 `n-1` 的新房间。给你一个 **下标从 0 开始** 且长度为 `n` 的整数数组  `prevRoom` 作为扩建计划。其中， `prevRoom[i]` 表示在构筑房间 `i` 之前，你必须先构筑房间 `prevRoom[i]` ，并且这两个房间必须 **直接** 相连。房间 `0` 已经构筑完成，所以 `prevRoom[0] = -1` 。扩建计划中还有一条硬性要求，在完成所有房间的构筑之后，从房间 `0` 可以访问到每个房间。

你一次只能构筑 **一个** 房间。你可以在 **已经构筑好的** 房间之间自由穿行，只要这些房间是 **相连的** 。如果房间  `prevRoom[i]` 已经构筑完成，那么你就可以构筑房间 `i` 。

返回你构筑所有房间的 **不同顺序的数目** 。由于答案可能很大，请返回对 `10^9 + 7` **取余** 的结果。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/19/d1.JPG" style="width: 200px; height: 212px;" />
```

输入：prevRoom = [-1,0,1]
输出：1
解释：仅有一种方案可以完成所有房间的构筑：0 → 1 → 2

```
 **示例 2：** 
 **<img alt="" src="https://assets.leetcode.com/uploads/2021/06/19/d2.JPG" style="width: 200px; height: 239px;" />** 

```

输入：prevRoom = [-1,0,0,1,2]
输出：6
解释：
有 6 种不同顺序：
0 → 1 → 3 → 2 → 4
0 → 2 → 4 → 1 → 3
0 → 1 → 2 → 3 → 4
0 → 1 → 2 → 4 → 3
0 → 2 → 1 → 3 → 4
0 → 2 → 1 → 4 → 3

```
 

 **提示：** 
-  `n == prevRoom.length` 
-  `2 <= n <= 10^5` 
-  `prevRoom[0] == -1` 
- 对于所有的  `1 <= i < n`  ，都有  `0 <= prevRoom[i] < n` 
- 题目保证所有房间都构筑完成后，从房间 `0` 可以访问到每个房间
 
**标签**
`树` `图` `拓扑排序` `数学` `动态规划` `组合数学` 


## 
```python

```
>
# 1917.Leetcodify 好友推荐
[https://leetcode-cn.com/problems/leetcodify-friends-recommendations](https://leetcode-cn.com/problems/leetcodify-friends-recommendations) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1918.第 K 小的子数组和·
[https://leetcode-cn.com/problems/kth-smallest-subarray-sum](https://leetcode-cn.com/problems/kth-smallest-subarray-sum) 
## 原题

 
**标签**
`数组` `二分查找` `滑动窗口` 


## 
```python

```
>
# 1919.兴趣相同的朋友
[https://leetcode-cn.com/problems/leetcodify-similar-friends](https://leetcode-cn.com/problems/leetcodify-similar-friends) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1920.基于排列构建数组
[https://leetcode-cn.com/problems/build-array-from-permutation](https://leetcode-cn.com/problems/build-array-from-permutation) 
## 原题
给你一个 **从 0 开始的排列** `nums` （ **下标也从 0 开始** ）。请你构建一个 **同样长度** 的数组 `ans` ，其中，对于每个 `i` （ `0 <= i < nums.length` ），都满足 `ans[i] = nums[nums[i]]` 。返回构建好的数组 `ans` 。

 **从 0 开始的排列** `nums` 是一个由 `0` 到  `nums.length - 1` （ `0` 和 `nums.length - 1` 也包含在内）的不同整数组成的数组。

 

 **示例 1：** 

```
输入：nums = [0,2,1,5,3,4]
输出：[0,1,2,4,5,3]
解释：数组 ans 构建如下：
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[0], nums[2], nums[1], nums[5], nums[3], nums[4]]
    = [0,1,2,4,5,3]
```
 **示例 2：** 

```
输入：nums = [5,0,1,2,3,4]
输出：[4,5,0,1,2,3]
解释：数组 ans 构建如下：
ans = [nums[nums[0]], nums[nums[1]], nums[nums[2]], nums[nums[3]], nums[nums[4]], nums[nums[5]]]
    = [nums[5], nums[0], nums[1], nums[2], nums[3], nums[4]]
    = [4,5,0,1,2,3]
```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `0 <= nums[i] < nums.length` 
-  `nums` 中的元素 **互不相同** 
 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 1921.消灭怪物的最大数量
[https://leetcode-cn.com/problems/eliminate-maximum-number-of-monsters](https://leetcode-cn.com/problems/eliminate-maximum-number-of-monsters) 
## 原题
你正在玩一款电子游戏，在游戏中你需要保护城市免受怪物侵袭。给你一个 **下标从 0 开始** 且长度为 `n` 的整数数组 `dist` ，其中 `dist[i]` 是第 `i` 个怪物与城市的 **初始距离** （单位：米）。

怪物以 **恒定** 的速度走向城市。给你一个长度为 `n` 的整数数组 `speed` 表示每个怪物的速度，其中 `speed[i]` 是第 `i` 个怪物的速度（单位：米/分）。

怪物从 **第 0 分钟** 时开始移动。你有一把武器，并可以 **选择** 在每一分钟的开始时使用，包括第 0 分钟。但是你无法在一分钟的中间使用武器。这种武器威力惊人，一次可以消灭任一还活着的怪物。

一旦任一怪物到达城市，你就输掉了这场游戏。如果某个怪物 **恰** 在某一分钟开始时到达城市，这会被视为 **输掉**  游戏，在你可以使用武器之前，游戏就会结束。

返回在你输掉游戏前可以消灭的怪物的 **最大** 数量。如果你可以在所有怪物到达城市前将它们全部消灭，返回  `n` 。

 

 **示例 1：** 

```

输入：dist = [1,3,4], speed = [1,1,1]
输出：3
解释：
第 0 分钟开始时，怪物的距离是 [1,3,4]，你消灭了第一个怪物。
第 1 分钟开始时，怪物的距离是 [X,2,3]，你没有消灭任何怪物。
第 2 分钟开始时，怪物的距离是 [X,1,2]，你消灭了第二个怪物。
第 3 分钟开始时，怪物的距离是 [X,X,1]，你消灭了第三个怪物。
所有 3 个怪物都可以被消灭。
```
 **示例 2：** 

```

输入：dist = [1,1,2,3], speed = [1,1,1,1]
输出：1
解释：
第 0 分钟开始时，怪物的距离是 [1,1,2,3]，你消灭了第一个怪物。
第 1 分钟开始时，怪物的距离是 [X,0,1,2]，你输掉了游戏。
你只能消灭 1 个怪物。

```
 **示例 3：** 

```

输入：dist = [3,2,4], speed = [5,3,2]
输出：1
解释：
第 0 分钟开始时，怪物的距离是 [3,2,4]，你消灭了第一个怪物。
第 1 分钟开始时，怪物的距离是 [X,0,2]，你输掉了游戏。 
你只能消灭 1 个怪物。

```
 

 **提示：** 
-  `n == dist.length == speed.length` 
-  `1 <= n <= 10^5` 
-  `1 <= dist[i], speed[i] <= 10^5` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1922.统计好数字的数目
[https://leetcode-cn.com/problems/count-good-numbers](https://leetcode-cn.com/problems/count-good-numbers) 
## 原题
我们称一个数字字符串是 **好数字** 当它满足（下标从 **0**  开始） **偶数** 下标处的数字为 **偶数**  且 **奇数**  下标处的数字为 **质数**  （ `2` ， `3` ， `5`  或  `7` ）。
- 比方说， `"2582"`  是好数字，因为偶数下标处的数字（ `2`  和  `8` ）是偶数且奇数下标处的数字（ `5` 和  `2` ）为质数。但  `"3245"`   **不是** 好数字，因为  `3`  在偶数下标处但不是偶数。
给你一个整数  `n`  ，请你返回长度为  `n`  且为好数字的数字字符串  **总数**  。由于答案可能会很大，请你将它对 ** ** `10^9 + 7`   **取余后返回**  。

一个 **数字字符串**  是每一位都由  `0`  到 `9`  组成的字符串，且可能包含前导 0 。

 

 **示例 1：** 

```

输入：n = 1
输出：5
解释：长度为 1 的好数字包括 "0"，"2"，"4"，"6"，"8" 。

```
 **示例 2：** 

```

输入：n = 4
输出：400

```
 **示例 3：** 

```

输入：n = 50
输出：564908303

```
 

 **提示：** 
-  `1 <= n <= 10^15` 
 
**标签**
`递归` `数学` 


## 
```python

```
>
# 1923.最长公共子路径
[https://leetcode-cn.com/problems/longest-common-subpath](https://leetcode-cn.com/problems/longest-common-subpath) 
## 原题
一个国家由 `n`  个编号为 `0`  到 `n - 1`  的城市组成。在这个国家里， **每两个**  城市之间都有一条道路连接。

总共有 `m`  个编号为 `0`  到 `m - 1`  的朋友想在这个国家旅游。他们每一个人的路径都会包含一些城市。每条路径都由一个整数数组表示，每个整数数组表示一个朋友按顺序访问过的城市序列。同一个城市在一条路径中可能 **重复** 出现，但同一个城市在一条路径中不会连续出现。

给你一个整数  `n`  和二维数组  `paths`  ，其中  `paths[i]`  是一个整数数组，表示第 `i`  个朋友走过的路径，请你返回 **每一个**  朋友都走过的 **最长公共子路径**  的长度，如果不存在公共子路径，请你返回 `0`  。

一个 **子路径** 指的是一条路径中连续的城市序列。

 

 **示例 1：** 

```

输入：n = 5, paths = [[0,1,2,3,4],
                     [2,3,4],
                     [4,0,1,2,3]]
输出：2
解释：最长公共子路径为 [2,3] 。

```
 **示例 2：** 

```

输入：n = 3, paths = [[0],[1],[2]]
输出：0
解释：三条路径没有公共子路径。

```
 **示例 3：** 

```

输入：n = 5, paths = [[0,1,2,3,4],
                     [4,3,2,1,0]]
输出：1
解释：最长公共子路径为 [0]，[1]，[2]，[3] 和 [4] 。它们长度都为 1 。
```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `m == paths.length` 
-  `2 <= m <= 10^5` 
-  `sum(paths[i].length) <= 10^5` 
-  `0 <= paths[i][j] < n` 
-  `paths[i]`  中同一个城市不会连续重复出现。
 
**标签**
`数组` `二分查找` `后缀数组` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 1924.安装栅栏 II
[https://leetcode-cn.com/problems/erect-the-fence-ii](https://leetcode-cn.com/problems/erect-the-fence-ii) 
## 原题

 
**标签**
`几何` `数组` `数学` 


## 
```python

```
>
# 1925.统计平方和三元组的数目
[https://leetcode-cn.com/problems/count-square-sum-triples](https://leetcode-cn.com/problems/count-square-sum-triples) 
## 原题
一个 **平方和三元组**   `(a,b,c)`  指的是满足 `a^2 + b^2 = c^2`  的 **整数 ** 三元组  `a` ， `b`  和  `c`  。

给你一个整数  `n`  ，请你返回满足 * * `1 <= a, b, c <= n`  的 **平方和三元组** 的数目。

 

 **示例 1：** 

```
输入：n = 5
输出：2
解释：平方和三元组为 (3,4,5) 和 (4,3,5) 。

```
 **示例 2：** 

```
输入：n = 10
输出：4
解释：平方和三元组为 (3,4,5)，(4,3,5)，(6,8,10) 和 (8,6,10) 。

```
 

 **提示：** 
-  `1 <= n <= 250` 
 
**标签**
`数学` `枚举` 


## 
```python

```
>
# 1926.迷宫中离入口最近的出口
[https://leetcode-cn.com/problems/nearest-exit-from-entrance-in-maze](https://leetcode-cn.com/problems/nearest-exit-from-entrance-in-maze) 
## 原题
给你一个  `m x n`  的迷宫矩阵  `maze`  （ **下标从 0 开始** ），矩阵中有空格子（用  `'.'`  表示）和墙（用  `'+'`  表示）。同时给你迷宫的入口  `entrance`  ，用  `entrance = [entrance<sub>row</sub>, entrance<sub>col</sub>]`  表示你一开始所在格子的行和列。

每一步操作，你可以往 **上** ， **下** ， **左** 或者 **右**  移动一个格子。你不能进入墙所在的格子，你也不能离开迷宫。你的目标是找到离  `entrance`   **最近**  的出口。 **出口**  的含义是  `maze`   **边界**  上的  **空格子** 。 `entrance`  格子  **不算**  出口。

请你返回从 `entrance`  到最近出口的最短路径的 **步数**  ，如果不存在这样的路径，请你返回 `-1`  。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/nearest1-grid.jpg" style="width: 333px; height: 253px;">
```
输入：maze = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]], entrance = [1,2]
输出：1
解释：总共有 3 个出口，分别位于 (1,0)，(0,2) 和 (2,3) 。
一开始，你在入口格子 (1,2) 处。
- 你可以往左移动 2 步到达 (1,0) 。
- 你可以往上移动 1 步到达 (0,2) 。
从入口处没法到达 (2,3) 。
所以，最近的出口是 (0,2) ，距离为 1 步。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/nearesr2-grid.jpg" style="width: 253px; height: 253px;">
```
输入：maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0]
输出：2
解释：迷宫中只有 1 个出口，在 (1,2) 处。
(1,0) 不算出口，因为它是入口格子。
初始时，你在入口与格子 (1,0) 处。
- 你可以往右移动 2 步到达 (1,2) 处。
所以，最近的出口为 (1,2) ，距离为 2 步。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/nearest3-grid.jpg" style="width: 173px; height: 93px;">
```
输入：maze = [[".","+"]], entrance = [0,0]
输出：-1
解释：这个迷宫中没有出口。

```
 

 **提示：** 
-  `maze.length == m` 
-  `maze[i].length == n` 
-  `1 <= m, n <= 100` 
-  `maze[i][j]` 要么是  `'.'`  ，要么是  `'+'`  。
-  `entrance.length == 2` 
-  `0 <= entrance<sub>row</sub> < m` 
-  `0 <= entrance<sub>col</sub> < n` 
-  `entrance`  一定是空格子。
 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 1927.求和游戏
[https://leetcode-cn.com/problems/sum-game](https://leetcode-cn.com/problems/sum-game) 
## 原题
Alice 和 Bob 玩一个游戏，两人轮流行动， **Alice 先手**  。

给你一个 **偶数长度**  的字符串  `num`  ，每一个字符为数字字符或者  `'?'`  。每一次操作中，如果 `num`  中至少有一个 `'?'`  ，那么玩家可以执行以下操作：
- 选择一个下标 `i`  满足  `num[i] == '?'`  。
- 将  `num[i]`  用  `'0'`  到  `'9'`  之间的一个数字字符替代。
当 `num`  中没有<span style=""> </span> `'?'` 时，游戏结束。

Bob 获胜的条件是 `num`  中前一半数字的和 **等于**  后一半数字的和。Alice 获胜的条件是前一半的和与后一半的和 **不相等**  。
- 比方说，游戏结束时  `num = "243801"`  ，那么 Bob 获胜，因为  `2+4+3 = 8+0+1`  。如果游戏结束时  `num = "243803"`  ，那么 Alice 获胜，因为  `2+4+3 != 8+0+3`  。
在 Alice 和 Bob 都采取 **最优**  策略的前提下，如果 Alice 获胜，请返回 `true`  ，如果 Bob 获胜，请返回 `false`  。

 

 **示例 1：** 

```

输入：num = "5023"
输出：false
解释：num 中没有 '?' ，没法进行任何操作。
前一半的和等于后一半的和：5 + 0 = 2 + 3 。

```
 **示例 2：** 

```

输入：num = "25??"
输出：true
解释：Alice 可以将两个 '?' 中的一个替换为 '9' ，Bob 无论如何都无法使前一半的和等于后一半的和。

```
 **示例 3：** 

```

输入：num = "?3295???"
输出：false
解释：Bob 总是能赢。一种可能的结果是：
- Alice 将第一个 '?' 用 '9' 替换。num = "93295???" 。
- Bob 将后面一半中的一个 '?' 替换为 '9' 。num = "932959??" 。
- Alice 将后面一半中的一个 '?' 替换为 '2' 。num = "9329592?" 。
- Bob 将后面一半中最后一个 '?' 替换为 '7' 。num = "93295927" 。
Bob 获胜，因为 9 + 3 + 2 + 9 = 5 + 9 + 2 + 7 。

```
 

 **提示：** 
-  `2 <= num.length <= 10^5` 
-  `num.length`  是 **偶数**  。
-  `num`  只包含数字字符和  `'?'`  。
 
**标签**
`贪心` `数学` `博弈` 


## 
```python

```
>
# 1928.规定时间内到达终点的最小花费
[https://leetcode-cn.com/problems/minimum-cost-to-reach-destination-in-time](https://leetcode-cn.com/problems/minimum-cost-to-reach-destination-in-time) 
## 原题
一个国家有 `n`  个城市，城市编号为  `0`  到  `n - 1`  ，题目保证 **所有城市**  都由双向道路 <b>连接在一起</b> 。道路由二维整数数组  `edges`  表示，其中  `edges[i] = [x<sub>i</sub>, y<sub>i</sub>, time<sub>i</sub>]`  表示城市  `x<sub>i</sub>` 和  `y<sub>i</sub>`  之间有一条双向道路，耗费时间为  `time<sub>i</sub>`  分钟。两个城市之间可能会有多条耗费时间不同的道路，但是不会有道路两头连接着同一座城市。

每次经过一个城市时，你需要付通行费。通行费用一个长度为 `n`  且下标从 **0**  开始的整数数组  `passingFees`  表示，其中  `passingFees[j]`  是你经过城市 `j`  需要支付的费用。

一开始，你在城市  `0`  ，你想要在 `maxTime`   **分钟以内**  （包含 `maxTime`  分钟）到达城市  `n - 1`  。旅行的 **费用** 为你经过的所有城市 **通行费之和**  （ **包括**  起点和终点城市的通行费）。

给你  `maxTime` ， `edges`  和  `passingFees`  ，请你返回完成旅行的  **最小费用**  ，如果无法在  `maxTime`  分钟以内完成旅行，请你返回  `-1`  。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/leetgraph1-1.png" style="width: 371px; height: 171px;" />

```

输入：maxTime = 30, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
输出：11
解释：最优路径为 0 -> 1 -> 2 -> 5 ，总共需要耗费 30 分钟，需要支付 11 的通行费。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode.com/uploads/2021/06/04/copy-of-leetgraph1-1.png" style="width: 371px; height: 171px;" />** 

```

输入：maxTime = 29, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
输出：48
解释：最优路径为 0 -> 3 -> 4 -> 5 ，总共需要耗费 26 分钟，需要支付 48 的通行费。
你不能选择路径 0 -> 1 -> 2 -> 5 ，因为这条路径耗费的时间太长。

```
 **示例 3：** 

```

输入：maxTime = 25, edges = [[0,1,10],[1,2,10],[2,5,10],[0,3,1],[3,4,10],[4,5,15]], passingFees = [5,1,2,20,20,3]
输出：-1
解释：无法在 25 分钟以内从城市 0 到达城市 5 。

```
 

 **提示：** 
-  `1 <= maxTime <= 1000` 
-  `n == passingFees.length` 
-  `2 <= n <= 1000` 
-  `n - 1 <= edges.length <= 1000` 
-  `0 <= x<sub>i</sub>, y<sub>i</sub> <= n - 1` 
-  `1 <= time<sub>i</sub> <= 1000` 
-  `1 <= passingFees[j] <= 1000`  
- 图中两个节点之间可能有多条路径。
- 图中不含有自环。
 
**标签**
`图` `动态规划` 


## 
```python

```
>
# 1929.数组串联
[https://leetcode-cn.com/problems/concatenation-of-array](https://leetcode-cn.com/problems/concatenation-of-array) 
## 原题
给你一个长度为 `n` 的整数数组 `nums` 。请你构建一个长度为 `2n` 的答案数组 `ans` ，数组下标 **从 0 开始计数** ，对于所有  `0 <= i < n` 的 `i` ，满足下述所有要求：
-  `ans[i] == nums[i]` 
-  `ans[i + n] == nums[i]` 
具体而言， `ans` 由两个 `nums` 数组 **串联** 形成。

返回数组 `ans` 。

 

 **示例 1：** 

```

输入：nums = [1,2,1]
输出：[1,2,1,1,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]
```
 **示例 2：** 

```

输入：nums = [1,3,2,1]
输出：[1,3,2,1,1,3,2,1]
解释：数组 ans 按下述方式形成：
- ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
- ans = [1,3,2,1,1,3,2,1]

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 1000` 
-  `1 <= nums[i] <= 1000` 
 
**标签**
`数组` 


## 
```python

```
>
# 1930.长度为 3 的不同回文子序列
[https://leetcode-cn.com/problems/unique-length-3-palindromic-subsequences](https://leetcode-cn.com/problems/unique-length-3-palindromic-subsequences) 
## 原题
给你一个字符串 `s` ，返回 `s` 中 **长度为 3** 的 **不同回文子序列** 的个数。

即便存在多种方法来构建相同的子序列，但相同的子序列只计数一次。

 **回文** 是正着读和反着读一样的字符串。

 **子序列** 是由原字符串删除其中部分字符（也可以不删除）且不改变剩余字符之间相对顺序形成的一个新字符串。
- 例如， `"ace"` 是 `" ** *a* ** b ** *c* ** d ** *e* ** "` 的一个子序列。
 

 **示例 1：** 

```

输入：s = "aabca"
输出：3
解释：长度为 3 的 3 个回文子序列分别是：
- "aba" ("aabca" 的子序列)
- "aaa" ("aabca" 的子序列)
- "aca" ("aabca" 的子序列)

```
 **示例 2：** 

```

输入：s = "adc"
输出：0
解释："adc" 不存在长度为 3 的回文子序列。

```
 **示例 3：** 

```

输入：s = "bbcbaba"
输出：4
解释：长度为 3 的 4 个回文子序列分别是：
- "bbb" ("bbcbaba" 的子序列)
- "bcb" ("bbcbaba" 的子序列)
- "bab" ("bbcbaba" 的子序列)
- "aba" ("bbcbaba" 的子序列)

```
 

 **提示：** 
-  `3 <= s.length <= 10^5` 
-  `s` 仅由小写英文字母组成
 
**标签**
`哈希表` `字符串` `前缀和` 


## 
```python

```
>
# 1931.用三种不同颜色为网格涂色
[https://leetcode-cn.com/problems/painting-a-grid-with-three-different-colors](https://leetcode-cn.com/problems/painting-a-grid-with-three-different-colors) 
## 原题
给你两个整数 `m` 和 `n` 。构造一个 `m x n` 的网格，其中每个单元格最开始是白色。请你用 **红、绿、蓝** 三种颜色为每个单元格涂色。所有单元格都需要被涂色。

涂色方案需要满足： **不存在相邻两个单元格颜色相同的情况** 。返回网格涂色的方法数。因为答案可能非常大， 返回 **对** `10^9 + 7` **取余** 的结果。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/colorthegrid.png" style="width: 200px; height: 50px;" />
```

输入：m = 1, n = 1
输出：3
解释：如上图所示，存在三种可能的涂色方案。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/22/copy-of-colorthegrid.png" style="width: 321px; height: 121px;" />
```

输入：m = 1, n = 2
输出：6
解释：如上图所示，存在六种可能的涂色方案。

```
 **示例 3：** 

```

输入：m = 5, n = 5
输出：580986

```
 

 **提示：** 
-  `1 <= m <= 5` 
-  `1 <= n <= 1000` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 1932.合并多棵二叉搜索树
[https://leetcode-cn.com/problems/merge-bsts-to-create-single-bst](https://leetcode-cn.com/problems/merge-bsts-to-create-single-bst) 
## 原题
给你 `n` 个 **二叉搜索树的根节点** ，存储在数组 `trees` 中（ **下标从 0 开始** ），对应 `n` 棵不同的二叉搜索树。 `trees` 中的每棵二叉搜索树 **最多有 3 个节点** ，且不存在值相同的两个根节点。在一步操作中，将会完成下述步骤：
- 选择两个 **不同的** 下标 `i` 和 `j` ，要求满足在  `trees[i]` 中的某个 **叶节点** 的值等于  `trees[j]` 的 **根节点的值** 。
- 用  `trees[j]` 替换 `trees[i]` 中的那个叶节点。
- 从 `trees` 中移除 `trees[j]` 。
如果在执行 `n - 1` 次操作后，能形成一棵有效的二叉搜索树，则返回结果二叉树的 **根节点** ；如果无法构造一棵有效的二叉搜索树 *，* 返回 `null` 。

二叉搜索树是一种二叉树，且树中每个节点均满足下述属性：
- 任意节点的左子树中的值都 **严格小于**  此节点的值。
- 任意节点的右子树中的值都 **严格大于**  此节点的值。
叶节点是不含子节点的节点。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/d1.png" style="width: 450px; height: 163px;" />
```

输入：trees = [[2,1],[3,2,5],[5,4]]
输出：[3,2,5,1,null,4]
解释：
第一步操作中，选出 i=1 和 j=0 ，并将 trees[0] 合并到 trees[1] 中。
删除 trees[0] ，trees = [[3,2,5,1],[5,4]] 。
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/24/diagram.png" style="width: 450px; height: 181px;" />
在第二步操作中，选出 i=0 和 j=1 ，将 trees[1] 合并到 trees[0] 中。
删除 trees[1] ，trees = [[3,2,5,1,null,4]] 。
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/24/diagram-2.png" style="width: 220px; height: 165px;" />
结果树如上图所示，为一棵有效的二叉搜索树，所以返回该树的根节点。
```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/d2.png" style="width: 450px; height: 171px;" />
```

输入：trees = [[5,3,8],[3,2,6]]
输出：[]
解释：
选出 i=0 和 j=1 ，然后将 trees[1] 合并到 trees[0] 中。
删除 trees[1] ，trees = [[5,3,8,2,6]] 。
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/24/diagram-3.png" style="width: 240px; height: 196px;" />
结果树如上图所示。仅能执行一次有效的操作，但结果树不是一棵有效的二叉搜索树，所以返回 null 。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/d3.png" style="width: 430px; height: 168px;" />
```

输入：trees = [[5,4],[3]]
输出：[]
解释：无法执行任何操作。

```
 **示例 4：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/08/d4.png" style="width: 250px; height: 158px;" />
```

输入：trees = [[2,1,3]]
输出：[2,1,3]
解释：trees 中只有一棵树，且这棵树已经是一棵有效的二叉搜索树，所以返回该树的根节点。

```
 

 **提示：** 
-  `n == trees.length` 
-  `1 <= n <= 5 * 10^4` 
- 每棵树中节点数目在范围 `[1, 3]` 内。
- 输入数据的每个节点可能有子节点但不存在子节点的子节点
-  `trees` 中不存在两棵树根节点值相同的情况。
- 输入中的所有树都是 **有效的二叉树搜索树** 。
-  `1 <= TreeNode.val <= 5 * 10^4` .
 
**标签**
`树` `深度优先搜索` `哈希表` `二分查找` `二叉树` 


## 
```python

```
>
# 1933.判断字符串是否可分解为值均等的子串
[https://leetcode-cn.com/problems/check-if-string-is-decomposable-into-value-equal-substrings](https://leetcode-cn.com/problems/check-if-string-is-decomposable-into-value-equal-substrings) 
## 原题

 
**标签**
`字符串` 


## 
```python

```
>
# 1935.可以输入的最大单词数
[https://leetcode-cn.com/problems/maximum-number-of-words-you-can-type](https://leetcode-cn.com/problems/maximum-number-of-words-you-can-type) 
## 原题
键盘出现了一些故障，有些字母键无法正常工作。而键盘上所有其他键都能够正常工作。

给你一个由若干单词组成的字符串 `text` ，单词间由单个空格组成（不含前导和尾随空格）；另有一个字符串 `brokenLetters` ，由所有已损坏的不同字母键组成，返回你可以使用此键盘完全输入的 `text` 中单词的数目。

 

 **示例 1：** 

```
输入：text = "hello world", brokenLetters = "ad"
输出：1
解释：无法输入 "world" ，因为字母键 'd' 已损坏。

```
 **示例 2：** 

```
输入：text = "leet code", brokenLetters = "lt"
输出：1
解释：无法输入 "leet" ，因为字母键 'l' 和 't' 已损坏。

```
 **示例 3：** 

```
输入：text = "leet code", brokenLetters = "e"
输出：0
解释：无法输入任何单词，因为字母键 'e' 已损坏。

```
 

 **提示：** 
-  `1 <= text.length <= 10^4` 
-  `0 <= brokenLetters.length <= 26` 
-  `text` 由若干用单个空格分隔的单词组成，且不含任何前导和尾随空格
- 每个单词仅由小写英文字母组成
-  `brokenLetters` 由 **互不相同** 的小写英文字母组成
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1936.新增的最少台阶数
[https://leetcode-cn.com/problems/add-minimum-number-of-rungs](https://leetcode-cn.com/problems/add-minimum-number-of-rungs) 
## 原题
给你一个 **严格递增** 的整数数组 `rungs` ，用于表示梯子上每一台阶的 **高度** 。当前你正站在高度为 `0` 的地板上，并打算爬到最后一个台阶。

另给你一个整数 `dist` 。每次移动中，你可以到达下一个距离你当前位置（地板或台阶） **不超过**   `dist`  高度的台阶。当然，你也可以在任何正 **整数** 高度处插入尚不存在的新台阶。

返回爬到最后一阶时必须添加到梯子上的 **最少**  台阶数。

 

 **示例 1：** 

```

输入：rungs = [1,3,5,10], dist = 2
输出：2
解释：
现在无法到达最后一阶。
在高度为 7 和 8 的位置增设新的台阶，以爬上梯子。 
梯子在高度为 [1,3,5,7,8,10] 的位置上有台阶。

```
 **示例 2：** 

```

输入：rungs = [3,6,8,10], dist = 3
输出：0
解释：
这个梯子无需增设新台阶也可以爬上去。

```
 **示例 3：** 

```

输入：rungs = [3,4,6,7], dist = 2
输出：1
解释：
现在无法从地板到达梯子的第一阶。 
在高度为 1 的位置增设新的台阶，以爬上梯子。 
梯子在高度为 [1,3,4,6,7] 的位置上有台阶。

```
 **示例 4：** 

```

输入：rungs = [5], dist = 10
输出：0
解释：这个梯子无需增设新台阶也可以爬上去。

```
 

 **提示：** 
-  `1 <= rungs.length <= 10^5` 
-  `1 <= rungs[i] <= 10^9` 
-  `1 <= dist <= 10^9` 
-  `rungs` **严格递增** 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1937.扣分后的最大得分
[https://leetcode-cn.com/problems/maximum-number-of-points-with-cost](https://leetcode-cn.com/problems/maximum-number-of-points-with-cost) 
## 原题
给你一个  `m x n`  的整数矩阵  `points`  （下标从 **0**  开始）。一开始你的得分为 `0`  ，你想最大化从矩阵中得到的分数。

你的得分方式为： **每一行**  中选取一个格子，选中坐标为  `(r, c)`  的格子会给你的总得分 **增加**   `points[r][c]`  。

然而，相邻行之间被选中的格子如果隔得太远，你会失去一些得分。对于相邻行  `r` 和  `r + 1`  （其中  `0 <= r < m - 1` ），选中坐标为  `(r, c<sub>1</sub>)` 和  `(r + 1, c<sub>2</sub>)`  的格子，你的总得分 <b>减少</b>  `abs(c<sub>1</sub> - c<sub>2</sub>)`  。

请你返回你能得到的 **最大**  得分。

 `abs(x)`  定义为：
- 如果  `x >= 0`  ，那么值为  `x`  。
- 如果  `x < 0`  ，那么值为 `-x`  。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-40-26-diagram-drawio-diagrams-net.png" style="width: 300px; height: 300px;" />
```

输入：points = [[1,2,3],[1,5,1],[3,1,1]]
输出：9
解释：
蓝色格子是最优方案选中的格子，坐标分别为 (0, 2)，(1, 1) 和 (2, 0) 。
你的总得分增加 3 + 5 + 3 = 11 。
但是你的总得分需要扣除 abs(2 - 1) + abs(1 - 0) = 2 。
你的最终得分为 11 - 2 = 9 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/12/screenshot-2021-07-12-at-13-42-14-diagram-drawio-diagrams-net.png" style="width: 200px; height: 299px;" />
```

输入：points = [[1,5],[2,3],[4,2]]
输出：11
解释：
蓝色格子是最优方案选中的格子，坐标分别为 (0, 1)，(1, 1) 和 (2, 0) 。
你的总得分增加 5 + 3 + 4 = 12 。
但是你的总得分需要扣除 abs(1 - 1) + abs(1 - 0) = 1 。
你的最终得分为 12 - 1 = 11 。

```
 

 **提示：** 
-  `m == points.length` 
-  `n == points[r].length` 
-  `1 <= m, n <= 10^5` 
-  `1 <= m * n <= 10^5` 
-  `0 <= points[r][c] <= 10^5` 
 
**标签**



## 
```python

```
>
# 1938.查询最大基因差
[https://leetcode-cn.com/problems/maximum-genetic-difference-query](https://leetcode-cn.com/problems/maximum-genetic-difference-query) 
## 原题
给你一棵 `n`  个节点的有根树，节点编号从  `0`  到  `n - 1`  。每个节点的编号表示这个节点的 **独一无二的基因值**  （也就是说节点 `x`  的基因值为 `x` ）。两个基因值的 **基因差**  是两者的 **异或和**  。给你整数数组  `parents`  ，其中  `parents[i]`  是节点 `i`  的父节点。如果节点 `x`  是树的 **根**  ，那么  `parents[x] == -1`  。

给你查询数组  `queries`  ，其中  `queries[i] = [node<sub>i</sub>, val<sub>i</sub>]`  。对于查询  `i`  ，请你找到 `val<sub>i</sub>`  和 `p<sub>i</sub>`  的 **最大基因差**  ，其中  `p<sub>i</sub>`  是节点 `node<sub>i</sub>`  到根之间的任意节点（包含 `node<sub>i</sub>`  和根节点）。更正式的，你想要最大化  `val<sub>i</sub> XOR p<sub>i</sub>` <sub> </sub>。

请你返回数组 * * `ans`  ，其中  `ans[i]`  是第 `i`  个查询的答案。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/29/c1.png" style="width: 118px; height: 163px;">
```
输入：parents = [-1,0,1,1], queries = [[0,2],[3,2],[2,5]]
输出：[2,3,7]
解释：查询数组处理如下：
- [0,2]：最大基因差的对应节点为 0 ，基因差为 2 XOR 0 = 2 。
- [3,2]：最大基因差的对应节点为 1 ，基因差为 2 XOR 1 = 3 。
- [2,5]：最大基因差的对应节点为 2 ，基因差为 5 XOR 2 = 7 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/29/c2.png" style="width: 256px; height: 221px;">
```
输入：parents = [3,7,-1,2,0,7,0,2], queries = [[4,6],[1,15],[0,5]]
输出：[6,14,7]
解释：查询数组处理如下：
- [4,6]：最大基因差的对应节点为 0 ，基因差为 6 XOR 0 = 6 。
- [1,15]：最大基因差的对应节点为 1 ，基因差为 15 XOR 1 = 14 。
- [0,5]：最大基因差的对应节点为 2 ，基因差为 5 XOR 2 = 7 。

```
 

 **提示：** 
-  `2 <= parents.length <= 10^5` 
- 对于每个  **不是**  根节点的  `i`  ，有  `0 <= parents[i] <= parents.length - 1`  。
-  `parents[root] == -1` 
-  `1 <= queries.length <= 3 * 10^4` 
-  `0 <= node<sub>i</sub> <= parents.length - 1` 
-  `0 <= val<sub>i</sub> <= 2 * 10^5` 
 
**标签**



## 
```python

```
>
# 1939.主动请求确认消息的用户
[https://leetcode-cn.com/problems/users-that-actively-request-confirmation-messages](https://leetcode-cn.com/problems/users-that-actively-request-confirmation-messages) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1940.排序数组之间的最长公共子序列
[https://leetcode-cn.com/problems/longest-common-subsequence-between-sorted-arrays](https://leetcode-cn.com/problems/longest-common-subsequence-between-sorted-arrays) 
## 原题

 
**标签**
`数组` `哈希表` `计数` 


## 
```python

```
>
# 1941.检查是否所有字符出现次数相同
[https://leetcode-cn.com/problems/check-if-all-characters-have-equal-number-of-occurrences](https://leetcode-cn.com/problems/check-if-all-characters-have-equal-number-of-occurrences) 
## 原题
给你一个字符串  `s`  ，如果 `s`  是一个 **好**  字符串，请你返回 `true`  ，否则请返回 `false`  。

如果 `s`  中出现过的  **所有** 字符的出现次数 **相同**  ，那么我们称字符串 `s`  是 **好**  字符串。

 

 **示例 1：** 

```
输入：s = "abacbc"
输出：true
解释：s 中出现过的字符为 'a'，'b' 和 'c' 。s 中所有字符均出现 2 次。

```
 **示例 2：** 

```
输入：s = "aaabb"
输出：false
解释：s 中出现过的字符为 'a' 和 'b' 。
'a' 出现了 3 次，'b' 出现了 2 次，两者出现次数不同。

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s`  只包含小写英文字母。
 
**标签**
`哈希表` `字符串` `计数` 


## 
```python

```
>
# 1942.最小未被占据椅子的编号
[https://leetcode-cn.com/problems/the-number-of-the-smallest-unoccupied-chair](https://leetcode-cn.com/problems/the-number-of-the-smallest-unoccupied-chair) 
## 原题
有 `n`  个朋友在举办一个派对，这些朋友从 `0`  到 `n - 1`  编号。派对里有 **无数**  张椅子，编号为 `0`  到 `infinity`  。当一个朋友到达派对时，他会占据  **编号最小**  且未被占据的椅子。
- 比方说，当一个朋友到达时，如果椅子  `0`  ， `1`  和  `5`  被占据了，那么他会占据  `2`  号椅子。
当一个朋友离开派对时，他的椅子会立刻变成未占据状态。如果同一时刻有另一个朋友到达，可以立即占据这张椅子。

给你一个下标从 **0**  开始的二维整数数组  `times`  ，其中  `times[i] = [arrival<sub>i</sub>, leaving<sub>i</sub>]`  表示第 `i`  个朋友到达和离开的时刻，同时给你一个整数 `targetFriend`  。所有到达时间 **互不相同**  。

请你返回编号为 `targetFriend`  的朋友占据的 **椅子编号**  。

 

 **示例 1：** 

```
输入：times = [[1,4],[2,3],[4,6]], targetFriend = 1
输出：1
解释：
- 朋友 0 时刻 1 到达，占据椅子 0 。
- 朋友 1 时刻 2 到达，占据椅子 1 。
- 朋友 1 时刻 3 离开，椅子 1 变成未占据。
- 朋友 0 时刻 4 离开，椅子 0 变成未占据。
- 朋友 2 时刻 4 到达，占据椅子 0 。
朋友 1 占据椅子 1 ，所以返回 1 。

```
 **示例 2：** 

```
输入：times = [[3,10],[1,5],[2,6]], targetFriend = 0
输出：2
解释：
- 朋友 1 时刻 1 到达，占据椅子 0 。
- 朋友 2 时刻 2 到达，占据椅子 1 。
- 朋友 0 时刻 3 到达，占据椅子 2 。
- 朋友 1 时刻 5 离开，椅子 0 变成未占据。
- 朋友 2 时刻 6 离开，椅子 1 变成未占据。
- 朋友 0 时刻 10 离开，椅子 2 变成未占据。
朋友 0 占据椅子 2 ，所以返回 2 。

```
 

 **提示：** 
-  `n == times.length` 
-  `2 <= n <= 10^4` 
-  `times[i].length == 2` 
-  `1 <= arrival<sub>i</sub> < leaving<sub>i</sub> <= 10^5` 
-  `0 <= targetFriend <= n - 1` 
- 每个  `arrival<sub>i</sub>`  时刻  **互不相同**  。
 
**标签**
`数组` `有序集合` `堆（优先队列）` 


## 
```python

```
>
# 1943.描述绘画结果
[https://leetcode-cn.com/problems/describe-the-painting](https://leetcode-cn.com/problems/describe-the-painting) 
## 原题
给你一个细长的画，用数轴表示。这幅画由若干有重叠的线段表示，每个线段有 **独一无二** 的颜色。给你二维整数数组 `segments` ，其中 `segments[i] = [start<sub>i</sub>, end<sub>i</sub>, color<sub>i</sub>]` 表示线段为 **半开区间** `[start<sub>i</sub>, end<sub>i</sub>)` 且颜色为 `color<sub>i</sub>` 。

线段间重叠部分的颜色会被 **混合** 。如果有两种或者更多颜色混合时，它们会形成一种新的颜色，用一个 **集合** 表示这个混合颜色。
- 比方说，如果颜色 `2` ， `4` 和 `6` 被混合，那么结果颜色为 `{2,4,6}` 。
为了简化题目，你不需要输出整个集合，只需要用集合中所有元素的 **和** 来表示颜色集合。

你想要用 **最少数目** 不重叠 **半开区间** 来 <b>表示</b> 这幅混合颜色的画。这些线段可以用二维数组 `painting` 表示，其中 `painting[j] = [left<sub>j</sub>, right<sub>j</sub>, mix<sub>j</sub>]` 表示一个 **半开区间** `[left<sub>j</sub>, right<sub>j</sub>)` 的颜色 **和** 为 `mix<sub>j</sub>` 。
- 比方说，这幅画由 `segments = [[1,4,5],[1,7,7]]` 组成，那么它可以表示为 `painting = [[1,4,12],[4,7,7]]` ，因为：

	
-  `[1,4)` 由颜色 `{5,7}` 组成（和为 `12` ），分别来自第一个线段和第二个线段。
-  `[4,7)` 由颜色 `{7}` 组成，来自第二个线段。
	
	
请你返回二维数组 `painting` ，它表示最终绘画的结果（ **没有** 被涂色的部分不出现在结果中）。你可以按 **任意顺序** 返回最终数组的结果。

 **半开区间** `[a, b)` 是数轴上点 `a` 和点 `b` 之间的部分， **包含** 点 `a` 且 **不包含** 点 `b` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/18/1.png" style="width: 529px; height: 241px;">
```
输入：segments = [[1,4,5],[4,7,7],[1,7,9]]
输出：[[1,4,14],[4,7,16]]
解释：绘画借故偶可以表示为：
- [1,4) 颜色为 {5,9} （和为 14），分别来自第一和第二个线段。
- [4,7) 颜色为 {7,9} （和为 16），分别来自第二和第三个线段。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/18/2.png" style="width: 532px; height: 219px;">
```
输入：segments = [[1,7,9],[6,8,15],[8,10,7]]
输出：[[1,6,9],[6,7,24],[7,8,15],[8,10,7]]
解释：绘画结果可以以表示为：
- [1,6) 颜色为 9 ，来自第一个线段。
- [6,7) 颜色为 {9,15} （和为 24），来自第一和第二个线段。
- [7,8) 颜色为 15 ，来自第二个线段。
- [8,10) 颜色为 7 ，来自第三个线段。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/04/c1.png" style="width: 529px; height: 289px;">
```
输入：segments = [[1,4,5],[1,4,7],[4,7,1],[4,7,11]]
输出：[[1,4,12],[4,7,12]]
解释：绘画结果可以表示为：
- [1,4) 颜色为 {5,7} （和为 12），分别来自第一和第二个线段。
- [4,7) 颜色为 {1,11} （和为 12），分别来自第三和第四个线段。
注意，只返回一个单独的线段 [1,7) 是不正确的，因为混合颜色的集合不相同。

```
 

 **提示：** 
-  `1 <= segments.length <= 2 * 10^4` 
-  `segments[i].length == 3` 
-  `1 <= start<sub>i</sub> < end<sub>i</sub> <= 10^5` 
-  `1 <= color<sub>i</sub> <= 10^9` 
- 每种颜色 `color<sub>i</sub>` 互不相同。
 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 1944.队列中可以看到的人数
[https://leetcode-cn.com/problems/number-of-visible-people-in-a-queue](https://leetcode-cn.com/problems/number-of-visible-people-in-a-queue) 
## 原题
有 `n` 个人排成一个队列， **从左到右** 编号为 `0` 到 `n - 1` 。给你以一个整数数组 `heights` ，每个整数 **互不相同** ， `heights[i]` 表示第 `i` 个人的高度。

一个人能 **看到** 他右边另一个人的条件是这两人之间的所有人都比他们两人 **矮** 。更正式的，第 `i` 个人能看到第 `j` 个人的条件是 `i < j` 且 `min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1])` 。

请你返回一个长度为 `n` 的数组 `answer` ，其中 `answer[i]` 是第 `i` 个人在他右侧队列中能 **看到** 的 **人数** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/05/29/queue-plane.jpg" style="width: 600px; height: 247px;" />

```

输入：heights = [10,6,8,5,11,9]
输出：[3,1,2,1,1,0]
解释：
第 0 个人能看到编号为 1 ，2 和 4 的人。
第 1 个人能看到编号为 2 的人。
第 2 个人能看到编号为 3 和 4 的人。
第 3 个人能看到编号为 4 的人。
第 4 个人能看到编号为 5 的人。
第 5 个人谁也看不到因为他右边没人。

```
 **示例 2：** 

```

输入：heights = [5,1,2,3,10]
输出：[4,1,1,1,0]

```
 

 **提示：** 
-  `n == heights.length` 
-  `1 <= n <= 10^5` 
-  `1 <= heights[i] <= 10^5` 
-  `heights` 中所有数 **互不相同** 。
 
**标签**
`栈` `数组` `单调栈` 


## 
```python

```
>
# 1945.字符串转化后的各位数字之和
[https://leetcode-cn.com/problems/sum-of-digits-of-string-after-convert](https://leetcode-cn.com/problems/sum-of-digits-of-string-after-convert) 
## 原题
给你一个由小写字母组成的字符串 `s` ，以及一个整数 `k` 。

首先，用字母在字母表中的位置替换该字母，将 `s` **转化** 为一个整数（也就是， `'a'` 用 `1` 替换， `'b'` 用 `2` 替换，... `'z'` 用 `26` 替换）。接着，将整数 **转换** 为其 **各位数字之和** 。共重复 **转换** 操作 ** `k` 次** 。

例如，如果 `s = "zbax"` 且 `k = 2` ，那么执行下述步骤后得到的结果是整数 `8` ：
-  **转化：** `"zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124` 
-  **转换 #1** ： `262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17` 
-  **转换 #2** ： `17 ➝ 1 + 7 ➝ 8` 
返回执行上述操作后得到的结果整数。

 

 **示例 1：** 

```

输入：s = "iiii", k = 1
输出：36
解释：操作如下：
- 转化："iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- 转换 #1：9999 ➝ 9 + 9 + 9 + 9 ➝ 36
因此，结果整数为 36 。

```
 **示例 2：** 

```

输入：s = "leetcode", k = 2
输出：6
解释：操作如下：
- 转化："leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- 转换 #1：12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- 转换 #2：33 ➝ 3 + 3 ➝ 6
因此，结果整数为 6 。

```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `1 <= k <= 10` 
-  `s` 由小写英文字母组成
 
**标签**
`字符串` `模拟` 


## 
```python

```
>
# 1946.子字符串突变后可能得到的最大整数
[https://leetcode-cn.com/problems/largest-number-after-mutating-substring](https://leetcode-cn.com/problems/largest-number-after-mutating-substring) 
## 原题
给你一个字符串 `num` ，该字符串表示一个大整数。另给你一个长度为 `10` 且 **下标从 0  开始** 的整数数组 `change` ，该数组将 `0-9` 中的每个数字映射到另一个数字。更规范的说法是，数字 `d` 映射为数字 `change[d]` 。

你可以选择 **突变** `num` 的任一子字符串。 **突变** 子字符串意味着将每位数字 `num[i]` 替换为该数字在 `change` 中的映射（也就是说，将 `num[i]` 替换为 `change[num[i]]` ）。

请你找出在对 `num` 的任一子字符串执行突变操作（也可以不执行）后，可能得到的 **最大整数** ，并用字符串表示返回。

 **子字符串** 是字符串中的一个连续序列。

 

 **示例 1：** 

```
输入：num = "132", change = [9,8,5,0,3,6,4,2,6,8]
输出："832"
解释：替换子字符串 "1"：
- 1 映射为 change[1] = 8 。
因此 "132" 变为 "832" 。
"832" 是可以构造的最大整数，所以返回它的字符串表示。

```
 **示例 2：** 

```
输入：num = "021", change = [9,4,3,5,7,2,1,9,0,6]
输出："934"
解释：替换子字符串 "021"：
- 0 映射为 change[0] = 9 。
- 2 映射为 change[2] = 3 。
- 1 映射为 change[1] = 4 。
因此，"021" 变为 "934" 。
"934" 是可以构造的最大整数，所以返回它的字符串表示。 

```
 **示例 3：** 

```
输入：num = "5", change = [1,4,7,5,3,2,5,6,9,4]
输出："5"
解释："5" 已经是可以构造的最大整数，所以返回它的字符串表示。

```
 

 **提示：** 
-  `1 <= num.length <= 10^5` 
-  `num` 仅由数字 `0-9` 组成
-  `change.length == 10` 
-  `0 <= change[d] <= 9` 
 
**标签**
`贪心` `数组` `字符串` 


## 
```python

```
>
# 1947.最大兼容性评分和
[https://leetcode-cn.com/problems/maximum-compatibility-score-sum](https://leetcode-cn.com/problems/maximum-compatibility-score-sum) 
## 原题
有一份由 `n` 个问题组成的调查问卷，每个问题的答案要么是 `0` （no，否），要么是 `1` （yes，是）。

这份调查问卷被分发给 `m` 名学生和 `m` 名导师，学生和导师的编号都是从 `0` 到 `m - 1` 。学生的答案用一个二维整数数组 `students` 表示，其中 `students[i]` 是一个整数数组，包含第 `i` 名学生对调查问卷给出的答案（ **下标从 0 开始** ）。导师的答案用一个二维整数数组 `mentors` 表示，其中 `mentors[j]` 是一个整数数组，包含第 `j` 名导师对调查问卷给出的答案（ **下标从 0 开始** ）。

每个学生都会被分配给 **一名** 导师，而每位导师也会分配到 **一名** 学生。配对的学生与导师之间的兼容性评分等于学生和导师答案相同的次数。
- 例如，学生答案为 `[1, ** *0* ** , ** *1* ** ]` 而导师答案为 `[0, ** *0* ** , ** *1* ** ]` ，那么他们的兼容性评分为 2 ，因为只有第二个和第三个答案相同。
请你找出最优的学生与导师的配对方案，以 **最大程度上** 提高 **兼容性评分和** 。

给你 `students` 和 `mentors` ，返回可以得到的 **最大兼容性评分和** 。

 

 **示例 1：** 

```
输入：students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]
输出：8
解释：按下述方式分配学生和导师：
- 学生 0 分配给导师 2 ，兼容性评分为 3 。
- 学生 1 分配给导师 0 ，兼容性评分为 2 。
- 学生 2 分配给导师 1 ，兼容性评分为 3 。
最大兼容性评分和为 3 + 2 + 3 = 8 。
```
 **示例 2：** 

```
输入：students = [[0,0],[0,0],[0,0]], mentors = [[1,1],[1,1],[1,1]]
输出：0
解释：任意学生与导师配对的兼容性评分都是 0 。

```
 

 **提示：** 
-  `m == students.length == mentors.length` 
-  `n == students[i].length == mentors[j].length` 
-  `1 <= m, n <= 8` 
-  `students[i][k]` 为 `0` 或 `1` 
-  `mentors[j][k]` 为 `0` 或 `1` 
 
**标签**
`位运算` `数组` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 1948.删除系统中的重复文件夹
[https://leetcode-cn.com/problems/delete-duplicate-folders-in-system](https://leetcode-cn.com/problems/delete-duplicate-folders-in-system) 
## 原题
由于一个漏洞，文件系统中存在许多重复文件夹。给你一个二维数组 `paths` ，其中 `paths[i]` 是一个表示文件系统中第 `i` 个文件夹的绝对路径的数组。
- 例如， `["one", "two", "three"]` 表示路径 `"/one/two/three"` 。
如果两个文件夹（不需要在同一层级）包含 **非空且** <b>相同的 </b>子文件夹 **集合** 并具有相同的子文件夹结构，则认为这两个文件夹是相同文件夹。相同文件夹的根层级 **不** 需要相同。如果存在两个（或两个以上） **相同** 文件夹，则需要将这些文件夹和所有它们的子文件夹 **标记** 为待删除。
- 例如，下面文件结构中的文件夹 `"/a"` 和 `"/b"` 相同。它们（以及它们的子文件夹）应该被 **全部** 标记为待删除：

	
-  `/a` 
-  `/a/x` 
-  `/a/x/y` 
-  `/a/z` 
-  `/b` 
-  `/b/x` 
-  `/b/x/y` 
-  `/b/z` 
	
	
- 然而，如果文件结构中还包含路径 `"/b/w"` ，那么文件夹 `"/a"` 和 `"/b"` 就不相同。注意，即便添加了新的文件夹 `"/b/w"` ，仍然认为 `"/a/x"` 和 `"/b/x"` 相同。
一旦所有的相同文件夹和它们的子文件夹都被标记为待删除，文件系统将会 **删除** 所有上述文件夹。文件系统只会执行一次删除操作。执行完这一次删除操作后，不会删除新出现的相同文件夹。

返回二维数组 `ans` ，该数组包含删除所有标记文件夹之后剩余文件夹的路径。路径可以按 **任意顺序** 返回。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/19/lc-dupfolder1.jpg" style="width: 200px; height: 218px;" />
```

输入：paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
输出：[["d"],["d","a"]]
解释：文件结构如上所示。
文件夹 "/a" 和 "/c"（以及它们的子文件夹）都会被标记为待删除，因为它们都包含名为 "b" 的空文件夹。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/19/lc-dupfolder2.jpg" style="width: 200px; height: 355px;" />
```

输入：paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
输出：[["c"],["c","b"],["a"],["a","b"]]
解释：文件结构如上所示。
文件夹 "/a/b/x" 和 "/w"（以及它们的子文件夹）都会被标记为待删除，因为它们都包含名为 "y" 的空文件夹。
注意，文件夹 "/a" 和 "/c" 在删除后变为相同文件夹，但这两个文件夹不会被删除，因为删除只会进行一次，且它们没有在删除前被标记。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/19/lc-dupfolder3.jpg" style="width: 200px; height: 201px;" />
```

输入：paths = [["a","b"],["c","d"],["c"],["a"]]
输出：[["c"],["c","d"],["a"],["a","b"]]
解释：文件系统中所有文件夹互不相同。
注意，返回的数组可以按不同顺序返回文件夹路径，因为题目对顺序没有要求。

```
 **示例 4：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/19/lc-dupfolder4_.jpg" style="width: 300px; height: 290px;" />
```

输入：paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"]]
输出：[]
解释：文件结构如上所示。
文件夹 "/a/x" 和 "/b/x"（以及它们的子文件夹）都会被标记为待删除，因为它们都包含名为 "y" 的空文件夹。
文件夹 "/a" 和 "/b"（以及它们的子文件夹）都会被标记为待删除，因为它们都包含一个名为 "z" 的空文件夹以及上面提到的文件夹 "x" 。

```
 **示例 5：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/19/lc-dupfolder5_.jpg" style="width: 300px; height: 282px;" />
```

输入：paths = [["a"],["a","x"],["a","x","y"],["a","z"],["b"],["b","x"],["b","x","y"],["b","z"],["b","w"]]
输出：[["b"],["b","w"],["b","z"],["a"],["a","z"]]
解释：本例与上例的结构基本相同，除了新增 "/b/w" 文件夹。
文件夹 "/a/x" 和 "/b/x" 仍然会被标记，但 "/a" 和 "/b" 不再被标记，因为 "/b" 中有名为 "w" 的空文件夹而 "/a" 没有。
注意，"/a/z" 和 "/b/z" 不会被标记，因为相同子文件夹的集合必须是非空集合，但这两个文件夹都是空的。

```
 

 **提示：** 
-  `1 <= paths.length <= 2 * 10^4` 
-  `1 <= paths[i].length <= 500` 
-  `1 <= paths[i][j].length <= 10` 
-  `1 <= sum(paths[i][j].length) <= 2 * 10^5` 
-  `path[i][j]` 由小写英文字母组成
- 不会存在两个路径都指向同一个文件夹的情况
- 对于不在根层级的任意文件夹，其父文件夹也会包含在输入中
 
**标签**
`字典树` `数组` `哈希表` `字符串` `哈希函数` 


## 
```python

```
>
# 1949.坚定的友谊
[https://leetcode-cn.com/problems/strong-friendship](https://leetcode-cn.com/problems/strong-friendship) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1950.所有子数组最小值中的最大值
[https://leetcode-cn.com/problems/maximum-of-minimum-values-in-all-subarrays](https://leetcode-cn.com/problems/maximum-of-minimum-values-in-all-subarrays) 
## 原题

 
**标签**
`栈` `数组` `单调栈` 


## 
```python

```
>
# 1951.查询具有最多共同关注者的所有两两结对组
[https://leetcode-cn.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers](https://leetcode-cn.com/problems/all-the-pairs-with-the-maximum-number-of-common-followers) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1952.三除数
[https://leetcode-cn.com/problems/three-divisors](https://leetcode-cn.com/problems/three-divisors) 
## 原题
给你一个整数 `n` 。如果 `n` **恰好有三个正除数** ，返回 `true` ；否则，返回 `false` 。

如果存在整数 `k` ，满足 `n = k * m` ，那么整数 `m` 就是 `n` 的一个 **除数** 。

 

 **示例 1：** 

```
输入：n = 2
输出：false
解释：2 只有两个除数：1 和 2 。
```
 **示例 2：** 

```
输入：n = 4
输出：true
解释：4 有三个除数：1、2 和 4 。

```
 

 **提示：** 
-  `1 <= n <= 10^4` 
 
**标签**
`数学` 


## 
```python

```
>
# 1953.你可以工作的最大周数
[https://leetcode-cn.com/problems/maximum-number-of-weeks-for-which-you-can-work](https://leetcode-cn.com/problems/maximum-number-of-weeks-for-which-you-can-work) 
## 原题
给你 `n` 个项目，编号从 `0` 到 `n - 1` 。同时给你一个整数数组 `milestones` ，其中每个 `milestones[i]` 表示第 `i` 个项目中的阶段任务数量。

你可以按下面两个规则参与项目中的工作：
- 每周，你将会完成 **某一个** 项目中的 **恰好一个** 阶段任务。你每周都 **必须** 工作。
- 在 **连续的** 两周中，你 **不能** 参与并完成同一个项目中的两个阶段任务。
一旦所有项目中的全部阶段任务都完成，或者仅剩余一个阶段任务都会导致你违反上面的规则，那么你将 **停止工作** 。注意，由于这些条件的限制，你可能无法完成所有阶段任务。

返回在不违反上面规则的情况下你 **最多** 能工作多少周。

 

 **示例 1：** 

```

输入：milestones = [1,2,3]
输出：6
解释：一种可能的情形是：
​​​​- 第 1 周，你参与并完成项目 0 中的一个阶段任务。
- 第 2 周，你参与并完成项目 2 中的一个阶段任务。
- 第 3 周，你参与并完成项目 1 中的一个阶段任务。
- 第 4 周，你参与并完成项目 2 中的一个阶段任务。
- 第 5 周，你参与并完成项目 1 中的一个阶段任务。
- 第 6 周，你参与并完成项目 2 中的一个阶段任务。
总周数是 6 。

```
 **示例 2：** 

```

输入：milestones = [5,2,1]
输出：7
解释：一种可能的情形是：
- 第 1 周，你参与并完成项目 0 中的一个阶段任务。
- 第 2 周，你参与并完成项目 1 中的一个阶段任务。
- 第 3 周，你参与并完成项目 0 中的一个阶段任务。
- 第 4 周，你参与并完成项目 1 中的一个阶段任务。
- 第 5 周，你参与并完成项目 0 中的一个阶段任务。
- 第 6 周，你参与并完成项目 2 中的一个阶段任务。
- 第 7 周，你参与并完成项目 0 中的一个阶段任务。
总周数是 7 。
注意，你不能在第 8 周参与完成项目 0 中的最后一个阶段任务，因为这会违反规则。
因此，项目 0 中会有一个阶段任务维持未完成状态。
```
 

 **提示：** 
-  `n == milestones.length` 
-  `1 <= n <= 10^5` 
-  `1 <= milestones[i] <= 10^9` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1954.收集足够苹果的最小花园周长
[https://leetcode-cn.com/problems/minimum-garden-perimeter-to-collect-enough-apples](https://leetcode-cn.com/problems/minimum-garden-perimeter-to-collect-enough-apples) 
## 原题
给你一个用无限二维网格表示的花园， **每一个** 整数坐标处都有一棵苹果树。整数坐标 `(i, j)` 处的苹果树有 `|i| + |j|` 个苹果。

你将会买下正中心坐标是 `(0, 0)` 的一块 **正方形土地** ，且每条边都与两条坐标轴之一平行。

给你一个整数 `neededApples` ，请你返回土地的 **最小周长** ，使得 **至少** 有 **** `neededApples` 个苹果在土地 **里面或者边缘上** 。

 `|x|` 的值定义为：
- 如果 `x >= 0` ，那么值为 `x` 
- 如果 `x < 0` ，那么值为 `-x` 
 

 **示例 1：** 
<img alt="" src="https://pic.leetcode-cn.com/1627790803-qcBKFw-image.png" style="width: 442px; height: 449px;" />
```

输入：neededApples = 1
输出：8
解释：边长长度为 1 的正方形不包含任何苹果。
但是边长为 2 的正方形包含 12 个苹果（如上图所示）。
周长为 2 * 4 = 8 。

```
 **示例 2：** 

```

输入：neededApples = 13
输出：16

```
 **示例 3：** 

```

输入：neededApples = 1000000000
输出：5040

```
 

 **提示：** 
-  `1 <= neededApples <= 10^15` 
 
**标签**
`数学` `二分查找` 


## 
```python

```
>
# 1955.统计特殊子序列的数目
[https://leetcode-cn.com/problems/count-number-of-special-subsequences](https://leetcode-cn.com/problems/count-number-of-special-subsequences) 
## 原题
 **特殊序列** 是由 **正整数** 个 `0` ，紧接着 **正整数** 个 `1` ，最后 **正整数** 个 `2` 组成的序列。
- 比方说， `[0,1,2]` 和 `[0,0,1,1,1,2]` 是特殊序列。
- 相反， `[2,1,0]` ， `[1]` 和 `[0,1,2,0]` 就不是特殊序列。
给你一个数组 `nums` （ **仅** 包含整数 `0` ， `1` 和 `2` ），请你返回 <b>不同特殊子序列的数目</b> 。由于答案可能很大，请你将它对 `10^9 + 7` **取余** 后返回。

一个数组的 **子序列** 是从原数组中删除零个或者若干个元素后，剩下元素不改变顺序得到的序列。如果两个子序列的 **下标集合** 不同，那么这两个子序列是 **不同的** 。

 

 **示例 1：** 

```

输入：nums = [0,1,2,2]
输出：3
解释：特殊子序列为 [0,1,2,2]，[0,1,2,2] 和 [0,1,2,2] 。

```
 **示例 2：** 

```

输入：nums = [2,2,0,0]
输出：0
解释：数组 [2,2,0,0] 中没有特殊子序列。

```
 **示例 3：** 

```

输入：nums = [0,1,2,0,1,2]
输出：7
解释：特殊子序列包括：
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]
- [0,1,2,0,1,2]

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 2` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1956.感染 K 种病毒所需的最短时间
[https://leetcode-cn.com/problems/minimum-time-for-k-virus-variants-to-spread](https://leetcode-cn.com/problems/minimum-time-for-k-virus-variants-to-spread) 
## 原题

 
**标签**
`几何` `数组` `数学` `二分查找` `枚举` 


## 
```python

```
>
# 1957.删除字符使字符串变好
[https://leetcode-cn.com/problems/delete-characters-to-make-fancy-string](https://leetcode-cn.com/problems/delete-characters-to-make-fancy-string) 
## 原题
一个字符串如果没有 **三个连续** 相同字符，那么它就是一个 **好字符串** 。

给你一个字符串 `s` ，请你从 `s` 删除 **最少** 的字符，使它变成一个 **好字符串** 。

请你返回删除后的字符串。题目数据保证答案总是 **唯一的** 。

 

 **示例 1：** 

```

输入：s = "leeetcode"
输出："leetcode"
解释：
从第一组 'e' 里面删除一个 'e' ，得到 "leetcode" 。
没有连续三个相同字符，所以返回 "leetcode" 。

```
 **示例 2：** 

```

输入：s = "aaabaaaa"
输出："aabaa"
解释：
从第一组 'a' 里面删除一个 'a' ，得到 "aabaaaa" 。
从第二组 'a' 里面删除两个 'a' ，得到 "aabaa" 。
没有连续三个相同字符，所以返回 "aabaa" 。

```
 **示例 3：** 

```

输入：s = "aab"
输出："aab"
解释：没有连续三个相同字符，所以返回 "aab" 。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s` 只包含小写英文字母。
 
**标签**
`字符串` 


## 
```python

```
>
# 1958.检查操作是否合法
[https://leetcode-cn.com/problems/check-if-move-is-legal](https://leetcode-cn.com/problems/check-if-move-is-legal) 
## 原题
给你一个下标从 **0** 开始的 `8 x 8` 网格 `board` ，其中 `board[r][c]` 表示游戏棋盘上的格子 `(r, c)` 。棋盘上空格用 `'.'` 表示，白色格子用 `'W'` 表示，黑色格子用 `'B'` 表示。

游戏中每次操作步骤为：选择一个空格子，将它变成你正在执行的颜色（要么白色，要么黑色）。但是， **合法** 操作必须满足：涂色后这个格子是 **好线段的一个端点** （好线段可以是水平的，竖直的或者是对角线）。

 **好线段** 指的是一个包含 **三个或者更多格子（包含端点格子）** 的线段，线段两个端点格子为 **同一种颜色** ，且中间剩余格子的颜色都为 **另一种颜色** （线段上不能有任何空格子）。你可以在下图找到好线段的例子：
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/22/goodlines5.png" style="width: 500px; height: 312px;" />
给你两个整数 `rMove` 和 `cMove` 以及一个字符 `color` ，表示你正在执行操作的颜色（白或者黑），如果将格子 `(rMove, cMove)` 变成颜色 `color` 后，是一个 **合法** 操作，那么返回 `true` ，如果不是合法操作返回 `false` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/07/10/grid11.png" style="width: 350px; height: 350px;" />

```

输入：board = [[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],[".",".",".","W",".",".",".","."],["W","B","B",".","W","W","W","B"],[".",".",".","B",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","W",".",".",".","."]], rMove = 4, cMove = 3, color = "B"
输出：true
解释：'.'，'W' 和 'B' 分别用颜色蓝色，白色和黑色表示。格子 (rMove, cMove) 用 'X' 标记。
以选中格子为端点的两个好线段在上图中用红色矩形标注出来了。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/07/10/grid2.png" style="width: 350px; height: 351px;" />

```

输入：board = [[".",".",".",".",".",".",".","."],[".","B",".",".","W",".",".","."],[".",".","W",".",".",".",".","."],[".",".",".","W","B",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".","B","W",".","."],[".",".",".",".",".",".","W","."],[".",".",".",".",".",".",".","B"]], rMove = 4, cMove = 4, color = "W"
输出：false
解释：虽然选中格子涂色后，棋盘上产生了好线段，但选中格子是作为中间格子，没有产生以选中格子为端点的好线段。

```
 

 **提示：** 
-  `board.length == board[r].length == 8` 
-  `0 <= rMove, cMove < 8` 
-  `board[rMove][cMove] == '.'` 
-  `color` 要么是 `'B'` 要么是 `'W'` 。
 
**标签**
`数组` `枚举` `矩阵` 


## 
```python

```
>
# 1959.K 次调整数组大小浪费的最小总空间
[https://leetcode-cn.com/problems/minimum-total-space-wasted-with-k-resizing-operations](https://leetcode-cn.com/problems/minimum-total-space-wasted-with-k-resizing-operations) 
## 原题
你正在设计一个动态数组。给你一个下标从 **0** 开始的整数数组 `nums` ，其中 `nums[i]` 是 `i` 时刻数组中的元素数目。除此以外，你还有一个整数 `k` ，表示你可以 **调整** 数组大小的 **最多** 次数（每次都可以调整成 **任意** 大小）。

 `t` 时刻数组的大小 `size<sub>t</sub>` 必须大于等于 `nums[t]` ，因为数组需要有足够的空间容纳所有元素。 `t` 时刻 **浪费的空间** 为 `size<sub>t</sub> - nums[t]` ， **总** 浪费空间为满足 `0 <= t < nums.length` 的每一个时刻 `t` 浪费的空间 **之和** 。

在调整数组大小不超过 `k` 次的前提下，请你返回 **最小总浪费空间** 。

 **注意：** 数组最开始时可以为 **任意大小** ，且 **不计入** 调整大小的操作次数。

 

 **示例 1：** 

```
输入：nums = [10,20], k = 0
输出：10
解释：size = [20,20].
我们可以让数组初始大小为 20 。
总浪费空间为 (20 - 10) + (20 - 20) = 10 。

```
 **示例 2：** 

```
输入：nums = [10,20,30], k = 1
输出：10
解释：size = [20,20,30].
我们可以让数组初始大小为 20 ，然后时刻 2 调整大小为 30 。
总浪费空间为 (20 - 10) + (20 - 20) + (30 - 30) = 10 。

```
 **示例 3：** 

```
输入：nums = [10,20,15,30,20], k = 2
输出：15
解释：size = [10,20,20,30,30].
我们可以让数组初始大小为 10 ，时刻 1 调整大小为 20 ，时刻 3 调整大小为 30 。
总浪费空间为 (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15 。

```
 

 **提示：** 
-  `1 <= nums.length <= 200` 
-  `1 <= nums[i] <= 10^6` 
-  `0 <= k <= nums.length - 1` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1960.两个回文子字符串长度的最大乘积
[https://leetcode-cn.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings](https://leetcode-cn.com/problems/maximum-product-of-the-length-of-two-palindromic-substrings) 
## 原题
给你一个下标从 **0** 开始的字符串 `s` ，你需要找到两个 **不重叠** **的回文** 子字符串，它们的长度都必须为 **奇数** ，使得它们长度的乘积最大。

更正式地，你想要选择四个整数 `i` ， `j` ， `k` ， `l` ，使得 `0 <= i <= j < k <= l < s.length` ，且子字符串 `s[i...j]` 和 `s[k...l]` 都是回文串且长度为奇数。 `s[i...j]` 表示下标从 `i` 到 `j` 且 **包含** 两端下标的子字符串。

请你返回两个不重叠回文子字符串长度的 **最大** 乘积。

 **回文字符串** 指的是一个从前往后读和从后往前读一模一样的字符串。 **子字符串** 指的是一个字符串中一段连续字符。

 

 **示例 1：** 

```

输入：s = "ababbb"
输出：9
解释：子字符串 "aba" 和 "bbb" 为奇数长度的回文串。乘积为 3 * 3 = 9 。

```
 **示例 2：** 

```

输入：s = "zaaaxbbby"
输出：9
解释：子字符串 "aaa" 和 "bbb" 为奇数长度的回文串。乘积为 3 * 3 = 9 。

```
 

 **提示：** 
-  `2 <= s.length <= 10^5` 
-  `s` 只包含小写英文字母。
 
**标签**
`字符串` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 1961.检查字符串是否为数组前缀
[https://leetcode-cn.com/problems/check-if-string-is-a-prefix-of-array](https://leetcode-cn.com/problems/check-if-string-is-a-prefix-of-array) 
## 原题
给你一个字符串 `s` 和一个字符串数组 `words` ，请你判断 `s` 是否为 `words` 的 **前缀字符串** 。

字符串 `s` 要成为 `words` 的 **前缀字符串** ，需要满足： `s` 可以由 `words` 中的前 `k` （ `k` 为 **正数** ）个字符串按顺序相连得到，且 `k` 不超过 `words.length` 。

如果 `s` 是 `words` 的 **前缀字符串** ，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：s = "iloveleetcode", words = ["i","love","leetcode","apples"]
输出：true
解释：
s 可以由 "i"、"love" 和 "leetcode" 相连得到。

```
 **示例 2：** 

```

输入：s = "iloveleetcode", words = ["apples","i","love","leetcode"]
输出：false
解释：
数组的前缀相连无法得到 s 。
```
 

 **提示：** 
-  `1 <= words.length <= 100` 
-  `1 <= words[i].length <= 20` 
-  `1 <= s.length <= 1000` 
-  `words[i]` 和 `s` 仅由小写英文字母组成
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 1962.移除石子使总数最小
[https://leetcode-cn.com/problems/remove-stones-to-minimize-the-total](https://leetcode-cn.com/problems/remove-stones-to-minimize-the-total) 
## 原题
给你一个整数数组 `piles` ，数组 **下标从 0 开始** ，其中 `piles[i]` 表示第 `i` 堆石子中的石子数量。另给你一个整数 `k` ，请你执行下述操作 **恰好** `k` 次：
- 选出任一石子堆 `piles[i]` ，并从中 **移除** `floor(piles[i] / 2)` 颗石子。
 **注意：** 你可以对 **同一堆** 石子多次执行此操作。

返回执行 `k` 次操作后，剩下石子的 **最小** 总数。

 `floor(x)` 为 **小于** 或 **等于** `x` 的 **最大** 整数。（即，对 `x` 向下取整）。

 

 **示例 1：** 

```

输入：piles = [5,4,9], k = 2
输出：12
解释：可能的执行情景如下：
- 对第 2 堆石子执行移除操作，石子分布情况变成 [5,4,5] 。
- 对第 0 堆石子执行移除操作，石子分布情况变成 [3,4,5] 。
剩下石子的总数为 12 。

```
 **示例 2：** 

```

输入：piles = [4,3,6,7], k = 3
输出：12
解释：可能的执行情景如下：
- 对第 2 堆石子执行移除操作，石子分布情况变成 [4,3,3,7] 。
- 对第 3 堆石子执行移除操作，石子分布情况变成 [4,3,3,4] 。
- 对第 0 堆石子执行移除操作，石子分布情况变成 [2,3,3,4] 。
剩下石子的总数为 12 。

```
 

 **提示：** 
-  `1 <= piles.length <= 10^5` 
-  `1 <= piles[i] <= 10^4` 
-  `1 <= k <= 10^5` 
 
**标签**
`数组` `堆（优先队列）` 


## 
```python

```
>
# 1963.使字符串平衡的最小交换次数
[https://leetcode-cn.com/problems/minimum-number-of-swaps-to-make-the-string-balanced](https://leetcode-cn.com/problems/minimum-number-of-swaps-to-make-the-string-balanced) 
## 原题
给你一个字符串 `s` ， **下标从 0 开始** ，且长度为偶数 `n` 。字符串 **恰好** 由 `n / 2` 个开括号 `'['` 和 `n / 2` 个闭括号 `']'` 组成。

只有能满足下述所有条件的字符串才能称为 **平衡字符串** ：
- 字符串是一个空字符串，或者
- 字符串可以记作 `AB` ，其中 `A` 和 `B` 都是 **平衡字符串** ，或者
- 字符串可以写成 `[C]` ，其中 `C` 是一个 **平衡字符串** 。
你可以交换 **任意** 两个下标所对应的括号 **任意** 次数。

返回使 `s` 变成 **平衡字符串** 所需要的 **最小** 交换次数。

 

 **示例 1：** 

```

输入：s = "][]["
输出：1
解释：交换下标 0 和下标 3 对应的括号，可以使字符串变成平衡字符串。
最终字符串变成 "[[]]" 。

```
 **示例 2：** 

```

输入：s = "]]][[["
输出：2
解释：执行下述操作可以使字符串变成平衡字符串：
- 交换下标 0 和下标 4 对应的括号，s = "[]][][" 。
- 交换下标 1 和下标 5 对应的括号，s = "[[][]]" 。
最终字符串变成 "[[][]]" 。

```
 **示例 3：** 

```

输入：s = "[]"
输出：0
解释：这个字符串已经是平衡字符串。

```
 

 **提示：** 
-  `n == s.length` 
-  `2 <= n <= 10^6` 
-  `n` 为偶数
-  `s[i]` 为 `'['` 或 `']'` 
- 开括号 `'['` 的数目为 `n / 2` ，闭括号 `']'` 的数目也是 `n / 2` 
 
**标签**
`栈` `贪心` `双指针` `字符串` 


## 
```python

```
>
# 1964.找出到每个位置为止最长的有效障碍赛跑路线
[https://leetcode-cn.com/problems/find-the-longest-valid-obstacle-course-at-each-position](https://leetcode-cn.com/problems/find-the-longest-valid-obstacle-course-at-each-position) 
## 原题
你打算构建一些障碍赛跑路线。给你一个 **下标从 0 开始** 的整数数组 `obstacles` ，数组长度为 `n` ，其中 `obstacles[i]` 表示第 `i` 个障碍的高度。

对于每个介于 `0` 和 `n - 1` 之间（包含 `0` 和 `n - 1` ）的下标 `i` ，在满足下述条件的前提下，请你找出 `obstacles` 能构成的最长障碍路线的长度：
- 你可以选择下标介于 `0` 到 `i` 之间（包含 `0` 和 `i` ）的任意个障碍。
- 在这条路线中，必须包含第 `i` 个障碍。
- 你必须按障碍在 `obstacles` 中的 **** **出现顺序** 布置这些障碍。
- 除第一个障碍外，路线中每个障碍的高度都必须和前一个障碍 **相同** 或者 **更高** 。
返回长度为 `n` 的答案数组 `ans` ，其中 `ans[i]` 是上面所述的下标 `i` 对应的最长障碍赛跑路线的长度。

 

 **示例 1：** 

```

输入：obstacles = [1,2,3,2]
输出：[1,2,3,3]
解释：每个位置的最长有效障碍路线是：
- i = 0: [1], [1] 长度为 1
- i = 1: [1,2], [1,2] 长度为 2
- i = 2: [1,2,3], [1,2,3] 长度为 3
- i = 3: [1,2,3,2], [1,2,2] 长度为 3

```
 **示例 2：** 

```

输入：obstacles = [2,2,1]
输出：[1,2,1]
解释：每个位置的最长有效障碍路线是：
- i = 0: [2], [2] 长度为 1
- i = 1: [2,2], [2,2] 长度为 2
- i = 2: [2,2,1], [1] 长度为 1

```
 **示例 3：** 

```

输入：obstacles = [3,1,5,6,4,2]
输出：[1,1,2,3,2,2]
解释：每个位置的最长有效障碍路线是：
- i = 0: [3], [3] 长度为 1
- i = 1: [3,1], [1] 长度为 1
- i = 2: [3,1,5], [3,5] 长度为 2, [1,5] 也是有效的障碍赛跑路线
- i = 3: [3,1,5,6], [3,5,6] 长度为 3, [1,5,6] 也是有效的障碍赛跑路线
- i = 4: [3,1,5,6,4], [3,4] 长度为 2, [1,4] 也是有效的障碍赛跑路线
- i = 5: [3,1,5,6,4,2], [1,2] 长度为 2

```
 

 **提示：** 
-  `n == obstacles.length` 
-  `1 <= n <= 10^5` 
-  `1 <= obstacles[i] <= 10^7` 
 
**标签**
`树状数组` `数组` `二分查找` 


## 
```python

```
>
# 1965.丢失信息的雇员
[https://leetcode-cn.com/problems/employees-with-missing-information](https://leetcode-cn.com/problems/employees-with-missing-information) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1966.未排序数组中的可被二分搜索的数
[https://leetcode-cn.com/problems/binary-searchable-numbers-in-an-unsorted-array](https://leetcode-cn.com/problems/binary-searchable-numbers-in-an-unsorted-array) 
## 原题

 
**标签**



## 
```python

```
>
# 1967.作为子字符串出现在单词中的字符串数目
[https://leetcode-cn.com/problems/number-of-strings-that-appear-as-substrings-in-word](https://leetcode-cn.com/problems/number-of-strings-that-appear-as-substrings-in-word) 
## 原题
给你一个字符串数组 `patterns` 和一个字符串 `word` ，统计 `patterns` 中有多少个字符串是 `word` 的子字符串。返回字符串数目。

 **子字符串** 是字符串中的一个连续字符序列。

 

 **示例 1：** 

```

输入：patterns = ["a","abc","bc","d"], word = "abc"
输出：3
解释：
- "a" 是 "abc" 的子字符串。
- "abc" 是 "abc" 的子字符串。
- "bc" 是 "abc" 的子字符串。
- "d" 不是 "abc" 的子字符串。
patterns 中有 3 个字符串作为子字符串出现在 word 中。

```
 **示例 2：** 

```

输入：patterns = ["a","b","c"], word = "aaaaabbbbb"
输出：2
解释：
- "a" 是 "aaaaabbbbb" 的子字符串。
- "b" 是 "aaaaabbbbb" 的子字符串。
- "c" 不是 "aaaaabbbbb" 的字符串。
patterns 中有 2 个字符串作为子字符串出现在 word 中。

```
 **示例 3：** 

```

输入：patterns = ["a","a","a"], word = "ab"
输出：3
解释：patterns 中的每个字符串都作为子字符串出现在 word "ab" 中。

```
 

 **提示：** 
-  `1 <= patterns.length <= 100` 
-  `1 <= patterns[i].length <= 100` 
-  `1 <= word.length <= 100` 
-  `patterns[i]` 和 `word` 由小写英文字母组成
 
**标签**
`字符串` 


## 
```python

```
>
# 1968.构造元素不等于两相邻元素平均值的数组
[https://leetcode-cn.com/problems/array-with-elements-not-equal-to-average-of-neighbors](https://leetcode-cn.com/problems/array-with-elements-not-equal-to-average-of-neighbors) 
## 原题
给你一个 **下标从 0 开始** 的数组 `nums` ，数组由若干 **互不相同的** 整数组成。你打算重新排列数组中的元素以满足：重排后，数组中的每个元素都 **不等于** 其两侧相邻元素的 **平均值** 。

更公式化的说法是，重新排列的数组应当满足这一属性：对于范围 `1 <= i < nums.length - 1` 中的每个 `i` ， `(nums[i-1] + nums[i+1]) / 2` **不等于** `nums[i]` 均成立 。

返回满足题意的任一重排结果。

 

 **示例 1：** 

```
输入：nums = [1,2,3,4,5]
输出：[1,2,4,5,3]
解释：
i=1, nums[i] = 2, 两相邻元素平均值为 (1+4) / 2 = 2.5
i=2, nums[i] = 4, 两相邻元素平均值为 (2+5) / 2 = 3.5
i=3, nums[i] = 5, 两相邻元素平均值为 (4+3) / 2 = 3.5

```
 **示例 2：** 

```
输入：nums = [6,2,0,9,7]
输出：[9,7,6,2,0]
解释：
i=1, nums[i] = 7, 两相邻元素平均值为 (9+6) / 2 = 7.5
i=2, nums[i] = 6, 两相邻元素平均值为 (7+2) / 2 = 4.5
i=3, nums[i] = 2, 两相邻元素平均值为 (6+0) / 2 = 3

```
 

 **提示：** 
-  `3 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^5` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1969.数组元素的最小非零乘积
[https://leetcode-cn.com/problems/minimum-non-zero-product-of-the-array-elements](https://leetcode-cn.com/problems/minimum-non-zero-product-of-the-array-elements) 
## 原题
给你一个正整数 `p` 。你有一个下标从 **1** 开始的数组 `nums` ，这个数组包含范围 `[1, 2^p - 1]` 内所有整数的二进制形式（两端都 **包含** ）。你可以进行以下操作 **任意** 次：
- 从 `nums` 中选择两个元素 `x` 和 `y` 。
- 选择 `x` 中的一位与 `y` 对应位置的位交换。对应位置指的是两个整数 **相同位置** 的二进制位。
比方说，如果 `x = 11 ***0*** 1` 且 `y = 00 ***1*** 1` ，交换右边数起第 `2` 位后，我们得到 `x = 11 ***1*** 1` 和 `y = 00 ***0*** 1` 。

请你算出进行以上操作 **任意次** 以后， `nums` 能得到的 **最小非零** 乘积。将乘积对 `10^9 + 7` **取余** 后返回。

 **注意：** 答案应为取余 **之前** 的最小值。

 

 **示例 1：** 

```

输入：p = 1
输出：1
解释：nums = [1] 。
只有一个元素，所以乘积为该元素。

```
 **示例 2：** 

```

输入：p = 2
输出：6
解释：nums = [01, 10, 11] 。
所有交换要么使乘积变为 0 ，要么乘积与初始乘积相同。
所以，数组乘积 1 * 2 * 3 = 6 已经是最小值。

```
 **示例 3：** 

```

输入：p = 3
输出：1512
解释：nums = [001, 010, 011, 100, 101, 110, 111]
- 第一次操作中，我们交换第二个和第五个元素最左边的数位。
    - 结果数组为 [001, 110, 011, 100, 001, 110, 111] 。
- 第二次操作中，我们交换第三个和第四个元素中间的数位。
    - 结果数组为 [001, 110, 001, 110, 001, 110, 111] 。
数组乘积 1 * 6 * 1 * 6 * 1 * 6 * 7 = 1512 是最小乘积。

```
 

 **提示：** 
-  `1 <= p <= 60` 
 
**标签**
`贪心` `递归` `数学` 


## 
```python

```
>
# 1970.你能穿过矩阵的最后一天
[https://leetcode-cn.com/problems/last-day-where-you-can-still-cross](https://leetcode-cn.com/problems/last-day-where-you-can-still-cross) 
## 原题
给你一个下标从 **1** 开始的二进制矩阵，其中 `0` 表示陆地， `1` 表示水域。同时给你 `row` 和 `col` 分别表示矩阵中行和列的数目。

一开始在第 `0` 天， **整个** 矩阵都是 **陆地** 。但每一天都会有一块新陆地被 **水** 淹没变成水域。给你一个下标从 **1** 开始的二维数组 `cells` ，其中 `cells[i] = [r<sub>i</sub>, c<sub>i</sub>]` 表示在第 `i` 天，第 `r<sub>i</sub>` 行 `c<sub>i</sub>` 列（下标都是从 **1** 开始）的陆地会变成 **水域** （也就是 `0` 变成 `1` ）。

你想知道从矩阵最 **上面** 一行走到最 **下面** 一行，且只经过陆地格子的 **最后一天** 是哪一天。你可以从最上面一行的 **任意** 格子出发，到达最下面一行的 **任意** 格子。你只能沿着 **四个** 基本方向移动（也就是上下左右）。

请返回只经过陆地格子能从最 **上面** 一行走到最 **下面** 一行的 **最后一天** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/1.png" style="width: 624px; height: 162px;">
```
输入：row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
输出：2
解释：上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 2 天。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/2.png" style="width: 504px; height: 178px;">
```
输入：row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
输出：1
解释：上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 1 天。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/3.png" style="width: 666px; height: 167px;">
```
输入：row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
输出：3
解释：上图描述了矩阵从第 0 天开始是如何变化的。
可以从最上面一行到最下面一行的最后一天是第 3 天。

```
 

 **提示：** 
-  `2 <= row, col <= 2 * 10^4` 
-  `4 <= row * col <= 2 * 10^4` 
-  `cells.length == row * col` 
-  `1 <= r<sub>i</sub> <= row` 
-  `1 <= c<sub>i</sub> <= col` 
-  `cells` 中的所有格子坐标都是 **唯一** 的。
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `二分查找` `矩阵` 


## 
```python

```
>
# 1971.寻找图中是否存在路径
[https://leetcode-cn.com/problems/find-if-path-exists-in-graph](https://leetcode-cn.com/problems/find-if-path-exists-in-graph) 
## 原题
有一个具有 `n` 个顶点的 **双向** 图，其中每个顶点标记从 `0` 到 `n - 1` （包含 `0` 和 `n - 1` ）。图中的边用一个二维整数数组 `edges` 表示，其中 `edges[i] = [u<sub>i</sub>, v<sub>i</sub>]` 表示顶点 `ui` 和顶点 `vi` 之间的双向边。 每个顶点对由 **最多一条** 边连接，并且没有顶点存在与自身相连的边。

请你确定是否存在从顶点 `start` 开始，到顶点 `end` 结束的 **有效路径** 。

给你数组 `edges` 和整数 `n` 、 `start` 和 `end` ，如果从 `start` 到 `end` 存在 **有效路径** ，则返回 `true` ，否则返回 `false` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/14/validpath-ex1.png" style="width: 141px; height: 121px;" />
```

输入：n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
输出：true
解释：存在由顶点 0 到顶点 2 的路径:
- 0 → 1 → 2 
- 0 → 2

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/08/14/validpath-ex2.png" style="width: 281px; height: 141px;" />
```

输入：n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
输出：false
解释：不存在由顶点 0 到顶点 5 的路径.

```
 

 **提示:** 
-  `1 <= n <= 2 * 10^5` 
-  `0 <= edges.length <= 2 * 10^5` 
-  `edges[i].length == 2` 
-  `0 <= u<sub>i</sub>, v<sub>i</sub> <= n - 1` 
-  `u<sub>i</sub> != v<sub>i</sub>` 
-  `0 <= start, end <= n - 1` 
- 不存在双向边
- 不存在指向顶点自身的边
 
**标签**
`深度优先搜索` `广度优先搜索` `图` 


## 
```python

```
>
# 1972.同一天的第一个电话和最后一个电话
[https://leetcode-cn.com/problems/first-and-last-call-on-the-same-day](https://leetcode-cn.com/problems/first-and-last-call-on-the-same-day) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1973.值等于子节点值之和的节点数量
[https://leetcode-cn.com/problems/count-nodes-equal-to-sum-of-descendants](https://leetcode-cn.com/problems/count-nodes-equal-to-sum-of-descendants) 
## 原题

 
**标签**



## 
```python

```
>
# 1974.使用特殊打字机键入单词的最少时间
[https://leetcode-cn.com/problems/minimum-time-to-type-word-using-special-typewriter](https://leetcode-cn.com/problems/minimum-time-to-type-word-using-special-typewriter) 
## 原题
有一个特殊打字机，它由一个 **圆盘** 和一个 **指针** 组成， 圆盘上标有小写英文字母 `'a'` 到 `'z'` 。 **只有** 当指针指向某个字母时，它才能被键入。指针 **初始时** 指向字符 `'a'` 。
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/31/chart.jpg" style="width: 530px; height: 410px;" />
每一秒钟，你可以执行以下操作之一：
- 将指针 **顺时针** 或者 <b>逆时针</b> 移动一个字符。
- 键入指针 **当前** 指向的字符。
给你一个字符串 `word` ，请你返回键入 `word` 所表示单词的 <b>最少</b> 秒数 。

 

 **示例 1：** 

```

输入：word = "abc"
输出：5
解释：
单词按如下操作键入：
- 花 1 秒键入字符 'a' in 1 ，因为指针初始指向 'a' ，故不需移动指针。
- 花 1 秒将指针顺时针移到 'b' 。
- 花 1 秒键入字符 'b' 。
- 花 1 秒将指针顺时针移到 'c' 。
- 花 1 秒键入字符 'c' 。

```
 **示例 2：** 

```

输入：word = "bza"
输出：7
解释：
单词按如下操作键入：
- 花 1 秒将指针顺时针移到 'b' 。
- 花 1 秒键入字符 'b' 。
- 花 2 秒将指针逆时针移到 'z' 。
- 花 1 秒键入字符 'z' 。
- 花 1 秒将指针顺时针移到 'a' 。
- 花 1 秒键入字符 'a' 。

```
 **示例 3：** 

```

输入：word = "zjpc"
输出：34
解释：
单词按如下操作键入：
- 花 1 秒将指针逆时针移到 'z' 。
- 花 1 秒键入字符 'z' 。
- 花 10 秒将指针顺时针移到 'j' 。
- 花 1 秒键入字符 'j' 。
- 花 6 秒将指针顺时针移到 'p' 。
- 花 1 秒键入字符 'p' 。
- 花 13 秒将指针逆时针移到 'c' 。
- 花 1 秒键入字符 'c' 。

```
 

 **提示：** 
-  `1 <= word.length <= 100` 
-  `word` 只包含小写英文字母。
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 1975.最大方阵和
[https://leetcode-cn.com/problems/maximum-matrix-sum](https://leetcode-cn.com/problems/maximum-matrix-sum) 
## 原题
给你一个 `n x n` 的整数方阵 `matrix` 。你可以执行以下操作 **任意次** ：
- 选择 `matrix` 中 **相邻** 两个元素，并将它们都 **乘以** `-1` 。
如果两个元素有 **公共边** ，那么它们就是 **相邻** 的。

你的目的是 **最大化** 方阵元素的和。请你在执行以上操作之后，返回方阵的 **最大** 和。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex1.png" style="width: 401px; height: 81px;">
```
输入：matrix = [[1,-1],[-1,1]]
输出：4
解释：我们可以执行以下操作使和等于 4 ：
- 将第一行的 2 个元素乘以 -1 。
- 将第一列的 2 个元素乘以 -1 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/16/pc79-q2ex2.png" style="width: 321px; height: 121px;">
```
输入：matrix = [[1,2,3],[-1,-2,-3],[1,2,3]]
输出：16
解释：我们可以执行以下操作使和等于 16 ：
- 将第二行的最后 2 个元素乘以 -1 。

```
 

 **提示：** 
-  `n == matrix.length == matrix[i].length` 
-  `2 <= n <= 250` 
-  `-10^5 <= matrix[i][j] <= 10^5` 
 
**标签**
`贪心` `数组` `矩阵` 


## 
```python

```
>
# 1976.到达目的地的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-arrive-at-destination](https://leetcode-cn.com/problems/number-of-ways-to-arrive-at-destination) 
## 原题
你在一个城市里，城市由 `n` 个路口组成，路口编号为 `0` 到 `n - 1` ，某些路口之间有 **双向** 道路。输入保证你可以从任意路口出发到达其他任意路口，且任意两个路口之间最多有一条路。

给你一个整数 `n` 和二维整数数组 `roads` ，其中 `roads[i] = [u<sub>i</sub>, v<sub>i</sub>, time<sub>i</sub>]` 表示在路口 `u<sub>i</sub>` 和 `v<sub>i</sub>` 之间有一条需要花费 `time<sub>i</sub>` 时间才能通过的道路。你想知道花费 **最少时间** 从路口 `0` 出发到达路口 `n - 1` 的方案数。

请返回花费 **最少时间** 到达目的地的 **路径数目** 。由于答案可能很大，将结果对 `10^9 + 7` **取余** 后返回。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/07/17/graph2.png" style="width: 235px; height: 381px;">
```
输入：n = 7, roads = [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]
输出：4
解释：从路口 0 出发到路口 6 花费的最少时间是 7 分钟。
四条花费 7 分钟的路径分别为：
- 0 ➝ 6
- 0 ➝ 4 ➝ 6
- 0 ➝ 1 ➝ 2 ➝ 5 ➝ 6
- 0 ➝ 1 ➝ 3 ➝ 5 ➝ 6

```
 **示例 2：** 

```
输入：n = 2, roads = [[1,0,10]]
输出：1
解释：只有一条从路口 0 到路口 1 的路，花费 10 分钟。

```
 

 **提示：** 
-  `1 <= n <= 200` 
-  `n - 1 <= roads.length <= n * (n - 1) / 2` 
-  `roads[i].length == 3` 
-  `0 <= u<sub>i</sub>, v<sub>i</sub> <= n - 1` 
-  `1 <= time<sub>i</sub> <= 10^9` 
-  `u<sub>i </sub>!= v<sub>i</sub>` 
- 任意两个路口之间至多有一条路。
- 从任意路口出发，你能够到达其他任意路口。
 
**标签**
`图` `拓扑排序` `动态规划` `最短路` 


## 
```python

```
>
# 1977.划分数字的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-separate-numbers](https://leetcode-cn.com/problems/number-of-ways-to-separate-numbers) 
## 原题
你写下了若干 **正整数** ，并将它们连接成了一个字符串 `num` 。但是你忘记给这些数字之间加逗号了。你只记得这一列数字是 **非递减** 的且 **没有** 任何数字有前导 0 。

请你返回有多少种可能的 **正整数数组** 可以得到字符串 `num` 。由于答案可能很大，将结果对 `10^9 + 7` <b>取余</b> 后返回。

 

 **示例 1：** 

```
输入：num = "327"
输出：2
解释：以下为可能的方案：
3, 27
327

```
 **示例 2：** 

```
输入：num = "094"
输出：0
解释：不能有数字有前导 0 ，且所有数字均为正数。

```
 **示例 3：** 

```
输入：num = "0"
输出：0
解释：不能有数字有前导 0 ，且所有数字均为正数。

```
 **示例 4：** 

```
输入：num = "9999999999999"
输出：101

```
 

 **提示：** 
-  `1 <= num.length <= 3500` 
-  `num` 只含有数字 `'0'` 到 `'9'` 。
 
**标签**
`字符串` `动态规划` `后缀数组` 


## 
```python

```
>
# 1978.上级经理已离职的公司员工
[https://leetcode-cn.com/problems/employees-whose-manager-left-the-company](https://leetcode-cn.com/problems/employees-whose-manager-left-the-company) 
## 原题

 
**标签**



## 
```python

```
>
# 1979.找出数组的最大公约数
[https://leetcode-cn.com/problems/find-greatest-common-divisor-of-array](https://leetcode-cn.com/problems/find-greatest-common-divisor-of-array) 
## 原题
给你一个整数数组 `nums` ，返回数组中最大数和最小数的 **最大公约数** 。

两个数的 **最大公约数** 是能够被两个数整除的最大正整数。

 

 **示例 1：** 

```
输入：nums = [2,5,6,9,10]
输出：2
解释：
nums 中最小的数是 2
nums 中最大的数是 10
2 和 10 的最大公约数是 2

```
 **示例 2：** 

```
输入：nums = [7,5,6,8,3]
输出：1
解释：
nums 中最小的数是 3
nums 中最大的数是 8
3 和 8 的最大公约数是 1

```
 **示例 3：** 

```
输入：nums = [3,3]
输出：3
解释：
nums 中最小的数是 3
nums 中最大的数是 3
3 和 3 的最大公约数是 3

```
 

 **提示：** 
-  `2 <= nums.length <= 1000` 
-  `1 <= nums[i] <= 1000` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 1980.找出不同的二进制字符串
[https://leetcode-cn.com/problems/find-unique-binary-string](https://leetcode-cn.com/problems/find-unique-binary-string) 
## 原题
给你一个字符串数组 `nums` ，该数组由 `n` 个 **互不相同** 的二进制字符串组成，且每个字符串长度都是 `n` 。请你找出并返回一个长度为 `n` 且 **没有出现** 在 `nums` 中的二进制字符串 *。* 如果存在多种答案，只需返回 **任意一个** 即可。

 

 **示例 1：** 

```

输入：nums = ["01","10"]
输出："11"
解释："11" 没有出现在 nums 中。"00" 也是正确答案。

```
 **示例 2：** 

```

输入：nums = ["00","01"]
输出："11"
解释："11" 没有出现在 nums 中。"10" 也是正确答案。

```
 **示例 3：** 

```

输入：nums = ["111","011","001"]
输出："101"
解释："101" 没有出现在 nums 中。"000"、"010"、"100"、"110" 也是正确答案。
```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 16` 
-  `nums[i].length == n` 
-  `nums[i]` 为 `'0'` 或 `'1'` 
-  `nums` 中的所有字符串 **互不相同** 
 
**标签**
`数组` `字符串` `回溯` 


## 
```python

```
>
# 1981.最小化目标值与所选元素的差
[https://leetcode-cn.com/problems/minimize-the-difference-between-target-and-chosen-elements](https://leetcode-cn.com/problems/minimize-the-difference-between-target-and-chosen-elements) 
## 原题
给你一个大小为 `m x n` 的整数矩阵 `mat` 和一个整数 `target` 。

从矩阵的 **每一行** 中选择一个整数，你的目标是 **最小化** 所有选中元素之 **和** 与目标值 `target` 的 **绝对差** 。

返回 **最小的绝对差** 。

 `a` 和 `b` 两数字的 **绝对差** 是 `a - b` 的绝对值。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/08/03/matrix1.png" style="width: 181px; height: 181px;" />

```

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], target = 13
输出：0
解释：一种可能的最优选择方案是：
- 第一行选出 1
- 第二行选出 5
- 第三行选出 7
所选元素的和是 13 ，等于目标值，所以绝对差是 0 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/08/03/matrix1-1.png" style="width: 61px; height: 181px;" />

```

输入：mat = [[1],[2],[3]], target = 100
输出：94
解释：唯一一种选择方案是：
- 第一行选出 1
- 第二行选出 2
- 第三行选出 3
所选元素的和是 6 ，绝对差是 94 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/08/03/matrix1-3.png" style="width: 301px; height: 61px;" />

```

输入：mat = [[1,2,9,8,7]], target = 6
输出：1
解释：最优的选择方案是选出第一行的 7 。
绝对差是 1 。

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat[i].length` 
-  `1 <= m, n <= 70` 
-  `1 <= mat[i][j] <= 70` 
-  `1 <= target <= 800` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 1982.从子集的和还原数组
[https://leetcode-cn.com/problems/find-array-given-subset-sums](https://leetcode-cn.com/problems/find-array-given-subset-sums) 
## 原题
存在一个未知数组需要你进行还原，给你一个整数 `n` 表示该数组的长度。另给你一个数组 `sums` ，由未知数组中全部 `2^n` 个 **子集的和** 组成（子集中的元素没有特定的顺序）。

返回一个长度为 `n` 的数组 `ans` 表示还原得到的未知数组。如果存在 **多种** 答案，只需返回其中 **任意一个** 。

如果可以由数组 `arr` 删除部分元素（也可能不删除或全删除）得到数组 `sub` ，那么数组 `sub` 就是数组 `arr` 的一个 **子集** 。 `sub` 的元素之和就是 `arr` 的一个 **子集的和** 。一个空数组的元素之和为 `0` 。

 **注意：** 生成的测试用例将保证至少存在一个正确答案。

 

 **示例 1：** 

```

输入：n = 3, sums = [-3,-2,-1,0,0,1,2,3]
输出：[1,2,-3]
解释：[1,2,-3] 能够满足给出的子集的和：
- []：和是 0
- [1]：和是 1
- [2]：和是 2
- [1,2]：和是 3
- [-3]：和是 -3
- [1,-3]：和是 -2
- [2,-3]：和是 -1
- [1,2,-3]：和是 0
注意，[1,2,-3] 的任何排列和 [-1,-2,3] 的任何排列都会被视作正确答案。

```
 **示例 2：** 

```

输入：n = 2, sums = [0,0,0,0]
输出：[0,0]
解释：唯一的正确答案是 [0,0] 。

```
 **示例 3：** 

```

输入：n = 4, sums = [0,0,5,5,4,-1,4,9,9,-1,4,3,4,8,3,8]
输出：[0,-1,4,5]
解释：[0,-1,4,5] 能够满足给出的子集的和。

```
 

 **提示：** 
-  `1 <= n <= 15` 
-  `sums.length == 2^n` 
-  `-10^4 <= sums[i] <= 10^4` 
 
**标签**
`数组` `分治` 


## 
```python

```
>
# 1984.学生分数的最小差值
[https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores](https://leetcode-cn.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores) 
## 原题
给你一个 **下标从 0 开始** 的整数数组 `nums` ，其中 `nums[i]` 表示第 `i` 名学生的分数。另给你一个整数 `k` 。

从数组中选出任意 `k` 名学生的分数，使这 `k` 个分数间 **最高分** 和 **最低分** 的 **差值** 达到 **最小化** 。

返回可能的 **最小差值** 。

 

 **示例 1：** 

```
输入：nums = [90], k = 1
输出：0
解释：选出 1 名学生的分数，仅有 1 种方法：
- [90] 最高分和最低分之间的差值是 90 - 90 = 0
可能的最小差值是 0

```
 **示例 2：** 

```
输入：nums = [9,4,1,7], k = 2
输出：2
解释：选出 2 名学生的分数，有 6 种方法：
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 4 = 5
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 1 = 8
- [9,4,1,7] 最高分和最低分之间的差值是 9 - 7 = 2
- [9,4,1,7] 最高分和最低分之间的差值是 4 - 1 = 3
- [9,4,1,7] 最高分和最低分之间的差值是 7 - 4 = 3
- [9,4,1,7] 最高分和最低分之间的差值是 7 - 1 = 6
可能的最小差值是 2
```
 

 **提示：** 
-  `1 <= k <= nums.length <= 1000` 
-  `0 <= nums[i] <= 10^5` 
 
**标签**
`数组` `排序` `滑动窗口` 


## 
```python

```
>
# 1985.找出数组中的第 K 大整数
[https://leetcode-cn.com/problems/find-the-kth-largest-integer-in-the-array](https://leetcode-cn.com/problems/find-the-kth-largest-integer-in-the-array) 
## 原题
给你一个字符串数组 `nums` 和一个整数 `k` 。 `nums` 中的每个字符串都表示一个不含前导零的整数。

返回 `nums` 中表示第 `k` 大整数的字符串。

 **注意：** 重复的数字在统计时会视为不同元素考虑。例如，如果 `nums` 是 `["1","2","2"]` ，那么 `"2"` 是最大的整数， `"2"` 是第二大的整数， `"1"` 是第三大的整数。

 

 **示例 1：** 

```

输入：nums = ["3","6","7","10"], k = 4
输出："3"
解释：
nums 中的数字按非递减顺序排列为 ["3","6","7","10"]
其中第 4 大整数是 "3"

```
 **示例 2：** 

```

输入：nums = ["2","21","12","1"], k = 3
输出："2"
解释：
nums 中的数字按非递减顺序排列为 ["1","2","12","21"]
其中第 3 大整数是 "2"

```
 **示例 3：** 

```

输入：nums = ["0","0"], k = 2
输出："0"
解释：
nums 中的数字按非递减顺序排列为 ["0","0"]
其中第 2 大整数是 "0"

```
 

 **提示：** 
-  `1 <= k <= nums.length <= 10^4` 
-  `1 <= nums[i].length <= 100` 
-  `nums[i]` 仅由数字组成
-  `nums[i]` 不含任何前导零
 
**标签**
`数组` `字符串` `分治` `快速选择` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1986.完成任务的最少工作时间段
[https://leetcode-cn.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks](https://leetcode-cn.com/problems/minimum-number-of-work-sessions-to-finish-the-tasks) 
## 原题
你被安排了 `n` 个任务。任务需要花费的时间用长度为 `n` 的整数数组 `tasks` 表示，第 `i` 个任务需要花费 `tasks[i]` 小时完成。一个 **工作时间段** 中，你可以 **至多** 连续工作 `sessionTime` 个小时，然后休息一会儿。

你需要按照如下条件完成给定任务：
- 如果你在某一个时间段开始一个任务，你需要在 **同一个** 时间段完成它。
- 完成一个任务后，你可以 **立马** 开始一个新的任务。
- 你可以按 **任意顺序** 完成任务。
给你 `tasks` 和 `sessionTime` ，请你按照上述要求，返回完成所有任务所需要的 **最少** 数目的 **工作时间段** 。

测试数据保证 `sessionTime` **大于等于** `tasks[i]` 中的 **最大值** 。

 

 **示例 1：** 

```
输入：tasks = [1,2,3], sessionTime = 3
输出：2
解释：你可以在两个工作时间段内完成所有任务。
- 第一个工作时间段：完成第一和第二个任务，花费 1 + 2 = 3 小时。
- 第二个工作时间段：完成第三个任务，花费 3 小时。

```
 **示例 2：** 

```
输入：tasks = [3,1,3,1,1], sessionTime = 8
输出：2
解释：你可以在两个工作时间段内完成所有任务。
- 第一个工作时间段：完成除了最后一个任务以外的所有任务，花费 3 + 1 + 3 + 1 = 8 小时。
- 第二个工作时间段，完成最后一个任务，花费 1 小时。

```
 **示例 3：** 

```
输入：tasks = [1,2,3,4,5], sessionTime = 15
输出：1
解释：你可以在一个工作时间段以内完成所有任务。

```
 

 **提示：** 
-  `n == tasks.length` 
-  `1 <= n <= 14` 
-  `1 <= tasks[i] <= 10` 
-  `max(tasks[i]) <= sessionTime <= 15` 
 
**标签**
`位运算` `数组` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 1987.不同的好子序列数目
[https://leetcode-cn.com/problems/number-of-unique-good-subsequences](https://leetcode-cn.com/problems/number-of-unique-good-subsequences) 
## 原题
给你一个二进制字符串 `binary` 。 `binary` 的一个 **子序列** 如果是 **非空** 的且没有 <b>前导</b> **0** （除非数字是 `"0"` 本身），那么它就是一个 **好** 的子序列。

请你找到 `binary` **不同好子序列** 的数目。
- 比方说，如果 `binary = "001"` ，那么所有 **好** 子序列为 `["0", "0", "1"]` ，所以 <b>不同</b> 的好子序列为 `"0"` 和 `"1"` 。 注意，子序列 `"00"` ， `"01"` 和 `"001"` 不是好的，因为它们有前导 0 。
请你返回 `binary` 中 **不同好子序列** 的数目。由于答案可能很大，请将它对 `10^9 + 7` **取余** 后返回。

一个 **子序列** 指的是从原数组中删除若干个（可以一个也不删除）元素后，不改变剩余元素顺序得到的序列。

 

 **示例 1：** 

```
输入：binary = "001"
输出：2
解释：好的二进制子序列为 ["0", "0", "1"] 。
不同的好子序列为 "0" 和 "1" 。

```
 **示例 2：** 

```
输入：binary = "11"
输出：2
解释：好的二进制子序列为 ["1", "1", "11"] 。
不同的好子序列为 "1" 和 "11" 。
```
 **示例 3：** 

```
输入：binary = "101"
输出：5
解释：好的二进制子序列为 ["1", "0", "1", "10", "11", "101"] 。
不同的好子序列为 "0" ，"1" ，"10" ，"11" 和 "101" 。

```
 

 **提示：** 
-  `1 <= binary.length <= 10^5` 
-  `binary` 只含有 `'0'` 和 `'1'` 。
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1988.找出每所学校的最低分数要求
[https://leetcode-cn.com/problems/find-cutoff-score-for-each-school](https://leetcode-cn.com/problems/find-cutoff-score-for-each-school) 
## 原题

 
**标签**



## 
```python

```
>
# 1990.统计实验的数量
[https://leetcode-cn.com/problems/count-the-number-of-experiments](https://leetcode-cn.com/problems/count-the-number-of-experiments) 
## 原题

 
**标签**



## 
```python

```
>
# 1991.找到数组的中间位置
[https://leetcode-cn.com/problems/find-the-middle-index-in-array](https://leetcode-cn.com/problems/find-the-middle-index-in-array) 
## 原题
给你一个下标从 **0** 开始的整数数组 `nums` ，请你找到 **最左边** 的中间位置 `middleIndex` （也就是所有可能中间位置下标最小的一个）。

中间位置 `middleIndex` 是满足 `nums[0] + nums[1] + ... + nums[middleIndex-1] == nums[middleIndex+1] + nums[middleIndex+2] + ... + nums[nums.length-1]` 的数组下标。

如果 `middleIndex == 0` ，左边部分的和定义为 `0` 。类似的，如果 `middleIndex == nums.length - 1` ，右边部分的和定义为 `0` 。

请你返回满足上述条件 **最左边** 的 `middleIndex` ，如果不存在这样的中间位置，请你返回 `-1` 。

 

 **示例 1：** 

```

输入：nums = [2,3,-1,8,4]
输出：3
解释：
下标 3 之前的数字和为：2 + 3 + -1 = 4
下标 3 之后的数字和为：4 = 4

```
 **示例 2：** 

```

输入：nums = [1,-1,4]
输出：2
解释：
下标 2 之前的数字和为：1 + -1 = 0
下标 2 之后的数字和为：0

```
 **示例 3：** 

```

输入：nums = [2,5]
输出：-1
解释：
不存在符合要求的 middleIndex 。

```
 **示例 4：** 

```

输入：nums = [1]
输出：0
解释：
下标 0 之前的数字和为：0
下标 0 之后的数字和为：0

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `-1000 <= nums[i] <= 1000` 
 

 **注意：** 本题与主站 724 题相同：<a href="https://leetcode-cn.com/problems/find-pivot-index/" target="_blank">https://leetcode-cn.com/problems/find-pivot-index/</a>

 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 1992.找到所有的农场组
[https://leetcode-cn.com/problems/find-all-groups-of-farmland](https://leetcode-cn.com/problems/find-all-groups-of-farmland) 
## 原题
给你一个下标从 **0** 开始，大小为 `m x n` 的二进制矩阵 `land` ，其中 `0` 表示一单位的森林土地， `1` 表示一单位的农场土地。

为了让农场保持有序，农场土地之间以矩形的 **农场组** 的形式存在。每一个农场组都 **仅** 包含农场土地。且题目保证不会有两个农场组相邻，也就是说一个农场组中的任何一块土地都 **不会** 与另一个农场组的任何一块土地在四个方向上相邻。

 `land` 可以用坐标系统表示，其中 `land` 左上角坐标为 `(0, 0)` ，右下角坐标为 `(m-1, n-1)` 。请你找到所有 <b>农场组</b> 最左上角和最右下角的坐标。一个左上角坐标为 `(r<sub>1</sub>, c<sub>1</sub>)` 且右下角坐标为 `(r<sub>2</sub>, c<sub>2</sub>)` 的 **农场组** 用长度为 4 的数组 `[r<sub>1</sub>, c<sub>1</sub>, r<sub>2</sub>, c<sub>2</sub>]` 表示。

请你返回一个二维数组，它包含若干个长度为 4 的子数组，每个子数组表示 `land` 中的一个 **农场组** 。如果没有任何农场组，请你返回一个空数组。可以以 **任意顺序** 返回所有农场组。

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-23-15-copy-of-diagram-drawio-diagrams-net.png" style="width: 300px; height: 300px;">

```
输入：land = [[1,0,0],[0,1,1],[0,1,1]]
输出：[[0,0,0,0],[1,1,2,2]]
解释：
第一个农场组的左上角为 land[0][0] ，右下角为 land[0][0] 。
第二个农场组的左上角为 land[1][1] ，右下角为 land[2][2] 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-30-26-copy-of-diagram-drawio-diagrams-net.png" style="width: 200px; height: 200px;">

```
输入：land = [[1,1],[1,1]]
输出：[[0,0,1,1]]
解释：
第一个农场组左上角为 land[0][0] ，右下角为 land[1][1] 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/07/27/screenshot-2021-07-27-at-12-32-24-copy-of-diagram-drawio-diagrams-net.png" style="width: 100px; height: 100px;">

```
输入：land = [[0]]
输出：[]
解释：
没有任何农场组。

```
 

 **提示：** 
-  `m == land.length` 
-  `n == land[i].length` 
-  `1 <= m, n <= 300` 
-  `land` 只包含 `0` 和 `1` 。
- 农场组都是 **矩形** 的形状。
 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 1993.树上的操作
[https://leetcode-cn.com/problems/operations-on-tree](https://leetcode-cn.com/problems/operations-on-tree) 
## 原题
给你一棵 `n` 个节点的树，编号从 `0` 到 `n - 1` ，以父节点数组 `parent` 的形式给出，其中 `parent[i]` 是第 `i` 个节点的父节点。树的根节点为 `0` 号节点，所以 `parent[0] = -1` ，因为它没有父节点。你想要设计一个数据结构实现树里面对节点的加锁，解锁和升级操作。

数据结构需要支持如下函数：
-  **Lock：** 指定用户给指定节点 **上锁** ，上锁后其他用户将无法给同一节点上锁。只有当节点处于未上锁的状态下，才能进行上锁操作。
-  **Unlock：** 指定用户给指定节点 **解锁** ，只有当指定节点当前正被指定用户锁住时，才能执行该解锁操作。
- <b>Upgrade：</b>指定用户给指定节点 **上锁** ，并且将该节点的所有子孙节点 **解锁** 。只有如下 3 个条件 **全部** 满足时才能执行升级操作：
	
- 指定节点当前状态为未上锁。
- 指定节点至少有一个上锁状态的子孙节点（可以是 **任意** 用户上锁的）。
- 指定节点没有任何上锁的祖先节点。
	
	
请你实现 `LockingTree` 类：
-  `LockingTree(int[] parent)` 用父节点数组初始化数据结构。
-  `lock(int num, int user)` 如果 id 为 `user` 的用户可以给节点 `num` 上锁，那么返回 `true` ，否则返回 `false` 。如果可以执行此操作，节点 `num` 会被 id 为 `user` 的用户 **上锁** 。
-  `unlock(int num, int user)` 如果 id 为 `user` 的用户可以给节点 `num` 解锁，那么返回 `true` ，否则返回 `false` 。如果可以执行此操作，节点 `num` 变为 **未上锁** 状态。
-  `upgrade(int num, int user)` 如果 id 为 `user` 的用户可以给节点 `num` 升级，那么返回 `true` ，否则返回 `false` 。如果可以执行此操作，节点 `num` 会被 **升级** 。
 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/07/29/untitled.png" style="width: 375px; height: 246px;">

```
输入：
["LockingTree", "lock", "unlock", "unlock", "lock", "upgrade", "lock"]
[[[-1, 0, 0, 1, 1, 2, 2]], [2, 2], [2, 3], [2, 2], [4, 5], [0, 1], [0, 1]]
输出：
[null, true, false, true, true, true, false]

解释：
LockingTree lockingTree = new LockingTree([-1, 0, 0, 1, 1, 2, 2]);
lockingTree.lock(2, 2);    // 返回 true ，因为节点 2 未上锁。
                           // 节点 2 被用户 2 上锁。
lockingTree.unlock(2, 3);  // 返回 false ，因为用户 3 无法解锁被用户 2 上锁的节点。
lockingTree.unlock(2, 2);  // 返回 true ，因为节点 2 之前被用户 2 上锁。
                           // 节点 2 现在变为未上锁状态。
lockingTree.lock(4, 5);    // 返回 true ，因为节点 4 未上锁。
                           // 节点 4 被用户 5 上锁。
lockingTree.upgrade(0, 1); // 返回 true ，因为节点 0 未上锁且至少有一个被上锁的子孙节点（节点 4）。
                           // 节点 0 被用户 1 上锁，节点 4 变为未上锁。
lockingTree.lock(0, 1);    // 返回 false ，因为节点 0 已经被上锁了。

```
 

 **提示：** 
-  `n == parent.length` 
-  `2 <= n <= 2000` 
- 对于 `i != 0` ，满足 `0 <= parent[i] <= n - 1` 
-  `parent[0] == -1` 
-  `0 <= num <= n - 1` 
-  `1 <= user <= 10^4` 
-  `parent` 表示一棵合法的树。
-  `lock` ， `unlock` 和 `upgrade` 的调用 **总共** 不超过 `2000` 次。
 
**标签**
`树` `广度优先搜索` `设计` `哈希表` 


## 
```python

```
>
# 1994.好子集的数目
[https://leetcode-cn.com/problems/the-number-of-good-subsets](https://leetcode-cn.com/problems/the-number-of-good-subsets) 
## 原题
给你一个整数数组 `nums` 。如果 `nums` 的一个子集中，所有元素的乘积可以用若干个 **互不相同的质数** 相乘得到，那么我们称它为 **好子集** 。
- 比方说，如果 `nums = [1, 2, 3, 4]` ：

	
-  `[2, 3]` ， `[1, 2, 3]` 和 `[1, 3]` 是 **好** 子集，乘积分别为 `6 = 2*3` ， `6 = 2*3` 和 `3 = 3` 。
-  `[1, 4]` 和 `[4]` 不是 **好** 子集，因为乘积分别为 `4 = 2*2` 和 `4 = 2*2` 。
	
	
请你返回 `nums` 中不同的 **好** 子集的数目对 `10^9 + 7` **取余** 的结果。

 `nums` 中的 **子集** 是通过删除 `nums` 中一些（可能一个都不删除，也可能全部都删除）元素后剩余元素组成的数组。如果两个子集删除的下标不同，那么它们被视为不同的子集。

 

 **示例 1：** 

```
输入：nums = [1,2,3,4]
输出：6
解释：好子集为：
- [1,2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [1,2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
- [1,3]：乘积为 3 ，可以表示为质数 3 的乘积。
- [2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [2,3]：乘积为 6 ，可以表示为互不相同的质数 2 和 3 的乘积。
- [3]：乘积为 3 ，可以表示为质数 3 的乘积。

```
 **示例 2：** 

```
输入：nums = [4,2,3,15]
输出：5
解释：好子集为：
- [2]：乘积为 2 ，可以表示为质数 2 的乘积。
- [2,3]：乘积为 6 ，可以表示为互不相同质数 2 和 3 的乘积。
- [2,15]：乘积为 30 ，可以表示为互不相同质数 2，3 和 5 的乘积。
- [3]：乘积为 3 ，可以表示为质数 3 的乘积。
- [15]：乘积为 15 ，可以表示为互不相同质数 3 和 5 的乘积。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 30` 
 
**标签**
`位运算` `数组` `数学` `动态规划` `状态压缩` 


## 
```python

```
>
# 1995.统计特殊四元组
[https://leetcode-cn.com/problems/count-special-quadruplets](https://leetcode-cn.com/problems/count-special-quadruplets) 
## 原题
给你一个 **下标从 0 开始** 的整数数组 `nums` ，返回满足下述条件的 **不同** 四元组 `(a, b, c, d)` 的 **数目** ：
-  `nums[a] + nums[b] + nums[c] == nums[d]` ，且
-  `a < b < c < d` 
 

 **示例 1：** 

```
输入：nums = [1,2,3,6]
输出：1
解释：满足要求的唯一一个四元组是 (0, 1, 2, 3) 因为 1 + 2 + 3 == 6 。

```
 **示例 2：** 

```
输入：nums = [3,3,6,4,5]
输出：0
解释：[3,3,6,4,5] 中不存在满足要求的四元组。

```
 **示例 3：** 

```
输入：nums = [1,1,1,3,5]
输出：4
解释：满足要求的 4 个四元组如下：
- (0, 1, 2, 3): 1 + 1 + 1 == 3
- (0, 1, 3, 4): 1 + 1 + 3 == 5
- (0, 2, 3, 4): 1 + 1 + 3 == 5
- (1, 2, 3, 4): 1 + 1 + 3 == 5

```
 

 **提示：** 
-  `4 <= nums.length <= 50` 
-  `1 <= nums[i] <= 100` 
 
**标签**
`数组` `枚举` 


## 
```python

```
>
# 1996.游戏中弱角色的数量
[https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game](https://leetcode-cn.com/problems/the-number-of-weak-characters-in-the-game) 
## 原题
你正在参加一个多角色游戏，每个角色都有两个主要属性： **攻击** 和 **防御** 。给你一个二维整数数组 `properties` ，其中 `properties[i] = [attack<sub>i</sub>, defense<sub>i</sub>]` 表示游戏中第 `i` 个角色的属性。

如果存在一个其他角色的攻击和防御等级 **都严格高于** 该角色的攻击和防御等级，则认为该角色为 **弱角色** 。更正式地，如果认为角色 `i` **弱于** 存在的另一个角色 `j` ，那么 `attack<sub>j</sub> > attack<sub>i</sub>` 且 `defense<sub>j</sub> > defense<sub>i</sub>` 。

返回 **弱角色** 的数量。

 

 **示例 1：** 

```

输入：properties = [[5,5],[6,3],[3,6]]
输出：0
解释：不存在攻击和防御都严格高于其他角色的角色。

```
 **示例 2：** 

```

输入：properties = [[2,2],[3,3]]
输出：1
解释：第一个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。

```
 **示例 3：** 

```

输入：properties = [[1,5],[10,4],[4,3]]
输出：1
解释：第三个角色是弱角色，因为第二个角色的攻击和防御严格大于该角色。

```
 

 **提示：** 
-  `2 <= properties.length <= 10^5` 
-  `properties[i].length == 2` 
-  `1 <= attack<sub>i</sub>, defense<sub>i</sub> <= 10^5` 
 
**标签**
`栈` `贪心` `数组` `排序` `单调栈` 


## 
```python

```
>
# 1997.访问完所有房间的第一天
[https://leetcode-cn.com/problems/first-day-where-you-have-been-in-all-the-rooms](https://leetcode-cn.com/problems/first-day-where-you-have-been-in-all-the-rooms) 
## 原题
你需要访问 `n` 个房间，房间从 `0` 到 `n - 1` 编号。同时，每一天都有一个日期编号，从 `0` 开始，依天数递增。你每天都会访问一个房间。

最开始的第 `0` 天，你访问 `0` 号房间。给你一个长度为 `n` 且 **下标从 0 开始** 的数组 `nextVisit` 。在接下来的几天中，你访问房间的 **次序** 将根据下面的 **规则** 决定：
- 假设某一天，你访问 `i` 号房间。
- 如果算上本次访问，访问 `i` 号房间的次数为 **奇数** ，那么 **第二天** 需要访问 `nextVisit[i]` 所指定的房间，其中 `0 <= nextVisit[i] <= i` 。
- 如果算上本次访问，访问 `i` 号房间的次数为 **偶数** ，那么 **第二天** 需要访问 `(i + 1) mod n` 号房间。
请返回你访问完所有房间的第一天的日期编号。题目数据保证总是存在这样的一天。由于答案可能很大，返回对 `10^9 + 7` 取余后的结果。

 

 **示例 1：** 

```

输入：nextVisit = [0,0]
输出：2
解释：
- 第 0 天，你访问房间 0 。访问 0 号房间的总次数为 1 ，次数为奇数。
  下一天你需要访问房间的编号是 nextVisit[0] = 0
- 第 1 天，你访问房间 0 。访问 0 号房间的总次数为 2 ，次数为偶数。
  下一天你需要访问房间的编号是 (0 + 1) mod 2 = 1
- 第 2 天，你访问房间 1 。这是你第一次完成访问所有房间的那天。

```
 **示例 2：** 

```

输入：nextVisit = [0,0,2]
输出：6
解释：
你每天访问房间的次序是 [0,0,1,0,0,1,2,...] 。
第 6 天是你访问完所有房间的第一天。

```
 **示例 3：** 

```

输入：nextVisit = [0,1,2,0]
输出：6
解释：
你每天访问房间的次序是 [0,0,1,1,2,2,3,...] 。
第 6 天是你访问完所有房间的第一天。

```
 

 **提示：** 
-  `n == nextVisit.length` 
-  `2 <= n <= 10^5` 
-  `0 <= nextVisit[i] <= i` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1998.数组的最大公因数排序
[https://leetcode-cn.com/problems/gcd-sort-of-an-array](https://leetcode-cn.com/problems/gcd-sort-of-an-array) 
## 原题
给你一个整数数组 `nums` ，你可以在 `nums` 上执行下述操作 **任意次** ：
- 如果 `gcd(nums[i], nums[j]) > 1` ，交换 `nums[i]` 和 `nums[j]` 的位置。其中 `gcd(nums[i], nums[j])` 是 `nums[i]` 和 `nums[j]` 的最大公因数。
如果能使用上述交换方式将 `nums` 按 **非递减顺序** 排列，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```
输入：nums = [7,21,3]
输出：true
解释：可以执行下述操作完成对 [7,21,3] 的排序：
- 交换 7 和 21 因为 gcd(7,21) = 7 。nums = [21,7,3]
- 交换 21 和 3 因为 gcd(21,3) = 3 。nums = [3,7,21]

```
 **示例 2：** 

```
输入：nums = [5,2,6,2]
输出：false
解释：无法完成排序，因为 5 不能与其他元素交换。

```
 **示例 3：** 

```
输入：nums = [10,5,9,3,15]
输出：true
解释：
可以执行下述操作完成对 [10,5,9,3,15] 的排序：
- 交换 10 和 15 因为 gcd(10,15) = 5 。nums = [15,5,9,3,10]
- 交换 15 和 3 因为 gcd(15,3) = 3 。nums = [3,5,9,15,10]
- 交换 10 和 15 因为 gcd(10,15) = 5 。nums = [3,5,9,10,15]

```
 

 **提示：** 
-  `1 <= nums.length <= 3 * 10^4` 
-  `2 <= nums[i] <= 10^5` 
 
**标签**
`并查集` `数组` `数学` `排序` 


## 
```python

```
>
# 1999.最小的仅由两个数组成的倍数
[https://leetcode-cn.com/problems/smallest-greater-multiple-made-of-two-digits](https://leetcode-cn.com/problems/smallest-greater-multiple-made-of-two-digits) 
## 原题

 
**标签**



## 
```python

```
>
# 2000.反转单词前缀
[https://leetcode-cn.com/problems/reverse-prefix-of-word](https://leetcode-cn.com/problems/reverse-prefix-of-word) 
## 原题
给你一个下标从 **0** 开始的字符串 `word` 和一个字符 `ch` 。找出 `ch` 第一次出现的下标 `i` ， **反转** `word` 中从下标 `0` 开始、直到下标 `i` 结束（含下标 `i` ）的那段字符。如果 `word` 中不存在字符 `ch` ，则无需进行任何操作。
- 例如，如果 `word = "abcdefd"` 且 `ch = "d"` ，那么你应该 **反转** 从下标 0 开始、直到下标 `3` 结束（含下标 `3` ）。结果字符串将会是 `" ***dcba*** efd"` 。
返回 **结果字符串** 。

 

 **示例 1：** 

```
输入：word = "abcdefd", ch = "d"
输出："dcbaefd"
解释："d" 第一次出现在下标 3 。 
反转从下标 0 到下标 3（含下标 3）的这段字符，结果字符串是 "dcbaefd" 。

```
 **示例 2：** 

```
输入：word = "xyxzxe", ch = "z"
输出："zxyxxe"
解释："z" 第一次也是唯一一次出现是在下标 3 。
反转从下标 0 到下标 3（含下标 3）的这段字符，结果字符串是 "zxyxxe" 。

```
 **示例 3：** 

```
输入：word = "abcd", ch = "z"
输出："abcd"
解释："z" 不存在于 word 中。
无需执行反转操作，结果字符串是 "abcd" 。

```
 

 **提示：** 
-  `1 <= word.length <= 250` 
-  `word` 由小写英文字母组成
-  `ch` 是一个小写英文字母
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
