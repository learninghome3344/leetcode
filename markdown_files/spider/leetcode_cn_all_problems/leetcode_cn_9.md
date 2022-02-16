# 901.股票价格跨度
[https://leetcode-cn.com/problems/online-stock-span](https://leetcode-cn.com/problems/online-stock-span) 
## 原题
编写一个 `StockSpanner` 类，它收集某些股票的每日报价，并返回该股票当日价格的跨度。

今天股票价格的跨度被定义为股票价格小于或等于今天价格的最大连续日数（从今天开始往回数，包括今天）。

例如，如果未来7天股票的价格是 `[100, 80, 60, 70, 60, 75, 85]` ，那么股票跨度将是 `[1, 1, 1, 2, 1, 4, 6]` 。

 

 **示例：** 

```
输入：["StockSpanner","next","next","next","next","next","next","next"], [[],[100],[80],[60],[70],[60],[75],[85]]
输出：[null,1,1,1,2,1,4,6]
解释：
首先，初始化 S = StockSpanner()，然后：
S.next(100) 被调用并返回 1，
S.next(80) 被调用并返回 1，
S.next(60) 被调用并返回 1，
S.next(70) 被调用并返回 2，
S.next(60) 被调用并返回 1，
S.next(75) 被调用并返回 4，
S.next(85) 被调用并返回 6。

注意 (例如) S.next(75) 返回 4，因为截至今天的最后 4 个价格
(包括今天的价格 75) 小于或等于今天的价格。

```
 

 **提示：** 
- 调用 `StockSpanner.next(int price)` 时，将有 `1 <= price <= 10^5` 。
- 每个测试用例最多可以调用 `10000` 次 `StockSpanner.next` 。
- 在所有测试用例中，最多调用 `150000` 次 `StockSpanner.next` 。
- 此问题的总时间限制减少了 50%。
 
**标签**
`栈` `设计` `数据流` `单调栈` 


## 
```python

```
>
# 902.最大为 N 的数字组合
[https://leetcode-cn.com/problems/numbers-at-most-n-given-digit-set](https://leetcode-cn.com/problems/numbers-at-most-n-given-digit-set) 
## 原题
给定一个按 **非递减顺序** 排列的数字数组<meta charset="UTF-8" /> `digits` 。你可以用任意次数 `digits[i]` 来写的数字。例如，如果<meta charset="UTF-8" /> `digits = ['1','3','5']` ，我们可以写数字，如<meta charset="UTF-8" /> `'13'` , `'551'` , 和 `'1351315'` 。

返回 *可以生成的小于或等于给定整数 `n` 的正整数的个数* 。

 

 **示例 1：** 

```

输入：digits = ["1","3","5","7"], n = 100
输出：20
解释：
可写出的 20 个数字是：
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.

```
 **示例 2：** 

```

输入：digits = ["1","4","9"], n = 1000000000
输出：29523
解释：
我们可以写 3 个一位数字，9 个两位数字，27 个三位数字，
81 个四位数字，243 个五位数字，729 个六位数字，
2187 个七位数字，6561 个八位数字和 19683 个九位数字。
总共，可以使用D中的数字写出 29523 个整数。
```
 **示例 3:** 

```

输入：digits = ["7"], n = 8
输出：1

```
 

 **提示：** 
<meta charset="UTF-8" />
-  `1 <= digits.length <= 9` 
-  `digits[i].length == 1` 
-  `digits[i]` 是从 `'1'` 到 `'9'` 的数
-  `digits` 中的所有值都 **不同** 
-  `digits` 按 **非递减顺序** 排列
-  `1 <= n <= 10^9` 
 
**标签**
`数组` `数学` `二分查找` `动态规划` 


## 
```python

```
>
# 903.DI 序列的有效排列
[https://leetcode-cn.com/problems/valid-permutations-for-di-sequence](https://leetcode-cn.com/problems/valid-permutations-for-di-sequence) 
## 原题
给定一个长度为 `n` 的字符串 `s` ，其中 `s[i]` 是:
-  `“D”` 意味着减少，或者
-  `“I”` 意味着增加
 **有效排列** 是对有 `n + 1` 个在 `[0, n]` 范围内的整数的一个排列 `perm` ，使得对所有的 `i` ：
- 如果 `s[i] == 'D'` ，那么 `perm[i] > perm[i+1]` ，以及；
- 如果 `s[i] == 'I'` ，那么 `perm[i] < perm[i+1]` 。
返回 ***有效排列*** `perm` *的数量* 。因为答案可能很大，所以请 **返回你的答案对** `10^9 + 7` **取余** 。

 

 **示例 1：** 

```

输入：s = "DID"
输出：5
解释：
(0, 1, 2, 3) 的五个有效排列是：
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)

```
 **示例 2:** 

```

输入: s = "D"
输出: 1

```
 

 **提示:** 
-  `n == s.length` 
-  `1 <= n <= 200` 
-  `s[i]` 不是 `'I'` 就是 `'D'` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 904.水果成篮
[https://leetcode-cn.com/problems/fruit-into-baskets](https://leetcode-cn.com/problems/fruit-into-baskets) 
## 原题
你正在探访一家农场，农场从左到右种植了一排果树。这些树用一个整数数组 `fruits` 表示，其中 `fruits[i]` 是第 `i` 棵树上的水果 **种类** 。

你想要尽可能多地收集水果。然而，农场的主人设定了一些严格的规矩，你必须按照要求采摘水果：
- 你只有 **两个** 篮子，并且每个篮子只能装 **单一类型** 的水果。每个篮子能够装的水果总量没有限制。
- 你可以选择任意一棵树开始采摘，你必须从 **每棵** 树（包括开始采摘的树）上 **恰好摘一个水果** 。采摘的水果应当符合篮子中的水果类型。每采摘一次，你将会向右移动到下一棵树，并继续采摘。
- 一旦你走到某棵树前，但水果不符合篮子的水果类型，那么就必须停止采摘。
给你一个整数数组 `fruits` ，返回你可以收集的水果的 **最大** 数目。

 

 **示例 1：** 

```

输入：fruits = [1,2,1]
输出：3
解释：可以采摘全部 3 棵树。

```
 **示例 2：** 

```

输入：fruits = [0,1,2,2]
输出：3
解释：可以采摘 [1,2,2] 这三棵树。
如果从第一棵树开始采摘，则只能采摘 [0,1] 这两棵树。

```
 **示例 3：** 

```

输入：fruits = [1,2,3,2,2]
输出：4
解释：可以采摘 [2,3,2,2] 这四棵树。
如果从第一棵树开始采摘，则只能采摘 [1,2] 这两棵树。

```
 **示例 4：** 

```

输入：fruits = [3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：可以采摘 [1,2,1,1,2] 这五棵树。

```
 

 **提示：** 
-  `1 <= fruits.length <= 10^5` 
-  `0 <= fruits[i] < fruits.length` 
 
**标签**
`数组` `哈希表` `滑动窗口` 


## 
```python

```
>
# 905.按奇偶排序数组
[https://leetcode-cn.com/problems/sort-array-by-parity](https://leetcode-cn.com/problems/sort-array-by-parity) 
## 原题
给定一个非负整数数组 `A` ，返回一个数组，在该数组中， `A` 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。

 

 **示例：** 

```
输入：[3,1,2,4]
输出：[2,4,3,1]
输出 [4,2,3,1]，[2,4,1,3] 和 [4,2,1,3] 也会被接受。

```
 

 **提示：** 
-  `1 <= A.length <= 5000` 
-  `0 <= A[i] <= 5000` 
 
**标签**
`数组` `双指针` `排序` 


## 
```python

```
>
# 906.超级回文数
[https://leetcode-cn.com/problems/super-palindromes](https://leetcode-cn.com/problems/super-palindromes) 
## 原题
如果一个正整数自身是回文数，而且它也是一个回文数的平方，那么我们称这个数为超级回文数。

现在，给定两个正整数 `L` 和 `R` （以字符串形式表示），返回包含在范围 `[L, R]` 中的超级回文数的数目。

 

 **示例：** 

```
输入：L = "4", R = "1000"
输出：4
解释：
4，9，121，以及 484 是超级回文数。
注意 676 不是一个超级回文数： 26 * 26 = 676，但是 26 不是回文数。
```
 

 **提示：** 
-  `1 <= len(L) <= 18` 
-  `1 <= len(R) <= 18` 
-  `L` 和 `R` 是表示 `[1, 10^18)` 范围的整数的字符串。
-  `int(L) <= int(R)` 
 

 
**标签**
`数学` `枚举` 


## 
```python

```
>
# 907.子数组的最小值之和
[https://leetcode-cn.com/problems/sum-of-subarray-minimums](https://leetcode-cn.com/problems/sum-of-subarray-minimums) 
## 原题
给定一个整数数组 `arr` ，找到 `min(b)`  的总和，其中 `b` 的范围为 `arr` 的每个（连续）子数组。

由于答案可能很大，因此 **返回答案模 `10^9 + 7` ** 。

 

 **示例 1：** 

```

输入：arr = [3,1,2,4]
输出：17
解释：
子数组为 [3]，[1]，[2]，[4]，[3,1]，[1,2]，[2,4]，[3,1,2]，[1,2,4]，[3,1,2,4]。 
最小值为 3，1，2，4，1，1，2，1，1，1，和为 17。
```
 **示例 2：** 

```

输入：arr = [11,81,94,43,3]
输出：444

```
 

 **提示：** 
-  `1 <= arr.length <= 3 * 10^4` 
-  `1 <= arr[i] <= 3 * 10^4` 
 

 
**标签**
`栈` `数组` `动态规划` `单调栈` 


## 
```python

```
>
# 908.最小差值 I
[https://leetcode-cn.com/problems/smallest-range-i](https://leetcode-cn.com/problems/smallest-range-i) 
## 原题
给你一个整数数组 `nums` ，和一个整数 `k` 。

在一个操作中，您可以选择 `0 <= i < nums` 的任何索引 `i` 。将 `nums[i]` 改为 `nums[i] + x` ，其中 `x` 是一个范围为 `[-k, k]` 的整数。对于每个索引 `i` ，最多 **只能** 应用 **一次** 此操作。

 `nums` 的 **分数** 是 `nums` 中最大和最小元素的差值。 

 *在对nums中的每个索引最多应用一次上述操作后，返回 `nums` 的最低 **分数*** 。

 

 **示例 1：** 

```

输入：nums = [1], k = 0
输出：0
解释：分数是 max(nums) - min(nums) = 1 - 1 = 0。

```
 **示例 2：** 

```

输入：nums = [0,10], k = 2
输出：6
解释：将 nums 改为 [2,8]。分数是 max(nums) - min(nums) = 8 - 2 = 6。

```
 **示例 3：** 

```

输入：nums = [1,3,6], k = 3
输出：0
解释：将 nums 改为 [4,4,4]。分数是 max(nums) - min(nums) = 4 - 4 = 0。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `0 <= nums[i] <= 10^4` 
-  `0 <= k <= 10^4` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 909.蛇梯棋
[https://leetcode-cn.com/problems/snakes-and-ladders](https://leetcode-cn.com/problems/snakes-and-ladders) 
## 原题
给你一个大小为 `n x n` 的整数矩阵 `board` ，方格按从 `1` 到 `n^2` 编号，编号遵循 <a href="https://baike.baidu.com/item/%E7%89%9B%E8%80%95%E5%BC%8F%E8%BD%AC%E8%A1%8C%E4%B9%A6%E5%86%99%E6%B3%95/17195786">转行交替方式</a> **** ， **从左下角开始** （即，从 `board[n - 1][0]` 开始）每一行交替方向。

玩家从棋盘上的方格 `1` （总是在最后一行、第一列）开始出发。

每一回合，玩家需要从当前方格 `curr` 开始出发，按下述要求前进：
- 选定目标方格 `next` ，目标方格的编号符合范围 `[curr + 1, min(curr + 6, n^2)]` 。

	
- 该选择模拟了掷 **六面体骰子** 的情景，无论棋盘大小如何，玩家最多只能有 6 个目的地。
	
	
- 传送玩家：如果目标方格 `next` 处存在蛇或梯子，那么玩家会传送到蛇或梯子的目的地。否则，玩家传送到目标方格 `next` 。 
- 当玩家到达编号 `n^2` 的方格时，游戏结束。
 `r` 行 `c` 列的棋盘，按前述方法编号，棋盘格中可能存在 “蛇” 或 “梯子”；如果 `board[r][c] != -1` ，那个蛇或梯子的目的地将会是 `board[r][c]` 。编号为 `1` 和 `n^2` 的方格上没有蛇或梯子。

注意，玩家在每回合的前进过程中最多只能爬过蛇或梯子一次：就算目的地是另一条蛇或梯子的起点，玩家也 **不能** 继续移动。
- 举个例子，假设棋盘是 `[[-1,4],[-1,3]]` ，第一次移动，玩家的目标方格是 `2` 。那么这个玩家将会顺着梯子到达方格 `3` ，但 **不能** 顺着方格 `3` 上的梯子前往方格 `4` 。
返回达到编号为 `n^2` 的方格所需的最少移动次数，如果不可能，则返回 `-1` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2018/09/23/snakes.png" style="width: 500px; height: 394px;" />
```

输入：board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
输出：4
解释：
首先，从方格 1 [第 5 行，第 0 列] 开始。 
先决定移动到方格 2 ，并必须爬过梯子移动到到方格 15 。
然后决定移动到方格 17 [第 3 行，第 4 列]，必须爬过蛇到方格 13 。
接着决定移动到方格 14 ，且必须通过梯子移动到方格 35 。 
最后决定移动到方格 36 , 游戏结束。 
可以证明需要至少 4 次移动才能到达最后一个方格，所以答案是 4 。 

```
 **示例 2：** 

```

输入：board = [[-1,-1],[-1,3]]
输出：1

```
 

 **提示：** 
-  `n == board.length == board[i].length` 
-  `2 <= n <= 20` 
-  `grid[i][j]` 的值是 `-1` 或在范围 `[1, n^2]` 内
- 编号为 `1` 和 `n^2` 的方格上没有蛇或梯子
 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 910.最小差值 II
[https://leetcode-cn.com/problems/smallest-range-ii](https://leetcode-cn.com/problems/smallest-range-ii) 
## 原题
给你一个整数数组 `nums` ，和一个整数 `k` 。

对于每个下标 `i` （ `0 <= i < nums.length` ），将 `nums[i]` 变成 **** `nums[i] + k` 或 `nums[i] - k` 。

 `nums` 的 **分数** 是 `nums` 中最大元素和最小元素的差值。

在更改每个下标对应的值之后，返回 `nums` 的最小 **分数** 。

 
 **示例 1：** 

```

输入：nums = [1], k = 0
输出：0
解释：分数 = max(nums) - min(nums) = 1 - 1 = 0 。

```
 **示例 2：** 

```

输入：nums = [0,10], k = 2
输出：6
解释：将数组变为 [2, 8] 。分数 = max(nums) - min(nums) = 8 - 2 = 6 。

```
 **示例 3：** 

```

输入：nums = [1,3,6], k = 3
输出：3
解释：将数组变为 [4, 6, 3] 。分数 = max(nums) - min(nums) = 6 - 3 = 3 。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `0 <= nums[i] <= 10^4` 
-  `0 <= k <= 10^4` 
 
**标签**
`贪心` `数组` `数学` `排序` 


## 
```python

```
>
# 911.在线选举
[https://leetcode-cn.com/problems/online-election](https://leetcode-cn.com/problems/online-election) 
## 原题
给你两个整数数组 `persons` 和 `times` 。在选举中，第 `i` 张票是在时刻为 `times[i]` 时投给候选人 `persons[i]` 的。

对于发生在时刻 `t` 的每个查询，需要找出在 `t` 时刻在选举中领先的候选人的编号。

在 `t` 时刻投出的选票也将被计入我们的查询之中。在平局的情况下，最近获得投票的候选人将会获胜。

实现 `TopVotedCandidate` 类：
-  `TopVotedCandidate(int[] persons, int[] times)` 使用 `persons` 和 `times` 数组初始化对象。
-  `int q(int t)` 根据前面描述的规则，返回在时刻 `t` 在选举中领先的候选人的编号。

 

 **示例：** 

```

输入：
["TopVotedCandidate", "q", "q", "q", "q", "q", "q"]
[[[0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]], [3], [12], [25], [15], [24], [8]]
输出：
[null, 0, 1, 1, 0, 0, 1]

解释：
TopVotedCandidate topVotedCandidate = new TopVotedCandidate([0, 1, 1, 0, 0, 1, 0], [0, 5, 10, 15, 20, 25, 30]);
topVotedCandidate.q(3); // 返回 0 ，在时刻 3 ，票数分布为 [0] ，编号为 0 的候选人领先。
topVotedCandidate.q(12); // 返回 1 ，在时刻 12 ，票数分布为 [0,1,1] ，编号为 1 的候选人领先。
topVotedCandidate.q(25); // 返回 1 ，在时刻 25 ，票数分布为 [0,1,1,0,0,1] ，编号为 1 的候选人领先。（在平局的情况下，1 是最近获得投票的候选人）。
topVotedCandidate.q(15); // 返回 0
topVotedCandidate.q(24); // 返回 0
topVotedCandidate.q(8); // 返回 1

```
 

 **提示：** 
-  `1 <= persons.length <= 5000` 
-  `times.length == persons.length` 
-  `0 <= persons[i] < persons.length` 
-  `0 <= times[i] <= 10^9` 
-  `times` 是一个严格递增的有序数组
-  `times[0] <= t <= 10^9` 
- 每个测试用例最多调用 `10^4` 次 `q` 
 
**标签**
`设计` `数组` `哈希表` `二分查找` 


## 
```python

```
>
# 912.排序数组
[https://leetcode-cn.com/problems/sort-an-array](https://leetcode-cn.com/problems/sort-an-array) 
## 原题
给你一个整数数组 `nums` ，请你将该数组升序排列。

 
 **示例 1：** 

```

输入：nums = [5,2,3,1]
输出：[1,2,3,5]

```
 **示例 2：** 

```

输入：nums = [5,1,1,2,0,0]
输出：[0,0,1,1,2,5]

```
 

 **提示：** 
-  `1 <= nums.length <= 5 * 10^4` 
-  `-5 * 10^4 <= nums[i] <= 5 * 10^4` 
 
**标签**
`数组` `分治` `桶排序` `计数排序` `基数排序` `排序` `堆（优先队列）` `归并排序` 


## 
```python

```
>
# 913.猫和老鼠
[https://leetcode-cn.com/problems/cat-and-mouse](https://leetcode-cn.com/problems/cat-and-mouse) 
## 原题
两位玩家分别扮演猫和老鼠，在一张 **无向** 图上进行游戏，两人轮流行动。

图的形式是： `graph[a]` 是一个列表，由满足 `ab` 是图中的一条边的所有节点 `b` 组成。

老鼠从节点 `1` 开始，第一个出发；猫从节点 `2` 开始，第二个出发。在节点 `0` 处有一个洞。

在每个玩家的行动中，他们 **必须** 沿着图中与所在当前位置连通的一条边移动。例如，如果老鼠在节点 `1` ，那么它必须移动到 `graph[1]` 中的任一节点。

此外，猫无法移动到洞中（节点 `0` ）。

然后，游戏在出现以下三种情形之一时结束：
- 如果猫和老鼠出现在同一个节点，猫获胜。
- 如果老鼠到达洞中，老鼠获胜。
- 如果某一位置重复出现（即，玩家的位置和移动顺序都与上一次行动相同），游戏平局。
给你一张图 `graph` ，并假设两位玩家都都以最佳状态参与游戏：
- 如果老鼠获胜，则返回 `1` ；
- 如果猫获胜，则返回 `2` ；
- 如果平局，则返回 `0` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/cat1.jpg" style="width: 300px; height: 300px;" />
```

输入：graph = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
输出：0

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/17/cat2.jpg" style="width: 200px; height: 200px;" />
```

输入：graph = [[1,3],[0],[3],[0,2]]
输出：1

```
 

 **提示：** 
-  `3 <= graph.length <= 50` 
-  `1 <= graph[i].length < graph.length` 
-  `0 <= graph[i][j] < graph.length` 
-  `graph[i][j] != i` 
-  `graph[i]` 互不相同
- 猫和老鼠在游戏中总是移动
 
**标签**
`广度优先搜索` `图` `记忆化搜索` `数学` `动态规划` `博弈` 


## 
```python

```
>
# 914.卡牌分组
[https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards](https://leetcode-cn.com/problems/x-of-a-kind-in-a-deck-of-cards) 
## 原题
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 `X` ，使我们可以将整副牌按下述规则分成 1 组或更多组：
- 每组都有 `X` 张牌。
- 组内所有的牌上都写着相同的整数。
仅当你可选的 `X >= 2` 时返回 `true` 。

 

 **示例 1：** 

```

输入：deck = [1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

```
 **示例 2：** 

```

输入：deck = [1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。

```
<br />
 **提示：** 
-  `1 <= deck.length <= 10^4` 
-  `0 <= deck[i] < 10^4` 
 
**标签**
`数组` `哈希表` `数学` `计数` `数论` 


## 
```python

```
>
# 915.分割数组
[https://leetcode-cn.com/problems/partition-array-into-disjoint-intervals](https://leetcode-cn.com/problems/partition-array-into-disjoint-intervals) 
## 原题
给定一个数组 `nums` ，将其划分为两个连续子数组 `left` 和 `right` ， 使得：
-  `left` 中的每个元素都小于或等于 `right` 中的每个元素。
-  `left` 和 `right` 都是非空的。
-  `left` 的长度要尽可能小。
 *在完成这样的分组后返回 `left` 的 **长度*** 。

用例可以保证存在这样的划分方法。

 

 **示例 1：** 

```

输入：nums = [5,0,3,8,6]
输出：3
解释：left = [5,0,3]，right = [8,6]

```
 **示例 2：** 

```

输入：nums = [1,1,1,0,6,12]
输出：4
解释：left = [1,1,1,0]，right = [6,12]

```
 

 **提示：** 
-  `2 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^6` 
- 可以保证至少有一种方法能够按题目所描述的那样对 `nums` 进行划分。
 
**标签**
`数组` 


## 
```python

```
>
# 916.单词子集
[https://leetcode-cn.com/problems/word-subsets](https://leetcode-cn.com/problems/word-subsets) 
## 原题
给你两个字符串数组 `words1` 和 `words2` 。

现在，如果 `b` 中的每个字母都出现在 `a` 中， **包括重复出现的字母** ，那么称字符串 `b` 是字符串 `a` 的 **子集** 。
- 例如， `"wrr"` 是 `"warrior"` 的子集，但不是 `"world"` 的子集。
如果对 `words2` 中的每一个单词 `b` ， `b` 都是 `a` 的子集，那么我们称 `words1` 中的单词 `a` 是 **通用单词** 。

以数组形式返回 `words1` 中所有的通用单词。你可以按 **任意顺序** 返回答案。

 
 **示例 1：** 

```

输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","o"]
输出：["facebook","google","leetcode"]

```
 **示例 2：** 

```

输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["l","e"]
输出：["apple","google","leetcode"]

```
 **示例 3：** 

```

输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["e","oo"]
输出：["facebook","google"]

```
 **示例 4：** 

```

输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["lo","eo"]
输出：["google","leetcode"]

```
 **示例 5：** 

```

输入：words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["ec","oc","ceo"]
输出：["facebook","leetcode"]

```
 

 **提示：** 
-  `1 <= words1.length, words2.length <= 10^4` 
-  `1 <= words1[i].length, words2[i].length <= 10` 
-  `words1[i]` 和 `words2[i]` 仅由小写英文字母组成
-  `words1` 中的所有字符串 **互不相同** 
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 917.仅仅反转字母
[https://leetcode-cn.com/problems/reverse-only-letters](https://leetcode-cn.com/problems/reverse-only-letters) 
## 原题
给定一个字符串 `S` ，返回 “反转后的” 字符串，其中不是字母的字符都保留在原地，而所有字母的位置发生反转。

 
 **示例 1：** 

```
输入："ab-cd"
输出："dc-ba"

```
 **示例 2：** 

```
输入："a-bC-dEf-ghIj"
输出："j-Ih-gfE-dCba"

```
 **示例 3：** 

```
输入："Test1ng-Leet=code-Q!"
输出："Qedo1ct-eeLg=ntse-T!"

```
 

 **提示：** 
-  `S.length <= 100` 
-  `33 <= S[i].ASCIIcode <= 122` 
-  `S` 中不包含 `\` or `"` 
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 918.环形子数组的最大和
[https://leetcode-cn.com/problems/maximum-sum-circular-subarray](https://leetcode-cn.com/problems/maximum-sum-circular-subarray) 
## 原题
给定一个长度为 `n` 的 **环形整数数组** `nums` ，返回 *`nums` 的非空 **子数组** 的最大可能和* 。

 **环形数组** 意味着数组的末端将会与开头相连呈环状。形式上， `nums[i]` 的下一个元素是 `nums[(i + 1) % n]` ， `nums[i]` 的前一个元素是 `nums[(i - 1 + n) % n]` 。

 **子数组** 最多只能包含固定缓冲区 `nums` 中的每个元素一次。形式上，对于子数组 `nums[i], nums[i + 1], ..., nums[j]` ，不存在 `i <= k1, k2 <= j` 其中 `k1 % n == k2 % n` 。

 

 **示例 1：** 

```

输入：nums = [1,-2,3,-2]
输出：3
解释：从子数组 [3] 得到最大和 3

```
 **示例 2：** 

```

输入：nums = [5,-3,5]
输出：10
解释：从子数组 [5,5] 得到最大和 5 + 5 = 10

```
 **示例 3：** 

```

输入：nums = [3,-2,2,-3]
输出：3
解释：从子数组 [3] 和 [3,-2,2] 都可以得到最大和 3

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 3 * 10^4` 
-  `-3 * 10^4 <= nums[i] <= 3 * 10^4` ​​​​​​​
 
**标签**
`队列` `数组` `分治` `动态规划` `单调队列` 


## 
```python

```
>
# 919.完全二叉树插入器
[https://leetcode-cn.com/problems/complete-binary-tree-inserter](https://leetcode-cn.com/problems/complete-binary-tree-inserter) 
## 原题
 **完全二叉树** 是每一层（除最后一层外）都是完全填充（即，节点数达到最大）的，并且所有的节点都尽可能地集中在左侧。

设计一种算法，将一个新节点插入到一个完整的二叉树中，并在插入后保持其完整。

实现 `CBTInserter` 类:
-  `CBTInserter(TreeNode root)` 使用头节点为 `root` 的给定树初始化该数据结构；
-  `CBTInserter.insert(int v)` 向树中插入一个值为 `Node.val == val` 的新节点 `TreeNode` 。使树保持完全二叉树的状态， **并返回插入节点** `TreeNode` **的父节点的值** ；
-  `CBTInserter.get_root()` 将返回树的头节点。
 
 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/08/03/lc-treeinsert.jpg" style="height: 143px; width: 500px;" />

```

输入
["CBTInserter", "insert", "insert", "get_root"]
[[[1, 2]], [3], [4], []]
输出
[null, 1, 2, [1, 2, 3, 4]]

解释
CBTInserter cBTInserter = new CBTInserter([1, 2]);
cBTInserter.insert(3);  // 返回 1
cBTInserter.insert(4);  // 返回 2
cBTInserter.get_root(); // 返回 [1, 2, 3, 4]
```
 

 **提示：** 
- 树中节点数量范围为 `[1, 1000]` 
-  `0 <= Node.val <= 5000` 
-  `root` 是完全二叉树
-  `0 <= val <= 5000` 
- 每个测试用例最多调用 `insert` 和 `get_root` 操作 `10^4` 次
 
**标签**
`树` `广度优先搜索` `设计` `二叉树` 


## 
```python

```
>
# 920.播放列表的数量
[https://leetcode-cn.com/problems/number-of-music-playlists](https://leetcode-cn.com/problems/number-of-music-playlists) 
## 原题
你的音乐播放器里有 `N` 首不同的歌，在旅途中，你的旅伴想要听 `L` 首歌（不一定不同，即，允许歌曲重复）。请你为她按如下规则创建一个播放列表：
- 每首歌至少播放一次。
- 一首歌只有在其他 `K` 首歌播放完之后才能再次播放。
返回可以满足要求的播放列表的数量。 **由于答案可能非常大，请返回它模 `10^9 + 7` 的结果。** 

 

 **示例 1：** 

```
输入：N = 3, L = 3, K = 1
输出：6
解释：有 6 种可能的播放列表。[1, 2, 3]，[1, 3, 2]，[2, 1, 3]，[2, 3, 1]，[3, 1, 2]，[3, 2, 1].

```
 **示例 2：** 

```
输入：N = 2, L = 3, K = 0
输出：6
解释：有 6 种可能的播放列表。[1, 1, 2]，[1, 2, 1]，[2, 1, 1]，[2, 2, 1]，[2, 1, 2]，[1, 2, 2]

```
 **示例 3：** 

```
输入：N = 2, L = 3, K = 1
输出：2
解释：有 2 种可能的播放列表。[1, 2, 1]，[2, 1, 2]

```
 

 **提示：** 
-  `0 <= K < N <= L <= 100` 
 
**标签**
`数学` `动态规划` `组合数学` 


## 
```python

```
>
# 921.使括号有效的最少添加
[https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid](https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid) 
## 原题
给定一个由 `';(';` 和 `';)';` 括号组成的字符串 `S` ，我们需要添加最少的括号（ `';(';` 或是 `';)';` ，可以在任何位置），以使得到的括号字符串有效。

从形式上讲，只有满足下面几点之一，括号字符串才是有效的：
- 它是一个空字符串，或者
- 它可以被写成 `AB` （ `A` 与 `B` 连接）, 其中 `A` 和 `B` 都是有效字符串，或者
- 它可以被写作 `(A)` ，其中 `A` 是有效字符串。
给定一个括号字符串，返回为使结果字符串有效而必须添加的最少括号数。

 

 **示例 1：** 

```
输入："())"
输出：1

```
 **示例 2：** 

```
输入："((("
输出：3

```
 **示例 3：** 

```
输入："()"
输出：0

```
 **示例 4：** 

```
输入："()))(("
输出：4
```
 

 **提示：** 
-  `S.length <= 1000` 
-  `S` 只包含 `';(';` 和 `';)';` 字符。
 

 
**标签**
`栈` `贪心` `字符串` 


## 
```python

```
>
# 922.按奇偶排序数组 II
[https://leetcode-cn.com/problems/sort-array-by-parity-ii](https://leetcode-cn.com/problems/sort-array-by-parity-ii) 
## 原题
给定一个非负整数数组 `nums` ， `nums` 中一半整数是 **奇数** ，一半整数是 **偶数** 。

对数组进行排序，以便当 `nums[i]` 为奇数时， `i` 也是 **奇数** ；当 `nums[i]` 为偶数时， `i` 也是 **偶数** 。

你可以返回 *任何满足上述条件的数组作为答案* 。

 

 **示例 1：** 

```

输入：nums = [4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

```
 **示例 2：** 

```

输入：nums = [2,3]
输出：[2,3]

```
 

 **提示：** 
-  `2 <= nums.length <= 2 * 10^4` 
-  `nums.length` 是偶数
-  `nums` 中一半是偶数
-  `0 <= nums[i] <= 1000` 
 

 **进阶：** 可以不使用额外空间解决问题吗？

 
**标签**
`数组` `双指针` `排序` 


## 
```python

```
>
# 923.三数之和的多种可能
[https://leetcode-cn.com/problems/3sum-with-multiplicity](https://leetcode-cn.com/problems/3sum-with-multiplicity) 
## 原题
给定一个整数数组<meta charset="UTF-8" /> `arr` ，以及一个整数 `target` 作为目标值，返回满足 `i < j < k` 且<meta charset="UTF-8" /> `arr[i] + arr[j] + arr[k] == target` 的元组 `i, j, k` 的数量。

由于结果会非常大，请返回 `10^9 + 7` 的模。

 

 **示例 1：** 

```

输入：arr = [1,1,2,2,3,3,4,4,5,5], target = 8
输出：20
解释：
按值枚举(arr[i], arr[j], arr[k])：
(1, 2, 5) 出现 8 次；
(1, 3, 4) 出现 8 次；
(2, 2, 4) 出现 2 次；
(2, 3, 3) 出现 2 次。

```
 **示例 2：** 

```

输入：arr = [1,1,2,2,2,2], target = 5
输出：12
解释：
arr[i] = 1, arr[j] = arr[k] = 2 出现 12 次：
我们从 [1,1] 中选择一个 1，有 2 种情况，
从 [2,2,2,2] 中选出两个 2，有 6 种情况。

```
 

 **提示：** 
-  `3 <= arr.length <= 3000` 
-  `0 <= arr[i] <= 100` 
-  `0 <= target <= 300` 
 
**标签**
`数组` `哈希表` `双指针` `计数` `排序` 


## 
```python

```
>
# 924.尽量减少恶意软件的传播
[https://leetcode-cn.com/problems/minimize-malware-spread](https://leetcode-cn.com/problems/minimize-malware-spread) 
## 原题
给出了一个由 `n` 个节点组成的网络，用 `n × n` 个邻接矩阵图<meta charset="UTF-8" /> `graph` 表示。在节点网络中，当 `graph[i][j] = 1` 时，表示节点 `i` 能够直接连接到另一个节点 `j` 。 

一些节点 `initial` 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。

假设 `M(initial)` 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。

如果从 `initial` 中 **移除某一节点** 能够最小化 `M(initial)` ， 返回该节点。如果有多个节点满足条件，就返回 **索引最小** 的节点。

请注意，如果某个节点已从受感染节点的列表 `initial` 中删除，它以后仍有可能因恶意软件传播而受到感染。

 
 **示例 1：** 

```

输入：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
输出：0

```
 **示例 2：** 

```

输入：graph = [[1,0,0],[0,1,0],[0,0,1]], initial = [0,2]
输出：0

```
 **示例 3：** 

```

输入：graph = [[1,1,1],[1,1,1],[1,1,1]], initial = [1,2]
输出：1

```
 

 **提示：** 
<meta charset="UTF-8" />
-  `n == graph.length` 
-  `n == graph[i].length` 
-  `2 <= n <= 300` 
-  `graph[i][j] == 0` 或 `1` .
-  `graph[i][j] == graph[j][i]` 
-  `graph[i][i] == 1` 
-  `1 <= initial.length <= n` 
-  `0 <= initial[i] <= n - 1` 
-  `initial` 中所有整数均 **不重复** 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` 


## 
```python

```
>
# 925.长按键入
[https://leetcode-cn.com/problems/long-pressed-name](https://leetcode-cn.com/problems/long-pressed-name) 
## 原题
你的朋友正在使用键盘输入他的名字 `name` 。偶尔，在键入字符 `c` 时，按键可能会被 *长按* ，而字符可能被输入 1 次或多次。

你将会检查键盘输入的字符 `typed` 。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 `True` 。

 

 **示例 1：** 

```

输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。

```
 **示例 2：** 

```

输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。

```
 **示例 3：** 

```

输入：name = "leelee", typed = "lleeelee"
输出：true

```
 **示例 4：** 

```

输入：name = "laiden", typed = "laiden"
输出：true
解释：长按名字中的字符并不是必要的。

```
 

 **提示：** 
-  `name.length <= 1000` 
-  `typed.length <= 1000` 
-  `name` 和 `typed` 的字符都是小写字母。
 

 

 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 926.将字符串翻转到单调递增
[https://leetcode-cn.com/problems/flip-string-to-monotone-increasing](https://leetcode-cn.com/problems/flip-string-to-monotone-increasing) 
## 原题
如果一个由 `'0'` 和 `'1'` 组成的字符串，是以一些 `'0'` （可能没有 `'0'` ）后面跟着一些 `'1'` （也可能没有 `'1'` ）的形式组成的，那么该字符串是 *单调递增* 的。

我们给出一个由字符 `'0'` 和 `'1'` 组成的字符串 `S` ，我们可以将任何 `'0'` 翻转为 `'1'` 或者将 `'1'` 翻转为 `'0'` 。

返回使 `S` 单调递增的最小翻转次数。

 

 **示例 1：** 

```

输入：s = "00110"
输出：1
解释：我们翻转最后一位得到 00111.

```
 **示例 2：** 

```

输入：s = "010110"
输出：2
解释：我们翻转得到 011111，或者是 000111。

```
 **示例 3：** 

```

输入：s = "00011000"
输出：2
解释：我们翻转得到 00000000。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `S` 中只包含字符 `'0'` 和 `'1'` 
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 927.三等分
[https://leetcode-cn.com/problems/three-equal-parts](https://leetcode-cn.com/problems/three-equal-parts) 
## 原题
给定一个由 `0` 和 `1` 组成的数组<meta charset="UTF-8" /> `arr` ，将数组分成 **3 个非空的部分** ，使得所有这些部分表示相同的二进制值。

如果可以做到，请返回 **任何** `[i, j]` ，其中 `i+1 < j` ，这样一来：
-  `arr[0], arr[1], ..., arr[i]` 为第一部分；
-  `arr[i + 1], arr[i + 2], ..., arr[j - 1]` 为第二部分；
-  `arr[j], arr[j + 1], ..., arr[arr.length - 1]` 为第三部分。
- 这三个部分所表示的二进制值相等。
如果无法做到，就返回 `[-1, -1]` 。

注意，在考虑每个部分所表示的二进制时，应当将其看作一个整体。例如， `[1,1,0]` 表示十进制中的 `6` ，而不会是 `3` 。此外，前导零也是 **被允许** 的，所以 `[0,1,1]` 和 `[1,1]` 表示相同的值。

 

 **示例 1：** 

```

输入：arr = [1,0,1,0,1]
输出：[0,3]

```
 **示例 2：** 

```

输入：arr = [1,1,0,1,1]
输出：[-1,-1]
```
 **示例 3:** 

```

输入：arr = [1,1,0,0,1]
输出：[0,2]

```
 

 **提示：** 
<meta charset="UTF-8" />
-  `3 <= arr.length <= 3 * 10^4` 
-  `arr[i]` 是 `0` 或 `1` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 928.尽量减少恶意软件的传播 II
[https://leetcode-cn.com/problems/minimize-malware-spread-ii](https://leetcode-cn.com/problems/minimize-malware-spread-ii) 
## 原题
给定一个由 `n` 个节点组成的网络，用 `n x n` 个邻接矩阵 `graph` 表示。在节点网络中，只有当 `graph[i][j] = 1` 时，节点 `i` 能够直接连接到另一个节点 `j` 。

一些节点 `initial` 最初被恶意软件感染。只要两个节点直接连接，且其中至少一个节点受到恶意软件的感染，那么两个节点都将被恶意软件感染。这种恶意软件的传播将继续，直到没有更多的节点可以被这种方式感染。

假设 `M(initial)` 是在恶意软件停止传播之后，整个网络中感染恶意软件的最终节点数。

我们可以从 `initial` 中 **删除一个节点** ， **并完全移除该节点以及从该节点到任何其他节点的任何连接。** 

请返回移除后能够使 `M(initial)` 最小化的节点。如果有多个节点满足条件，返回索引 **最小的节点** 。

 
 **示例 1：** 

```

输出：graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
输入：0

```
 **示例 2：** 

```

输入：graph = [[1,1,0],[1,1,1],[0,1,1]], initial = [0,1]
输出：1

```
 **示例 3：** 

```

输入：graph = [[1,1,0,0],[1,1,1,0],[0,1,1,1],[0,0,1,1]], initial = [0,1]
输出：1

```
 

 **提示：** 
<meta charset="UTF-8" />
-  `n == graph.length` 
-  `n == graph[i].length` 
-  `2 <= n <= 300` 
-  `graph[i][j]` 是 `0` 或 `1` .
-  `graph[i][j] == graph[j][i]` 
-  `graph[i][i] == 1` 
-  `1 <= initial.length < n` 
-  `0 <= initial[i] <= n - 1` 
-  `initial` 中每个整数都 **不同** 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` 


## 
```python

```
>
# 929.独特的电子邮件地址
[https://leetcode-cn.com/problems/unique-email-addresses](https://leetcode-cn.com/problems/unique-email-addresses) 
## 原题
每个 **有效电子邮件地址** 都由一个 **本地名** 和一个 **域名** 组成，以 `'@'` 符号分隔。除小写字母之外，电子邮件地址还可以含有一个或多个 `'.'` 或 `'+'` 。
- 例如，在 `alice@leetcode.com` 中， `alice` 是 **本地名** ，而 `leetcode.com` 是 **域名** 。
如果在电子邮件地址的 **本地名** 部分中的某些字符之间添加句点（ `'.'` ），则发往那里的邮件将会转发到本地名中没有点的同一地址。请注意，此规则 **不适用于域名** 。
- 例如， `"alice.z@leetcode.com”` 和 `“alicez@leetcode.com”` 会转发到同一电子邮件地址。
如果在 **本地名** 中添加加号（ `'+'` ），则会忽略第一个加号后面的所有内容。这允许过滤某些电子邮件。同样，此规则 **不适用于域名** 。
- 例如 `m.y+name@email.com` 将转发到 `my@email.com` 。
可以同时使用这两个规则。

给你一个字符串数组 `emails` ，我们会向每个 `emails[i]` 发送一封电子邮件。返回实际收到邮件的不同地址数目。

 

 **示例 1：** 

```

输入：emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
输出：2
解释：实际收到邮件的是 "testemail@leetcode.com" 和 "testemail@lee.tcode.com"。

```
 **示例 2：** 

```

输入：emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
输出：3

```
<br />
 **提示：** 
-  `1 <= emails.length <= 100` 
-  `1 <= emails[i].length <= 100` 
-  `emails[i]` 由小写英文字母、 `'+'` 、 `'.'` 和 `'@'` 组成
- 每个 `emails[i]` 都包含有且仅有一个 `'@'` 字符
- 所有本地名和域名都不为空
- 本地名不会以 `'+'` 字符作为开头
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 930.和相同的二元子数组
[https://leetcode-cn.com/problems/binary-subarrays-with-sum](https://leetcode-cn.com/problems/binary-subarrays-with-sum) 
## 原题
给你一个二元数组 `nums` ，和一个整数 `goal` ，请你统计并返回有多少个和为 `goal` 的 **非空** 子数组。

 **子数组** 是数组的一段连续部分。

 

 **示例 1：** 

```

输入：nums = [1,0,1,0,1], goal = 2
输出：4
解释：
有 4 个满足题目要求的子数组：[1,0,1]、[1,0,1,0]、[0,1,0,1]、[1,0,1]

```
 **示例 2：** 

```

输入：nums = [0,0,0,0,0], goal = 0
输出：15

```
 

 **提示：** 
-  `1 <= nums.length <= 3 * 10^4` 
-  `nums[i]` 不是 `0` 就是 `1` 
-  `0 <= goal <= nums.length` 
 
**标签**
`数组` `哈希表` `前缀和` `滑动窗口` 


## 
```python

```
>
# 931.下降路径最小和
[https://leetcode-cn.com/problems/minimum-falling-path-sum](https://leetcode-cn.com/problems/minimum-falling-path-sum) 
## 原题
给你一个 `n x n` 的 **方形** 整数数组 `matrix` ，请你找出并返回通过 `matrix` 的 **下降路径** 的 **** **最小和** 。

 **下降路径** 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 `(row, col)` 的下一个元素应当是 `(row + 1, col - 1)` 、 `(row + 1, col)` 或者 `(row + 1, col + 1)` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/failing1-grid.jpg" style="height: 500px; width: 499px;" />

```

输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
输出：13
解释：如图所示，为和最小的两条下降路径

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/failing2-grid.jpg" style="height: 365px; width: 164px;" />

```

输入：matrix = [[-19,57],[-40,-5]]
输出：-59
解释：如图所示，为和最小的下降路径

```
 

 **提示：** 
-  `n == matrix.length == matrix[i].length` 
-  `1 <= n <= 100` 
-  `-100 <= matrix[i][j] <= 100` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 932.漂亮数组
[https://leetcode-cn.com/problems/beautiful-array](https://leetcode-cn.com/problems/beautiful-array) 
## 原题
对于某些固定的 `N` ，如果数组 `A` 是整数 `1, 2, ..., N` 组成的排列，使得：

对于每个 `i < j` ，都 **不存在** `k` 满足 `i < k < j` 使得 `A[k] * 2 = A[i] + A[j]` 。

那么数组 `A` 是漂亮数组。

 

给定 `N` ，返回 **任意** 漂亮数组 `A` （保证存在一个）。

 

 **示例 1：** 

```
输入：4
输出：[2,1,4,3]

```
 **示例 2：** 

```
输入：5
输出：[3,1,2,5,4]
```
 

 **提示：** 
-  `1 <= N <= 1000` 
 

 
**标签**
`数组` `数学` `分治` 


## 
```python

```
>
# 933.最近的请求次数
[https://leetcode-cn.com/problems/number-of-recent-calls](https://leetcode-cn.com/problems/number-of-recent-calls) 
## 原题
写一个 `RecentCounter` 类来计算特定时间范围内最近的请求。

请你实现 `RecentCounter` 类：
-  `RecentCounter()` 初始化计数器，请求数为 0 。
-  `int ping(int t)` 在时间 `t` 添加一个新请求，其中 `t` 表示以毫秒为单位的某个时间，并返回过去 `3000` 毫秒内发生的所有请求数（包括新请求）。确切地说，返回在 `[t-3000, t]` 内发生的请求数。
 **保证** 每次对 `ping` 的调用都使用比之前更大的 `t` 值。

 

 **示例 1：** 

```

输入：
["RecentCounter", "ping", "ping", "ping", "ping"]
[[], [1], [100], [3001], [3002]]
输出：
[null, 1, 2, 3, 3]

解释：
RecentCounter recentCounter = new RecentCounter();
recentCounter.ping(1);     // requests = [1]，范围是 [-2999,1]，返回 1
recentCounter.ping(100);   // requests = [1, 100]，范围是 [-2900,100]，返回 2
recentCounter.ping(3001);  // requests = [1, 100, 3001]，范围是 [1,3001]，返回 3
recentCounter.ping(3002);  // requests = [1, 100, 3001, 3002]，范围是 [2,3002]，返回 3

```
 

 **提示：** 
-  `1 <= t <= 10^9` 
- 保证每次对 `ping` 调用所使用的 `t` 值都 **严格递增** 
- 至多调用 `ping` 方法 `10^4` 次
 
**标签**
`设计` `队列` `数据流` 


## 
```python

```
>
# 934.最短的桥
[https://leetcode-cn.com/problems/shortest-bridge](https://leetcode-cn.com/problems/shortest-bridge) 
## 原题
在给定的二维二进制数组  `A`  中，存在两座岛。（岛是由四面相连的 `1` 形成的一个最大组。）

现在，我们可以将  `0`  变为  `1` ，以使两座岛连接起来，变成一座岛。

返回必须翻转的  `0` 的最小数目。（可以保证答案至少是 `1` 。）

 

 **示例 1：** 

```

输入：A = [[0,1],[1,0]]
输出：1

```
 **示例 2：** 

```

输入：A = [[0,1,0],[0,0,0],[0,0,1]]
输出：2

```
 **示例 3：** 

```

输入：A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
输出：1
```
 

 **提示：** 
-  `2 <= A.length == A[0].length <= 100` 
-  `A[i][j] == 0` 或 `A[i][j] == 1` 
 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 935.骑士拨号器
[https://leetcode-cn.com/problems/knight-dialer](https://leetcode-cn.com/problems/knight-dialer) 
## 原题
象棋骑士有一个 **独特的移动方式** ，它可以垂直移动两个方格，水平移动一个方格，或者水平移动两个方格，垂直移动一个方格(两者都形成一个 **L** 的形状)。

象棋骑士可能的移动方式如下图所示:

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/18/chess.jpg" style="height: 200px; width: 200px;" />

我们有一个象棋骑士和一个电话垫，如下所示，骑士 **只能站在一个数字单元格上** (即蓝色单元格)。

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/18/phone.jpg" style="height: 200px; width: 150px;" />

给定一个整数 n，返回我们可以拨多少个长度为 n 的不同电话号码。

你可以将骑士放置在 **任何数字单元格** 上，然后你应该执行 n - 1 次移动来获得长度为 n 的号码。所有的跳跃应该是 **有效** 的骑士跳跃。

因为答案可能很大， **所以输出答案模** `10^9 + 7` .

 
 **示例 1：** 

```

输入：n = 1
输出：10
解释：我们需要拨一个长度为1的数字，所以把骑士放在10个单元格中的任何一个数字单元格上都能满足条件。

```
 **示例 2：** 

```

输入：n = 2
输出：20
解释：我们可以拨打的所有有效号码为[04, 06, 16, 18, 27, 29, 34, 38, 40, 43, 49, 60, 61, 67, 72, 76, 81, 83, 92, 94]

```
 **示例 3：** 

```

输入：n = 3131
输出：136006598
解释：注意取模

```
 

 **提示：** 
-  `1 <= n <= 5000` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 936.戳印序列
[https://leetcode-cn.com/problems/stamping-the-sequence](https://leetcode-cn.com/problems/stamping-the-sequence) 
## 原题
你想要用 **小写字母** 组成一个目标字符串 `target` 。 

开始的时候，序列由 `target.length` 个 `';?';` 记号组成。而你有一个小写字母印章 `stamp` 。

在每个回合，你可以将印章放在序列上，并将序列中的每个字母替换为印章上的相应字母。你最多可以进行 `10 * target.length` 个回合。

举个例子，如果初始序列为 "?????"，而你的印章 `stamp` 是 `"abc"` ，那么在第一回合，你可以得到 "abc??"、"?abc?"、"??abc"。（请注意，印章必须完全包含在序列的边界内才能盖下去。）

如果可以印出序列，那么返回一个数组，该数组由每个回合中被印下的最左边字母的索引组成。如果不能印出序列，就返回一个空数组。

例如，如果序列是 "ababc"，印章是 `"abc"` ，那么我们就可以返回与操作 "?????" -> "abc??" -> "ababc" 相对应的答案 `[0, 2]` ；

另外，如果可以印出序列，那么需要保证可以在 `10 * target.length` 个回合内完成。任何超过此数字的答案将不被接受。

 

 **示例 1：** 

```
输入：stamp = "abc", target = "ababc"
输出：[0,2]
（[1,0,2] 以及其他一些可能的结果也将作为答案被接受）

```
 **示例 2：** 

```
输入：stamp = "abca", target = "aabcaca"
输出：[3,0,1]

```
 

 **提示：** 
-  `1 <= stamp.length <= target.length <= 1000` 
-  `stamp` 和 `target` 只包含小写字母。
 
**标签**
`栈` `贪心` `队列` `字符串` 


## 
```python

```
>
# 937.重新排列日志文件
[https://leetcode-cn.com/problems/reorder-data-in-log-files](https://leetcode-cn.com/problems/reorder-data-in-log-files) 
## 原题
给你一个日志数组 `logs` 。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的 **标识符** 。

有两种不同类型的日志：
-  **字母日志** ：除标识符之外，所有字均由小写字母组成
-  **数字日志** ：除标识符之外，所有字均由数字组成
请按下述规则将日志重新排序：
- 所有 **字母日志** 都排在 **数字日志** 之前。
-  **字母日志** 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
-  **数字日志** 应该保留原来的相对顺序。
返回日志的最终顺序。

 

 **示例 1：** 

```

输入：logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
输出：["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
解释：
字母日志的内容都不同，所以顺序为 "art can", "art zero", "own kit dig" 。
数字日志保留原来的相对顺序 "dig1 8 1 5 1", "dig2 3 6" 。

```
 **示例 2：** 

```

输入：logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]

```
 

 **提示：** 
-  `1 <= logs.length <= 100` 
-  `3 <= logs[i].length <= 100` 
-  `logs[i]` 中，字与字之间都用 **单个** 空格分隔
- 题目数据保证 `logs[i]` 都有一个标识符，并且在标识符之后至少存在一个字
 
**标签**
`数组` `字符串` `排序` 


## 
```python

```
>
# 938.二叉搜索树的范围和
[https://leetcode-cn.com/problems/range-sum-of-bst](https://leetcode-cn.com/problems/range-sum-of-bst) 
## 原题
给定二叉搜索树的根结点  `root` ，返回值位于范围 *`[low, high]`* 之间的所有结点的值的和。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst1.jpg" style="width: 400px; height: 222px;" />
```

输入：root = [10,5,15,3,7,null,18], low = 7, high = 15
输出：32

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/bst2.jpg" style="width: 400px; height: 335px;" />
```

输入：root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
输出：23

```
 

 **提示：** 
- 树中节点数目在范围 `[1, 2 * 10^4]` 内
-  `1 <= Node.val <= 10^5` 
-  `1 <= low <= high <= 10^5` 
- 所有 `Node.val` **互不相同** 
 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 939.最小面积矩形
[https://leetcode-cn.com/problems/minimum-area-rectangle](https://leetcode-cn.com/problems/minimum-area-rectangle) 
## 原题
给定在 xy 平面上的一组点，确定由这些点组成的矩形的最小面积，其中矩形的边平行于 x 轴和 y 轴。

如果没有任何矩形，就返回 0。

 

 **示例 1：** 

```
输入：[[1,1],[1,3],[3,1],[3,3],[2,2]]
输出：4

```
 **示例 2：** 

```
输入：[[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
输出：2

```
 

 **提示：** 
-  `1 <= points.length <= 500` 
-  `0 <= points[i][0] <= 40000` 
-  `0 <= points[i][1] <= 40000` 
- 所有的点都是不同的。
 
**标签**
`几何` `数组` `哈希表` `数学` `排序` 


## 
```python

```
>
# 940.不同的子序列 II
[https://leetcode-cn.com/problems/distinct-subsequences-ii](https://leetcode-cn.com/problems/distinct-subsequences-ii) 
## 原题
给定一个字符串 `s` ，计算 `s` 的 **不同非空子序列** 的个数。因为结果可能很大，所以返回答案需要对 **** ** `10^9 + 7` 取余** 。

字符串的 **子序列** 是经由原字符串删除一些（也可能不删除）字符但不改变剩余字符相对位置的一个新字符串。
- 例如， `"ace"` 是 `" ***a*** b ***c*** d ***e*** "` 的一个子序列，但 `"aec"` 不是。
 

 **示例 1：** 

```

输入：s = "abc"
输出：7
解释：7 个不同的子序列分别是 "a", "b", "c", "ab", "ac", "bc", 以及 "abc"。

```
 **示例 2：** 

```

输入：s = "aba"
输出：6
解释：6 个不同的子序列分别是 "a", "b", "ab", "ba", "aa" 以及 "aba"。

```
 **示例 3：** 

```

输入：s = "aaa"
输出：3
解释：3 个不同的子序列分别是 "a", "aa" 以及 "aaa"。

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
# 941.有效的山脉数组
[https://leetcode-cn.com/problems/valid-mountain-array](https://leetcode-cn.com/problems/valid-mountain-array) 
## 原题
给定一个整数数组 `arr` ，如果它是有效的山脉数组就返回 `true` ，否则返回 `false` 。

让我们回顾一下，如果 `arr` 满足下述条件，那么它是一个山脉数组：
-  `arr.length >= 3` 
- 在 `0 < i < arr.length - 1` 条件下，存在 `i` 使得：
	
-  `arr[0] < arr[1] < ... arr[i-1] < arr[i]` 
-  `arr[i] > arr[i+1] > ... > arr[arr.length - 1]` 
	
	
 

<img alt="" src="https://assets.leetcode.com/uploads/2019/10/20/hint_valid_mountain_array.png" style="height: 316px; width: 500px;" />

 

 **示例 1：** 

```

输入：arr = [2,1]
输出：false

```
 **示例 2：** 

```

输入：arr = [3,5,5]
输出：false

```
 **示例 3：** 

```

输入：arr = [0,3,2,1]
输出：true
```
 

 **提示：** 
-  `1 <= arr.length <= 10^4` 
-  `0 <= arr[i] <= 10^4` 
 
**标签**
`数组` 


## 
```python

```
>
# 942.增减字符串匹配
[https://leetcode-cn.com/problems/di-string-match](https://leetcode-cn.com/problems/di-string-match) 
## 原题
由范围 `[0,n]` 内所有整数组成的 `n + 1` 个整数的排列序列可以表示为长度为 `n` 的字符串 `s` ，其中:
- 如果 `perm[i] < perm[i + 1]` ，那么 `s[i] == 'I'` 
- 如果 `perm[i] > perm[i + 1]` ，那么 `s[i] == 'D'` 
给定一个字符串 `s` ，重构排列 `perm` 并返回它。如果有多个有效排列perm，则返回其中 **任何一个** 。

 

 **示例 1：** 

```

输入：s = "IDID"
输出：[0,4,1,3,2]

```
 **示例 2：** 

```

输入：s = "III"
输出：[0,1,2,3]

```
 **示例 3：** 

```

输入：s = "DDI"
输出：[3,2,0,1]
```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `<font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">s</span></span></font></font>` 只包含字符 `"I"` 或 `"D"` 
 
**标签**
`贪心` `数组` `数学` `双指针` `字符串` 


## 
```python

```
>
# 943.最短超级串
[https://leetcode-cn.com/problems/find-the-shortest-superstring](https://leetcode-cn.com/problems/find-the-shortest-superstring) 
## 原题
给定一个字符串数组 `words` ，找到以 `words` 中每个字符串作为子字符串的最短字符串。如果有多个有效最短字符串满足题目条件，返回其中 **任意一个** 即可。

我们可以假设 `words` 中没有字符串是 `words` 中另一个字符串的子字符串。

 

 **示例 1：** 

```

输入：words = ["alex","loves","leetcode"]
输出："alexlovesleetcode"
解释："alex"，"loves"，"leetcode" 的所有排列都会被接受。
```
 **示例 2：** 

```

输入：words = ["catg","ctaagt","gcta","ttca","atgcatc"]
输出："gctaagttcatgcatc"
```
 

 **提示：** 
-  `1 <= words.length <= 12` 
-  `1 <= words[i].length <= 20` 
-  `words[i]` 由小写英文字母组成
-  `words` 中的所有字符串 **互不相同** 
 
**标签**
`位运算` `数组` `字符串` `动态规划` `状态压缩` 


## 
```python

```
>
# 944.删列造序
[https://leetcode-cn.com/problems/delete-columns-to-make-sorted](https://leetcode-cn.com/problems/delete-columns-to-make-sorted) 
## 原题
给你由 `n` 个小写字母字符串组成的数组 `strs` ，其中每个字符串长度相等。

这些字符串可以每个一行，排成一个网格。例如， `strs = ["abc", "bce", "cae"]` 可以排列为：

```

abc
bce
cae
```
你需要找出并删除 **不是按字典序升序排列的** 列。在上面的例子（下标从 0 开始）中，列 0（ `'a'` , `'b'` , `'c'` ）和列 2（ `'c'` , `'e'` , `'e'` ）都是按升序排列的，而列 1（ `'b'` , `'c'` , `'a'` ）不是，所以要删除列 1 。

返回你需要删除的列数。

 

 **示例 1：** 

```

输入：strs = ["cba","daf","ghi"]
输出：1
解释：网格示意如下：
  cba
  daf
  ghi
列 0 和列 2 按升序排列，但列 1 不是，所以只需要删除列 1 。

```
 **示例 2：** 

```

输入：strs = ["a","b"]
输出：0
解释：网格示意如下：
  a
  b
只有列 0 这一列，且已经按升序排列，所以不用删除任何列。

```
 **示例 3：** 

```

输入：strs = ["zyx","wvu","tsr"]
输出：3
解释：网格示意如下：
  zyx
  wvu
  tsr
所有 3 列都是非升序排列的，所以都要删除。

```
 

 **提示：** 
-  `n == strs.length` 
-  `1 <= n <= 100` 
-  `1 <= strs[i].length <= 1000` 
-  `strs[i]` 由小写英文字母组成
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 945.使数组唯一的最小增量
[https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique](https://leetcode-cn.com/problems/minimum-increment-to-make-array-unique) 
## 原题
给你一个整数数组 `nums` 。每次 move 操作将会选择任意一个满足 `0 <= i < nums.length` 的下标 `i` ，并将 `nums[i]` 递增 `1` 。

返回使 `nums` 中的每个值都变成唯一的所需要的最少操作次数。
 

 **示例 1：** 

```

输入：nums = [1,2,2]
输出：1
解释：经过一次 move 操作，数组将变为 [1, 2, 3]。

```
 **示例 2：** 

```

输入：nums = [3,2,1,2,1,7]
输出：6
解释：经过 6 次 move 操作，数组将变为 [3, 4, 1, 2, 5, 7]。
可以看出 5 次或 5 次以下的 move 操作是不能让数组的每个值唯一的。
```
 
 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^5` 
 
**标签**
`贪心` `数组` `计数` `排序` 


## 
```python

```
>
# 946.验证栈序列
[https://leetcode-cn.com/problems/validate-stack-sequences](https://leetcode-cn.com/problems/validate-stack-sequences) 
## 原题
给定 `pushed` 和 `popped` 两个序列，每个序列中的 **值都不重复** ，只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
输出：true
解释：我们可以按以下顺序执行：
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

```
 **示例 2：** 

```

输入：pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
输出：false
解释：1 不能在 2 之前弹出。

```
 

 **提示：** 
-  `1 <= pushed.length <= 1000` 
-  `0 <= pushed[i] <= 1000` 
-  `pushed` 的所有元素 **互不相同** 
-  `popped.length == pushed.length` 
-  `popped` 是 `pushed` 的一个排列
 
**标签**
`栈` `数组` `模拟` 


## 
```python

```
>
# 947.移除最多的同行或同列石头
[https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column](https://leetcode-cn.com/problems/most-stones-removed-with-same-row-or-column) 
## 原题
 `n` 块石头放置在二维平面中的一些整数坐标点上。每个坐标点上最多只能有一块石头。

如果一块石头的 **同行或者同列** 上有其他石头存在，那么就可以移除这块石头。

给你一个长度为 `n` 的数组 `stones` ，其中 `stones[i] = [x<sub>i</sub>, y<sub>i</sub>]` 表示第 `i` 块石头的位置，返回 **可以移除的石子** 的最大数量。

 

 **示例 1：** 

```

输入：stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
输出：5
解释：一种移除 5 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,1] 同行。
2. 移除石头 [2,1] ，因为它和 [0,1] 同列。
3. 移除石头 [1,2] ，因为它和 [1,0] 同行。
4. 移除石头 [1,0] ，因为它和 [0,0] 同列。
5. 移除石头 [0,1] ，因为它和 [0,0] 同行。
石头 [0,0] 不能移除，因为它没有与另一块石头同行/列。
```
 **示例 2：** 

```

输入：stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
输出：3
解释：一种移除 3 块石头的方法如下所示：
1. 移除石头 [2,2] ，因为它和 [2,0] 同行。
2. 移除石头 [2,0] ，因为它和 [0,0] 同列。
3. 移除石头 [0,2] ，因为它和 [0,0] 同行。
石头 [0,0] 和 [1,1] 不能移除，因为它们没有与另一块石头同行/列。
```
 **示例 3：** 

```

输入：stones = [[0,0]]
输出：0
解释：[0,0] 是平面上唯一一块石头，所以不可以移除它。
```
 

 **提示：** 
-  `1 <= stones.length <= 1000` 
-  `0 <= x<sub>i</sub>, y<sub>i</sub> <= 10^4` 
- 不会有两块石头放在同一个坐标点上
 
**标签**
`深度优先搜索` `并查集` `图` 


## 
```python

```
>
# 948.令牌放置
[https://leetcode-cn.com/problems/bag-of-tokens](https://leetcode-cn.com/problems/bag-of-tokens) 
## 原题
你的初始 **能量** 为  `P` ，初始 **分数** 为  `0` ，只有一包令牌 `tokens` 。其中 `tokens[i]` 是第 `i` 个令牌的值（下标从 0 开始）。

令牌可能的两种使用方法如下：
- 如果你至少有  `token[i]`  点 **能量** ，可以将令牌 `i` 置为正面朝上，失去  `token[i]`  点 **能量** ，并得到  `1`   **分** 。
- 如果我们至少有  `1`   **分** ，可以将令牌 `i` 置为反面朝上，获得  `token[i]` 点 **能量** ，并失去  `1`   **分** 。
每个令牌 **最多** 只能使用一次，使用 **顺序不限** ， **不需** 使用所有令牌。

在使用任意数量的令牌后，返回我们可以得到的最大 **分数** 。

 
 **示例 1：** 

```

输入：tokens = [100], P = 50
输出：0
解释：无法使用唯一的令牌，因为能量和分数都太少了。
```
 **示例 2：** 

```

输入：tokens = [100,200], P = 150
输出：1
解释：令牌 0 正面朝上，能量变为 50，分数变为 1 。不必使用令牌 1 ，因为你无法使用它来提高分数。
```
 **示例 3：** 

```

输入：tokens = [100,200,300,400], P = 200
输出：2
解释：按下面顺序使用令牌可以得到 2 分：
1. 令牌 0 正面朝上，能量变为 100 ，分数变为 1
2. 令牌 3 正面朝下，能量变为 500 ，分数变为 0
3. 令牌 1 正面朝上，能量变为 300 ，分数变为 1
4. 令牌 2 正面朝上，能量变为 0 ，分数变为 2
```
 

 **提示：** 
-  `0 <= tokens.length <= 1000` 
-  `0 <= tokens[i], P < 10^4` 
 
**标签**
`贪心` `数组` `双指针` `排序` 


## 
```python

```
>
# 949.给定数字能组成的最大时间
[https://leetcode-cn.com/problems/largest-time-for-given-digits](https://leetcode-cn.com/problems/largest-time-for-given-digits) 
## 原题
给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。

24 小时格式为 `"HH:MM"` ，其中 `HH` 在 `00` 到 `23` 之间， `MM` 在 `00` 到 `59` 之间。最小的 24 小时制时间是  `00:00` ，而最大的是  `23:59` 。从 00:00 （午夜）开始算起，过得越久，时间越大。

以长度为 5 的字符串，按 `"HH:MM"` 格式返回答案。如果不能确定有效时间，则返回空字符串。

 

 **示例 1：** 

```

输入：arr = [1,2,3,4]
输出："23:41"
解释：有效的 24 小时制时间是 "12:34"，"12:43"，"13:24"，"13:42"，"14:23"，"14:32"，"21:34"，"21:43"，"23:14" 和 "23:41" 。这些时间中，"23:41" 是最大时间。

```
 **示例 2：** 

```

输入：arr = [5,5,5,5]
输出：""
解释：不存在有效的 24 小时制时间，因为 "55:55" 无效。

```
 **示例 3：** 

```

输入：arr = [0,0,0,0]
输出："00:00"

```
 **示例 4：** 

```

输入：arr = [0,0,1,0]
输出："10:00"

```
 

 **提示：** 
-  `arr.length == 4` 
-  `0 <= arr[i] <= 9` 
 
**标签**
`字符串` `枚举` 


## 
```python

```
>
# 950.按递增顺序显示卡牌
[https://leetcode-cn.com/problems/reveal-cards-in-increasing-order](https://leetcode-cn.com/problems/reveal-cards-in-increasing-order) 
## 原题
牌组中的每张卡牌都对应有一个唯一的整数。你可以按你想要的顺序对这套卡片进行排序。

最初，这些卡牌在牌组里是正面朝下的（即，未显示状态）。

现在，重复执行以下步骤，直到显示所有卡牌为止：
- 从牌组顶部抽一张牌，显示它，然后将其从牌组中移出。
- 如果牌组中仍有牌，则将下一张处于牌组顶部的牌放在牌组的底部。
- 如果仍有未显示的牌，那么返回步骤 1。否则，停止行动。
返回能以 **递增顺序** 显示卡牌的牌组顺序。

答案中的第一张牌被认为处于牌堆顶部。

 

 **示例：** 

```
输入：[17,13,11,2,3,5,7]
输出：[2,13,3,11,5,17,7]
解释：
我们得到的牌组顺序为 [17,13,11,2,3,5,7]（这个顺序不重要），然后将其重新排序。
重新排序后，牌组以 [2,13,3,11,5,17,7] 开始，其中 2 位于牌组的顶部。
我们显示 2，然后将 13 移到底部。牌组现在是 [3,11,5,17,7,13]。
我们显示 3，并将 11 移到底部。牌组现在是 [5,17,7,13,11]。
我们显示 5，然后将 17 移到底部。牌组现在是 [7,13,11,17]。
我们显示 7，并将 13 移到底部。牌组现在是 [11,17,13]。
我们显示 11，然后将 17 移到底部。牌组现在是 [13,17]。
我们展示 13，然后将 17 移到底部。牌组现在是 [17]。
我们显示 17。
由于所有卡片都是按递增顺序排列显示的，所以答案是正确的。

```
 

 **提示：** 
-  `1 <= A.length <= 1000` 
-  `1 <= A[i] <= 10^6` 
- 对于所有的 `i != j` ， `A[i] != A[j]` 
 
**标签**
`队列` `数组` `排序` `模拟` 


## 
```python

```
>
# 951.翻转等价二叉树
[https://leetcode-cn.com/problems/flip-equivalent-binary-trees](https://leetcode-cn.com/problems/flip-equivalent-binary-trees) 
## 原题
我们可以为二叉树 **T** 定义一个 **翻转操作** ，如下所示：选择任意节点，然后交换它的左子树和右子树。

只要经过一定次数的翻转操作后，能使 **X** 等于 **Y** ，我们就称二叉树 **X** *翻转 等价* 于二叉树 **Y** 。

这些树由根节点 `root1` 和 `root2` 给出。如果两个二叉树是否是 *翻转 等价* 的函数，则返回 `true` ，否则返回 `false` 。

 

 **示例 1：** 

<img alt="Flipped Trees Diagram" src="https://assets.leetcode.com/uploads/2018/11/29/tree_ex.png" />

```

输入：root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 = [1,3,2,null,6,4,5,null,null,null,null,8,7]
输出：true
解释：我们翻转值为 1，3 以及 5 的三个节点。

```
 **示例 2:** 

```

输入: root1 = [], root2 = []
输出: true

```
 **示例 3:** 

```

输入: root1 = [], root2 = [1]
输出: false

```
 

 **提示：** 
- 每棵树节点数在 `[0, 100]` 范围内
- 每棵树中的每个值都是唯一的、在 `[0, 99]` 范围内的整数
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 952.按公因数计算最大组件大小
[https://leetcode-cn.com/problems/largest-component-size-by-common-factor](https://leetcode-cn.com/problems/largest-component-size-by-common-factor) 
## 原题
给定一个由不同正整数的组成的非空数组 `nums` ，考虑下面的图：
- 有 `nums.length` 个节点，按从 `nums[0]` 到 `nums[nums.length - 1]` 标记；
- 只有当 `nums[i]` 和 `nums[j]` 共用一个大于 1 的公因数时， `nums[i]` 和 `nums[j]` 之间才有一条边。
返回 *图中最大连通组件的大小* 。

 
 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2018/12/01/ex1.png" style="height: 97px; width: 500px;" />

```

输入：nums = [4,6,15,35]
输出：4

```
 **示例 2：** 

<img src="https://assets.leetcode.com/uploads/2018/12/01/ex2.png" style="height: 85px; width: 500px;" />

```

输入：nums = [20,50,9,63]
输出：2

```
 **示例 3：** 

<img src="https://assets.leetcode.com/uploads/2018/12/01/ex3.png" style="height: 260px; width: 500px;" />

```

输入：nums = [2,3,6,7,4,12,21,39]
输出：8

```
 

 **提示：** 
-  `1 <= nums.length <= 2 * 10^4` 
-  `1 <= nums[i] <= 10^5` 
-  `nums` 中所有值都 **不同** 
 
**标签**
`并查集` `数组` `数学` 


## 
```python

```
>
# 953.验证外星语词典
[https://leetcode-cn.com/problems/verifying-an-alien-dictionary](https://leetcode-cn.com/problems/verifying-an-alien-dictionary) 
## 原题
某种外星语也使用英文小写字母，但可能顺序 `order` 不同。字母表的顺序（ `order` ）是一些小写字母的排列。

给定一组用外星语书写的单词 `words` ，以及其字母表的顺序 `order` ，只有当给定的单词在这种外星语中按字典序排列时，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true
解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
```
 **示例 2：** 

```

输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
输出：false
解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。
```
 **示例 3：** 

```

输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
输出：false
解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（<a href="https://baike.baidu.com/item/%E5%AD%97%E5%85%B8%E5%BA%8F" target="_blank">更多信息）。

```
 

 **提示：** 
-  `1 <= words.length <= 100` 
-  `1 <= words[i].length <= 20` 
-  `order.length == 26` 
- 在  `words[i]`  和  `order`  中的所有字符都是英文小写字母。
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 954.二倍数对数组
[https://leetcode-cn.com/problems/array-of-doubled-pairs](https://leetcode-cn.com/problems/array-of-doubled-pairs) 
## 原题
给定一个长度为偶数的整数数组 `arr` ，只有对 `arr` 进行重组后可以满足 “对于每个 `0 <= i < len(arr) / 2` ，都有 `arr[2 * i + 1] = 2 * arr[2 * i]` ” 时，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：arr = [3,1,3,6]
输出：false

```
 **示例 2：** 

```

输入：arr = [2,1,2,6]
输出：false

```
 **示例 3：** 

```

输入：arr = [4,-2,2,-4]
输出：true
解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]

```
 **示例 4：** 

```

输入：arr = [1,2,4,16,8,4]
输出：false

```
 

 **提示：** 
-  `0 <= arr.length <= 3 * 10^4` 
-  `arr.length` 是偶数
-  `-10^5 <= arr[i] <= 10^5` 
 
**标签**
`贪心` `数组` `哈希表` `排序` 


## 
```python

```
>
# 955.删列造序 II
[https://leetcode-cn.com/problems/delete-columns-to-make-sorted-ii](https://leetcode-cn.com/problems/delete-columns-to-make-sorted-ii) 
## 原题
给定由 `n` 个字符串组成的数组 `strs` ，其中每个字符串长度相等。

选取一个删除索引序列，对于 `strs` 中的每个字符串，删除对应每个索引处的字符。

比如，有 `strs = ["abcdef", "uvwxyz"]` ，删除索引序列  `{0, 2, 3}` ，删除后 `strs` 为 `["bef", "vyz"]` 。

假设，我们选择了一组删除索引 `answer` ，那么在执行删除操作之后，最终得到的数组的元素是按 **字典序** （ `strs[0] <= strs[1] <= strs[2] ... <= strs[n - 1]` ）排列的，然后请你返回 `answer.length`  的最小可能值。

 
 **示例 1：** 

```

输入：strs = ["ca","bb","ac"]
输出：1
解释： 
删除第一列后，strs = ["a", "b", "c"]。
现在 strs 中元素是按字典排列的 (即，strs[0] <= strs[1] <= strs[2])。
我们至少需要进行 1 次删除，因为最初 strs 不是按字典序排列的，所以答案是 1。

```
 **示例 2：** 

```

输入：strs = ["xc","yb","za"]
输出：0
解释：
strs 的列已经是按字典序排列了，所以我们不需要删除任何东西。
注意 strs 的行不需要按字典序排列。
也就是说，strs[0][0] <= strs[0][1] <= ... 不一定成立。

```
 **示例 3：** 

```

输入：strs = ["zyx","wvu","tsr"]
输出：3
解释：
我们必须删掉每一列。

```
 

 **提示：** 
-  `n == strs.length` 
-  `1 <= n <= 100` 
-  `1 <= strs[i].length <= 100` 
-  `strs[i]` 由小写英文字母组成
 
**标签**
`贪心` `数组` `字符串` 


## 
```python

```
>
# 956.最高的广告牌
[https://leetcode-cn.com/problems/tallest-billboard](https://leetcode-cn.com/problems/tallest-billboard) 
## 原题
你正在安装一个广告牌，并希望它高度最大。这块广告牌将有两个钢制支架，两边各一个。每个钢支架的高度必须相等。

你有一堆可以焊接在一起的钢筋 `rods` 。举个例子，如果钢筋的长度为 `1` 、 `2` 和 `3` ，则可以将它们焊接在一起形成长度为 `6` 的支架。

返回 *广告牌的最大可能安装高度* 。如果没法安装广告牌，请返回 `0` 。

 

 **示例 1：** 

```

输入：[1,2,3,6]
输出：6
解释：我们有两个不相交的子集 {1,2,3} 和 {6}，它们具有相同的和 sum = 6。

```
 **示例 2：** 

```

输入：[1,2,3,4,5,6]
输出：10
解释：我们有两个不相交的子集 {2,3,5} 和 {4,6}，它们具有相同的和 sum = 10。
```
 **示例 3：** 

```

输入：[1,2]
输出：0
解释：没法安装广告牌，所以返回 0。
```
 

 **提示：** 
-  `0 <= rods.length <= 20` 
-  `1 <= rods[i] <= 1000` 
-  `sum(rods[i]) <= 5000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 957.N 天后的牢房
[https://leetcode-cn.com/problems/prison-cells-after-n-days](https://leetcode-cn.com/problems/prison-cells-after-n-days) 
## 原题
8 间牢房排成一排，每间牢房不是有人住就是空着。

每天，无论牢房是被占用或空置，都会根据以下规则进行更改：
- 如果一间牢房的两个相邻的房间都被占用或都是空的，那么该牢房就会被占用。
- 否则，它就会被空置。
（请注意，由于监狱中的牢房排成一行，所以行中的第一个和最后一个房间无法有两个相邻的房间。）

我们用以下方式描述监狱的当前状态：如果第 `i` 间牢房被占用，则 `cell[i]==1` ，否则 `cell[i]==0` 。

根据监狱的初始状态，在 `N` 天后返回监狱的状况（和上述 N 种变化）。

 
 **示例 1：** 

```
输入：cells = [0,1,0,1,1,0,0,1], N = 7
输出：[0,0,1,1,0,0,0,0]
解释：
下表概述了监狱每天的状况：
Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
Day 1: [0, 1, 1, 0, 0, 0, 0, 0]
Day 2: [0, 0, 0, 0, 1, 1, 1, 0]
Day 3: [0, 1, 1, 0, 0, 1, 0, 0]
Day 4: [0, 0, 0, 0, 0, 1, 0, 0]
Day 5: [0, 1, 1, 1, 0, 1, 0, 0]
Day 6: [0, 0, 1, 0, 1, 1, 0, 0]
Day 7: [0, 0, 1, 1, 0, 0, 0, 0]
```
 **示例 2：** 

```
输入：cells = [1,0,0,1,0,0,1,0], N = 1000000000
输出：[0,0,1,1,1,1,1,0]

```
 

 **提示：** 
-  `cells.length == 8` 
-  `cells[i]` 的值为 `0` 或 `1` 
-  `1 <= N <= 10^9` 
 
**标签**
`位运算` `数组` `哈希表` `数学` 


## 
```python

```
>
# 958.二叉树的完全性检验
[https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree](https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree) 
## 原题
给定一个二叉树的<meta charset="UTF-8" /> `root` ，确定它是否是一个 *完全二叉树* 。

在一个 **<a href="https://baike.baidu.com/item/完全二叉树/7773232?fr=aladdin" target="_blank">完全二叉树</a>** 中，除了最后一个关卡外，所有关卡都是完全被填满的，并且最后一个关卡中的所有节点都是尽可能靠左的。它可以包含<meta charset="UTF-8" /> `1` 到<meta charset="UTF-8" /> `2^h` 节点之间的最后一级 `h` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/complete-binary-tree-1.png" />

```

输入：root = [1,2,3,4,5,6]
输出：true
解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/complete-binary-tree-2.png" />** 

```

输入：root = [1,2,3,4,5,null,7]
输出：false
解释：值为 7 的结点没有尽可能靠向左侧。

```
 

 **提示：** 
- 树的结点数在范围 <meta charset="UTF-8" /> `[1, 100]` 内。
-  `1 <= Node.val <= 1000` 
 
**标签**
`树` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 959.由斜杠划分区域
[https://leetcode-cn.com/problems/regions-cut-by-slashes](https://leetcode-cn.com/problems/regions-cut-by-slashes) 
## 原题
在由 `1 x 1` 方格组成的 `n x n` 网格 `grid` 中，每个 `1 x 1` 方块由 `'/'` 、 `'\'` 或空格构成。这些字符会将方块划分为一些共边的区域。

给定网格 `grid` 表示为一个字符串数组，返回 *区域的数量* 。

请注意，反斜杠字符是转义的，因此 `'\'` 用 `'\\'` 表示。

 
 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2018/12/15/1.png" style="height: 200px; width: 200px;" />

```

输入：grid = [" /","/ "]
输出：2
```
 **示例 2：** 

<img src="https://assets.leetcode.com/uploads/2018/12/15/2.png" style="height: 198px; width: 200px;" />

```

输入：grid = [" /","  "]
输出：1

```
 **示例 3：** 

<img src="https://assets.leetcode.com/uploads/2018/12/15/4.png" style="height: 200px; width: 200px;" />

```

输入：grid = ["/\\","\\/"]
输出：5
解释：回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。

```
 

 **提示：** 
-  `n == grid.length == grid[i].length` 
-  `1 <= n <= 30` 
-  `grid[i][j]` 是 `'/'` 、 `'\'` 、或 `' '` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `图` 


## 
```python

```
>
# 960.删列造序 III
[https://leetcode-cn.com/problems/delete-columns-to-make-sorted-iii](https://leetcode-cn.com/problems/delete-columns-to-make-sorted-iii) 
## 原题
给定由<meta charset="UTF-8" /> `n` 个小写字母字符串组成的数组<meta charset="UTF-8" /> `strs` ，其中每个字符串长度相等。

选取一个删除索引序列，对于<meta charset="UTF-8" /> `strs` 中的每个字符串，删除对应每个索引处的字符。

比如，有<meta charset="UTF-8" /> `strs = ["abcdef","uvwxyz"]` ，删除索引序列<meta charset="UTF-8" /> `{0, 2, 3}` ，删除后为<meta charset="UTF-8" /> `["bef", "vyz"]` 。

假设，我们选择了一组删除索引<meta charset="UTF-8" /> `answer` ，那么在执行删除操作之后，最终得到的数组的行中的 **每个元素** 都是按 **字典序** 排列的（即 `(strs[0][0] <= strs[0][1] <= ... <= strs[0][strs[0].length - 1])` 和 `(strs[1][0] <= strs[1][1] <= ... <= strs[1][strs[1].length - 1])` ，依此类推）。

请返回<meta charset="UTF-8" /> *`answer.length` 的最小可能值* 。

 

 **示例 1：** 

```

输入：strs = ["babca","bbazb"]
输出：3
解释：
删除 0、1 和 4 这三列后，最终得到的数组是 A = ["bc", "az"]。
这两行是分别按字典序排列的（即，A[0][0] <= A[0][1] 且 A[1][0] <= A[1][1]）。
注意，A[0] > A[1] —— 数组 A 不一定是按字典序排列的。

```
 **示例 2：** 

```

输入：strs = ["edcba"]
输出：4
解释：如果删除的列少于 4 列，则剩下的行都不会按字典序排列。

```
 **示例 3：** 

```

输入：strs = ["ghi","def","abc"]
输出：0
解释：所有行都已按字典序排列。

```
 

 **提示：** 
<meta charset="UTF-8" />
-  `n == strs.length` 
-  `1 <= n <= 100` 
-  `1 <= strs[i].length <= 100` 
-  `strs[i]` 由小写英文字母组成
 
**标签**
`数组` `字符串` `动态规划` 


## 
```python

```
>
# 961.在长度 2N 的数组中找出重复 N 次的元素
[https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array](https://leetcode-cn.com/problems/n-repeated-element-in-size-2n-array) 
## 原题
给你一个整数数组 `nums` ，该数组具有以下属性：
-  `nums.length == 2 * n` .
-  `nums` 包含 `n + 1` 个 **不同的** 元素
-  `nums` 中恰有一个元素重复 `n` 次
找出并返回重复了 `n` 次的那个元素。

 

 **示例 1：** 

```

输入：nums = [1,2,3,3]
输出：3

```
 **示例 2：** 

```

输入：nums = [2,1,2,5,3,2]
输出：2

```
 **示例 3：** 

```

输入：nums = [5,1,5,2,5,3,5,4]
输出：5

```
 

 **提示：** 
-  `2 <= n <= 5000` 
-  `nums.length == 2 * n` 
-  `0 <= nums[i] <= 10^4` 
-  `nums` 由 `n + 1` 个 **不同的** 元素组成，且其中一个元素恰好重复 `n` 次
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 962.最大宽度坡
[https://leetcode-cn.com/problems/maximum-width-ramp](https://leetcode-cn.com/problems/maximum-width-ramp) 
## 原题
给定一个整数数组 `A` ， *坡* 是元组 `(i, j)` ，其中 `i < j` 且 `A[i] <= A[j]` 。这样的坡的宽度为 `j - i` 。

找出 `A` 中的坡的最大宽度，如果不存在，返回 0 。

 

 **示例 1：** 

```
输入：[6,0,8,2,1,5]
输出：4
解释：
最大宽度的坡为 (i, j) = (1, 5): A[1] = 0 且 A[5] = 5.

```
 **示例 2：** 

```
输入：[9,8,1,0,1,9,4,0,4,1]
输出：7
解释：
最大宽度的坡为 (i, j) = (2, 9): A[2] = 1 且 A[9] = 1.

```
 

 **提示：** 
-  `2 <= A.length <= 50000` 
-  `0 <= A[i] <= 50000` 
 

 
**标签**
`栈` `数组` `单调栈` 


## 
```python

```
>
# 963.最小面积矩形 II
[https://leetcode-cn.com/problems/minimum-area-rectangle-ii](https://leetcode-cn.com/problems/minimum-area-rectangle-ii) 
## 原题
给定在 xy 平面上的一组点，确定由这些点组成的任何矩形的最小面积，其中矩形的边 **不一定平行于** x 轴和 y 轴。

如果没有任何矩形，就返回 0。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/22/1a.png" style="height: 151px; width: 150px;">** 

```
输入：[[1,2],[2,1],[1,0],[0,1]]
输出：2.00000
解释：最小面积的矩形出现在 [1,2],[2,1],[1,0],[0,1] 处，面积为 2。
```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/23/2.png" style="height: 94px; width: 150px;">

```
输入：[[0,1],[2,1],[1,1],[1,0],[2,0]]
输出：1.00000
解释：最小面积的矩形出现在 [1,0],[1,1],[2,1],[2,0] 处，面积为 1。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/23/3.png" style="height: 94px; width: 150px;">

```
输入：[[0,3],[1,2],[3,1],[1,3],[2,1]]
输出：0
解释：没法从这些点中组成任何矩形。

```
 **示例 4：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/21/4c.png" style="height: 155px; width: 160px;">** 

```
输入：[[3,1],[1,1],[0,1],[2,1],[3,3],[3,2],[0,2],[2,3]]
输出：2.00000
解释：最小面积的矩形出现在 [2,1],[2,3],[3,3],[3,1] 处，面积为 2。

```
 

 **提示：** 
-  `1 <= points.length <= 50` 
-  `0 <= points[i][0] <= 40000` 
-  `0 <= points[i][1] <= 40000` 
- 所有的点都是不同的。
- 与真实值误差不超过 `10^-5` 的答案将视为正确结果。
 
**标签**
`几何` `数组` `数学` 


## 
```python

```
>
# 964.表示数字的最少运算符
[https://leetcode-cn.com/problems/least-operators-to-express-number](https://leetcode-cn.com/problems/least-operators-to-express-number) 
## 原题
给定一个正整数 `x` ，我们将会写出一个形如 `x (op1) x (op2) x (op3) x ...` 的表达式，其中每个运算符 `op1` ， `op2` ，… 可以是加、减、乘、除（ `+` ， `-` ， `*` ，或是 `/` ）之一。例如，对于 `x = 3` ，我们可以写出表达式 `3 * 3 / 3 + 3 - 3` ，该式的值为 3 。

在写这样的表达式时，我们需要遵守下面的惯例：
- 除运算符（ `/` ）返回有理数。
- 任何地方都没有括号。
- 我们使用通常的操作顺序：乘法和除法发生在加法和减法之前。
- 不允许使用一元否定运算符（ `-` ）。例如，“ `x - x` ” 是一个有效的表达式，因为它只使用减法，但是 “ `-x + x` ” 不是，因为它使用了否定运算符。 
我们希望编写一个能使表达式等于给定的目标值 `target` 且运算符最少的表达式。返回所用运算符的最少数量。

 

 **示例 1：** 

```

输入：x = 3, target = 19
输出：5
解释：3 * 3 + 3 * 3 + 3 / 3 。表达式包含 5 个运算符。

```
 **示例 2：** 

```

输入：x = 5, target = 501
输出：8
解释：5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5 。表达式包含 8 个运算符。

```
 **示例 3：** 

```

输入：x = 100, target = 100000000
输出：3
解释：100 * 100 * 100 * 100 。表达式包含 3 个运算符。
```
 

 **提示：** 
-  `2 <= x <= 100` 
-  `1 <= target <= 2 * 10^8` 
 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 965.单值二叉树
[https://leetcode-cn.com/problems/univalued-binary-tree](https://leetcode-cn.com/problems/univalued-binary-tree) 
## 原题
如果二叉树每个节点都具有相同的值，那么该二叉树就是 *单值* 二叉树。

只有给定的树是单值二叉树时，才返回 `true` ；否则返回 `false` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/screen-shot-2018-12-25-at-50104-pm.png" style="height: 159px; width: 200px;">

```
输入：[1,1,1,1,1,null,1]
输出：true

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/screen-shot-2018-12-25-at-50050-pm.png" style="height: 158px; width: 200px;">

```
输入：[2,2,2,5,2]
输出：false

```
 

 **提示：** 
- 给定树的节点数范围是 `[1, 100]` 。
- 每个节点的值都是整数，范围为 `[0, 99]` 。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 966.元音拼写检查器
[https://leetcode-cn.com/problems/vowel-spellchecker](https://leetcode-cn.com/problems/vowel-spellchecker) 
## 原题
在给定单词列表 `wordlist` 的情况下，我们希望实现一个拼写检查器，将查询单词转换为正确的单词。

对于给定的查询单词 `query` ，拼写检查器将会处理两类拼写错误：
- 大小写：如果查询匹配单词列表中的某个单词（ **不区分大小写** ），则返回的正确单词与单词列表中的大小写相同。

	
- 例如： `wordlist = ["yellow"]` , `query = "YellOw"` : `correct = "yellow"` 
- 例如： `wordlist = ["Yellow"]` , `query = "yellow"` : `correct = "Yellow"` 
- 例如： `wordlist = ["yellow"]` , `query = "yellow"` : `correct = "yellow"` 
	
	
- 元音错误：如果在将查询单词中的元音 `('a', 'e', 'i', 'o', 'u')` 分别替换为任何元音后，能与单词列表中的单词匹配（ **不区分大小写** ），则返回的正确单词与单词列表中的匹配项大小写相同。
	
- 例如： `wordlist = ["YellOw"]` , `query = "yollow"` : `correct = "YellOw"` 
- 例如： `wordlist = ["YellOw"]` , `query = "yeellow"` : `correct = ""` （无匹配项）
- 例如： `wordlist = ["YellOw"]` , `query = "yllw"` : `correct = ""` （无匹配项）
	
	
此外，拼写检查器还按照以下优先级规则操作：
- 当查询完全匹配单词列表中的某个单词（ **区分大小写** ）时，应返回相同的单词。
- 当查询匹配到大小写问题的单词时，您应该返回单词列表中的第一个这样的匹配项。
- 当查询匹配到元音错误的单词时，您应该返回单词列表中的第一个这样的匹配项。
- 如果该查询在单词列表中没有匹配项，则应返回空字符串。
给出一些查询 `queries` ，返回一个单词列表 `answer` ，其中 `answer[i]` 是由查询 `query = queries[i]` 得到的正确单词。

 

 **示例 1：** 

```

输入：wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
输出：["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
```
 **示例 2:** 

```

输入：wordlist = ["yellow"], queries = ["YellOw"]
输出：["yellow"]

```
 

 **提示：** 
-  `1 <= wordlist.length, queries.length <= 5000` 
-  `1 <= wordlist[i].length, queries[i].length <= 7` 
-  `wordlist[i]` 和 `queries[i]` 只包含英文字母
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 967.连续差相同的数字
[https://leetcode-cn.com/problems/numbers-with-same-consecutive-differences](https://leetcode-cn.com/problems/numbers-with-same-consecutive-differences) 
## 原题
返回所有长度为 `n` 且满足其每两个连续位上的数字之间的差的绝对值为 `k` 的 **非负整数** 。

请注意， **除了** 数字 `0` 本身之外，答案中的每个数字都 **不能** 有前导零。例如， `01` 有一个前导零，所以是无效的；但 `0` 是有效的。

你可以按 **任何顺序** 返回答案。

 

 **示例 1：** 

```

输入：n = 3, k = 7
输出：[181,292,707,818,929]
解释：注意，070 不是一个有效的数字，因为它有前导零。

```
 **示例 2：** 

```

输入：n = 2, k = 1
输出：[10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
```
 **示例 3：** 

```

输入：n = 2, k = 0
输出：[11,22,33,44,55,66,77,88,99]

```
 **示例 4：** 

```

输入：n = 2, k = 2
输出：[13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]

```
 

 **提示：** 
-  `2 <= n <= 9` 
-  `0 <= k <= 9` 
 
**标签**
`广度优先搜索` `回溯` 


## 
```python

```
>
# 968.监控二叉树
[https://leetcode-cn.com/problems/binary-tree-cameras](https://leetcode-cn.com/problems/binary-tree-cameras) 
## 原题
给定一个二叉树，我们在树的节点上安装摄像头。

节点上的每个摄影头都可以监视 **其父对象、自身及其直接子对象。** 

计算监控树的所有节点所需的最小摄像头数量。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/bst_cameras_01.png" style="height: 163px; width: 138px;">

```
输入：[0,0,null,0,0]
输出：1
解释：如图所示，一台摄像头足以监控所有节点。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/29/bst_cameras_02.png" style="height: 312px; width: 139px;">

```
输入：[0,0,null,0,null,0,null,null,0]
输出：2
解释：需要至少两个摄像头来监视树的所有节点。 上图显示了摄像头放置的有效位置之一。

```
<br>
 **提示：** 
- 给定树的节点数的范围是 `[1, 1000]` 。
- 每个节点的值都是 0。
 
**标签**
`树` `深度优先搜索` `动态规划` `二叉树` 


## 
```python

```
>
# 969.煎饼排序
[https://leetcode-cn.com/problems/pancake-sorting](https://leetcode-cn.com/problems/pancake-sorting) 
## 原题
给你一个整数数组 `arr` ，请使用 **煎饼翻转** 完成对数组的排序。

一次煎饼翻转的执行过程如下：
- 选择一个整数 `k` ， `1 <= k <= arr.length` 
- 反转子数组 `arr[0...k-1]` （ **下标从 0 开始** ）
例如， `arr = [3,2,1,4]` ，选择 `k = 3` 进行一次煎饼翻转，反转子数组 `[3,2,1]` ，得到 `arr = [ **1** , **2** , **3** ,4]` 。

以数组形式返回能使 `arr` 有序的煎饼翻转操作所对应的 `k` 值序列。任何将数组排序且翻转次数在  `10 * arr.length` 范围内的有效答案都将被判断为正确。

 

 **示例 1：** 

```

输入：[3,2,4,1]
输出：[4,2,4,3]
解释：
我们执行 4 次煎饼翻转，k 值分别为 4，2，4，和 3。
初始状态 arr = [3, 2, 4, 1]
第一次翻转后（k = 4）：arr = [1, 4, 2, 3]
第二次翻转后（k = 2）：arr = [4, 1, 2, 3]
第三次翻转后（k = 4）：arr = [3, 2, 1, 4]
第四次翻转后（k = 3）：arr = [1, 2, 3, 4]，此时已完成排序。 

```
 **示例 2：** 

```

输入：[1,2,3]
输出：[]
解释：
输入已经排序，因此不需要翻转任何内容。
请注意，其他可能的答案，如 [3，3] ，也将被判断为正确。

```
 

 **提示：** 
-  `1 <= arr.length <= 100` 
-  `1 <= arr[i] <= arr.length` 
-  `arr` 中的所有整数互不相同（即， `arr` 是从 `1` 到 `arr.length` 整数的一个排列）
 
**标签**
`贪心` `数组` `双指针` `排序` 


## 
```python

```
>
# 970.强整数
[https://leetcode-cn.com/problems/powerful-integers](https://leetcode-cn.com/problems/powerful-integers) 
## 原题
给定三个整数 `x` 、 `y` 和 `bound` ，返回 *值小于或等于 `bound` 的所有 **强整数** 组成的列表* 。

如果某一整数可以表示为 `x^i + y^j` ，其中整数 `i >= 0` 且 `j >= 0` ，那么我们认为该整数是一个 **强整数** 。

你可以按 **任何顺序** 返回答案。在你的回答中，每个值 **最多** 出现一次。

 

 **示例 1：** 

```

输入：x = 2, y = 3, bound = 10
输出：[2,3,4,5,7,9,10]
解释： 
2 = 2^0 + 3^0
3 = 2^1 + 3^0
4 = 2^0 + 3^1
5 = 2^1 + 3^1
7 = 2^2 + 3^1
9 = 2^3 + 3^0
10 = 2^0 + 3^2
```
 **示例 2：** 

```

输入：x = 3, y = 5, bound = 15
输出：[2,4,6,8,10,14]

```
 

 **提示：** 
-  `1 <= x, y <= 100` 
-  `0 <= bound <= 10^6` 
 
**标签**
`哈希表` `数学` 


## 
```python

```
>
# 971.翻转二叉树以匹配先序遍历
[https://leetcode-cn.com/problems/flip-binary-tree-to-match-preorder-traversal](https://leetcode-cn.com/problems/flip-binary-tree-to-match-preorder-traversal) 
## 原题
给你一棵二叉树的根节点 `root` ，树中有 `n` 个节点，每个节点都有一个不同于其他节点且处于 `1` 到 `n` 之间的值。

另给你一个由 `n` 个值组成的行程序列 `voyage` ，表示 **预期** 的二叉树 <a href="https://baike.baidu.com/item/%E5%85%88%E5%BA%8F%E9%81%8D%E5%8E%86/6442839?fr=aladdin" target="_blank"> **先序遍历** </a> 结果。

通过交换节点的左右子树，可以 **翻转** 该二叉树中的任意节点。例，翻转节点 1 的效果如下：
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/15/fliptree.jpg" style="width: 400px; height: 187px;" />
请翻转 **最少** 的树中节点，使二叉树的 **先序遍历** 与预期的遍历行程  `voyage`   **相匹配** 。 

如果可以，则返回 **翻转的** 所有节点的值的列表。你可以按任何顺序返回答案。如果不能，则返回列表 `[-1]` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-01.png" style="width: 150px; height: 205px;" />
```

输入：root = [1,2], voyage = [2,1]
输出：[-1]
解释：翻转节点无法令先序遍历匹配预期行程。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-02.png" style="width: 150px; height: 142px;" />
```

输入：root = [1,2,3], voyage = [1,3,2]
输出：[1]
解释：交换节点 2 和 3 来翻转节点 1 ，先序遍历可以匹配预期行程。
```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/02/1219-02.png" style="width: 150px; height: 142px;" />
```

输入：root = [1,2,3], voyage = [1,2,3]
输出：[]
解释：先序遍历已经匹配预期行程，所以不需要翻转节点。

```
 

 **提示：** 
- 树中的节点数目为 `n` 
-  `n == voyage.length` 
-  `1 <= n <= 100` 
-  `1 <= Node.val, voyage[i] <= n` 
- 树中的所有值 **互不相同** 
-  `voyage` 中的所有值 **互不相同** 
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 972.相等的有理数
[https://leetcode-cn.com/problems/equal-rational-numbers](https://leetcode-cn.com/problems/equal-rational-numbers) 
## 原题
给定两个字符串 `s` 和 `t` ，每个字符串代表一个非负有理数，只有当它们表示相同的数字时才返回 `true` 。字符串中可以使用括号来表示有理数的重复部分。

 **有理数** 最多可以用三个部分来表示： *整数部分* `<IntegerPart>` 、 *小数非重复部分* `<NonRepeatingPart>` 和 *小数重复部分* `<(><RepeatingPart><)>` 。数字可以用以下三种方法之一来表示：
-  `<IntegerPart>` 

	
- 例： `0` , `12` 和 `123` 
	
	
-  `<IntegerPart><.><NonRepeatingPart>` 
	
- 例： `0.5<font color="#333333"><font face="Helvetica Neue, Helvetica, Arial, sans-serif"><span style="font-size:14px"><span style="background-color:#ffffff"> , </span></span></font></font>` <font color="#333333"><font face="Helvetica Neue, Helvetica, Arial, sans-serif"><span style="font-size:14px"><span style="background-color:#ffffff"> `1.` , </span></span></font></font> `2.12` 和 `123.0001` 
	
	
-  `<IntegerPart><.><NonRepeatingPart><(><RepeatingPart><)>` 
	
- 例： `0.1(6)` ， `1.(9)` ， `123.00(1212)` 
	
	
十进制展开的重复部分通常在一对圆括号内表示。例如：
-  `1 / 6 = 0.16666666... = 0.1(6) = 0.1666(6) = 0.166(66)` 
 

 **示例 1：** 

```

输入：s = "0.(52)", t = "0.5(25)"
输出：true
解释：因为 "0.(52)" 代表 0.52525252...，而 "0.5(25)" 代表 0.52525252525.....，则这两个字符串表示相同的数字。

```
 **示例 2：** 

```

输入：s = "0.1666(6)", t = "0.166(66)"
输出：true

```
 **示例 3：** 

```

输入：s = "0.9(9)", t = "1."
输出：true
解释："0.9(9)" 代表 0.999999999... 永远重复，等于 1 。[<a href="https://baike.baidu.com/item/0.999…/5615429?fr=aladdin" target="_blank">有关说明，请参阅此链接]
"1." 表示数字 1，其格式正确：(IntegerPart) = "1" 且 (NonRepeatingPart) = "" 。
```
 

 **提示：** 
- 每个部分仅由数字组成。
- 整数部分 `<IntegerPart>` 不会以零开头。（零本身除外）
-  `1 <= <IntegerPart>.length <= 4` 
-  `0 <= <NonRepeatingPart>.length <= 4` 
-  `1 <= <RepeatingPart>.length <= 4` 

<span style="display:block"><span style="height:0px"><span style="position:absolute">​​​​​</span></span></span>
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 973.最接近原点的 K 个点
[https://leetcode-cn.com/problems/k-closest-points-to-origin](https://leetcode-cn.com/problems/k-closest-points-to-origin) 
## 原题
给定一个数组 `points` ，其中 `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` 表示 **X-Y** 平面上的一个点，并且是一个整数 `k` ，返回离原点 `(0,0)` 最近的 `k` 个点。

这里，平面上两点之间的距离是 **欧几里德距离** （ `√(x<sub>1</sub> - x<sub>2</sub>)^2 + (y<sub>1</sub> - y<sub>2</sub>)^2` ）。

你可以按 **任何顺序** 返回答案。除了点坐标的顺序之外，答案 **确保** 是 **唯一** 的。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/03/03/closestplane1.jpg" style="height: 400px; width: 400px;" />

```

输入：points = [[1,3],[-2,2]], k = 1
输出：[[-2,2]]
解释： 
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。

```
 **示例 2：** 

```

输入：points = [[3,3],[5,-1],[-2,4]], k = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）

```
 

 **提示：** 
-  `1 <= k <= points.length <= 10^4` 
-  `-10^4 < x<sub>i</sub>, y<sub>i</sub> < 10^4` 
 
**标签**
`几何` `数组` `数学` `分治` `快速选择` `排序` `堆（优先队列）` 


## 
```python

```
>
# 974.和可被 K 整除的子数组
[https://leetcode-cn.com/problems/subarray-sums-divisible-by-k](https://leetcode-cn.com/problems/subarray-sums-divisible-by-k) 
## 原题
给定一个整数数组 `nums` 和一个整数 `k` ，返回其中元素之和可被 `k` 整除的（连续、非空） **子数组** 的数目。

 **子数组** 是数组的 **连续** 部分。

 

 **示例 1：** 

```

输入：nums = [4,5,0,-2,-3,1], k = 5
输出：7
解释：
有 7 个子数组满足其元素之和可被 k = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

```
 **示例 2:** 

```

输入: nums = [5], k = 9
输出: 0

```
 

 **提示:** 
-  `1 <= nums.length <= 3 * 10^4` 
-  `-10^4 <= nums[i] <= 10^4` 
-  `2 <= k <= 10^4` 
 
**标签**
`数组` `哈希表` `前缀和` 


## 
```python

```
>
# 975.奇偶跳
[https://leetcode-cn.com/problems/odd-even-jump](https://leetcode-cn.com/problems/odd-even-jump) 
## 原题
给定一个整数数组 `A` ，你可以从某一起始索引出发，跳跃一定次数。在你跳跃的过程中，第 1、3、5... 次跳跃称为奇数跳跃，而第 2、4、6... 次跳跃称为偶数跳跃。

你可以按以下方式从索引 `i` 向后跳转到索引 `j` （其中 `i < j` ）：
- 在进行奇数跳跃时（如，第 1，3，5... 次跳跃），你将会跳到索引 `j` ，使得 `A[i] <= A[j]` ， `A[j]` 是可能的最小值。如果存在多个这样的索引 `j` ，你只能跳到满足要求的 **最小** 索引 `j` 上。
- 在进行偶数跳跃时（如，第 2，4，6... 次跳跃），你将会跳到索引 `j` ，使得 `A[i] >= A[j]` ， `A[j]` 是可能的最大值。如果存在多个这样的索引 `j` ，你只能跳到满足要求的 **最小** 索引 `j` 上。
- （对于某些索引 `i` ，可能无法进行合乎要求的跳跃。）
如果从某一索引开始跳跃一定次数（可能是 0 次或多次），就可以到达数组的末尾（索引 `A.length - 1` ），那么该索引就会被认为是好的起始索引。

返回好的起始索引的数量。

 

 **示例 1：** 

```
输入：[10,13,12,14,15]
输出：2
解释： 
从起始索引 i = 0 出发，我们可以跳到 i = 2，（因为 A[2] 是 A[1]，A[2]，A[3]，A[4] 中大于或等于 A[0] 的最小值），然后我们就无法继续跳下去了。
从起始索引 i = 1 和 i = 2 出发，我们可以跳到 i = 3，然后我们就无法继续跳下去了。
从起始索引 i = 3 出发，我们可以跳到 i = 4，到达数组末尾。
从起始索引 i = 4 出发，我们已经到达数组末尾。
总之，我们可以从 2 个不同的起始索引（i = 3, i = 4）出发，通过一定数量的跳跃到达数组末尾。

```
 **示例 2：** 

```
输入：[2,3,1,1,4]
输出：3
解释：
从起始索引 i=0 出发，我们依次可以跳到 i = 1，i = 2，i = 3：

在我们的第一次跳跃（奇数）中，我们先跳到 i = 1，因为 A[1] 是（A[1]，A[2]，A[3]，A[4]）中大于或等于 A[0] 的最小值。

在我们的第二次跳跃（偶数）中，我们从 i = 1 跳到 i = 2，因为 A[2] 是（A[2]，A[3]，A[4]）中小于或等于 A[1] 的最大值。A[3] 也是最大的值，但 2 是一个较小的索引，所以我们只能跳到 i = 2，而不能跳到 i = 3。

在我们的第三次跳跃（奇数）中，我们从 i = 2 跳到 i = 3，因为 A[3] 是（A[3]，A[4]）中大于或等于 A[2] 的最小值。

我们不能从 i = 3 跳到 i = 4，所以起始索引 i = 0 不是好的起始索引。

类似地，我们可以推断：
从起始索引 i = 1 出发， 我们跳到 i = 4，这样我们就到达数组末尾。
从起始索引 i = 2 出发， 我们跳到 i = 3，然后我们就不能再跳了。
从起始索引 i = 3 出发， 我们跳到 i = 4，这样我们就到达数组末尾。
从起始索引 i = 4 出发，我们已经到达数组末尾。
总之，我们可以从 3 个不同的起始索引（i = 1, i = 3, i = 4）出发，通过一定数量的跳跃到达数组末尾。

```
 **示例 3：** 

```
输入：[5,1,3,4,2]
输出：3
解释： 
我们可以从起始索引 1，2，4 出发到达数组末尾。

```
 

 **提示：** 
-  `1 <= A.length <= 20000` 
-  `0 <= A[i] < 100000` 
 
**标签**
`栈` `数组` `动态规划` `有序集合` `单调栈` 


## 
```python

```
>
# 976.三角形的最大周长
[https://leetcode-cn.com/problems/largest-perimeter-triangle](https://leetcode-cn.com/problems/largest-perimeter-triangle) 
## 原题
给定由一些正数（代表长度）组成的数组 `nums` ，返回 *由其中三个长度组成的、 **面积不为零** 的三角形的最大周长* 。如果不能形成任何面积不为零的三角形，返回 `0` 。

 
 **示例 1：** 

```

输入：nums = [2,1,2]
输出：5

```
 **示例 2：** 

```

输入：nums = [1,2,1]
输出：0

```
 

 **提示：** 
-  `3 <= nums.length <= 10^4` 
-  `1 <= nums[i] <= 10^6` 
 
**标签**
`贪心` `数组` `数学` `排序` 


## 
```python

```
>
# 977.有序数组的平方
[https://leetcode-cn.com/problems/squares-of-a-sorted-array](https://leetcode-cn.com/problems/squares-of-a-sorted-array) 
## 原题
给你一个按 **非递减顺序** 排序的整数数组 `nums` ，返回 **每个数字的平方** 组成的新数组，要求也按 **非递减顺序** 排序。
 

 **示例 1：** 

```

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
```
 **示例 2：** 

```

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]

```
 

 **提示：** 
-  `<span>1 <= nums.length <= </span>10^4` 
-  `-10^4 <= nums[i] <= 10^4` 
-  `nums` 已按 **非递减顺序** 排序
 

 **进阶：** 
- 请你<span style="color: rgb(36, 41, 46); font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji"; font-size: 14px; font-style: normal; font-variant-ligatures: normal; font-variant-caps: normal; font-weight: 400; letter-spacing: normal; orphans: 2; text-align: start; text-indent: 0px; text-transform: none; white-space: normal; widows: 2; word-spacing: 0px; -webkit-text-stroke-width: 0px; background-color: rgb(255, 255, 255); text-decoration-style: initial; text-decoration-color: initial; display: inline !important; float: none;">设计时间复杂度为 `O(n)` 的算法解决本问题</span>
 
**标签**
`数组` `双指针` `排序` 


## 
```python

```
>
# 978.最长湍流子数组
[https://leetcode-cn.com/problems/longest-turbulent-subarray](https://leetcode-cn.com/problems/longest-turbulent-subarray) 
## 原题
给定一个整数数组 `arr` ，返回 `arr` 的 *最大湍流子数组的 **长度*** **** 。

如果比较符号在子数组中的每个相邻元素对之间翻转，则该子数组是 **湍流子数组** 。

更正式地来说，当 `arr` 的子数组 `A[i], A[i+1], ..., A[j]` 满足仅满足下列条件时，我们称其为 *湍流子数组* ：
- 若 `i <= k < j` ：

	
- 当 `k` 为奇数时， `A[k] > A[k+1]` ，且
- 当 `k` 为偶数时， `A[k] < A[k+1]` ；
	
	
-  **或** 若 `i <= k < j` ：
	
- 当 `k` 为偶数时， `A[k] > A[k+1]` ，且
- 当 `k` 为奇数时， `A[k] < A[k+1]` 。
	
	
 

 **示例 1：** 

```

输入：arr = [9,4,2,10,7,8,8,1,9]
输出：5
解释：arr[1] > arr[2] < arr[3] > arr[4] < arr[5]
```
 **示例 2：** 

```

输入：arr = [4,8,12,16]
输出：2

```
 **示例 3：** 

```

输入：arr = [100]
输出：1

```
 

 **提示：** 
-  `1 <= arr.length <= 4 * 10^4` 
-  `0 <= arr[i] <= 10^9` 
 
**标签**
`数组` `动态规划` `滑动窗口` 


## 
```python

```
>
# 979.在二叉树中分配硬币
[https://leetcode-cn.com/problems/distribute-coins-in-binary-tree](https://leetcode-cn.com/problems/distribute-coins-in-binary-tree) 
## 原题
给定一个有 `N` 个结点的二叉树的根结点 `root` ，树中的每个结点上都对应有 `node.val` 枚硬币，并且总共有 `N` 枚硬币。

在一次移动中，我们可以选择两个相邻的结点，然后将一枚硬币从其中一个结点移动到另一个结点。(移动可以是从父结点到子结点，或者从子结点移动到父结点。)。

返回使每个结点上只有一枚硬币所需的移动次数。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/19/tree1.png" style="height: 142px; width: 150px;">** 

```
输入：[3,0,0]
输出：2
解释：从树的根结点开始，我们将一枚硬币移到它的左子结点上，一枚硬币移到它的右子结点上。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/19/tree2.png" style="height: 142px; width: 150px;">** 

```
输入：[0,3,0]
输出：3
解释：从根结点的左子结点开始，我们将两枚硬币移到根结点上 [移动两次]。然后，我们把一枚硬币从根结点移到右子结点上。

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/19/tree3.png" style="height: 142px; width: 150px;">** 

```
输入：[1,0,2]
输出：2

```
 **示例 4：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/01/19/tree4.png" style="height: 156px; width: 155px;">** 

```
输入：[1,0,0,null,3]
输出：4

```
 

 **提示：** 
-  `1<= N <= 100` 
-  `0 <= node.val <= N` 
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 980.不同路径 III
[https://leetcode-cn.com/problems/unique-paths-iii](https://leetcode-cn.com/problems/unique-paths-iii) 
## 原题
在二维网格 `grid` 上，有 4 种类型的方格：
-  `1` 表示起始方格。且只有一个起始方格。
-  `2` 表示结束方格，且只有一个结束方格。
-  `0` 表示我们可以走过的空方格。
-  `-1` 表示我们无法跨越的障碍。
返回在四个方向（上、下、左、右）上行走时，从起始方格到结束方格的不同路径的数目 **。** 

 **每一个无障碍方格都要通过一次，但是一条路径中不能重复通过同一个方格** 。

 

 **示例 1：** 

```
输入：[[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
输出：2
解释：我们有以下两条路径：
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
```
 **示例 2：** 

```
输入：[[1,0,0,0],[0,0,0,0],[0,0,0,2]]
输出：4
解释：我们有以下四条路径： 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
```
 **示例 3：** 

```
输入：[[0,1],[2,0]]
输出：0
解释：
没有一条路能完全穿过每一个空的方格一次。
请注意，起始和结束方格可以位于网格中的任意位置。

```
 

 **提示：** 
-  `1 <= grid.length * grid[0].length <= 20` 
 
**标签**
`位运算` `数组` `回溯` `矩阵` 


## 
```python

```
>
# 981.基于时间的键值存储
[https://leetcode-cn.com/problems/time-based-key-value-store](https://leetcode-cn.com/problems/time-based-key-value-store) 
## 原题
设计一个基于时间的键值数据结构，该结构可以在不同时间戳存储对应同一个键的多个值，并针对特定时间戳检索键对应的值。

实现 `TimeMap` 类：
-  `TimeMap()` 初始化数据结构对象
-  `void set(String key, String value, int timestamp)` 存储键  `key` 、值  `value` ，以及给定的时间戳  `timestamp` 。
-  `String get(String key, int timestamp)` 
	
- 返回先前调用  `set(key, value, timestamp_prev)`  所存储的值，其中  `timestamp_prev <= timestamp` 。
- 如果有多个这样的值，则返回对应最大的   `timestamp_prev`  的那个值。
- 如果没有值，则返回空字符串（ `""` ）。
	
	

 

 **示例：** 

```

输入：
["TimeMap", "set", "get", "get", "set", "get", "get"]
[[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
输出：
[null, null, "bar", "bar", null, "bar2", "bar2"]

解释：
TimeMap timeMap = new TimeMap();
timeMap.set("foo", "bar", 1);  // 存储键 "foo" 和值 "bar" ，时间戳 timestamp = 1   
timeMap.get("foo", 1);         // 返回 "bar"
timeMap.get("foo", 3);         // 返回 "bar", 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，所以唯一的值位于时间戳 1 处（即 "bar"） 。
timeMap.set("foo", "bar2", 4); // 存储键 "foo" 和值 "bar2" ，时间戳 timestamp = 4  
timeMap.get("foo", 4);         // 返回 "bar2"
timeMap.get("foo", 5);         // 返回 "bar2"

```
 

 **提示：** 
-  `1 <= key.length, value.length <= 100` 
-  `key` 和 `value` 由小写英文字母和数字组成
-  `1 <= timestamp <= 10^7` 
-  `set` 操作中的时间戳 `timestamp` 都是严格递增的
- 最多调用  `set` 和 `get` 操作 `2 * 10^5` 次
 
**标签**
`设计` `哈希表` `字符串` `二分查找` 


## 
```python

```
>
# 982.按位与为零的三元组
[https://leetcode-cn.com/problems/triples-with-bitwise-and-equal-to-zero](https://leetcode-cn.com/problems/triples-with-bitwise-and-equal-to-zero) 
## 原题
给定一个整数数组 `A` ，找出索引为 (i, j, k) 的三元组，使得：
-  `0 <= i < A.length` 
-  `0 <= j < A.length` 
-  `0 <= k < A.length` 
-  `A[i] &amp; A[j] &amp; A[k] == 0` ，其中 `&amp;` 表示按位与（AND）操作符。
 

 **示例：** 

```
输入：[2,1,3]
输出：12
解释：我们可以选出如下 i, j, k 三元组：
(i=0, j=0, k=1) : 2 &amp; 2 &amp; 1
(i=0, j=1, k=0) : 2 &amp; 1 &amp; 2
(i=0, j=1, k=1) : 2 &amp; 1 &amp; 1
(i=0, j=1, k=2) : 2 &amp; 1 &amp; 3
(i=0, j=2, k=1) : 2 &amp; 3 &amp; 1
(i=1, j=0, k=0) : 1 &amp; 2 &amp; 2
(i=1, j=0, k=1) : 1 &amp; 2 &amp; 1
(i=1, j=0, k=2) : 1 &amp; 2 &amp; 3
(i=1, j=1, k=0) : 1 &amp; 1 &amp; 2
(i=1, j=2, k=0) : 1 &amp; 3 &amp; 2
(i=2, j=0, k=1) : 3 &amp; 2 &amp; 1
(i=2, j=1, k=0) : 3 &amp; 1 &amp; 2

```
 

 **提示：** 
-  `1 <= A.length <= 1000` 
-  `0 <= A[i] < 2^16` 
 
**标签**
`位运算` `数组` `哈希表` 


## 
```python

```
>
# 983.最低票价
[https://leetcode-cn.com/problems/minimum-cost-for-tickets](https://leetcode-cn.com/problems/minimum-cost-for-tickets) 
## 原题
在一个火车旅行很受欢迎的国度，你提前一年计划了一些火车旅行。在接下来的一年里，你要旅行的日子将以一个名为 `days` 的数组给出。每一项是一个从 `1` 到 `365` 的整数。

火车票有 **三种不同的销售方式** ：
- 一张 **为期一天** 的通行证售价为 `costs[0]` 美元；
- 一张 **为期七天** 的通行证售价为 `costs[1]` 美元；
- 一张 **为期三十天** 的通行证售价为 `costs[2]` 美元。
通行证允许数天无限制的旅行。 例如，如果我们在第 `2` 天获得一张 **为期 7 天** 的通行证，那么我们可以连着旅行 7 天：第 `2` 天、第 `3` 天、第 `4` 天、第 `5` 天、第 `6` 天、第 `7` 天和第 `8` 天。

返回 *你想要完成在给定的列表 `days` 中列出的每一天的旅行所需要的最低消费* 。

 

 **示例 1：** 

```

输入：days = [1,4,6,7,8,20], costs = [2,7,15]
输出：11
解释： 
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划：
在第 1 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 1 天生效。
在第 3 天，你花了 costs[1] = $7 买了一张为期 7 天的通行证，它将在第 3, 4, ..., 9 天生效。
在第 20 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 20 天生效。
你总共花了 $11，并完成了你计划的每一天旅行。

```
 **示例 2：** 

```

输入：days = [1,2,3,4,5,6,7,8,9,10,30,31], costs = [2,7,15]
输出：17
解释：
例如，这里有一种购买通行证的方法，可以让你完成你的旅行计划： 
在第 1 天，你花了 costs[2] = $15 买了一张为期 30 天的通行证，它将在第 1, 2, ..., 30 天生效。
在第 31 天，你花了 costs[0] = $2 买了一张为期 1 天的通行证，它将在第 31 天生效。 
你总共花了 $17，并完成了你计划的每一天旅行。

```
 

 **提示：** 
-  `1 <= days.length <= 365` 
-  `1 <= days[i] <= 365` 
-  `days` 按顺序严格递增
-  `costs.length == 3` 
-  `1 <= costs[i] <= 1000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 984.不含 AAA 或 BBB 的字符串
[https://leetcode-cn.com/problems/string-without-aaa-or-bbb](https://leetcode-cn.com/problems/string-without-aaa-or-bbb) 
## 原题
给定两个整数 `a` 和 `b` ，返回 **任意** 字符串 `s` ，要求满足：
-  `s` 的长度为 `a + b` ，且正好包含 `<font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.600000381469727px"><span style="caret-color:#c7254e"><span style="background-color:#f9f2f4">a</span></span></span></font></font>` 个 `'a'` 字母与 `<font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.600000381469727px"><span style="caret-color:#c7254e"><span style="background-color:#f9f2f4">b</span></span></span></font></font>` 个 `'b'` 字母；
- 子串 `'aaa'` 没有出现在 `s` 中；
- 子串 `'bbb'` 没有出现在 `s` 中。
 

 **示例 1：** 

```

输入：a = 1, b = 2
输出："abb"
解释："abb", "bab" 和 "bba" 都是正确答案。

```
 **示例 2：** 

```

输入：a = 4, b = 1
输出："aabaa"
```
 

 **提示：** 
-  `0 <= a, b <= 100` 
- 对于给定的 `a` 和 `b` ，保证存在满足要求的 `s` 

<span style="display:block"><span style="height:0px"><span style="position:absolute">​​​</span></span></span>
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 985.查询后的偶数和
[https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries](https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries) 
## 原题
给出一个整数数组 `A` 和一个查询数组 `queries` 。

对于第 `i` 次查询，有 `val = queries[i][0], index = queries[i][1]` ，我们会把 `val` 加到 `A[index]` 上。然后，第 `i` 次查询的答案是 `A` 中偶数值的和。

 *（此处给定的 `index = queries[i][1]` 是从 0 开始的索引，每次查询都会永久修改数组 `A` 。）* 

返回所有查询的答案。你的答案应当以数组 `answer` 给出， `answer[i]` 为第 `i` 次查询的答案。

 

 **示例：** 

```
输入：A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
输出：[8,6,2,4]
解释：
开始时，数组为 [1,2,3,4]。
将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。

```
 

 **提示：** 
-  `1 <= A.length <= 10000` 
-  `-10000 <= A[i] <= 10000` 
-  `1 <= queries.length <= 10000` 
-  `-10000 <= queries[i][0] <= 10000` 
-  `0 <= queries[i][1] < A.length` 
 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 986.区间列表的交集
[https://leetcode-cn.com/problems/interval-list-intersections](https://leetcode-cn.com/problems/interval-list-intersections) 
## 原题
给定两个由一些 **闭区间** 组成的列表， `firstList` 和 `secondList` ，其中 `firstList[i] = [start<sub>i</sub>, end<sub>i</sub>]` 而  `secondList[j] = [start<sub>j</sub>, end<sub>j</sub>]` 。每个区间列表都是成对 **不相交** 的，并且 **已经排序** 。

返回这 **两个区间列表的交集** 。

形式上， **闭区间**   `[a, b]` （其中  `a <= b` ）表示实数  `x`  的集合，而  `a <= x <= b` 。

两个闭区间的 **交集** 是一组实数，要么为空集，要么为闭区间。例如， `[1, 3]` 和 `[2, 4]` 的交集为 `[2, 3]` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2019/01/30/interval1.png" style="width: 700px; height: 194px;" />
```

输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

```
 **示例 2：** 

```

输入：firstList = [[1,3],[5,9]], secondList = []
输出：[]

```
 **示例 3：** 

```

输入：firstList = [], secondList = [[4,8],[10,12]]
输出：[]

```
 **示例 4：** 

```

输入：firstList = [[1,7]], secondList = [[3,10]]
输出：[[3,7]]

```
 

 **提示：** 
-  `0 <= firstList.length, secondList.length <= 1000` 
-  `firstList.length + secondList.length >= 1` 
-  `0 <= start<sub>i</sub> < end<sub>i</sub> <= 10^9` 
-  `end<sub>i</sub> < start<sub>i+1</sub>` 
-  `0 <= start<sub>j</sub> < end<sub>j</sub> <= 10^9` 
-  `end<sub>j</sub> < start<sub>j+1</sub>` 
 
**标签**
`数组` `双指针` 


## 
```python

```
>
# 987.二叉树的垂序遍历
[https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree](https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree) 
## 原题
给你二叉树的根结点 `root` ，请你设计算法计算二叉树的 **垂序遍历** 序列。

对位于  `(row, col)`  的每个结点而言，其左右子结点分别位于  `(row + 1, col - 1)`  和  `(row + 1, col + 1)` 。树的根结点位于 `(0, 0)` 。

二叉树的 **垂序遍历** 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。如果同行同列上有多个结点，则按结点的值从小到大进行排序。

返回二叉树的 **垂序遍历** 序列。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/29/vtree1.jpg" style="width: 431px; height: 304px;" />
```

输入：root = [3,9,20,null,null,15,7]
输出：[[9],[3,15],[20],[7]]
解释：
列 -1 ：只有结点 9 在此列中。
列  0 ：只有结点 3 和 15 在此列中，按从上到下顺序。
列  1 ：只有结点 20 在此列中。
列  2 ：只有结点 7 在此列中。
```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/29/vtree2.jpg" style="width: 512px; height: 304px;" />
```

输入：root = [1,2,3,4,5,6,7]
输出：[[4],[2],[1,5,6],[3],[7]]
解释：
列 -2 ：只有结点 4 在此列中。
列 -1 ：只有结点 2 在此列中。
列  0 ：结点 1 、5 和 6 都在此列中。
          1 在上面，所以它出现在前面。
          5 和 6 位置都是 (2, 0) ，所以按值从小到大排序，5 在 6 的前面。
列  1 ：只有结点 3 在此列中。
列  2 ：只有结点 7 在此列中。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/29/vtree3.jpg" style="width: 512px; height: 304px;" />
```

输入：root = [1,2,3,4,6,5,7]
输出：[[4],[2],[1,5,6],[3],[7]]
解释：
这个示例实际上与示例 2 完全相同，只是结点 5 和 6 在树中的位置发生了交换。
因为 5 和 6 的位置仍然相同，所以答案保持不变，仍然按值从小到大排序。
```
 

 **提示：** 
- 树中结点数目总数在范围 `[1, 1000]` 内
-  `0 <= Node.val <= 1000` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `哈希表` `二叉树` 


## 
```python

```
>
# 988.从叶结点开始的最小字符串
[https://leetcode-cn.com/problems/smallest-string-starting-from-leaf](https://leetcode-cn.com/problems/smallest-string-starting-from-leaf) 
## 原题
给定一颗根结点为 `root` 的二叉树，树中的每一个结点都有一个 `[0, 25]` 范围内的值，分别代表字母 `'a'` 到 `'z'` 。

返回 ***按字典序最小** 的字符串，该字符串从这棵树的一个叶结点开始，到根结点结束* 。

<blockquote>
注 **：** 字符串中任何较短的前缀在 **字典序上** 都是 **较小** 的：
- 例如，在字典序上 `"ab"` 比 `"aba"` 要小。叶结点是指没有子结点的结点。 

</blockquote>

节点的叶节点是没有子节点的节点。

 
 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/02/tree1.png" style="height: 358px; width: 534px;" />** 

```

输入：root = [0,1,2,3,4,3,4]
输出："dba"

```
 **示例 2：** 

<img src="https://assets.leetcode.com/uploads/2019/01/30/tree2.png" />

```

输入：root = [25,1,3,1,3,0,2]
输出："adz"

```
 **示例 3：** 

<img src="https://assets.leetcode.com/uploads/2019/02/01/tree3.png" style="height: 513px; width: 490px;" />

```

输入：root = [2,2,1,null,1,0,null,0]
输出："abc"

```
 

 **提示：** 
- 给定树的结点数在 `[1, 8500]` 范围内
-  `0 <= Node.val <= 25` 
 
**标签**
`树` `深度优先搜索` `字符串` `二叉树` 


## 
```python

```
>
# 989.数组形式的整数加法
[https://leetcode-cn.com/problems/add-to-array-form-of-integer](https://leetcode-cn.com/problems/add-to-array-form-of-integer) 
## 原题
对于非负整数 `X` 而言， *`X`* 的 *数组形式* 是每位数字按从左到右的顺序形成的数组。例如，如果 `X = 1231` ，那么其数组形式为 `[1,2,3,1]` 。

给定非负整数 `X` 的数组形式 `A` ，返回整数 `X+K` 的数组形式。

 
 **示例 1：** 

```
输入：A = [1,2,0,0], K = 34
输出：[1,2,3,4]
解释：1200 + 34 = 1234

```
 **示例 2：** 

```
输入：A = [2,7,4], K = 181
输出：[4,5,5]
解释：274 + 181 = 455

```
 **示例 3：** 

```
输入：A = [2,1,5], K = 806
输出：[1,0,2,1]
解释：215 + 806 = 1021

```
 **示例 4：** 

```
输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
输出：[1,0,0,0,0,0,0,0,0,0,0]
解释：9999999999 + 1 = 10000000000

```
 

 **提示：** 
-  `1 <= A.length <= 10000` 
-  `0 <= A[i] <= 9` 
-  `0 <= K <= 10000` 
- 如果 `A.length > 1` ，那么 `A[0] != 0` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 990.等式方程的可满足性
[https://leetcode-cn.com/problems/satisfiability-of-equality-equations](https://leetcode-cn.com/problems/satisfiability-of-equality-equations) 
## 原题
给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 `equations[i]` 的长度为 `4` ，并采用两种不同的形式之一： `"a==b"` 或 `"a!=b"` 。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。

只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 `true` ，否则返回 `false` 。 

 
 **示例 1：** 

```
输入：["a==b","b!=a"]
输出：false
解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。

```
 **示例 2：** 

```
输入：["b==a","a==b"]
输出：true
解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。

```
 **示例 3：** 

```
输入：["a==b","b==c","a==c"]
输出：true

```
 **示例 4：** 

```
输入：["a==b","b!=c","c==a"]
输出：false

```
 **示例 5：** 

```
输入：["c==c","b==d","x!=z"]
输出：true

```
 

 **提示：** 
-  `1 <= equations.length <= 500` 
-  `equations[i].length == 4` 
-  `equations[i][0]` 和 `equations[i][3]` 是小写字母
-  `equations[i][1]` 要么是 `';=';` ，要么是 `';!';` 
-  `equations[i][2]` 是 `';=';` 
 
**标签**
`并查集` `图` `数组` `字符串` 


## 
```python

```
>
# 991.坏了的计算器
[https://leetcode-cn.com/problems/broken-calculator](https://leetcode-cn.com/problems/broken-calculator) 
## 原题
在显示着数字 `startValue` 的坏计算器上，我们可以执行以下两种操作：
-  **双倍（Double）：** 将显示屏上的数字乘 2；
-  **递减（Decrement）：** 将显示屏上的数字减 `1` 。
给定两个整数 `startValue` 和 `target` 。返回显示数字 `target` 所需的最小操作数。

 

 **示例 1：** 

```

输入：startValue = 2, target = 3
输出：2
解释：先进行双倍运算，然后再进行递减运算 {2 -> 4 -> 3}.

```
 **示例 2：** 

```

输入：startValue = 5, target = 8
输出：2
解释：先递减，再双倍 {5 -> 4 -> 8}.

```
 **示例 3：** 

```

输入：startValue = 3, target = 10
输出：3
解释：先双倍，然后递减，再双倍 {3 -> 6 -> 5 -> 10}.

```
 

 **提示：** 
-  `1 <= x, y <= 10^9` 
 
**标签**
`贪心` `数学` 


## 
```python

```
>
# 992.K 个不同整数的子数组
[https://leetcode-cn.com/problems/subarrays-with-k-different-integers](https://leetcode-cn.com/problems/subarrays-with-k-different-integers) 
## 原题
给定一个正整数数组 `nums` 和一个整数 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">k</span></span></font></font> ，返回 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">num</span></span></font></font> 中 「 **好子数组」** 的数目。

如果 `nums` 的某个子数组中不同整数的个数恰好为 `k` ，则称 `nums` 的这个连续、不一定不同的子数组为 **「** **好子数组 」** 。
- 例如， `[1,2,3,1,2]` 中有 `3` 个不同的整数： `1` ， `2` ，以及 `3` 。
 **子数组** 是数组的 **连续** 部分。

 

 **示例 1：** 

```

输入：nums = [1,2,1,2,3], k = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

```
 **示例 2：** 

```

输入：nums = [1,2,1,3,4], k = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].

```
 

 **提示：** 
-  `1 <= nums.length <= 2 * 10^4` 
-  `1 <= nums[i], k <= nums.length` 
 
**标签**
`数组` `哈希表` `计数` `滑动窗口` 


## 
```python

```
>
# 993.二叉树的堂兄弟节点
[https://leetcode-cn.com/problems/cousins-in-binary-tree](https://leetcode-cn.com/problems/cousins-in-binary-tree) 
## 原题
在二叉树中，根节点位于深度 `0` 处，每个深度为 `k` 的节点的子节点位于深度 `k+1` 处。

如果二叉树的两个节点深度相同，但 **父节点不同** ，则它们是一对 *堂兄弟节点* 。

我们给出了具有唯一值的二叉树的根节点 `root` ，以及树中两个不同节点的值 `x` 和 `y` 。

只有与值 `x` 和 `y` 对应的节点是堂兄弟节点时，才返回 `true` 。否则，返回 `false` 。

 

 **示例 1：<br />
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-01.png" style="height: 160px; width: 180px;" />** 

```

输入：root = [1,2,3,4], x = 4, y = 3
输出：false

```
 **示例 2：<br />
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-02.png" style="height: 160px; width: 201px;" />** 

```

输入：root = [1,2,3,null,4,null,5], x = 5, y = 4
输出：true

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/q1248-03.png" style="height: 160px; width: 156px;" />** 

```

输入：root = [1,2,3,null,4], x = 2, y = 3
输出：false
```
 

 **提示：** 
- 二叉树的节点数介于  `2` 到  `100`  之间。
- 每个节点的值都是唯一的、范围为  `1` 到  `100`  的整数。
 

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 994.腐烂的橘子
[https://leetcode-cn.com/problems/rotting-oranges](https://leetcode-cn.com/problems/rotting-oranges) 
## 原题
在给定的 `m x n` 网格<meta charset="UTF-8" /> `grid` 中，每个单元格可以有以下三个值之一：
- 值 `0` 代表空单元格；
- 值 `1` 代表新鲜橘子；
- 值 `2` 代表腐烂的橘子。
每分钟，腐烂的橘子 **周围 4 个方向上相邻** 的新鲜橘子都会腐烂。

返回 *直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 `-1`* 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/16/oranges.png" style="height: 137px; width: 650px;" />** 

```

输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4

```
 **示例 2：** 

```

输入：grid = [[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。

```
 **示例 3：** 

```

输入：grid = [[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 10` 
-  `grid[i][j]` 仅为 `0` 、 `1` 或 `2` 
 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 995.K 连续位的最小翻转次数
[https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips](https://leetcode-cn.com/problems/minimum-number-of-k-consecutive-bit-flips) 
## 原题
给定一个二进制数组 `nums` 和一个整数 `k` 。

 **k位翻转** 就是从 `nums` 中选择一个长度为 `k` 的 **子数组** ，同时把子数组中的每一个 `0` 都改成 `1` ，把子数组中的每一个 `1` 都改成 `0` 。

返回数组中不存在 `0` 所需的最小 **k位翻转** 次数。如果不可能，则返回 `-1` 。

 **子数组** 是数组的 **连续** 部分。

 

 **示例 1：** 

```

输入：nums = [0,1,0], K = 1
输出：2
解释：先翻转 A[0]，然后翻转 A[2]。

```
 **示例 2：** 

```

输入：nums = [1,1,0], K = 2
输出：-1
解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。

```
 **示例 3：** 

```

输入：nums = [0,0,0,1,0,1,1,0], K = 3
输出：3
解释：
翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= k <= nums.length` 
 
**标签**
`位运算` `数组` `前缀和` `滑动窗口` 


## 
```python

```
>
# 996.正方形数组的数目
[https://leetcode-cn.com/problems/number-of-squareful-arrays](https://leetcode-cn.com/problems/number-of-squareful-arrays) 
## 原题
给定一个非负整数数组 `A` ，如果该数组每对相邻元素之和是一个完全平方数，则称这一数组为 *正方形* 数组。

返回 A 的正方形排列的数目。两个排列 `A1` 和 `A2` 不同的充要条件是存在某个索引 `i` ，使得 A1[i] != A2[i]。

 

 **示例 1：** 

```
输入：[1,17,8]
输出：2
解释：
[1,8,17] 和 [17,8,1] 都是有效的排列。

```
 **示例 2：** 

```
输入：[2,2,2]
输出：1

```
 

 **提示：** 
-  `1 <= A.length <= 12` 
-  `0 <= A[i] <= 1e9` 
 
**标签**
`位运算` `数组` `数学` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 997.找到小镇的法官
[https://leetcode-cn.com/problems/find-the-town-judge](https://leetcode-cn.com/problems/find-the-town-judge) 
## 原题
小镇里有 `n` 个人，按从 `1` 到 `n` 的顺序编号。传言称，这些人中有一个暗地里是小镇法官。

如果小镇法官真的存在，那么：
- 小镇法官不会信任任何人。
- 每个人（除了小镇法官）都信任这位小镇法官。
- 只有一个人同时满足属性 **1** 和属性 **2** 。
给你一个数组 `trust` ，其中 `trust[i] = [a<sub>i</sub>, b<sub>i</sub>]` 表示编号为 `a<sub>i</sub>` 的人信任编号为 `b<sub>i</sub>` 的人。

如果小镇法官存在并且可以确定他的身份，请返回该法官的编号；否则，返回 `-1` 。

 

 **示例 1：** 

```

输入：n = 2, trust = [[1,2]]
输出：2

```
 **示例 2：** 

```

输入：n = 3, trust = [[1,3],[2,3]]
输出：3

```
 **示例 3：** 

```

输入：n = 3, trust = [[1,3],[2,3],[3,1]]
输出：-1

```

 

 **提示：** 
-  `1 <= n <= 1000` 
-  `0 <= trust.length <= 10^4` 
-  `trust[i].length == 2` 
-  `trust` 中的所有 `trust[i] = [a<sub>i</sub>, b<sub>i</sub>]` **互不相同** 
-  `a<sub>i</sub> != b<sub>i</sub>` 
-  `1 <= a<sub>i</sub>, b<sub>i</sub> <= n` 
 
**标签**
`图` `数组` `哈希表` 


## 
```python

```
>
# 998.最大二叉树 II
[https://leetcode-cn.com/problems/maximum-binary-tree-ii](https://leetcode-cn.com/problems/maximum-binary-tree-ii) 
## 原题
最大树定义：一个树，其中每个节点的值都大于其子树中的任何其他值。

给出最大树的根节点 `root` 。

就像<a href="https://leetcode-cn.com/problems/maximum-binary-tree/">之前的问题</a>那样，给定的树是从列表  `A` （ `root = Construct(A)` ）递归地使用下述  `Construct(A)`  例程构造的：
- 如果  `A`  为空，返回  `null` 
- 否则，令  `A[i]`  作为 A 的最大元素。创建一个值为  `A[i]`  的根节点 `root` 
-  `root`  的左子树将被构建为  `Construct([A[0], A[1], ..., A[i-1]])` 
-  `root`  的右子树将被构建为 `Construct([A[i+1], A[i+2], ..., A[A.length - 1]])` 
- 返回  `root` 
请注意，我们没有直接给定 A，只有一个根节点  `root = Construct(A)` .

假设 `B` 是 `A` 的副本，并在末尾附加值 `val` 。题目数据保证 `B`  中的值是不同的。

返回  `Construct(B)` 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-1-1.png" style="height: 160px; width: 159px;" /><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-1-2.png" style="height: 160px; width: 169px;" />** 

```

输入：root = [4,1,3,null,null,2], val = 5
输出：[5,4,null,1,3,null,null,2]
解释：A = [1,4,2,3], B = [1,4,2,3,5]

```
 **示例 2：<br />
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-2-1.png" style="height: 160px; width: 180px;" /><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-2-2.png" style="height: 160px; width: 214px;" />** 

```

输入：root = [5,2,4,null,1], val = 3
输出：[5,2,4,null,1,null,3]
解释：A = [2,1,5,4], B = [2,1,5,4,3]

```
 **示例 3：<br />
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-3-1.png" style="height: 160px; width: 180px;" /><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/maximum-binary-tree-3-2.png" style="height: 160px; width: 201px;" />** 

```

输入：root = [5,2,3,null,1], val = 4
输出：[5,2,4,null,1,3]
解释：A = [2,1,5,3], B = [2,1,5,3,4]

```
 

 **提示：** 
-  `1 <= B.length <= 100` 
 

 

 
**标签**
`树` `二叉树` 


## 
```python

```
>
# 999.可以被一步捕获的棋子数
[https://leetcode-cn.com/problems/available-captures-for-rook](https://leetcode-cn.com/problems/available-captures-for-rook) 
## 原题
在一个 8 x 8 的棋盘上，有一个白色的车（ `Rook` ），用字符 `';R';` 表示。棋盘上还可能存在空方块，白色的象（ `Bishop` ）以及黑色的卒（ `pawn` ），分别用字符 `';.';` ， `';B';` 和 `';p';` 表示。不难看出，大写字符表示的是白棋，小写字符表示的是黑棋。

车按国际象棋中的规则移动。东，西，南，北四个基本方向任选其一，然后一直向选定的方向移动，直到满足下列四个条件之一：
- 棋手选择主动停下来。
- 棋子因到达棋盘的边缘而停下。
- 棋子移动到某一方格来捕获位于该方格上敌方（黑色）的卒，停在该方格内。
- 车不能进入/越过已经放有其他友方棋子（白色的象）的方格，停在友方棋子前。
你现在可以控制车移动一次，请你统计有多少敌方的卒处于你的捕获范围内（即，可以被一步捕获的棋子数）。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_1_improved.PNG" style="height: 305px; width: 300px;">

```
输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
输出：3
解释：
在本例中，车能够捕获所有的卒。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_2_improved.PNG" style="height: 306px; width: 300px;">

```
输入：[[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
输出：0
解释：
象阻止了车捕获任何卒。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/23/1253_example_3_improved.PNG" style="height: 305px; width: 300px;">

```
输入：[[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
输出：3
解释： 
车可以捕获位置 b5，d6 和 f5 的卒。

```
 

 **提示：** 
-  `board.length == board[i].length == 8` 
-  `board[i][j]` 可以是 `';R';` ， `';.';` ， `';B';` 或 `';p';` 
- 只有一个格子上存在 `board[i][j] == ';R';` 
 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 1000.合并石头的最低成本
[https://leetcode-cn.com/problems/minimum-cost-to-merge-stones](https://leetcode-cn.com/problems/minimum-cost-to-merge-stones) 
## 原题
有 `N` 堆石头排成一排，第 `i` 堆中有 `stones[i]` 块石头。

每次 *移动（move）* 需要将 **连续的** `K` 堆石头合并为一堆，而这个移动的成本为这 `K` 堆石头的总数。

找出把所有石头合并成一堆的最低成本。如果不可能，返回 `-1` 。

 

 **示例 1：** 

```
输入：stones = [3,2,4,1], K = 2
输出：20
解释：
从 [3, 2, 4, 1] 开始。
合并 [3, 2]，成本为 5，剩下 [5, 4, 1]。
合并 [4, 1]，成本为 5，剩下 [5, 5]。
合并 [5, 5]，成本为 10，剩下 [10]。
总成本 20，这是可能的最小值。

```
 **示例 2：** 

```
输入：stones = [3,2,4,1], K = 3
输出：-1
解释：任何合并操作后，都会剩下 2 堆，我们无法再进行合并。所以这项任务是不可能完成的。.

```
 **示例 3：** 

```
输入：stones = [3,5,1,2,6], K = 3
输出：25
解释：
从 [3, 5, 1, 2, 6] 开始。
合并 [5, 1, 2]，成本为 8，剩下 [3, 8, 6]。
合并 [3, 8, 6]，成本为 17，剩下 [17]。
总成本 25，这是可能的最小值。

```
 

 **提示：** 
-  `1 <= stones.length <= 30` 
-  `2 <= K <= 30` 
-  `1 <= stones[i] <= 100` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
