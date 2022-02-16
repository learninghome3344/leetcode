# 1501.可以放心投资的国家
[https://leetcode-cn.com/problems/countries-you-can-safely-invest-in](https://leetcode-cn.com/problems/countries-you-can-safely-invest-in) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1502.判断能否形成等差数列
[https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence](https://leetcode-cn.com/problems/can-make-arithmetic-progression-from-sequence) 
## 原题
给你一个数字数组 `arr` 。

如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 **等差数列** 。

如果可以重新排列数组形成等差数列，请返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```
输入：arr = [3,5,1]
输出：true
解释：对数组重新排序得到 [1,3,5] 或者 [5,3,1] ，任意相邻两项的差分别为 2 或 -2 ，可以形成等差数列。

```
 **示例 2：** 

```
输入：arr = [1,2,4]
输出：false
解释：无法通过重新排序得到等差数列。

```
 

 **提示：** 
-  `2 <= arr.length <= 1000` 
-  `-10^6 <= arr[i] <= 10^6` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 1503.所有蚂蚁掉下来前的最后一刻
[https://leetcode-cn.com/problems/last-moment-before-all-ants-fall-out-of-a-plank](https://leetcode-cn.com/problems/last-moment-before-all-ants-fall-out-of-a-plank) 
## 原题
有一块木板，长度为 `n` 个 **单位** 。一些蚂蚁在木板上移动，每只蚂蚁都以 **每秒一个单位** 的速度移动。其中，一部分蚂蚁向 **左** 移动，其他蚂蚁向 **右** 移动。

当两只向 **不同** 方向移动的蚂蚁在某个点相遇时，它们会同时改变移动方向并继续移动。假设更改方向不会花费任何额外时间。

而当蚂蚁在某一时刻 `t` 到达木板的一端时，它立即从木板上掉下来。

给你一个整数 `n` 和两个整数数组 `left` 以及 `right` 。两个数组分别标识向左或者向右移动的蚂蚁在 `t = 0` 时的位置。请你返回最后一只蚂蚁从木板上掉下来的时刻。

 

 **示例 1：** 

 

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/17/ants.jpg" style="height: 610px; width: 450px;">

```
输入：n = 4, left = [4,3], right = [0,1]
输出：4
解释：如上图所示：
-下标 0 处的蚂蚁命名为 A 并向右移动。
-下标 1 处的蚂蚁命名为 B 并向右移动。
-下标 3 处的蚂蚁命名为 C 并向左移动。
-下标 4 处的蚂蚁命名为 D 并向左移动。
请注意，蚂蚁在木板上的最后时刻是 t = 4 秒，之后蚂蚁立即从木板上掉下来。（也就是说在 t = 4.0000000001 时，木板上没有蚂蚁）。
```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/17/ants2.jpg" style="height: 101px; width: 639px;">

```
输入：n = 7, left = [], right = [0,1,2,3,4,5,6,7]
输出：7
解释：所有蚂蚁都向右移动，下标为 0 的蚂蚁需要 7 秒才能从木板上掉落。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/17/ants3.jpg" style="height: 100px; width: 639px;">

```
输入：n = 7, left = [0,1,2,3,4,5,6,7], right = []
输出：7
解释：所有蚂蚁都向左移动，下标为 7 的蚂蚁需要 7 秒才能从木板上掉落。

```
 **示例 4：** 

```
输入：n = 9, left = [5], right = [4]
输出：5
解释：t = 1 秒时，两只蚂蚁将回到初始位置，但移动方向与之前相反。

```
 **示例 5：** 

```
输入：n = 6, left = [6], right = [0]
输出：6

```
 

 **提示：** 
-  `1 <= n <= 10^4` 
-  `0 <= left.length <= n + 1` 
-  `0 <= left[i] <= n` 
-  `0 <= right.length <= n + 1` 
-  `0 <= right[i] <= n` 
-  `1 <= left.length + right.length <= n + 1` 
-  `left` 和 `right` 中的所有值都是唯一的，并且每个值 **只能出现在二者之一** 中。
 
**标签**
`脑筋急转弯` `数组` `模拟` 


## 
```python

```
>
# 1504.统计全 1 子矩形
[https://leetcode-cn.com/problems/count-submatrices-with-all-ones](https://leetcode-cn.com/problems/count-submatrices-with-all-ones) 
## 原题
给你一个只包含 0 和 1 的 `rows * columns` 矩阵 `mat` ，请你返回有多少个 **子矩形** 的元素全部都是 1 。

 

 **示例 1：** 

```

输入：mat = [[1,0,1],
            [1,1,0],
            [1,1,0]]
输出：13
解释：
有 6 个 1x1 的矩形。
有 2 个 1x2 的矩形。
有 3 个 2x1 的矩形。
有 1 个 2x2 的矩形。
有 1 个 3x1 的矩形。
矩形数目总共 = 6 + 2 + 3 + 1 + 1 = 13 。

```
 **示例 2：** 

```

输入：mat = [[0,1,1,0],
            [0,1,1,1],
            [1,1,1,0]]
输出：24
解释：
有 8 个 1x1 的子矩形。
有 5 个 1x2 的子矩形。
有 2 个 1x3 的子矩形。
有 4 个 2x1 的子矩形。
有 2 个 2x2 的子矩形。
有 2 个 3x1 的子矩形。
有 1 个 3x2 的子矩形。
矩形数目总共 = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24 。

```
 **示例 3：** 

```

输入：mat = [[1,1,1,1,1,1]]
输出：21

```
 **示例 4：** 

```

输入：mat = [[1,0,1],[0,1,0],[1,0,1]]
输出：5

```
 

 **提示：** 
-  `1 <= rows <= 150` 
-  `1 <= columns <= 150` 
-  `0 <= mat[i][j] <= 1` 
 
**标签**
`栈` `数组` `动态规划` `矩阵` `单调栈` 


## 
```python

```
>
# 1505.最多 K 次交换相邻数位后得到的最小整数
[https://leetcode-cn.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits](https://leetcode-cn.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits) 
## 原题
给你一个字符串 `num` 和一个整数 `k` 。其中， `num` 表示一个很大的整数，字符串中的每个字符依次对应整数上的各个 **数位** 。

你可以交换这个整数相邻数位的数字 **最多** `k` 次。

请你返回你能得到的最小整数，并以字符串形式返回。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/06/17/q4_1.jpg" style="height:40px; width:500px" />

```

输入：num = "4321", k = 4
输出："1342"
解释：4321 通过 4 次交换相邻数位得到最小整数的步骤如上图所示。

```
 **示例 2：** 

```

输入：num = "100", k = 1
输出："010"
解释：输出可以包含前导 0 ，但输入保证不会有前导 0 。

```
 **示例 3：** 

```

输入：num = "36789", k = 1000
输出："36789"
解释：不需要做任何交换。

```
 **示例 4：** 

```

输入：num = "22", k = 22
输出："22"

```
 **示例 5：** 

```

输入：num = "9438957234785635408", k = 23
输出："0345989723478563548"

```
 

 **提示：** 
-  `1 <= num.length <= 30000` 
-  `num` 只包含 **数字** 且不含有 **前导 0** 。
-  `1 <= k <= 10^9` 
 
**标签**
`贪心` `树状数组` `线段树` `字符串` 


## 
```python

```
>
# 1506.找到 N 叉树的根节点
[https://leetcode-cn.com/problems/find-root-of-n-ary-tree](https://leetcode-cn.com/problems/find-root-of-n-ary-tree) 
## 原题

 
**标签**
`位运算` `树` `深度优先搜索` `哈希表` 


## 
```python

```
>
# 1507.转变日期格式
[https://leetcode-cn.com/problems/reformat-date](https://leetcode-cn.com/problems/reformat-date) 
## 原题
给你一个字符串 `date` ，它的格式为 `Day Month Year` ，其中：
-  `Day` 是集合 `{"1st", "2nd", "3rd", "4th", ..., "30th", "31st"}` 中的一个元素。
-  `Month` 是集合 `{"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}` 中的一个元素。
-  `Year` 的范围在 ​ `[1900, 2100]` 之间。
请你将字符串转变为 `YYYY-MM-DD` 的格式，其中：
-  `YYYY` 表示 4 位的年份。
-  `MM` 表示 2 位的月份。
-  `DD` 表示 2 位的天数。
 

 **示例 1：** 

```
输入：date = "20th Oct 2052"
输出："2052-10-20"

```
 **示例 2：** 

```
输入：date = "6th Jun 1933"
输出："1933-06-06"

```
 **示例 3：** 

```
输入：date = "26th May 1960"
输出："1960-05-26"

```
 

 **提示：** 
- 给定日期保证是合法的，所以不需要处理异常输入。
 
**标签**
`字符串` 


## 
```python

```
>
# 1508.子数组和排序后的区间和
[https://leetcode-cn.com/problems/range-sum-of-sorted-subarray-sums](https://leetcode-cn.com/problems/range-sum-of-sorted-subarray-sums) 
## 原题
给你一个数组 `nums` ，它包含 `n` 个正整数。你需要计算所有非空连续子数组的和，并将它们按升序排序，得到一个新的包含 `n * (n + 1) / 2` 个数字的数组。

请你返回在新数组中下标为 `left` 到 `right` **（下标从 1 开始）** 的所有数字和（包括左右端点）。由于答案可能很大，请你将它对 10^9 + 7 取模后返回。

 

 **示例 1：** 

```

输入：nums = [1,2,3,4], n = 4, left = 1, right = 5
输出：13 
解释：所有的子数组和为 1, 3, 6, 10, 2, 5, 9, 3, 7, 4 。将它们升序排序后，我们得到新的数组 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 1 到 ri = 5 的和为 1 + 2 + 3 + 3 + 4 = 13 。

```
 **示例 2：** 

```

输入：nums = [1,2,3,4], n = 4, left = 3, right = 4
输出：6
解释：给定数组与示例 1 一样，所以新数组为 [1, 2, 3, 3, 4, 5, 6, 7, 9, 10] 。下标从 le = 3 到 ri = 4 的和为 3 + 3 = 6 。

```
 **示例 3：** 

```

输入：nums = [1,2,3,4], n = 4, left = 1, right = 10
输出：50

```
 

 **提示：** 
-  `1 <= nums.length <= 10^3` 
-  `nums.length == n` 
-  `1 <= nums[i] <= 100` 
-  `1 <= left <= right <= n * (n + 1) / 2` 
 
**标签**
`数组` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 1509.三次操作后最大值与最小值的最小差
[https://leetcode-cn.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves](https://leetcode-cn.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves) 
## 原题
给你一个数组 `nums` ，每次操作你可以选择 `nums` 中的任意一个元素并将它改成任意值。

请你返回三次操作后， `nums` 中最大值与最小值的差的最小值。

 

 **示例 1：** 

```
输入：nums = [5,3,2,4]
输出：0
解释：将数组 [5,3,2,4] 变成 [2,2,2,2].
最大值与最小值的差为 2-2 = 0 。
```
 **示例 2：** 

```
输入：nums = [1,5,0,10,14]
输出：1
解释：将数组 [1,5,0,10,14] 变成 [1,1,0,1,1] 。
最大值与最小值的差为 1-0 = 1 。

```
 **示例 3：** 

```
输入：nums = [6,6,0,1,1,4,6]
输出：2

```
 **示例 4：** 

```
输入：nums = [1,5,6,14,15]
输出：1

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-10^9 <= nums[i] <= 10^9` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1510.石子游戏 IV
[https://leetcode-cn.com/problems/stone-game-iv](https://leetcode-cn.com/problems/stone-game-iv) 
## 原题
Alice 和 Bob 两个人轮流玩一个游戏，Alice 先手。

一开始，有 `n` 个石子堆在一起。每个人轮流操作，正在操作的玩家可以从石子堆里拿走 **任意** 非零 **平方数** 个石子。

如果石子堆里没有石子了，则无法操作的玩家输掉游戏。

给你正整数 `n` ，且已知两个人都采取最优策略。如果 Alice 会赢得比赛，那么返回 `True` ，否则返回 `False` 。

 

 **示例 1：** 

```

输入：n = 1
输出：true
解释：Alice 拿走 1 个石子并赢得胜利，因为 Bob 无法进行任何操作。
```
 **示例 2：** 

```

输入：n = 2
输出：false
解释：Alice 只能拿走 1 个石子，然后 Bob 拿走最后一个石子并赢得胜利（2 -> 1 -> 0）。
```
 **示例 3：** 

```

输入：n = 4
输出：true
解释：n 已经是一个平方数，Alice 可以一次全拿掉 4 个石子并赢得胜利（4 -> 0）。

```
 **示例 4：** 

```

输入：n = 7
输出：false
解释：当 Bob 采取最优策略时，Alice 无法赢得比赛。
如果 Alice 一开始拿走 4 个石子， Bob 会拿走 1 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7 -> 3 -> 2 -> 1 -> 0）。
如果 Alice 一开始拿走 1 个石子， Bob 会拿走 4 个石子，然后 Alice 只能拿走 1 个石子，Bob 拿走最后一个石子并赢得胜利（7 -> 6 -> 2 -> 1 -> 0）。
```
 **示例 5：** 

```

输入：n = 17
输出：false
解释：如果 Bob 采取最优策略，Alice 无法赢得胜利。

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
 
**标签**
`数学` `动态规划` `博弈` 


## 
```python

```
>
# 1511.消费者下单频率
[https://leetcode-cn.com/problems/customer-order-frequency](https://leetcode-cn.com/problems/customer-order-frequency) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1512.好数对的数目
[https://leetcode-cn.com/problems/number-of-good-pairs](https://leetcode-cn.com/problems/number-of-good-pairs) 
## 原题
给你一个整数数组 `nums` 。

如果一组数字 `(i,j)` 满足 `nums[i]` == `nums[j]` 且 `i` < `j` ，就可以认为这是一组 **好数对** 。

返回好数对的数目。

 

 **示例 1：** 

```
输入：nums = [1,2,3,1,1,3]
输出：4
解释：有 4 组好数对，分别是 (0,3), (0,4), (3,4), (2,5) ，下标从 0 开始

```
 **示例 2：** 

```
输入：nums = [1,1,1,1]
输出：6
解释：数组中的每组数字都是好数对
```
 **示例 3：** 

```
输入：nums = [1,2,3]
输出：0

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `1 <= nums[i] <= 100` 
 
**标签**
`数组` `哈希表` `数学` `计数` 


## 
```python

```
>
# 1513.仅含 1 的子串数
[https://leetcode-cn.com/problems/number-of-substrings-with-only-1s](https://leetcode-cn.com/problems/number-of-substrings-with-only-1s) 
## 原题
给你一个二进制字符串 `s` （仅由 ';0'; 和 ';1'; 组成的字符串）。

返回所有字符都为 1 的子字符串的数目。

由于答案可能很大，请你将它对 10^9 + 7 取模后返回。

 

 **示例 1：** 

```
输入：s = "0110111"
输出：9
解释：共有 9 个子字符串仅由 ';1'; 组成
"1" -> 5 次
"11" -> 3 次
"111" -> 1 次
```
 **示例 2：** 

```
输入：s = "101"
输出：2
解释：子字符串 "1" 在 s 中共出现 2 次

```
 **示例 3：** 

```
输入：s = "111111"
输出：21
解释：每个子字符串都仅由 ';1'; 组成

```
 **示例 4：** 

```
输入：s = "000"
输出：0

```
 

 **提示：** 
-  `s[i] == ';0';` 或 `s[i] == ';1';` 
-  `1 <= s.length <= 10^5` 
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 1514.概率最大的路径
[https://leetcode-cn.com/problems/path-with-maximum-probability](https://leetcode-cn.com/problems/path-with-maximum-probability) 
## 原题
给你一个由 `n` 个节点（下标从 0 开始）组成的无向加权图，该图由一个描述边的列表组成，其中 `edges[i] = [a, b]` 表示连接节点 a 和 b 的一条无向边，且该边遍历成功的概率为 `succProb[i]` 。

指定两个节点分别作为起点 `start` 和终点 `end` ，请你找出从起点到终点成功概率最大的路径，并返回其成功概率。

如果不存在从 `start` 到 `end` 的路径，请 **返回 0** 。只要答案与标准答案的误差不超过 **1e-5** ，就会被视作正确答案。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/1558_ex1.png" style="height: 186px; width: 187px;">** 

```
输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.2], start = 0, end = 2
输出：0.25000
解释：从起点到终点有两条路径，其中一条的成功概率为 0.2 ，而另一条为 0.5 * 0.5 = 0.25

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/1558_ex2.png" style="height: 186px; width: 189px;">** 

```
输入：n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start = 0, end = 2
输出：0.30000

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/1558_ex3.png" style="height: 191px; width: 215px;">** 

```
输入：n = 3, edges = [[0,1]], succProb = [0.5], start = 0, end = 2
输出：0.00000
解释：节点 0 和 节点 2 之间不存在路径

```
 

 **提示：** 
-  `2 <= n <= 10^4` 
-  `0 <= start, end < n` 
-  `start != end` 
-  `0 <= a, b < n` 
-  `a != b` 
-  `0 <= succProb.length == edges.length <= 2*10^4` 
-  `0 <= succProb[i] <= 1` 
- 每两个节点之间最多有一条边
 
**标签**
`图` `最短路` `堆（优先队列）` 


## 
```python

```
>
# 1515.服务中心的最佳位置
[https://leetcode-cn.com/problems/best-position-for-a-service-centre](https://leetcode-cn.com/problems/best-position-for-a-service-centre) 
## 原题
一家快递公司希望在新城市建立新的服务中心。公司统计了该城市所有客户在二维地图上的坐标，并希望能够以此为依据为新的服务中心选址：使服务中心 **到所有客户的欧几里得距离的总和最小** 。

给你一个数组 `positions` ，其中 `positions[i] = [x<sub>i</sub>, y<sub>i</sub>]` 表示第 `i` 个客户在二维地图上的位置，返回到所有客户的 **欧几里得距离的最小总和 。** 

换句话说，请你为服务中心选址，该位置的坐标 `[x<sub>centre</sub>, y<sub>centre</sub>]` 需要使下面的公式取到最小值：

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/q4_edited.jpg" />

与真实值误差在 `10^-5` 之内的答案将被视作正确答案。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/q4_e1.jpg" />

```

输入：positions = [[0,1],[1,0],[1,2],[2,1]]
输出：4.00000
解释：如图所示，你可以选 [xcentre, ycentre] = [1, 1] 作为新中心的位置，这样一来到每个客户的距离就都是 1，所有距离之和为 4 ，这也是可以找到的最小值。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/12/q4_e3.jpg" />

```

输入：positions = [[1,1],[3,3]]
输出：2.82843
解释：欧几里得距离可能的最小总和为 sqrt(2) + sqrt(2) = 2.82843

```
 

 **提示：** 
-  `1 <= positions.length <= 50` 
-  `positions[i].length == 2` 
-  `0 <= x<sub>i</sub>, y<sub>i</sub> <= 100` 
 
**标签**
`几何` `数学` `随机化` 


## 
```python

```
>
# 1516.移动 N 叉树的子树
[https://leetcode-cn.com/problems/move-sub-tree-of-n-ary-tree](https://leetcode-cn.com/problems/move-sub-tree-of-n-ary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` 


## 
```python

```
>
# 1517.查找拥有有效邮箱的用户
[https://leetcode-cn.com/problems/find-users-with-valid-e-mails](https://leetcode-cn.com/problems/find-users-with-valid-e-mails) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1518.换酒问题
[https://leetcode-cn.com/problems/water-bottles](https://leetcode-cn.com/problems/water-bottles) 
## 原题
小区便利店正在促销，用 `numExchange` 个空酒瓶可以兑换一瓶新酒。你购入了 `numBottles` 瓶酒。

如果喝掉了酒瓶中的酒，那么酒瓶就会变成空的。

请你计算 **最多** 能喝到多少瓶酒。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/sample_1_1875.png" style="height: 240px; width: 480px;">** 

```
输入：numBottles = 9, numExchange = 3
输出：13
解释：你可以用 3 个空酒瓶兑换 1 瓶酒。
所以最多能喝到 9 + 3 + 1 = 13 瓶酒。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/sample_2_1875.png" style="height: 240px; width: 790px;">

```
输入：numBottles = 15, numExchange = 4
输出：19
解释：你可以用 4 个空酒瓶兑换 1 瓶酒。
所以最多能喝到 15 + 3 + 1 = 19 瓶酒。

```
 **示例 3：** 

```
输入：numBottles = 5, numExchange = 5
输出：6

```
 **示例 4：** 

```
输入：numBottles = 2, numExchange = 3
输出：2

```
 

 **提示：** 
-  `1 <= numBottles <= 100` 
-  `2 <= numExchange <= 100` 
 
**标签**
`数学` `模拟` 


## 
```python

```
>
# 1519.子树中标签相同的节点数
[https://leetcode-cn.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label](https://leetcode-cn.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label) 
## 原题
给你一棵树（即，一个连通的无环无向图），这棵树由编号从 `0` 到 `n - 1` 的 n 个节点组成，且恰好有 `n - 1` 条 `edges` 。树的根节点为节点 `0` ，树上的每一个节点都有一个标签，也就是字符串 `labels` 中的一个小写字符（编号为 `i` 的 节点的标签就是 `labels[i]` ）

边数组 `edges` 以 `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]` 的形式给出，该格式表示节点 `a<sub>i</sub>` 和 `b<sub>i</sub>` 之间存在一条边。

返回一个大小为 *`n`* 的数组，其中 `ans[i]` 表示第 `i` 个节点的子树中与节点 `i` 标签相同的节点数。

树 `T` 中的子树是由 `T` 中的某个节点及其所有后代节点组成的树。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/q3e1.jpg" style="height: 321px; width: 441px;">

```
输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
输出：[2,1,1,1,1,1,1]
解释：节点 0 的标签为 ';a'; ，以 ';a'; 为根节点的子树中，节点 2 的标签也是 ';a'; ，因此答案为 2 。注意树中的每个节点都是这棵子树的一部分。
节点 1 的标签为 ';b'; ，节点 1 的子树包含节点 1、4 和 5，但是节点 4、5 的标签与节点 1 不同，故而答案为 1（即，该节点本身）。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/q3e2.jpg" style="height: 321px; width: 381px;">

```
输入：n = 4, edges = [[0,1],[1,2],[0,3]], labels = "bbbb"
输出：[4,2,1,1]
解释：节点 2 的子树中只有节点 2 ，所以答案为 1 。
节点 3 的子树中只有节点 3 ，所以答案为 1 。
节点 1 的子树中包含节点 1 和 2 ，标签都是 ';b'; ，因此答案为 2 。
节点 0 的子树中包含节点 0、1、2 和 3，标签都是 ';b';，因此答案为 4 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/q3e3.jpg" style="height: 321px; width: 381px;">

```
输入：n = 5, edges = [[0,1],[0,2],[1,3],[0,4]], labels = "aabab"
输出：[3,2,1,1,1]

```
 **示例 4：** 

```
输入：n = 6, edges = [[0,1],[0,2],[1,3],[3,4],[4,5]], labels = "cbabaa"
输出：[1,2,1,1,2,1]

```
 **示例 5：** 

```
输入：n = 7, edges = [[0,1],[1,2],[2,3],[3,4],[4,5],[5,6]], labels = "aaabaaa"
输出：[6,5,4,1,3,2,1]

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `edges.length == n - 1` 
-  `edges[i].length == 2` 
-  `0 <= a<sub>i</sub>, b<sub>i</sub> < n` 
-  `a<sub>i</sub> != b<sub>i</sub>` 
-  `labels.length == n` 
-  `labels` 仅由小写英文字母组成
 
**标签**
`树` `深度优先搜索` `广度优先搜索` 


## 
```python

```
>
# 1520.最多的不重叠子字符串
[https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-substrings](https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-substrings) 
## 原题
给你一个只包含小写字母的字符串 `s` ，你需要找到 `s` 中最多数目的非空子字符串，满足如下条件：
- 这些字符串之间互不重叠，也就是说对于任意两个子字符串 `s[i..j]` 和 `s[k..l]` ，要么 `j < k` 要么 `i > l` 。
- 如果一个子字符串包含字符 `char` ，那么 `s` 中所有 `char` 字符都应该在这个子字符串中。
请你找到满足上述条件的最多子字符串数目。如果有多个解法有相同的子字符串数目，请返回这些子字符串总长度最小的一个解。可以证明最小总长度解是唯一的。

请注意，你可以以 **任意** 顺序返回最优解的子字符串。

 

 **示例 1：** 

```
输入：s = "adefaddaccc"
输出：["e","f","ccc"]
解释：下面为所有满足第二个条件的子字符串：
[
  "adefaddaccc"
  "adefadda",
  "ef",
  "e",
  "f",
  "ccc",
]
如果我们选择第一个字符串，那么我们无法再选择其他任何字符串，所以答案为 1 。如果我们选择 "adefadda" ，剩下子字符串中我们只可以选择 "ccc" ，它是唯一不重叠的子字符串，所以答案为 2 。同时我们可以发现，选择 "ef" 不是最优的，因为它可以被拆分成 2 个子字符串。所以最优解是选择 ["e","f","ccc"] ，答案为 3 。不存在别的相同数目子字符串解。

```
 **示例 2：** 

```
输入：s = "abbaccd"
输出：["d","bb","cc"]
解释：注意到解 ["d","abba","cc"] 答案也为 3 ，但它不是最优解，因为它的总长度更长。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s` 只包含小写英文字母。
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 1521.找到最接近目标值的函数值
[https://leetcode-cn.com/problems/find-a-value-of-a-mysterious-function-closest-to-target](https://leetcode-cn.com/problems/find-a-value-of-a-mysterious-function-closest-to-target) 
## 原题
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/19/change.png" style="height: 312px; width: 635px;">

Winston 构造了一个如上所示的函数 `func` 。他有一个整数数组 `arr` 和一个整数 `target` ，他想找到让 `|func(arr, l, r) - target|` 最小的 `l` 和 `r` 。

请你返回 `|func(arr, l, r) - target|` 的最小值。

请注意， `func` 的输入参数 `l` 和 `r` 需要满足 `0 <= l, r < arr.length` 。

 

 **示例 1：** 

```
输入：arr = [9,12,3,7,15], target = 5
输出：2
解释：所有可能的 [l,r] 数对包括 [[0,0],[1,1],[2,2],[3,3],[4,4],[0,1],[1,2],[2,3],[3,4],[0,2],[1,3],[2,4],[0,3],[1,4],[0,4]]， Winston 得到的相应结果为 [9,12,3,7,15,8,0,3,7,0,0,3,0,0,0] 。最接近 5 的值是 7 和 3，所以最小差值为 2 。

```
 **示例 2：** 

```
输入：arr = [1000000,1000000,1000000], target = 1
输出：999999
解释：Winston 输入函数的所有可能 [l,r] 数对得到的函数值都为 1000000 ，所以最小差值为 999999 。

```
 **示例 3：** 

```
输入：arr = [1,2,4,8,16], target = 0
输出：0

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `1 <= arr[i] <= 10^6` 
-  `0 <= target <= 10^7` 
 
**标签**
`位运算` `线段树` `数组` `二分查找` 


## 
```python

```
>
# 1522.N 叉树的直径
[https://leetcode-cn.com/problems/diameter-of-n-ary-tree](https://leetcode-cn.com/problems/diameter-of-n-ary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` 


## 
```python

```
>
# 1523.在区间范围内统计奇数数目
[https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range](https://leetcode-cn.com/problems/count-odd-numbers-in-an-interval-range) 
## 原题
给你两个非负整数 `low` 和 `high` 。请你返回 `low` 和 `high` 之间（包括二者）奇数的数目。

 

 **示例 1：** 

```
输入：low = 3, high = 7
输出：3
解释：3 到 7 之间奇数数字为 [3,5,7] 。
```
 **示例 2：** 

```
输入：low = 8, high = 10
输出：1
解释：8 到 10 之间奇数数字为 [9] 。
```
 

 **提示：** 
-  `0 <= low <= high <= 10^9` 
 
**标签**
`数学` 


## 
```python

```
>
# 1524.和为奇数的子数组数目
[https://leetcode-cn.com/problems/number-of-sub-arrays-with-odd-sum](https://leetcode-cn.com/problems/number-of-sub-arrays-with-odd-sum) 
## 原题
给你一个整数数组 `arr` 。请你返回和为 **奇数** 的子数组数目。

由于答案可能会很大，请你将结果对 `10^9 + 7` 取余后返回。

 

 **示例 1：** 

```
输入：arr = [1,3,5]
输出：4
解释：所有的子数组为 [[1],[1,3],[1,3,5],[3],[3,5],[5]] 。
所有子数组的和为 [1,4,9,3,8,5].
奇数和包括 [1,9,3,5] ，所以答案为 4 。

```
 **示例 2 ：** 

```
输入：arr = [2,4,6]
输出：0
解释：所有子数组为 [[2],[2,4],[2,4,6],[4],[4,6],[6]] 。
所有子数组和为 [2,6,12,4,10,6] 。
所有子数组和都是偶数，所以答案为 0 。

```
 **示例 3：** 

```
输入：arr = [1,2,3,4,5,6,7]
输出：16

```
 **示例 4：** 

```
输入：arr = [100,100,99,99]
输出：4

```
 **示例 5：** 

```
输入：arr = [7]
输出：1

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `1 <= arr[i] <= 100` 
 
**标签**
`数组` `数学` `动态规划` `前缀和` 


## 
```python

```
>
# 1525.字符串的好分割数目
[https://leetcode-cn.com/problems/number-of-good-ways-to-split-a-string](https://leetcode-cn.com/problems/number-of-good-ways-to-split-a-string) 
## 原题
给你一个字符串 `s` ，一个分割被称为 「好分割」 当它满足：将 `s` 分割成 2 个字符串 `p` 和 `q` ，它们连接起来等于 `s` 且 `p` 和 `q` 中不同字符的数目相同。

请你返回 `s` 中好分割的数目。

 

 **示例 1：** 

```
输入：s = "aacaba"
输出：2
解释：总共有 5 种分割字符串 "aacaba" 的方法，其中 2 种是好分割。
("a", "acaba") 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
("aa", "caba") 左边字符串和右边字符串分别包含 1 个和 3 个不同的字符。
("aac", "aba") 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
("aaca", "ba") 左边字符串和右边字符串分别包含 2 个和 2 个不同的字符。这是一个好分割。
("aacab", "a") 左边字符串和右边字符串分别包含 3 个和 1 个不同的字符。

```
 **示例 2：** 

```
输入：s = "abcd"
输出：1
解释：好分割为将字符串分割成 ("ab", "cd") 。

```
 **示例 3：** 

```
输入：s = "aaaaa"
输出：4
解释：所有分割都是好分割。
```
 **示例 4：** 

```
输入：s = "acbadbaada"
输出：2

```
 

 **提示：** 
-  `s` 只包含小写英文字母。
-  `1 <= s.length <= 10^5` 
 
**标签**
`位运算` `字符串` `动态规划` 


## 
```python

```
>
# 1526.形成目标数组的子数组最少增加次数
[https://leetcode-cn.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array](https://leetcode-cn.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array) 
## 原题
给你一个整数数组 `target` 和一个数组 `initial` ， `initial` 数组与 `target` 数组有同样的维度，且一开始全部为 0 。

请你返回从 `initial` 得到 `target` 的最少操作次数，每次操作需遵循以下规则：
- 在 `initial` 中选择 **任意** 子数组，并将子数组中每个元素增加 1 。
答案保证在 32 位有符号整数以内。

 

 **示例 1：** 

```
输入：target = [1,2,3,2,1]
输出：3
解释：我们需要至少 3 次操作从 intial 数组得到 target 数组。
[0,0,0,0,0] 将下标为 0 到 4 的元素（包含二者）加 1 。
[1,1,1,1,1] 将下标为 1 到 3 的元素（包含二者）加 1 。
[1,2,2,2,1] 将下表为 2 的元素增加 1 。
[1,2,3,2,1] 得到了目标数组。

```
 **示例 2：** 

```
输入：target = [3,1,1,2]
输出：4
解释：(initial)[0,0,0,0] -> [1,1,1,1] -> [1,1,1,2] -> [2,1,1,2] -> [3,1,1,2] (target) 。

```
 **示例 3：** 

```
输入：target = [3,1,5,4,2]
输出：7
解释：(initial)[0,0,0,0,0] -> [1,1,1,1,1] -> [2,1,1,1,1] -> [3,1,1,1,1] 
                                  -> [3,1,2,2,2] -> [3,1,3,3,2] -> [3,1,4,4,2] -> [3,1,5,4,2] (target)。

```
 **示例 4：** 

```
输入：target = [1,1,1,1]
输出：1

```
 

 **提示：** 
-  `1 <= target.length <= 10^5` 
-  `1 <= target[i] <= 10^5` 
 
**标签**
`栈` `贪心` `数组` `动态规划` `单调栈` 


## 
```python

```
>
# 1527.患某种疾病的患者
[https://leetcode-cn.com/problems/patients-with-a-condition](https://leetcode-cn.com/problems/patients-with-a-condition) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1528.重新排列字符串
[https://leetcode-cn.com/problems/shuffle-string](https://leetcode-cn.com/problems/shuffle-string) 
## 原题
给你一个字符串 `s` 和一个 **长度相同** 的整数数组 `indices` 。

请你重新排列字符串 `s` ，其中第 `i` 个字符需要移动到 `indices[i]` 指示的位置。

返回重新排列后的字符串。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/26/q1.jpg" style="height: 243px; width: 321px;">

```
输入：s = "codeleet", indices = [4,5,6,7,0,2,1,3]
输出："leetcode"
解释：如图所示，"codeleet" 重新排列后变为 "leetcode" 。

```
 **示例 2：** 

```
输入：s = "abc", indices = [0,1,2]
输出："abc"
解释：重新排列后，每个字符都还留在原来的位置上。

```
 **示例 3：** 

```
输入：s = "aiohn", indices = [3,1,4,2,0]
输出："nihao"

```
 **示例 4：** 

```
输入：s = "aaiougrt", indices = [4,0,2,6,7,3,1,5]
输出："arigatou"

```
 **示例 5：** 

```
输入：s = "art", indices = [1,0,2]
输出："rat"

```
 

 **提示：** 
-  `s.length == indices.length == n` 
-  `1 <= n <= 100` 
-  `s` 仅包含小写英文字母。
-  `0 <= indices[i] < n` 
-  `indices` 的所有的值都是唯一的（也就是说， `indices` 是整数 `0` 到 `n - 1` 形成的一组排列）。
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 1529.最少的后缀翻转次数
[https://leetcode-cn.com/problems/minimum-suffix-flips](https://leetcode-cn.com/problems/minimum-suffix-flips) 
## 原题
给你一个长度为 `n` 、下标从 **0** 开始的二进制字符串 `target` 。你自己有另一个长度为 `n` 的二进制字符串 `s` ，最初每一位上都是 0 。你想要让 `s` 和 `target` 相等。

在一步操作，你可以选择下标 `i` （ `0 <= i < n` ）并翻转在 **闭区间** `[i, n - 1]` 内的所有位。翻转意味着 `'0'` 变为 `'1'` ，而 `'1'` 变为 `'0'` 。
返回使 `s` 与 `target` 相等需要的最少翻转次数。

 

 **示例 1：** 

```

输入：target = "10111"
输出：3
解释：最初，s = "00000" 。
选择下标 i = 2: "00000" -> "00111"
选择下标 i = 0: "00111" -> "11000"
选择下标 i = 1: "11000" -> "10111"
要达成目标，需要至少 3 次翻转。

```
 **示例 2：** 

```

输入：target = "101"
输出：3
解释：最初，s = "000" 。
选择下标 i = 0: "000" -> "111"
选择下标 i = 1: "111" -> "100"
选择下标 i = 2: "100" -> "101"
要达成目标，需要至少 3 次翻转。

```
 **示例 3：** 

```

输入：target = "00000"
输出：0
解释：由于 s 已经等于目标，所以不需要任何操作

```
 

 **提示：** 
-  `n == target.length` 
-  `1 <= n <= 10^5` 
-  `target[i]` 为 `'0'` 或 `'1'` 
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 1530.好叶子节点对的数量
[https://leetcode-cn.com/problems/number-of-good-leaf-nodes-pairs](https://leetcode-cn.com/problems/number-of-good-leaf-nodes-pairs) 
## 原题
给你二叉树的根节点 `root` 和一个整数 `distance` 。

如果二叉树中两个 **叶** 节点之间的 **最短路径长度** 小于或者等于 `distance` ，那它们就可以构成一组 **好叶子节点对** 。

返回树中 **好叶子节点对的数量** 。

 

 **示例 1：** 

 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/26/e1.jpg" style="height: 321px; width: 321px;">

```
输入：root = [1,2,3,null,4], distance = 3
输出：1
解释：树的叶节点是 3 和 4 ，它们之间的最短路径的长度是 3 。这是唯一的好叶子节点对。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/26/e2.jpg" style="height: 321px; width: 441px;">

```
输入：root = [1,2,3,4,5,6,7], distance = 3
输出：2
解释：好叶子节点对为 [4,5] 和 [6,7] ，最短路径长度都是 2 。但是叶子节点对 [4,6] 不满足要求，因为它们之间的最短路径长度为 4 。

```
 **示例 3：** 

```
输入：root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
输出：1
解释：唯一的好叶子节点对是 [2,5] 。

```
 **示例 4：** 

```
输入：root = [100], distance = 1
输出：0

```
 **示例 5：** 

```
输入：root = [1,1,1], distance = 2
输出：1

```
 

 **提示：** 
-  `tree` 的节点数在 `[1, 2^10]` 范围内。
- 每个节点的值都在 `[1, 100]` 之间。
-  `1 <= distance <= 10` 
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1531.压缩字符串 II
[https://leetcode-cn.com/problems/string-compression-ii](https://leetcode-cn.com/problems/string-compression-ii) 
## 原题
<a href="https://baike.baidu.com/item/%E8%A1%8C%E7%A8%8B%E9%95%BF%E5%BA%A6%E7%BC%96%E7%A0%81/2931940?fr=aladdin" target="_blank">行程长度编码</a> 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。例如，用此方法压缩字符串 `"aabccc"` ，将 `"aa"` 替换为 `"a2"` ， `"ccc"` 替换为` `"c3"` 。因此压缩后的字符串变为 `"a2bc3"` 。

注意，本问题中，压缩时没有在单个字符后附加计数 `';1';` 。

给你一个字符串 `s` 和一个整数 `k` 。你需要从字符串 `s` 中删除最多 `k` 个字符，以使 `s` 的行程长度编码长度最小。

请你返回删除最多 `k` 个字符后， `s` **行程长度编码的最小长度** 。

 

 **示例 1：** 

```
输入：s = "aaabcccd", k = 2
输出：4
解释：在不删除任何内容的情况下，压缩后的字符串是 "a3bc3d" ，长度为 6 。最优的方案是删除 ';b'; 和 ';d';，这样一来，压缩后的字符串为 "a3c3" ，长度是 4 。
```
 **示例 2：** 

```
输入：s = "aabbaa", k = 2
输出：2
解释：如果删去两个 ';b'; 字符，那么压缩后的字符串是长度为 2 的 "a4" 。

```
 **示例 3：** 

```
输入：s = "aaaaaaaaaaa", k = 0
输出：3
解释：由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 "a11" ，长度为 3 。

```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `0 <= k <= s.length` 
-  `s` 仅包含小写英文字母
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1532.最近的三笔订单
[https://leetcode-cn.com/problems/the-most-recent-three-orders](https://leetcode-cn.com/problems/the-most-recent-three-orders) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1533.找到最大整数的索引
[https://leetcode-cn.com/problems/find-the-index-of-the-large-integer](https://leetcode-cn.com/problems/find-the-index-of-the-large-integer) 
## 原题

 
**标签**
`数组` `二分查找` `交互` 


## 
```python

```
>
# 1534.统计好三元组
[https://leetcode-cn.com/problems/count-good-triplets](https://leetcode-cn.com/problems/count-good-triplets) 
## 原题
给你一个整数数组 `arr` ，以及 `a` 、 `b` 、 `c` 三个整数。请你统计其中好三元组的数量。

如果三元组 `(arr[i], arr[j], arr[k])` 满足下列全部条件，则认为它是一个 **好三元组** 。
-  `0 <= i < j < k < arr.length` 
-  `|arr[i] - arr[j]| <= a` 
-  `|arr[j] - arr[k]| <= b` 
-  `|arr[i] - arr[k]| <= c` 
其中 `|x|` 表示 `x` 的绝对值。

返回 **好三元组的数量** 。

 

 **示例 1：** 

```
输入：arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
输出：4
解释：一共有 4 个好三元组：[(3,0,1), (3,0,1), (3,1,1), (0,1,1)] 。

```
 **示例 2：** 

```
输入：arr = [1,1,2,2,3], a = 0, b = 0, c = 1
输出：0
解释：不存在满足所有条件的三元组。

```
 

 **提示：** 
-  `3 <= arr.length <= 100` 
-  `0 <= arr[i] <= 1000` 
-  `0 <= a, b, c <= 1000` 
 
**标签**
`数组` `枚举` 


## 
```python

```
>
# 1535.找出数组游戏的赢家
[https://leetcode-cn.com/problems/find-the-winner-of-an-array-game](https://leetcode-cn.com/problems/find-the-winner-of-an-array-game) 
## 原题
给你一个由 **不同** 整数组成的整数数组 `arr` 和一个整数 `k` 。

每回合游戏都在数组的前两个元素（即 `arr[0]` 和 `arr[1]` ）之间进行。比较 `arr[0]` 与 `arr[1]` 的大小，较大的整数将会取得这一回合的胜利并保留在位置 `0` ，较小的整数移至数组的末尾。当一个整数赢得 `k` 个连续回合时，游戏结束，该整数就是比赛的 **赢家** 。

返回赢得比赛的整数。

题目数据 **保证** 游戏存在赢家。

 

 **示例 1：** 

```
输入：arr = [2,1,3,5,4,6,7], k = 2
输出：5
解释：一起看一下本场游戏每回合的情况：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/07/30/q-example.png" style="height: 90px; width: 400px;">
因此将进行 4 回合比赛，其中 5 是赢家，因为它连胜 2 回合。

```
 **示例 2：** 

```
输入：arr = [3,2,1], k = 10
输出：3
解释：3 将会在前 10 个回合中连续获胜。

```
 **示例 3：** 

```
输入：arr = [1,9,8,2,3,7,6,4,5], k = 7
输出：9

```
 **示例 4：** 

```
输入：arr = [1,11,22,33,44,55,66,77,88,99], k = 1000000000
输出：99

```
 

 **提示：** 
-  `2 <= arr.length <= 10^5` 
-  `1 <= arr[i] <= 10^6` 
-  `arr` 所含的整数 **各不相同** 。
-  `1 <= k <= 10^9` 
 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 1536.排布二进制网格的最少交换次数
[https://leetcode-cn.com/problems/minimum-swaps-to-arrange-a-binary-grid](https://leetcode-cn.com/problems/minimum-swaps-to-arrange-a-binary-grid) 
## 原题
给你一个 `n x n` 的二进制网格 `grid` ，每一次操作中，你可以选择网格的 **相邻两行** 进行交换。

一个符合要求的网格需要满足主对角线以上的格子全部都是 **0** 。

请你返回使网格满足要求的最少操作次数，如果无法使网格符合要求，请你返回 **-1** 。

主对角线指的是从 `(1, 1)` 到 `(n, n)` 的这些格子。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/02/fw.jpg" style="height: 141px; width: 750px;">

```
输入：grid = [[0,0,1],[1,1,0],[1,0,0]]
输出：3

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/02/e2.jpg" style="height: 270px; width: 270px;">

```
输入：grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
输出：-1
解释：所有行都是一样的，交换相邻行无法使网格符合要求。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/02/e3.jpg" style="height: 210px; width: 210px;">

```
输入：grid = [[1,0,0],[1,1,0],[1,1,1]]
输出：0

```
 

 **提示：** 
-  `n == grid.length` 
-  `n == grid[i].length` 
-  `1 <= n <= 200` 
-  `grid[i][j]` 要么是 `0` 要么是 `1` 。
 
**标签**
`贪心` `数组` `矩阵` 


## 
```python

```
>
# 1537.最大得分
[https://leetcode-cn.com/problems/get-the-maximum-score](https://leetcode-cn.com/problems/get-the-maximum-score) 
## 原题
你有两个 **有序** 且数组内元素互不相同的数组 `nums1` 和 `nums2` 。

一条 **合法路径** 定义如下：
- 选择数组 nums1 或者 nums2 开始遍历（从下标 0 处开始）。
- 从左到右遍历当前数组。
- 如果你遇到了 `nums1` 和 `nums2` 中都存在的值，那么你可以切换路径到另一个数组对应数字处继续遍历（但在合法路径中重复数字只会被统计一次）。
得分定义为合法路径中不同数字的和。

请你返回所有可能合法路径中的最大得分。

由于答案可能很大，请你将它对 10^9 + 7 取余后返回。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/02/sample_1_1893.png" style="height: 163px; width: 538px;">** 

```
输入：nums1 = [2,4,5,8,10], nums2 = [4,6,8,9]
输出：30
解释：合法路径包括：
[2,4,5,8,10], [2,4,5,8,9], [2,4,6,8,9], [2,4,6,8,10],（从 nums1 开始遍历）
[4,6,8,9], [4,5,8,10], [4,5,8,9], [4,6,8,10]  （从 nums2 开始遍历）
最大得分为上图中的绿色路径 [2,4,6,8,10] 。

```
 **示例 2：** 

```
输入：nums1 = [1,3,5,7,9], nums2 = [3,5,100]
输出：109
解释：最大得分由路径 [1,3,5,100] 得到。

```
 **示例 3：** 

```
输入：nums1 = [1,2,3,4,5], nums2 = [6,7,8,9,10]
输出：40
解释：nums1 和 nums2 之间无相同数字。
最大得分由路径 [6,7,8,9,10] 得到。

```
 **示例 4：** 

```
输入：nums1 = [1,4,5,8,9,11,19], nums2 = [2,3,4,11,12]
输出：61

```
 

 **提示：** 
-  `1 <= nums1.length <= 10^5` 
-  `1 <= nums2.length <= 10^5` 
-  `1 <= nums1[i], nums2[i] <= 10^7` 
-  `nums1` 和 `nums2` 都是严格递增的数组。
 
**标签**
`贪心` `数组` `双指针` `动态规划` 


## 
```python

```
>
# 1538.找出隐藏数组中出现次数最多的元素
[https://leetcode-cn.com/problems/guess-the-majority-in-a-hidden-array](https://leetcode-cn.com/problems/guess-the-majority-in-a-hidden-array) 
## 原题

 
**标签**
`数组` `数学` `交互` 


## 
```python

```
>
# 1539.第 k 个缺失的正整数
[https://leetcode-cn.com/problems/kth-missing-positive-number](https://leetcode-cn.com/problems/kth-missing-positive-number) 
## 原题
给你一个 **严格升序排列** 的正整数数组 `arr` 和一个整数 `k` 。

请你找到这个数组里第 `k` 个缺失的正整数。

 

 **示例 1：** 

```
输入：arr = [2,3,4,7,11], k = 5
输出：9
解释：缺失的正整数包括 [1,5,6,8,9,10,12,13,...] 。第 5 个缺失的正整数为 9 。

```
 **示例 2：** 

```
输入：arr = [1,2,3,4], k = 2
输出：6
解释：缺失的正整数包括 [5,6,7,...] 。第 2 个缺失的正整数为 6 。

```
 

 **提示：** 
-  `1 <= arr.length <= 1000` 
-  `1 <= arr[i] <= 1000` 
-  `1 <= k <= 1000` 
- 对于所有 `1 <= i < j <= arr.length` 的 `i` 和 `j` 满足 `arr[i] < arr[j]` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 1540.K 次操作转变字符串
[https://leetcode-cn.com/problems/can-convert-string-in-k-moves](https://leetcode-cn.com/problems/can-convert-string-in-k-moves) 
## 原题
给你两个字符串 `s` 和 `t` ，你的目标是在 `k` 次操作以内把字符串 `s` 转变成 `t` 。

在第 `i` 次操作时（ `1 <= i <= k` ），你可以选择进行如下操作：
- 选择字符串 `s` 中满足 `1 <= j <= s.length` 且之前未被选过的任意下标 `j` （下标从 1 开始），并将此位置的字符切换 `i` 次。
- 不进行任何操作。
切换 1 个字符的意思是用字母表中该字母的下一个字母替换它（字母表环状接起来，所以 `'z'` 切换后会变成 `'a'` ）。第 `i` 次操作意味着该字符应切换 `i` 次

请记住任意一个下标 `j` 最多只能被操作 1 次。

如果在不超过 `k` 次操作内可以把字符串 `s` 转变成 `t` ，那么请你返回 `true` ，否则请你返回 `false` 。

 

 **示例 1：** 

```

输入：s = "input", t = "ouput", k = 9
输出：true
解释：第 6 次操作时，我们将 'i' 切换 6 次得到 'o' 。第 7 次操作时，我们将 'n' 切换 7 次得到 'u' 。

```
 **示例 2：** 

```

输入：s = "abc", t = "bcd", k = 10
输出：false
解释：我们需要将每个字符切换 1 次才能得到 t 。我们可以在第 1 次操作时将 'a' 切换成 'b' ，但另外 2 个字母在剩余操作中无法再转变为 t 中对应字母。

```
 **示例 3：** 

```

输入：s = "aab", t = "bbb", k = 27
输出：true
解释：第 1 次操作时，我们将第一个 'a' 切换 1 次得到 'b' 。在第 27 次操作时，我们将第二个字母 'a' 切换 27 次得到 'b' 。

```
 

 **提示：** 
-  `1 <= s.length, t.length <= 10^5` 
-  `0 <= k <= 10^9` 
-  `s` 和 `t` 只包含小写英文字母。
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1541.平衡括号字符串的最少插入次数
[https://leetcode-cn.com/problems/minimum-insertions-to-balance-a-parentheses-string](https://leetcode-cn.com/problems/minimum-insertions-to-balance-a-parentheses-string) 
## 原题
给你一个括号字符串 `s` ，它只包含字符 `';(';` 和 `';)';` 。一个括号字符串被称为平衡的当它满足：
- 任何左括号 `';(';` 必须对应两个连续的右括号 `';))';` 。
- 左括号 `';(';` 必须在对应的连续两个右括号 `';))';` 之前。
比方说 `"())"` ， `"())(())))"` 和 `"(())())))"` 都是平衡的， `")()"` ， `"()))"` 和 `"(()))"` 都是不平衡的。

你可以在任意位置插入字符 ';('; 和 ';)'; 使字符串平衡。

请你返回让 `s` 平衡的最少插入次数。

 

 **示例 1：** 

```
输入：s = "(()))"
输出：1
解释：第二个左括号有与之匹配的两个右括号，但是第一个左括号只有一个右括号。我们需要在字符串结尾额外增加一个 ';)'; 使字符串变成平衡字符串 "(())))" 。

```
 **示例 2：** 

```
输入：s = "())"
输出：0
解释：字符串已经平衡了。

```
 **示例 3：** 

```
输入：s = "))())("
输出：3
解释：添加 ';('; 去匹配最开头的 ';))'; ，然后添加 ';))'; 去匹配最后一个 ';('; 。

```
 **示例 4：** 

```
输入：s = "(((((("
输出：12
解释：添加 12 个 ';)'; 得到平衡字符串。

```
 **示例 5：** 

```
输入：s = ")))))))"
输出：5
解释：在字符串开头添加 4 个 ';('; 并在结尾添加 1 个 ';)'; ，字符串变成平衡字符串 "(((())))))))" 。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s` 只包含 `';(';` 和 `';)';` 。
 
**标签**
`栈` `贪心` `字符串` 


## 
```python

```
>
# 1542.找出最长的超赞子字符串
[https://leetcode-cn.com/problems/find-longest-awesome-substring](https://leetcode-cn.com/problems/find-longest-awesome-substring) 
## 原题
给你一个字符串 `s` 。请返回 `s` 中最长的 **超赞子字符串** 的长度。

「超赞子字符串」需满足满足下述两个条件：
- 该字符串是 `s` 的一个非空子字符串
- 进行任意次数的字符交换后，该字符串可以变成一个回文字符串
 

 **示例 1：** 

```
输入：s = "3242415"
输出：5
解释："24241" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "24142"

```
 **示例 2：** 

```
输入：s = "12345678"
输出：1

```
 **示例 3：** 

```
输入：s = "213123"
输出：6
解释："213123" 是最长的超赞子字符串，交换其中的字符后，可以得到回文 "231132"

```
 **示例 4：** 

```
输入：s = "00"
输出：2

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s` 仅由数字组成
 
**标签**
`位运算` `哈希表` `字符串` 


## 
```python

```
>
# 1543.产品名称格式修复
[https://leetcode-cn.com/problems/fix-product-name-format](https://leetcode-cn.com/problems/fix-product-name-format) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1544.整理字符串
[https://leetcode-cn.com/problems/make-the-string-great](https://leetcode-cn.com/problems/make-the-string-great) 
## 原题
给你一个由大小写英文字母组成的字符串 `s` 。

一个整理好的字符串中，两个相邻字符 `s[i]` 和 `s[i+1]` ，其中 `0<= i <= s.length-2` ，要满足如下条件:
- 若 `s[i]` 是小写字符，则 `s[i+1]` 不可以是相同的大写字符。
- 若 `s[i]` 是大写字符，则 `s[i+1]` 不可以是相同的小写字符。
请你将字符串整理好，每次你都可以从字符串中选出满足上述条件的 **两个相邻** 字符并删除，直到字符串整理好为止。

请返回整理好的 **字符串** 。题目保证在给出的约束条件下，测试样例对应的答案是唯一的。

 **注意：** 空字符串也属于整理好的字符串，尽管其中没有任何字符。

 

 **示例 1：** 

```

输入：s = "leEeetcode"
输出："leetcode"
解释：无论你第一次选的是 i = 1 还是 i = 2，都会使 "leEeetcode" 缩减为 "leetcode" 。

```
 **示例 2：** 

```

输入：s = "abBAcC"
输出：""
解释：存在多种不同情况，但所有的情况都会导致相同的结果。例如：
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

```
 **示例 3：** 

```

输入：s = "s"
输出："s"

```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `s` 只包含小写和大写英文字母
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 1545.找出第 N 个二进制字符串中的第 K 位
[https://leetcode-cn.com/problems/find-kth-bit-in-nth-binary-string](https://leetcode-cn.com/problems/find-kth-bit-in-nth-binary-string) 
## 原题
给你两个正整数 `n` 和 `k` ，二进制字符串  `S<sub>n</sub>` 的形成规则如下：
-  `S<sub>1</sub> = "0"` 
- 当 `i > 1` 时， `S<sub>i</sub> = S<sub>i-1</sub> + "1" + reverse(invert(S<sub>i-1</sub>))` 
其中 `+` 表示串联操作， `reverse(x)` 返回反转 `x` 后得到的字符串，而 `invert(x)` 则会翻转 x 中的每一位（0 变为 1，而 1 变为 0）。

例如，符合上述描述的序列的前 4 个字符串依次是：
-  `S<sub>1 </sub>= "0"` 
-  `S<sub>2 </sub>= "0 **1** 1"` 
-  `S<sub>3 </sub>= "011 **1** 001"` 
-  `S<sub>4</sub> = "0111001 **1** 0110001"` 
请你返回  `S<sub>n</sub>` 的 **第 `k` 位字符** ，题目数据保证 `k` 一定在 `S<sub>n</sub>` 长度范围以内。

 

 **示例 1：** 

```

输入：n = 3, k = 1
输出："0"
解释：S3 为 "0111001"，其第 1 位为 "0" 。

```
 **示例 2：** 

```

输入：n = 4, k = 11
输出："1"
解释：S4 为 "011100110110001"，其第 11 位为 "1" 。

```
 **示例 3：** 

```

输入：n = 1, k = 1
输出："0"

```
 **示例 4：** 

```

输入：n = 2, k = 3
输出："1"

```
 

 **提示：** 
-  `1 <= n <= 20` 
-  `1 <= k <= 2^n - 1` 
 
**标签**
`递归` `字符串` 


## 
```python

```
>
# 1546.和为目标值且不重叠的非空子数组的最大数目
[https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target](https://leetcode-cn.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target) 
## 原题
给你一个数组 `nums` 和一个整数 `target` 。

请你返回 **非空不重叠** 子数组的最大数目，且每个子数组中数字和都为 `target` 。

 

 **示例 1：** 

```
输入：nums = [1,1,1,1,1], target = 2
输出：2
解释：总共有 2 个不重叠子数组（加粗数字表示） [1,1,1,1,1] ，它们的和为目标值 2 。

```
 **示例 2：** 

```
输入：nums = [-1,3,5,1,4,2,-9], target = 6
输出：2
解释：总共有 3 个子数组和为 6 。
([5,1], [4,2], [3,5,1,4,2,-9]) 但只有前 2 个是不重叠的。
```
 **示例 3：** 

```
输入：nums = [-2,6,6,3,5,4,1,2,8], target = 10
输出：3

```
 **示例 4：** 

```
输入：nums = [0,0,0], target = 0
输出：3

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-10^4 <= nums[i] <= 10^4` 
-  `0 <= target <= 10^6` 
 
**标签**
`贪心` `数组` `哈希表` `前缀和` 


## 
```python

```
>
# 1547.切棍子的最小成本
[https://leetcode-cn.com/problems/minimum-cost-to-cut-a-stick](https://leetcode-cn.com/problems/minimum-cost-to-cut-a-stick) 
## 原题
有一根长度为 `n` 个单位的木棍，棍上从 `0` 到 `n` 标记了若干位置。例如，长度为 **6** 的棍子可以标记如下：

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/09/statement.jpg" style="height: 111px; width: 521px;" />

给你一个整数数组 `cuts` ，其中 `cuts[i]` 表示你需要将棍子切开的位置。

你可以按顺序完成切割，也可以根据需要更改切割的顺序。

每次切割的成本都是当前要切割的棍子的长度，切棍子的总成本是历次切割成本的总和。对棍子进行切割将会把一根木棍分成两根较小的木棍（这两根木棍的长度和就是切割前木棍的长度）。请参阅第一个示例以获得更直观的解释。

返回切棍子的 **最小总成本** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/09/e1.jpg" style="height: 284px; width: 350px;" />

```

输入：n = 7, cuts = [1,3,4,5]
输出：16
解释：按 [1, 3, 4, 5] 的顺序切割的情况如下所示：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/09/e11.jpg" style="height: 284px; width: 350px;" />
第一次切割长度为 7 的棍子，成本为 7 。第二次切割长度为 6 的棍子（即第一次切割得到的第二根棍子），第三次切割为长度 4 的棍子，最后切割长度为 3 的棍子。总成本为 7 + 6 + 4 + 3 = 20 。
而将切割顺序重新排列为 [3, 5, 1, 4] 后，总成本 = 16（如示例图中 7 + 4 + 3 + 2 = 16）。

```
 **示例 2：** 

```

输入：n = 9, cuts = [5,6,1,4,2]
输出：22
解释：如果按给定的顺序切割，则总成本为 25 。总成本 <= 25 的切割顺序很多，例如，[4, 6, 5, 2, 1] 的总成本 = 22，是所有可能方案中成本最小的。
```
 

 **提示：** 
-  `2 <= n <= 10^6` 
-  `1 <= cuts.length <= min(n - 1, 100)` 
-  `1 <= cuts[i] <= n - 1` 
-  `cuts` 数组中的所有整数都 **互不相同** 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1548.图中最相似的路径
[https://leetcode-cn.com/problems/the-most-similar-path-in-a-graph](https://leetcode-cn.com/problems/the-most-similar-path-in-a-graph) 
## 原题

 
**标签**
`图` `动态规划` 


## 
```python

```
>
# 1549.每件商品的最新订单
[https://leetcode-cn.com/problems/the-most-recent-orders-for-each-product](https://leetcode-cn.com/problems/the-most-recent-orders-for-each-product) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1550.存在连续三个奇数的数组
[https://leetcode-cn.com/problems/three-consecutive-odds](https://leetcode-cn.com/problems/three-consecutive-odds) 
## 原题
给你一个整数数组 `arr` ，请你判断数组中是否存在连续三个元素都是奇数的情况：如果存在，请返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```
输入：arr = [2,6,4,1]
输出：false
解释：不存在连续三个元素都是奇数的情况。

```
 **示例 2：** 

```
输入：arr = [1,2,34,3,4,5,7,23,12]
输出：true
解释：存在连续三个元素都是奇数的情况，即 [5,7,23] 。

```
 

 **提示：** 
-  `1 <= arr.length <= 1000` 
-  `1 <= arr[i] <= 1000` 
 
**标签**
`数组` 


## 
```python

```
>
# 1551.使数组中所有元素相等的最小操作数
[https://leetcode-cn.com/problems/minimum-operations-to-make-array-equal](https://leetcode-cn.com/problems/minimum-operations-to-make-array-equal) 
## 原题
存在一个长度为 `n` 的数组 `arr` ，其中 `arr[i] = (2 * i) + 1` （ `0 <= i < n` ）。

一次操作中，你可以选出两个下标，记作 `x` 和 `y` （ `0 <= x, y < n` ）并使 `arr[x]` 减去 `1` 、 `arr[y]` 加上 `1` （即 `arr[x] -=1` 且 `arr[y] += 1` ）。最终的目标是使数组中的所有元素都 **相等** 。题目测试用例将会 **保证** ：在执行若干步操作后，数组中的所有元素最终可以全部相等。

给你一个整数 `n` ，即数组的长度。请你返回使数组 `arr` 中所有元素相等所需的 **最小操作数** 。

 

 **示例 1：** 

```
输入：n = 3
输出：2
解释：arr = [1, 3, 5]
第一次操作选出 x = 2 和 y = 0，使数组变为 [2, 3, 4]
第二次操作继续选出 x = 2 和 y = 0，数组将会变成 [3, 3, 3]

```
 **示例 2：** 

```
输入：n = 6
输出：9

```
 

 **提示：** 
-  `1 <= n <= 10^4` 
 
**标签**
`数学` 


## 
```python

```
>
# 1552.两球之间的磁力
[https://leetcode-cn.com/problems/magnetic-force-between-two-balls](https://leetcode-cn.com/problems/magnetic-force-between-two-balls) 
## 原题
在代号为 C-137 的地球上，Rick 发现如果他将两个球放在他新发明的篮子里，它们之间会形成特殊形式的磁力。Rick 有 `n` 个空的篮子，第 `i` 个篮子的位置在 `position[i]` ，Morty 想把 `m` 个球放到这些篮子里，使得任意两球间 **最小磁力** 最大。

已知两个球如果分别位于 `x` 和 `y` ，那么它们之间的磁力为 `|x - y|` 。

给你一个整数数组 `position` 和一个整数 `m` ，请你返回最大化的最小磁力。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/16/q3v1.jpg" style="height: 195px; width: 562px;">

```
输入：position = [1,2,3,4,7], m = 3
输出：3
解释：将 3 个球分别放入位于 1，4 和 7 的三个篮子，两球间的磁力分别为 [3, 3, 6]。最小磁力为 3 。我们没办法让最小磁力大于 3 。

```
 **示例 2：** 

```
输入：position = [5,4,3,2,1,1000000000], m = 2
输出：999999999
解释：我们使用位于 1 和 1000000000 的篮子时最小磁力最大。

```
 

 **提示：** 
-  `n == position.length` 
-  `2 <= n <= 10^5` 
-  `1 <= position[i] <= 10^9` 
- 所有 `position` 中的整数 **互不相同** 。
-  `2 <= m <= position.length` 
 
**标签**
`数组` `二分查找` `排序` 


## 
```python

```
>
# 1553.吃掉 N 个橘子的最少天数
[https://leetcode-cn.com/problems/minimum-number-of-days-to-eat-n-oranges](https://leetcode-cn.com/problems/minimum-number-of-days-to-eat-n-oranges) 
## 原题
厨房里总共有 `n` 个橘子，你决定每一天选择如下方式之一吃这些橘子：
- 吃掉一个橘子。
- 如果剩余橘子数 `n` 能被 2 整除，那么你可以吃掉 `n/2` 个橘子。
- 如果剩余橘子数 `n` 能被 3 整除，那么你可以吃掉 `2*(n/3)` 个橘子。
每天你只能从以上 3 种方案中选择一种方案。

请你返回吃掉所有 `n` 个橘子的最少天数。

 

 **示例 1：** 

```
输入：n = 10
输出：4
解释：你总共有 10 个橘子。
第 1 天：吃 1 个橘子，剩余橘子数 10 - 1 = 9。
第 2 天：吃 6 个橘子，剩余橘子数 9 - 2*(9/3) = 9 - 6 = 3。（9 可以被 3 整除）
第 3 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。
第 4 天：吃掉最后 1 个橘子，剩余橘子数 1 - 1 = 0。
你需要至少 4 天吃掉 10 个橘子。

```
 **示例 2：** 

```
输入：n = 6
输出：3
解释：你总共有 6 个橘子。
第 1 天：吃 3 个橘子，剩余橘子数 6 - 6/2 = 6 - 3 = 3。（6 可以被 2 整除）
第 2 天：吃 2 个橘子，剩余橘子数 3 - 2*(3/3) = 3 - 2 = 1。（3 可以被 3 整除）
第 3 天：吃掉剩余 1 个橘子，剩余橘子数 1 - 1 = 0。
你至少需要 3 天吃掉 6 个橘子。

```
 **示例 3：** 

```
输入：n = 1
输出：1

```
 **示例 4：** 

```
输入：n = 56
输出：6

```
 

 **提示：** 
-  `1 <= n <= 2*10^9` 
 
**标签**
`记忆化搜索` `动态规划` 


## 
```python

```
>
# 1554.只有一个不同字符的字符串
[https://leetcode-cn.com/problems/strings-differ-by-one-character](https://leetcode-cn.com/problems/strings-differ-by-one-character) 
## 原题

 
**标签**
`哈希表` `字符串` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 1555.银行账户概要
[https://leetcode-cn.com/problems/bank-account-summary](https://leetcode-cn.com/problems/bank-account-summary) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1556.千位分隔数
[https://leetcode-cn.com/problems/thousand-separator](https://leetcode-cn.com/problems/thousand-separator) 
## 原题
给你一个整数 `n` ，请你每隔三位添加点（即 "." 符号）作为千位分隔符，并将结果以字符串格式返回。

 

 **示例 1：** 

```
输入：n = 987
输出："987"

```
 **示例 2：** 

```
输入：n = 1234
输出："1.234"

```
 **示例 3：** 

```
输入：n = 123456789
输出："123.456.789"

```
 **示例 4：** 

```
输入：n = 0
输出："0"

```
 

 **提示：** 
-  `0 <= n < 2^31` 
 
**标签**
`字符串` 


## 
```python

```
>
# 1557.可以到达所有点的最少点数目
[https://leetcode-cn.com/problems/minimum-number-of-vertices-to-reach-all-nodes](https://leetcode-cn.com/problems/minimum-number-of-vertices-to-reach-all-nodes) 
## 原题
给你一个 **有向无环图** ， `n` 个节点编号为 `0` 到 `n-1` ，以及一个边数组 `edges` ，其中 `edges[i] = [from<sub>i</sub>, to<sub>i</sub>]` 表示一条从点 `from<sub>i</sub>` 到点 `to<sub>i</sub>` 的有向边。

找到最小的点集使得从这些点出发能到达图中所有点。题目保证解存在且唯一。

你可以以任意顺序返回这些节点编号。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5480e1.png" style="height: 181px; width: 231px;">

```
输入：n = 6, edges = [[0,1],[0,2],[2,5],[3,4],[4,2]]
输出：[0,3]
解释：从单个节点出发无法到达所有节点。从 0 出发我们可以到达 [0,1,2,5] 。从 3 出发我们可以到达 [3,4,2,5] 。所以我们输出 [0,3] 。
```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5480e2.png" style="height: 201px; width: 201px;">

```
输入：n = 5, edges = [[0,1],[2,1],[3,1],[1,4],[2,4]]
输出：[0,2,3]
解释：注意到节点 0，3 和 2 无法从其他节点到达，所以我们必须将它们包含在结果点集中，这些点都能到达节点 1 和 4 。

```
 

 **提示：** 
-  `2 <= n <= 10^5` 
-  `1 <= edges.length <= min(10^5, n * (n - 1) / 2)` 
-  `edges[i].length == 2` 
-  `0 <= from<sub>i,</sub> to<sub>i</sub> < n` 
- 所有点对 `(from<sub>i</sub>, to<sub>i</sub>)` 互不相同。
 
**标签**
`图` 


## 
```python

```
>
# 1558.得到目标数组的最少函数调用次数
[https://leetcode-cn.com/problems/minimum-numbers-of-function-calls-to-make-target-array](https://leetcode-cn.com/problems/minimum-numbers-of-function-calls-to-make-target-array) 
## 原题
<img alt="" src="https://assets.leetcode.com/uploads/2020/07/10/sample_2_1887.png" style="height:294px; width:573px" />

给你一个与 `nums` 大小相同且初始值全为 0 的数组 `arr` ，请你调用以上函数得到整数数组 `nums` 。

请你返回将 `arr` 变成 `nums` 的最少函数调用次数。

答案保证在 32 位有符号整数以内。

 

 **示例 1：** 

```

输入：nums = [1,5]
输出：5
解释：给第二个数加 1 ：[0, 0] 变成 [0, 1] （1 次操作）。
将所有数字乘以 2 ：[0, 1] -> [0, 2] -> [0, 4] （2 次操作）。
给两个数字都加 1 ：[0, 4] -> [1, 4] -> [1, 5] （2 次操作）。
总操作次数为：1 + 2 + 2 = 5 。

```
 **示例 2：** 

```

输入：nums = [2,2]
输出：3
解释：给两个数字都加 1 ：[0, 0] -> [0, 1] -> [1, 1] （2 次操作）。
将所有数字乘以 2 ： [1, 1] -> [2, 2] （1 次操作）。
总操作次数为： 2 + 1 = 3 。

```
 **示例 3：** 

```

输入：nums = [4,2,5]
输出：6
解释：（初始）[0,0,0] -> [1,0,0] -> [1,0,1] -> [2,0,2] -> [2,1,2] -> [4,2,4] -> [4,2,5] （nums 数组）。

```
 **示例 4：** 

```

输入：nums = [3,2,2,4]
输出：7

```
 **示例 5：** 

```

输入：nums = [2,4,8,16]
输出：8

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^9` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1559.二维网格图中探测环
[https://leetcode-cn.com/problems/detect-cycles-in-2d-grid](https://leetcode-cn.com/problems/detect-cycles-in-2d-grid) 
## 原题
给你一个二维字符网格数组 `grid` ，大小为 `m x n` ，你需要检查 `grid` 中是否存在 **相同值** 形成的环。

一个环是一条开始和结束于同一个格子的长度 **大于等于 4** 的路径。对于一个给定的格子，你可以移动到它上、下、左、右四个方向相邻的格子之一，可以移动的前提是这两个格子有 **相同的值** 。

同时，你也不能回到上一次移动时所在的格子。比方说，环 `(1, 1) -> (1, 2) -> (1, 1)` 是不合法的，因为从 `(1, 2)` 移动到 `(1, 1)` 回到了上一次移动时的格子。

如果 `grid` 中有相同值形成的环，请你返回 `true` ，否则返回 `false` 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5482e1.png" style="height: 152px; width: 231px;">** 

```
输入：grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
输出：true
解释：如下图所示，有 2 个用不同颜色标出来的环：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5482e11.png" style="height: 163px; width: 225px;">

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5482e2.png" style="height: 154px; width: 236px;">** 

```
输入：grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
输出：true
解释：如下图所示，只有高亮所示的一个合法环：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5482e22.png" style="height: 157px; width: 229px;">

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/5482e3.png" style="height: 120px; width: 183px;">** 

```
输入：grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
输出：false

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m <= 500` 
-  `1 <= n <= 500` 
-  `grid` 只包含小写英文字母。
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` 


## 
```python

```
>
# 1560.圆形赛道上经过次数最多的扇区
[https://leetcode-cn.com/problems/most-visited-sector-in-a-circular-track](https://leetcode-cn.com/problems/most-visited-sector-in-a-circular-track) 
## 原题
给你一个整数 `n` 和一个整数数组 `rounds` 。有一条圆形赛道由 `n` 个扇区组成，扇区编号从 `1` 到 `n` 。现将在这条赛道上举办一场马拉松比赛，该马拉松全程由 `m` 个阶段组成。其中，第 `i` 个阶段将会从扇区 `rounds[i - 1]` 开始，到扇区 `rounds[i]` 结束。举例来说，第 `1` 阶段从 `rounds[0]` 开始，到 `rounds[1]` 结束。

请你以数组形式返回经过次数最多的那几个扇区，按扇区编号 **升序** 排列。

注意，赛道按扇区编号升序逆时针形成一个圆（请参见第一个示例）。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/22/3rd45e.jpg" style="height: 341px; width: 433px;">

```
输入：n = 4, rounds = [1,3,1,2]
输出：[1,2]
解释：本场马拉松比赛从扇区 1 开始。经过各个扇区的次序如下所示：
1 --> 2 --> 3（阶段 1 结束）--> 4 --> 1（阶段 2 结束）--> 2（阶段 3 结束，即本场马拉松结束）
其中，扇区 1 和 2 都经过了两次，它们是经过次数最多的两个扇区。扇区 3 和 4 都只经过了一次。
```
 **示例 2：** 

```
输入：n = 2, rounds = [2,1,2,1,2,1,2,1,2]
输出：[2]

```
 **示例 3：** 

```
输入：n = 7, rounds = [1,3,5,7]
输出：[1,2,3,4,5,6,7]

```
 

 **提示：** 
-  `2 <= n <= 100` 
-  `1 <= m <= 100` 
-  `rounds.length == m + 1` 
-  `1 <= rounds[i] <= n` 
-  `rounds[i] != rounds[i + 1]` ，其中 `0 <= i < m` 
 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 1561.你可以获得的最大硬币数目
[https://leetcode-cn.com/problems/maximum-number-of-coins-you-can-get](https://leetcode-cn.com/problems/maximum-number-of-coins-you-can-get) 
## 原题
有 3n 堆数目不一的硬币，你和你的朋友们打算按以下方式分硬币：
- 每一轮中，你将会选出 **任意** 3 堆硬币（不一定连续）。
- Alice 将会取走硬币数量最多的那一堆。
- 你将会取走硬币数量第二多的那一堆。
- Bob 将会取走最后一堆。
- 重复这个过程，直到没有更多硬币。
给你一个整数数组 `piles` ，其中 `piles[i]` 是第 `i` 堆中硬币的数目。

返回你可以获得的最大硬币数目。

 

 **示例 1：** 

```
输入：piles = [2,4,1,2,7,8]
输出：9
解释：选出 (2, 7, 8) ，Alice 取走 8 枚硬币的那堆，你取走 7 枚硬币的那堆，Bob 取走最后一堆。
选出 (1, 2, 4) , Alice 取走 4 枚硬币的那堆，你取走 2 枚硬币的那堆，Bob 取走最后一堆。
你可以获得的最大硬币数目：7 + 2 = 9.
考虑另外一种情况，如果选出的是 (1, 2, 8) 和 (2, 4, 7) ，你就只能得到 2 + 4 = 6 枚硬币，这不是最优解。

```
 **示例 2：** 

```
输入：piles = [2,4,5]
输出：4

```
 **示例 3：** 

```
输入：piles = [9,8,7,6,5,1,2,3,4]
输出：18

```
 

 **提示：** 
-  `3 <= piles.length <= 10^5` 
-  `piles.length % 3 == 0` 
-  `1 <= piles[i] <= 10^4` 
 
**标签**
`贪心` `数组` `数学` `博弈` `排序` 


## 
```python

```
>
# 1562.查找大小为 M 的最新分组
[https://leetcode-cn.com/problems/find-latest-group-of-size-m](https://leetcode-cn.com/problems/find-latest-group-of-size-m) 
## 原题
给你一个数组 `arr` ，该数组表示一个从 `1` 到 `n` 的数字排列。有一个长度为 `n` 的二进制字符串，该字符串上的所有位最初都设置为 `0` 。

在从 `1` 到 `n` 的每个步骤 `i` 中（假设二进制字符串和 `arr` 都是从 `1` 开始索引的情况下），二进制字符串上位于位置 `arr[i]` 的位将会设为 `1` 。

给你一个整数 `m` ，请你找出二进制字符串上存在长度为 `m` 的一组 `1` 的最后步骤。一组 `1` 是一个连续的、由 `1` 组成的子串，且左右两边不再有可以延伸的 `1` 。

返回存在长度 **恰好** 为 `m` 的 **一组 `1` ** 的最后步骤。如果不存在这样的步骤，请返回 `-1` 。

 

 **示例 1：** 

```
输入：arr = [3,5,1,2,4], m = 1
输出：4
解释：
步骤 1："00100"，由 1 构成的组：["1"]
步骤 2："00101"，由 1 构成的组：["1", "1"]
步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
步骤 4："11101"，由 1 构成的组：["111", "1"]
步骤 5："11111"，由 1 构成的组：["11111"]
存在长度为 1 的一组 1 的最后步骤是步骤 4 。
```
 **示例 2：** 

```
输入：arr = [3,1,5,4,2], m = 2
输出：-1
解释：
步骤 1："00100"，由 1 构成的组：["1"]
步骤 2："10100"，由 1 构成的组：["1", "1"]
步骤 3："10101"，由 1 构成的组：["1", "1", "1"]
步骤 4："10111"，由 1 构成的组：["1", "111"]
步骤 5："11111"，由 1 构成的组：["11111"]
不管是哪一步骤都无法形成长度为 2 的一组 1 。

```
 **示例 3：** 

```
输入：arr = [1], m = 1
输出：1

```
 **示例 4：** 

```
输入：arr = [2,1], m = 2
输出：2

```
 

 **提示：** 
-  `n == arr.length` 
-  `1 <= n <= 10^5` 
-  `1 <= arr[i] <= n` 
-  `arr` 中的所有整数 **互不相同** 
-  `1 <= m <= arr.length` 
 
**标签**
`数组` `二分查找` `模拟` 


## 
```python

```
>
# 1563.石子游戏 V
[https://leetcode-cn.com/problems/stone-game-v](https://leetcode-cn.com/problems/stone-game-v) 
## 原题
几块石子 **排成一行** ，每块石子都有一个关联值，关联值为整数，由数组 `stoneValue` 给出。

游戏中的每一轮：Alice 会将这行石子分成两个 **非空行** （即，左侧行和右侧行）；Bob 负责计算每一行的值，即此行中所有石子的值的总和。Bob 会丢弃值最大的行，Alice 的得分为剩下那行的值（每轮累加）。如果两行的值相等，Bob 让 Alice 决定丢弃哪一行。下一轮从剩下的那一行开始。

只 **剩下一块石子** 时，游戏结束。Alice 的分数最初为 ** `0` ** 。

返回 **Alice 能够获得的最大分数** *。* 

 

 **示例 1：** 

```
输入：stoneValue = [6,2,3,4,5,5]
输出：18
解释：在第一轮中，Alice 将行划分为 [6，2，3]，[4，5，5] 。左行的值是 11 ，右行的值是 14 。Bob 丢弃了右行，Alice 的分数现在是 11 。
在第二轮中，Alice 将行分成 [6]，[2，3] 。这一次 Bob 扔掉了左行，Alice 的分数变成了 16（11 + 5）。
最后一轮 Alice 只能将行分成 [2]，[3] 。Bob 扔掉右行，Alice 的分数现在是 18（16 + 2）。游戏结束，因为这行只剩下一块石头了。

```
 **示例 2：** 

```
输入：stoneValue = [7,7,7,7,7,7,7]
输出：28

```
 **示例 3：** 

```
输入：stoneValue = [4]
输出：0

```
 

 **提示：** 
-  `1 <= stoneValue.length <= 500` 
-  `1 <= stoneValue[i] <= 10^6` 
 
**标签**
`数组` `数学` `动态规划` `博弈` 


## 
```python

```
>
# 1564.把箱子放进仓库里 I
[https://leetcode-cn.com/problems/put-boxes-into-the-warehouse-i](https://leetcode-cn.com/problems/put-boxes-into-the-warehouse-i) 
## 原题

 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1565.按月统计订单数与顾客数
[https://leetcode-cn.com/problems/unique-orders-and-customers-per-month](https://leetcode-cn.com/problems/unique-orders-and-customers-per-month) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1566.重复至少 K 次且长度为 M 的模式
[https://leetcode-cn.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times](https://leetcode-cn.com/problems/detect-pattern-of-length-m-repeated-k-or-more-times) 
## 原题
给你一个正整数数组 `arr` ，请你找出一个长度为 `m` 且在数组中至少重复 `k` 次的模式。

 **模式** 是由一个或多个值组成的子数组（连续的子序列）， **连续** 重复多次但 **不重叠** 。 模式由其长度和重复次数定义。

如果数组中存在至少重复 `k` 次且长度为 `m` 的模式，则返回 `true` ，否则返回 `false` 。

 

 **示例 1：** 

```
输入：arr = [1,2,4,4,4,4], m = 1, k = 3
输出：true
解释：模式 (4) 的长度为 1 ，且连续重复 4 次。注意，模式可以重复 k 次或更多次，但不能少于 k 次。

```
 **示例 2：** 

```
输入：arr = [1,2,1,2,1,1,1,3], m = 2, k = 2
输出：true
解释：模式 (1,2) 长度为 2 ，且连续重复 2 次。另一个符合题意的模式是 (2,1) ，同样重复 2 次。

```
 **示例 3：** 

```
输入：arr = [1,2,1,2,1,3], m = 2, k = 3
输出：false
解释：模式 (1,2) 长度为 2 ，但是只连续重复 2 次。不存在长度为 2 且至少重复 3 次的模式。

```
 **示例 4：** 

```
输入：arr = [1,2,3,1,2], m = 2, k = 2
输出：false
解释：模式 (1,2) 出现 2 次但并不连续，所以不能算作连续重复 2 次。

```
 **示例 5：** 

```
输入：arr = [2,2,2,2], m = 2, k = 3
输出：false
解释：长度为 2 的模式只有 (2,2) ，但是只连续重复 2 次。注意，不能计算重叠的重复次数。

```
 

 **提示：** 
-  `2 <= arr.length <= 100` 
-  `1 <= arr[i] <= 100` 
-  `1 <= m <= 100` 
-  `2 <= k <= 100` 
 
**标签**
`数组` `枚举` 


## 
```python

```
>
# 1567.乘积为正数的最长子数组长度
[https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product](https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product) 
## 原题
给你一个整数数组 `nums` ，请你求出乘积为正数的最长子数组的长度。

一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。

请你返回乘积为正数的最长子数组长度。

 

 **示例  1：** 

```

输入：nums = [1,-2,-3,4]
输出：4
解释：数组本身乘积就是正数，值为 24 。

```
 **示例 2：** 

```

输入：nums = [0,1,-2,-3,-4]
输出：3
解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
```
 **示例 3：** 

```

输入：nums = [-1,-2,-3,0,1]
输出：2
解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-10^9 <= nums[i] <= 10^9` 
 

 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 1568.使陆地分离的最少天数
[https://leetcode-cn.com/problems/minimum-number-of-days-to-disconnect-island](https://leetcode-cn.com/problems/minimum-number-of-days-to-disconnect-island) 
## 原题
给你一个由若干 `0` 和 `1` 组成的二维网格 `grid` ，其中 `0` 表示水，而 `1` 表示陆地。岛屿由水平方向或竖直方向上相邻的 `1` （陆地）连接形成。

如果 **恰好只有一座岛屿** ，则认为陆地是 **连通的** ；否则，陆地就是 **分离的** 。

一天内，可以将任何单个陆地单元（ `1` ）更改为水单元（ `0` ）。

返回使陆地分离的最少天数。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/30/1926_island.png" style="height: 139px; width: 498px;">** 

```
输入：grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
输出：2
解释：至少需要 2 天才能得到分离的陆地。
将陆地 grid[1][1] 和 grid[0][2] 更改为水，得到两个分离的岛屿。

```
 **示例 2：** 

```
输入：grid = [[1,1]]
输出：2
解释：如果网格中都是水，也认为是分离的 ([[1,1]] -> [[0,0]])，0 岛屿。

```
 **示例 3：** 

```
输入：grid = [[1,0,1,0]]
输出：0

```
 **示例 4：** 

```
输入：grid = [[1,1,0,1,1],
             [1,1,1,1,1],
             [1,1,0,1,1],
             [1,1,0,1,1]]
输出：1

```
 **示例 5：** 

```
输入：grid = [[1,1,0,1,1],
             [1,1,1,1,1],
             [1,1,0,1,1],
             [1,1,1,1,1]]
输出：2

```
 

 **提示：** 
-  `1 <= grid.length, grid[i].length <= 30` 
-  `grid[i][j]` 为 `0` 或 `1` 
 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `矩阵` `强连通分量` 


## 
```python

```
>
# 1569.将子数组重新排序得到同一个二叉查找树的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-reorder-array-to-get-same-bst](https://leetcode-cn.com/problems/number-of-ways-to-reorder-array-to-get-same-bst) 
## 原题
给你一个数组 `nums` 表示 `1` 到 `n` 的一个排列。我们按照元素在 `nums` 中的顺序依次插入一个初始为空的二叉查找树（BST）。请你统计将 `nums` 重新排序后，统计满足如下条件的方案数：重排后得到的二叉查找树与 `nums` 原本数字顺序得到的二叉查找树相同。

比方说，给你 `nums = [2,1,3]` ，我们得到一棵 2 为根，1 为左孩子，3 为右孩子的树。数组 `[2,3,1]` 也能得到相同的 BST，但 `[3,2,1]` 会得到一棵不同的 BST 。

请你返回重排 `nums` 后，与原数组 `nums` 得到相同二叉查找树的方案数。

由于答案可能会很大，请将结果对 **** `10^9 + 7` 取余数。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/30/bb.png" style="height: 101px; width: 121px;">

```
输入：nums = [2,1,3]
输出：1
解释：我们将 nums 重排， [2,3,1] 能得到相同的 BST 。没有其他得到相同 BST 的方案了。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/30/ex1.png" style="height: 161px; width: 241px;">** 

```
输入：nums = [3,4,5,1,2]
输出：5
解释：下面 5 个数组会得到相同的 BST：
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/30/ex4.png" style="height: 161px; width: 121px;">** 

```
输入：nums = [1,2,3]
输出：0
解释：没有别的排列顺序能得到相同的 BST 。

```
 **示例 4：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/08/30/abc.png" style="height: 161px; width: 241px;">** 

```
输入：nums = [3,1,2,5,4,6]
输出：19

```
 **示例  5：** 

```
输入：nums = [9,4,2,1,3,6,5,7,8,14,11,10,12,13,16,15,17,18]
输出：216212978
解释：得到相同 BST 的方案数是 3216212999。将它对 10^9 + 7 取余后得到 216212978。

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `1 <= nums[i] <= nums.length` 
-  `nums` 中所有数 **互不相同** 。
 
**标签**
`树` `并查集` `二叉搜索树` `记忆化搜索` `数组` `数学` `分治` `动态规划` `二叉树` `组合数学` 


## 
```python

```
>
# 1570.两个稀疏向量的点积
[https://leetcode-cn.com/problems/dot-product-of-two-sparse-vectors](https://leetcode-cn.com/problems/dot-product-of-two-sparse-vectors) 
## 原题

 
**标签**
`设计` `数组` `哈希表` `双指针` 


## 
```python

```
>
# 1571.仓库经理
[https://leetcode-cn.com/problems/warehouse-manager](https://leetcode-cn.com/problems/warehouse-manager) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1572.矩阵对角线元素的和
[https://leetcode-cn.com/problems/matrix-diagonal-sum](https://leetcode-cn.com/problems/matrix-diagonal-sum) 
## 原题
给你一个正方形矩阵 `mat` ，请你返回矩阵对角线元素的和。

请你返回在矩阵主对角线上的元素和副对角线上且不在主对角线上元素的和。

 

 **示例  1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/14/sample_1911.png" style="height:174px; width:336px" />

```

输入：mat = [[1,2,3],
            [4,5,6],
            [7,8,9]]
输出：25
解释：对角线的和为：1 + 5 + 9 + 3 + 7 = 25
请注意，元素 mat[1][1] = 5 只会被计算一次。

```
 **示例  2：** 

```

输入：mat = [[1,1,1,1],
            [1,1,1,1],
            [1,1,1,1],
            [1,1,1,1]]
输出：8

```
 **示例 3：** 

```

输入：mat = [[5]]
输出：5

```
 

 **提示：** 
-  `n == mat.length == mat[i].length` 
-  `1 <= n <= 100` 
-  `1 <= mat[i][j] <= 100` 
 
**标签**
`数组` `矩阵` 


## 
```python

```
>
# 1573.分割字符串的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-split-a-string](https://leetcode-cn.com/problems/number-of-ways-to-split-a-string) 
## 原题
给你一个二进制串 `s` （一个只包含 0 和 1 的字符串），我们可以将 `s` 分割成 3 个 **非空** 字符串 s1, s2, s3 （s1 + s2 + s3 = s）。

请你返回分割 `s` 的方案数，满足 s1，s2 和 s3 中字符 ';1'; 的数目相同。

由于答案可能很大，请将它对 10^9 + 7 取余后返回。

 

 **示例 1：** 

```
输入：s = "10101"
输出：4
解释：总共有 4 种方法将 s 分割成含有 ';1'; 数目相同的三个子字符串。
"1|010|1"
"1|01|01"
"10|10|1"
"10|1|01"

```
 **示例 2：** 

```
输入：s = "1001"
输出：0

```
 **示例 3：** 

```
输入：s = "0000"
输出：3
解释：总共有 3 种分割 s 的方法。
"0|0|00"
"0|00|0"
"00|0|0"

```
 **示例 4：** 

```
输入：s = "100100010100110"
输出：12

```
 

 **提示：** 
-  `s[i] == ';0';` 或者 `s[i] == ';1';` 
-  `3 <= s.length <= 10^5` 
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 1574.删除最短的子数组使剩余数组有序
[https://leetcode-cn.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted](https://leetcode-cn.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted) 
## 原题
给你一个整数数组 `arr` ，请你删除一个子数组（可以为空），使得 `arr` 中剩下的元素是 **非递减** 的。

一个子数组指的是原数组中连续的一个子序列。

请你返回满足题目要求的最短子数组的长度。

 

 **示例 1：** 

```

输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。
```
 **示例 2：** 

```

输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。

```
 **示例 3：** 

```

输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。

```
 **示例 4：** 

```

输入：arr = [1]
输出：0

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `0 <= arr[i] <= 10^9` 
 
**标签**
`栈` `数组` `双指针` `二分查找` `单调栈` 


## 
```python

```
>
# 1575.统计所有可行路径
[https://leetcode-cn.com/problems/count-all-possible-routes](https://leetcode-cn.com/problems/count-all-possible-routes) 
## 原题
给你一个 **互不相同** 的整数数组，其中 `locations[i]` 表示第 `i` 个城市的位置。同时给你 `start` ， `finish` 和 `fuel` 分别表示出发城市、目的地城市和你初始拥有的汽油总量

每一步中，如果你在城市 `i` ，你可以选择任意一个城市 `j` ，满足 `j != i` 且 `0 <= j < locations.length` ，并移动到城市 `j` 。从城市 `i` 移动到 `j` 消耗的汽油量为 `|locations[i] - locations[j]|` ， `|x|` 表示 `x` 的绝对值。

请注意， `fuel` 任何时刻都 **不能** 为负，且你 **可以** 经过任意城市超过一次（包括 `start` 和 `finish` ）。

请你返回从 `start` 到 `finish` 所有可能路径的数目。

由于答案可能很大， 请将它对 `10^9 + 7` 取余后返回。

 

 **示例 1：** 

```

输入：locations = [2,3,6,8,4], start = 1, finish = 3, fuel = 5
输出：4
解释：以下为所有可能路径，每一条都用了 5 单位的汽油：
1 -> 3
1 -> 2 -> 3
1 -> 4 -> 3
1 -> 4 -> 2 -> 3

```
 **示例 2：** 

```

输入：locations = [4,3,1], start = 1, finish = 0, fuel = 6
输出：5
解释：以下为所有可能的路径：
1 -> 0，使用汽油量为 fuel = 1
1 -> 2 -> 0，使用汽油量为 fuel = 5
1 -> 2 -> 1 -> 0，使用汽油量为 fuel = 5
1 -> 0 -> 1 -> 0，使用汽油量为 fuel = 3
1 -> 0 -> 1 -> 0 -> 1 -> 0，使用汽油量为 fuel = 5

```
 **示例 3：** 

```

输入：locations = [5,2,1], start = 0, finish = 2, fuel = 3
输出：0
解释：没有办法只用 3 单位的汽油从 0 到达 2 。因为最短路径需要 4 单位的汽油。
```
 **示例 4 ：** 

```

输入：locations = [2,1,5], start = 0, finish = 0, fuel = 3
输出：2
解释：总共有两条可行路径，0 和 0 -> 1 -> 0 。
```
 **示例 5：** 

```

输入：locations = [1,2,3], start = 0, finish = 2, fuel = 40
输出：615088286
解释：路径总数为 2615088300 。将结果对 10^9 + 7 取余，得到 615088286 。

```
 

 **提示：** 
-  `2 <= locations.length <= 100` 
-  `1 <= locations[i] <= 10^9` 
- 所有 `locations` 中的整数 **互不相同** 。
-  `0 <= start, finish < locations.length` 
-  `1 <= fuel <= 200` 
 
**标签**
`记忆化搜索` `数组` `动态规划` 


## 
```python

```
>
# 1576.替换所有的问号
[https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters](https://leetcode-cn.com/problems/replace-all-s-to-avoid-consecutive-repeating-characters) 
## 原题
给你一个仅包含小写英文字母和 `';?';` 字符的字符串 `s` ，请你将所有的 `';?';` 转换为若干小写字母，使最终的字符串不包含任何 **连续重复** 的字符。

注意：你 **不能** 修改非 `';?';` 字符。

题目测试用例保证 **除** `';?';` 字符 **之外** ，不存在连续重复的字符。

在完成所有转换（可能无需转换）后返回最终的字符串。如果有多个解决方案，请返回其中任何一个。可以证明，在给定的约束条件下，答案总是存在的。

 

 **示例 1：** 

```
输入：s = "?zs"
输出："azs"
解释：该示例共有 25 种解决方案，从 "azs" 到 "yzs" 都是符合题目要求的。只有 "z" 是无效的修改，因为字符串 "zzs" 中有连续重复的两个 ';z'; 。
```
 **示例 2：** 

```
输入：s = "ubv?w"
输出："ubvaw"
解释：该示例共有 24 种解决方案，只有替换成 "v" 和 "w" 不符合题目要求。因为 "ubvvw" 和 "ubvww" 都包含连续重复的字符。

```
 **示例 3：** 

```
输入：s = "j?qg??b"
输出："jaqgacb"

```
 **示例 4：** 

```
输入：s = "??yw?ipkj?"
输出："acywaipkja"

```
 

 **提示：** 
- 
	 `1 <= s.length <= 100` 
	
- 
	 `s` 仅包含小写英文字母和 `';?';` 字符
	
 
**标签**
`字符串` 


## 
```python

```
>
# 1577.数的平方等于两数乘积的方法数
[https://leetcode-cn.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers](https://leetcode-cn.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers) 
## 原题
给你两个整数数组 `nums1` 和 `nums2` ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：
- 类型 1：三元组 `(i, j, k)` ，如果 `nums1[i]^2 == nums2[j] * nums2[k]` 其中 `0 <= i < nums1.length` 且 `0 <= j < k < nums2.length` 
- 类型 2：三元组 `(i, j, k)` ，如果 `nums2[i]^2 == nums1[j] * nums1[k]` 其中 `0 <= i < nums2.length` 且 `0 <= j < k < nums1.length` 
 

 **示例 1：** 

```
输入：nums1 = [7,4], nums2 = [5,2,8,9]
输出：1
解释：类型 1：(1,1,2), nums1[1]^2 = nums2[1] * nums2[2] (4^2 = 2 * 8)
```
 **示例 2：** 

```
输入：nums1 = [1,1], nums2 = [1,1,1]
输出：9
解释：所有三元组都符合题目要求，因为 1^2 = 1 * 1
类型 1：(0,0,1), (0,0,2), (0,1,2), (1,0,1), (1,0,2), (1,1,2), nums1[i]^2 = nums2[j] * nums2[k]
类型 2：(0,0,1), (1,0,1), (2,0,1), nums2[i]^2 = nums1[j] * nums1[k]

```
 **示例 3：** 

```
输入：nums1 = [7,7,8,3], nums2 = [1,2,9,7]
输出：2
解释：有两个符合题目要求的三元组
类型 1：(3,0,2), nums1[3]^2 = nums2[0] * nums2[2]
类型 2：(3,0,1), nums2[3]^2 = nums1[0] * nums1[1]

```
 **示例 4：** 

```
输入：nums1 = [4,7,9,11,23], nums2 = [3,5,1024,12,18]
输出：0
解释：不存在符合题目要求的三元组

```
 

 **提示：** 
-  `1 <= nums1.length, nums2.length <= 1000` 
-  `1 <= nums1[i], nums2[i] <= 10^5` 
 
**标签**
`数组` `哈希表` `数学` `双指针` 


## 
```python

```
>
# 1578.使绳子变成彩色的最短时间
[https://leetcode-cn.com/problems/minimum-time-to-make-rope-colorful](https://leetcode-cn.com/problems/minimum-time-to-make-rope-colorful) 
## 原题
Alice 把 `n` 个气球排列在一根绳子上。给你一个下标从 **0** 开始的字符串 `colors` ，其中 `colors[i]` 是第 `i` 个气球的颜色。

Alice 想要把绳子装扮成 **彩色** ，且她不希望两个连续的气球涂着相同的颜色，所以她喊来 Bob 帮忙。Bob 可以从绳子上移除一些气球使绳子变成 **彩色** 。给你一个下标从 **0** 开始的整数数组 `neededTime` ，其中 `neededTime[i]` 是 Bob 从绳子上移除第 `i` 个气球需要的时间（以秒为单位）。

返回 Bob 使绳子变成 **彩色** 需要的 **最少时间** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/ballon1.jpg" style="width: 404px; height: 243px;" />
```

输入：colors = "abaac", neededTime = [1,2,3,4,5]
输出：3
解释：在上图中，'a' 是蓝色，'b' 是红色且 'c' 是绿色。
Bob 可以移除下标 2 的蓝色气球。这将花费 3 秒。
移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 3 。
```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon2.jpg" style="width: 244px; height: 243px;" />
```

输入：colors = "abc", neededTime = [1,2,3]
输出：0
解释：绳子已经是彩色的，Bob 不需要从绳子上移除任何气球。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/13/balloon3.jpg" style="width: 404px; height: 243px;" />
```

输入：colors = "aabaa", neededTime = [1,2,3,4,1]
输出：2
解释：Bob 会移除下标 0 和下标 4 处的气球。这两个气球各需要 1 秒来移除。
移除后，不存在两个连续的气球涂着相同的颜色。总时间 = 1 + 1 = 2 。

```
 

 **提示：** 
-  `n == colors.length == neededTime.length` 
-  `1 <= n <= 10^5` 
-  `1 <= neededTime[i] <= 10^4` 
-  `colors` 仅由小写英文字母组成
 
**标签**
`贪心` `数组` `字符串` `动态规划` 


## 
```python

```
>
# 1579.保证图可完全遍历
[https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable](https://leetcode-cn.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable) 
## 原题
Alice 和 Bob 共有一个无向图，其中包含 n 个节点和 3  种类型的边：
- 类型 1：只能由 Alice 遍历。
- 类型 2：只能由 Bob 遍历。
- 类型 3：Alice 和 Bob 都可以遍历。
给你一个数组 `edges` ，其中 `edges[i] = [type<sub>i</sub>, u<sub>i</sub>, v<sub>i</sub>]` 表示节点 `u<sub>i</sub>` 和 `v<sub>i</sub>` 之间存在类型为 `type<sub>i</sub>` 的双向边。请你在保证图仍能够被 Alice和 Bob 完全遍历的前提下，找出可以删除的最大边数。如果从任何节点开始，Alice 和 Bob 都可以到达所有其他节点，则认为图是可以完全遍历的。

返回可以删除的最大边数，如果 Alice 和 Bob 无法完全遍历图，则返回 -1 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/06/5510ex1.png" style="height: 191px; width: 179px;">** 

```
输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
输出：2
解释：如果删除 [1,1,2] 和 [1,1,3] 这两条边，Alice 和 Bob 仍然可以完全遍历这个图。再删除任何其他的边都无法保证图可以完全遍历。所以可以删除的最大边数是 2 。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/06/5510ex2.png" style="height: 190px; width: 178px;">** 

```
输入：n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
输出：0
解释：注意，删除任何一条边都会使 Alice 和 Bob 无法完全遍历这个图。

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/06/5510ex3.png" style="height: 190px; width: 178px;">** 

```
输入：n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
输出：-1
解释：在当前图中，Alice 无法从其他节点到达节点 4 。类似地，Bob 也不能达到节点 1 。因此，图无法完全遍历。
```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)` 
-  `edges[i].length == 3` 
-  `1 <= edges[i][0] <= 3` 
-  `1 <= edges[i][1] < edges[i][2] <= n` 
- 所有元组 `(type<sub>i</sub>, u<sub>i</sub>, v<sub>i</sub>)` 互不相同
 
**标签**
`并查集` `图` 


## 
```python

```
>
# 1580.把箱子放进仓库里 II
[https://leetcode-cn.com/problems/put-boxes-into-the-warehouse-ii](https://leetcode-cn.com/problems/put-boxes-into-the-warehouse-ii) 
## 原题

 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1581.进店却未进行过交易的顾客
[https://leetcode-cn.com/problems/customer-who-visited-but-did-not-make-any-transactions](https://leetcode-cn.com/problems/customer-who-visited-but-did-not-make-any-transactions) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1582.二进制矩阵中的特殊位置
[https://leetcode-cn.com/problems/special-positions-in-a-binary-matrix](https://leetcode-cn.com/problems/special-positions-in-a-binary-matrix) 
## 原题
给你一个大小为 `rows x cols` 的矩阵 `mat` ，其中 `mat[i][j]` 是 `0` 或 `1` ，请返回 **矩阵 *`mat`* 中特殊位置的数目** 。

 **特殊位置** 定义：如果 `mat[i][j] == 1` 并且第 `i` 行和第 `j` 列中的所有其他元素均为 `0` （行和列的下标均 **从 0 开始** ），则位置 `(i, j)` 被称为特殊位置。

 

 **示例 1：** 

```
输入：mat = [[1,0,0],
            [0,0,1],
            [1,0,0]]
输出：1
解释：(1,2) 是一个特殊位置，因为 mat[1][2] == 1 且所处的行和列上所有其他元素都是 0

```
 **示例 2：** 

```
输入：mat = [[1,0,0],
            [0,1,0],
            [0,0,1]]
输出：3
解释：(0,0), (1,1) 和 (2,2) 都是特殊位置

```
 **示例 3：** 

```
输入：mat = [[0,0,0,1],
            [1,0,0,0],
            [0,1,1,0],
            [0,0,0,0]]
输出：2

```
 **示例 4：** 

```
输入：mat = [[0,0,0,0,0],
            [1,0,0,0,0],
            [0,1,0,0,0],
            [0,0,1,0,0],
            [0,0,0,1,1]]
输出：3

```
 

 **提示：** 
-  `rows == mat.length` 
-  `cols == mat[i].length` 
-  `1 <= rows, cols <= 100` 
-  `mat[i][j]` 是 `0` 或 `1` 
 
**标签**
`数组` `矩阵` 


## 
```python

```
>
# 1583.统计不开心的朋友
[https://leetcode-cn.com/problems/count-unhappy-friends](https://leetcode-cn.com/problems/count-unhappy-friends) 
## 原题
给你一份 `n` 位朋友的亲近程度列表，其中 `n` 总是 **偶数** 。

对每位朋友 `i` ， `preferences[i]` 包含一份 **按亲近程度从高** **到低排列** 的朋友列表。换句话说，排在列表前面的朋友与 `i` 的亲近程度比排在列表后面的朋友更高。每个列表中的朋友均以 `0` 到 `n-1` 之间的整数表示。

所有的朋友被分成几对，配对情况以列表 `pairs` 给出，其中 `pairs[i] = [x<sub>i</sub>, y<sub>i</sub>]` 表示 `x<sub>i</sub>` 与 `y<sub>i</sub>` 配对，且 `y<sub>i</sub>` 与 `x<sub>i</sub>` 配对。

但是，这样的配对情况可能会使其中部分朋友感到不开心。在 `x` 与 `y` 配对且 `u` 与 `v` 配对的情况下，如果同时满足下述两个条件， `x` 就会不开心：
-  `x` 与 `u` 的亲近程度胜过 `x` 与 `y` ，且
-  `u` 与 `x` 的亲近程度胜过 `u` 与 `v` 
返回 **不开心的朋友的数目** 。

 

 **示例 1：** 

```

输入：n = 4, preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]], pairs = [[0, 1], [2, 3]]
输出：2
解释：
朋友 1 不开心，因为：
- 1 与 0 配对，但 1 与 3 的亲近程度比 1 与 0 高，且
- 3 与 1 的亲近程度比 3 与 2 高。
朋友 3 不开心，因为：
- 3 与 2 配对，但 3 与 1 的亲近程度比 3 与 2 高，且
- 1 与 3 的亲近程度比 1 与 0 高。
朋友 0 和 2 都是开心的。

```
 **示例 2：** 

```

输入：n = 2, preferences = [[1], [0]], pairs = [[1, 0]]
输出：0
解释：朋友 0 和 1 都开心。

```
 **示例 3：** 

```

输入：n = 4, preferences = [[1, 3, 2], [2, 3, 0], [1, 3, 0], [0, 2, 1]], pairs = [[1, 3], [0, 2]]
输出：4

```
 

 **提示：** 
-  `2 <= n <= 500` 
-  `n` 是偶数
-  `preferences.length == n` 
-  `preferences[i].length == n - 1` 
-  `0 <= preferences[i][j] <= n - 1` 
-  `preferences[i]` 不包含 `i` 
-  `preferences[i]` 中的所有值都是独一无二的
-  `pairs.length == n/2` 
-  `pairs[i].length == 2` 
-  `x<sub>i</sub> != y<sub>i</sub>` 
-  `0 <= x<sub>i</sub>, y<sub>i</sub> <= n - 1` 
- 每位朋友都 **恰好** 被包含在一对中
 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 1584.连接所有点的最小费用
[https://leetcode-cn.com/problems/min-cost-to-connect-all-points](https://leetcode-cn.com/problems/min-cost-to-connect-all-points) 
## 原题
给你一个 `points` 数组，表示 2D 平面上的一些点，其中 `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` 。

连接点 `[x<sub>i</sub>, y<sub>i</sub>]` 和点 `[x<sub>j</sub>, y<sub>j</sub>]` 的费用为它们之间的 **曼哈顿距离** ： `|x<sub>i</sub> - x<sub>j</sub>| + |y<sub>i</sub> - y<sub>j</sub>|` ，其中 `|val|` 表示 `val` 的绝对值。

请你返回将所有点连接的最小总费用。只有任意两点之间 **有且仅有** 一条简单路径时，才认为所有点都已连接。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/d.png" style="height:268px; width:214px; background:#e5e5e5" />

```

输入：points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
输出：20
解释：
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/26/c.png" style="height:268px; width:214px; background:#e5e5e5" />
我们可以按照上图所示连接所有点得到最小总费用，总费用为 20 。
注意到任意两个点之间只有唯一一条路径互相到达。

```
 **示例 2：** 

```

输入：points = [[3,12],[-2,5],[-4,1]]
输出：18

```
 **示例 3：** 

```

输入：points = [[0,0],[1,1],[1,0],[-1,1]]
输出：4

```
 **示例 4：** 

```

输入：points = [[-1000000,-1000000],[1000000,1000000]]
输出：4000000

```
 **示例 5：** 

```

输入：points = [[0,0]]
输出：0

```
 

 **提示：** 
-  `1 <= points.length <= 1000` 
-  `-10^6 <= x<sub>i</sub>, y<sub>i</sub> <= 10^6` 
- 所有点 `(x<sub>i</sub>, y<sub>i</sub>)` 两两不同。
 
**标签**
`并查集` `数组` `最小生成树` 


## 
```python

```
>
# 1585.检查字符串是否可以通过排序子字符串得到另一个字符串
[https://leetcode-cn.com/problems/check-if-string-is-transformable-with-substring-sort-operations](https://leetcode-cn.com/problems/check-if-string-is-transformable-with-substring-sort-operations) 
## 原题
给你两个字符串 `s` 和 `t` ，请你通过若干次以下操作将字符串 `s` 转化成字符串 `t` ：
- 选择 `s` 中一个 **非空** 子字符串并将它包含的字符就地 **升序** 排序。
比方说，对下划线所示的子字符串进行操作可以由 `"1 **4234** "` 得到 `"1 **2344** "` 。

如果可以将字符串 `s` 变成 `t` ，返回 `true` 。否则，返回 `false` 。

一个 **子字符串** 定义为一个字符串中连续的若干字符。

 

 **示例 1：** 

```

输入：s = "84532", t = "34852"
输出：true
解释：你可以按以下操作将 s 转变为 t ：
"84532" （从下标 2 到下标 3）-> "84352"
"84352" （从下标 0 到下标 2） -> "34852"

```
 **示例 2：** 

```

输入：s = "34521", t = "23415"
输出：true
解释：你可以按以下操作将 s 转变为 t ：
"34521" -> "23451"
"23451" -> "23415"

```
 **示例 3：** 

```

输入：s = "12345", t = "12435"
输出：false

```
 **示例 4：** 

```

输入：s = "1", t = "2"
输出：false

```
 

 **提示：** 
-  `s.length == t.length` 
-  `1 <= s.length <= 10^5` 
-  `s` 和 `t` 都只包含数字字符，即 `';0';` 到 `';9';` 。
 
**标签**
`贪心` `字符串` `排序` 


## 
```python

```
>
# 1586.二叉搜索树迭代器 II
[https://leetcode-cn.com/problems/binary-search-tree-iterator-ii](https://leetcode-cn.com/problems/binary-search-tree-iterator-ii) 
## 原题

 
**标签**
`栈` `树` `设计` `二叉搜索树` `二叉树` `迭代器` 


## 
```python

```
>
# 1587.银行账户概要 II
[https://leetcode-cn.com/problems/bank-account-summary-ii](https://leetcode-cn.com/problems/bank-account-summary-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1588.所有奇数长度子数组的和
[https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays](https://leetcode-cn.com/problems/sum-of-all-odd-length-subarrays) 
## 原题
给你一个正整数数组 `arr` ，请你计算所有可能的奇数长度子数组的和。

 **子数组** 定义为原数组中的一个连续子序列。

请你返回 `arr` 中 **所有奇数长度子数组的和** 。

 

 **示例 1：** 

```
输入：arr = [1,4,2,5,3]
输出：58
解释：所有奇数长度子数组和它们的和为：
[1] = 1
[4] = 4
[2] = 2
[5] = 5
[3] = 3
[1,4,2] = 7
[4,2,5] = 11
[2,5,3] = 10
[1,4,2,5,3] = 15
我们将所有值求和得到 1 + 4 + 2 + 5 + 3 + 7 + 11 + 10 + 15 = 58
```
 **示例 2：** 

```
输入：arr = [1,2]
输出：3
解释：总共只有 2 个长度为奇数的子数组，[1] 和 [2]。它们的和为 3 。
```
 **示例 3：** 

```
输入：arr = [10,11,12]
输出：66

```
 

 **提示：** 
-  `1 <= arr.length <= 100` 
-  `1 <= arr[i] <= 1000` 
 
**标签**
`数组` `数学` `前缀和` 


## 
```python

```
>
# 1589.所有排列中的最大和
[https://leetcode-cn.com/problems/maximum-sum-obtained-of-any-permutation](https://leetcode-cn.com/problems/maximum-sum-obtained-of-any-permutation) 
## 原题
有一个整数数组 `nums` ，和一个查询数组 `requests` ，其中 `requests[i] = [start<sub>i</sub>, end<sub>i</sub>]` 。第 `i` 个查询求 `nums[start<sub>i</sub>] + nums[start<sub>i</sub> + 1] + ... + nums[end<sub>i</sub> - 1] + nums[end<sub>i</sub>]` 的结果 ， `start<sub>i</sub>` 和 `end<sub>i</sub>` 数组索引都是 **从 0 开始** 的。

你可以任意排列 `nums` 中的数字，请你返回所有查询结果之和的最大值。

由于答案可能会很大，请你将它对 `10^9 + 7` **取余** 后返回。

 

 **示例 1：** 

```
输入：nums = [1,2,3,4,5], requests = [[1,3],[0,1]]
输出：19
解释：一个可行的 nums 排列为 [2,1,3,4,5]，并有如下结果：
requests[0] -> nums[1] + nums[2] + nums[3] = 1 + 3 + 4 = 8
requests[1] -> nums[0] + nums[1] = 2 + 1 = 3
总和为：8 + 3 = 11。
一个总和更大的排列为 [3,5,4,2,1]，并有如下结果：
requests[0] -> nums[1] + nums[2] + nums[3] = 5 + 4 + 2 = 11
requests[1] -> nums[0] + nums[1] = 3 + 5  = 8
总和为： 11 + 8 = 19，这个方案是所有排列中查询之和最大的结果。

```
 **示例 2：** 

```
输入：nums = [1,2,3,4,5,6], requests = [[0,1]]
输出：11
解释：一个总和最大的排列为 [6,5,4,3,2,1] ，查询和为 [11]。
```
 **示例 3：** 

```
输入：nums = [1,2,3,4,5,10], requests = [[0,2],[1,3],[1,1]]
输出：47
解释：一个和最大的排列为 [4,10,5,3,2,1] ，查询结果分别为 [19,18,10]。
```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 10^5` 
-  `0 <= nums[i] <= 10^5` 
-  `1 <= requests.length <= 10^5` 
-  `requests[i].length == 2` 
-  `0 <= start<sub>i</sub> <= end<sub>i</sub> < n` 
 
**标签**
`贪心` `数组` `前缀和` `排序` 


## 
```python

```
>
# 1590.使数组和能被 P 整除
[https://leetcode-cn.com/problems/make-sum-divisible-by-p](https://leetcode-cn.com/problems/make-sum-divisible-by-p) 
## 原题
给你一个正整数数组 `nums` ，请你移除 **最短** 子数组（可以为 **空** ），使得剩余元素的 **和** 能被 `p` 整除。 **不允许** 将整个数组都移除。

请你返回你需要移除的最短子数组的长度，如果无法满足题目要求，返回 `-1` 。

 **子数组** 定义为原数组中连续的一组元素。

 

 **示例 1：** 

```
输入：nums = [3,1,4,2], p = 6
输出：1
解释：nums 中元素和为 10，不能被 p 整除。我们可以移除子数组 [4] ，剩余元素的和为 6 。

```
 **示例 2：** 

```
输入：nums = [6,3,5,2], p = 9
输出：2
解释：我们无法移除任何一个元素使得和被 9 整除，最优方案是移除子数组 [5,2] ，剩余元素为 [6,3]，和为 9 。

```
 **示例 3：** 

```
输入：nums = [1,2,3], p = 3
输出：0
解释：和恰好为 6 ，已经能被 3 整除了。所以我们不需要移除任何元素。

```
 **示例  4：** 

```
输入：nums = [1,2,3], p = 7
输出：-1
解释：没有任何方案使得移除子数组后剩余元素的和被 7 整除。

```
 **示例 5：** 

```
输入：nums = [1000000000,1000000000,1000000000], p = 3
输出：0

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^9` 
-  `1 <= p <= 10^9` 
 
**标签**
`数组` `哈希表` `前缀和` 


## 
```python

```
>
# 1591.奇怪的打印机 II
[https://leetcode-cn.com/problems/strange-printer-ii](https://leetcode-cn.com/problems/strange-printer-ii) 
## 原题
给你一个奇怪的打印机，它有如下两个特殊的打印规则：
- 每一次操作时，打印机会用同一种颜色打印一个矩形的形状，每次打印会覆盖矩形对应格子里原本的颜色。
- 一旦矩形根据上面的规则使用了一种颜色，那么 **相同的颜色不能再被使用** 。
给你一个初始没有颜色的 `m x n` 的矩形 `targetGrid` ，其中 `targetGrid[row][col]` 是位置 `(row, col)` 的颜色。

如果你能按照上述规则打印出矩形 `targetGrid` ，请你返回 `true` ，否则返回 `false` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/19/sample_1_1929.png" style="height: 138px; width: 483px;">

```
输入：targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
输出：true

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/19/sample_2_1929.png" style="height: 290px; width: 483px;">

```
输入：targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
输出：true

```
 **示例 3：** 

```
输入：targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
输出：false
解释：没有办法得到 targetGrid ，因为每一轮操作使用的颜色互不相同。
```
 **示例 4：** 

```
输入：targetGrid = [[1,1,1],[3,1,3]]
输出：false

```
 

 **提示：** 
-  `m == targetGrid.length` 
-  `n == targetGrid[i].length` 
-  `1 <= m, n <= 60` 
-  `1 <= targetGrid[row][col] <= 60` 
 
**标签**
`图` `拓扑排序` `数组` `矩阵` 


## 
```python

```
>
# 1592.重新排列单词间的空格
[https://leetcode-cn.com/problems/rearrange-spaces-between-words](https://leetcode-cn.com/problems/rearrange-spaces-between-words) 
## 原题
给你一个字符串 `text` ，该字符串由若干被空格包围的单词组成。每个单词由一个或者多个小写英文字母组成，并且两个单词之间至少存在一个空格。题目测试用例保证 `text` **至少包含一个单词** 。

请你重新排列空格，使每对相邻单词之间的空格数目都 **相等** ，并尽可能 **最大化** 该数目。如果不能重新平均分配所有空格，请 **将多余的空格放置在字符串末尾** ，这也意味着返回的字符串应当与原 `text` 字符串的长度相等。

返回 **重新排列空格后的字符串** 。

 

 **示例 1：** 

```
输入：text = "  this   is  a sentence "
输出："this   is   a   sentence"
解释：总共有 9 个空格和 4 个单词。可以将 9 个空格平均分配到相邻单词之间，相邻单词间空格数为：9 / (4-1) = 3 个。

```
 **示例 2：** 

```
输入：text = " practice   makes   perfect"
输出："practice   makes   perfect "
解释：总共有 7 个空格和 3 个单词。7 / (3-1) = 3 个空格加上 1 个多余的空格。多余的空格需要放在字符串的末尾。

```
 **示例 3：** 

```
输入：text = "hello   world"
输出："hello   world"

```
 **示例 4：** 

```
输入：text = "  walks  udp package   into  bar a"
输出："walks  udp  package  into  bar  a "

```
 **示例 5：** 

```
输入：text = "a"
输出："a"

```
 

 **提示：** 
-  `1 <= text.length <= 100` 
-  `text` 由小写英文字母和 `'; ';` 组成
-  `text` 中至少包含一个单词
 
**标签**
`字符串` 


## 
```python

```
>
# 1593.拆分字符串使唯一子字符串的数目最大
[https://leetcode-cn.com/problems/split-a-string-into-the-max-number-of-unique-substrings](https://leetcode-cn.com/problems/split-a-string-into-the-max-number-of-unique-substrings) 
## 原题
给你一个字符串 `s` ，请你拆分该字符串，并返回拆分后唯一子字符串的最大数目。

字符串 `s` 拆分后可以得到若干 **非空子字符串** ，这些子字符串连接后应当能够还原为原字符串。但是拆分出来的每个子字符串都必须是 **唯一的** 。

注意： **子字符串** 是字符串中的一个连续字符序列。

 

 **示例 1：** 

```
输入：s = "ababccc"
输出：5
解释：一种最大拆分方法为 [';a';, ';b';, ';ab';, ';c';, ';cc';] 。像 [';a';, ';b';, ';a';, ';b';, ';c';, ';cc';] 这样拆分不满足题目要求，因为其中的 ';a'; 和 ';b'; 都出现了不止一次。

```
 **示例 2：** 

```
输入：s = "aba"
输出：2
解释：一种最大拆分方法为 [';a';, ';ba';] 。

```
 **示例 3：** 

```
输入：s = "aa"
输出：1
解释：无法进一步拆分字符串。

```
 

 **提示：** 
- 
	 `1 <= s.length <= 16` 
	
- 
	 `s` 仅包含小写英文字母
	
 
**标签**
`哈希表` `字符串` `回溯` 


## 
```python

```
>
# 1594.矩阵的最大非负积
[https://leetcode-cn.com/problems/maximum-non-negative-product-in-a-matrix](https://leetcode-cn.com/problems/maximum-non-negative-product-in-a-matrix) 
## 原题
给你一个大小为 `rows x cols` 的矩阵 `grid` 。最初，你位于左上角 `(0, 0)` ，每一步，你可以在矩阵中 **向右** 或 **向下** 移动。

在从左上角 `(0, 0)` 开始到右下角 `(rows - 1, cols - 1)` 结束的所有路径中，找出具有 **最大非负积** 的路径。路径的积是沿路径访问的单元格中所有整数的乘积。

返回 **最大非负积** 对 ** `10^9 + 7` ** **取余** 的结果。如果最大积为负数，则返回 `-1` 。

 **注意，** 取余是在得到最大积之后执行的。

 

 **示例 1：** 

```
输入：grid = [[-1,-2,-3],
             [-2,-3,-3],
             [-3,-3,-2]]
输出：-1
解释：从 (0, 0) 到 (2, 2) 的路径中无法得到非负积，所以返回 -1

```
 **示例 2：** 

```
输入：grid = [[1,-2,1],
             [1,-2,1],
             [3,-4,1]]
输出：8
解释：最大非负积对应的路径已经用粗体标出 (1 * 1 * -2 * -4 * 1 = 8)

```
 **示例 3：** 

```
输入：grid = [[1, 3],
             [0,-4]]
输出：0
解释：最大非负积对应的路径已经用粗体标出 (1 * 0 * -4 = 0)

```
 **示例 4：** 

```
输入：grid = [[ 1, 4,4,0],
             [-2, 0,0,1],
             [ 1,-1,1,1]]
输出：2
解释：最大非负积对应的路径已经用粗体标出 (1 * -2 * 1 * -1 * 1 * 1 = 2)

```
 

 **提示：** 
-  `1 <= rows, cols <= 15` 
-  `-4 <= grid[i][j] <= 4` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 1595.连通两组点的最小成本
[https://leetcode-cn.com/problems/minimum-cost-to-connect-two-groups-of-points](https://leetcode-cn.com/problems/minimum-cost-to-connect-two-groups-of-points) 
## 原题
给你两组点，其中第一组中有 `size<sub>1</sub>` 个点，第二组中有 `size<sub>2</sub>` 个点，且 `size<sub>1</sub> >= size<sub>2</sub>` 。

任意两点间的连接成本 `cost` 由大小为 `size<sub>1</sub> x size<sub>2</sub>` 矩阵给出，其中 `cost[i][j]` 是第一组中的点 `i` 和第二组中的点 `j` 的连接成本。 **如果两个组中的每个点都与另一组中的一个或多个点连接，则称这两组点是连通的。** 换言之，第一组中的每个点必须至少与第二组中的一个点连接，且第二组中的每个点必须至少与第一组中的一个点连接。

返回连通两组点所需的最小成本。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/20/ex1.jpg" style="height: 243px; width: 322px;">

```
输入：cost = [[15, 96], [36, 2]]
输出：17
解释：连通两组点的最佳方法是：
1--A
2--B
总成本为 17 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/20/ex2.jpg" style="height: 403px; width: 322px;">

```
输入：cost = [[1, 3, 5], [4, 1, 1], [1, 5, 3]]
输出：4
解释：连通两组点的最佳方法是：
1--A
2--B
2--C
3--A
最小成本为 4 。
请注意，虽然有多个点连接到第一组中的点 2 和第二组中的点 A ，但由于题目并不限制连接点的数目，所以只需要关心最低总成本。
```
 **示例 3：** 

```
输入：cost = [[2, 5, 1], [3, 4, 7], [8, 1, 2], [6, 2, 4], [3, 8, 8]]
输出：10

```
 

 **提示：** 
-  `size<sub>1</sub> == cost.length` 
-  `size<sub>2</sub> == cost[i].length` 
-  `1 <= size<sub>1</sub>, size<sub>2</sub> <= 12` 
-  `size<sub>1</sub> >= size<sub>2</sub>` 
-  `0 <= cost[i][j] <= 100` 
 
**标签**
`位运算` `数组` `动态规划` `状态压缩` `矩阵` 


## 
```python

```
>
# 1596.每位顾客最经常订购的商品
[https://leetcode-cn.com/problems/the-most-frequently-ordered-products-for-each-customer](https://leetcode-cn.com/problems/the-most-frequently-ordered-products-for-each-customer) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1597.根据中缀表达式构造二叉表达式树
[https://leetcode-cn.com/problems/build-binary-expression-tree-from-infix-expression](https://leetcode-cn.com/problems/build-binary-expression-tree-from-infix-expression) 
## 原题

 
**标签**
`栈` `树` `字符串` `二叉树` 


## 
```python

```
>
# 1598.文件夹操作日志搜集器
[https://leetcode-cn.com/problems/crawler-log-folder](https://leetcode-cn.com/problems/crawler-log-folder) 
## 原题
每当用户执行变更文件夹操作时，LeetCode 文件系统都会保存一条日志记录。

下面给出对变更操作的说明：
-  `"../"` ：移动到当前文件夹的父文件夹。如果已经在主文件夹下，则 **继续停留在当前文件夹** 。
-  `"./"` ：继续停留在当前文件夹 **。** 
-  `"x/"` ：移动到名为 `x` 的子文件夹中。题目数据 **保证总是存在文件夹 `x` ** 。
给你一个字符串列表 `logs` ，其中 `logs[i]` 是用户在 `i^th` 步执行的操作。

文件系统启动时位于主文件夹，然后执行 `logs` 中的操作。

执行完所有变更文件夹操作后，请你找出 **返回主文件夹所需的最小步数** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/sample_11_1957.png" style="height: 151px; width: 775px;">

```
输入：logs = ["d1/","d2/","../","d21/","./"]
输出：2
解释：执行 "../" 操作变更文件夹 2 次，即可回到主文件夹

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/sample_22_1957.png" style="height: 270px; width: 600px;">

```
输入：logs = ["d1/","d2/","./","d3/","../","d31/"]
输出：3

```
 **示例 3：** 

```
输入：logs = ["d1/","../","../","../"]
输出：0

```
 

 **提示：** 
-  `1 <= logs.length <= 10^3` 
-  `2 <= logs[i].length <= 10` 
-  `logs[i]` 包含小写英文字母，数字， `';.';` 和 `';/';` 
-  `logs[i]` 符合语句中描述的格式
- 文件夹名称由小写英文字母和数字组成
 
**标签**
`栈` `数组` `字符串` 


## 
```python

```
>
# 1599.经营摩天轮的最大利润
[https://leetcode-cn.com/problems/maximum-profit-of-operating-a-centennial-wheel](https://leetcode-cn.com/problems/maximum-profit-of-operating-a-centennial-wheel) 
## 原题
你正在经营一座摩天轮，该摩天轮共有 **4 个座舱** ，每个座舱 **最多可以容纳 4 位游客** 。你可以 **逆时针** 轮转座舱，但每次轮转都需要支付一定的运行成本 `runningCost` 。摩天轮每次轮转都恰好转动 1 / 4 周。

给你一个长度为 `n` 的数组 `customers` ， `customers[i]` 是在第 `i` 次轮转（下标从 0 开始）之前到达的新游客的数量。这也意味着你必须在新游客到来前轮转 `i` 次。每位游客在登上离地面最近的座舱前都会支付登舱成本 `boardingCost` ，一旦该座舱再次抵达地面，他们就会离开座舱结束游玩。

你可以随时停下摩天轮，即便是 **在服务所有游客之前** 。如果你决定停止运营摩天轮，为了保证所有游客安全着陆， **将免费进行** **所有后续轮转** 。注意，如果有超过 4 位游客在等摩天轮，那么只有 4 位游客可以登上摩天轮，其余的需要等待 **下一次轮转** 。

返回最大化利润所需执行的 **最小轮转次数** 。 如果不存在利润为正的方案，则返回 `-1` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/wheeldiagram12.png" style="height: 291px; width: 906px;">

```
输入：customers = [8,3], boardingCost = 5, runningCost = 6
输出：3
解释：座舱上标注的数字是该座舱的当前游客数。
1. 8 位游客抵达，4 位登舱，4 位等待下一舱，摩天轮轮转。当前利润为 4 * $5 - 1 * $6 = $14 。
2. 3 位游客抵达，4 位在等待的游客登舱，其他 3 位等待，摩天轮轮转。当前利润为 8 * $5 - 2 * $6 = $28 。
3. 最后 3 位游客登舱，摩天轮轮转。当前利润为 11 * $5 - 3 * $6 = $37 。
轮转 3 次得到最大利润，最大利润为 $37 。
```
 **示例 2：** 

```
输入：customers = [10,9,6], boardingCost = 6, runningCost = 4
输出：7
解释：
1. 10 位游客抵达，4 位登舱，6 位等待下一舱，摩天轮轮转。当前利润为 4 * $6 - 1 * $4 = $20 。
2. 9 位游客抵达，4 位登舱，11 位等待（2 位是先前就在等待的，9 位新加入等待的），摩天轮轮转。当前利润为 8 * $6 - 2 * $4 = $40 。
3. 最后 6 位游客抵达，4 位登舱，13 位等待，摩天轮轮转。当前利润为 12 * $6 - 3 * $4 = $60 。
4. 4 位登舱，9 位等待，摩天轮轮转。当前利润为 * $6 - 4 * $4 = $80 。
5. 4 位登舱，5 位等待，摩天轮轮转。当前利润为 20 * $6 - 5 * $4 = $100 。
6. 4 位登舱，1 位等待，摩天轮轮转。当前利润为 24 * $6 - 6 * $4 = $120 。
7. 1 位登舱，摩天轮轮转。当前利润为 25 * $6 - 7 * $4 = $122 。
轮转 7 次得到最大利润，最大利润为$122 。

```
 **示例 3：** 

```
输入：customers = [3,4,0,5,1], boardingCost = 1, runningCost = 92
输出：-1
解释：
1. 3 位游客抵达，3 位登舱，0 位等待，摩天轮轮转。当前利润为 3 * $1 - 1 * $92 = -$89 。
2. 4 位游客抵达，4 位登舱，0 位等待，摩天轮轮转。当前利润为 is 7 * $1 - 2 * $92 = -$177 。
3. 0 位游客抵达，0 位登舱，0 位等待，摩天轮轮转。当前利润为 7 * $1 - 3 * $92 = -$269 。
4. 5 位游客抵达，4 位登舱，1 位等待，摩天轮轮转。当前利润为 12 * $1 - 4 * $92 = -$356 。
5. 1 位游客抵达，2 位登舱，0 位等待，摩天轮轮转。当前利润为 13 * $1 - 5 * $92 = -$447 。
利润永不为正，所以返回 -1 。

```
 **示例 4：** 

```
输入：customers = [10,10,6,4,7], boardingCost = 3, runningCost = 8
输出：9
解释：
1. 10 位游客抵达，4 位登舱，6 位等待，摩天轮轮转。当前利润为 4 * $3 - 1 * $8 = $4 。
2. 10 位游客抵达，4 位登舱，12 位等待，摩天轮轮转。当前利润为 8 * $3 - 2 * $8 = $8 。
3. 6 位游客抵达，4 位登舱，14 位等待，摩天轮轮转。当前利润为 12 * $3 - 3 * $8 = $12 。
4. 4 位游客抵达，4 位登舱，14 位等待，摩天轮轮转。当前利润为 16 * $3 - 4 * $8 = $16 。
5. 7 位游客抵达，4 位登舱，17 位等待，摩天轮轮转。当前利润为 20 * $3 - 5 * $8 = $20 。
6. 4 位登舱，13 位等待，摩天轮轮转。当前利润为 24 * $3 - 6 * $8 = $24 。
7. 4 位登舱，9 位等待，摩天轮轮转。当前利润为 28 * $3 - 7 * $8 = $28 。
8. 4 位登舱，5 位等待，摩天轮轮转。当前利润为 32 * $3 - 8 * $8 = $32 。
9. 4 位登舱，1 位等待，摩天轮轮转。当前利润为 36 * $3 - 9 * $8 = $36 。
​​​​​​​10. 1 位登舱，0 位等待，摩天轮轮转。当前利润为 37 * $3 - 10 * $8 = $31 。
轮转 9 次得到最大利润，最大利润为 $36 。

```
 

 **提示：** 
-  `n == customers.length` 
-  `1 <= n <= 10^5` 
-  `0 <= customers[i] <= 50` 
-  `1 <= boardingCost, runningCost <= 100` 
 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 1600.皇位继承顺序
[https://leetcode-cn.com/problems/throne-inheritance](https://leetcode-cn.com/problems/throne-inheritance) 
## 原题
一个王国里住着国王、他的孩子们、他的孙子们等等。每一个时间点，这个家庭里有人出生也有人死亡。

这个王国有一个明确规定的皇位继承顺序，第一继承人总是国王自己。我们定义递归函数 `Successor(x, curOrder)` ，给定一个人 `x` 和当前的继承顺序，该函数返回 `x` 的下一继承人。

```
Successor(x, curOrder):
    如果 x 没有孩子或者所有 x 的孩子都在 curOrder 中：
        如果 x 是国王，那么返回 null
        否则，返回 Successor(x 的父亲, curOrder)
    否则，返回 x 不在 curOrder 中最年长的孩子

```
比方说，假设王国由国王，他的孩子 Alice 和 Bob （Alice 比 Bob 年长）和 Alice 的孩子 Jack 组成。
- 一开始， `curOrder` 为 `["king"]` .
- 调用 `Successor(king, curOrder)` ，返回 Alice ，所以我们将 Alice 放入 `curOrder` 中，得到 `["king", "Alice"]` 。
- 调用 `Successor(Alice, curOrder)` ，返回 Jack ，所以我们将 Jack 放入 `curOrder` 中，得到 `["king", "Alice", "Jack"]` 。
- 调用 `Successor(Jack, curOrder)` ，返回 Bob ，所以我们将 Bob 放入 `curOrder` 中，得到 `["king", "Alice", "Jack", "Bob"]` 。
- 调用 `Successor(Bob, curOrder)` ，返回 `null` 。最终得到继承顺序为 `["king", "Alice", "Jack", "Bob"]` 。
通过以上的函数，我们总是能得到一个唯一的继承顺序。

请你实现 `ThroneInheritance` 类：
-  `ThroneInheritance(string kingName)` 初始化一个 `ThroneInheritance` 类的对象。国王的名字作为构造函数的参数传入。
-  `void birth(string parentName, string childName)` 表示 `parentName` 新拥有了一个名为 `childName` 的孩子。
-  `void death(string name)` 表示名为 `name` 的人死亡。一个人的死亡不会影响 `Successor` 函数，也不会影响当前的继承顺序。你可以只将这个人标记为死亡状态。
-  `string[] getInheritanceOrder()` 返回 **除去** 死亡人员的当前继承顺序列表。
 

 **示例：** 

```
输入：
["ThroneInheritance", "birth", "birth", "birth", "birth", "birth", "birth", "getInheritanceOrder", "death", "getInheritanceOrder"]
[["king"], ["king", "andy"], ["king", "bob"], ["king", "catherine"], ["andy", "matthew"], ["bob", "alex"], ["bob", "asha"], [null], ["bob"], [null]]
输出：
[null, null, null, null, null, null, null, ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"], null, ["king", "andy", "matthew", "alex", "asha", "catherine"]]

解释：
ThroneInheritance t= new ThroneInheritance("king"); // 继承顺序：king
t.birth("king", "andy"); // 继承顺序：king > andy
t.birth("king", "bob"); // 继承顺序：king > andy > bob
t.birth("king", "catherine"); // 继承顺序：king > andy > bob > catherine
t.birth("andy", "matthew"); // 继承顺序：king > andy > matthew > bob > catherine
t.birth("bob", "alex"); // 继承顺序：king > andy > matthew > bob > alex > catherine
t.birth("bob", "asha"); // 继承顺序：king > andy > matthew > bob > alex > asha > catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "bob", "alex", "asha", "catherine"]
t.death("bob"); // 继承顺序：king > andy > matthew > bob（已经去世）> alex > asha > catherine
t.getInheritanceOrder(); // 返回 ["king", "andy", "matthew", "alex", "asha", "catherine"]

```
 

 **提示：** 
-  `1 <= kingName.length, parentName.length, childName.length, name.length <= 15` 
-  `kingName` ， `parentName` ， `childName` 和 `name` 仅包含小写英文字母。
- 所有的参数 `childName` 和 `kingName` **互不相同** 。
- 所有 `death` 函数中的死亡名字 `name` 要么是国王，要么是已经出生了的人员名字。
- 每次调用 `birth(parentName, childName)` 时，测试用例都保证 `parentName` 对应的人员是活着的。
- 最多调用 `10^5` 次 `birth` 和 `death` 。
- 最多调用 `10` 次 `getInheritanceOrder` 。
 
**标签**
`树` `深度优先搜索` `设计` `哈希表` 


## 
```python

```
>
