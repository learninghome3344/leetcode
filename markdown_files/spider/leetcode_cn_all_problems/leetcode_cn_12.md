# 1201.丑数 III
[https://leetcode-cn.com/problems/ugly-number-iii](https://leetcode-cn.com/problems/ugly-number-iii) 
## 原题
给你四个整数： `n` 、 `a` 、 `b` 、 `c` ，请你设计一个算法来找出第  `n`  个丑数。

丑数是可以被  `a`   **或**   `b`   **或** `c`  整除的 **正整数** 。

 

 **示例 1：** 

```

输入：n = 3, a = 2, b = 3, c = 5
输出：4
解释：丑数序列为 2, 3, 4, 5, 6, 8, 9, 10... 其中第 3 个是 4。
```
 **示例 2：** 

```

输入：n = 4, a = 2, b = 3, c = 4
输出：6
解释：丑数序列为 2, 3, 4, 6, 8, 9, 10, 12... 其中第 4 个是 6。

```
 **示例 3：** 

```

输入：n = 5, a = 2, b = 11, c = 13
输出：10
解释：丑数序列为 2, 4, 6, 8, 10, 11, 12, 13... 其中第 5 个是 10。

```
 **示例 4：** 

```

输入：n = 1000000000, a = 2, b = 217983653, c = 336916467
输出：1999999984

```
 

 **提示：** 
-  `1 <= n, a, b, c <= 10^9` 
-  `1 <= a * b * c <= 10^18` 
- 本题结果在  `[1, 2 * 10^9]`  的范围内
 
**标签**
`数学` `二分查找` `数论` 


## 
```python

```
>
# 1202.交换字符串中的元素
[https://leetcode-cn.com/problems/smallest-string-with-swaps](https://leetcode-cn.com/problems/smallest-string-with-swaps) 
## 原题
给你一个字符串 `s` ，以及该字符串中的一些「索引对」数组 `pairs` ，其中 `pairs[i] = [a, b]` 表示字符串中的两个索引（编号从 0 开始）。

你可以 **任意多次交换** 在 `pairs` 中任意一对索引处的字符。

返回在经过若干次交换后， `s` 可以变成的按字典序最小的字符串。

 

 **示例 1:** 

```
输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释： 
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"

```
 **示例 2：** 

```
输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"
```
 **示例 3：** 

```
输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `0 <= pairs.length <= 10^5` 
-  `0 <= pairs[i][0], pairs[i][1] < s.length` 
-  `s` 中只含有小写英文字母
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `哈希表` `字符串` 


## 
```python

```
>
# 1203.项目管理
[https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies](https://leetcode-cn.com/problems/sort-items-by-groups-respecting-dependencies) 
## 原题
有 `n` 个项目，每个项目或者不属于任何小组，或者属于 `m` 个小组之一。 `group[i]` 表示第 `i` 个项目所属的小组，如果第 `i` 个项目不属于任何小组，则 `group[i]` 等于 `-1` 。项目和小组都是从零开始编号的。可能存在小组不负责任何项目，即没有任何项目属于这个小组。

请你帮忙按要求安排这些项目的进度，并返回排序后的项目列表：
- 同一小组的项目，排序后在列表中彼此相邻。
- 项目之间存在一定的依赖关系，我们用一个列表 `beforeItems`  来表示，其中  `beforeItems[i]`  表示在进行第  `i`  个项目前（位于第 `i`  个项目左侧）应该完成的所有项目。
如果存在多个解决方案，只需要返回其中任意一个即可。如果没有合适的解决方案，就请返回一个 **空列表** 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/22/1359_ex1.png" style="height: 181px; width: 191px;" />** 

```

输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
输出：[6,3,4,1,5,2,0,7]

```
 **示例 2：** 

```

输入：n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3],[],[4],[]]
输出：[]
解释：与示例 1 大致相同，但是在排序后的列表中，4 必须放在 6 的前面。

```
 

 **提示：** 
-  `1 <= m <= n <= 3 * 10^4` 
-  `group.length == beforeItems.length == n` 
-  `-1 <= group[i] <= m - 1` 
-  `0 <= beforeItems[i].length <= n - 1` 
-  `0 <= beforeItems[i][j] <= n - 1` 
-  `i != beforeItems[i][j]` 
-  `beforeItems[i]` 不含重复元素
 
**标签**
`深度优先搜索` `广度优先搜索` `图` `拓扑排序` 


## 
```python

```
>
# 1204.最后一个能进入电梯的人
[https://leetcode-cn.com/problems/last-person-to-fit-in-the-bus](https://leetcode-cn.com/problems/last-person-to-fit-in-the-bus) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1205.每月交易II
[https://leetcode-cn.com/problems/monthly-transactions-ii](https://leetcode-cn.com/problems/monthly-transactions-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1206.设计跳表
[https://leetcode-cn.com/problems/design-skiplist](https://leetcode-cn.com/problems/design-skiplist) 
## 原题
不使用任何库函数，设计一个 **跳表** 。

 **跳表** 是在 `O(log(n))` 时间内完成增加、删除、搜索操作的数据结构。跳表相比于树堆与红黑树，其功能与性能相当，并且跳表的代码长度相较下更短，其设计思想与链表相似。

例如，一个跳表包含 `[30, 40, 50, 60, 70, 90]` ，然后增加 `80` 、 `45` 到跳表中，以下图的方式操作：

<img alt="" src="https://assets.leetcode.com/uploads/2019/09/27/1506_skiplist.gif" /><br />
<small>Artyom Kalinin [CC BY-SA 3.0], via <a href="https://commons.wikimedia.org/wiki/File:Skip_list_add_element-en.gif" target="_blank" title="Artyom Kalinin [CC BY-SA 3.0 (https://creativecommons.org/licenses/by-sa/3.0)], via Wikimedia Commons">Wikimedia Commons</a></small>

跳表中有很多层，每一层是一个短的链表。在第一层的作用下，增加、删除和搜索操作的时间复杂度不超过 `O(n)` 。跳表的每一个操作的平均时间复杂度是 `O(log(n))` ，空间复杂度是 `O(n)` 。

了解更多 : <a href="https://en.wikipedia.org/wiki/Skip_list" target="_blank">https://en.wikipedia.org/wiki/Skip_list</a>

在本题中，你的设计应该要包含这些函数：
-  `bool search(int target)` : 返回target是否存在于跳表中。
-  `void add(int num)` : 插入一个元素到跳表。
-  `bool erase(int num)` : 在跳表中删除一个值，如果 `num` 不存在，直接返回false. 如果存在多个 `num` ，删除其中任意一个即可。
注意，跳表中可能存在多个相同的值，你的代码需要处理这种情况。

 

 **示例 1:** 

```

输入
["Skiplist", "add", "add", "add", "search", "add", "search", "erase", "erase", "search"]
[[], [1], [2], [3], [0], [4], [1], [0], [1], [1]]
输出
[null, null, null, null, false, null, true, false, true, false]

解释
Skiplist skiplist = new Skiplist();
skiplist.add(1);
skiplist.add(2);
skiplist.add(3);
skiplist.search(0);   // 返回 false
skiplist.add(4);
skiplist.search(1);   // 返回 true
skiplist.erase(0);    // 返回 false，0 不在跳表中
skiplist.erase(1);    // 返回 true
skiplist.search(1);   // 返回 false，1 已被擦除

```
 

 **提示:** 
-  `0 <= num, target <= 2 * 10^4` 
- 调用 `search` , `add` , `erase` 操作次数不大于 `5 * 10^4` 
 
**标签**
`设计` `链表` 


## 
```python

```
>
# 1207.独一无二的出现次数
[https://leetcode-cn.com/problems/unique-number-of-occurrences](https://leetcode-cn.com/problems/unique-number-of-occurrences) 
## 原题
给你一个整数数组 `arr` ，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 `true` ；否则返回 `false` 。

 

 **示例 1：** 

```
输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
```
 **示例 2：** 

```
输入：arr = [1,2]
输出：false

```
 **示例 3：** 

```
输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
输出：true

```
 

 **提示：** 
-  `1 <= arr.length <= 1000` 
-  `-1000 <= arr[i] <= 1000` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1208.尽可能使字符串相等
[https://leetcode-cn.com/problems/get-equal-substrings-within-budget](https://leetcode-cn.com/problems/get-equal-substrings-within-budget) 
## 原题
给你两个长度相同的字符串， `s` 和 `t` 。

将 `s`  中的第  `i`  个字符变到  `t`  中的第 `i` 个字符需要  `|s[i] - t[i]|`  的开销（开销可能为 0），也就是两个字符的 ASCII 码值的差的绝对值。

用于变更字符串的最大预算是  `maxCost` 。在转化字符串时，总开销应当小于等于该预算，这也意味着字符串的转化可能是不完全的。

如果你可以将 `s` 的子字符串转化为它在 `t` 中对应的子字符串，则返回可以转化的最大长度。

如果 `s` 中没有子字符串可以转化成 `t` 中对应的子字符串，则返回 `0` 。

 

 **示例 1：** 

```

输入：s = "abcd", t = "bcdf", maxCost = 3
输出：3
解释：s 中的 "abc" 可以变为 "bcd"。开销为 3，所以最大长度为 3。
```
 **示例 2：** 

```

输入：s = "abcd", t = "cdef", maxCost = 3
输出：1
解释：s 中的任一字符要想变成 t 中对应的字符，其开销都是 2。因此，最大长度为 1。

```
 **示例 3：** 

```

输入：s = "abcd", t = "acde", maxCost = 0
输出：1
解释：a -> a, cost = 0，字符串未发生变化，所以最大长度为 1。

```
 

 **提示：** 
-  `1 <= s.length, t.length <= 10^5` 
-  `0 <= maxCost <= 10^6` 
-  `s` 和  `t`  都只含小写英文字母。
 
**标签**
`字符串` `二分查找` `前缀和` `滑动窗口` 


## 
```python

