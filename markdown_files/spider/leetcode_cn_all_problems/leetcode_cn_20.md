# 2001.可互换矩形的组数
[https://leetcode-cn.com/problems/number-of-pairs-of-interchangeable-rectangles](https://leetcode-cn.com/problems/number-of-pairs-of-interchangeable-rectangles) 
## 原题
用一个下标从 **0** 开始的二维整数数组 `rectangles` 来表示 `n` 个矩形，其中 `rectangles[i] = [width<sub>i</sub>, height<sub>i</sub>]` 表示第 `i` 个矩形的宽度和高度。

如果两个矩形 `i` 和 `j` （ `i < j` ）的宽高比相同，则认为这两个矩形 **可互换** 。更规范的说法是，两个矩形满足 `width<sub>i</sub>/height<sub>i</sub> == width<sub>j</sub>/height<sub>j</sub>` （使用实数除法而非整数除法），则认为这两个矩形 **可互换** 。

计算并返回 `rectangles` 中有多少对 **可互换** 矩形。

 

 **示例 1：** 

```

输入：rectangles = [[4,8],[3,6],[10,20],[15,30]]
输出：6
解释：下面按下标（从 0 开始）列出可互换矩形的配对情况：
- 矩形 0 和矩形 1 ：4/8 == 3/6
- 矩形 0 和矩形 2 ：4/8 == 10/20
- 矩形 0 和矩形 3 ：4/8 == 15/30
- 矩形 1 和矩形 2 ：3/6 == 10/20
- 矩形 1 和矩形 3 ：3/6 == 15/30
- 矩形 2 和矩形 3 ：10/20 == 15/30

```
 **示例 2：** 

```

输入：rectangles = [[4,5],[7,8]]
输出：0
解释：不存在成对的可互换矩形。

```
 

 **提示：** 
-  `n == rectangles.length` 
-  `1 <= n <= 10^5` 
-  `rectangles[i].length == 2` 
-  `1 <= width<sub>i</sub>, height<sub>i</sub> <= 10^5` 
 
**标签**
`数组` `哈希表` `数学` `计数` `数论` 


## 
```python

```
>
# 2002.两个回文子序列长度的最大乘积
[https://leetcode-cn.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences](https://leetcode-cn.com/problems/maximum-product-of-the-length-of-two-palindromic-subsequences) 
## 原题
给你一个字符串 `s` ，请你找到 `s` 中两个 **不相交回文子序列** ，使得它们长度的 **乘积最大** 。两个子序列在原字符串中如果没有任何相同下标的字符，则它们是 **不相交** 的。

请你返回两个回文子序列长度可以达到的 **最大乘积** 。

 **子序列** 指的是从原字符串中删除若干个字符（可以一个也不删除）后，剩余字符不改变顺序而得到的结果。如果一个字符串从前往后读和从后往前读一模一样，那么这个字符串是一个 **回文字符串** 。

 

 **示例 1：** 

<img alt="example-1" src="https://assets.leetcode.com/uploads/2021/08/24/two-palindromic-subsequences.png" style="width: 550px; height: 124px;">

```
输入：s = "leetcodecom"
输出：9
解释：最优方案是选择 "ete" 作为第一个子序列，"cdc" 作为第二个子序列。
它们的乘积为 3 * 3 = 9 。

```
 **示例 2：** 

```
输入：s = "bb"
输出：1
解释：最优方案为选择 "b" （第一个字符）作为第一个子序列，"b" （第二个字符）作为第二个子序列。
它们的乘积为 1 * 1 = 1 。

```
 **示例 3：** 

```
输入：s = "accbcaxxcxx"
输出：25
解释：最优方案为选择 "accca" 作为第一个子序列，"xxcxx" 作为第二个子序列。
它们的乘积为 5 * 5 = 25 。

```
 

 **提示：** 
-  `2 <= s.length <= 12` 
-  `s` 只含有小写英文字母。
 
**标签**
`位运算` `字符串` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 2003.每棵子树内缺失的最小基因值
[https://leetcode-cn.com/problems/smallest-missing-genetic-value-in-each-subtree](https://leetcode-cn.com/problems/smallest-missing-genetic-value-in-each-subtree) 
## 原题
有一棵根节点为 `0` 的 **家族树** ，总共包含 `n` 个节点，节点编号为 `0` 到 `n - 1` 。给你一个下标从 **0** 开始的整数数组 `parents` ，其中 `parents[i]` 是节点 `i` 的父节点。由于节点 `0` 是 **根** ，所以 `parents[0] == -1` 。

总共有 `10^5` 个基因值，每个基因值都用 **闭区间** `[1, 10^5]` 中的一个整数表示。给你一个下标从 **0** 开始的整数数组 `nums` ，其中 `nums[i]` 是节点 `i` 的基因值，且基因值 **互不相同** 。

请你返回一个数组 `ans` ，长度为 `n` ，其中 `ans[i]` 是以节点 `i` 为根的子树内 <b>缺失</b> 的 **最小** 基因值。

节点 `x` 为根的 **子树** 包含节点 `x` 和它所有的 **后代** 节点。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/08/23/case-1.png" style="width: 204px; height: 167px;">

```
输入：parents = [-1,0,0,2], nums = [1,2,3,4]
输出：[5,1,1,1]
解释：每个子树答案计算结果如下：
- 0：子树包含节点 [0,1,2,3] ，基因值分别为 [1,2,3,4] 。5 是缺失的最小基因值。
- 1：子树只包含节点 1 ，基因值为 2 。1 是缺失的最小基因值。
- 2：子树包含节点 [2,3] ，基因值分别为 [3,4] 。1 是缺失的最小基因值。
- 3：子树只包含节点 3 ，基因值为 4 。1是缺失的最小基因值。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/08/23/case-2.png" style="width: 247px; height: 168px;">

```
输入：parents = [-1,0,1,0,3,3], nums = [5,4,6,2,1,3]
输出：[7,1,1,4,2,1]
解释：每个子树答案计算结果如下：
- 0：子树内包含节点 [0,1,2,3,4,5] ，基因值分别为 [5,4,6,2,1,3] 。7 是缺失的最小基因值。
- 1：子树内包含节点 [1,2] ，基因值分别为 [4,6] 。 1 是缺失的最小基因值。
- 2：子树内只包含节点 2 ，基因值为 6 。1 是缺失的最小基因值。
- 3：子树内包含节点 [3,4,5] ，基因值分别为 [2,1,3] 。4 是缺失的最小基因值。
- 4：子树内只包含节点 4 ，基因值为 1 。2 是缺失的最小基因值。
- 5：子树内只包含节点 5 ，基因值为 3 。1 是缺失的最小基因值。

```
 **示例 3：** 

```
输入：parents = [-1,2,3,0,2,4,1], nums = [2,3,4,5,6,7,8]
输出：[1,1,1,1,1,1,1]
解释：所有子树都缺失基因值 1 。

```
 

 **提示：** 
-  `n == parents.length == nums.length` 
-  `2 <= n <= 10^5` 
- 对于 `i != 0` ，满足 `0 <= parents[i] <= n - 1` 
-  `parents[0] == -1` 
-  `parents` 表示一棵合法的树。
-  `1 <= nums[i] <= 10^5` 
-  `nums[i]` 互不相同。
 
**标签**
`树` `深度优先搜索` `并查集` `动态规划` 


## 
```python

```
>
# 2005.斐波那契树的移除子树游戏
[https://leetcode-cn.com/problems/subtree-removal-game-with-fibonacci-tree](https://leetcode-cn.com/problems/subtree-removal-game-with-fibonacci-tree) 
## 原题

 
**标签**



## 
```python

```
>
# 2006.差的绝对值为 K 的数对数目
[https://leetcode-cn.com/problems/count-number-of-pairs-with-absolute-difference-k](https://leetcode-cn.com/problems/count-number-of-pairs-with-absolute-difference-k) 
## 原题
给你一个整数数组 `nums` 和一个整数 `k` ，请你返回数对 `(i, j)` 的数目，满足 `i < j` 且 `|nums[i] - nums[j]| == k` 。

 `|x|` 的值定义为：
- 如果 `x >= 0` ，那么值为 `x` 。
- 如果 `x < 0` ，那么值为 `-x` 。
 

 **示例 1：** 

```
输入：nums = [1,2,2,1], k = 1
输出：4
解释：差的绝对值为 1 的数对为：
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]
- [1,2,2,1]

```
 **示例 2：** 

```
输入：nums = [1,3], k = 3
输出：0
解释：没有任何数对差的绝对值为 3 。

```
 **示例 3：** 

```
输入：nums = [3,2,1,5,4], k = 2
输出：3
解释：差的绝对值为 2 的数对为：
- [3,2,1,5,4]
- [3,2,1,5,4]
- [3,2,1,5,4]

```
 

 **提示：** 
-  `1 <= nums.length <= 200` 
-  `1 <= nums[i] <= 100` 
-  `1 <= k <= 99` 
 
**标签**
`数组` `哈希表` `计数` 


## 
```python

```
>
# 2007.从双倍数组中还原原数组
[https://leetcode-cn.com/problems/find-original-array-from-doubled-array](https://leetcode-cn.com/problems/find-original-array-from-doubled-array) 
## 原题
一个整数数组 `original` 可以转变成一个 **双倍** 数组 `changed` ，转变方式为将 `original` 中每个元素 **值乘以 2** 加入数组中，然后将所有元素 **随机打乱** 。

给你一个数组 `changed` ，如果 `change` 是 **双倍** 数组，那么请你返回 `original` 数组，否则请返回空数组。 `original` 的元素可以以 **任意** 顺序返回。

 

 **示例 1：** 

```
输入：changed = [1,3,4,2,6,8]
输出：[1,3,4]
解释：一个可能的 original 数组为 [1,3,4] :
- 将 1 乘以 2 ，得到 1 * 2 = 2 。
- 将 3 乘以 2 ，得到 3 * 2 = 6 。
- 将 4 乘以 2 ，得到 4 * 2 = 8 。
其他可能的原数组方案为 [4,3,1] 或者 [3,1,4] 。

```
 **示例 2：** 

```
输入：changed = [6,3,0,1]
输出：[]
解释：changed 不是一个双倍数组。

```
 **示例 3：** 

```
输入：changed = [1]
输出：[]
解释：changed 不是一个双倍数组。

```
 

 **提示：** 
-  `1 <= changed.length <= 10^5` 
-  `0 <= changed[i] <= 10^5` 
 
**标签**
`贪心` `数组` `哈希表` `排序` 


## 
```python

```
>
# 2008.出租车的最大盈利
[https://leetcode-cn.com/problems/maximum-earnings-from-taxi](https://leetcode-cn.com/problems/maximum-earnings-from-taxi) 
## 原题
你驾驶出租车行驶在一条有 `n` 个地点的路上。这 `n` 个地点从近到远编号为 `1` 到 `n` ，你想要从 `1` 开到 `n` ，通过接乘客订单盈利。你只能沿着编号递增的方向前进，不能改变方向。

乘客信息用一个下标从 **0** 开始的二维数组 `rides` 表示，其中 `rides[i] = [start<sub>i</sub>, end<sub>i</sub>, tip<sub>i</sub>]` 表示第 `i` 位乘客需要从地点 `start<sub>i</sub>` 前往 `end<sub>i</sub>` ，愿意支付 `tip<sub>i</sub>` 元的小费。

 **每一位** 你选择接单的乘客 `i` ，你可以 **盈利** `end<sub>i</sub> - start<sub>i</sub> + tip<sub>i</sub>` 元。你同时 **最多** 只能接一个订单。

给你 `n` 和 `rides` ，请你返回在最优接单方案下，你能盈利 **最多** 多少元。

 **注意：** 你可以在一个地点放下一位乘客，并在同一个地点接上另一位乘客。

 

 **示例 1：** 

```
输入：n = 5, rides = [[2,5,4],[1,5,1]]
输出：7
解释：我们可以接乘客 0 的订单，获得 5 - 2 + 4 = 7 元。

```
 **示例 2：** 

```
输入：n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
输出：20
解释：我们可以接以下乘客的订单：
- 将乘客 1 从地点 3 送往地点 10 ，获得 10 - 3 + 2 = 9 元。
- 将乘客 2 从地点 10 送往地点 12 ，获得 12 - 10 + 3 = 5 元。
- 将乘客 5 从地点 13 送往地点 18 ，获得 18 - 13 + 1 = 6 元。
我们总共获得 9 + 5 + 6 = 20 元。
```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `1 <= rides.length <= 3 * 10^4` 
-  `rides[i].length == 3` 
-  `1 <= start<sub>i</sub> < end<sub>i</sub> <= n` 
-  `1 <= tip<sub>i</sub> <= 10^5` 
 
**标签**
`数组` `二分查找` `动态规划` `排序` 


## 
```python

```
>
# 2009.使数组连续的最少操作数
[https://leetcode-cn.com/problems/minimum-number-of-operations-to-make-array-continuous](https://leetcode-cn.com/problems/minimum-number-of-operations-to-make-array-continuous) 
## 原题
给你一个整数数组 `nums` 。每一次操作中，你可以将 `nums` 中 **任意** 一个元素替换成 **任意** 整数。

如果 `nums` 满足以下条件，那么它是 **连续的** ：
-  `nums` 中所有元素都是 <b>互不相同</b> 的。
-  `nums` 中 **最大** 元素与 **最小** 元素的差等于 `nums.length - 1` 。
比方说， `nums = [4, 2, 5, 3]` 是 **连续的** ，但是 `nums = [1, 2, 3, 5, 6]` **不是连续的** 。

请你返回使 `nums` **连续** 的 **最少** 操作次数。

 

 **示例 1：** 

```
输入：nums = [4,2,5,3]
输出：0
解释：nums 已经是连续的了。

```
 **示例 2：** 

```
输入：nums = [1,2,3,5,6]
输出：1
解释：一个可能的解是将最后一个元素变为 4 。
结果数组为 [1,2,3,5,4] ，是连续数组。

```
 **示例 3：** 

```
输入：nums = [1,10,100,1000]
输出：3
解释：一个可能的解是：
- 将第二个元素变为 2 。
- 将第三个元素变为 3 。
- 将第四个元素变为 4 。
结果数组为 [1,2,3,4] ，是连续数组。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^9` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 2011.执行操作后的变量值
[https://leetcode-cn.com/problems/final-value-of-variable-after-performing-operations](https://leetcode-cn.com/problems/final-value-of-variable-after-performing-operations) 
## 原题
存在一种仅支持 4 种操作和 1 个变量 `X` 的编程语言：
-  `++X` 和 `X++` 使变量 `X` 的值 **加** `1` 
-  `--X` 和 `X--` 使变量 `X` 的值 **减** `1` 
最初， `X` 的值是 `0` 

给你一个字符串数组 `operations` ，这是由操作组成的一个列表，返回执行所有操作后， `X` 的 **最终值** 。

 

 **示例 1：** 

```

输入：operations = ["--X","X++","X++"]
输出：1
解释：操作按下述步骤执行：
最初，X = 0
--X：X 减 1 ，X =  0 - 1 = -1
X++：X 加 1 ，X = -1 + 1 =  0
X++：X 加 1 ，X =  0 + 1 =  1

```
 **示例 2：** 

```

输入：operations = ["++X","++X","X++"]
输出：3
解释：操作按下述步骤执行： 
最初，X = 0
++X：X 加 1 ，X = 0 + 1 = 1
++X：X 加 1 ，X = 1 + 1 = 2
X++：X 加 1 ，X = 2 + 1 = 3

```
 **示例 3：** 

```

输入：operations = ["X++","++X","--X","X--"]
输出：0
解释：操作按下述步骤执行：
最初，X = 0
X++：X 加 1 ，X = 0 + 1 = 1
++X：X 加 1 ，X = 1 + 1 = 2
--X：X 减 1 ，X = 2 - 1 = 1
X--：X 减 1 ，X = 1 - 1 = 0

```
 

 **提示：** 
-  `1 <= operations.length <= 100` 
-  `operations[i]` 将会是 `"++X"` 、 `"X++"` 、 `"--X"` 或 `"X--"` 
 
**标签**
`数组` `字符串` `模拟` 


## 
```python

```
>
# 2012.数组美丽值求和
[https://leetcode-cn.com/problems/sum-of-beauty-in-the-array](https://leetcode-cn.com/problems/sum-of-beauty-in-the-array) 
## 原题
给你一个下标从 **0** 开始的整数数组 `nums` 。对于每个下标 `i` （ `1 <= i <= nums.length - 2` ）， `nums[i]` 的 **美丽值** 等于：
-  `2` ，对于所有 `0 <= j < i` 且 `i < k <= nums.length - 1` ，满足 `nums[j] < nums[i] < nums[k]` 
-  `1` ，如果满足 `nums[i - 1] < nums[i] < nums[i + 1]` ，且不满足前面的条件
-  `0` ，如果上述条件全部不满足
返回符合 `1 <= i <= nums.length - 2` 的所有 `nums[i]` 的 **美丽值的总和** 。

 

 **示例 1：** 

```
输入：nums = [1,2,3]
输出：2
解释：对于每个符合范围 1 <= i <= 1 的下标 i :
- nums[1] 的美丽值等于 2

```
 **示例 2：** 

```
输入：nums = [2,4,6,4]
输出：1
解释：对于每个符合范围 1 <= i <= 2 的下标 i :
- nums[1] 的美丽值等于 1
- nums[2] 的美丽值等于 0

```
 **示例 3：** 

```
输入：nums = [3,2,1]
输出：0
解释：对于每个符合范围 1 <= i <= 1 的下标 i :
- nums[1] 的美丽值等于 0

```
 

 **提示：** 
-  `3 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^5` 
 
**标签**
`数组` 


## 
```python

```
>
# 2013.检测正方形
[https://leetcode-cn.com/problems/detect-squares](https://leetcode-cn.com/problems/detect-squares) 
## 原题
给你一个在 X-Y 平面上的点构成的数据流。设计一个满足下述要求的算法：
-  **添加** 一个在数据流中的新点到某个数据结构中 **。** 可以添加 **重复** 的点，并会视作不同的点进行处理。
- 给你一个查询点，请你从数据结构中选出三个点，使这三个点和查询点一同构成一个 **面积为正** 的 **轴对齐正方形** ， **统计** 满足该要求的方案数目 **。** 
 **轴对齐正方形** 是一个正方形，除四条边长度相同外，还满足每条边都与 x-轴 或 y-轴 平行或垂直。

实现 `DetectSquares` 类：
-  `DetectSquares()` 使用空数据结构初始化对象
-  `void add(int[] point)` 向数据结构添加一个新的点 `point = [x, y]` 
-  `int count(int[] point)` 统计按上述方式与点 `point = [x, y]` 共同构造 **轴对齐正方形** 的方案数。
 

 **示例：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/01/image.png" style="width: 869px; height: 504px;" />
```

输入：
["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]
[[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]
输出：
[null, null, null, null, 1, 0, null, 2]

解释：
DetectSquares detectSquares = new DetectSquares();
detectSquares.add([3, 10]);
detectSquares.add([11, 2]);
detectSquares.add([3, 2]);
detectSquares.count([11, 10]); // 返回 1 。你可以选择：
                               //   - 第一个，第二个，和第三个点
detectSquares.count([14, 8]);  // 返回 0 。查询点无法与数据结构中的这些点构成正方形。
detectSquares.add([11, 2]);    // 允许添加重复的点。
detectSquares.count([11, 10]); // 返回 2 。你可以选择：
                               //   - 第一个，第二个，和第三个点
                               //   - 第一个，第三个，和第四个点

```
 

 **提示：** 
-  `point.length == 2` 
-  `0 <= x, y <= 1000` 
- 调用 `add` 和 `count` 的 **总次数** 最多为 `5000` 
 
**标签**
`设计` `数组` `哈希表` `计数` 


## 
```python

```
>
# 2014.重复 K 次的最长子序列
[https://leetcode-cn.com/problems/longest-subsequence-repeated-k-times](https://leetcode-cn.com/problems/longest-subsequence-repeated-k-times) 
## 原题
给你一个长度为 `n` 的字符串 `s` ，和一个整数 `k` 。请你找出字符串 `s` 中 **重复** `k` 次的 **最长子序列** 。

 **子序列** 是由其他字符串删除某些（或不删除）字符派生而来的一个字符串。

如果 `seq * k` 是 `s` 的一个子序列，其中 `seq * k` 表示一个由 `seq` 串联 `k` 次构造的字符串，那么就称 `seq` **** 是字符串 `s` 中一个 **重复 `k` 次** 的子序列。
- 举个例子， `"bba"` 是字符串 `"bababcba"` 中的一个重复 `2` 次的子序列，因为字符串 `"bbabba"` 是由 `"bba"` 串联 `2` 次构造的，而 `"bbabba"` 是字符串 `" ***b*** a ***bab*** c ***ba*** "` 的一个子序列。
返回字符串 `s` 中 **重复 k 次的最长子序列** 。如果存在多个满足的子序列，则返回 **字典序最大** 的那个。如果不存在这样的子序列，返回一个 **空** 字符串。

 

 **示例 1：** 

<img alt="example 1" src="https://assets.leetcode.com/uploads/2021/08/30/longest-subsequence-repeat-k-times.png" style="width: 457px; height: 99px;" />

```

输入：s = "letsleetcode", k = 2
输出："let"
解释：存在两个最长子序列重复 2 次：let" 和 "ete" 。
"let" 是其中字典序最大的一个。

```
 **示例 2：** 

```

输入：s = "bb", k = 2
输出："b"
解释：重复 2 次的最长子序列是 "b" 。

```
 **示例 3：** 

```

输入：s = "ab", k = 2
输出：""
解释：不存在重复 2 次的最长子序列。返回空字符串。

```
 **示例 4：** 

```

输入：s = "bbabbabbbbabaababab", k = 3
输出："bbbb"
解释：在 "bbabbabbbbabaababab" 中重复 3 次的最长子序列是 "bbbb" 。

```
 

 **提示：** 
-  `n == s.length` 
-  `2 <= k <= 2000` 
-  `2 <= n < k * 8` 
-  `s` 由小写英文字母组成
 
**标签**
`贪心` `字符串` `回溯` `计数` `枚举` 


## 
```python

```
>
# 2016.增量元素之间的最大差值
[https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements](https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements) 
## 原题
给你一个下标从 **0** 开始的整数数组 `nums` ，该数组的大小为 `n` ，请你计算 `nums[j] - nums[i]` 能求得的 **最大差值** ，其中 `0 <= i < j < n` 且 `nums[i] < nums[j]` 。

返回 **最大差值** 。如果不存在满足要求的 `i` 和 `j` ，返回 `-1` 。

 

 **示例 1：** 

```
输入：nums = [7,1,5,4]
输出：4
解释：
最大差值出现在 i = 1 且 j = 2 时，nums[j] - nums[i] = 5 - 1 = 4 。
注意，尽管 i = 1 且 j = 0 时 ，nums[j] - nums[i] = 7 - 1 = 6 > 4 ，但 i > j 不满足题面要求，所以 6 不是有效的答案。

```
 **示例 2：** 

```
输入：nums = [9,4,3,2]
输出：-1
解释：
不存在同时满足 i < j 和 nums[i] < nums[j] 这两个条件的 i, j 组合。

```
 **示例 3：** 

```
输入：nums = [1,5,2,10]
输出：9
解释：
最大差值出现在 i = 0 且 j = 3 时，nums[j] - nums[i] = 10 - 1 = 9 。

```
 

 **提示：** 
-  `n == nums.length` 
-  `2 <= n <= 1000` 
-  `1 <= nums[i] <= 10^9` 
 
**标签**
`数组` 


## 
```python

```
>
# 2017.网格游戏
[https://leetcode-cn.com/problems/grid-game](https://leetcode-cn.com/problems/grid-game) 
## 原题
给你一个下标从 **0** 开始的二维数组 `grid` ，数组大小为 `2 x n` ，其中 `grid[r][c]` 表示矩阵中 `(r, c)` 位置上的点数。现在有两个机器人正在矩阵上参与一场游戏。

两个机器人初始位置都是 `(0, 0)` ，目标位置是 `(1, n-1)` 。每个机器人只会 **向右** ( `(r, c)` 到 `(r, c + 1)` ) 或 **向下** ( `(r, c)` 到 `(r + 1, c)` ) 。

游戏开始， **第一个** 机器人从 `(0, 0)` 移动到 `(1, n-1)` ，并收集路径上单元格的全部点数。对于路径上所有单元格 `(r, c)` ，途经后 `grid[r][c]` 会重置为 `0` 。然后， **第二个** 机器人从 `(0, 0)` 移动到 `(1, n-1)` ，同样收集路径上单元的全部点数。注意，它们的路径可能会存在相交的部分。

 **第一个** 机器人想要打击竞争对手，使 **第二个** 机器人收集到的点数 **最小化** 。与此相对， **第二个** 机器人想要 **最大化** 自己收集到的点数。两个机器人都发挥出自己的 **最佳水平** 的前提下，返回 **第二个** 机器人收集到的 **点数** *。* 

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/08/a1.png" style="width: 388px; height: 103px;" />

```

输入：grid = [[2,5,4],[1,5,1]]
输出：4
解释：第一个机器人的最佳路径如红色所示，第二个机器人的最佳路径如蓝色所示。
第一个机器人访问过的单元格将会重置为 0 。
第二个机器人将会收集到 0 + 0 + 4 + 0 = 4 个点。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/08/a2.png" style="width: 384px; height: 105px;" />
```

输入：grid = [[3,3,1],[8,5,2]]
输出：4
解释：第一个机器人的最佳路径如红色所示，第二个机器人的最佳路径如蓝色所示。 
第一个机器人访问过的单元格将会重置为 0 。
第二个机器人将会收集到 0 + 3 + 1 + 0 = 4 个点。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/09/08/a3.png" style="width: 493px; height: 103px;" />
```

输入：grid = [[1,3,1,15],[1,3,3,1]]
输出：7
解释：第一个机器人的最佳路径如红色所示，第二个机器人的最佳路径如蓝色所示。
第一个机器人访问过的单元格将会重置为 0 。
第二个机器人将会收集到 0 + 1 + 3 + 3 + 0 = 7 个点。

```
 

 **提示：** 
-  `grid.length == 2` 
-  `n == grid[r].length` 
-  `1 <= n <= 5 * 10^4` 
-  `1 <= grid[r][c] <= 10^5` 
 
**标签**
`数组` `矩阵` `前缀和` 


## 
```python

```
>
# 2018.判断单词是否能放入填字游戏内
[https://leetcode-cn.com/problems/check-if-word-can-be-placed-in-crossword](https://leetcode-cn.com/problems/check-if-word-can-be-placed-in-crossword) 
## 原题
给你一个 `m x n` 的矩阵 `board` ，它代表一个填字游戏 **当前** 的状态。填字游戏格子中包含小写英文字母（已填入的单词），表示 **空** 格的 `' '` 和表示 **障碍** 格子的 `'#'` 。

如果满足以下条件，那么我们可以 **水平** （从左到右 **或者** 从右到左）或 **竖直** （从上到下 **或者** 从下到上）填入一个单词：
- 该单词不占据任何 `'#'` 对应的格子。
- 每个字母对应的格子要么是 `' '` （空格）要么与 `board` 中已有字母 **匹配** 。
- 如果单词是 **水平** 放置的，那么该单词左边和右边 **相邻** 格子不能为 `' '` 或小写英文字母。
- 如果单词是 **竖直** 放置的，那么该单词上边和下边 **相邻** **** 格子不能为 `' '` 或小写英文字母。
给你一个字符串 `word` ，如果 `word` 可以被放入 `board` 中，请你返回 `true` ，否则请返回 `false` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/18/crossword-1.png" style="width: 170px; height: 150px;" />

```

输入：board = [["#", " ", "#"], [" ", " ", "#"], ["#", "c", " "]], word = "abc"
输出：true
解释：单词 "abc" 可以如上图放置（从上往下）。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/18/c2.png" style="width: 170px; height: 151px;" />

```

输入：board = [[" ", "#", "a"], [" ", "#", "c"], [" ", "#", "a"]], word = "ac"
输出：false
解释：无法放置单词，因为放置该单词后上方或者下方相邻格会有空格。
```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/18/crossword-2.png" style="width: 171px; height: 146px;" />

```

输入：board = [["#", " ", "#"], [" ", " ", "#"], ["#", " ", "c"]], word = "ca"
输出：true
解释：单词 "ca" 可以如上图放置（从右到左）。

```
 

 **提示：** 
-  `m == board.length` 
-  `n == board[i].length` 
-  `1 <= m * n <= 2 * 10^5` 
-  `board[i][j]` 可能为 `' '` ， `'#'` 或者一个小写英文字母。
-  `1 <= word.length <= max(m, n)` 
-  `word` 只包含小写英文字母。
 
**标签**
`数组` `枚举` `矩阵` 


## 
```python

```
>
# 2019.解出数学表达式的学生分数
[https://leetcode-cn.com/problems/the-score-of-students-solving-math-expression](https://leetcode-cn.com/problems/the-score-of-students-solving-math-expression) 
## 原题
给你一个字符串 `s` ，它 **只** 包含数字 `0-9` ，加法运算符 `'+'` 和乘法运算符 `'*'` ，这个字符串表示一个 **合法** 的只含有 **个位数** **数字** 的数学表达式（比方说 `3+5*2` ）。有 `n` 位小学生将计算这个数学表达式，并遵循如下 **运算顺序** ：
- 按照 **从左到右** 的顺序计算 **乘法** ，然后
- 按照 **从左到右** 的顺序计算 **加法** 。
给你一个长度为 `n` 的整数数组 `answers` ，表示每位学生提交的答案。你的任务是给 `answer` 数组按照如下 **规则** 打分：
- 如果一位学生的答案 **等于** 表达式的正确结果，这位学生将得到 `5` 分。
- 否则，如果答案由 **一处或多处错误的运算顺序** 计算得到，那么这位学生能得到 `2` 分。
- 否则，这位学生将得到 `0` 分。
请你返回所有学生的分数和。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/17/student_solving_math.png" style="width: 678px; height: 109px;">

```
输入：s = "7+3*1*2", answers = [20,13,42]
输出：7
解释：如上图所示，正确答案为 13 ，因此有一位学生得分为 5 分：[20,13,42] 。
一位学生可能通过错误的运算顺序得到结果 20 ：7+3=10，10*1=10，10*2=20 。所以这位学生得分为 2 分：[20,13,42] 。
所有学生得分分别为：[2,5,0] 。所有得分之和为 2+5+0=7 。

```
 **示例 2：** 

```
输入：s = "3+5*2", answers = [13,0,10,13,13,16,16]
输出：19
解释：表达式的正确结果为 13 ，所以有 3 位学生得到 5 分：[13,0,10,13,13,16,16] 。
学生可能通过错误的运算顺序得到结果 16 ：3+5=8，8*2=16 。所以两位学生得到 2 分：[13,0,10,13,13,16,16] 。
所有学生得分分别为：[5,0,0,5,5,2,2] 。所有得分之和为 5+0+0+5+5+2+2=19 。

```
 **示例 3：** 

```
输入：s = "6+0*1", answers = [12,9,6,4,8,6]
输出：10
解释：表达式的正确结果为 6 。
如果一位学生通过错误的运算顺序计算该表达式，结果仍为 6 。
根据打分规则，运算顺序错误的学生也将得到 5 分（因为他们仍然得到了正确的结果），而不是 2 分。
所有学生得分分别为：[0,0,5,0,0,5] 。所有得分之和为 10 分。

```
 

 **提示：** 
-  `3 <= s.length <= 31` 
-  `s` 表示一个只包含 `0-9` ， `'+'` 和 `'*'` 的合法表达式。
- 表达式中所有整数运算数字都在闭区间 `[0, 9]` 以内。
-  `1 <=` 数学表达式中所有运算符数目（ `'+'` 和 `'*'` ） `<= 15` 
- 测试数据保证正确表达式结果在范围 `[0, 1000]` 以内。
-  `n == answers.length` 
-  `1 <= n <= 10^4` 
-  `0 <= answers[i] <= 1000` 
 
**标签**
`栈` `记忆化搜索` `数组` `数学` `字符串` `动态规划` 


## 
```python

```
>
# 2021.街上最亮的位置
[https://leetcode-cn.com/problems/brightest-position-on-street](https://leetcode-cn.com/problems/brightest-position-on-street) 
## 原题

 
**标签**
`数组` `有序集合` `前缀和` 


## 
```python

```
>
# 2022.将一维数组转变成二维数组
[https://leetcode-cn.com/problems/convert-1d-array-into-2d-array](https://leetcode-cn.com/problems/convert-1d-array-into-2d-array) 
## 原题
给你一个下标从 **0** 开始的一维整数数组 `original` 和两个整数 `m` 和 `n` 。你需要使用 `original` 中 **所有** 元素创建一个 `m` 行 `n` 列的二维数组。

 `original` 中下标从 `0` 到 `n - 1` （都 **包含** ）的元素构成二维数组的第一行，下标从 `n` 到 `2 * n - 1` （都 **包含** ）的元素构成二维数组的第二行，依此类推。

请你根据上述过程返回一个 `m x n` 的二维数组。如果无法构成这样的二维数组，请你返回一个空的二维数组。

 

 **示例 1：** 
<img src="https://assets.leetcode.com/uploads/2021/08/26/image-20210826114243-1.png" style="width: 500px; height: 174px;">
```
输入：original = [1,2,3,4], m = 2, n = 2
输出：[[1,2],[3,4]]
解释：
构造出的二维数组应该包含 2 行 2 列。
original 中第一个 n=2 的部分为 [1,2] ，构成二维数组的第一行。
original 中第二个 n=2 的部分为 [3,4] ，构成二维数组的第二行。

```
 **示例 2：** 

```
输入：original = [1,2,3], m = 1, n = 3
输出：[[1,2,3]]
解释：
构造出的二维数组应该包含 1 行 3 列。
将 original 中所有三个元素放入第一行中，构成要求的二维数组。

```
 **示例 3：** 

```
输入：original = [1,2], m = 1, n = 1
输出：[]
解释：
original 中有 2 个元素。
无法将 2 个元素放入到一个 1x1 的二维数组中，所以返回一个空的二维数组。

```
 **示例 4：** 

```
输入：original = [3], m = 1, n = 2
输出：[]
解释：
original 中只有 1 个元素。
无法将 1 个元素放满一个 1x2 的二维数组，所以返回一个空的二维数组。

```
 

 **提示：** 
-  `1 <= original.length <= 5 * 10^4` 
-  `1 <= original[i] <= 10^5` 
-  `1 <= m, n <= 4 * 10^4` 
 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 2023.连接后等于目标字符串的字符串对
[https://leetcode-cn.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target](https://leetcode-cn.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target) 
## 原题
给你一个 **数字** 字符串数组 `nums` 和一个 **数字** 字符串 `target` ，请你返回 `nums[i] + nums[j]` （两个字符串连接）结果等于 `target` 的下标 `(i, j)` （需满足 `i != j` ）的数目。

 

 **示例 1：** 

```
输入：nums = ["777","7","77","77"], target = "7777"
输出：4
解释：符合要求的下标对包括：
- (0, 1)："777" + "7"
- (1, 0)："7" + "777"
- (2, 3)："77" + "77"
- (3, 2)："77" + "77"

```
 **示例 2：** 

```
输入：nums = ["123","4","12","34"], target = "1234"
输出：2
解释：符合要求的下标对包括
- (0, 1)："123" + "4"
- (2, 3)："12" + "34"

```
 **示例 3：** 

```
输入：nums = ["1","1","1"], target = "11"
输出：6
解释：符合要求的下标对包括
- (0, 1)："1" + "1"
- (1, 0)："1" + "1"
- (0, 2)："1" + "1"
- (2, 0)："1" + "1"
- (1, 2)："1" + "1"
- (2, 1)："1" + "1"

```
 

 **提示：** 
-  `2 <= nums.length <= 100` 
-  `1 <= nums[i].length <= 100` 
-  `2 <= target.length <= 100` 
-  `nums[i]` 和 `target` 只包含数字。
-  `nums[i]` 和 `target` 不含有任何前导 0 。
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 2024.考试的最大困扰度
[https://leetcode-cn.com/problems/maximize-the-confusion-of-an-exam](https://leetcode-cn.com/problems/maximize-the-confusion-of-an-exam) 
## 原题
一位老师正在出一场由 `n` 道判断题构成的考试，每道题的答案为 true （用 `<span style="">'T'</span>` 表示）或者 false （用 `'F'` 表示）。老师想增加学生对自己做出答案的不确定性，方法是 **最大化** 有 **连续相同** 结果的题数。（也就是连续出现 true 或者连续出现 false）。

给你一个字符串 `answerKey` ，其中 `answerKey[i]` 是第 `i` 个问题的正确结果。除此以外，还给你一个整数 `k` ，表示你能进行以下操作的最多次数：
- 每次操作中，将问题的正确答案改为 `'T'` 或者 `'F'` （也就是将 `answerKey[i]` 改为 `'T'` 或者 `'F'` ）。
请你返回在不超过 `k` 次操作的情况下， **最大** 连续 `'T'` 或者 `'F'` 的数目。

 

 **示例 1：** 

```

输入：answerKey = "TTFF", k = 2
输出：4
解释：我们可以将两个 'F' 都变为 'T' ，得到 answerKey = "TTTT" 。
总共有四个连续的 'T' 。

```
 **示例 2：** 

```

输入：answerKey = "TFFT", k = 1
输出：3
解释：我们可以将最前面的 'T' 换成 'F' ，得到 answerKey = "FFFT" 。
或者，我们可以将第二个 'T' 换成 'F' ，得到 answerKey = "TFFF" 。
两种情况下，都有三个连续的 'F' 。

```
 **示例 3：** 

```

输入：answerKey = "TTFTTFTT", k = 1
输出：5
解释：我们可以将第一个 'F' 换成 'T' ，得到 answerKey = "TTTTTFTT" 。
或者我们可以将第二个 'F' 换成 'T' ，得到 answerKey = "TTFTTTTT" 。
两种情况下，都有五个连续的 'T' 。

```
 

 **提示：** 
-  `n == answerKey.length` 
-  `1 <= n <= 5 * 10^4` 
-  `answerKey[i]` 要么是 `'T'` ，要么是 `'F'` 
-  `1 <= k <= n` 
 
**标签**
`字符串` `二分查找` `前缀和` `滑动窗口` 


## 
```python

```
>
# 2025.分割数组的最多方案数
[https://leetcode-cn.com/problems/maximum-number-of-ways-to-partition-an-array](https://leetcode-cn.com/problems/maximum-number-of-ways-to-partition-an-array) 
## 原题
给你一个下标从 **0** 开始且长度为 `n` 的整数数组 `nums` 。 **分割** 数组 `nums` 的方案数定义为符合以下两个条件的 `pivot` 数目：
-  `1 <= pivot < n` 
-  `nums[0] + nums[1] + ... + nums[pivot - 1] == nums[pivot] + nums[pivot + 1] + ... + nums[n - 1]` 
同时给你一个整数 `k` 。你可以将 `nums` 中 **一个** 元素变为 `k` 或 **不改变** 数组。

请你返回在 **至多** 改变一个元素的前提下， **最多** 有多少种方法 **分割** `nums` 使得上述两个条件都满足。

 

 **示例 1：** 

```
输入：nums = [2,-1,2], k = 3
输出：1
解释：一个最优的方案是将 nums[0] 改为 k 。数组变为 [3,-1,2] 。
有一种方法分割数组：
- pivot = 2 ，我们有分割 [3,-1 | 2]：3 + -1 == 2 。

```
 **示例 2：** 

```
输入：nums = [0,0,0], k = 1
输出：2
解释：一个最优的方案是不改动数组。
有两种方法分割数组：
- pivot = 1 ，我们有分割 [0 | 0,0]：0 == 0 + 0 。
- pivot = 2 ，我们有分割 [0,0 | 0]: 0 + 0 == 0 。

```
 **示例 3：** 

```
输入：nums = [22,4,-25,-20,-15,15,-16,7,19,-10,0,-13,-14], k = -33
输出：4
解释：一个最优的方案是将 nums[2] 改为 k 。数组变为 [22,4,-33,-20,-15,15,-16,7,19,-10,0,-13,-14] 。
有四种方法分割数组。

```
 

 **提示：** 
-  `n == nums.length` 
-  `2 <= n <= 10^5` 
-  `-10^5 <= k, nums[i] <= 10^5` 
 
**标签**
`数组` `哈希表` `计数` `枚举` `前缀和` 


## 
```python

```
>
# 2026.低质量的问题
[https://leetcode-cn.com/problems/low-quality-problems](https://leetcode-cn.com/problems/low-quality-problems) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 2027.转换字符串的最少操作次数
[https://leetcode-cn.com/problems/minimum-moves-to-convert-string](https://leetcode-cn.com/problems/minimum-moves-to-convert-string) 
## 原题
给你一个字符串 `s` ，由 `n` 个字符组成，每个字符不是 `'X'` 就是 `'O'` 。

一次 **操作** 定义为从 `s` 中选出 **三个连续字符** 并将选中的每个字符都转换为 `'O'` 。注意，如果字符已经是 `'O'` ，只需要保持 **不变** 。

返回将 `s` 中所有字符均转换为 `'O'` 需要执行的 **最少** 操作次数。

 

 **示例 1：** 

```

输入：s = "XXX"
输出：1
解释：XXX -> OOO
一次操作，选中全部 3 个字符，并将它们转换为 'O' 。

```
 **示例 2：** 

```

输入：s = "XXOX"
输出：2
解释：XXOX -> OOOX -> OOOO
第一次操作，选择前 3 个字符，并将这些字符转换为 'O' 。
然后，选中后 3 个字符，并执行转换。最终得到的字符串全由字符 'O' 组成。
```
 **示例 3：** 

```

输入：s = "OOOO"
输出：0
解释：s 中不存在需要转换的 'X' 。

```
 

 **提示：** 
-  `3 <= s.length <= 1000` 
-  `s[i]` 为 `'X'` 或 `'O'` 
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 2028.找出缺失的观测数据
[https://leetcode-cn.com/problems/find-missing-observations](https://leetcode-cn.com/problems/find-missing-observations) 
## 原题
现有一份 `n + m` 次投掷单个 **六面** 骰子的观测数据，骰子的每个面从 `1` 到 `6` 编号。观测数据中缺失了 `n` 份，你手上只拿到剩余 `m` 次投掷的数据。幸好你有之前计算过的这 `n + m` 次投掷数据的 **平均值** 。

给你一个长度为 `m` 的整数数组 `rolls` ，其中 `rolls[i]` 是第 `i` 次观测的值。同时给你两个整数 `mean` 和 `n` 。

返回一个长度为 `n` 的数组，包含所有缺失的观测数据，且满足这 `n + m` 次投掷的 **平均值** 是 `mean` 。如果存在多组符合要求的答案，只需要返回其中任意一组即可。如果不存在答案，返回一个空数组。

 `k` 个数字的 **平均值** 为这些数字求和后再除以 `k` 。

注意 `mean` 是一个整数，所以 `n + m` 次投掷的总和需要被 `n + m` 整除。

 

 **示例 1：** 

```

输入：rolls = [3,2,4,3], mean = 4, n = 2
输出：[6,6]
解释：所有 n + m 次投掷的平均值是 (3 + 2 + 4 + 3 + 6 + 6) / 6 = 4 。

```
 **示例 2：** 

```

输入：rolls = [1,5,6], mean = 3, n = 4
输出：[2,3,2,2]
解释：所有 n + m 次投掷的平均值是 (1 + 5 + 6 + 2 + 3 + 2 + 2) / 7 = 3 。

```
 **示例 3：** 

```

输入：rolls = [1,2,3,4], mean = 6, n = 4
输出：[]
解释：无论丢失的 4 次数据是什么，平均值都不可能是 6 。

```
 **示例 4：** 

```

输入：rolls = [1], mean = 3, n = 1
输出：[5]
解释：所有 n + m 次投掷的平均值是 (1 + 5) / 2 = 3 。

```
 

 **提示：** 
-  `m == rolls.length` 
-  `1 <= n, m <= 10^5` 
-  `1 <= rolls[i], mean <= 6` 
 
**标签**
`数组` `数学` `模拟` 


## 
```python

```
>
# 2029.石子游戏 IX
[https://leetcode-cn.com/problems/stone-game-ix](https://leetcode-cn.com/problems/stone-game-ix) 
## 原题
Alice 和 Bob 再次设计了一款新的石子游戏。现有一行 n 个石子，每个石子都有一个关联的数字表示它的价值。给你一个整数数组 `stones` ，其中 `stones[i]` 是第 `i` 个石子的价值。

Alice 和 Bob 轮流进行自己的回合， **Alice** 先手。每一回合，玩家需要从 `stones` 中移除任一石子。
- 如果玩家移除石子后，导致 **所有已移除石子** 的价值 **总和** 可以被 3 整除，那么该玩家就 **输掉游戏** 。
- 如果不满足上一条，且移除后没有任何剩余的石子，那么 Bob 将会直接获胜（即便是在 Alice 的回合）。
假设两位玩家均采用 **最佳** 决策。如果 Alice 获胜，返回 `true` ；如果 Bob 获胜，返回 `false` 。

 

 **示例 1：** 

```

输入：stones = [2,1]
输出：true
解释：游戏进行如下：
- 回合 1：Alice 可以移除任意一个石子。
- 回合 2：Bob 移除剩下的石子。 
已移除的石子的值总和为 1 + 2 = 3 且可以被 3 整除。因此，Bob 输，Alice 获胜。

```
 **示例 2：** 

```

输入：stones = [2]
输出：false
解释：Alice 会移除唯一一个石子，已移除石子的值总和为 2 。 
由于所有石子都已移除，且值总和无法被 3 整除，Bob 获胜。

```
 **示例 3：** 

```

输入：stones = [5,1,2,4,3]
输出：false
解释：Bob 总会获胜。其中一种可能的游戏进行方式如下：
- 回合 1：Alice 可以移除值为 1 的第 2 个石子。已移除石子值总和为 1 。
- 回合 2：Bob 可以移除值为 3 的第 5 个石子。已移除石子值总和为 = 1 + 3 = 4 。
- 回合 3：Alices 可以移除值为 4 的第 4 个石子。已移除石子值总和为 = 1 + 3 + 4 = 8 。
- 回合 4：Bob 可以移除值为 2 的第 3 个石子。已移除石子值总和为 = 1 + 3 + 4 + 2 = 10.
- 回合 5：Alice 可以移除值为 5 的第 1 个石子。已移除石子值总和为 = 1 + 3 + 4 + 2 + 5 = 15.
Alice 输掉游戏，因为已移除石子值总和（15）可以被 3 整除，Bob 获胜。

```
 

 **提示：** 
-  `1 <= stones.length <= 10^5` 
-  `1 <= stones[i] <= 10^4` 
 
**标签**
`贪心` `数组` `数学` `计数` `博弈` 


## 
```python

```
>
# 2030.含特定字母的最小子序列
[https://leetcode-cn.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter](https://leetcode-cn.com/problems/smallest-k-length-subsequence-with-occurrences-of-a-letter) 
## 原题
给你一个字符串 `s` ，一个整数 `k` ，一个字母 `letter` 以及另一个整数 `repetition` 。

返回 `s` 中长度为 `k` 且 **字典序最小** 的子序列，该子序列同时应满足字母 `letter` 出现 **至少** `repetition` 次。生成的测试用例满足 `letter` 在 `s` 中出现 **至少** `repetition` 次。

 **子序列** 是由原字符串删除一些（或不删除）字符且不改变剩余字符顺序得到的剩余字符串。

字符串 `a` 字典序比字符串 `b` 小的定义为：在 `a` 和 `b` 出现不同字符的第一个位置上，字符串 `a` 的字符在字母表中的顺序早于字符串 `b` 的字符。

 

 **示例 1：** 

```

输入：s = "leet", k = 3, letter = "e", repetition = 1
输出："eet"
解释：存在 4 个长度为 3 ，且满足字母 'e' 出现至少 1 次的子序列：
- "lee"（"leet"）
- "let"（"leet"）
- "let"（"leet"）
- "eet"（"leet"）
其中字典序最小的子序列是 "eet" 。

```
 **示例 2：** 

<img alt="example-2" src="https://assets.leetcode.com/uploads/2021/09/13/smallest-k-length-subsequence.png" style="width: 339px; height: 67px;" />

```

输入：s = "leetcode", k = 4, letter = "e", repetition = 2
输出："ecde"
解释："ecde" 是长度为 4 且满足字母 "e" 出现至少 2 次的字典序最小的子序列。

```
 **示例 3：** 

```

输入：s = "bb", k = 2, letter = "b", repetition = 2
输出："bb"
解释："bb" 是唯一一个长度为 2 且满足字母 "b" 出现至少 2 次的子序列。

```
 

 **提示：** 
-  `1 <= repetition <= k <= s.length <= 5 * 10^4` 
-  `s` 由小写英文字母组成
-  `letter` 是一个小写英文字母，在 `s` 中至少出现 `repetition` 次
 
**标签**
`栈` `贪心` `字符串` `单调栈` 


## 
```python

```
>
# 2031.1 比 0 多的子数组个数
[https://leetcode-cn.com/problems/count-subarrays-with-more-ones-than-zeros](https://leetcode-cn.com/problems/count-subarrays-with-more-ones-than-zeros) 
## 原题

 
**标签**
`树状数组` `线段树` `数组` `二分查找` `分治` `有序集合` `归并排序` 


## 
```python

```
>
# 2032.至少在两个数组中出现的值
[https://leetcode-cn.com/problems/two-out-of-three](https://leetcode-cn.com/problems/two-out-of-three) 
## 原题
给你三个整数数组 `nums1` 、 `nums2` 和 `nums3` ，请你构造并返回一个 **与这三个数组都不同的** 数组，且由 **至少** 在 **两个** 数组中出现的所有值组成 *。* 数组中的元素可以按 **任意** 顺序排列。
 

 **示例 1：** 

```

输入：nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
输出：[3,2]
解释：至少在两个数组中出现的所有值为：
- 3 ，在全部三个数组中都出现过。
- 2 ，在数组 nums1 和 nums2 中出现过。

```
 **示例 2：** 

```

输入：nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
输出：[2,3,1]
解释：至少在两个数组中出现的所有值为：
- 2 ，在数组 nums2 和 nums3 中出现过。
- 3 ，在数组 nums1 和 nums2 中出现过。
- 1 ，在数组 nums1 和 nums3 中出现过。

```
 **示例 3：** 

```

输入：nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
输出：[]
解释：不存在至少在两个数组中出现的值。

```
 

 **提示：** 
-  `1 <= nums1.length, nums2.length, nums3.length <= 100` 
-  `1 <= nums1[i], nums2[j], nums3[k] <= 100` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 2033.获取单值网格的最小操作数
[https://leetcode-cn.com/problems/minimum-operations-to-make-a-uni-value-grid](https://leetcode-cn.com/problems/minimum-operations-to-make-a-uni-value-grid) 
## 原题
给你一个大小为 `m x n` 的二维整数网格 `grid` 和一个整数 `x` 。每一次操作，你可以对 `grid` 中的任一元素 **加** `x` 或 **减** `x` 。

 **单值网格** 是全部元素都相等的网格。

返回使网格化为单值网格所需的 **最小** 操作数。如果不能，返回 `-1` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/gridtxt.png" style="width: 164px; height: 165px;" />

```

输入：grid = [[2,4],[6,8]], x = 2
输出：4
解释：可以执行下述操作使所有元素都等于 4 ： 
- 2 加 x 一次。
- 6 减 x 一次。
- 8 减 x 两次。
共计 4 次操作。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/gridtxt-1.png" style="width: 164px; height: 165px;" />

```

输入：grid = [[1,5],[2,3]], x = 1
输出：5
解释：可以使所有元素都等于 3 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/gridtxt-2.png" style="width: 164px; height: 165px;" />

```

输入：grid = [[1,2],[3,4]], x = 2
输出：-1
解释：无法使所有元素相等。

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 10^5` 
-  `1 <= m * n <= 10^5` 
-  `1 <= x, grid[i][j] <= 10^4` 
 
**标签**
`数组` `数学` `矩阵` `排序` 


## 
```python

```
>
# 2034.股票价格波动
[https://leetcode-cn.com/problems/stock-price-fluctuation](https://leetcode-cn.com/problems/stock-price-fluctuation) 
## 原题
给你一支股票价格的数据流。数据流中每一条记录包含一个 **时间戳** 和该时间点股票对应的 **价格** 。

不巧的是，由于股票市场内在的波动性，股票价格记录可能不是按时间顺序到来的。某些情况下，有的记录可能是错的。如果两个有相同时间戳的记录出现在数据流中，前一条记录视为错误记录，后出现的记录 <b>更正</b> 前一条错误的记录。

请你设计一个算法，实现：
-  **更新** 股票在某一时间戳的股票价格，如果有之前同一时间戳的价格，这一操作将 **更正** 之前的错误价格。
- 找到当前记录里 <b>最新股票价格</b> 。 **最新股票价格** 定义为时间戳最晚的股票价格。
- 找到当前记录里股票的 **最高价格** 。
- 找到当前记录里股票的 **最低价格** 。
请你实现 `StockPrice` 类：
-  `StockPrice()` 初始化对象，当前无股票价格记录。
-  `void update(int timestamp, int price)` 在时间点 `timestamp` 更新股票价格为 `price` 。
-  `int current()` 返回股票 **最新价格** 。
-  `int maximum()` 返回股票 **最高价格** 。
-  `int minimum()` 返回股票 **最低价格** 。
 

 **示例 1：** 

```
输入：
["StockPrice", "update", "update", "current", "maximum", "update", "maximum", "update", "minimum"]
[[], [1, 10], [2, 5], [], [], [1, 3], [], [4, 2], []]
输出：
[null, null, null, 5, 10, null, 5, null, 2]

解释：
StockPrice stockPrice = new StockPrice();
stockPrice.update(1, 10); // 时间戳为 [1] ，对应的股票价格为 [10] 。
stockPrice.update(2, 5);  // 时间戳为 [1,2] ，对应的股票价格为 [10,5] 。
stockPrice.current();     // 返回 5 ，最新时间戳为 2 ，对应价格为 5 。
stockPrice.maximum();     // 返回 10 ，最高价格的时间戳为 1 ，价格为 10 。
stockPrice.update(1, 3);  // 之前时间戳为 1 的价格错误，价格更新为 3 。
                          // 时间戳为 [1,2] ，对应股票价格为 [3,5] 。
stockPrice.maximum();     // 返回 5 ，更正后最高价格为 5 。
stockPrice.update(4, 2);  // 时间戳为 [1,2,4] ，对应价格为 [3,5,2] 。
stockPrice.minimum();     // 返回 2 ，最低价格时间戳为 4 ，价格为 2 。

```
 

 **提示：** 
-  `1 <= timestamp, price <= 10^9` 
-  `update` ， `current` ， `maximum` 和 `minimum` **总** 调用次数不超过 `10^5` 。
-  `current` ， `maximum` 和 `minimum` 被调用时， `update` 操作 **至少** 已经被调用过 **一次** 。
 
**标签**
`设计` `哈希表` `数据流` `有序集合` `堆（优先队列）` 


## 
```python

```
>
# 2035.将数组分成两个数组并最小化数组和的差
[https://leetcode-cn.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference](https://leetcode-cn.com/problems/partition-array-into-two-arrays-to-minimize-sum-difference) 
## 原题
给你一个长度为 `2 * n` 的整数数组。你需要将 `nums` 分成 **两个** 长度为 `n` 的数组，分别求出两个数组的和，并 **最小化** 两个数组和之 <b>差的绝对值</b> 。 `nums` 中每个元素都需要放入两个数组之一。

请你返回 **最小** 的数组和之差。

 

 **示例 1：** 

<img alt="example-1" src="https://assets.leetcode.com/uploads/2021/10/02/ex1.png" style="width: 240px; height: 106px;">

```
输入：nums = [3,9,7,3]
输出：2
解释：最优分组方案是分成 [3,9] 和 [7,3] 。
数组和之差的绝对值为 abs((3 + 9) - (7 + 3)) = 2 。

```
 **示例 2：** 

```
输入：nums = [-36,36]
输出：72
解释：最优分组方案是分成 [-36] 和 [36] 。
数组和之差的绝对值为 abs((-36) - (36)) = 72 。

```
 **示例 3：** 

<img alt="example-3" src="https://assets.leetcode.com/uploads/2021/10/02/ex3.png" style="width: 316px; height: 106px;">

```
输入：nums = [2,-1,0,4,-2,-9]
输出：0
解释：最优分组方案是分成 [2,4,-9] 和 [-1,0,-2] 。
数组和之差的绝对值为 abs((2 + 4 + -9) - (-1 + 0 + -2)) = 0 。

```
 

 **提示：** 
-  `1 <= n <= 15` 
-  `nums.length == 2 * n` 
-  `-10^7 <= nums[i] <= 10^7` 
 
**标签**
`位运算` `数组` `双指针` `二分查找` `动态规划` `状态压缩` `有序集合` 


## 
```python

```
>
# 2036.最大交替子数组和
[https://leetcode-cn.com/problems/maximum-alternating-subarray-sum](https://leetcode-cn.com/problems/maximum-alternating-subarray-sum) 
## 原题

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 2037.使每位学生都有座位的最少移动次数
[https://leetcode-cn.com/problems/minimum-number-of-moves-to-seat-everyone](https://leetcode-cn.com/problems/minimum-number-of-moves-to-seat-everyone) 
## 原题
一个房间里有 `n` 个座位和 `n` 名学生，房间用一个数轴表示。给你一个长度为 `n` 的数组 `seats` ，其中 `seats[i]` 是第 `i` 个座位的位置。同时给你一个长度为 `n` 的数组 `students` ，其中 `students[j]` 是第 `j` 位学生的位置。

你可以执行以下操作任意次：
- 增加或者减少第 `i` 位学生的位置，每次变化量为 `1` （也就是将第 `i` 位学生从位置 `x` 移动到 `x + 1` 或者 `x - 1` ）
请你返回使所有学生都有座位坐的 **最少移动次数** ，并确保没有两位学生的座位相同。

请注意，初始时有可能有多个座位或者多位学生在 **同一** 位置。

 

 **示例 1：** 

```
输入：seats = [3,1,5], students = [2,7,4]
输出：4
解释：学生移动方式如下：
- 第一位学生从位置 2 移动到位置 1 ，移动 1 次。
- 第二位学生从位置 7 移动到位置 5 ，移动 2 次。
- 第三位学生从位置 4 移动到位置 3 ，移动 1 次。
总共 1 + 2 + 1 = 4 次移动。

```
 **示例 2：** 

```
输入：seats = [4,1,5,9], students = [1,3,2,6]
输出：7
解释：学生移动方式如下：
- 第一位学生不移动。
- 第二位学生从位置 3 移动到位置 4 ，移动 1 次。
- 第三位学生从位置 2 移动到位置 5 ，移动 3 次。
- 第四位学生从位置 6 移动到位置 9 ，移动 3 次。
总共 0 + 1 + 3 + 3 = 7 次移动。

```
 **示例 3：** 

```
输入：seats = [2,2,6,6], students = [1,3,2,6]
输出：4
解释：学生移动方式如下：
- 第一位学生从位置 1 移动到位置 2 ，移动 1 次。
- 第二位学生从位置 3 移动到位置 6 ，移动 3 次。
- 第三位学生不移动。
- 第四位学生不移动。
总共 1 + 3 + 0 + 0 = 4 次移动。

```
 

 **提示：** 
-  `n == seats.length == students.length` 
-  `1 <= n <= 100` 
-  `1 <= seats[i], students[j] <= 100` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 2038.如果相邻两个颜色均相同则删除当前颜色
[https://leetcode-cn.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color](https://leetcode-cn.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color) 
## 原题
总共有 `n` 个颜色片段排成一列，每个颜色片段要么是 `'A'` 要么是 `'B'` 。给你一个长度为 `n` 的字符串 `colors` ，其中 `colors[i]` 表示第 `i` 个颜色片段的颜色。

Alice 和 Bob 在玩一个游戏，他们 **轮流** 从这个字符串中删除颜色。Alice **先手** 。
- 如果一个颜色片段为 `'A'` 且 **相邻两个颜色** 都是颜色 `'A'` ，那么 Alice 可以删除该颜色片段。Alice **不可以** 删除任何颜色 `'B'` 片段。
- 如果一个颜色片段为 `'B'` 且 **相邻两个颜色** 都是颜色 `'B'` ，那么 Bob 可以删除该颜色片段。Bob **不可以** 删除任何颜色 `'A'` 片段。
- Alice 和 Bob **不能** 从字符串两端删除颜色片段。
- 如果其中一人无法继续操作，则该玩家 <b>输</b> 掉游戏且另一玩家 **获胜** 。
假设 Alice 和 Bob 都采用最优策略，如果 Alice 获胜，请返回 `true` ，否则 Bob 获胜，返回 `false` 。

 

 **示例 1：** 

```
输入：colors = "AAABABB"
输出：true
解释：
AAABABB -> AABABB
Alice 先操作。
她删除从左数第二个 'A' ，这也是唯一一个相邻颜色片段都是 'A' 的 'A' 。

现在轮到 Bob 操作。
Bob 无法执行任何操作，因为没有相邻位置都是 'B' 的颜色片段 'B' 。
因此，Alice 获胜，返回 true 。

```
 **示例 2：** 

```
输入：colors = "AA"
输出：false
解释：
Alice 先操作。
只有 2 个 'A' 且它们都在字符串的两端，所以她无法执行任何操作。
因此，Bob 获胜，返回 false 。

```
 **示例 3：** 

```
输入：colors = "ABBBBBBBAAA"
输出：false
解释：
ABBBBBBBAAA -> ABBBBBBBAA
Alice 先操作。
她唯一的选择是删除从右数起第二个 'A' 。

ABBBBBBBAA -> ABBBBBBAA
接下来轮到 Bob 操作。
他有许多选择，他可以选择任何一个 'B' 删除。

然后轮到 Alice 操作，她无法删除任何片段。
所以 Bob 获胜，返回 false 。

```
 

 **提示：** 
-  `1 <= colors.length <= 10^5` 
-  `colors` 只包含字母 `'A'` 和 `'B'` 
 
**标签**
`贪心` `数学` `字符串` `博弈` 


## 
```python

```
>
# 2039.网络空闲的时刻
[https://leetcode-cn.com/problems/the-time-when-the-network-becomes-idle](https://leetcode-cn.com/problems/the-time-when-the-network-becomes-idle) 
## 原题
给你一个有 `n` 个服务器的计算机网络，服务器编号为 `0` 到 `n - 1` 。同时给你一个二维整数数组 `edges` ，其中 `edges[i] = [u<sub>i</sub>, v<sub>i</sub>]` 表示服务器 `u<sub>i</sub>` 和 `v<sub>i</sub>` <sub> </sub>之间有一条信息线路，在 **一秒** 内它们之间可以传输 **任意** 数目的信息。再给你一个长度为 `n` 且下标从 **0** 开始的整数数组 `patience` 。

题目保证所有服务器都是 <b>相通</b> 的，也就是说一个信息从任意服务器出发，都可以通过这些信息线路直接或间接地到达任何其他服务器。

编号为 `0` 的服务器是 **主** 服务器，其他服务器为 **数据** 服务器。每个数据服务器都要向主服务器发送信息，并等待回复。信息在服务器之间按 **最优** 线路传输，也就是说每个信息都会以 **最少时间** 到达主服务器。主服务器会处理 **所有** 新到达的信息并 **立即** 按照每条信息来时的路线 **反方向** 发送回复信息。

在 `0` 秒的开始，所有数据服务器都会发送各自需要处理的信息。从第 `1` 秒开始， **每** 一秒最 **开始** 时，每个数据服务器都会检查它是否收到了主服务器的回复信息（包括新发出信息的回复信息）：
- 如果还没收到任何回复信息，那么该服务器会周期性 **重发** 信息。数据服务器 `i` 每 `patience[i]` 秒都会重发一条信息，也就是说，数据服务器 `i` 在上一次发送信息给主服务器后的 `patience[i]` 秒 **后** 会重发一条信息给主服务器。
- 否则，该数据服务器 **不会重发** 信息。
当没有任何信息在线路上传输或者到达某服务器时，该计算机网络变为 **空闲** 状态。

请返回计算机网络变为 **空闲** 状态的 **最早秒数** 。

 

 **示例 1：** 

<img alt="example 1" src="https://assets.leetcode.com/uploads/2021/09/22/quiet-place-example1.png" style="width: 750px; height: 384px;">

```
输入：edges = [[0,1],[1,2]], patience = [0,2,1]
输出：8
解释：
0 秒最开始时，
- 数据服务器 1 给主服务器发出信息（用 1A 表示）。
- 数据服务器 2 给主服务器发出信息（用 2A 表示）。

1 秒时，
- 信息 1A 到达主服务器，主服务器立刻处理信息 1A 并发出 1A 的回复信息。
- 数据服务器 1 还没收到任何回复。距离上次发出信息过去了 1 秒（1 < patience[1] = 2），所以不会重发信息。
- 数据服务器 2 还没收到任何回复。距离上次发出信息过去了 1 秒（1 == patience[2] = 1），所以它重发一条信息（用 2B 表示）。

2 秒时，
- 回复信息 1A 到达服务器 1 ，服务器 1 不会再重发信息。
- 信息 2A 到达主服务器，主服务器立刻处理信息 2A 并发出 2A 的回复信息。
- 服务器 2 重发一条信息（用 2C 表示）。
...
4 秒时，
- 回复信息 2A 到达服务器 2 ，服务器 2 不会再重发信息。
...
7 秒时，回复信息 2D 到达服务器 2 。

从第 8 秒开始，不再有任何信息在服务器之间传输，也不再有信息到达服务器。
所以第 8 秒是网络变空闲的最早时刻。

```
 **示例 2：** 

<img alt="example 2" src="https://assets.leetcode.com/uploads/2021/09/04/network_a_quiet_place_2.png" style="width: 100px; height: 85px;">

```
输入：edges = [[0,1],[0,2],[1,2]], patience = [0,10,10]
输出：3
解释：数据服务器 1 和 2 第 2 秒初收到回复信息。
从第 3 秒开始，网络变空闲。

```
 

 **提示：** 
-  `n == patience.length` 
-  `2 <= n <= 10^5` 
-  `patience[0] == 0` 
- 对于 `1 <= i < n` ，满足 `1 <= patience[i] <= 10^5` 
-  `1 <= edges.length <= min(10^5, n * (n - 1) / 2)` 
-  `edges[i].length == 2` 
-  `0 <= u<sub>i</sub>, v<sub>i</sub> < n` 
-  `u<sub>i</sub> != v<sub>i</sub>` 
- 不会有重边。
- 每个服务器都直接或间接与别的服务器相连。
 
**标签**
`广度优先搜索` `图` `数组` 


## 
```python

```
>
# 2040.两个有序数组的第 K 小乘积
[https://leetcode-cn.com/problems/kth-smallest-product-of-two-sorted-arrays](https://leetcode-cn.com/problems/kth-smallest-product-of-two-sorted-arrays) 
## 原题
给你两个 **从小到大排好序** 且下标从 **0** 开始的整数数组 `nums1` 和 `nums2` 以及一个整数 `k` ，请你返回第 `k` （从 **1** 开始编号）小的 `nums1[i] * nums2[j]` 的乘积，其中 `0 <= i < nums1.length` 且 `0 <= j < nums2.length` 。
 

 **示例 1：** 

```
输入：nums1 = [2,5], nums2 = [3,4], k = 2
输出：8
解释：第 2 小的乘积计算如下：
- nums1[0] * nums2[0] = 2 * 3 = 6
- nums1[0] * nums2[1] = 2 * 4 = 8
第 2 小的乘积为 8 。

```
 **示例 2：** 

```
输入：nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
输出：0
解释：第 6 小的乘积计算如下：
- nums1[0] * nums2[1] = (-4) * 4 = -16
- nums1[0] * nums2[0] = (-4) * 2 = -8
- nums1[1] * nums2[1] = (-2) * 4 = -8
- nums1[1] * nums2[0] = (-2) * 2 = -4
- nums1[2] * nums2[0] = 0 * 2 = 0
- nums1[2] * nums2[1] = 0 * 4 = 0
第 6 小的乘积为 0 。

```
 **示例 3：** 

```
输入：nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
输出：-6
解释：第 3 小的乘积计算如下：
- nums1[0] * nums2[4] = (-2) * 5 = -10
- nums1[0] * nums2[3] = (-2) * 4 = -8
- nums1[4] * nums2[0] = 2 * (-3) = -6
第 3 小的乘积为 -6 。

```
 

 **提示：** 
-  `1 <= nums1.length, nums2.length <= 5 * 10^4` 
-  `-10^5 <= nums1[i], nums2[j] <= 10^5` 
-  `1 <= k <= nums1.length * nums2.length` 
-  `nums1` 和 `nums2` 都是从小到大排好序的。
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 2041.面试中被录取的候选人
[https://leetcode-cn.com/problems/accepted-candidates-from-the-interviews](https://leetcode-cn.com/problems/accepted-candidates-from-the-interviews) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 2042.检查句子中的数字是否递增
[https://leetcode-cn.com/problems/check-if-numbers-are-ascending-in-a-sentence](https://leetcode-cn.com/problems/check-if-numbers-are-ascending-in-a-sentence) 
## 原题
句子是由若干 **token** 组成的一个列表， **token** 间用 **单个** 空格分隔，句子没有前导或尾随空格。每个 token 要么是一个由数字 `0-9` 组成的不含前导零的 **正整数** ，要么是一个由小写英文字母组成的 **单词** 。
- 示例， `"a puppy has 2 eyes 4 legs"` 是一个由 7 个 token 组成的句子： `"2"` 和 `"4"` 是数字，其他像 `"puppy"` 这样的 tokens 属于单词。
给你一个表示句子的字符串 `s` ，你需要检查 `s` 中的 **全部** 数字是否从左到右严格递增（即，除了最后一个数字， `s` 中的 **每个** 数字都严格小于它 **右侧** 的数字）。

如果满足题目要求，返回 `true` ，否则，返回 `false` 。

 

 **示例 1：** 

<img alt="example-1" src="https://assets.leetcode.com/uploads/2021/09/30/example1.png" style="width: 637px; height: 48px;" />

```

输入：s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
输出：true
解释：句子中的数字是：1, 3, 4, 6, 12 。
这些数字是按从左到右严格递增的 1 < 3 < 4 < 6 < 12 。

```
 **示例 2：** 

```

输入：s = "hello world 5 x 5"
输出：false
解释：句子中的数字是：5, 5 。这些数字不是严格递增的。

```
 **示例 3：** 

<img alt="example-3" src="https://assets.leetcode.com/uploads/2021/09/30/example3.png" style="width: 794px; height: 48px;" />

```

输入：s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
输出：false
解释：s 中的数字是：7, 51, 50, 60 。这些数字不是严格递增的。

```
 **示例 4：** 

```

输入：s = "4 5 11 26"
输出：true
解释：s 中的数字是：4, 5, 11, 26 。
这些数字是按从左到右严格递增的：4 < 5 < 11 < 26 。

```
 

 **提示：** 
-  `3 <= s.length <= 200` 
-  `s` 由小写英文字母、空格和数字 `0` 到 `9` 组成（包含 `0` 和 `9` ）
-  `s` 中数字 token 的数目在 `2` 和 `100` 之间（包含 `2` 和 `100` ）
-  `s` 中的 token 之间由单个空格分隔
-  `s` 中至少有 **两个** 数字
-  `s` 中的每个数字都是一个 **小于** `100` 的 **正** 数，且不含前导零
-  `s` 不含前导或尾随空格
 
**标签**
`字符串` 


## 
```python

```
>
# 2043.简易银行系统
[https://leetcode-cn.com/problems/simple-bank-system](https://leetcode-cn.com/problems/simple-bank-system) 
## 原题
你的任务是为一个很受欢迎的银行设计一款程序，以自动化执行所有传入的交易（转账，存款和取款）。银行共有 `n` 个账户，编号从 `1` 到 `n` 。每个账号的初始余额存储在一个下标从 **0** 开始的整数数组 `balance` 中，其中第 `(i + 1)` 个账户的初始余额是 `balance[i]` 。

请你执行所有 **有效的** 交易。如果满足下面全部条件，则交易 **有效** ：
- 指定的账户数量在 `1` 和 `n` 之间，且
- 取款或者转账需要的钱的总数 **小于或者等于** 账户余额。
实现 `Bank` 类：
-  `Bank(long[] balance)` 使用下标从 **0** 开始的整数数组 `balance` 初始化该对象。
-  `boolean transfer(int account1, int account2, long money)` 从编号为 `account1` 的账户向编号为 `account2` 的账户转帐 `money` 美元。如果交易成功，返回 `true` ，否则，返回 `false` 。
-  `boolean deposit(int account, long money)` 向编号为 `account` 的账户存款 `money` 美元。如果交易成功，返回 `true` ；否则，返回 `false` 。
-  `boolean withdraw(int account, long money)` 从编号为 `account` 的账户取款 `money` 美元。如果交易成功，返回 `true` ；否则，返回 `false` 。
 

 **示例：** 

```

输入：
["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
输出：
[null, true, true, true, false, false]

解释：
Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // 返回 true ，账户 3 的余额是 $20 ，所以可以取款 $10 。
                         // 账户 3 余额为 $20 - $10 = $10 。
bank.transfer(5, 1, 20); // 返回 true ，账户 5 的余额是 $30 ，所以可以转账 $20 。
                         // 账户 5 的余额为 $30 - $20 = $10 ，账户 1 的余额为 $10 + $20 = $30 。
bank.deposit(5, 20);     // 返回 true ，可以向账户 5 存款 $20 。
                         // 账户 5 的余额为 $10 + $20 = $30 。
bank.transfer(3, 4, 15); // 返回 false ，账户 3 的当前余额是 $10 。
                         // 所以无法转账 $15 。
bank.withdraw(10, 50);   // 返回 false ，交易无效，因为账户 10 并不存在。

```
 

 **提示：** 
-  `n == balance.length` 
-  `1 <= n, account, account1, account2 <= 10^5` 
-  `0 <= balance[i], money <= 10^12` 
-  `transfer` , `deposit` , `withdraw` 三个函数， **每个** 最多调用 `10^4` 次
 
**标签**
`设计` `数组` `哈希表` `模拟` 


## 
```python

```
>
# 2044.统计按位或能得到最大值的子集数目
[https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets](https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets) 
## 原题
给你一个整数数组 `nums` ，请你找出 `nums` 子集 **按位或** 可能得到的 **** **最大值** ，并返回按位或能得到最大值的 **不同非空子集的数目** 。

如果数组 `a` 可以由数组 `b` 删除一些元素（或不删除）得到，则认为数组 `a` 是数组 `b` 的一个 **子集** 。如果选中的元素下标位置不一样，则认为两个子集 **不同** 。

对数组 `a` 执行 **按位或** ，结果等于 `a[0] **OR** a[1] **OR** ... **OR** a[a.length - 1]` （下标从 **0** 开始）。

 

 **示例 1：** 

```

输入：nums = [3,1]
输出：2
解释：子集按位或能得到的最大值是 3 。有 2 个子集按位或可以得到 3 ：
- [3]
- [3,1]

```
 **示例 2：** 

```

输入：nums = [2,2,2]
输出：7
解释：[2,2,2] 的所有非空子集的按位或都可以得到 2 。总共有 2^3 - 1 = 7 个子集。

```
 **示例 3：** 

```

输入：nums = [3,2,1,5]
输出：6
解释：子集按位或可能的最大值是 7 。有 6 个子集按位或可以得到 7 ：
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
```
 

 **提示：** 
-  `1 <= nums.length <= 16` 
-  `1 <= nums[i] <= 10^5` 
 
**标签**
`位运算` `数组` `回溯` 


## 
```python

```
>
# 2045.到达目的地的第二短时间
[https://leetcode-cn.com/problems/second-minimum-time-to-reach-destination](https://leetcode-cn.com/problems/second-minimum-time-to-reach-destination) 
## 原题
城市用一个 **双向连通** 图表示，图中有 `n` 个节点，从 `1` 到 `n` 编号（包含 `1` 和 `n` ）。图中的边用一个二维整数数组 `edges` 表示，其中每个 `edges[i] = [u<sub>i</sub>, v<sub>i</sub>]` 表示一条节点 `u<sub>i</sub>` 和节点 `v<sub>i</sub>` 之间的双向连通边。每组节点对由 **最多一条** 边连通，顶点不存在连接到自身的边。穿过任意一条边的时间是 `time` 分钟。

每个节点都有一个交通信号灯，每 `change` 分钟改变一次，从绿色变成红色，再由红色变成绿色，循环往复。所有信号灯都 **同时** 改变。你可以在 **任何时候** 进入某个节点，但是 **只能** 在节点 **信号灯是绿色时** 才能离开。如果信号灯是 **绿色** ，你 **不能** 在节点等待，必须离开。

 **第二小的值** 是 **严格大于** 最小值的所有值中最小的值。
- 例如， `[2, 3, 4]` 中第二小的值是 `3` ，而 `[2, 2, 4]` 中第二小的值是 `4` 。
给你 `n` 、 `edges` 、 `time` 和 `change` ，返回从节点 `1` 到节点 `n` 需要的 **第二短时间** 。

 **注意：** 
- 你可以 **任意次** 穿过任意顶点， **包括** `1` 和 `n` 。
- 你可以假设在 **启程时** ，所有信号灯刚刚变成 **绿色** 。
 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/29/e1.png" style="width: 200px; height: 250px;" />        <img alt="" src="https://assets.leetcode.com/uploads/2021/09/29/e2.png" style="width: 200px; height: 250px;" />

```

输入：n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
输出：13
解释：
上面的左图展现了给出的城市交通图。
右图中的蓝色路径是最短时间路径。
花费的时间是：
- 从节点 1 开始，总花费时间=0
- 1 -> 4：3 分钟，总花费时间=3
- 4 -> 5：3 分钟，总花费时间=6
因此需要的最小时间是 6 分钟。

右图中的红色路径是第二短时间路径。
- 从节点 1 开始，总花费时间=0
- 1 -> 3：3 分钟，总花费时间=3
- 3 -> 4：3 分钟，总花费时间=6
- 在节点 4 等待 4 分钟，总花费时间=10
- 4 -> 5：3 分钟，总花费时间=13
因此第二短时间是 13 分钟。      

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/29/eg2.png" style="width: 225px; height: 50px;" />

```

输入：n = 2, edges = [[1,2]], time = 3, change = 2
输出：11
解释：
最短时间路径是 1 -> 2 ，总花费时间 = 3 分钟
第二短时间路径是 1 -> 2 -> 1 -> 2 ，总花费时间 = 11 分钟
```
 

 **提示：** 
-  `2 <= n <= 10^4` 
-  `n - 1 <= edges.length <= min(2 * 10^4, n * (n - 1) / 2)` 
-  `edges[i].length == 2` 
-  `1 <= u<sub>i</sub>, v<sub>i</sub> <= n` 
-  `u<sub>i</sub> != v<sub>i</sub>` 
- 不含重复边
- 每个节点都可以从其他节点直接或者间接到达
-  `1 <= time, change <= 10^3` 
 
**标签**
`广度优先搜索` `图` `最短路` 


## 
```python

```
>
# 2046.给按照绝对值排序的链表排序
[https://leetcode-cn.com/problems/sort-linked-list-already-sorted-using-absolute-values](https://leetcode-cn.com/problems/sort-linked-list-already-sorted-using-absolute-values) 
## 原题

 
**标签**
`链表` `双指针` `排序` 


## 
```python

```
>
# 2047.句子中的有效单词数
[https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence](https://leetcode-cn.com/problems/number-of-valid-words-in-a-sentence) 
## 原题
句子仅由小写字母（ `'a'` 到 `'z'` ）、数字（ `'0'` 到 `'9'` ）、连字符（ `'-'` ）、标点符号（ `'!'` 、 `'.'` 和 `','` ）以及空格（ `' '` ）组成。每个句子可以根据空格分解成 **一个或者多个 token** ，这些 token 之间由一个或者多个空格 `' '` 分隔。

如果一个 token 同时满足下述条件，则认为这个 token 是一个有效单词：
- 仅由小写字母、连字符和/或标点（不含数字）组成。
-  **至多一个** 连字符 `'-'` 。如果存在，连字符两侧应当都存在小写字母（ `"a-b"` 是一个有效单词，但 `"-ab"` 和 `"ab-"` 不是有效单词）。
-  **至多一个** 标点符号。如果存在，标点符号应当位于 token 的 **末尾** 。
这里给出几个有效单词的例子： `"a-b."` 、 `"afad"` 、 `"ba-c"` 、 `"a!"` 和 `"!"` 。

给你一个字符串 `sentence` ，请你找出并返回 `sentence` 中 **有效单词的数目** 。

 

 **示例 1：** 

```

输入：sentence = "cat and  dog"
输出：3
解释：句子中的有效单词是 "cat"、"and" 和 "dog"

```
 **示例 2：** 

```

输入：sentence = "!this  1-s b8d!"
输出：0
解释：句子中没有有效单词
"!this" 不是有效单词，因为它以一个标点开头
"1-s" 和 "b8d" 也不是有效单词，因为它们都包含数字

```
 **示例 3：** 

```

输入：sentence = "alice and  bob are playing stone-game10"
输出：5
解释：句子中的有效单词是 "alice"、"and"、"bob"、"are" 和 "playing"
"stone-game10" 不是有效单词，因为它含有数字

```
 **示例 4：** 

```

输入：sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
输出：6
解释：句子中的有效单词是 "he"、"bought"、"pencils,"、"erasers,"、"and" 和 "pencil-sharpener."

```
 

 **提示：** 
-  `1 <= sentence.length <= 1000` 
-  `sentence` 由小写英文字母、数字（ `0-9` ）、以及字符（ `' '` 、 `'-'` 、 `'!'` 、 `'.'` 和 `','` ）组成
- 句子中至少有 `1` 个 token
 
**标签**
`字符串` 


## 
```python

```
>
# 2048.下一个更大的数值平衡数
[https://leetcode-cn.com/problems/next-greater-numerically-balanced-number](https://leetcode-cn.com/problems/next-greater-numerically-balanced-number) 
## 原题
如果整数 `x` 满足：对于每个数位 `d` ，这个数位 **恰好** 在 `x` 中出现 `d` 次。那么整数 `x` 就是一个 **数值平衡数** 。

给你一个整数 `n` ，请你返回 **严格大于** `n` 的 **最小数值平衡数** 。

 

 **示例 1：** 

```

输入：n = 1
输出：22
解释：
22 是一个数值平衡数，因为：
- 数字 2 出现 2 次 
这也是严格大于 1 的最小数值平衡数。

```
 **示例 2：** 

```

输入：n = 1000
输出：1333
解释：
1333 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。 
这也是严格大于 1000 的最小数值平衡数。
注意，1022 不能作为本输入的答案，因为数字 0 的出现次数超过了 0 。
```
 **示例 3：** 

```

输入：n = 3000
输出：3133
解释：
3133 是一个数值平衡数，因为：
- 数字 1 出现 1 次。
- 数字 3 出现 3 次。 
这也是严格大于 3000 的最小数值平衡数。

```
 

 **提示：** 
-  `0 <= n <= 10^6` 
 
**标签**
`数学` `回溯` `枚举` 


## 
```python

```
>
# 2049.统计最高分的节点数目
[https://leetcode-cn.com/problems/count-nodes-with-the-highest-score](https://leetcode-cn.com/problems/count-nodes-with-the-highest-score) 
## 原题
给你一棵根节点为 `0` 的 **二叉树** ，它总共有 `n` 个节点，节点编号为 `0` 到 `n - 1` 。同时给你一个下标从 **0** 开始的整数数组 `parents` 表示这棵树，其中 `parents[i]` 是节点 `i` 的父节点。由于节点 `0` 是根，所以 `parents[0] == -1` 。

一个子树的 **大小** 为这个子树内节点的数目。每个节点都有一个与之关联的 **分数** 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 **删除** ，剩余部分是若干个 **非空** 子树，这个节点的 **分数** 为所有这些子树 **大小的乘积** 。

请你返回有 **最高得分** 节点的 **数目** 。

 

 **示例 1:** 

<img alt="example-1" src="https://assets.leetcode.com/uploads/2021/10/03/example-1.png" style="width: 604px; height: 266px;">

```
输入：parents = [-1,2,0,2,0]
输出：3
解释：
- 节点 0 的分数为：3 * 1 = 3
- 节点 1 的分数为：4 = 4
- 节点 2 的分数为：1 * 1 * 2 = 2
- 节点 3 的分数为：4 = 4
- 节点 4 的分数为：4 = 4
最高得分为 4 ，有三个节点得分为 4 （分别是节点 1，3 和 4 ）。

```
 **示例 2：** 

<img alt="example-2" src="https://assets.leetcode.com/uploads/2021/10/03/example-2.png" style="width: 95px; height: 143px;">

```
输入：parents = [-1,2,0]
输出：2
解释：
- 节点 0 的分数为：2 = 2
- 节点 1 的分数为：2 = 2
- 节点 2 的分数为：1 * 1 = 1
最高分数为 2 ，有两个节点分数为 2 （分别为节点 0 和 1 ）。

```
 

 **提示：** 
-  `n == parents.length` 
-  `2 <= n <= 10^5` 
-  `parents[0] == -1` 
- 对于 `i != 0` ，有 `0 <= parents[i] <= n - 1` 
-  `parents` 表示一棵二叉树。
 
**标签**
`树` `深度优先搜索` `数组` `二叉树` 


## 
```python

```
>
# 2050.并行课程 III
[https://leetcode-cn.com/problems/parallel-courses-iii](https://leetcode-cn.com/problems/parallel-courses-iii) 
## 原题
给你一个整数 `n` ，表示有 `n` 节课，课程编号从 `1` 到 `n` 。同时给你一个二维整数数组 `relations` ，其中 `relations[j] = [prevCourse<sub>j</sub>, nextCourse<sub>j</sub>]` ，表示课程 `prevCourse<sub>j</sub>` 必须在课程 `nextCourse<sub>j</sub>` **之前** 完成（先修课的关系）。同时给你一个下标从 **0** 开始的整数数组 `time` ，其中 `time[i]` 表示完成第 `(i+1)` 门课程需要花费的 **月份** 数。

请你根据以下规则算出完成所有课程所需要的 **最少** 月份数：
- 如果一门课的所有先修课都已经完成，你可以在 **任意** 时间开始这门课程。
- 你可以 **同时** 上 **任意门课程** 。
请你返回完成所有课程所需要的 **最少** 月份数。

 **注意：** 测试数据保证一定可以完成所有课程（也就是先修课的关系构成一个有向无环图）。

 

 **示例 1:** 

 **<img alt="" src="https://assets.leetcode.com/uploads/2021/10/07/ex1.png" style="width: 392px; height: 232px;">** 

```
输入：n = 3, relations = [[1,3],[2,3]], time = [3,2,5]
输出：8
解释：上图展示了输入数据所表示的先修关系图，以及完成每门课程需要花费的时间。
你可以在月份 0 同时开始课程 1 和 2 。
课程 1 花费 3 个月，课程 2 花费 2 个月。
所以，最早开始课程 3 的时间是月份 3 ，完成所有课程所需时间为 3 + 5 = 8 个月。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode.com/uploads/2021/10/07/ex2.png" style="width: 500px; height: 365px;">** 

```
输入：n = 5, relations = [[1,5],[2,5],[3,5],[3,4],[4,5]], time = [1,2,3,4,5]
输出：12
解释：上图展示了输入数据所表示的先修关系图，以及完成每门课程需要花费的时间。
你可以在月份 0 同时开始课程 1 ，2 和 3 。
在月份 1，2 和 3 分别完成这三门课程。
课程 4 需在课程 3 之后开始，也就是 3 个月后。课程 4 在 3 + 4 = 7 月完成。
课程 5 需在课程 1，2，3 和 4 之后开始，也就是在 max(1,2,3,7) = 7 月开始。
所以完成所有课程所需的最少时间为 7 + 5 = 12 个月。

```
 

 **提示：** 
-  `1 <= n <= 5 * 10^4` 
-  `0 <= relations.length <= min(n * (n - 1) / 2, 5 * 10^4)` 
-  `relations[j].length == 2` 
-  `1 <= prevCourse<sub>j</sub>, nextCourse<sub>j</sub> <= n` 
-  `prevCourse<sub>j</sub> != nextCourse<sub>j</sub>` 
- 所有的先修课程对 `[prevCourse<sub>j</sub>, nextCourse<sub>j</sub>]` 都是 **互不相同** 的。
-  `time.length == n` 
-  `1 <= time[i] <= 10^4` 
- 先修课程图是一个有向无环图。
 
**标签**
`图` `拓扑排序` `动态规划` 


## 
```python

```
>
# 2052.将句子分隔成行的最低成本
[https://leetcode-cn.com/problems/minimum-cost-to-separate-sentence-into-rows](https://leetcode-cn.com/problems/minimum-cost-to-separate-sentence-into-rows) 
## 原题

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 2053.数组中第 K 个独一无二的字符串
[https://leetcode-cn.com/problems/kth-distinct-string-in-an-array](https://leetcode-cn.com/problems/kth-distinct-string-in-an-array) 
## 原题
 **独一无二的字符串** 指的是在一个数组中只出现过 **一次** 的字符串。

给你一个字符串数组 `arr` 和一个整数 `k` ，请你返回 `arr` 中第 `k` 个 **独一无二的字符串** 。如果 **少于** `k` 个独一无二的字符串，那么返回 **空字符串** `""` 。

注意，按照字符串在原数组中的 **顺序** 找到第 `k` 个独一无二字符串。

 

 **示例 1:** 

```
输入：arr = ["d","b","c","b","c","a"], k = 2
输出："a"
解释：
arr 中独一无二字符串包括 "d" 和 "a" 。
"d" 首先出现，所以它是第 1 个独一无二字符串。
"a" 第二个出现，所以它是 2 个独一无二字符串。
由于 k == 2 ，返回 "a" 。

```
 **示例 2:** 

```
输入：arr = ["aaa","aa","a"], k = 1
输出："aaa"
解释：
arr 中所有字符串都是独一无二的，所以返回第 1 个字符串 "aaa" 。

```
 **示例 3：** 

```
输入：arr = ["a","b","a"], k = 3
输出：""
解释：
唯一一个独一无二字符串是 "b" 。由于少于 3 个独一无二字符串，我们返回空字符串 "" 。

```
 

 **提示：** 
-  `1 <= k <= arr.length <= 1000` 
-  `1 <= arr[i].length <= 5` 
-  `arr[i]` 只包含小写英文字母。
 
**标签**
`数组` `哈希表` `字符串` `计数` 


## 
```python

```
>
# 2054.两个最好的不重叠活动
[https://leetcode-cn.com/problems/two-best-non-overlapping-events](https://leetcode-cn.com/problems/two-best-non-overlapping-events) 
## 原题
给你一个下标从 **0** 开始的二维整数数组 `events` ，其中 `events[i] = [startTime<sub>i</sub>, endTime<sub>i</sub>, value<sub>i</sub>]` 。第 `i` 个活动开始于 `startTime<sub>i</sub>` ，结束于 `endTime<sub>i</sub>` ，如果你参加这个活动，那么你可以得到价值 `value<sub>i</sub>` 。你 **最多** 可以参加 **两个时间不重叠** 活动，使得它们的价值之和 **最大** 。

请你返回价值之和的 **最大值** 。

注意，活动的开始时间和结束时间是 **包括** 在活动时间内的，也就是说，你不能参加两个活动且它们之一的开始时间等于另一个活动的结束时间。更具体的，如果你参加一个活动，且结束时间为 `t` ，那么下一个活动必须在 `t + 1` 或之后的时间开始。

 

 **示例 1:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/picture5.png" style="width: 400px; height: 75px;">

```
输入：events = [[1,3,2],[4,5,2],[2,4,3]]
输出：4
解释：选择绿色的活动 0 和 1 ，价值之和为 2 + 2 = 4 。

```
 **示例 2：** 

<img alt="Example 1 Diagram" src="https://assets.leetcode.com/uploads/2021/09/21/picture1.png" style="width: 400px; height: 77px;">

```
输入：events = [[1,3,2],[4,5,2],[1,5,5]]
输出：5
解释：选择活动 2 ，价值和为 5 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/21/picture3.png" style="width: 400px; height: 66px;">

```
输入：events = [[1,5,3],[1,5,1],[6,6,5]]
输出：8
解释：选择活动 0 和 2 ，价值之和为 3 + 5 = 8 。
```
 

 **提示：** 
-  `2 <= events.length <= 10^5` 
-  `events[i].length == 3` 
-  `1 <= startTime<sub>i</sub> <= endTime<sub>i</sub> <= 10^9` 
-  `1 <= value<sub>i</sub> <= 10^6` 
 
**标签**
`数组` `二分查找` `动态规划` `排序` `堆（优先队列）` 


## 
```python

```
>
# 2055.蜡烛之间的盘子
[https://leetcode-cn.com/problems/plates-between-candles](https://leetcode-cn.com/problems/plates-between-candles) 
## 原题
给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 **0** 开始的字符串 `s` ，它只包含字符 `'*'` 和 `'|'` ，其中 `'*'` 表示一个 **盘子** ， `'|'` 表示一支 **蜡烛** 。

同时给你一个下标从 **0** 开始的二维整数数组 `queries` ，其中 `queries[i] = [left<sub>i</sub>, right<sub>i</sub>]` 表示 **子字符串** `s[left<sub>i</sub>...right<sub>i</sub>]` （ **包含左右端点的字符** ）。对于每个查询，你需要找到 **子字符串中** 在 **两支蜡烛之间** 的盘子的 <b>数目</b> 。如果一个盘子在 **子字符串中** 左边和右边 **都** 至少有一支蜡烛，那么这个盘子满足在 **两支蜡烛之间** 。
- 比方说， `s = "||**||**|*"` ，查询 `[3, 8]` ，表示的是子字符串 `"*|| ** **** ** |"` 。子字符串中在两支蜡烛之间的盘子数目为 `2` ，子字符串中右边两个盘子在它们左边和右边 **都** 至少有一支蜡烛。
请你返回一个整数数组 `answer` ，其中 `answer[i]` 是第 `i` 个查询的答案。

 

 **示例 1:** 

<img alt="ex-1" src="https://assets.leetcode.com/uploads/2021/10/04/ex-1.png" style="width: 400px; height: 134px;">

```
输入：s = "**|**|***|", queries = [[2,5],[5,9]]
输出：[2,3]
解释：
- queries[0] 有两个盘子在蜡烛之间。
- queries[1] 有三个盘子在蜡烛之间。

```
 **示例 2:** 

<img alt="ex-2" src="https://assets.leetcode.com/uploads/2021/10/04/ex-2.png" style="width: 600px; height: 193px;">

```
输入：s = "***|**|*****|**||**|*", queries = [[1,17],[4,5],[14,17],[5,11],[15,16]]
输出：[9,0,0,0,0]
解释：
- queries[0] 有 9 个盘子在蜡烛之间。
- 另一个查询没有盘子在蜡烛之间。

```
 

 **提示：** 
-  `3 <= s.length <= 10^5` 
-  `s` 只包含字符 `'*'` 和 `'|'` 。
-  `1 <= queries.length <= 10^5` 
-  `queries[i].length == 2` 
-  `0 <= left<sub>i</sub> <= right<sub>i</sub> < s.length` 
 
**标签**
`数组` `字符串` `二分查找` `前缀和` 


## 
```python

```
>
# 2056.棋盘上有效移动组合的数目
[https://leetcode-cn.com/problems/number-of-valid-move-combinations-on-chessboard](https://leetcode-cn.com/problems/number-of-valid-move-combinations-on-chessboard) 
## 原题
有一个 `8 x 8` 的棋盘，它包含 `n` 个棋子（棋子包括车，后和象三种）。给你一个长度为 `n` 的字符串数组 `pieces` ，其中 `pieces[i]` 表示第 `i` 个棋子的类型（车，后或象）。除此以外，还给你一个长度为 `n` 的二维整数数组 `positions` ，其中 `positions[i] = [r<sub>i</sub>, c<sub>i</sub>]` 表示第 `i` 个棋子现在在棋盘上的位置为 `(r<sub>i</sub>, c<sub>i</sub>)` ，棋盘下标从 **1** 开始。

棋盘上每个棋子都可以移动 <b>至多一次</b> 。每个棋子的移动中，首先选择移动的 **方向** ，然后选择 **移动的步数** ，同时你要确保移动过程中棋子不能移到棋盘以外的地方。棋子需按照以下规则移动：
- 车可以 **水平或者竖直** 从 `(r, c)` 沿着方向 `(r+1, c)` ， `(r-1, c)` ， `(r, c+1)` 或者 `(r, c-1)` 移动。
- 后可以 **水平竖直或者斜对角** 从 `(r, c)` 沿着方向 `(r+1, c)` ， `(r-1, c)` ， `(r, c+1)` ， `(r, c-1)` ， `(r+1, c+1)` ， `(r+1, c-1)` ， `(r-1, c+1)` ， `(r-1, c-1)` 移动。
- 象可以 **斜对角** 从 `(r, c)` 沿着方向 `(r+1, c+1)` ， `(r+1, c-1)` ， `(r-1, c+1)` ， `(r-1, c-1)` 移动。
 **移动组合** 包含所有棋子的 **移动** 。每一秒，每个棋子都沿着它们选择的方向往前移动 **一步** ，直到它们到达目标位置。所有棋子从时刻 `0` 开始移动。如果在某个时刻，两个或者更多棋子占据了同一个格子，那么这个移动组合 **不有效** 。

请你返回 **有效** 移动组合的数目。

 **注意：** 
- 初始时， **不会有两个棋子** 在 **同一个位置 。** 
- 有可能在一个移动组合中，有棋子不移动。
- 如果两个棋子 **直接相邻** 且两个棋子下一秒要互相占据对方的位置，可以将它们在同一秒内 **交换位置** 。
 

 **示例 1:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/23/a1.png" style="width: 215px; height: 215px;" />

```

输入：pieces = ["rook"], positions = [[1,1]]
输出：15
解释：上图展示了棋子所有可能的移动。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/23/a2.png" style="width: 215px; height: 215px;" />

```

输入：pieces = ["queen"], positions = [[1,1]]
输出：22
解释：上图展示了棋子所有可能的移动。

```
 **示例 3:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/23/a3.png" style="width: 214px; height: 215px;" />

```

输入：pieces = ["bishop"], positions = [[4,3]]
输出：12
解释：上图展示了棋子所有可能的移动。

```
 **示例 4:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/23/a4.png" style="width: 216px; height: 219px;" />

```

输入：pieces = ["rook","rook"], positions = [[1,1],[8,8]]
输出：223
解释：每个车有 15 种移动，所以总共有 15 * 15 = 225 种移动组合。
但是，有两个是不有效的移动组合：
- 将两个车都移动到 (8, 1) ，会导致它们在同一个格子相遇。
- 将两个车都移动到 (1, 8) ，会导致它们在同一个格子相遇。
所以，总共有 225 - 2 = 223 种有效移动组合。
注意，有两种有效的移动组合，分别是一个车在 (1, 8) ，另一个车在 (8, 1) 。
即使棋盘状态是相同的，这两个移动组合被视为不同的，因为每个棋子移动操作是不相同的。

```
 **示例 5：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/09/23/a5.png" style="width: 214px; height: 213px;" />

```

输入：pieces = ["queen","bishop"], positions = [[5,7],[3,4]]
输出：281
解释：总共有 12 * 24 = 288 种移动组合。
但是，有一些不有效的移动组合：
- 如果后停在 (6, 7) ，它会阻挡象到达 (6, 7) 或者 (7, 8) 。
- 如果后停在 (5, 6) ，它会阻挡象到达 (5, 6) ，(6, 7) 或者 (7, 8) 。
- 如果象停在 (5, 2) ，它会阻挡后到达 (5, 2) 或者 (5, 1) 。
在 288 个移动组合当中，281 个是有效的。

```
 

 **提示：** 
-  `n == pieces.length` 
-  `n == positions.length` 
-  `1 <= n <= 4` 
-  `pieces` 只包含字符串 `"rook"` ， `"queen"` 和 `"bishop"` 。
- 棋盘上总共最多只有一个后。
-  `1 <= x<sub>i</sub>, y<sub>i</sub> <= 8` 
- 每一个 `positions[i]` 互不相同。
 
**标签**
`数组` `字符串` `回溯` `模拟` 


## 
```python

```
>
# 2057.值相等的最小索引
[https://leetcode-cn.com/problems/smallest-index-with-equal-value](https://leetcode-cn.com/problems/smallest-index-with-equal-value) 
## 原题
给你一个下标从 0 开始的整数数组 `nums` ，返回 `nums` 中满足 `i mod 10 == nums[i]` 的最小下标 `i` ；如果不存在这样的下标，返回 `-1` 。

 `x mod y` 表示 `x` 除以 `y` 的 **余数** 。

 

 **示例 1：** 

```
输入：nums = [0,1,2]
输出：0
解释：
i=0: 0 mod 10 = 0 == nums[0].
i=1: 1 mod 10 = 1 == nums[1].
i=2: 2 mod 10 = 2 == nums[2].
所有下标都满足 i mod 10 == nums[i] ，所以返回最小下标 0

```
 **示例 2：** 

```
输入：nums = [4,3,2,1]
输出：2
解释：
i=0: 0 mod 10 = 0 != nums[0].
i=1: 1 mod 10 = 1 != nums[1].
i=2: 2 mod 10 = 2 == nums[2].
i=3: 3 mod 10 = 3 != nums[3].
2 唯一一个满足 i mod 10 == nums[i] 的下标

```
 **示例 3：** 

```
输入：nums = [1,2,3,4,5,6,7,8,9,0]
输出：-1
解释：不存在满足 i mod 10 == nums[i] 的下标

```
 **示例 4：** 

```
输入：nums = [2,1,3,5,2]
输出：1
解释：1 是唯一一个满足 i mod 10 == nums[i] 的下标

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `0 <= nums[i] <= 9` 
 
**标签**
`数组` 


## 
```python

```
>
# 2058.找出临界点之间的最小和最大距离
[https://leetcode-cn.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points](https://leetcode-cn.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points) 
## 原题
链表中的 **临界点** 定义为一个 **局部极大值点** **或** **局部极小值点 。** 

如果当前节点的值 **严格大于** 前一个节点和后一个节点，那么这个节点就是一个 **局部极大值点** 。

如果当前节点的值 **严格小于** 前一个节点和后一个节点，那么这个节点就是一个 **局部极小值点** 。

注意：节点只有在同时存在前一个节点和后一个节点的情况下，才能成为一个 **局部极大值点 / 极小值点** 。

给你一个链表 `head` ，返回一个长度为 2 的数组 `[minDistance, maxDistance]` ，其中 `minDistance` 是任意两个不同临界点之间的最小距离， `maxDistance` 是任意两个不同临界点之间的最大距离。如果临界点少于两个，则返回 `[-1，-1]` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/13/a1.png" style="width: 148px; height: 55px;" />

```

输入：head = [3,1]
输出：[-1,-1]
解释：链表 [3,1] 中不存在临界点。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/13/a2.png" style="width: 624px; height: 46px;" />

```

输入：head = [5,3,1,2,5,1,2]
输出：[1,3]
解释：存在三个临界点：
- [5,3,1,2,5,1,2]：第三个节点是一个局部极小值点，因为 1 比 3 和 2 小。
- [5,3,1,2,5,1,2]：第五个节点是一个局部极大值点，因为 5 比 2 和 1 大。
- [5,3,1,2,5,1,2]：第六个节点是一个局部极小值点，因为 1 比 5 和 2 小。
第五个节点和第六个节点之间距离最小。minDistance = 6 - 5 = 1 。
第三个节点和第六个节点之间距离最大。maxDistance = 6 - 3 = 3 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/14/a5.png" style="width: 624px; height: 39px;" />

```

输入：head = [1,3,2,2,3,2,2,2,7]
输出：[3,3]
解释：存在两个临界点：
- [1,3,2,2,3,2,2,2,7]：第二个节点是一个局部极大值点，因为 3 比 1 和 2 大。
- [1,3,2,2,3,2,2,2,7]：第五个节点是一个局部极大值点，因为 3 比 2 和 2 大。
最小和最大距离都存在于第二个节点和第五个节点之间。
因此，minDistance 和 maxDistance 是 5 - 2 = 3 。
注意，最后一个节点不算一个局部极大值点，因为它之后就没有节点了。

```
 **示例 4：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/13/a4.png" style="width: 345px; height: 52px;" />

```

输入：head = [2,3,3,2]
输出：[-1,-1]
解释：链表 [2,3,3,2] 中不存在临界点。

```
 

 **提示：** 
- 链表中节点的数量在范围 `[2, 10^5]` 内
-  `1 <= Node.val <= 10^5` 
 
**标签**
`链表` 


## 
```python

```
>
# 2059.转化数字的最小运算数
[https://leetcode-cn.com/problems/minimum-operations-to-convert-number](https://leetcode-cn.com/problems/minimum-operations-to-convert-number) 
## 原题
给你一个下标从 **0** 开始的整数数组 `nums` ，该数组由 **互不相同** 的数字组成。另给你两个整数 `start` 和 `goal` 。

整数 `x` 的值最开始设为 `start` ，你打算执行一些运算使 `x` 转化为 `goal` 。你可以对数字 `x` 重复执行下述运算：

如果 `0 <= x <= 1000` ，那么，对于数组中的任一下标 `i` （ `0 <= i < nums.length` ），可以将 `x` 设为下述任一值：
-  `x + nums[i]` 
-  `x - nums[i]` 
-  `x ^ nums[i]` （按位异或 XOR）
注意，你可以按任意顺序使用每个 `nums[i]` 任意次。使 `x` 越过 `0 <= x <= 1000` 范围的运算同样可以生效，但该运算执行后将不能执行其他运算。

返回将 `x = start` 转化为 `goal` 的最小操作数；如果无法完成转化，则返回 `-1` 。

 

 **示例 1：** 

```

输入：nums = [1,3], start = 6, goal = 4
输出：2
解释：
可以按 6 → 7 → 4 的转化路径进行，只需执行下述 2 次运算：
- 6 ^ 1 = 7
- 7 ^ 3 = 4

```
 **示例 2：** 

```

输入：nums = [2,4,12], start = 2, goal = 12
输出：2
解释：
可以按 2 → 14 → 12 的转化路径进行，只需执行下述 2 次运算：
- 2 + 12 = 14
- 14 - 2 = 12

```
 **示例 3：** 

```

输入：nums = [3,5,7], start = 0, goal = -4
输出：2
解释：
可以按 0 → 3 → -4 的转化路径进行，只需执行下述 2 次运算：
- 0 + 3 = 3
- 3 - 7 = -4
注意，最后一步运算使 x 超过范围 0 <= x <= 1000 ，但该运算仍然可以生效。

```
 **示例 4：** 

```

输入：nums = [2,8,16], start = 0, goal = 1
输出：-1
解释：
无法将 0 转化为 1
```
 **示例 5：** 

```

输入：nums = [1], start = 0, goal = 3
输出：3
解释：
可以按 0 → 1 → 2 → 3 的转化路径进行，只需执行下述 3 次运算：
- 0 + 1 = 1 
- 1 + 1 = 2
- 2 + 1 = 3

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `-10^9 <= nums[i], goal <= 10^9` 
-  `0 <= start <= 1000` 
-  `start != goal` 
-  `nums` 中的所有整数互不相同
 
**标签**
`广度优先搜索` `数组` 


## 
```python

```
>
# 2061.扫地机器人清扫过的空间个数
[https://leetcode-cn.com/problems/number-of-spaces-cleaning-robot-cleaned](https://leetcode-cn.com/problems/number-of-spaces-cleaning-robot-cleaned) 
## 原题

 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 2062.统计字符串中的元音子字符串
[https://leetcode-cn.com/problems/count-vowel-substrings-of-a-string](https://leetcode-cn.com/problems/count-vowel-substrings-of-a-string) 
## 原题
 **子字符串** 是字符串中的一个连续（非空）的字符序列。

 **元音子字符串** 是 **仅** 由元音（ `'a'` 、 `'e'` 、 `'i'` 、 `'o'` 和 `'u'` ）组成的一个子字符串，且必须包含 **全部五种** 元音。

给你一个字符串 `word` ，统计并返回 `word` 中 **元音子字符串的数目** 。

 

 **示例 1：** 

```

输入：word = "aeiouu"
输出：2
解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
- "aeiouu"
- "aeiouu"

```
 **示例 2：** 

```

输入：word = "unicornarihan"
输出：0
解释：word 中不含 5 种元音，所以也不会存在元音子字符串。

```
 **示例 3：** 

```

输入：word = "cuaieuouac"
输出：7
解释：下面列出 word 中的元音子字符串（斜体加粗部分）：
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
- "cuaieuouac"
```
 **示例 4：** 

```

输入：word = "bbaeixoubb"
输出：0
解释：所有包含全部五种元音的子字符串都含有辅音，所以不存在元音子字符串。

```
 

 **提示：** 
-  `1 <= word.length <= 100` 
-  `word` 仅由小写英文字母组成
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 2063.所有子字符串中的元音
[https://leetcode-cn.com/problems/vowels-of-all-substrings](https://leetcode-cn.com/problems/vowels-of-all-substrings) 
## 原题
给你一个字符串 `word` ，返回 `word` 的所有子字符串中 **元音的总数** ，元音是指 `'a'` 、 `'e'` *、* `'i'` *、* `'o'` 和 `'u'` *。* 

 **子字符串** 是字符串中一个连续（非空）的字符序列。

 **注意：** 由于对 `word` 长度的限制比较宽松，答案可能超过有符号 32 位整数的范围。计算时需当心。

 

 **示例 1：** 

```

输入：word = "aba"
输出：6
解释：
所有子字符串是："a"、"ab"、"aba"、"b"、"ba" 和 "a" 。
- "b" 中有 0 个元音
- "a"、"ab"、"ba" 和 "a" 每个都有 1 个元音
- "aba" 中有 2 个元音
因此，元音总数 = 0 + 1 + 1 + 1 + 1 + 2 = 6 。

```
 **示例 2：** 

```

输入：word = "abc"
输出：3
解释：
所有子字符串是："a"、"ab"、"abc"、"b"、"bc" 和 "c" 。
- "a"、"ab" 和 "abc" 每个都有 1 个元音
- "b"、"bc" 和 "c" 每个都有 0 个元音
因此，元音总数 = 1 + 1 + 1 + 0 + 0 + 0 = 3 。
```
 **示例 3：** 

```

输入：word = "ltcd"
输出：0
解释："ltcd" 的子字符串均不含元音。
```
 **示例 4：** 

```

输入：word = "noosabasboosa"
输出：237
解释：所有子字符串中共有 237 个元音。

```
 

 **提示：** 
-  `1 <= word.length <= 10^5` 
-  `word` 由小写英文字母组成
 
**标签**
`数学` `字符串` `动态规划` `组合数学` 


## 
```python

```
>
# 2064.分配给商店的最多商品的最小值
[https://leetcode-cn.com/problems/minimized-maximum-of-products-distributed-to-any-store](https://leetcode-cn.com/problems/minimized-maximum-of-products-distributed-to-any-store) 
## 原题
给你一个整数 `n` ，表示有 `n` 间零售商店。总共有 `m` 种产品，每种产品的数目用一个下标从 **0** 开始的整数数组 `quantities` 表示，其中 `quantities[i]` 表示第 `i` 种商品的数目。

你需要将 **所有商品** 分配到零售商店，并遵守这些规则：
- 一间商店 **至多** 只能有 **一种商品** ，但一间商店拥有的商品数目可以为 **任意** 件。
- 分配后，每间商店都会被分配一定数目的商品（可能为 `0` 件）。用 `x` 表示所有商店中分配商品数目的最大值，你希望 `x` 越小越好。也就是说，你想 **最小化** 分配给任意商店商品数目的 **最大值** 。
请你返回最小的可能的 `x` 。

 

 **示例 1：** 

```

输入：n = 6, quantities = [11,6]
输出：3
解释： 一种最优方案为：
- 11 件种类为 0 的商品被分配到前 4 间商店，分配数目分别为：2，3，3，3 。
- 6 件种类为 1 的商品被分配到另外 2 间商店，分配数目分别为：3，3 。
分配给所有商店的最大商品数目为 max(2, 3, 3, 3, 3, 3) = 3 。

```
 **示例 2：** 

```

输入：n = 7, quantities = [15,10,10]
输出：5
解释：一种最优方案为：
- 15 件种类为 0 的商品被分配到前 3 间商店，分配数目为：5，5，5 。
- 10 件种类为 1 的商品被分配到接下来 2 间商店，数目为：5，5 。
- 10 件种类为 2 的商品被分配到最后 2 间商店，数目为：5，5 。
分配给所有商店的最大商品数目为 max(5, 5, 5, 5, 5, 5, 5) = 5 。

```
 **示例 3：** 

```

输入：n = 1, quantities = [100000]
输出：100000
解释：唯一一种最优方案为：
- 所有 100000 件商品 0 都分配到唯一的商店中。
分配给所有商店的最大商品数目为 max(100000) = 100000 。

```
 

 **提示：** 
-  `m == quantities.length` 
-  `1 <= m <= n <= 10^5` 
-  `1 <= quantities[i] <= 10^5` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 2065.最大化一张图中的路径价值
[https://leetcode-cn.com/problems/maximum-path-quality-of-a-graph](https://leetcode-cn.com/problems/maximum-path-quality-of-a-graph) 
## 原题
给你一张 **无向** 图，图中有 `n` 个节点，节点编号从 `0` 到 `n - 1` （ **都包括** ）。同时给你一个下标从 **0** 开始的整数数组 `values` ，其中 `values[i]` 是第 `i` 个节点的 **价值** 。同时给你一个下标从 **0** 开始的二维整数数组 `edges` ，其中 `edges[j] = [u<sub>j</sub>, v<sub>j</sub>, time<sub>j</sub>]` 表示节点 `u<sub>j</sub>` 和 `v<sub>j</sub>` 之间有一条需要 `time<sub>j</sub>` 秒才能通过的无向边。最后，给你一个整数 `maxTime` 。

 **合法路径** 指的是图中任意一条从节点 `0` 开始，最终回到节点 `0` ，且花费的总时间 **不超过** `maxTime` 秒的一条路径。你可以访问一个节点任意次。一条合法路径的 <b>价值</b> 定义为路径中 **不同节点** 的价值 **之和** （每个节点的价值 **至多** 算入价值总和中一次）。

请你返回一条合法路径的 **最大** 价值。

 **注意：** 每个节点 **至多** 有 **四条** 边与之相连。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/19/ex1drawio.png" style="width: 269px; height: 170px;" />

```

输入：values = [0,32,10,43], edges = [[0,1,10],[1,2,15],[0,3,10]], maxTime = 49
输出：75
解释：
一条可能的路径为：0 -> 1 -> 0 -> 3 -> 0 。总花费时间为 10 + 10 + 10 + 10 = 40 <= 49 。
访问过的节点为 0 ，1 和 3 ，最大路径价值为 0 + 32 + 43 = 75 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/19/ex2drawio.png" style="width: 269px; height: 170px;" />

```

输入：values = [5,10,15,20], edges = [[0,1,10],[1,2,10],[0,3,10]], maxTime = 30
输出：25
解释：
一条可能的路径为：0 -> 3 -> 0 。总花费时间为 10 + 10 = 20 <= 30 。
访问过的节点为 0 和 3 ，最大路径价值为 5 + 20 = 25 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/19/ex31drawio.png" style="width: 236px; height: 170px;" />

```

输入：values = [1,2,3,4], edges = [[0,1,10],[1,2,11],[2,3,12],[1,3,13]], maxTime = 50
输出：7
解释：
一条可能的路径为：0 -> 1 -> 3 -> 1 -> 0 。总花费时间为 10 + 13 + 13 + 10 = 46 <= 50 。
访问过的节点为 0 ，1 和 3 ，最大路径价值为 1 + 2 + 4 = 7 。
```
 **示例 4：** 

 **<img alt="" src="https://assets.leetcode.com/uploads/2021/10/21/ex4drawio.png" style="width: 270px; height: 71px;" />** 

```

输入：values = [0,1,2], edges = [[1,2,10]], maxTime = 10
输出：0
解释：
唯一一条路径为 0 。总花费时间为 0 。
唯一访问过的节点为 0 ，最大路径价值为 0 。

```
 

 **提示：** 
-  `n == values.length` 
-  `1 <= n <= 1000` 
-  `0 <= values[i] <= 10^8` 
-  `0 <= edges.length <= 2000` 
-  `edges[j].length == 3` 
-  `0 <= u<sub>j </sub>< v<sub>j</sub> <= n - 1` 
-  `10 <= time<sub>j</sub>, maxTime <= 100` 
-  `[u<sub>j</sub>, v<sub>j</sub>]` 所有节点对 **互不相同** 。
- 每个节点 **至多有四条** 边。
- 图可能不连通。
 
**标签**
`图` `数组` `回溯` 


## 
```python

```
>
# 2066.账户余额
[https://leetcode-cn.com/problems/account-balance](https://leetcode-cn.com/problems/account-balance) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 2068.检查两个字符串是否几乎相等
[https://leetcode-cn.com/problems/check-whether-two-strings-are-almost-equivalent](https://leetcode-cn.com/problems/check-whether-two-strings-are-almost-equivalent) 
## 原题
如果两个字符串 `word1` 和 `word2` 中从 `'a'` 到 `'z'` 每一个字母出现频率之差都 **不超过** `3` ，那么我们称这两个字符串 `word1` 和 `word2` **几乎相等** 。

给你两个长度都为 `n` 的字符串 `word1` 和 `word2` ，如果 `word1` 和 `word2` **几乎相等** ，请你返回 `true` ，否则返回 `false` 。

一个字母 `x` 的出现 **频率** 指的是它在字符串中出现的次数。

 

 **示例 1：** 

```
输入：word1 = "aaaa", word2 = "bccb"
输出：false
解释：字符串 "aaaa" 中有 4 个 'a' ，但是 "bccb" 中有 0 个 'a' 。
两者之差为 4 ，大于上限 3 。

```
 **示例 2：** 

```
输入：word1 = "abcdeef", word2 = "abaaacc"
输出：true
解释：word1 和 word2 中每个字母出现频率之差至多为 3 ：
- 'a' 在 word1 中出现了 1 次，在 word2 中出现了 4 次，差为 3 。
- 'b' 在 word1 中出现了 1 次，在 word2 中出现了 1 次，差为 0 。
- 'c' 在 word1 中出现了 1 次，在 word2 中出现了 2 次，差为 1 。
- 'd' 在 word1 中出现了 1 次，在 word2 中出现了 0 次，差为 1 。
- 'e' 在 word1 中出现了 2 次，在 word2 中出现了 0 次，差为 2 。
- 'f' 在 word1 中出现了 1 次，在 word2 中出现了 0 次，差为 1 。

```
 **示例 3：** 

```
输入：word1 = "cccddabba", word2 = "babababab"
输出：true
解释：word1 和 word2 中每个字母出现频率之差至多为 3 ：
- 'a' 在 word1 中出现了 2 次，在 word2 中出现了 4 次，差为 2 。
- 'b' 在 word1 中出现了 2 次，在 word2 中出现了 5 次，差为 3 。
- 'c' 在 word1 中出现了 3 次，在 word2 中出现了 0 次，差为 3 。
- 'd' 在 word1 中出现了 2 次，在 word2 中出现了 0 次，差为 2 。

```
 

 **提示：** 
-  `n == word1.length == word2.length` 
-  `1 <= n <= 100` 
-  `word1` 和 `word2` 都只包含小写英文字母。
 
**标签**
`哈希表` `字符串` `计数` 


## 
```python

```
>
# 2069.模拟行走机器人 II
[https://leetcode-cn.com/problems/walking-robot-simulation-ii](https://leetcode-cn.com/problems/walking-robot-simulation-ii) 
## 原题
给你一个在 XY 平面上的 `width x height` 的网格图， **左下角** 的格子为 `(0, 0)` ， **右上角** 的格子为 `(width - 1, height - 1)` 。网格图中相邻格子为四个基本方向之一（ `"North"` ， `"East"` ， `"South"` 和 `"West"` ）。一个机器人 **初始** 在格子 `(0, 0)` ，方向为 `"East"` 。

机器人可以根据指令移动指定的 **步数** 。每一步，它可以执行以下操作。
- 沿着当前方向尝试 **往前一步** 。
- 如果机器人下一步将到达的格子 **超出了边界** ，机器人会 **逆时针** 转 90 度，然后再尝试往前一步。
如果机器人完成了指令要求的移动步数，它将停止移动并等待下一个指令。

请你实现 `Robot` 类：
-  `Robot(int width, int height)` 初始化一个 `width x height` 的网格图，机器人初始在 `(0, 0)` ，方向朝 `"East"` 。
-  `void move(int num)` 给机器人下达前进 `num` 步的指令。
-  `int[] getPos()` 返回机器人当前所处的格子位置，用一个长度为 2 的数组 `[x, y]` 表示。
-  `String getDir()` 返回当前机器人的朝向，为 `"North"` ， `"East"` ， `"South"` 或者 `"West"` 。
 

 **示例 1：** 

<img alt="example-1" src="https://assets.leetcode.com/uploads/2021/10/09/example-1.png" style="width: 498px; height: 268px;">

```
输入：
["Robot", "move", "move", "getPos", "getDir", "move", "move", "move", "getPos", "getDir"]
[[6, 3], [2], [2], [], [], [2], [1], [4], [], []]
输出：
[null, null, null, [4, 0], "East", null, null, null, [1, 2], "West"]

解释：
Robot robot = new Robot(6, 3); // 初始化网格图，机器人在 (0, 0) ，朝东。
robot.move(2);  // 机器人朝东移动 2 步，到达 (2, 0) ，并朝东。
robot.move(2);  // 机器人朝东移动 2 步，到达 (4, 0) ，并朝东。
robot.getPos(); // 返回 [4, 0]
robot.getDir(); // 返回 "East"
robot.move(2);  // 朝东移动 1 步到达 (5, 0) ，并朝东。
                // 下一步继续往东移动将出界，所以逆时针转变方向朝北。
                // 然后，往北移动 1 步到达 (5, 1) ，并朝北。
robot.move(1);  // 朝北移动 1 步到达 (5, 2) ，并朝 北 （不是朝西）。
robot.move(4);  // 下一步继续往北移动将出界，所以逆时针转变方向朝西。
                // 然后，移动 4 步到 (1, 2) ，并朝西。
robot.getPos(); // 返回 [1, 2]
robot.getDir(); // 返回 "West"
```
 

 **提示：** 
-  `2 <= width, height <= 100` 
-  `1 <= num <= 10^5` 
-  `move` ， `getPos` 和 `getDir` **总共** 调用次数不超过 `10^4` 次。
 
**标签**
`设计` `模拟` 


## 
```python

```
>
# 2070.每一个查询的最大美丽值
[https://leetcode-cn.com/problems/most-beautiful-item-for-each-query](https://leetcode-cn.com/problems/most-beautiful-item-for-each-query) 
## 原题
给你一个二维整数数组 `items` ，其中 `items[i] = [price<sub>i</sub>, beauty<sub>i</sub>]` 分别表示每一个物品的 **价格** 和 **美丽值** 。

同时给你一个下标从 **0** 开始的整数数组 `queries` 。对于每个查询 `queries[j]` ，你想求出价格小于等于 `queries[j]` 的物品中， **最大的美丽值** 是多少。如果不存在符合条件的物品，那么查询的结果为 `0` 。

请你返回一个长度与 `queries` 相同的数组 `answer` ，其中 `answer[j]` 是第 `j` 个查询的答案。

 

 **示例 1：** 

```
输入：items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
输出：[2,4,5,5,6,6]
解释：
- queries[0]=1 ，[1,2] 是唯一价格 <= 1 的物品。所以这个查询的答案为 2 。
- queries[1]=2 ，符合条件的物品有 [1,2] 和 [2,4] 。
  它们中的最大美丽值为 4 。
- queries[2]=3 和 queries[3]=4 ，符合条件的物品都为 [1,2] ，[3,2] ，[2,4] 和 [3,5] 。
  它们中的最大美丽值为 5 。
- queries[4]=5 和 queries[5]=6 ，所有物品都符合条件。
  所以，答案为所有物品中的最大美丽值，为 6 。

```
 **示例 2：** 

```
输入：items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
输出：[4]
解释：
每个物品的价格均为 1 ，所以我们选择最大美丽值 4 。
注意，多个物品可能有相同的价格和美丽值。

```
 **示例 3：** 

```
输入：items = [[10,1000]], queries = [5]
输出：[0]
解释：
没有物品的价格小于等于 5 ，所以没有物品可以选择。
因此，查询的结果为 0 。

```
 

 **提示：** 
-  `1 <= items.length, queries.length <= 10^5` 
-  `items[i].length == 2` 
-  `1 <= price<sub>i</sub>, beauty<sub>i</sub>, queries[j] <= 10^9` 
 
**标签**
`数组` `二分查找` `排序` 


## 
```python

```
>
# 2071.你可以安排的最多任务数目
[https://leetcode-cn.com/problems/maximum-number-of-tasks-you-can-assign](https://leetcode-cn.com/problems/maximum-number-of-tasks-you-can-assign) 
## 原题
给你 `n` 个任务和 `m` 个工人。每个任务需要一定的力量值才能完成，需要的力量值保存在下标从 **0** 开始的整数数组 `tasks` 中，第 `i` 个任务需要 `tasks[i]` 的力量才能完成。每个工人的力量值保存在下标从 **0** 开始的整数数组 `workers` 中，第 `j` 个工人的力量值为 `workers[j]` 。每个工人只能完成 **一个** 任务，且力量值需要 **大于等于** 该任务的力量要求值（即 `workers[j] >= tasks[i]` ）。

除此以外，你还有 `pills` 个神奇药丸，可以给 **一个工人的力量值** 增加 `strength` 。你可以决定给哪些工人使用药丸，但每个工人 **最多** 只能使用 **一片** 药丸。

给你下标从 **0** 开始的整数数组 `tasks` 和 `workers` 以及两个整数 `pills` 和 `strength` ，请你返回 **最多** 有多少个任务可以被完成。

 

 **示例 1：** 

```
输入：tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
输出：3
解释：
我们可以按照如下方案安排药丸：
- 给 0 号工人药丸。
- 0 号工人完成任务 2（0 + 1 >= 1）
- 1 号工人完成任务 1（3 >= 2）
- 2 号工人完成任务 0（3 >= 3）

```
 **示例 2：** 

```
输入：tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
输出：1
解释：
我们可以按照如下方案安排药丸：
- 给 0 号工人药丸。
- 0 号工人完成任务 0（0 + 5 >= 5）

```
 **示例 3：** 

```
输入：tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
输出：2
解释：
我们可以按照如下方案安排药丸：
- 给 0 号和 1 号工人药丸。
- 0 号工人完成任务 0（0 + 10 >= 10）
- 1 号工人完成任务 1（10 + 10 >= 15）

```
 **示例 4：** 

```
输入：tasks = [5,9,8,5,9], workers = [1,6,4,2,6], pills = 1, strength = 5
输出：3
解释：
我们可以按照如下方案安排药丸：
- 给 2 号工人药丸。
- 1 号工人完成任务 0（6 >= 5）
- 2 号工人完成任务 2（4 + 5 >= 8）
- 4 号工人完成任务 3（6 >= 5）

```
 

 **提示：** 
-  `n == tasks.length` 
-  `m == workers.length` 
-  `1 <= n, m <= 5 * 10^4` 
-  `0 <= pills <= m` 
-  `0 <= tasks[i], workers[j], strength <= 10^9` 
 
**标签**
`贪心` `队列` `数组` `二分查找` `排序` `单调队列` 


## 
```python

```
>
# 2072.赢得比赛的大学
[https://leetcode-cn.com/problems/the-winner-university](https://leetcode-cn.com/problems/the-winner-university) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 2073.买票需要的时间
[https://leetcode-cn.com/problems/time-needed-to-buy-tickets](https://leetcode-cn.com/problems/time-needed-to-buy-tickets) 
## 原题
有 `n` 个人前来排队买票，其中第 `0` 人站在队伍 **最前方** ，第 `(n - 1)` 人站在队伍 **最后方** 。

给你一个下标从 **0** 开始的整数数组 `tickets` ，数组长度为 `n` ，其中第 `i` 人想要购买的票数为 `tickets[i]` 。

每个人买票都需要用掉 **恰好 1 秒** 。一个人 **一次只能买一张票** ，如果需要购买更多票，他必须走到 **队尾** 重新排队（ **瞬间** 发生，不计时间）。如果一个人没有剩下需要买的票，那他将会 **离开** 队伍。

返回位于位置 `k` （下标从 **0** 开始）的人完成买票需要的时间（以秒为单位）。

 

 **示例 1：** 

```
输入：tickets = [2,3,2], k = 2
输出：6
解释： 
- 第一轮，队伍中的每个人都买到一张票，队伍变为 [1, 2, 1] 。
- 第二轮，队伍中的每个都又都买到一张票，队伍变为 [0, 1, 0] 。
位置 2 的人成功买到 2 张票，用掉 3 + 3 = 6 秒。

```
 **示例 2：** 

```
输入：tickets = [5,1,1,1], k = 0
输出：8
解释：
- 第一轮，队伍中的每个人都买到一张票，队伍变为 [4, 0, 0, 0] 。
- 接下来的 4 轮，只有位置 0 的人在买票。
位置 0 的人成功买到 5 张票，用掉 4 + 1 + 1 + 1 + 1 = 8 秒。

```
 

 **提示：** 
-  `n == tickets.length` 
-  `1 <= n <= 100` 
-  `1 <= tickets[i] <= 100` 
-  `0 <= k < n` 
 
**标签**
`队列` `数组` `模拟` 


## 
```python

```
>
# 2074.反转偶数长度组的节点
[https://leetcode-cn.com/problems/reverse-nodes-in-even-length-groups](https://leetcode-cn.com/problems/reverse-nodes-in-even-length-groups) 
## 原题
给你一个链表的头节点 `head` 。

链表中的节点 **按顺序** 划分成若干 **非空** 组，这些非空组的长度构成一个自然数序列（ `1, 2, 3, 4, ...` ）。一个组的 **长度** 就是组中分配到的节点数目。换句话说：
- 节点 `1` 分配给第一组
- 节点 `2` 和 `3` 分配给第二组
- 节点 `4` 、 `5` 和 `6` 分配给第三组，以此类推
注意，最后一组的长度可能小于或者等于 `1 + 倒数第二组的长度` 。

 **反转** 每个 **偶数** 长度组中的节点，并返回修改后链表的头节点 `head` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/25/eg1.png" style="width: 699px; height: 124px;" />

```

输入：head = [5,2,6,3,9,1,7,3,8,4]
输出：[5,6,2,3,9,1,4,8,3,7]
解释：
- 第一组长度为 1 ，奇数，没有发生反转。
- 第二组长度为 2 ，偶数，节点反转。
- 第三组长度为 3 ，奇数，没有发生反转。
- 最后一组长度为 4 ，偶数，节点反转。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/25/eg2.png" style="width: 284px; height: 114px;" />

```

输入：head = [1,1,0,6]
输出：[1,0,1,6]
解释：
- 第一组长度为 1 ，没有发生反转。
- 第二组长度为 2 ，节点反转。
- 最后一组长度为 1 ，没有发生反转。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/28/eg3.png" style="width: 139px; height: 114px;" />

```

输入：head = [2,1]
输出：[2,1]
解释：
- 第一组长度为 1 ，没有发生反转。
- 最后一组长度为 1 ，没有发生反转。

```
 **示例 4：** 

```

输入：head = [8]
输出：[8]
解释：只有一个长度为 1 的组，没有发生反转。

```
 

 **提示：** 
- 链表中节点数目范围是 `[1, 10^5]` 
-  `0 <= Node.val <= 10^5` 
 
**标签**
`链表` 


## 
```python

```
>
# 2075.解码斜向换位密码
[https://leetcode-cn.com/problems/decode-the-slanted-ciphertext](https://leetcode-cn.com/problems/decode-the-slanted-ciphertext) 
## 原题
字符串 `originalText` 使用 **斜向换位密码** ，经由 **行数固定** 为 `rows` 的矩阵辅助，加密得到一个字符串 `encodedText` 。

 `originalText` 先按从左上到右下的方式放置到矩阵中。
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/07/exa11.png" style="width: 300px; height: 185px;" />
先填充蓝色单元格，接着是红色单元格，然后是黄色单元格，以此类推，直到到达 `originalText` 末尾。箭头指示顺序即为单元格填充顺序。所有空单元格用 `' '` 进行填充。矩阵的列数需满足：用 `originalText` 填充之后，最右侧列 **不为空** 。

接着按行将字符附加到矩阵中，构造 `encodedText` 。
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/07/exa12.png" style="width: 300px; height: 200px;" />
先把蓝色单元格中的字符附加到 `encodedText` 中，接着是红色单元格，最后是黄色单元格。箭头指示单元格访问顺序。

例如，如果 `originalText = "cipher"` 且 `rows = 3` ，那么我们可以按下述方法将其编码：
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/25/desc2.png" style="width: 281px; height: 211px;" />
蓝色箭头标识 `originalText` 是如何放入矩阵中的，红色箭头标识形成 `encodedText` 的顺序。在上述例子中， `encodedText = "ch   ie   pr"` 。

给你编码后的字符串 `encodedText` 和矩阵的行数 `rows` ，返回源字符串 `originalText` 。

 **注意：** `originalText` **不** 含任何尾随空格 `' '` 。生成的测试用例满足 **仅存在一个** 可能的 `originalText` 。

 

 **示例 1：** 

```

输入：encodedText = "ch   ie   pr", rows = 3
输出："cipher"
解释：此示例与问题描述中的例子相同。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/26/exam1.png" style="width: 250px; height: 168px;" />

```

输入：encodedText = "iveo    eed   l te   olc", rows = 4
输出："i love leetcode"
解释：上图标识用于编码 originalText 的矩阵。 
蓝色箭头展示如何从 encodedText 找到 originalText 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/26/eg2.png" style="width: 300px; height: 51px;" />

```

输入：encodedText = "coding", rows = 1
输出："coding"
解释：由于只有 1 行，所以 originalText 和 encodedText 是相同的。

```
 **示例 4：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/10/26/exam3.png" style="width: 150px; height: 101px;" />
```

输入：encodedText = " b  ac", rows = 2
输出：" abc"
解释：originalText 不能含尾随空格，但它可能会有一个或者多个前置空格。

```
 

 **提示：** 
-  `0 <= encodedText.length <= 10^6` 
-  `encodedText` 仅由小写英文字母和 `' '` 组成
-  `encodedText` 是对某个 **不含** 尾随空格的 `originalText` 的一个有效编码
-  `1 <= rows <= 1000` 
- 生成的测试用例满足 **仅存在一个** 可能的 `originalText` 
 
**标签**
`字符串` `模拟` 


## 
```python

```
>
# 2076.处理含限制条件的好友请求
[https://leetcode-cn.com/problems/process-restricted-friend-requests](https://leetcode-cn.com/problems/process-restricted-friend-requests) 
## 原题
给你一个整数 `n` ，表示网络上的用户数目。每个用户按从 `0` 到 `n - 1` 进行编号。

给你一个下标从 **0** 开始的二维整数数组 `restrictions` ，其中 `restrictions[i] = [x<sub>i</sub>, y<sub>i</sub>]` 意味着用户 `x<sub>i</sub>` 和用户 `y<sub>i</sub>` **不能** 成为 **朋友** ，不管是 **直接** 还是通过其他用户 **间接** 。

最初，用户里没有人是其他用户的朋友。给你一个下标从 **0** 开始的二维整数数组 `requests` 表示好友请求的列表，其中 `requests[j] = [u<sub>j</sub>, v<sub>j</sub>]` 是用户 `u<sub>j</sub>` 和用户 `v<sub>j</sub>` 之间的一条好友请求。

如果 `u<sub>j</sub>` 和 `v<sub>j</sub>` 可以成为 **朋友** ，那么好友请求将会 **成功** 。每个好友请求都会按列表中给出的顺序进行处理（即， `requests[j]` 会在 `requests[j + 1]` 前）。一旦请求成功，那么对所有未来的好友请求而言， `u<sub>j</sub>` 和 `v<sub>j</sub>` 将会 **成为直接朋友 。** 

返回一个 **布尔数组** `result` ，其中元素遵循此规则：如果第 `j` 个好友请求 **成功** ，那么 `result[j]` 就是 `true` ；否则，为 `false` 。

 **注意：** 如果 `u<sub>j</sub>` 和 `v<sub>j</sub>` 已经是直接朋友，那么他们之间的请求将仍然 **成功** 。

 

 **示例 1：** 

```

输入：n = 3, restrictions = [[0,1]], requests = [[0,2],[2,1]]
输出：[true,false]
解释：
请求 0 ：用户 0 和 用户 2 可以成为朋友，所以他们成为直接朋友。 
请求 1 ：用户 2 和 用户 1 不能成为朋友，因为这会使 用户 0 和 用户 1 成为间接朋友 (1--2--0) 。

```
 **示例 2：** 

```

输入：n = 3, restrictions = [[0,1]], requests = [[1,2],[0,2]]
输出：[true,false]
解释：
请求 0 ：用户 1 和 用户 2 可以成为朋友，所以他们成为直接朋友。 
请求 1 ：用户 0 和 用户 2 不能成为朋友，因为这会使 用户 0 和 用户 1 成为间接朋友 (0--2--1) 。

```
 **示例 3：** 

```

输入：n = 5, restrictions = [[0,1],[1,2],[2,3]], requests = [[0,4],[1,2],[3,1],[3,4]]
输出：[true,false,true,false]
解释：
请求 0 ：用户 0 和 用户 4 可以成为朋友，所以他们成为直接朋友。 
请求 1 ：用户 1 和 用户 2 不能成为朋友，因为他们之间存在限制。
请求 2 ：用户 3 和 用户 1 可以成为朋友，所以他们成为直接朋友。 
请求 3 ：用户 3 和 用户 4 不能成为朋友，因为这会使 用户 0 和 用户 1 成为间接朋友 (0--4--3--1) 。

```
 

 **提示：** 
-  `2 <= n <= 1000` 
-  `0 <= restrictions.length <= 1000` 
-  `restrictions[i].length == 2` 
-  `0 <= x<sub>i</sub>, y<sub>i</sub> <= n - 1` 
-  `x<sub>i</sub> != y<sub>i</sub>` 
-  `1 <= requests.length <= 1000` 
-  `requests[j].length == 2` 
-  `0 <= u<sub>j</sub>, v<sub>j</sub> <= n - 1` 
-  `u<sub>j</sub> != v<sub>j</sub>` 
 
**标签**
`并查集` `图` 


## 
```python

```
>
# 2078.两栋颜色不同且距离最远的房子
[https://leetcode-cn.com/problems/two-furthest-houses-with-different-colors](https://leetcode-cn.com/problems/two-furthest-houses-with-different-colors) 
## 原题
街上有 `n` 栋房子整齐地排成一列，每栋房子都粉刷上了漂亮的颜色。给你一个下标从 **0** 开始且长度为 `n` 的整数数组 `colors` ，其中 `colors[i]` 表示第 `i` 栋房子的颜色。

返回 **两栋** 颜色 **不同** 房子之间的 **最大** 距离。

第 `i` 栋房子和第 `j` 栋房子之间的距离是 `abs(i - j)` ，其中 `abs(x)` 是 `x` 的绝对值。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/31/eg1.png" style="width: 610px; height: 84px;" />

```

输入：colors = [1,1,1,6,1,1,1]
输出：3
解释：上图中，颜色 1 标识成蓝色，颜色 6 标识成红色。
两栋颜色不同且距离最远的房子是房子 0 和房子 3 。
房子 0 的颜色是颜色 1 ，房子 3 的颜色是颜色 6 。两栋房子之间的距离是 abs(0 - 3) = 3 。
注意，房子 3 和房子 6 也可以产生最佳答案。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/31/eg2.png" style="width: 426px; height: 84px;" />

```

输入：colors = [1,8,3,8,3]
输出：4
解释：上图中，颜色 1 标识成蓝色，颜色 8 标识成黄色，颜色 3 标识成绿色。
两栋颜色不同且距离最远的房子是房子 0 和房子 4 。
房子 0 的颜色是颜色 1 ，房子 4 的颜色是颜色 3 。两栋房子之间的距离是 abs(0 - 4) = 4 。

```
 **示例 3：** 

```

输入：colors = [0,1]
输出：1
解释：两栋颜色不同且距离最远的房子是房子 0 和房子 1 。
房子 0 的颜色是颜色 0 ，房子 1 的颜色是颜色 1 。两栋房子之间的距离是 abs(0 - 1) = 1 。

```
 

 **提示：** 
-  `n == colors.length` 
-  `2 <= n <= 100` 
-  `0 <= colors[i] <= 100` 
- 生成的测试数据满足 **至少** 存在 2 栋颜色不同的房子
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 2079.给植物浇水
[https://leetcode-cn.com/problems/watering-plants](https://leetcode-cn.com/problems/watering-plants) 
## 原题
你打算用一个水罐给花园里的 `n` 株植物浇水。植物排成一行，从左到右进行标记，编号从 `0` 到 `n - 1` 。其中，第 `i` 株植物的位置是 `x = i` 。 `x = -1` 处有一条河，你可以在那里重新灌满你的水罐。

每一株植物都需要浇特定量的水。你将会按下面描述的方式完成浇水：
- 按从左到右的顺序给植物浇水。
- 在给当前植物浇完水之后，如果你没有足够的水 **完全** 浇灌下一株植物，那么你就需要返回河边重新装满水罐。
- 你 **不能** 提前重新灌满水罐。
最初，你在河边（也就是， `x = -1` ），在 x 轴上每移动 **一个单位** 都需要 **一步** 。

给你一个下标从 **0** 开始的整数数组 `plants` ，数组由 `n` 个整数组成。其中， `plants[i]` 为第 `i` 株植物需要的水量。另有一个整数 `capacity` 表示水罐的容量，返回浇灌所有植物需要的 **步数** 。

 

 **示例 1：** 

```

输入：plants = [2,2,3,3], capacity = 5
输出：14
解释：从河边开始，此时水罐是装满的：
- 走到植物 0 (1 步) ，浇水。水罐中还有 3 单位的水。
- 走到植物 1 (1 步) ，浇水。水罐中还有 1 单位的水。
- 由于不能完全浇灌植物 2 ，回到河边取水 (2 步)。
- 走到植物 2 (3 步) ，浇水。水罐中还有 2 单位的水。
- 由于不能完全浇灌植物 3 ，回到河边取水 (3 步)。
- 走到植物 3 (4 步) ，浇水。
需要的步数是 = 1 + 1 + 2 + 3 + 3 + 4 = 14 。

```
 **示例 2：** 

```

输入：plants = [1,1,1,4,2,3], capacity = 4
输出：30
解释：从河边开始，此时水罐是装满的：
- 走到植物 0，1，2 (3 步) ，浇水。回到河边取水 (3 步)。
- 走到植物 3 (4 步) ，浇水。回到河边取水 (4 步)。
- 走到植物 4 (5 步) ，浇水。回到河边取水 (5 步)。
- 走到植物 5 (6 步) ，浇水。
需要的步数是 = 3 + 3 + 4 + 4 + 5 + 5 + 6 = 30 。
```
 **示例 3：** 

```

输入：plants = [7,7,7,7,7,7,7], capacity = 8
输出：49
解释：每次浇水都需要重新灌满水罐。
需要的步数是 = 1 + 1 + 2 + 2 + 3 + 3 + 4 + 4 + 5 + 5 + 6 + 6 + 7 = 49 。

```
 

 **提示：** 
-  `n == plants.length` 
-  `1 <= n <= 1000` 
-  `1 <= plants[i] <= 10^6` 
-  `max(plants[i]) <= capacity <= 10^9` 
 
**标签**
`数组` 


## 
```python

```
>
# 2080.区间内查询数字的频率
[https://leetcode-cn.com/problems/range-frequency-queries](https://leetcode-cn.com/problems/range-frequency-queries) 
## 原题
请你设计一个数据结构，它能求出给定子数组内一个给定值的 **频率** 。

子数组中一个值的 **频率** 指的是这个子数组中这个值的出现次数。

请你实现 `RangeFreqQuery` 类：
-  `RangeFreqQuery(int[] arr)` 用下标从 **0** 开始的整数数组 `arr` 构造一个类的实例。
-  `int query(int left, int right, int value)` 返回子数组 `arr[left...right]` 中 `value` 的 **频率** 。
一个 **子数组** 指的是数组中一段连续的元素。 `arr[left...right]` 指的是 `nums` 中包含下标 `left` 和 `right` **在内** 的中间一段连续元素。

 

 **示例 1：** 

```
输入：
["RangeFreqQuery", "query", "query"]
[[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]], [1, 2, 4], [0, 11, 33]]
输出：
[null, 1, 2]

解释：
RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56]);
rangeFreqQuery.query(1, 2, 4); // 返回 1 。4 在子数组 [33, 4] 中出现 1 次。
rangeFreqQuery.query(0, 11, 33); // 返回 2 。33 在整个子数组中出现 2 次。

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `1 <= arr[i], value <= 10^4` 
-  `0 <= left <= right < arr.length` 
- 调用 `query` 不超过 `10^5` 次。
 
**标签**
`设计` `线段树` `数组` `哈希表` `二分查找` 


## 
```python

```
>
# 2081.k 镜像数字的和
[https://leetcode-cn.com/problems/sum-of-k-mirror-numbers](https://leetcode-cn.com/problems/sum-of-k-mirror-numbers) 
## 原题
一个 **k 镜像数字** 指的是一个在十进制和 k 进制下从前往后读和从后往前读都一样的 **没有前导 0** 的 **正** 整数。
- 比方说， `9` 是一个 2 镜像数字。 `9` 在十进制下为 `9` ，二进制下为 `1001` ，两者从前往后读和从后往前读都一样。
- 相反地， `4` 不是一个 2 镜像数字。 `4` 在二进制下为 `100` ，从前往后和从后往前读不相同。
给你进制 `k` 和一个数字 `n` ，请你返回 k 镜像数字中 **最小** 的 `n` 个数 **之和** 。

 

<b>示例 1：</b>

```
输入：k = 2, n = 5
输出：25
解释：
最小的 5 个 2 镜像数字和它们的二进制表示如下：
  十进制       二进制
    1          1
    3          11
    5          101
    7          111
    9          1001
它们的和为 1 + 3 + 5 + 7 + 9 = 25 。

```
 **示例 2：** 

```
输入：k = 3, n = 7
输出：499
解释：
7 个最小的 3 镜像数字和它们的三进制表示如下：
  十进制       三进制
    1          1
    2          2
    4          11
    8          22
    121        11111
    151        12121
    212        21212
它们的和为 1 + 2 + 4 + 8 + 121 + 151 + 212 = 499 。

```
 **示例 3：** 

```
输入：k = 7, n = 17
输出：20379000
解释：17 个最小的 7 镜像数字分别为：
1, 2, 3, 4, 5, 6, 8, 121, 171, 242, 292, 16561, 65656, 2137312, 4602064, 6597956, 6958596

```
 

 **提示：** 
-  `2 <= k <= 9` 
-  `1 <= n <= 30` 
 
**标签**
`数学` `枚举` 


## 
```python

```
>
# 2082.富有客户的数量
[https://leetcode-cn.com/problems/the-number-of-rich-customers](https://leetcode-cn.com/problems/the-number-of-rich-customers) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 2083.求以相同字母开头和结尾的子串总数
[https://leetcode-cn.com/problems/substrings-that-begin-and-end-with-the-same-letter](https://leetcode-cn.com/problems/substrings-that-begin-and-end-with-the-same-letter) 
## 原题

 
**标签**
`哈希表` `数学` `字符串` `计数` `前缀和` 


## 
```python

```
>
# 2084.为订单类型为 0 的客户删除类型为 1 的订单
[https://leetcode-cn.com/problems/drop-type-1-orders-for-customers-with-type-0-orders](https://leetcode-cn.com/problems/drop-type-1-orders-for-customers-with-type-0-orders) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 2085.统计出现过一次的公共字符串
[https://leetcode-cn.com/problems/count-common-words-with-one-occurrence](https://leetcode-cn.com/problems/count-common-words-with-one-occurrence) 
## 原题
给你两个字符串数组 `words1` 和 `words2` ，请你返回在两个字符串数组中 **都恰好出现一次** 的字符串的数目。

 

 **示例 1：** 

```

输入：words1 = ["leetcode","is","amazing","as","is"], words2 = ["amazing","leetcode","is"]
输出：2
解释：
- "leetcode" 在两个数组中都恰好出现一次，计入答案。
- "amazing" 在两个数组中都恰好出现一次，计入答案。
- "is" 在两个数组中都出现过，但在 words1 中出现了 2 次，不计入答案。
- "as" 在 words1 中出现了一次，但是在 words2 中没有出现过，不计入答案。
所以，有 2 个字符串在两个数组中都恰好出现了一次。

```
 **示例 2：** 

```

输入：words1 = ["b","bb","bbb"], words2 = ["a","aa","aaa"]
输出：0
解释：没有字符串在两个数组中都恰好出现一次。

```
 **示例 3：** 

```

输入：words1 = ["a","ab"], words2 = ["a","a","a","ab"]
输出：1
解释：唯一在两个数组中都出现一次的字符串是 "ab" 。

```
 

 **提示：** 
-  `1 <= words1.length, words2.length <= 1000` 
-  `1 <= words1[i].length, words2[j].length <= 30` 
-  `words1[i]` 和 `words2[j]` 都只包含小写英文字母。
 
**标签**
`数组` `哈希表` `字符串` `计数` 


## 
```python

```
>
# 2086.从房屋收集雨水需要的最少水桶数
[https://leetcode-cn.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses](https://leetcode-cn.com/problems/minimum-number-of-buckets-required-to-collect-rainwater-from-houses) 
## 原题
给你一个下标从 **0** 开始的字符串 `street` 。 `street` 中每个字符要么是表示房屋的 `'H'` ，要么是表示空位的 `'.'` 。

你可以在 **空位** 放置水桶，从相邻的房屋收集雨水。位置在 `i - 1` **或者** `i + 1` 的水桶可以收集位置为 `i` 处房屋的雨水。一个水桶如果相邻两个位置都有房屋，那么它可以收集 **两个** 房屋的雨水。

在确保 **每个** 房屋旁边都 **至少** 有一个水桶的前提下，请你返回需要的 **最少** 水桶数。如果无解请返回 `-1` 。

 

 **示例 1：** 

```
输入：street = "H..H"
输出：2
解释：
我们可以在下标为 1 和 2 处放水桶。
"H..H" -> "HBBH"（'B' 表示放置水桶）。
下标为 0 处的房屋右边有水桶，下标为 3 处的房屋左边有水桶。
所以每个房屋旁边都至少有一个水桶收集雨水。

```
 **示例 2：** 

```
输入：street = ".H.H."
输出：1
解释：
我们可以在下标为 2 处放置一个水桶。
".H.H." -> ".HBH."（'B' 表示放置水桶）。
下标为 1 处的房屋右边有水桶，下标为 3 处的房屋左边有水桶。
所以每个房屋旁边都至少有一个水桶收集雨水。

```
 **示例 3：** 

```
输入：street = ".HHH."
输出：-1
解释：
没有空位可以放置水桶收集下标为 2 处的雨水。
所以没有办法收集所有房屋的雨水。

```
 **示例 4：** 

```
输入：street = "H"
输出：-1
解释：
没有空位放置水桶。
所以没有办法收集所有房屋的雨水。

```
 **示例 5：** 

```
输入：street = "."
输出：0
解释：
没有房屋需要收集雨水。
所以需要 0 个水桶。

```
 

 **提示：** 
-  `1 <= street.length <= 10^5` 
-  `street[i]` 要么是 `'H'` ，要么是 `'.'` 。
 
**标签**
`贪心` `字符串` `动态规划` 


## 
```python

```
>
# 2087.网格图中机器人回家的最小代价
[https://leetcode-cn.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid](https://leetcode-cn.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid) 
## 原题
给你一个 `m x n` 的网格图，其中 `(0, 0)` 是最左上角的格子， `(m - 1, n - 1)` 是最右下角的格子。给你一个整数数组 `startPos` ， `startPos = [start<sub>row</sub>, start<sub>col</sub>]` 表示 **初始** 有一个 **机器人** 在格子 `(start<sub>row</sub>, start<sub>col</sub>)` 处。同时给你一个整数数组 `homePos` ， `homePos = [home<sub>row</sub>, home<sub>col</sub>]` 表示机器人的 **家** 在格子 `(home<sub>row</sub>, home<sub>col</sub>)` 处。

机器人需要回家。每一步它可以往四个方向移动： **上** ， **下** ， **左** ， **右** ，同时机器人不能移出边界。每一步移动都有一定代价。再给你两个下标从 **0** 开始的额整数数组：长度为 `m` 的数组 `rowCosts` 和长度为 `n` 的数组 `colCosts` 。
- 如果机器人往 **上** 或者往 **下** 移动到第 `r` **行** 的格子，那么代价为 `rowCosts[r]` 。
- 如果机器人往 **左** 或者往 **右** 移动到第 `c` **列** 的格子，那么代价为 `colCosts[c]` 。
请你返回机器人回家需要的 **最小总代价** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/11/eg-1.png" style="width: 282px; height: 217px;">

```
输入：startPos = [1, 0], homePos = [2, 3], rowCosts = [5, 4, 3], colCosts = [8, 2, 6, 7]
输出：18
解释：一个最优路径为：
从 (1, 0) 开始
-> 往下走到 (2, 0) 。代价为 rowCosts[2] = 3 。
-> 往右走到 (2, 1) 。代价为 colCosts[1] = 2 。
-> 往右走到 (2, 2) 。代价为 colCosts[2] = 6 。
-> 往右走到 (2, 3) 。代价为 colCosts[3] = 7 。
总代价为 3 + 2 + 6 + 7 = 18
```
 **示例 2：** 

```
输入：startPos = [0, 0], homePos = [0, 0], rowCosts = [5], colCosts = [26]
输出：0
解释：机器人已经在家了，所以不需要移动。总代价为 0 。

```
 

 **提示：** 
-  `m == rowCosts.length` 
-  `n == colCosts.length` 
-  `1 <= m, n <= 10^5` 
-  `0 <= rowCosts[r], colCosts[c] <= 10^4` 
-  `startPos.length == 2` 
-  `homePos.length == 2` 
-  `0 <= start<sub>row</sub>, home<sub>row</sub> < m` 
-  `0 <= start<sub>col</sub>, home<sub>col</sub> < n` 
 
**标签**
`贪心` `数组` `矩阵` 


## 
```python

```
>
# 2088.统计农场中肥沃金字塔的数目
[https://leetcode-cn.com/problems/count-fertile-pyramids-in-a-land](https://leetcode-cn.com/problems/count-fertile-pyramids-in-a-land) 
## 原题
有一个 **矩形网格** 状的农场，划分为 `m` 行 `n` 列的单元格。每个格子要么是 **肥沃的** （用 `1` 表示），要么是 **贫瘠** 的（用 `0` 表示）。网格图以外的所有与格子都视为贫瘠的。

农场中的 **金字塔** 区域定义如下：
- 区域内格子数目 **大于** `1` 且所有格子都是 **肥沃的** 。
- 金字塔 **顶端** 是这个金字塔 **最上方** 的格子。金字塔的高度是它所覆盖的行数。令 `(r, c)` 为金字塔的顶端且高度为 `h` ，那么金字塔区域内包含的任一格子 `(i, j)` 需满足 `r <= i <= r + h - 1` **且** `c - (i - r) <= j <= c + (i - r)` 。
一个 **倒金字塔** 类似定义如下：
- 区域内格子数目 **大于** `1` 且所有格子都是 <b>肥沃的</b> 。
- 倒金字塔的 **顶端** 是这个倒金字塔 **最下方** 的格子。倒金字塔的高度是它所覆盖的行数。令 `(r, c)` 为金字塔的顶端且高度为 `h` ，那么金字塔区域内包含的任一格子 `(i, j)` 需满足 `r - h + 1 <= i <= r` **且** `c - (r - i) <= j <= c + (r - i)` 。
下图展示了部分符合定义和不符合定义的金字塔区域。黑色区域表示肥沃的格子。

<img src="https://assets.leetcode.com/uploads/2021/11/08/image.png" style="width: 700px; height: 156px;">

给你一个下标从 **0** 开始且大小为 `m x n` 的二进制矩阵 `grid` ，它表示农场，请你返回 `grid` 中金字塔和倒金字塔的 **总数目** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg11.png" style="width: 200px; height: 102px;"> <img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/exa12.png" style="width: 200px; height: 102px;"> <img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/exa13.png" style="width: 200px; height: 102px;">

```
输入：grid = [[0,1,1,0],[1,1,1,1]]
输出：2
解释：
2 个可能的金字塔区域分别如上图蓝色和红色区域所示。
这个网格图中没有倒金字塔区域。
所以金字塔区域总数为 2 + 0 = 2 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg21.png" style="width: 180px; height: 122px;"> <img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/exa22.png" style="width: 180px; height: 122px;"> <img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/exa23.png" style="width: 180px; height: 122px;">

```
输入：grid = [[1,1,1],[1,1,1]]
输出：2
解释：
金字塔区域如上图蓝色区域所示，倒金字塔如上图红色区域所示。
所以金字塔区域总数目为 1 + 1 = 2 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg3.png" style="width: 149px; height: 150px;">

```
输入：grid = [[1,0,1],[0,0,0],[1,0,1]]
输出：0
解释：
网格图中没有任何金字塔或倒金字塔区域。

```
 **示例 4：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg41.png" style="width: 180px; height: 144px;"> <img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg42.png" style="width: 180px; height: 144px;"> <img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg43.png" style="width: 180px; height: 144px;"> <img alt="" src="https://assets.leetcode.com/uploads/2021/10/23/eg44.png" style="width: 180px; height: 144px;">

```
输入：grid = [[1,1,1,1,0],[1,1,1,1,1],[1,1,1,1,1],[0,1,0,0,1]]
输出：13
解释：
有 7 个金字塔区域。上图第二和第三张图中展示了它们中的 3 个。
有 6 个倒金字塔区域。上图中最后一张图展示了它们中的 2 个。
所以金字塔区域总数目为 7 + 6 = 13.

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 1000` 
-  `1 <= m * n <= 10^5` 
-  `grid[i][j]` 要么是 `0` ，要么是 `1` 。
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 2089.找出数组排序后的目标下标
[https://leetcode-cn.com/problems/find-target-indices-after-sorting-array](https://leetcode-cn.com/problems/find-target-indices-after-sorting-array) 
## 原题
给你一个下标从 **0** 开始的整数数组 `nums` 以及一个目标元素 `target` 。

 **目标下标** 是一个满足 `nums[i] == target` 的下标 `i` 。

将 `nums` 按 **非递减** 顺序排序后，返回由 `nums` 中目标下标组成的列表。如果不存在目标下标，返回一个 **空** 列表。返回的列表必须按 **递增** 顺序排列。

 

 **示例 1：** 

```
输入：nums = [1,2,5,2,3], target = 2
输出：[1,2]
解释：排序后，nums 变为 [1,2,2,3,5] 。
满足 nums[i] == 2 的下标是 1 和 2 。

```
 **示例 2：** 

```
输入：nums = [1,2,5,2,3], target = 3
输出：[3]
解释：排序后，nums 变为 [1,2,2,3,5] 。
满足 nums[i] == 3 的下标是 3 。

```
 **示例 3：** 

```
输入：nums = [1,2,5,2,3], target = 5
输出：[4]
解释：排序后，nums 变为 [1,2,2,3,5] 。
满足 nums[i] == 5 的下标是 4 。

```
 **示例 4：** 

```
输入：nums = [1,2,5,2,3], target = 4
输出：[]
解释：nums 中不含值为 4 的元素。

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `1 <= nums[i], target <= 100` 
 
**标签**
`数组` `二分查找` `排序` 


## 
```python

```
>
# 2090.半径为 k 的子数组平均值
[https://leetcode-cn.com/problems/k-radius-subarray-averages](https://leetcode-cn.com/problems/k-radius-subarray-averages) 
## 原题
给你一个下标从 **0** 开始的数组 `nums` ，数组中有 `n` 个整数，另给你一个整数 `k` 。

 **半径为 k 的子数组平均值** 是指： `nums` 中一个以下标 `i` 为 **中心** 且 **半径** 为 `k` 的子数组中所有元素的平均值，即下标在 `i - k` 和 `i + k` 范围（ **含** `i - k` 和 `i + k` ）内所有元素的平均值。如果在下标 `i` 前或后不足 `k` 个元素，那么 **半径为 k 的子数组平均值** 是 `-1` 。

构建并返回一个长度为 `n` 的数组 `avgs` ，其中 `avgs[i]` 是以下标 `i` 为中心的子数组的 **半径为 k 的子数组平均值** 。

 `x` 个元素的 **平均值** 是 `x` 个元素相加之和除以 `x` ，此时使用截断式 **整数除法** ，即需要去掉结果的小数部分。
- 例如，四个元素 `2` 、 `3` 、 `1` 和 `5` 的平均值是 `(2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75` ，截断后得到 `2` 。
 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/07/eg1.png" style="width: 343px; height: 119px;" />

```

输入：nums = [7,4,3,9,1,8,5,2,6], k = 3
输出：[-1,-1,-1,5,4,4,-1,-1,-1]
解释：
- avg[0]、avg[1] 和 avg[2] 是 -1 ，因为在这几个下标前的元素数量都不足 k 个。
- 中心为下标 3 且半径为 3 的子数组的元素总和是：7 + 4 + 3 + 9 + 1 + 8 + 5 = 37 。
  使用截断式 整数除法，avg[3] = 37 / 7 = 5 。
- 中心为下标 4 的子数组，avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4 。
- 中心为下标 5 的子数组，avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4 。
- avg[6]、avg[7] 和 avg[8] 是 -1 ，因为在这几个下标后的元素数量都不足 k 个。

```
 **示例 2：** 

```

输入：nums = [100000], k = 0
输出：[100000]
解释：
- 中心为下标 0 且半径 0 的子数组的元素总和是：100000 。
  avg[0] = 100000 / 1 = 100000 。

```
 **示例 3：** 

```

输入：nums = [8], k = 100000
输出：[-1]
解释：
- avg[0] 是 -1 ，因为在下标 0 前后的元素数量均不足 k 。

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 10^5` 
-  `0 <= nums[i], k <= 10^5` 
 
**标签**
`数组` `滑动窗口` 


## 
```python

```
>
# 2091.从数组中移除最大值和最小值
[https://leetcode-cn.com/problems/removing-minimum-and-maximum-from-array](https://leetcode-cn.com/problems/removing-minimum-and-maximum-from-array) 
## 原题
给你一个下标从 **0** 开始的数组 `nums` ，数组由若干 **互不相同** 的整数组成。

 `nums` 中有一个值最小的元素和一个值最大的元素。分别称为 **最小值** 和 **最大值** 。你的目标是从数组中移除这两个元素。

一次 **删除** 操作定义为从数组的 **前面** 移除一个元素或从数组的 **后面** 移除一个元素。

返回将数组中最小值和最大值 **都** 移除需要的最小删除次数。

 

 **示例 1：** 

```

输入：nums = [2,10,7,5,4,1,8,6]
输出：5
解释：
数组中的最小元素是 nums[5] ，值为 1 。
数组中的最大元素是 nums[1] ，值为 10 。
将最大值和最小值都移除需要从数组前面移除 2 个元素，从数组后面移除 3 个元素。
结果是 2 + 3 = 5 ，这是所有可能情况中的最小删除次数。

```
 **示例 2：** 

```

输入：nums = [0,-4,19,1,8,-2,-3,5]
输出：3
解释：
数组中的最小元素是 nums[1] ，值为 -4 。
数组中的最大元素是 nums[2] ，值为 19 。
将最大值和最小值都移除需要从数组前面移除 3 个元素。
结果是 3 ，这是所有可能情况中的最小删除次数。 

```
 **示例 3：** 

```

输入：nums = [101]
输出：1
解释：
数组中只有这一个元素，那么它既是数组中的最小值又是数组中的最大值。
移除它只需要 1 次删除操作。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-10^5 <= nums[i] <= 10^5` 
-  `nums` 中的整数 **互不相同** 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 2092.找出知晓秘密的所有专家
[https://leetcode-cn.com/problems/find-all-people-with-secret](https://leetcode-cn.com/problems/find-all-people-with-secret) 
## 原题
给你一个整数 `n` ，表示有 `n` 个专家从 `0` 到 `n - 1` 编号。另外给你一个下标从 0 开始的二维整数数组 `meetings` ，其中 `meetings[i] = [x<sub>i</sub>, y<sub>i</sub>, time<sub>i</sub>]` 表示专家 `x<sub>i</sub>` 和专家 `y<sub>i</sub>` 在时间 `time<sub>i</sub>` 要开一场会。一个专家可以同时参加 **多场会议** 。最后，给你一个整数 `firstPerson` 。

专家 `0` 有一个 **秘密** ，最初，他在时间 `0` 将这个秘密分享给了专家 `firstPerson` 。接着，这个秘密会在每次有知晓这个秘密的专家参加会议时进行传播。更正式的表达是，每次会议，如果专家 `x<sub>i</sub>` 在时间 `time<sub>i</sub>` 时知晓这个秘密，那么他将会与专家 `y<sub>i</sub>` 分享这个秘密，反之亦然。

秘密共享是 **瞬时发生** 的。也就是说，在同一时间，一个专家不光可以接收到秘密，还能在其他会议上与其他专家分享。

在所有会议都结束之后，返回所有知晓这个秘密的专家列表。你可以按 **任何顺序** 返回答案。

 

 **示例 1：** 

```

输入：n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1
输出：[0,1,2,3,5]
解释：
时间 0 ，专家 0 将秘密与专家 1 共享。
时间 5 ，专家 1 将秘密与专家 2 共享。
时间 8 ，专家 2 将秘密与专家 3 共享。
时间 10 ，专家 1 将秘密与专家 5 共享。
因此，在所有会议结束后，专家 0、1、2、3 和 5 都将知晓这个秘密。

```
 **示例 2：** 

```

输入：n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3
输出：[0,1,3]
解释：
时间 0 ，专家 0 将秘密与专家 3 共享。
时间 2 ，专家 1 与专家 2 都不知晓这个秘密。
时间 3 ，专家 3 将秘密与专家 0 和专家 1 共享。
因此，在所有会议结束后，专家 0、1 和 3 都将知晓这个秘密。

```
 **示例 3：** 

```

输入：n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1
输出：[0,1,2,3,4]
解释：
时间 0 ，专家 0 将秘密与专家 1 共享。
时间 1 ，专家 1 将秘密与专家 2 共享，专家 2 将秘密与专家 3 共享。
注意，专家 2 可以在收到秘密的同一时间分享此秘密。
时间 2 ，专家 3 将秘密与专家 4 共享。
因此，在所有会议结束后，专家 0、1、2、3 和 4 都将知晓这个秘密。
```
 **示例 4：** 

```

输入：n = 6, meetings = [[0,2,1],[1,3,1],[4,5,1]], firstPerson = 1
输出：[0,1,2,3]
解释：
时间 0 ，专家 0 将秘密与专家 1 共享。
时间 1 ，专家 0 将秘密与专家 2 共享，专家 1 将秘密与专家 3 共享。
因此，在所有会议结束后，专家 0、1、2 和 3 都将知晓这个秘密。

```
 

 **提示：** 
-  `2 <= n <= 10^5` 
-  `1 <= meetings.length <= 10^5` 
-  `meetings[i].length == 3` 
-  `0 <= x<sub>i</sub>, y<sub>i </sub><= n - 1` 
-  `x<sub>i</sub> != y<sub>i</sub>` 
-  `1 <= time<sub>i</sub> <= 10^5` 
-  `1 <= firstPerson <= n - 1` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `图` `排序` 


## 
```python

```
>
# 2094.找出 3 位偶数
[https://leetcode-cn.com/problems/finding-3-digit-even-numbers](https://leetcode-cn.com/problems/finding-3-digit-even-numbers) 
## 原题
给你一个整数数组 `digits` ，其中每个元素是一个数字（ `0 - 9` ）。数组中可能存在重复元素。

你需要找出 **所有** 满足下述条件且 **互不相同** 的整数：
- 该整数由 `digits` 中的三个元素按 **任意** 顺序 **依次连接** 组成。
- 该整数不含 **前导零** 
- 该整数是一个 **偶数** 
例如，给定的 `digits` 是 `[1, 2, 3]` ，整数 `132` 和 `312` 满足上面列出的全部条件。

将找出的所有互不相同的整数按 **递增顺序** 排列，并以数组形式返回 *。* 

 

 **示例 1：** 

```

输入：digits = [2,1,3,0]
输出：[102,120,130,132,210,230,302,310,312,320]
解释：
所有满足题目条件的整数都在输出数组中列出。 
注意，答案数组中不含有 奇数 或带 前导零 的整数。
```
 **示例 2：** 

```

输入：digits = [2,2,8,8,2]
输出：[222,228,282,288,822,828,882]
解释：
同样的数字（0 - 9）在构造整数时可以重复多次，重复次数最多与其在 digits 中出现的次数一样。 
在这个例子中，数字 8 在构造 288、828 和 882 时都重复了两次。 

```
 **示例 3：** 

```

输入：digits = [3,7,5]
输出：[]
解释：
使用给定的 digits 无法构造偶数。

```
 **示例 4：** 

```

输入：digits = [0,2,0,0]
输出：[200]
解释：
唯一一个不含 前导零 且满足全部条件的整数是 200 。

```
 **示例 5：** 

```

输入：digits = [0,0,0]
输出：[]
解释：
构造的所有整数都会有 前导零 。因此，不存在满足题目条件的整数。

```
 

 **提示：** 
-  `3 <= digits.length <= 100` 
-  `0 <= digits[i] <= 9` 
 
**标签**
`数组` `哈希表` `枚举` `排序` 


## 
```python

```
>
# 2095.删除链表的中间节点
[https://leetcode-cn.com/problems/delete-the-middle-node-of-a-linked-list](https://leetcode-cn.com/problems/delete-the-middle-node-of-a-linked-list) 
## 原题
给你一个链表的头节点 `head` 。 **删除** 链表的 **中间节点** ，并返回修改后的链表的头节点 `head` 。

长度为 `n` 链表的中间节点是从头数起第 `⌊n / 2⌋` 个节点（下标从 **0** 开始），其中 `⌊x⌋` 表示小于或等于 `x` 的最大整数。
- 对于 `n` = `1` 、 `2` 、 `3` 、 `4` 和 `5` 的情况，中间节点的下标分别是 `0` 、 `1` 、 `1` 、 `2` 和 `2` 。
 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg1drawio.png" style="width: 500px; height: 77px;" />

```

输入：head = [1,3,4,7,1,2,6]
输出：[1,3,4,1,2,6]
解释：
上图表示给出的链表。节点的下标分别标注在每个节点的下方。
由于 n = 7 ，值为 7 的节点 3 是中间节点，用红色标注。
返回结果为移除节点后的新链表。 

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg2drawio.png" style="width: 250px; height: 43px;" />

```

输入：head = [1,2,3,4]
输出：[1,2,4]
解释：
上图表示给出的链表。
对于 n = 4 ，值为 3 的节点 2 是中间节点，用红色标注。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/16/eg3drawio.png" style="width: 150px; height: 58px;" />

```

输入：head = [2,1]
输出：[2]
解释：
上图表示给出的链表。
对于 n = 2 ，值为 1 的节点 1 是中间节点，用红色标注。
值为 2 的节点 0 是移除节点 1 后剩下的唯一一个节点。
```
 

 **提示：** 
- 链表中节点的数目在范围 `[1, 10^5]` 内
-  `1 <= Node.val <= 10^5` 
 
**标签**
`链表` `双指针` 


## 
```python

```
>
# 2096.从二叉树一个节点到另一个节点每一步的方向
[https://leetcode-cn.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another](https://leetcode-cn.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another) 
## 原题
给你一棵 **二叉树** 的根节点 `root` ，这棵二叉树总共有 `n` 个节点。每个节点的值为 `1` 到 `n` 中的一个整数，且互不相同。给你一个整数 `startValue` ，表示起点节点 `s` 的值，和另一个不同的整数 `destValue` ，表示终点节点 `t` 的值。

请找到从节点 `s` 到节点 `t` 的 **最短路径** ，并以字符串的形式返回每一步的方向。每一步用 **大写** 字母 `'L'` ， `'R'` 和 `'U'` 分别表示一种方向：
-  `'L'` 表示从一个节点前往它的 **左孩子** 节点。
-  `'R'` 表示从一个节点前往它的 **右孩子** 节点。
-  `'U'` 表示从一个节点前往它的 **父** 节点。
请你返回从 `s` 到 `t` **最短路径** 每一步的方向。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/15/eg1.png" style="width: 214px; height: 163px;">

```
输入：root = [5,1,2,3,null,6,4], startValue = 3, destValue = 6
输出："UURL"
解释：最短路径为：3 → 1 → 5 → 2 → 6 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/15/eg2.png" style="width: 74px; height: 102px;">

```
输入：root = [2,1], startValue = 2, destValue = 1
输出："L"
解释：最短路径为：2 → 1 。

```
 

 **提示：** 
- 树中节点数目为 `n` 。
-  `2 <= n <= 10^5` 
-  `1 <= Node.val <= n` 
- 树中所有节点的值 **互不相同** 。
-  `1 <= startValue, destValue <= n` 
-  `startValue != destValue` 
 
**标签**
`树` `深度优先搜索` `字符串` `二叉树` 


## 
```python

```
>
# 2097.合法重新排列数对
[https://leetcode-cn.com/problems/valid-arrangement-of-pairs](https://leetcode-cn.com/problems/valid-arrangement-of-pairs) 
## 原题
给你一个下标从 **0** 开始的二维整数数组 `pairs` ，其中 `pairs[i] = [start<sub>i</sub>, end<sub>i</sub>]` 。如果 `pairs` 的一个重新排列，满足对每一个下标 `i` （ `1 <= i < pairs.length` ）都有 `end<sub>i-1</sub> == start<sub>i</sub>` <sub> </sub>，那么我们就认为这个重新排列是 `pairs` 的一个 **合法重新排列** 。

请你返回 **任意一个** `pairs` 的合法重新排列。

<b>注意：</b>数据保证至少存在一个 `pairs` 的合法重新排列。

 

 **示例 1：** 

```

输入：pairs = [[5,1],[4,5],[11,9],[9,4]]
输出：[[11,9],[9,4],[4,5],[5,1]]
解释：
输出的是一个合法重新排列，因为每一个 endi-1 都等于 starti 。
end0 = 9 == 9 = start1 
end1 = 4 == 4 = start2
end2 = 5 == 5 = start3

```
 **示例 2：** 

```

输入：pairs = [[1,3],[3,2],[2,1]]
输出：[[1,3],[3,2],[2,1]]
解释：
输出的是一个合法重新排列，因为每一个 endi-1 都等于 starti 。
end0 = 3 == 3 = start1
end1 = 2 == 2 = start2
重新排列后的数组 [[2,1],[1,3],[3,2]] 和 [[3,2],[2,1],[1,3]] 都是合法的。

```
 **示例 3：** 

```

输入：pairs = [[1,2],[1,3],[2,1]]
输出：[[1,2],[2,1],[1,3]]
解释：
输出的是一个合法重新排列，因为每一个 endi-1 都等于 starti 。
end0 = 2 == 2 = start1
end1 = 1 == 1 = start2

```
 

 **提示：** 
-  `1 <= pairs.length <= 10^5` 
-  `pairs[i].length == 2` 
-  `0 <= start<sub>i</sub>, end<sub>i</sub> <= 10^9` 
-  `start<sub>i</sub> != end<sub>i</sub>` 
-  `pairs` 中不存在一模一样的数对。
- 至少 **存在** 一个合法的 `pairs` 重新排列。
 
**标签**
`深度优先搜索` `图` `欧拉回路` 


## 
```python

```
>
# 2099.找到和最大的长度为 K 的子序列
[https://leetcode-cn.com/problems/find-subsequence-of-length-k-with-the-largest-sum](https://leetcode-cn.com/problems/find-subsequence-of-length-k-with-the-largest-sum) 
## 原题
给你一个整数数组 `nums` 和一个整数 `k` 。你需要找到 `nums` 中长度为 `k` 的 **子序列** ，且这个子序列的 **和最大** 。

请你返回 **任意** 一个长度为 `k` 的整数子序列。

 **子序列** 定义为从一个数组里删除一些元素后，不改变剩下元素的顺序得到的数组。

 

 **示例 1：** 

```
输入：nums = [2,1,3,3], k = 2
输出：[3,3]
解释：
子序列有最大和：3 + 3 = 6 。
```
 **示例 2：** 

```
输入：nums = [-1,-2,3,4], k = 3
输出：[-1,3,4]
解释：
子序列有最大和：-1 + 3 + 4 = 6 。

```
 **示例 3：** 

```
输入：nums = [3,4,3,3], k = 2
输出：[3,4]
解释：
子序列有最大和：3 + 4 = 7 。
另一个可行的子序列为 [4, 3] 。

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `-10^5 <= nums[i] <= 10^5` 
-  `1 <= k <= nums.length` 
 
**标签**
`数组` `哈希表` `排序` `堆（优先队列）` 


## 
```python

```
>
# 2100.适合打劫银行的日子
[https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank](https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank) 
## 原题
你和一群强盗准备打劫银行。给你一个下标从 **0** 开始的整数数组 `security` ，其中 `security[i]` 是第 `i` 天执勤警卫的数量。日子从 `0` 开始编号。同时给你一个整数 `time` 。

如果第 `i` 天满足以下所有条件，我们称它为一个适合打劫银行的日子：
- 第 `i` 天前和后都分别至少有 `time` 天。
- 第 `i` 天前连续 `time` 天警卫数目都是非递增的。
- 第 `i` 天后连续 `time` 天警卫数目都是非递减的。
更正式的，第 `i` 天是一个合适打劫银行的日子当且仅当： `security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time]` .

请你返回一个数组，包含 **所有** 适合打劫银行的日子（下标从 **0** 开始）。返回的日子可以 **任意** 顺序排列。

 

 **示例 1：** 

```

输入：security = [5,3,3,3,5,6,2], time = 2
输出：[2,3]
解释：
第 2 天，我们有 security[0] >= security[1] >= security[2] <= security[3] <= security[4] 。
第 3 天，我们有 security[1] >= security[2] >= security[3] <= security[4] <= security[5] 。
没有其他日子符合这个条件，所以日子 2 和 3 是适合打劫银行的日子。

```
 **示例 2：** 

```

输入：security = [1,1,1,1,1], time = 0
输出：[0,1,2,3,4]
解释：
因为 time 等于 0 ，所以每一天都是适合打劫银行的日子，所以返回每一天。

```
 **示例 3：** 

```

输入：security = [1,2,3,4,5,6], time = 2
输出：[]
解释：
没有任何一天的前 2 天警卫数目是非递增的。
所以没有适合打劫银行的日子，返回空数组。

```
 **示例 4：** 

```

输入：security = [1], time = 5
输出：[]
解释：
没有日子前面和后面有 5 天时间。
所以没有适合打劫银行的日子，返回空数组。
```
 

 **提示：** 
-  `1 <= security.length <= 10^5` 
-  `0 <= security[i], time <= 10^5` 
 
**标签**
`数组` `动态规划` `前缀和` 


## 
```python

```
>