```
>
# 1209.删除字符串中的所有相邻重复项 II
[https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string-ii) 
## 原题
给你一个字符串 `s` ，「 `k` 倍重复项删除操作」将会从 `s` 中选择 `k` 个相邻且相等的字母，并删除它们，使被删去的字符串的左侧和右侧连在一起。

你需要对 `s` 重复进行无限次这样的删除操作，直到无法继续为止。

在执行完所有删除操作后，返回最终得到的字符串。

本题答案保证唯一。

 

 **示例 1：** 

```
输入：s = "abcd", k = 2
输出："abcd"
解释：没有要删除的内容。
```
 **示例 2：** 

```
输入：s = "deeedbbcccbdaa", k = 3
输出："aa"
解释： 
先删除 "eee" 和 "ccc"，得到 "ddbbbdaa"
再删除 "bbb"，得到 "dddaa"
最后删除 "ddd"，得到 "aa"
```
 **示例 3：** 

```
输入：s = "pbbcggttciiippooaais", k = 2
输出："ps"

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `2 <= k <= 10^4` 
-  `s` 中只含有小写英文字母。
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 1210.穿过迷宫的最少移动次数
[https://leetcode-cn.com/problems/minimum-moves-to-reach-target-with-rotations](https://leetcode-cn.com/problems/minimum-moves-to-reach-target-with-rotations) 
## 原题
你还记得那条风靡全球的贪吃蛇吗？

我们在一个 `n*n` 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（ `(0, 0)` 和 `(0, 1)` ）开始移动。我们用 `0` 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（ `(n-1, n-2)` 和 `(n-1, n-1)` ）。

每次移动，蛇可以这样走：
- 如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
- 如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
- 如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（ `(r, c)` 、 `(r, c+1)` ）移动到 （ `(r, c)` 、 `(r+1, c)` ）。<br>
	<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/28/image-2.png" style="height: 134px; width: 300px;">
- 如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（ `(r, c)` 、 `(r+1, c)` ）移动到（ `(r, c)` 、 `(r, c+1)` ）。<br>
	<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/28/image-1.png" style="height: 121px; width: 300px;">
返回蛇抵达目的地所需的最少移动次数。

如果无法到达目的地，请返回 `-1` 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/28/image.png" style="height: 439px; width: 400px;">** 

```
输入：grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
输出：11
解释：
一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。

```
 **示例 2：** 

```
输入：grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
输出：9

```
 

 **提示：** 
-  `2 <= n <= 100` 
-  `0 <= grid[i][j] <= 1` 
- 蛇保证从空单元格开始出发。
 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 1211.查询结果的质量和占比
[https://leetcode-cn.com/problems/queries-quality-and-percentage](https://leetcode-cn.com/problems/queries-quality-and-percentage) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1212.查询球队积分
[https://leetcode-cn.com/problems/team-scores-in-football-tournament](https://leetcode-cn.com/problems/team-scores-in-football-tournament) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1213.三个有序数组的交集
[https://leetcode-cn.com/problems/intersection-of-three-sorted-arrays](https://leetcode-cn.com/problems/intersection-of-three-sorted-arrays) 
## 原题

 
**标签**
`数组` `哈希表` `二分查找` `计数` 


## 
```python

```
>
# 1214.查找两棵二叉搜索树之和
[https://leetcode-cn.com/problems/two-sum-bsts](https://leetcode-cn.com/problems/two-sum-bsts) 
## 原题

 
**标签**
`栈` `树` `深度优先搜索` `二叉搜索树` `双指针` `二分查找` `二叉树` 


## 
```python

```
>
# 1215.步进数
[https://leetcode-cn.com/problems/stepping-numbers](https://leetcode-cn.com/problems/stepping-numbers) 
## 原题

 
**标签**
`广度优先搜索` `回溯` 


## 
```python

```
>
# 1216.验证回文字符串 III
[https://leetcode-cn.com/problems/valid-palindrome-iii](https://leetcode-cn.com/problems/valid-palindrome-iii) 
## 原题

 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1217.玩筹码
[https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position](https://leetcode-cn.com/problems/minimum-cost-to-move-chips-to-the-same-position) 
## 原题
有 `n` 个筹码。第 `i` 个芯片的位置是<meta charset="UTF-8" /> `position[i]` 。

我们需要把所有筹码移到同一个位置。在一步中，我们可以将第 `i` 个芯片的位置从 `position[i]` 改变为:

<meta charset="UTF-8" />
-  `position[i] + 2` 或 `position[i] - 2` ，此时 `cost = 0` 
-  `position[i] + 1` 或 `position[i] - 1` ，此时 `cost = 1` 
返回将所有筹码移动到同一位置上所需要的 *最小代价* 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chips_e1.jpg" style="height: 217px; width: 750px;" />

```

输入：position = [1,2,3]
输出：1
解释：第一步:将位置3的芯片移动到位置1，成本为0。
第二步:将位置2的芯片移动到位置1，成本= 1。
总成本是1。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/15/chip_e2.jpg" style="height: 306px; width: 750px;" />

```

输入：position = [2,2,2,3,3]
输出：2
解释：我们可以把位置3的两个芯片移到位置2。每一步的成本为1。总成本= 2。

```
 **示例 3:** 

```

输入：position = [1,1000000000]
输出：1

```
 

 **提示：** 
-  `1 <= chips.length <= 100` 
-  `1 <= chips[i] <= 10^9` 
 
**标签**
`贪心` `数组` `数学` 


## 
```python

```
>
# 1218.最长定差子序列
[https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference](https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference) 
## 原题
给你一个整数数组  `arr`  和一个整数  `difference` ，请你找出并返回 `arr`  中最长等差子序列的长度，该子序列中相邻元素之间的差等于 `difference` 。

 **子序列** 是指在不改变其余元素顺序的情况下，通过删除一些元素或不删除任何元素而从 `arr` 派生出来的序列。

 

 **示例 1：** 

```

输入：arr = [1,2,3,4], difference = 1
输出：4
解释：最长的等差子序列是 [1,2,3,4]。
```
 **示例 2：** 

```

输入：arr = [1,3,5,7], difference = 1
输出：1
解释：最长的等差子序列是任意单个元素。

```
 **示例 3：** 

```

输入：arr = [1,5,7,8,5,3,4,2,1], difference = -2
输出：4
解释：最长的等差子序列是 [7,5,3,1]。

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `-10^4 <= arr[i], difference <= 10^4` 
 
**标签**
`数组` `哈希表` `动态规划` 


## 
```python

```
>
# 1219.黄金矿工
[https://leetcode-cn.com/problems/path-with-maximum-gold](https://leetcode-cn.com/problems/path-with-maximum-gold) 
## 原题
你要开发一座金矿，地质勘测学家已经探明了这座金矿中的资源分布，并用大小为 `m * n` 的网格 `grid` 进行了标注。每个单元格中的整数就表示这一单元格中的黄金数量；如果该单元格是空的，那么就是 `0` 。

为了使收益最大化，矿工需要按以下规则来开采黄金：
- 每当矿工进入一个单元，就会收集该单元格中的所有黄金。
- 矿工每次可以从当前位置向上下左右四个方向走。
- 每个单元格只能被开采（进入）一次。
-  **不得开采** （进入）黄金数目为 `0` 的单元格。
- 矿工可以从网格中 **任意一个** 有黄金的单元格出发或者是停止。
 

 **示例 1：** 

```
输入：grid = [[0,6,0],[5,8,7],[0,9,0]]
输出：24
解释：
[[0,6,0],
 [5,8,7],
 [0,9,0]]
一种收集最多黄金的路线是：9 -> 8 -> 7。

```
 **示例 2：** 

```
输入：grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
输出：28
解释：
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
一种收集最多黄金的路线是：1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7。

```
 

 **提示：** 
-  `1 <= grid.length, grid[i].length <= 15` 
-  `0 <= grid[i][j] <= 100` 
- 最多 **25** 个单元格中有黄金。
 
**标签**
`数组` `回溯` `矩阵` 


## 
```python

```
>
# 1220.统计元音字母序列的数目
[https://leetcode-cn.com/problems/count-vowels-permutation](https://leetcode-cn.com/problems/count-vowels-permutation) 
## 原题
给你一个整数 `n` ，请你帮忙统计一下我们可以按下述规则形成多少个长度为 `n` 的字符串：
- 字符串中的每个字符都应当是小写元音字母（ `';a';` , `';e';` , `';i';` , `';o';` , `';u';` ）
- 每个元音 `';a';` 后面都只能跟着 `';e';` 
- 每个元音 `';e';` 后面只能跟着 `';a';` 或者是 `';i';` 
- 每个元音 `';i';` 后面 **不能** 再跟着另一个 `';i';` 
- 每个元音 `';o';` 后面只能跟着 `';i';` 或者是 `';u';` 
- 每个元音 `';u';` 后面只能跟着 `';a';` 
由于答案可能会很大，所以请你返回 模 `10^9 + 7` 之后的结果。

 

 **示例 1：** 

```
输入：n = 1
输出：5
解释：所有可能的字符串分别是："a", "e", "i" , "o" 和 "u"。

```
 **示例 2：** 

```
输入：n = 2
输出：10
解释：所有可能的字符串分别是："ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" 和 "ua"。

```
 **示例 3：** 

```
输入：n = 5
输出：68
```
 

 **提示：** 
-  `1 <= n <= 2 * 10^4` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 1221.分割平衡字符串
[https://leetcode-cn.com/problems/split-a-string-in-balanced-strings](https://leetcode-cn.com/problems/split-a-string-in-balanced-strings) 
## 原题
在一个 **平衡字符串** 中， `'L'` 和 `'R'` 字符的数量是相同的。

给你一个平衡字符串 `s` ，请你将它分割成尽可能多的平衡字符串。

 **注意：** 分割得到的每个字符串都必须是平衡字符串，且分割得到的平衡字符串是原平衡字符串的连续子串。

返回可以通过分割得到的平衡字符串的 **最大数量** **。** 

 

 **示例 1：** 

```

输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL"、"RRLL"、"RL"、"RL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

```
 **示例 2：** 

```

输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL"、"LLLRRR"、"LR" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

```
 **示例 3：** 

```

输入：s = "LLLLRRRR"
输出：1
解释：s 只能保持原样 "LLLLRRRR".

```
 **示例 4：** 

```

输入：s = "RLRRRLLRLL"
输出：2
解释：s 可以分割为 "RL"、"RRRLLRLL" ，每个子字符串中都包含相同数量的 'L' 和 'R' 。

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s[i] = 'L' 或 'R'` 
-  `s` 是一个 **平衡** 字符串
 
**标签**
`贪心` `字符串` `计数` 


## 
```python

```
>
# 1222.可以攻击国王的皇后
[https://leetcode-cn.com/problems/queens-that-can-attack-the-king](https://leetcode-cn.com/problems/queens-that-can-attack-the-king) 
## 原题
在一个 **8x8** 的棋盘上，放置着若干「黑皇后」和一个「白国王」。

给定一个由整数坐标组成的数组 `queens` ，表示黑皇后的位置；以及一对坐标 `king` ，表示白国王的位置，返回所有可以攻击国王的皇后的坐标(任意顺序)。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/13/untitled-diagram.jpg" />

```

输入：queens = [[0,1],[1,0],[4,0],[0,4],[3,3],[2,4]], king = [0,0]
输出：[[0,1],[1,0],[3,3]]
解释： 
[0,1] 的皇后可以攻击到国王，因为他们在同一行上。 
[1,0] 的皇后可以攻击到国王，因为他们在同一列上。 
[3,3] 的皇后可以攻击到国王，因为他们在同一条对角线上。 
[0,4] 的皇后无法攻击到国王，因为她被位于 [0,1] 的皇后挡住了。 
[4,0] 的皇后无法攻击到国王，因为她被位于 [1,0] 的皇后挡住了。 
[2,4] 的皇后无法攻击到国王，因为她和国王不在同一行/列/对角线上。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/13/untitled-diagram-1.jpg" />** 

```

输入：queens = [[0,0],[1,1],[2,2],[3,4],[3,5],[4,4],[4,5]], king = [3,3]
输出：[[2,2],[3,4],[4,4]]

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/13/untitled-diagram-2.jpg" />** 

```

输入：queens = [[5,6],[7,7],[2,1],[0,7],[1,6],[5,1],[3,7],[0,3],[4,0],[1,2],[6,3],[5,0],[0,4],[2,2],[1,1],[6,4],[5,4],[0,0],[2,6],[4,5],[5,2],[1,4],[7,5],[2,3],[0,5],[4,2],[1,0],[2,7],[0,1],[4,6],[6,1],[0,6],[4,3],[1,7]], king = [3,4]
输出：[[2,3],[1,4],[1,6],[3,7],[4,3],[5,4],[4,5]]

```
 

 **提示：** 
-  `1 <= queens.length <= 63` 
-  `queens[i].length == 2` 
-  `0 <= queens[i][j] < 8` 
-  `king.length == 2` 
-  `0 <= king[0], king[1] < 8` 
- 一个棋盘格上最多只能放置一枚棋子。
 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 1223.掷骰子模拟
[https://leetcode-cn.com/problems/dice-roll-simulation](https://leetcode-cn.com/problems/dice-roll-simulation) 
## 原题
有一个骰子模拟器会每次投掷的时候生成一个 1 到 6 的随机数。

不过我们在使用它时有个约束，就是使得投掷骰子时， **连续** 掷出数字 `i` 的次数不能超过 `rollMax[i]` （ `i` 从 1 开始编号）。

现在，给你一个整数数组 `rollMax` 和一个整数 `n` ，请你来计算掷 `n` 次骰子可得到的不同点数序列的数量。

假如两个序列中至少存在一个元素不同，就认为这两个序列是不同的。由于答案可能很大，所以请返回 **模 `10^9 + 7` ** 之后的结果。

 

 **示例 1：** 

```
输入：n = 2, rollMax = [1,1,2,2,2,3]
输出：34
解释：我们掷 2 次骰子，如果没有约束的话，共有 6 * 6 = 36 种可能的组合。但是根据 rollMax 数组，数字 1 和 2 最多连续出现一次，所以不会出现序列 (1,1) 和 (2,2)。因此，最终答案是 36-2 = 34。

```
 **示例 2：** 

```
输入：n = 2, rollMax = [1,1,1,1,1,1]
输出：30

```
 **示例 3：** 

```
输入：n = 3, rollMax = [1,1,1,2,2,3]
输出：181

```
 

 **提示：** 
-  `1 <= n <= 5000` 
-  `rollMax.length == 6` 
-  `1 <= rollMax[i] <= 15` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1224.最大相等频率
[https://leetcode-cn.com/problems/maximum-equal-frequency](https://leetcode-cn.com/problems/maximum-equal-frequency) 
## 原题
给你一个正整数数组 `nums` ，请你帮忙从该数组中找出能满足下面要求的 **最长** 前缀，并返回该前缀的长度：
- 从前缀中 **恰好删除一个** 元素后，剩下每个数字的出现次数都相同。
如果删除这个元素后没有剩余元素存在，仍可认为每个数字都具有相同的出现次数（也就是 0 次）。

 

 **示例 1：** 

```

输入：nums = [2,2,1,1,5,3,3,5]
输出：7
解释：对于长度为 7 的子数组 [2,2,1,1,5,3,3]，如果我们从中删去 nums[4] = 5，就可以得到 [2,2,1,1,3,3]，里面每个数字都出现了两次。

```
 **示例 2：** 

```

输入：nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
输出：13

```
 

 **提示：** 
-  `2 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^5` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1225.报告系统状态的连续日期
[https://leetcode-cn.com/problems/report-contiguous-dates](https://leetcode-cn.com/problems/report-contiguous-dates) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1226.哲学家进餐
[https://leetcode-cn.com/problems/the-dining-philosophers](https://leetcode-cn.com/problems/the-dining-philosophers) 
## 原题
5 个沉默寡言的哲学家围坐在圆桌前，每人面前一盘意面。叉子放在哲学家之间的桌面上。（5 个哲学家，5 根叉子）

所有的哲学家都只会在思考和进餐两种行为间交替。哲学家只有同时拿到左边和右边的叉子才能吃到面，而同一根叉子在同一时间只能被一个哲学家使用。每个哲学家吃完面后都需要把叉子放回桌面以供其他哲学家吃面。只要条件允许，哲学家可以拿起左边或者右边的叉子，但在没有同时拿到左右叉子时不能进食。

假设面的数量没有限制，哲学家也能随便吃，不需要考虑吃不吃得下。

设计一个进餐规则（并行算法）使得每个哲学家都不会挨饿；也就是说，在没有人知道别人什么时候想吃东西或思考的情况下，每个哲学家都可以在吃饭和思考之间一直交替下去。

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/23/an_illustration_of_the_dining_philosophers_problem.png" style="height: 415px; width: 400px;">

 *问题描述和图片来自维基百科 <a href="https://en.wikipedia.org/wiki/Dining_philosophers_problem" target="_blank">wikipedia.org</a>* 

 

哲学家从 **0** 到 **4** 按 **顺时针** 编号。请实现函数 `void wantsToEat(philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork)` ：
-  `philosopher` 哲学家的编号。
-  `pickLeftFork` 和 `pickRightFork` 表示拿起左边或右边的叉子。
-  `eat` 表示吃面。
-  `putLeftFork` 和 `putRightFork` 表示放下左边或右边的叉子。
- 由于哲学家不是在吃面就是在想着啥时候吃面，所以思考这个方法没有对应的回调。
给你 5 个线程，每个都代表一个哲学家，请你使用类的同一个对象来模拟这个过程。在最后一次调用结束之前，可能会为同一个哲学家多次调用该函数。

 

 **示例：** 

```
输入：n = 1
输出：[[4,2,1],[4,1,1],[0,1,1],[2,2,1],[2,1,1],[2,0,3],[2,1,2],[2,2,2],[4,0,3],[4,1,2],[0,2,1],[4,2,2],[3,2,1],[3,1,1],[0,0,3],[0,1,2],[0,2,2],[1,2,1],[1,1,1],[3,0,3],[3,1,2],[3,2,2],[1,0,3],[1,1,2],[1,2,2]]
解释:
n 表示每个哲学家需要进餐的次数。
输出数组描述了叉子的控制和进餐的调用，它的格式如下：
output[i] = [a, b, c] (3个整数)
- a 哲学家编号。
- b 指定叉子：{1 : 左边, 2 : 右边}.
- c 指定行为：{1 : 拿起, 2 : 放下, 3 : 吃面}。
如 [4,2,1] 表示 4 号哲学家拿起了右边的叉子。

```
 

 **提示：** 
-  `1 <= n <= 60` 
 
**标签**
`多线程` 


## 
```python

```
>
# 1227.飞机座位分配概率
[https://leetcode-cn.com/problems/airplane-seat-assignment-probability](https://leetcode-cn.com/problems/airplane-seat-assignment-probability) 
## 原题
有 `n` 位乘客即将登机，飞机正好有 `n` 个座位。第一位乘客的票丢了，他随便选了一个座位坐下。

剩下的乘客将会：
- 
	如果他们自己的座位还空着，就坐到自己的座位上，
	
- 当他们自己的座位被占用时，随机选择其他座位
第 `n` 位乘客坐在自己的座位上的概率是多少？

 

 **示例 1：** 

```

输入：n = 1
输出：1.00000
解释：第一个人只会坐在自己的位置上。
```
 **示例 2：** 

```

输入: n = 2
输出: 0.50000
解释：在第一个人选好座位坐下后，第二个人坐在自己的座位上的概率是 0.5。

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
 
**标签**
`脑筋急转弯` `数学` `动态规划` `概率与统计` 


## 
```python

```
>
# 1228.等差数列中缺失的数字
[https://leetcode-cn.com/problems/missing-number-in-arithmetic-progression](https://leetcode-cn.com/problems/missing-number-in-arithmetic-progression) 
## 原题

 
**标签**
`数组` `数学` 


## 
```python

```
>
# 1229.安排会议日程
[https://leetcode-cn.com/problems/meeting-scheduler](https://leetcode-cn.com/problems/meeting-scheduler) 
## 原题

 
**标签**
`数组` `双指针` `排序` 


## 
```python

```
>
# 1230.抛掷硬币
[https://leetcode-cn.com/problems/toss-strange-coins](https://leetcode-cn.com/problems/toss-strange-coins) 
## 原题

 
**标签**
`数学` `动态规划` `概率与统计` 


## 
```python

```
>
# 1231.分享巧克力
[https://leetcode-cn.com/problems/divide-chocolate](https://leetcode-cn.com/problems/divide-chocolate) 
## 原题

 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 1232.缀点成线
[https://leetcode-cn.com/problems/check-if-it-is-a-straight-line](https://leetcode-cn.com/problems/check-if-it-is-a-straight-line) 
## 原题
给定一个数组 `coordinates` ，其中 `coordinates[i] = [x, y]` ，<meta charset="UTF-8" /> `[x, y]` 表示横坐标为 `x` 、纵坐标为 `y` 的点。请你来判断，这些点是否在该坐标系中属于同一条直线上。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-2.jpg" />

```

输入：coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
输出：true

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/untitled-diagram-1.jpg" />** 

```

输入：coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
输出：false

```
 

 **提示：** 
-  `2 <= coordinates.length <= 1000` 
-  `coordinates[i].length == 2` 
-  `-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4` 
-  `coordinates` 中不含重复的点
 
**标签**
`几何` `数组` `数学` 


## 
```python

```
>
# 1233.删除子文件夹
[https://leetcode-cn.com/problems/remove-sub-folders-from-the-filesystem](https://leetcode-cn.com/problems/remove-sub-folders-from-the-filesystem) 
## 原题
你是一位系统管理员，手里有一份文件夹列表 `folder` ，你的任务是要删除该列表中的所有 **子文件夹** ，并以 **任意顺序** 返回剩下的文件夹。

如果文件夹 `folder[i]` 位于另一个文件夹 `folder[j]` 下，那么 `folder[i]` 就是 `folder[j]` 的 **子文件夹** 。

文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：<font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'/'</span></span></font></font> 后跟一个或者多个小写英文字母。
- 例如， `"/leetcode"` 和 `"/leetcode/problems"` 都是有效的路径，而空字符串和 `"/"` 不是。
 

 **示例 1：** 

```

输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
输出：["/a","/c/d","/c/f"]
解释："/a/b/" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。

```
 **示例 2：** 

```

输入：folder = ["/a","/a/b/c","/a/b/d"]
输出：["/a"]
解释：文件夹 "/a/b/c" 和 "/a/b/d/" 都会被删除，因为它们都是 "/a" 的子文件夹。

```
 **示例 3：** 

```

输入: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
输出: ["/a/b/c","/a/b/ca","/a/b/d"]
```
 

 **提示：** 
-  `1 <= folder.length <= 4 * 10^4` 
-  `2 <= folder[i].length <= 100` 
-  `folder[i]` 只包含小写字母和 `'/'` 
-  `folder[i]` 总是以字符 `'/'` 起始
- 每个文件夹名都是 **唯一** 的
 
**标签**
`字典树` `数组` `字符串` 


## 
```python

```
>
# 1234.替换子串得到平衡字符串
[https://leetcode-cn.com/problems/replace-the-substring-for-balanced-string](https://leetcode-cn.com/problems/replace-the-substring-for-balanced-string) 
## 原题
有一个只含有 `';Q';, ';W';, ';E';, ';R';` 四种字符，且长度为 `n` 的字符串。

假如在该字符串中，这四个字符都恰好出现 `n/4` 次，那么它就是一个「平衡字符串」。

 

给你一个这样的字符串 `s` ，请通过「替换一个子串」的方式，使原字符串 `s` 变成一个「平衡字符串」。

你可以用和「待替换子串」长度相同的 **任何** 其他字符串来完成替换。

请返回待替换子串的最小可能长度。

如果原字符串自身就是一个平衡字符串，则返回 `0` 。

 

 **示例 1：** 

```
输入：s = "QWER"
输出：0
解释：s 已经是平衡的了。
```
 **示例 2：** 

```
输入：s = "QQWE"
输出：1
解释：我们需要把一个 ';Q'; 替换成 ';R';，这样得到的 "RQWE" (或 "QRWE") 是平衡的。

```
 **示例 3：** 

```
输入：s = "QQQW"
输出：2
解释：我们可以把前面的 "QQ" 替换成 "ER"。 

```
 **示例 4：** 

```
输入：s = "QQQQ"
输出：3
解释：我们可以替换后 3 个 ';Q';，使 s = "QWER"。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s.length` 是 `4` 的倍数
-  `s` 中只含有 `';Q';` , `';W';` , `';E';` , `';R';` 四种字符
 
**标签**
`字符串` `滑动窗口` 


## 
```python

```
>
# 1235.规划兼职工作
[https://leetcode-cn.com/problems/maximum-profit-in-job-scheduling](https://leetcode-cn.com/problems/maximum-profit-in-job-scheduling) 
## 原题
你打算利用空闲时间来做兼职工作赚些零花钱。

这里有 `n` 份兼职工作，每份工作预计从 `startTime[i]` 开始到 `endTime[i]` 结束，报酬为 `profit[i]` 。

给你一份兼职工作表，包含开始时间 `startTime` ，结束时间 `endTime` 和预计报酬 `profit` 三个数组，请你计算并返回可以获得的最大报酬。

注意，时间上出现重叠的 2 份工作不能同时进行。

如果你选择的工作在时间 `X` 结束，那么你可以立刻进行在时间 `X` 开始的下一份工作。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/sample1_1584.png" style="width: 300px;">** 

```
输入：startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
输出：120
解释：
我们选出第 1 份和第 4 份工作， 
时间范围是 [1-3]+[3-6]，共获得报酬 120 = 50 + 70。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/sample22_1584.png" style="height: 112px; width: 600px;">** 

```
输入：startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
输出：150
解释：
我们选择第 1，4，5 份工作。 
共获得报酬 150 = 20 + 70 + 60。

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/19/sample3_1584.png" style="height: 112px; width: 400px;">** 

```
输入：startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
输出：6

```
 

 **提示：** 
-  `1 <= startTime.length == endTime.length == profit.length <= 5 * 10^4` 
-  `1 <= startTime[i] < endTime[i] <= 10^9` 
-  `1 <= profit[i] <= 10^4` 
 
**标签**
`数组` `二分查找` `动态规划` `排序` 


## 
```python

```
>
# 1236.网络爬虫
[https://leetcode-cn.com/problems/web-crawler](https://leetcode-cn.com/problems/web-crawler) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `字符串` `交互` 


## 
```python

```
>
# 1237.找出给定方程的正整数解
[https://leetcode-cn.com/problems/find-positive-integer-solution-for-a-given-equation](https://leetcode-cn.com/problems/find-positive-integer-solution-for-a-given-equation) 
## 原题
给你一个函数   `f(x, y)`  和一个目标结果  `z` ，函数公式未知，请你计算方程  `f(x,y) == z`  所有可能的正整数 **数对**   `x` 和 `y` 。满足条件的结果数对可以按任意顺序返回。

尽管函数的具体式子未知，但它是单调递增函数，也就是说：
-  `f(x, y) < f(x + 1, y)` 
-  `f(x, y) < f(x, y + 1)` 
函数接口定义如下：

```

interface CustomFunction {
public:
  // Returns some positive integer f(x, y) for two positive integers x and y based on a formula.
  int f(int x, int y);
};
```
你的解决方案将按如下规则进行评判：
- 判题程序有一个由 `CustomFunction` 的 `9` 种实现组成的列表，以及一种为特定的 `z` 生成所有有效数对的答案的方法。
- 判题程序接受两个输入： `function_id` （决定使用哪种实现测试你的代码）以及目标结果 `z` 。
- 判题程序将会调用你实现的 `findSolution` 并将你的结果与答案进行比较。
- 如果你的结果与答案相符，那么解决方案将被视作正确答案，即 `Accepted` 。
 

 **示例 1：** 

```

输入：function_id = 1, z = 5
输出：[[1,4],[2,3],[3,2],[4,1]]
解释：function_id = 1 暗含的函数式子为 f(x, y) = x + y
以下 x 和 y 满足 f(x, y) 等于 5：
x=1, y=4 -> f(1, 4) = 1 + 4 = 5
x=2, y=3 -> f(2, 3) = 2 + 3 = 5
x=3, y=2 -> f(3, 2) = 3 + 2 = 5
x=4, y=1 -> f(4, 1) = 4 + 1 = 5

```
 **示例 2：** 

```

输入：function_id = 2, z = 5
输出：[[1,5],[5,1]]
解释：function_id = 2 暗含的函数式子为 f(x, y) = x * y
以下 x 和 y 满足 f(x, y) 等于 5：
x=1, y=5 -> f(1, 5) = 1 * 5 = 5
x=5, y=1 -> f(5, 1) = 5 * 1 = 5
```
 

 **提示：** 
-  `1 <= function_id <= 9` 
-  `1 <= z <= 100` 
- 题目保证  `f(x, y) == z`  的解处于  `1 <= x, y <= 1000`  的范围内。
- 在 `1 <= x, y <= 1000`  的前提下，题目保证  `f(x, y)`  是一个 32 位有符号整数。
 
**标签**
`数学` `双指针` `二分查找` `交互` 


## 
```python

```
>
# 1238.循环码排列
[https://leetcode-cn.com/problems/circular-permutation-in-binary-representation](https://leetcode-cn.com/problems/circular-permutation-in-binary-representation) 
## 原题
给你两个整数 `n` 和 `start` 。你的任务是返回任意 `(0,1,2,,...,2^n-1)` 的排列 `p` ，并且满足：
-  `p[0] = start` 
-  `p[i]` 和 `p[i+1]` 的二进制表示形式只有一位不同
-  `p[0]` 和 `p[2^n -1]` 的二进制表示形式也只有一位不同
 

 **示例 1：** 

```
输入：n = 2, start = 3
输出：[3,2,0,1]
解释：这个排列的二进制表示是 (11,10,00,01)
     所有的相邻元素都有一位是不同的，另一个有效的排列是 [3,1,0,2]

```
 **示例 2：** 

```
输出：n = 3, start = 2
输出：[2,6,7,5,4,0,1,3]
解释：这个排列的二进制表示是 (010,110,111,101,100,000,001,011)

```
 

 **提示：** 
-  `1 <= n <= 16` 
-  `0 <= start < 2^n` 
 
**标签**
`位运算` `数学` `回溯` 


## 
```python

```
>
# 1239.串联字符串的最大长度
[https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters](https://leetcode-cn.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters) 
## 原题
给定一个字符串数组 `arr` ，字符串 `s` 是将 `arr` 某一子序列字符串连接所得的字符串，如果 `s` 中的每一个字符都只出现过一次，那么它就是一个可行解。

请返回所有可行解 `s` 中最长长度。

 

 **示例 1：** 

```
输入：arr = ["un","iq","ue"]
输出：4
解释：所有可能的串联组合是 "","un","iq","ue","uniq" 和 "ique"，最大长度为 4。

```
 **示例 2：** 

```
输入：arr = ["cha","r","act","ers"]
输出：6
解释：可能的解答有 "chaers" 和 "acters"。

```
 **示例 3：** 

```
输入：arr = ["abcdefghijklmnopqrstuvwxyz"]
输出：26

```
 

 **提示：** 
-  `1 <= arr.length <= 16` 
-  `1 <= arr[i].length <= 26` 
-  `arr[i]` 中只含有小写英文字母
 
**标签**
`位运算` `数组` `字符串` `回溯` 


## 
```python

```
>
# 1240.铺瓷砖
[https://leetcode-cn.com/problems/tiling-a-rectangle-with-the-fewest-squares](https://leetcode-cn.com/problems/tiling-a-rectangle-with-the-fewest-squares) 
## 原题
你是一位施工队的工长，根据设计师的要求准备为一套设计风格独特的房子进行室内装修。

房子的客厅大小为 `n` x `m` ，为保持极简的风格，需要使用尽可能少的 **正方形** 瓷砖来铺盖地面。

假设正方形瓷砖的规格不限，边长都是整数。

请你帮设计师计算一下，最少需要用到多少块方形瓷砖？

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/25/sample_11_1592.png" style="height: 106px; width: 154px;">

```
输入：n = 2, m = 3
输出：3
解释：3 块地砖就可以铺满卧室。
     2 块 1x1 地砖
     1 块 2x2 地砖
```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/25/sample_22_1592.png" style="height: 126px; width: 224px;">

```
输入：n = 5, m = 8
输出：5

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/10/25/sample_33_1592.png" style="height: 189px; width: 224px;">

```
输入：n = 11, m = 13
输出：6

```
 

 **提示：** 
-  `1 <= n <= 13` 
-  `1 <= m <= 13` 
 
**标签**
`动态规划` `回溯` 


## 
```python

```
>
# 1241.每个帖子的评论数
[https://leetcode-cn.com/problems/number-of-comments-per-post](https://leetcode-cn.com/problems/number-of-comments-per-post) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1242.多线程网页爬虫
[https://leetcode-cn.com/problems/web-crawler-multithreaded](https://leetcode-cn.com/problems/web-crawler-multithreaded) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `多线程` 


## 
```python

```
>
# 1243.数组变换
[https://leetcode-cn.com/problems/array-transformation](https://leetcode-cn.com/problems/array-transformation) 
## 原题

 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 1244.力扣排行榜
[https://leetcode-cn.com/problems/design-a-leaderboard](https://leetcode-cn.com/problems/design-a-leaderboard) 
## 原题

 
**标签**
`设计` `哈希表` `排序` 


## 
```python

```
>
# 1245.树的直径
[https://leetcode-cn.com/problems/tree-diameter](https://leetcode-cn.com/problems/tree-diameter) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` 


## 
```python

```
>
# 1246.删除回文子数组
[https://leetcode-cn.com/problems/palindrome-removal](https://leetcode-cn.com/problems/palindrome-removal) 
## 原题

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1247.交换字符使得字符串相同
[https://leetcode-cn.com/problems/minimum-swaps-to-make-strings-equal](https://leetcode-cn.com/problems/minimum-swaps-to-make-strings-equal) 
## 原题
有两个长度相同的字符串 `s1` 和 `s2` ，且它们其中 **只含有** 字符 `"x"` 和 `"y"` ，你需要通过「交换字符」的方式使这两个字符串相同。

每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。

交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。也就是说，我们可以交换 `s1[i]` 和 `s2[j]` ，但不能交换 `s1[i]` 和 `s1[j]` 。

最后，请你返回使 `s1` 和 `s2` 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 `-1` 。

 

 **示例 1：** 

```
输入：s1 = "xx", s2 = "yy"
输出：1
解释：
交换 s1[0] 和 s2[1]，得到 s1 = "yx"，s2 = "yx"。
```
 **示例 2：** 

```
输入：s1 = "xy", s2 = "yx"
输出：2
解释：
交换 s1[0] 和 s2[0]，得到 s1 = "yy"，s2 = "xx" 。
交换 s1[0] 和 s2[1]，得到 s1 = "xy"，s2 = "xy" 。
注意，你不能交换 s1[0] 和 s1[1] 使得 s1 变成 "yx"，因为我们只能交换属于两个不同字符串的字符。
```
 **示例 3：** 

```
输入：s1 = "xx", s2 = "xy"
输出：-1

```
 **示例 4：** 

```
输入：s1 = "xxyyxyxyxx", s2 = "xyyxyxxxyx"
输出：4

```
 

 **提示：** 
-  `1 <= s1.length, s2.length <= 1000` 
-  `s1, s2` 只包含 `';x';` 或 `';y';` 。
 
**标签**
`贪心` `数学` `字符串` 


## 
```python

```
>
# 1248.统计「优美子数组」
[https://leetcode-cn.com/problems/count-number-of-nice-subarrays](https://leetcode-cn.com/problems/count-number-of-nice-subarrays) 
## 原题
给你一个整数数组 `nums` 和一个整数 `k` 。如果某个连续子数组中恰好有 `k` 个奇数数字，我们就认为这个子数组是「 **优美子数组** 」。

请返回这个数组中 **「优美子数组」** 的数目。

 

 **示例 1：** 

```

输入：nums = [1,1,2,1,1], k = 3
输出：2
解释：包含 3 个奇数的子数组是 [1,1,2,1] 和 [1,2,1,1] 。

```
 **示例 2：** 

```

输入：nums = [2,4,6], k = 1
输出：0
解释：数列中不包含任何奇数，所以不存在优美子数组。

```
 **示例 3：** 

```

输入：nums = [2,2,2,1,2,2,1,2,2,2], k = 2
输出：16

```
 

 **提示：** 
-  `1 <= nums.length <= 50000` 
-  `1 <= nums[i] <= 10^5` 
-  `1 <= k <= nums.length` 
 
**标签**
`数组` `哈希表` `数学` `滑动窗口` 


## 
```python

```
>
# 1249.移除无效的括号
[https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses](https://leetcode-cn.com/problems/minimum-remove-to-make-valid-parentheses) 
## 原题
给你一个由 `'('` 、 `')'` 和小写字母组成的字符串 `s` 。

你需要从字符串中删除最少数目的 `'('` 或者 `')'` （可以删除任意位置的括号)，使得剩下的「括号字符串」有效。

请返回任意一个合法字符串。

有效「括号字符串」应当符合以下 **任意一条** 要求：
- 空字符串或只包含小写字母的字符串
- 可以被写作 `AB` （ `A` 连接 `B` ）的字符串，其中 `A` 和 `B` 都是有效「括号字符串」
- 可以被写作 `(A)` 的字符串，其中 `A` 是一个有效的「括号字符串」
 

 **示例 1：** 

```

输入：s = "lee(t(c)o)de)"
输出："lee(t(c)o)de"
解释："lee(t(co)de)" , "lee(t(c)ode)" 也是一个可行答案。

```
 **示例 2：** 

```

输入：s = "a)b(c)d"
输出："ab(c)d"

```
 **示例 3：** 

```

输入：s = "))(("
输出：""
解释：空字符串也是有效的

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s[i]` 可能是 `'('` 、 `')'` 或英文小写字母
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 1250.检查「好数组」
[https://leetcode-cn.com/problems/check-if-it-is-a-good-array](https://leetcode-cn.com/problems/check-if-it-is-a-good-array) 
## 原题
给你一个正整数数组 `nums` ，你需要从中任选一些子集，然后将子集中每一个数乘以一个 **任意整数** ，并求出他们的和。

假如该和结果为 `1` ，那么原数组就是一个「 **好数组** 」，则返回 `True` ；否则请返回 `False` 。

 

 **示例 1：** 

```
输入：nums = [12,5,7,23]
输出：true
解释：挑选数字 5 和 7。
5*3 + 7*(-2) = 1

```
 **示例 2：** 

```
输入：nums = [29,6,10]
输出：true
解释：挑选数字 29, 6 和 10。
29*1 + 6*(-3) + 10*(-1) = 1

```
 **示例 3：** 

```
输入：nums = [3,6]
输出：false

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^9` 
 
**标签**
`数组` `数学` `数论` 


## 
```python

```
>
# 1251.平均售价
[https://leetcode-cn.com/problems/average-selling-price](https://leetcode-cn.com/problems/average-selling-price) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1252.奇数值单元格的数目
[https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix](https://leetcode-cn.com/problems/cells-with-odd-values-in-a-matrix) 
## 原题
给你一个 `m x n` 的矩阵，最开始的时候，每个单元格中的值都是 `0` 。

另有一个二维索引数组  `indices` ， `indices[i] = [ri, ci]` 指向矩阵中的某个位置，其中 `ri` 和 `ci` 分别表示指定的行和列（ **从 `0` 开始编号** ）。

对 `indices[i]` 所指向的每个位置，应同时执行下述增量操作：
-  `r<sub>i</sub>` 行上的所有单元格，加 `1` 。
-  `c<sub>i</sub>` 列上的所有单元格，加 `1` 。
给你 `m` 、 `n` 和 `indices` 。请你在执行完所有  `indices`  指定的增量操作后，返回矩阵中 **奇数值单元格** 的数目。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/06/e1.png" style="height: 118px; width: 600px;" />

```

输入：m = 2, n = 3, indices = [[0,1],[1,1]]
输出：6
解释：最开始的矩阵是 [[0,0,0],[0,0,0]]。
第一次增量操作后得到 [[1,2,1],[0,1,0]]。
最后的矩阵是 [[1,3,1],[1,3,1]]，里面有 6 个奇数。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/06/e2.png" style="height: 150px; width: 600px;" />

```

输入：m = 2, n = 2, indices = [[1,1],[0,0]]
输出：0
解释：最后的矩阵是 [[2,2],[2,2]]，里面没有奇数。

```
 

 **提示：** 
-  `1 <= m, n <= 50` 
-  `1 <= indices.length <= 100` 
-  `0 <= r<sub>i</sub> < m` 
-  `0 <= c<sub>i</sub> < n` 
 

 **进阶：** 你可以设计一个时间复杂度为 `O(n + m + indices.length)` 且仅用 `O(n + m)` 额外空间的算法来解决此问题吗？

 
**标签**
`数组` `数学` `模拟` 


## 
```python

```
>
# 1253.重构 2 行二进制矩阵
[https://leetcode-cn.com/problems/reconstruct-a-2-row-binary-matrix](https://leetcode-cn.com/problems/reconstruct-a-2-row-binary-matrix) 
## 原题
给你一个 `2` 行 `n` 列的二进制数组：
- 矩阵是一个二进制矩阵，这意味着矩阵中的每个元素不是 `0` 就是 `1` 。
- 第 `0` 行的元素之和为 `upper` 。
- 第 `1` 行的元素之和为 `lower` 。
- 第 `i` 列（从 `0` 开始编号）的元素之和为 `colsum[i]` ， `colsum` 是一个长度为 `n` 的整数数组。
你需要利用 `upper` ， `lower` 和 `colsum` 来重构这个矩阵，并以二维整数数组的形式返回它。

如果有多个不同的答案，那么任意一个都可以通过本题。

如果不存在符合要求的答案，就请返回一个空的二维数组。

 

 **示例 1：** 

```
输入：upper = 2, lower = 1, colsum = [1,1,1]
输出：[[1,1,0],[0,0,1]]
解释：[[1,0,1],[0,1,0]] 和 [[0,1,1],[1,0,0]] 也是正确答案。

```
 **示例 2：** 

```
输入：upper = 2, lower = 3, colsum = [2,2,1,1]
输出：[]

```
 **示例 3：** 

```
输入：upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
输出：[[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]

```
 

 **提示：** 
-  `1 <= colsum.length <= 10^5` 
-  `0 <= upper, lower <= colsum.length` 
-  `0 <= colsum[i] <= 2` 
 
**标签**
`贪心` `数组` `矩阵` 


## 
```python

```
>
# 1254.统计封闭岛屿的数目
[https://leetcode-cn.com/problems/number-of-closed-islands](https://leetcode-cn.com/problems/number-of-closed-islands) 
## 原题
二维矩阵 `grid` 由 `0` （土地）和 `1` （水）组成。岛是由最大的4个方向连通的 `0` 组成的群，封闭岛是一个 `完全` 由1包围（左、上、右、下）的岛。

请返回 *封闭岛屿* 的数目。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2019/10/31/sample_3_1610.png" style="height: 151px; width: 240px;" />

```

输入：grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
输出：2
解释：
灰色区域的岛屿是封闭岛屿，因为这座岛屿完全被水域包围（即被 1 区域包围）。
```
 **示例 2：** 

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/07/sample_4_1610.png" style="height: 98px; width: 160px;" />

```

输入：grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
输出：1

```
 **示例 3：** 

```

输入：grid = [[1,1,1,1,1,1,1],
             [1,0,0,0,0,0,1],
             [1,0,1,1,1,0,1],
             [1,0,1,0,1,0,1],
             [1,0,1,1,1,0,1],
             [1,0,0,0,0,0,1],
             [1,1,1,1,1,1,1]]
输出：2

```
 

 **提示：** 
-  `1 <= grid.length, grid[0].length <= 100` 
-  `0 <= grid[i][j] <=1` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` 


## 
```python

```
>
# 1255.得分最高的单词集合
[https://leetcode-cn.com/problems/maximum-score-words-formed-by-letters](https://leetcode-cn.com/problems/maximum-score-words-formed-by-letters) 
## 原题
你将会得到一份单词表 `words` ，一个字母表 `letters` （可能会有重复字母），以及每个字母对应的得分情况表 `score` 。

请你帮忙计算玩家在单词拼写游戏中所能获得的「最高得分」：能够由 `letters` 里的字母拼写出的 **任意** 属于 `words` 单词子集中，分数最高的单词集合的得分。

单词拼写游戏的规则概述如下：
- 玩家需要用字母表 `letters` 里的字母来拼写单词表 `words` 中的单词。
- 可以只使用字母表 `letters` 中的部分字母，但是每个字母最多被使用一次。
- 单词表 `words` 中每个单词只能计分（使用）一次。
- 根据字母得分情况表 `score` ，字母 `';a';` , `';b';` , `';c';` , ... , `';z';` 对应的得分分别为 `score[0]` , `score[1]` , ..., `score[25]` 。
- 本场游戏的「得分」是指：玩家所拼写出的单词集合里包含的所有字母的得分之和。
 

 **示例 1：** 

```
输入：words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
输出：23
解释：
字母得分为  a=1, c=9, d=5, g=3, o=2
使用给定的字母表 letters，我们可以拼写单词 "dad" (5+1+5)和 "good" (3+2+2+5)，得分为 23 。
而单词 "dad" 和 "dog" 只能得到 21 分。
```
 **示例 2：** 

```
输入：words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
输出：27
解释：
字母得分为  a=4, b=4, c=4, x=5, z=10
使用给定的字母表 letters，我们可以组成单词 "ax" (4+5)， "bx" (4+5) 和 "cx" (4+5) ，总得分为 27 。
单词 "xxxz" 的得分仅为 25 。
```
 **示例 3：** 

```
输入：words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
输出：0
解释：
字母 "e" 在字母表 letters 中只出现了一次，所以无法组成单词表 words 中的单词。
```
 

 **提示：** 
-  `1 <= words.length <= 14` 
-  `1 <= words[i].length <= 15` 
-  `1 <= letters.length <= 100` 
-  `letters[i].length == 1` 
-  `score.length == 26` 
-  `0 <= score[i] <= 10` 
-  `words[i]` 和 `letters[i]` 只包含小写的英文字母。
 
**标签**
`位运算` `数组` `字符串` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 1256.加密数字
[https://leetcode-cn.com/problems/encode-number](https://leetcode-cn.com/problems/encode-number) 
## 原题

 
**标签**
`位运算` `数学` `字符串` 


## 
```python

```
>
# 1257.最小公共区域
[https://leetcode-cn.com/problems/smallest-common-region](https://leetcode-cn.com/problems/smallest-common-region) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `数组` `哈希表` `字符串` 


## 
```python

```
>
# 1258.近义词句子
[https://leetcode-cn.com/problems/synonymous-sentences](https://leetcode-cn.com/problems/synonymous-sentences) 
## 原题

 
**标签**
`并查集` `数组` `哈希表` `字符串` `回溯` 


## 
```python

```
>
# 1259.不相交的握手
[https://leetcode-cn.com/problems/handshakes-that-dont-cross](https://leetcode-cn.com/problems/handshakes-that-dont-cross) 
## 原题

 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 1260.二维网格迁移
[https://leetcode-cn.com/problems/shift-2d-grid](https://leetcode-cn.com/problems/shift-2d-grid) 
## 原题
给你一个 `m` 行 `n`  列的二维网格  `grid`  和一个整数  `k` 。你需要将  `grid`  迁移  `k`  次。

每次「迁移」操作将会引发下述活动：
- 位于 `grid[i][j]`  的元素将会移动到  `grid[i][j + 1]` 。
- 位于  `grid[i][n - 1]` 的元素将会移动到  `grid[i + 1][0]` 。
- 位于 `grid[m - 1][n - 1]`  的元素将会移动到  `grid[0][0]` 。
请你返回  `k` 次迁移操作后最终得到的 **二维网格** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/e1-1.png" style="height: 158px; width: 400px;" />

```

输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[9,1,2],[3,4,5],[6,7,8]]

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/e2-1.png" style="height: 166px; width: 400px;" />

```

输入：grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
输出：[[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

```
 **示例 3：** 

```

输入：grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
输出：[[1,2,3],[4,5,6],[7,8,9]]

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m <= 50` 
-  `1 <= n <= 50` 
-  `-1000 <= grid[i][j] <= 1000` 
-  `0 <= k <= 100` 
 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 1261.在受污染的二叉树中查找元素
[https://leetcode-cn.com/problems/find-elements-in-a-contaminated-binary-tree](https://leetcode-cn.com/problems/find-elements-in-a-contaminated-binary-tree) 
## 原题
给出一个满足下述规则的二叉树：
-  `root.val == 0` 
- 如果 `treeNode.val == x` 且 `treeNode.left != null` ，那么 `treeNode.left.val == 2 * x + 1` 
- 如果 `treeNode.val == x` 且 `treeNode.right != null` ，那么 `treeNode.right.val == 2 * x + 2` 
现在这个二叉树受到「污染」，所有的 `treeNode.val` 都变成了 `-1` 。

请你先还原二叉树，然后实现 `FindElements` 类：
-  `FindElements(TreeNode* root)` 用受污染的二叉树初始化对象，你需要先把它还原。
-  `bool find(int target)` 判断目标值 `target` 是否存在于还原后的二叉树中并返回结果。
 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/untitled-diagram-4-1.jpg" style="height: 119px; width: 320px;">** 

```
输入：
["FindElements","find","find"]
[[[-1,null,-1]],[1],[2]]
输出：
[null,false,true]
解释：
FindElements findElements = new FindElements([-1,null,-1]); 
findElements.find(1); // return False 
findElements.find(2); // return True 
```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/untitled-diagram-4.jpg" style="height: 198px; width: 400px;">** 

```
输入：
["FindElements","find","find","find"]
[[[-1,-1,-1,-1,-1]],[1],[3],[5]]
输出：
[null,true,true,false]
解释：
FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
findElements.find(1); // return True
findElements.find(3); // return True
findElements.find(5); // return False
```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/untitled-diagram-4-1-1.jpg" style="height: 274px; width: 306px;">** 

```
输入：
["FindElements","find","find","find","find"]
[[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
输出：
[null,true,false,false,true]
解释：
FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
findElements.find(2); // return True
findElements.find(3); // return False
findElements.find(4); // return False
findElements.find(5); // return True

```
 

 **提示：** 
-  `TreeNode.val == -1` 
- 二叉树的高度不超过 `20` 
- 节点的总数在 `[1, 10^4]` 之间
- 调用 `find()` 的总次数在 `[1, 10^4]` 之间
-  `0 <= target <= 10^6` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `设计` `二叉树` 


## 
```python

```
>
# 1262.可被三整除的最大和
[https://leetcode-cn.com/problems/greatest-sum-divisible-by-three](https://leetcode-cn.com/problems/greatest-sum-divisible-by-three) 
## 原题
给你一个整数数组 `nums` ，请你找出并返回能被三整除的元素最大和。
 

 **示例 1：** 

```
输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
```
 **示例 2：** 

```
输入：nums = [4]
输出：0
解释：4 不能被 3 整除，所以无法选出数字，返回 0。

```
 **示例 3：** 

```
输入：nums = [1,2,3,4,4]
输出：12
解释：选出数字 1, 3, 4 以及 4，它们的和是 12（可被 3 整除的最大和）。

```
 

 **提示：** 
-  `1 <= nums.length <= 4 * 10^4` 
-  `1 <= nums[i] <= 10^4` 
 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 1263.推箱子
[https://leetcode-cn.com/problems/minimum-moves-to-move-a-box-to-their-target-location](https://leetcode-cn.com/problems/minimum-moves-to-move-a-box-to-their-target-location) 
## 原题
「推箱子」是一款风靡全球的益智小游戏，玩家需要将箱子推到仓库中的目标位置。

游戏地图用大小为 `n * m` 的网格 `grid` 表示，其中每个元素可以是墙、地板或者是箱子。

现在你将作为玩家参与游戏，按规则将箱子 `';B';` 移动到目标位置 `';T';` ：
- 玩家用字符 `';S';` 表示，只要他在地板上，就可以在网格中向上、下、左、右四个方向移动。
- 地板用字符 `';.';` 表示，意味着可以自由行走。
- 墙用字符 `';#';` 表示，意味着障碍物，不能通行。 
- 箱子仅有一个，用字符 `';B';` 表示。相应地，网格上有一个目标位置 `';T';` 。
- 玩家需要站在箱子旁边，然后沿着箱子的方向进行移动，此时箱子会被移动到相邻的地板单元格。记作一次「推动」。
- 玩家无法越过箱子。
返回将箱子推到目标位置的最小 **推动** 次数，如果无法做到，请返回 `-1` 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/16/sample_1_1620.png" style="height: 349px; width: 520px;">** 

```
输入：grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#",".","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：3
解释：我们只需要返回推箱子的次数。
```
 **示例 2：** 

```
输入：grid = [["#","#","#","#","#","#"],
             ["#","T","#","#","#","#"],
             ["#",".",".","B",".","#"],
             ["#","#","#","#",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：-1

```
 **示例 3：** 

```
输入：grid = [["#","#","#","#","#","#"],
             ["#","T",".",".","#","#"],
             ["#",".","#","B",".","#"],
             ["#",".",".",".",".","#"],
             ["#",".",".",".","S","#"],
             ["#","#","#","#","#","#"]]
输出：5
解释：向下、向左、向左、向上再向上。

```
 **示例 4：** 

```
输入：grid = [["#","#","#","#","#","#","#"],
             ["#","S","#",".","B","T","#"],
             ["#","#","#","#","#","#","#"]]
输出：-1

```
 

 **提示：** 
-  `1 <= grid.length <= 20` 
-  `1 <= grid[i].length <= 20` 
-  `grid` 仅包含字符 `';.';` , `';#';` , `';S';` , `';T';` , 以及 `';B';` 。
-  `grid` 中 `';S';` , `';B';` 和 `';T';` 各只能出现一个。
 
**标签**
`广度优先搜索` `数组` `矩阵` `堆（优先队列）` 


## 
```python

```
>
# 1264.页面推荐
[https://leetcode-cn.com/problems/page-recommendations](https://leetcode-cn.com/problems/page-recommendations) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1265.逆序打印不可变链表
[https://leetcode-cn.com/problems/print-immutable-linked-list-in-reverse](https://leetcode-cn.com/problems/print-immutable-linked-list-in-reverse) 
## 原题

 
**标签**
`栈` `递归` `链表` `双指针` 


## 
```python

```
>
# 1266.访问所有点的最小时间
[https://leetcode-cn.com/problems/minimum-time-visiting-all-points](https://leetcode-cn.com/problems/minimum-time-visiting-all-points) 
## 原题
平面上有  `n`  个点，点的位置用整数坐标表示 `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` 。请你计算访问所有这些点需要的 **最小时间** （以秒为单位）。

你需要按照下面的规则在平面上移动：
- 每一秒内，你可以：
	
- 沿水平方向移动一个单位长度，或者
- 沿竖直方向移动一个单位长度，或者
- 跨过对角线移动 `sqrt(2)` 个单位长度（可以看作在一秒内向水平和竖直方向各移动一个单位长度）。
	
	
- 必须按照数组中出现的顺序来访问这些点。
- 在访问某个点时，可以经过该点后面出现的点，但经过的那些点不算作有效访问。
 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/1626_example_1.png" style="height: 428px; width: 500px;" />

```

输入：points = [[1,1],[3,4],[-1,0]]
输出：7
解释：一条最佳的访问路径是： [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
从 [1,1] 到 [3,4] 需要 3 秒 
从 [3,4] 到 [-1,0] 需要 4 秒
一共需要 7 秒
```
 **示例 2：** 

```

输入：points = [[3,2],[-2,2]]
输出：5

```
 

 **提示：** 
-  `points.length == n` 
-  `1 <= n <= 100` 
-  `points[i].length == 2` 
-  `-1000 <= points[i][0], points[i][1] <= 1000` 
 
**标签**
`几何` `数组` `数学` 


## 
```python

```
>
# 1267.统计参与通信的服务器
[https://leetcode-cn.com/problems/count-servers-that-communicate](https://leetcode-cn.com/problems/count-servers-that-communicate) 
## 原题
这里有一幅服务器分布图，服务器的位置标识在 `m * n` 的整数矩阵网格 `grid` 中，1 表示单元格上有服务器，0 表示没有。

如果两台服务器位于同一行或者同一列，我们就认为它们之间可以进行通信。

请你统计并返回能够与至少一台其他服务器进行通信的服务器的数量。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/untitled-diagram-6.jpg" style="height: 203px; width: 202px;">

```
输入：grid = [[1,0],[0,1]]
输出：0
解释：没有一台服务器能与其他服务器进行通信。
```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/untitled-diagram-4-1.jpg" style="height: 203px; width: 203px;">** 

```
输入：grid = [[1,0],[1,1]]
输出：3
解释：所有这些服务器都至少可以与一台别的服务器进行通信。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/11/24/untitled-diagram-1-3.jpg" style="height: 443px; width: 443px;">

```
输入：grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
输出：4
解释：第一行的两台服务器互相通信，第三列的两台服务器互相通信，但右下角的服务器无法与其他服务器通信。

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m <= 250` 
-  `1 <= n <= 250` 
-  `grid[i][j] == 0 or 1` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `计数` `矩阵` 


## 
```python

```
>
# 1268.搜索推荐系统
[https://leetcode-cn.com/problems/search-suggestions-system](https://leetcode-cn.com/problems/search-suggestions-system) 
## 原题
给你一个产品数组 `products` 和一个字符串 `searchWord` ， `products` 数组中每个产品都是一个字符串。

请你设计一个推荐系统，在依次输入单词 `searchWord` 的每一个字母后，推荐 `products` 数组中前缀与 `searchWord` 相同的最多三个产品。如果前缀相同的可推荐产品超过三个，请按字典序返回最小的三个。

请你以二维列表的形式，返回在输入 `searchWord` 每个字母后相应的推荐产品的列表。

 

 **示例 1：** 

```
输入：products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
输出：[
["mobile","moneypot","monitor"],
["mobile","moneypot","monitor"],
["mouse","mousepad"],
["mouse","mousepad"],
["mouse","mousepad"]
]
解释：按字典序排序后的产品列表是 ["mobile","moneypot","monitor","mouse","mousepad"]
输入 m 和 mo，由于所有产品的前缀都相同，所以系统返回字典序最小的三个产品 ["mobile","moneypot","monitor"]
输入 mou， mous 和 mouse 后系统都返回 ["mouse","mousepad"]

```
 **示例 2：** 

```
输入：products = ["havana"], searchWord = "havana"
输出：[["havana"],["havana"],["havana"],["havana"],["havana"],["havana"]]

```
 **示例 3：** 

```
输入：products = ["bags","baggage","banner","box","cloths"], searchWord = "bags"
输出：[["baggage","bags","banner"],["baggage","bags","banner"],["baggage","bags"],["bags"]]

```
 **示例 4：** 

```
输入：products = ["havana"], searchWord = "tatiana"
输出：[[],[],[],[],[],[],[]]

```
 

 **提示：** 
-  `1 <= products.length <= 1000` 
-  `1 <= &Sigma; products[i].length <= 2 * 10^4` 
-  `products[i]` 中所有的字符都是小写英文字母。
-  `1 <= searchWord.length <= 1000` 
-  `searchWord` 中所有字符都是小写英文字母。
 
**标签**
`字典树` `数组` `字符串` 


## 
```python

```
>
# 1269.停在原地的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps](https://leetcode-cn.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps) 
## 原题
有一个长度为  `arrLen`  的数组，开始有一个指针在索引  `0` 处。

每一步操作中，你可以将指针向左或向右移动 1 步，或者停在原地（指针不能被移动到数组范围外）。

给你两个整数  `steps` 和  `arrLen` ，请你计算并返回：在恰好执行  `steps`  次操作以后，指针仍然指向索引  `0` 处的方案数。

由于答案可能会很大，请返回方案数 **模**   `10^9 + 7` 后的结果。

 

 **示例 1：** 

```

输入：steps = 3, arrLen = 2
输出：4
解释：3 步后，总共有 4 种不同的方法可以停在索引 0 处。
向右，向左，不动
不动，向右，向左
向右，不动，向左
不动，不动，不动

```
 **示例  2：** 

```

输入：steps = 2, arrLen = 4
输出：2
解释：2 步后，总共有 2 种不同的方法可以停在索引 0 处。
向右，向左
不动，不动

```
 **示例 3：** 

```

输入：steps = 4, arrLen = 2
输出：8

```
 

 **提示：** 
-  `1 <= steps <= 500` 
-  `1 <= arrLen <= 10^6` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 1270.向公司CEO汇报工作的所有人
[https://leetcode-cn.com/problems/all-people-report-to-the-given-manager](https://leetcode-cn.com/problems/all-people-report-to-the-given-manager) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1271.十六进制魔术数字
[https://leetcode-cn.com/problems/hexspeak](https://leetcode-cn.com/problems/hexspeak) 
## 原题

 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 1272.删除区间
[https://leetcode-cn.com/problems/remove-interval](https://leetcode-cn.com/problems/remove-interval) 
## 原题

 
**标签**
`数组` 


## 
```python

```
>
# 1273.删除树节点
[https://leetcode-cn.com/problems/delete-tree-nodes](https://leetcode-cn.com/problems/delete-tree-nodes) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` 


## 
```python

```
>
# 1274.矩形内船只的数目
[https://leetcode-cn.com/problems/number-of-ships-in-a-rectangle](https://leetcode-cn.com/problems/number-of-ships-in-a-rectangle) 
## 原题

 
**标签**
`数组` `分治` `交互` 


## 
```python

```
>
# 1275.找出井字棋的获胜者
[https://leetcode-cn.com/problems/find-winner-on-a-tic-tac-toe-game](https://leetcode-cn.com/problems/find-winner-on-a-tic-tac-toe-game) 
## 原题
 *A* 和 *B* 在一个 *3* x *3* 的网格上玩井字棋。

井字棋游戏的规则如下：
- 玩家轮流将棋子放在空方格 (" ") 上。
- 第一个玩家 A 总是用 "X" 作为棋子，而第二个玩家 B 总是用 "O" 作为棋子。
- "X" 和 "O" 只能放在空方格中，而不能放在已经被占用的方格上。
- 只要有 3 个相同的（非空）棋子排成一条直线（行、列、对角线）时，游戏结束。
- 如果所有方块都放满棋子（不为空），游戏也会结束。
- 游戏结束后，棋子无法再进行任何移动。
给你一个数组 `moves` ，其中每个元素是大小为 `2` 的另一个数组（元素分别对应网格的行和列），它按照 *A* 和 *B* 的行动顺序（先 *A* 后 *B* ）记录了两人各自的棋子位置。

如果游戏存在获胜者（ *A* 或 *B* ），就返回该游戏的获胜者；如果游戏以平局结束，则返回 "Draw"；如果仍会有行动（游戏未结束），则返回 "Pending"。

你可以假设 `moves` 都 **有效** （遵循井字棋规则），网格最初是空的， *A* 将先行动。

 

 **示例 1：** 

```
输入：moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
输出："A"
解释："A" 获胜，他总是先走。
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"

```
 **示例 2：** 

```
输入：moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
输出："B"
解释："B" 获胜。
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "

```
 **示例 3：** 

```
输入：moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
输出："Draw"
输出：由于没有办法再行动，游戏以平局结束。
"XXO"
"OOX"
"XOX"

```
 **示例 4：** 

```
输入：moves = [[0,0],[1,1]]
输出："Pending"
解释：游戏还没有结束。
"X  "
" O "
"   "

```
 

 **提示：** 
-  `1 <= moves.length <= 9` 
-  `moves[i].length == 2` 
-  `0 <= moves[i][j] <= 2` 
-  `moves` 里没有重复的元素。
-  `moves` 遵循井字棋的规则。
 
**标签**
`数组` `哈希表` `矩阵` `模拟` 


## 
```python

```
>
# 1276.不浪费原料的汉堡制作方案
[https://leetcode-cn.com/problems/number-of-burgers-with-no-waste-of-ingredients](https://leetcode-cn.com/problems/number-of-burgers-with-no-waste-of-ingredients) 
## 原题
圣诞活动预热开始啦，汉堡店推出了全新的汉堡套餐。为了避免浪费原料，请你帮他们制定合适的制作计划。

给你两个整数 `tomatoSlices` 和 `cheeseSlices` ，分别表示番茄片和奶酪片的数目。不同汉堡的原料搭配如下：
-  **巨无霸汉堡：** 4 片番茄和 1 片奶酪
-  **小皇堡：** 2 片番茄和 1 片奶酪
请你以 `[total_jumbo, total_small]` （[巨无霸汉堡总数，小皇堡总数]）的格式返回恰当的制作方案，使得剩下的番茄片 `tomatoSlices` 和奶酪片 `cheeseSlices` 的数量都是 `0` 。

如果无法使剩下的番茄片 `tomatoSlices` 和奶酪片 `cheeseSlices` 的数量为 `0` ，就请返回 `[]` 。

 

 **示例 1：** 

```
输入：tomatoSlices = 16, cheeseSlices = 7
输出：[1,6]
解释：制作 1 个巨无霸汉堡和 6 个小皇堡需要 4*1 + 2*6 = 16 片番茄和 1 + 6 = 7 片奶酪。不会剩下原料。

```
 **示例 2：** 

```
输入：tomatoSlices = 17, cheeseSlices = 4
输出：[]
解释：只制作小皇堡和巨无霸汉堡无法用光全部原料。

```
 **示例 3：** 

```
输入：tomatoSlices = 4, cheeseSlices = 17
输出：[]
解释：制作 1 个巨无霸汉堡会剩下 16 片奶酪，制作 2 个小皇堡会剩下 15 片奶酪。

```
 **示例 4：** 

```
输入：tomatoSlices = 0, cheeseSlices = 0
输出：[0,0]

```
 **示例 5：** 

```
输入：tomatoSlices = 2, cheeseSlices = 1
输出：[0,1]

```
 

 **提示：** 
-  `0 <= tomatoSlices <= 10^7` 
-  `0 <= cheeseSlices <= 10^7` 
 
**标签**
`数学` 


## 
```python

```
>
# 1277.统计全为 1 的正方形子矩阵
[https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones](https://leetcode-cn.com/problems/count-square-submatrices-with-all-ones) 
## 原题
给你一个 `m * n` 的矩阵，矩阵中的元素不是 `0` 就是 `1` ，请你统计并返回其中完全由 `1` 组成的 **正方形** 子矩阵的个数。

 

 **示例 1：** 

```
输入：matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
输出：15
解释： 
边长为 1 的正方形有 10 个。
边长为 2 的正方形有 4 个。
边长为 3 的正方形有 1 个。
正方形的总数 = 10 + 4 + 1 = 15.

```
 **示例 2：** 

```
输入：matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
输出：7
解释：
边长为 1 的正方形有 6 个。 
边长为 2 的正方形有 1 个。
正方形的总数 = 6 + 1 = 7.

```
 

 **提示：** 
-  `1 <= arr.length <= 300` 
-  `1 <= arr[0].length <= 300` 
-  `0 <= arr[i][j] <= 1` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 1278.分割回文串 III
[https://leetcode-cn.com/problems/palindrome-partitioning-iii](https://leetcode-cn.com/problems/palindrome-partitioning-iii) 
## 原题
给你一个由小写字母组成的字符串 `s` ，和一个整数 `k` 。

请你按下面的要求分割字符串：
- 首先，你可以将 `s` 中的部分字符修改为其他的小写英文字母。
- 接着，你需要把 `s` 分割成 `k` 个非空且不相交的子串，并且每个子串都是回文串。
请返回以这种方式分割字符串所需修改的最少字符数。

 

 **示例 1：** 

```
输入：s = "abc", k = 2
输出：1
解释：你可以把字符串分割成 "ab" 和 "c"，并修改 "ab" 中的 1 个字符，将它变成回文串。

```
 **示例 2：** 

```
输入：s = "aabbc", k = 3
输出：0
解释：你可以把字符串分割成 "aa"、"bb" 和 "c"，它们都是回文串。
```
 **示例 3：** 

```
输入：s = "leetcode", k = 8
输出：0

```
 

 **提示：** 
-  `1 <= k <= s.length <= 100` 
-  `s` 中只含有小写英文字母。
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1279.红绿灯路口
[https://leetcode-cn.com/problems/traffic-light-controlled-intersection](https://leetcode-cn.com/problems/traffic-light-controlled-intersection) 
## 原题

 
**标签**
`多线程` 


## 
```python

```
>
# 1280.学生们参加各科测试的次数
[https://leetcode-cn.com/problems/students-and-examinations](https://leetcode-cn.com/problems/students-and-examinations) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1281.整数的各位积和之差
[https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer](https://leetcode-cn.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer) 
## 原题
给你一个整数 `n` ，请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。

 

 **示例 1：** 

```
输入：n = 234
输出：15 
解释：
各位数之积 = 2 * 3 * 4 = 24 
各位数之和 = 2 + 3 + 4 = 9 
结果 = 24 - 9 = 15

```
 **示例 2：** 

```
输入：n = 4421
输出：21
解释： 
各位数之积 = 4 * 4 * 2 * 1 = 32 
各位数之和 = 4 + 4 + 2 + 1 = 11 
结果 = 32 - 11 = 21

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
 
**标签**
`数学` 


## 
```python

```
>
# 1282.用户分组
[https://leetcode-cn.com/problems/group-the-people-given-the-group-size-they-belong-to](https://leetcode-cn.com/problems/group-the-people-given-the-group-size-they-belong-to) 
## 原题
有 `n` 个人被分成数量未知的组。每个人都被标记为一个从 `0` 到 `n - 1` 的 **唯一ID** 。

给定一个整数数组 `groupSizes` ，其中<meta charset="UTF-8" /> `groupSizes[i]` 是第 `i` 个人所在的组的大小。例如，如果 `groupSizes[1] = 3` ，则第 `1` 个人必须位于大小为 `3` 的组中。

返回一个组列表，使每个人 `i` 都在一个大小为<meta charset="UTF-8" /> *`groupSizes[i]`* 的组中。

每个人应该 **恰好只** 出现在 **一个组** 中，并且每个人必须在一个组中。如果有多个答案，返回其中 **任何** 一个。可以 **保证** 给定输入 **至少有一个** 有效的解。

 

 **示例 1：** 

```

输入：groupSizes = [3,3,3,3,3,1,3]
输出：[[5],[0,1,2],[3,4,6]]
解释：
第一组是 [5]，大小为 1，groupSizes[5] = 1。
第二组是 [0,1,2]，大小为 3，groupSizes[0] = groupSizes[1] = groupSizes[2] = 3。
第三组是 [3,4,6]，大小为 3，groupSizes[3] = groupSizes[4] = groupSizes[6] = 3。 
其他可能的解决方案有 [[2,1,6],[5],[0,4,3]] 和 [[5],[0,6,2],[4,3,1]]。

```
 **示例 2：** 

```

输入：groupSizes = [2,1,3,3,3,2]
输出：[[1],[0,5],[2,3,4]]

```
 

 **提示：** 
-  `groupSizes.length == n` 
-  `1 <= n <= 500` 
-  `1 <= groupSizes[i] <= n` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1283.使结果不超过阈值的最小除数
[https://leetcode-cn.com/problems/find-the-smallest-divisor-given-a-threshold](https://leetcode-cn.com/problems/find-the-smallest-divisor-given-a-threshold) 
## 原题
给你一个整数数组 `nums` 和一个正整数 `threshold` ，你需要选择一个正整数作为除数，然后将数组里每个数都除以它，并对除法结果求和。

请你找出能够使上述结果小于等于阈值 `threshold` 的除数中 **最小** 的那个。

每个数除以除数后都向上取整，比方说 7/3 = 3 ， 10/2 = 5 。

题目保证一定有解。

 

 **示例 1：** 

```

输入：nums = [1,2,5,9], threshold = 6
输出：5
解释：如果除数为 1 ，我们可以得到和为 17 （1+2+5+9）。
如果除数为 4 ，我们可以得到和为 7 (1+1+2+3) 。如果除数为 5 ，和为 5 (1+1+1+2)。

```
 **示例 2：** 

```

输入：nums = [2,3,5,7,11], threshold = 11
输出：3

```
 **示例 3：** 

```

输入：nums = [19], threshold = 5
输出：4

```
 

 **提示：** 
-  `1 <= nums.length <= 5 * 10^4` 
-  `1 <= nums[i] <= 10^6` 
-  `nums.length <= threshold <= 10^6` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 1284.转化为全零矩阵的最少反转次数
[https://leetcode-cn.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix](https://leetcode-cn.com/problems/minimum-number-of-flips-to-convert-binary-matrix-to-zero-matrix) 
## 原题
给你一个 `m x n` 的二进制矩阵 `mat` 。每一步，你可以选择一个单元格并将它反转（反转表示 `0` 变 `1` ， `1` 变 `0` ）。如果存在和它相邻的单元格，那么这些相邻的单元格也会被反转。相邻的两个单元格共享同一条边。

请你返回将矩阵 `mat` 转化为全零矩阵的 *最少反转次数* ，如果无法转化为全零矩阵，请返回 `-1` 。

 **二进制矩阵** 的每一个格子要么是 `0` 要么是 `1` 。

 **全零矩阵** 是所有格子都为 `0` 的矩阵。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/13/matrix.png" />

```

输入：mat = [[0,0],[0,1]]
输出：3
解释：一个可能的解是反转 (1, 0)，然后 (0, 1) ，最后是 (1, 1) 。

```
 **示例 2：** 

```

输入：mat = [[0]]
输出：0
解释：给出的矩阵是全零矩阵，所以你不需要改变它。

```
 **示例 3：** 

```

输入：mat = [[1,0,0],[1,0,0]]
输出：-1
解释：该矩阵无法转变成全零矩阵

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat[0].length` 
-  `1 <= m <= 3` 
-  `1 <= n <= 3` 
-  `mat[i][j]` 是 0 或 1 。
 
**标签**
`位运算` `广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 1285.找到连续区间的开始和结束数字
[https://leetcode-cn.com/problems/find-the-start-and-end-number-of-continuous-ranges](https://leetcode-cn.com/problems/find-the-start-and-end-number-of-continuous-ranges) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1286.字母组合迭代器
[https://leetcode-cn.com/problems/iterator-for-combination](https://leetcode-cn.com/problems/iterator-for-combination) 
## 原题
请你设计一个迭代器类，包括以下内容：
- 一个构造函数，输入参数包括：一个 **有序且字符唯一** 的字符串 `characters` （该字符串只包含小写英文字母）和一个数字 `combinationLength` 。
- 函数 *next()* ，按 **字典序** 返回长度为 `combinationLength` 的下一个字母组合。
- 函数 *hasNext()* ，只有存在长度为 `combinationLength` 的下一个字母组合时，才返回 `True` ；否则，返回 `False` 。
 

 **示例：** 

```
CombinationIterator iterator = new CombinationIterator("abc", 2); // 创建迭代器 iterator

iterator.next(); // 返回 "ab"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "ac"
iterator.hasNext(); // 返回 true
iterator.next(); // 返回 "bc"
iterator.hasNext(); // 返回 false

```
 

 **提示：** 
-  `1 <= combinationLength <= characters.length <= 15` 
- 每组测试数据最多包含 `10^4` 次函数调用。
- 题目保证每次调用函数 `next` 时都存在下一个字母组合。
 
**标签**
`设计` `字符串` `回溯` `迭代器` 


## 
```python

```
>
# 1287.有序数组中出现次数超过25%的元素
[https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array](https://leetcode-cn.com/problems/element-appearing-more-than-25-in-sorted-array) 
## 原题
给你一个非递减的 **有序** 整数数组，已知这个数组中恰好有一个整数，它的出现次数超过数组元素总数的 25%。

请你找到并返回这个整数

 

 **示例：** 

```

输入：arr = [1,2,2,6,6,6,6,7,10]
输出：6

```
 

 **提示：** 
-  `1 <= arr.length <= 10^4` 
-  `0 <= arr[i] <= 10^5` 
 
**标签**
`数组` 


## 
```python

```
>
# 1288.删除被覆盖区间
[https://leetcode-cn.com/problems/remove-covered-intervals](https://leetcode-cn.com/problems/remove-covered-intervals) 
## 原题
给你一个区间列表，请你删除列表中被其他区间所覆盖的区间。

只有当 `c <= a` 且 `b <= d` 时，我们才认为区间 `[a,b)` 被区间 `[c,d)` 覆盖。

在完成所有删除操作后，请你返回列表中剩余区间的数目。

 

 **示例：** 

```

输入：intervals = [[1,4],[3,6],[2,8]]
输出：2
解释：区间 [3,6] 被区间 [2,8] 覆盖，所以它被删除了。

```
 

 **提示：** ​​​​​​
-  `1 <= intervals.length <= 1000` 
-  `0 <= intervals[i][0] < intervals[i][1] <= 10^5` 
- 对于所有的 `i != j` ： `intervals[i] != intervals[j]` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 1289.下降路径最小和  II
[https://leetcode-cn.com/problems/minimum-falling-path-sum-ii](https://leetcode-cn.com/problems/minimum-falling-path-sum-ii) 
## 原题
给你一个整数方阵 `arr` ，定义「非零偏移下降路径」为：从 `arr` 数组中的每一行选择一个数字，且按顺序选出来的数字中，相邻数字不在原数组的同一列。

请你返回非零偏移下降路径数字和的最小值。

 

 **示例 1：** 

```

输入：arr = [[1,2,3],[4,5,6],[7,8,9]]
输出：13
解释：
所有非零偏移下降路径包括：
[1,5,9], [1,5,7], [1,6,7], [1,6,8],
[2,4,8], [2,4,9], [2,6,7], [2,6,8],
[3,4,8], [3,4,9], [3,5,7], [3,5,9]
下降路径中数字和最小的是 [1,5,7] ，所以答案是 13 。

```
 

 **提示：** 
-  `1 <= arr.length == arr[i].length <= 200` 
-  `-99 <= arr[i][j] <= 99` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 1290.二进制链表转整数
[https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer](https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer) 
## 原题
给你一个单链表的引用结点 `head` 。链表中每个结点的值不是 0 就是 1。已知此链表是一个整数数字的二进制表示形式。

请你返回该链表所表示数字的 **十进制值** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/15/graph-1.png" style="height: 108px; width: 426px;">

```
输入：head = [1,0,1]
输出：5
解释：二进制数 (101) 转化为十进制数 (5)

```
 **示例 2：** 

```
输入：head = [0]
输出：0

```
 **示例 3：** 

```
输入：head = [1]
输出：1

```
 **示例 4：** 

```
输入：head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
输出：18880

```
 **示例 5：** 

```
输入：head = [0,0]
输出：0

```
 

 **提示：** 
- 链表不为空。
- 链表的结点总数不超过 `30` 。
- 每个结点的值不是 `0` 就是 `1` 。
 
**标签**
`链表` `数学` 


## 
```python

```
>
# 1291.顺次数
[https://leetcode-cn.com/problems/sequential-digits](https://leetcode-cn.com/problems/sequential-digits) 
## 原题
我们定义「顺次数」为：每一位上的数字都比前一位上的数字大 `1` 的整数。

请你返回由 `[low, high]` 范围内所有顺次数组成的 **有序** 列表（从小到大排序）。

 

 **示例 1：** 

```
输出：low = 100, high = 300
输出：[123,234]

```
 **示例 2：** 

```
输出：low = 1000, high = 13000
输出：[1234,2345,3456,4567,5678,6789,12345]

```
 

 **提示：** 
-  `10 <= low <= high <= 10^9` 
 
**标签**
`枚举` 


## 
```python

```
>
# 1292.元素和小于等于阈值的正方形的最大边长
[https://leetcode-cn.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold](https://leetcode-cn.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold) 
## 原题
给你一个大小为  `m x n`  的矩阵  `mat`  和一个整数阈值  `threshold` 。

请你返回元素总和小于或等于阈值的正方形区域的最大边长；如果没有这样的正方形区域，则返回 **0 ** 。<br />
 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/15/e1.png" style="height: 186px; width: 335px;" />

```

输入：mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
输出：2
解释：总和小于或等于 4 的正方形的最大边长为 2，如图所示。

```
 **示例 2：** 

```

输入：mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
输出：0

```
 **示例 3：** 

```

输入：mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
输出：3

```
 **示例 4：** 

```

输入：mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
输出：2

```
 

 **提示：** 
-  `1 <= m, n <= 300` 
-  `m == mat.length` 
-  `n == mat[i].length` 
-  `0 <= mat[i][j] <= 10000` 
-  `0 <= threshold <= 10^5` 
 
**标签**
`数组` `二分查找` `矩阵` `前缀和` 


## 
```python

```
>
# 1293.网格中的最短路径
[https://leetcode-cn.com/problems/shortest-path-in-a-grid-with-obstacles-elimination](https://leetcode-cn.com/problems/shortest-path-in-a-grid-with-obstacles-elimination) 
## 原题
给你一个 `m * n` 的网格，其中每个单元格不是 `0` （空）就是 `1` （障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。

如果您 **最多** 可以消除 `k` 个障碍物，请找出从左上角 `(0, 0)` 到右下角 `(m-1, n-1)` 的最短路径，并返回通过该路径所需的步数。如果找不到这样的路径，则返回 -1。

 

 **示例 1：** 

```
输入： 
grid = 
[[0,0,0],
 [1,1,0],
 [0,0,0],
 [0,1,1],
 [0,0,0]], 
k = 1
输出：6
解释：
不消除任何障碍的最短路径是 10。
消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).

```
 

 **示例 2：** 

```
输入：
grid = 
[[0,1,1],
 [1,1,1],
 [1,0,0]], 
k = 1
输出：-1
解释：
我们至少需要消除两个障碍才能找到这样的路径。

```
 

 **提示：** 
-  `grid.length == m` 
-  `grid[0].length == n` 
-  `1 <= m, n <= 40` 
-  `1 <= k <= m*n` 
-  `grid[i][j] == 0 **or** 1` 
-  `grid[0][0] == grid[m-1][n-1] == 0` 
 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 1294.不同国家的天气类型
[https://leetcode-cn.com/problems/weather-type-in-each-country](https://leetcode-cn.com/problems/weather-type-in-each-country) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1295.统计位数为偶数的数字
[https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits](https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits) 
## 原题
给你一个整数数组 `nums` ，请你返回其中位数为 **偶数** 的数字的个数。

 

 **示例 1：** 

```
输入：nums = [12,345,2,6,7896]
输出：2
解释：
12 是 2 位数字（位数为偶数） 
345 是 3 位数字（位数为奇数）  
2 是 1 位数字（位数为奇数） 
6 是 1 位数字 位数为奇数） 
7896 是 4 位数字（位数为偶数）  
因此只有 12 和 7896 是位数为偶数的数字

```
 **示例 2：** 

```
输入：nums = [555,901,482,1771]
输出：1 
解释： 
只有 1771 是位数为偶数的数字。

```
 

 **提示：** 
-  `1 <= nums.length <= 500` 
-  `1 <= nums[i] <= 10^5` 
 
**标签**
`数组` 


## 
```python

```
>
# 1296.划分数组为连续数字的集合
[https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers](https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers) 
## 原题
给你一个整数数组 `nums` 和一个正整数 `k` ，请你判断是否可以把这个数组划分成一些由 `k` 个连续数字组成的集合。<br />
如果可以，请返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：nums = [1,2,3,3,4,4,5,6], k = 4
输出：true
解释：数组可以分成 [1,2,3,4] 和 [3,4,5,6]。

```
 **示例 2：** 

```

输入：nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
输出：true
解释：数组可以分成 [1,2,3] , [2,3,4] , [3,4,5] 和 [9,10,11]。

```
 **示例 3：** 

```

输入：nums = [3,3,2,2,1,1], k = 3
输出：true

```
 **示例 4：** 

```

输入：nums = [1,2,3,4], k = 3
输出：false
解释：数组不能分成几个大小为 3 的子数组。

```
 

 **提示：** 
-  `1 <= k <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^9` 
 

 **注意：** 此题目与 846 重复：<a href="https://leetcode-cn.com/problems/hand-of-straights/" target="_blank">https://leetcode-cn.com/problems/hand-of-straights/</a>

 
**标签**
`贪心` `数组` `哈希表` `排序` 


## 
```python

```
>
# 1297.子串的最大出现次数
[https://leetcode-cn.com/problems/maximum-number-of-occurrences-of-a-substring](https://leetcode-cn.com/problems/maximum-number-of-occurrences-of-a-substring) 
## 原题
给你一个字符串 `s` ，请你返回满足以下条件且出现次数最大的 **任意** 子串的出现次数：
- 子串中不同字母的数目必须小于等于 `maxLetters` 。
- 子串的长度必须大于等于 `minSize` 且小于等于 `maxSize` 。
 

 **示例 1：** 

```
输入：s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
输出：2
解释：子串 "aab" 在原字符串中出现了 2 次。
它满足所有的要求：2 个不同的字母，长度为 3 （在 minSize 和 maxSize 范围内）。

```
 **示例 2：** 

```
输入：s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
输出：2
解释：子串 "aaa" 在原字符串中出现了 2 次，且它们有重叠部分。

```
 **示例 3：** 

```
输入：s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
输出：3

```
 **示例 4：** 

```
输入：s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
输出：0

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `1 <= maxLetters <= 26` 
-  `1 <= minSize <= maxSize <= min(26, s.length)` 
-  `s` 只包含小写英文字母。
 
**标签**
`哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
# 1298.你能从盒子里获得的最大糖果数
[https://leetcode-cn.com/problems/maximum-candies-you-can-get-from-boxes](https://leetcode-cn.com/problems/maximum-candies-you-can-get-from-boxes) 
## 原题
给你 `n` 个盒子，每个盒子的格式为 `[status, candies, keys, containedBoxes]` ，其中：
- 状态字 `status[i]` ：整数，如果 `box[i]` 是开的，那么是 **1** ，否则是 **0** 。
- 糖果数 `candies[i]` : 整数，表示 `box[i]` 中糖果的数目。
- 钥匙 `keys[i]` ：数组，表示你打开 `box[i]` 后，可以得到一些盒子的钥匙，每个元素分别为该钥匙对应盒子的下标。
- 内含的盒子 `containedBoxes[i]` ：整数，表示放在 `box[i]` 里的盒子所对应的下标。
给你一个 `initialBoxes` 数组，表示你现在得到的盒子，你可以获得里面的糖果，也可以用盒子里的钥匙打开新的盒子，还可以继续探索从这个盒子里找到的其他盒子。

请你按照上述规则，返回可以获得糖果的 **最大数目** 。

 

 **示例 1：** 

```
输入：status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
输出：16
解释：
一开始你有盒子 0 。你将获得它里面的 7 个糖果和盒子 1 和 2。
盒子 1 目前状态是关闭的，而且你还没有对应它的钥匙。所以你将会打开盒子 2 ，并得到里面的 4 个糖果和盒子 1 的钥匙。
在盒子 1 中，你会获得 5 个糖果和盒子 3 ，但是你没法获得盒子 3 的钥匙所以盒子 3 会保持关闭状态。
你总共可以获得的糖果数目 = 7 + 4 + 5 = 16 个。

```
 **示例 2：** 

```
输入：status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
输出：6
解释：
你一开始拥有盒子 0 。打开它你可以找到盒子 1,2,3,4,5 和它们对应的钥匙。
打开这些盒子，你将获得所有盒子的糖果，所以总糖果数为 6 个。

```
 **示例 3：** 

```
输入：status = [1,1,1], candies = [100,1,100], keys = [[],[0,2],[]], containedBoxes = [[],[],[]], initialBoxes = [1]
输出：1

```
 **示例 4：** 

```
输入：status = [1], candies = [100], keys = [[]], containedBoxes = [[]], initialBoxes = []
输出：0

```
 **示例 5：** 

```
输入：status = [1,1,1], candies = [2,3,2], keys = [[],[],[]], containedBoxes = [[],[],[]], initialBoxes = [2,1,0]
输出：7

```
 

 **提示：** 
-  `1 <= status.length <= 1000` 
-  `status.length == candies.length == keys.length == containedBoxes.length == n` 
-  `status[i]` 要么是 `0` 要么是 `1` 。
-  `1 <= candies[i] <= 1000` 
-  `0 <= keys[i].length <= status.length` 
-  `0 <= keys[i][j] < status.length` 
-  `keys[i]` 中的值都是互不相同的。
-  `0 <= containedBoxes[i].length <= status.length` 
-  `0 <= containedBoxes[i][j] < status.length` 
-  `containedBoxes[i]` 中的值都是互不相同的。
- 每个盒子最多被一个盒子包含。
-  `0 <= initialBoxes.length <= status.length` 
-  `0 <= initialBoxes[i] < status.length` 
 
**标签**
`广度优先搜索` `数组` 


## 
```python

```
>
# 1299.将每个元素替换为右侧最大元素
[https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side](https://leetcode-cn.com/problems/replace-elements-with-greatest-element-on-right-side) 
## 原题
给你一个数组  `arr`  ，请你将每个元素用它右边最大的元素替换，如果是最后一个元素，用  `-1` 替换。

完成所有替换操作后，请你返回这个数组。

 

 **示例 1：** 

```

输入：arr = [17,18,5,4,6,1]
输出：[18,6,6,6,1,-1]
解释：
- 下标 0 的元素 --> 右侧最大元素是下标 1 的元素 (18)
- 下标 1 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 2 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 3 的元素 --> 右侧最大元素是下标 4 的元素 (6)
- 下标 4 的元素 --> 右侧最大元素是下标 5 的元素 (1)
- 下标 5 的元素 --> 右侧没有其他元素，替换为 -1

```
 **示例 2：** 

```

输入：arr = [400]
输出：[-1]
解释：下标 0 的元素右侧没有其他元素。

```
 

 **提示：** 
-  `1 <= arr.length <= 10^4` 
-  `1 <= arr[i] <= 10^5` 
 
**标签**
`数组` 


## 
```python

```
>
# 1300.转变数组后最接近目标值的数组和
[https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target](https://leetcode-cn.com/problems/sum-of-mutated-array-closest-to-target) 
## 原题
给你一个整数数组 `arr` 和一个目标值 `target` ，请你返回一个整数 `value` ，使得将数组中所有大于 `value` 的值变成 `value` 后，数组的和最接近 `target` （最接近表示两者之差的绝对值最小）。

如果有多种使得和最接近 `target` 的方案，请你返回这些整数中的最小值。

请注意，答案不一定是 `arr` 中的数字。

 

 **示例 1：** 

```
输入：arr = [4,9,3], target = 10
输出：3
解释：当选择 value 为 3 时，数组会变成 [3, 3, 3]，和为 9 ，这是最接近 target 的方案。

```
 **示例 2：** 

```
输入：arr = [2,3,5], target = 10
输出：5

```
 **示例 3：** 

```
输入：arr = [60864,25176,27249,21296,20204], target = 56803
输出：11361

```
 

 **提示：** 
-  `1 <= arr.length <= 10^4` 
-  `1 <= arr[i], target <= 10^5` 
 
**标签**
`数组` `二分查找` `排序` 


## 
```python

```
>
