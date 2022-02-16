# 2101.引爆最多的炸弹
[https://leetcode-cn.com/problems/detonate-the-maximum-bombs](https://leetcode-cn.com/problems/detonate-the-maximum-bombs) 
## 原题
给你一个炸弹列表。一个炸弹的 **爆炸范围** 定义为以炸弹为圆心的一个圆。

炸弹用一个下标从 **0** 开始的二维整数数组 `bombs` 表示，其中 `bombs[i] = [x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub>]` 。 `x<sub>i</sub>` 和 `y<sub>i</sub>` 表示第 `i` 个炸弹的 X 和 Y 坐标， `r<sub>i</sub>` 表示爆炸范围的 **半径** 。

你需要选择引爆 **一个** 炸弹。当这个炸弹被引爆时， **所有** 在它爆炸范围内的炸弹都会被引爆，这些炸弹会进一步将它们爆炸范围内的其他炸弹引爆。

给你数组 `bombs` ，请你返回在引爆 **一个** 炸弹的前提下， **最多** 能引爆的炸弹数目。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/06/desmos-eg-3.png" style="width: 300px; height: 300px;">

```
输入：bombs = [[2,1,3],[6,1,4]]
输出：2
解释：
上图展示了 2 个炸弹的位置和爆炸范围。
如果我们引爆左边的炸弹，右边的炸弹不会被影响。
但如果我们引爆右边的炸弹，两个炸弹都会爆炸。
所以最多能引爆的炸弹数目是 max(1, 2) = 2 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/06/desmos-eg-2.png" style="width: 300px; height: 300px;">

```
输入：bombs = [[1,1,5],[10,10,5]]
输出：1
解释：
引爆任意一个炸弹都不会引爆另一个炸弹。所以最多能引爆的炸弹数目为 1 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/07/desmos-eg1.png" style="width: 300px; height: 300px;">

```
输入：bombs = [[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
输出：5
解释：
最佳引爆炸弹为炸弹 0 ，因为：
- 炸弹 0 引爆炸弹 1 和 2 。红色圆表示炸弹 0 的爆炸范围。
- 炸弹 2 引爆炸弹 3 。蓝色圆表示炸弹 2 的爆炸范围。
- 炸弹 3 引爆炸弹 4 。绿色圆表示炸弹 3 的爆炸范围。
所以总共有 5 个炸弹被引爆。

```
 

 **提示：** 
-  `1 <= bombs.length <= 100` 
-  `bombs[i].length == 3` 
-  `1 <= x<sub>i</sub>, y<sub>i</sub>, r<sub>i</sub> <= 10^5` 
 
**标签**
`深度优先搜索` `广度优先搜索` `图` `几何` `数组` `数学` 


## 
```python

```
>
# 2102.序列顺序查询
[https://leetcode-cn.com/problems/sequentially-ordinal-rank-tracker](https://leetcode-cn.com/problems/sequentially-ordinal-rank-tracker) 
## 原题
一个观光景点由它的名字 `name` 和景点评分 `score` 组成，其中 `name` 是所有观光景点中 **唯一** 的字符串， `score` 是一个整数。景点按照最好到最坏排序。景点评分 **越高** ，这个景点越好。如果有两个景点的评分一样，那么 **字典序较小** 的景点更好。

你需要搭建一个系统，查询景点的排名。初始时系统里没有任何景点。这个系统支持：
-  **添加** 景点，每次添加 **一个** 景点。
-  **查询** 已经添加景点中第 `i` **好** 的景点，其中 `i` 是系统目前位置查询的次数（包括当前这一次）。
	
- 比方说，如果系统正在进行第 `4` 次查询，那么需要返回所有已经添加景点中第 `4` 好的。
	
	
注意，测试数据保证 **任意查询时刻** ，查询次数都 **不超过** 系统中景点的数目。

请你实现 `SORTracker` 类：
-  `SORTracker()` 初始化系统。
-  `void add(string name, int score)` 向系统中添加一个名为 `name` 评分为 `score` 的景点。
-  `string get()` 查询第 `i` 好的景点，其中 `i` 是目前系统查询的次数（包括当前这次查询）。
 

 **示例：** 

```

输入：
["SORTracker", "add", "add", "get", "add", "get", "add", "get", "add", "get", "add", "get", "get"]
[[], ["bradford", 2], ["branford", 3], [], ["alps", 2], [], ["orland", 2], [], ["orlando", 3], [], ["alpine", 2], [], []]
输出：
[null, null, null, "branford", null, "alps", null, "bradford", null, "bradford", null, "bradford", "orland"]

解释：
SORTracker tracker = new SORTracker(); // 初始化系统
tracker.add("bradford", 2); // 添加 name="bradford" 且 score=2 的景点。
tracker.add("branford", 3); // 添加 name="branford" 且 score=3 的景点。
tracker.get();              // 从好带坏的景点为：branford ，bradford 。
                            // 注意到 branford 比 bradford 好，因为它的 评分更高 (3 > 2) 。
                            // 这是第 1 次调用 get() ，所以返回最好的景点："branford" 。
tracker.add("alps", 2);     // 添加 name="alps" 且 score=2 的景点。
tracker.get();              // 从好到坏的景点为：branford, alps, bradford 。
                            // 注意 alps 比 bradford 好，虽然它们评分相同，都为 2 。
                            // 这是因为 "alps" 字典序 比 "bradford" 小。
                            // 返回第 2 好的地点 "alps" ，因为当前为第 2 次调用 get() 。
tracker.add("orland", 2);   // 添加 name="orland" 且 score=2 的景点。
tracker.get();              // 从好到坏的景点为：branford, alps, bradford, orland 。
                            // 返回 "bradford" ，因为当前为第 3 次调用 get() 。
tracker.add("orlando", 3);  // 添加 name="orlando" 且 score=3 的景点。
tracker.get();              // 从好到坏的景点为：branford, orlando, alps, bradford, orland 。
                            // 返回 "bradford".
tracker.add("alpine", 2);   // 添加 name="alpine" 且 score=2 的景点。
tracker.get();              // 从好到坏的景点为：branford, orlando, alpine, alps, bradford, orland 。
                            // 返回 "bradford" 。
tracker.get();              // 从好到坏的景点为：branford, orlando, alpine, alps, bradford, orland 。
                            // 返回 "orland" 。

```
 

 **提示：** 
-  `name` 只包含小写英文字母，且每个景点名字互不相同。
-  `1 <= name.length <= 10` 
-  `1 <= score <= 10^5` 
- 任意时刻，调用 `get` 的次数都不超过调用 `add` 的次数。
-  **总共** 调用 `add` 和 `get` 不超过 `4 * 10^4` 
 
**标签**
`设计` `数据流` `有序集合` `堆（优先队列）` 


## 
```python

```
>
# 2103.环和杆
[https://leetcode-cn.com/problems/rings-and-rods](https://leetcode-cn.com/problems/rings-and-rods) 
## 原题
总计有 `n` 个环，环的颜色可以是红、绿、蓝中的一种。这些环分布穿在 10 根编号为 `0` 到 `9` 的杆上。

给你一个长度为 `2n` 的字符串 `rings` ，表示这 `n` 个环在杆上的分布。 `rings` 中每两个字符形成一个 **颜色位置对** ，用于描述每个环：
- 第 `i` 对中的 **第一个** 字符表示第 `i` 个环的 **颜色** （ `'R'` 、 `'G'` 、 `'B'` ）。
- 第 `i` 对中的 **第二个** 字符表示第 `i` 个环的 **位置** ，也就是位于哪根杆上（ `'0'` 到 `'9'` ）。
例如， `"R3G2B1"` 表示：共有 `n == 3` 个环，红色的环在编号为 3 的杆上，绿色的环在编号为 2 的杆上，蓝色的环在编号为 1 的杆上。

找出所有集齐 **全部三种颜色** 环的杆，并返回这种杆的数量。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/23/ex1final.png" style="width: 258px; height: 130px;">
```
输入：rings = "B0B6G0R6R0R6G9"
输出：1
解释：
- 编号 0 的杆上有 3 个环，集齐全部颜色：红、绿、蓝。
- 编号 6 的杆上有 3 个环，但只有红、蓝两种颜色。
- 编号 9 的杆上只有 1 个绿色环。
因此，集齐全部三种颜色环的杆的数目为 1 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/23/ex2final.png" style="width: 266px; height: 130px;">
```
输入：rings = "B0R0G0R9R0B0G0"
输出：1
解释：
- 编号 0 的杆上有 6 个环，集齐全部颜色：红、绿、蓝。
- 编号 9 的杆上只有 1 个红色环。
因此，集齐全部三种颜色环的杆的数目为 1 。

```
 **示例 3：** 

```
输入：rings = "G4"
输出：0
解释：
只给了一个环，因此，不存在集齐全部三种颜色环的杆。

```
 

 **提示：** 
-  `rings.length == 2 * n` 
-  `1 <= n <= 100` 
- 如 `i` 是 **偶数** ，则 `rings[i]` 的值可以取 `'R'` 、 `'G'` 或 `'B'` （下标从 **0** 开始计数）
- 如 `i` 是 **奇数** ，则 `rings[i]` 的值可以取 `'0'` 到 `'9'` 中的一个数字（下标从 **0** 开始计数）
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 2104.子数组范围和
[https://leetcode-cn.com/problems/sum-of-subarray-ranges](https://leetcode-cn.com/problems/sum-of-subarray-ranges) 
## 原题
给你一个整数数组 `nums` 。 `nums` 中，子数组的 **范围** 是子数组中最大元素和最小元素的差值。

返回 `nums` 中 **所有** 子数组范围的 **和** *。* 

子数组是数组中一个连续 **非空** 的元素序列。

 

 **示例 1：** 

```

输入：nums = [1,2,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0 
[2]，范围 = 2 - 2 = 0
[3]，范围 = 3 - 3 = 0
[1,2]，范围 = 2 - 1 = 1
[2,3]，范围 = 3 - 2 = 1
[1,2,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 1 + 1 + 2 = 4
```
 **示例 2：** 

```

输入：nums = [1,3,3]
输出：4
解释：nums 的 6 个子数组如下所示：
[1]，范围 = 最大 - 最小 = 1 - 1 = 0
[3]，范围 = 3 - 3 = 0
[3]，范围 = 3 - 3 = 0
[1,3]，范围 = 3 - 1 = 2
[3,3]，范围 = 3 - 3 = 0
[1,3,3]，范围 = 3 - 1 = 2
所有范围的和是 0 + 0 + 0 + 2 + 0 + 2 = 4

```
 **示例 3：** 

```

输入：nums = [4,-2,-3,4,1]
输出：59
解释：nums 中所有子数组范围的和是 59

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `-10^9 <= nums[i] <= 10^9` 
 

 **进阶：** 你可以设计一种时间复杂度为 `O(n)` 的解决方案吗？

 
**标签**
`栈` `数组` `单调栈` 


## 
```python

```
>
# 2105.给植物浇水 II
[https://leetcode-cn.com/problems/watering-plants-ii](https://leetcode-cn.com/problems/watering-plants-ii) 
## 原题
Alice 和 Bob 打算给花园里的 `n` 株植物浇水。植物排成一行，从左到右进行标记，编号从 `0` 到 `n - 1` 。其中，第 `i` 株植物的位置是 `x = i` 。

每一株植物都需要浇特定量的水。Alice 和 Bob 每人有一个水罐， **最初是满的** 。他们按下面描述的方式完成浇水：
-  Alice 按 **从左到右** 的顺序给植物浇水，从植物 `0` 开始。Bob 按 **从右到左** 的顺序给植物浇水，从植物 `n - 1` 开始。他们 **同时** 给植物浇水。
- 如果没有足够的水 **完全** 浇灌下一株植物，他 / 她会立即重新灌满浇水罐。
- 不管植物需要多少水，浇水所耗费的时间都是一样的。
-  **不能** 提前重新灌满水罐。
- 每株植物都可以由 Alice 或者 Bob 来浇水。
- 如果 Alice 和 Bob 到达同一株植物，那么当前水罐中水更多的人会给这株植物浇水。如果他俩水量相同，那么 Alice 会给这株植物浇水。
给你一个下标从 **0** 开始的整数数组 `plants` ，数组由 `n` 个整数组成。其中， `plants[i]` 为第 `i` 株植物需要的水量。另有两个整数 `capacityA` 和 `capacityB` 分别表示 Alice 和 Bob 水罐的容量。返回两人浇灌所有植物过程中重新灌满水罐的 **次数** 。

 

 **示例 1：** 

```
输入：plants = [2,2,3,3], capacityA = 5, capacityB = 5
输出：1
解释：
- 最初，Alice 和 Bob 的水罐中各有 5 单元水。
- Alice 给植物 0 浇水，Bob 给植物 3 浇水。
- Alice 和 Bob 现在分别剩下 3 单元和 2 单元水。
- Alice 有足够的水给植物 1 ，所以她直接浇水。Bob 的水不够给植物 2 ，所以他先重新装满水，再浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 0 + 1 + 0 = 1 。
```
 **示例 2：** 

```
输入：plants = [2,2,3,3], capacityA = 3, capacityB = 4
输出：2
解释：
- 最初，Alice 的水罐中有 3 单元水，Bob 的水罐中有 4 单元水。
- Alice 给植物 0 浇水，Bob 给植物 3 浇水。
- Alice 和 Bob 现在都只有 1 单元水，并分别需要给植物 1 和植物 2 浇水。
- 由于他们的水量均不足以浇水，所以他们重新灌满水罐再进行浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 1 + 1 + 0 = 2 。
```
 **示例 3：** 

```
输入：plants = [5], capacityA = 10, capacityB = 8
输出：0
解释：
- 只有一株植物
- Alice 的水罐有 10 单元水，Bob 的水罐有 8 单元水。因此 Alice 的水罐中水更多，她会给这株植物浇水。
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 。
```
 **示例 4：** 

```
输入：plants = [1,2,4,4,5], capacityA = 6, capacityB = 5
输出：2
解释：
- 最初，Alice 的水罐中有 6 单元水，Bob 的水罐中有 5 单元水。
- Alice 给植物 0 浇水，Bob 给植物 4 浇水。
- Alice 和 Bob 现在分别剩下 5 单元和 0 单元水。
- Alice 有足够的水给植物 1 ，所以她直接浇水。Bob 的水不够给植物 3 ，所以他先重新装满水，再浇水。
- Alice 和 Bob 现在分别剩下 3 单元和 1 单元水。
- 由于 Alice 的水更多，所以由她给植物 2 浇水。然而，她水罐里的水不够给植物 2 ，所以她先重新装满水，再浇水。 
所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 0 + 0 + 1 + 1 + 0 = 2 。
```
 **示例 5：** 

```
输入：plants = [2,2,5,2,2], capacityA = 5, capacityB = 5
输出：1
解释：
Alice 和 Bob 都会到达中间的植物，并且此时他俩剩下的水量相同，所以 Alice 会给这株植物浇水。
由于她到达时只剩下 1 单元水，所以需要重新灌满水罐。
这是唯一一次需要重新灌满水罐的情况。所以，两人浇灌所有植物过程中重新灌满水罐的次数 = 1 。

```
 

 **提示：** 
-  `n == plants.length` 
-  `1 <= n <= 10^5` 
-  `1 <= plants[i] <= 10^6` 
-  `max(plants[i]) <= capacityA, capacityB <= 10^9` 
 
**标签**
`数组` `双指针` `模拟` 


## 
```python

```
>
# 2106.摘水果
[https://leetcode-cn.com/problems/maximum-fruits-harvested-after-at-most-k-steps](https://leetcode-cn.com/problems/maximum-fruits-harvested-after-at-most-k-steps) 
## 原题
在一个无限的 x 坐标轴上，有许多水果分布在其中某些位置。给你一个二维整数数组 `fruits` ，其中 `fruits[i] = [position<sub>i</sub>, amount<sub>i</sub>]` 表示共有 `amount<sub>i</sub>` 个水果放置在 `position<sub>i</sub>` 上。 `fruits` 已经按 `position<sub>i</sub>` **升序排列** ，每个 `position<sub>i</sub>` **互不相同** 。

另给你两个整数 `startPos` 和 `k` 。最初，你位于 `startPos` 。从任何位置，你可以选择 **向左或者向右** 走。在 x 轴上每移动 **一个单位** ，就记作 **一步** 。你总共可以走 **最多** `k` 步。你每达到一个位置，都会摘掉全部的水果，水果也将从该位置消失（不会再生）。

返回你可以摘到水果的 **最大总数** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/21/1.png" style="width: 472px; height: 115px;">
```
输入：fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4
输出：9
解释：
最佳路线为：
- 向右移动到位置 6 ，摘到 3 个水果
- 向右移动到位置 8 ，摘到 6 个水果
移动 3 步，共摘到 3 + 6 = 9 个水果

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/21/2.png" style="width: 512px; height: 129px;">
```
输入：fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4
输出：14
解释：
可以移动最多 k = 4 步，所以无法到达位置 0 和位置 10 。
最佳路线为：
- 在初始位置 5 ，摘到 7 个水果
- 向左移动到位置 4 ，摘到 1 个水果
- 向右移动到位置 6 ，摘到 2 个水果
- 向右移动到位置 7 ，摘到 4 个水果
移动 1 + 3 = 4 步，共摘到 7 + 1 + 2 + 4 = 14 个水果

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/11/21/3.png" style="width: 476px; height: 100px;">
```
输入：fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2
输出：0
解释：
最多可以移动 k = 2 步，无法到达任一有水果的地方

```
 

 **提示：** 
-  `1 <= fruits.length <= 10^5` 
-  `fruits[i].length == 2` 
-  `0 <= startPos, position<sub>i</sub> <= 2 * 10^5` 
- 对于任意 `i > 0` ， `position<sub>i-1</sub> < position<sub>i</sub>` 均成立（下标从 **0** 开始计数）
-  `1 <= amount<sub>i</sub> <= 10^4` 
-  `0 <= k <= 2 * 10^5` 
 
**标签**
`数组` `二分查找` `前缀和` `滑动窗口` 


## 
```python

```
>
# 2108.找出数组中的第一个回文字符串
[https://leetcode-cn.com/problems/find-first-palindromic-string-in-the-array](https://leetcode-cn.com/problems/find-first-palindromic-string-in-the-array) 
## 原题
给你一个字符串数组 `words` ，找出并返回数组中的 **第一个回文字符串** 。如果不存在满足要求的字符串，返回一个 **空字符串**  `""` 。

 **回文字符串** 的定义为：如果一个字符串正着读和反着读一样，那么该字符串就是一个 **回文字符串** 。

 

 **示例 1：** 

```
输入：words = ["abc","car","ada","racecar","cool"]
输出："ada"
解释：第一个回文字符串是 "ada" 。
注意，"racecar" 也是回文字符串，但它不是第一个。

```
 **示例 2：** 

```
输入：words = ["notapalindrome","racecar"]
输出："racecar"
解释：第一个也是唯一一个回文字符串是 "racecar" 。

```
 **示例 3：** 

```
输入：words = ["def","ghi"]
输出：""
解释：不存在回文字符串，所以返回一个空字符串。

```
 

 **提示：** 
-  `1 <= words.length <= 100` 
-  `1 <= words[i].length <= 100` 
-  `words[i]` 仅由小写英文字母组成
 
**标签**
`数组` `双指针` `字符串` 


## 
```python

```
>
# 2109.向字符串添加空格
[https://leetcode-cn.com/problems/adding-spaces-to-a-string](https://leetcode-cn.com/problems/adding-spaces-to-a-string) 
## 原题
给你一个下标从 **0** 开始的字符串 `s` ，以及一个下标从 **0** 开始的整数数组 `spaces` 。

数组 `spaces` 描述原字符串中需要添加空格的下标。每个空格都应该插入到给定索引处的字符值 **之前** 。
- 例如， `s = "EnjoyYourCoffee"` 且 `spaces = [5, 9]` ，那么我们需要在 `'Y'` 和 `'C'` 之前添加空格，这两个字符分别位于下标 `5` 和下标 `9` 。因此，最终得到 `"Enjoy ***Y*** our ***C*** offee"` 。
请你添加空格，并返回修改后的字符串 *。* 

 

 **示例 1：** 

```

输入：s = "LeetcodeHelpsMeLearn", spaces = [8,13,15]
输出："Leetcode Helps Me Learn"
解释：
下标 8、13 和 15 对应 "LeetcodeHelpsMeLearn" 中加粗斜体字符。
接着在这些字符前添加空格。

```
 **示例 2：** 

```

输入：s = "icodeinpython", spaces = [1,5,7,9]
输出："i code in py thon"
解释：
下标 1、5、7 和 9 对应 "icodeinpython" 中加粗斜体字符。
接着在这些字符前添加空格。

```
 **示例 3：** 

```

输入：s = "spacing", spaces = [0,1,2,3,4,5,6]
输出：" s p a c i n g"
解释：
字符串的第一个字符前可以添加空格。

```
 

 **提示：** 
-  `1 <= s.length <= 3 * 10^5` 
-  `s` 仅由大小写英文字母组成
-  `1 <= spaces.length <= 3 * 10^5` 
-  `0 <= spaces[i] <= s.length - 1` 
-  `spaces` 中的所有值 **严格递增** 
 
**标签**
`数组` `字符串` `模拟` 


## 
```python

```
>
# 2110.股票平滑下跌阶段的数目
[https://leetcode-cn.com/problems/number-of-smooth-descent-periods-of-a-stock](https://leetcode-cn.com/problems/number-of-smooth-descent-periods-of-a-stock) 
## 原题
给你一个整数数组 `prices` ，表示一支股票的历史每日股价，其中 `prices[i]` 是这支股票第 `i` 天的价格。

一个 **平滑下降的阶段** 定义为：对于 **连续一天或者多天** ，每日股价都比 **前一日股价恰好少** `1` ，这个阶段第一天的股价没有限制。

请你返回 **平滑下降阶段** 的数目。

 

 **示例 1：** 

```
输入：prices = [3,2,1,4]
输出：7
解释：总共有 7 个平滑下降阶段：
[3], [2], [1], [4], [3,2], [2,1] 和 [3,2,1]
注意，仅一天按照定义也是平滑下降阶段。

```
 **示例 2：** 

```
输入：prices = [8,6,7,7]
输出：4
解释：总共有 4 个连续平滑下降阶段：[8], [6], [7] 和 [7]
由于 8 - 6 ≠ 1 ，所以 [8,6] 不是平滑下降阶段。

```
 **示例 3：** 

```
输入：prices = [1]
输出：1
解释：总共有 1 个平滑下降阶段：[1]

```
 

 **提示：** 
-  `1 <= prices.length <= 10^5` 
-  `1 <= prices[i] <= 10^5` 
 
**标签**
`数组` `数学` `动态规划` 


## 
```python

```
>
# 2111.使数组 K 递增的最少操作次数
[https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-k-increasing](https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-k-increasing) 
## 原题
给你一个下标从 **0** 开始包含 `n` 个正整数的数组 `arr` ，和一个正整数 `k` 。

如果对于每个满足 `k <= i <= n-1` 的下标 `i` ，都有 `arr[i-k] <= arr[i]` ，那么我们称 `arr` 是 **K** **递增** 的。
- 比方说， `arr = [4, 1, 5, 2, 6, 2]` 对于 `k = 2` 是 K 递增的，因为：

	
-  `arr[0] <= arr[2] (4 <= 5)` 
-  `arr[1] <= arr[3] (1 <= 2)` 
-  `arr[2] <= arr[4] (5 <= 6)` 
-  `arr[3] <= arr[5] (2 <= 2)` 
	
	
- 但是，相同的数组 `arr` 对于 `k = 1` 不是 K 递增的（因为 `arr[0] > arr[1]` ），对于 `k = 3` 也不是 K 递增的（因为 `arr[0] > arr[3]` ）。
每一次 **操作** 中，你可以选择一个下标 `i` 并将 `arr[i]` **改成任意** 正整数。

请你返回对于给定的 `k` ，使数组变成 K 递增的 **最少操作次数** 。

 

 **示例 1：** 

```
输入：arr = [5,4,3,2,1], k = 1
输出：4
解释：
对于 k = 1 ，数组最终必须变成非递减的。
可行的 K 递增结果数组为 [5,6,7,8,9]，[1,1,1,1,1]，[2,2,3,4,4] 。它们都需要 4 次操作。
次优解是将数组变成比方说 [6,7,8,9,10] ，因为需要 5 次操作。
显然我们无法使用少于 4 次操作将数组变成 K 递增的。

```
 **示例 2：** 

```
输入：arr = [4,1,5,2,6,2], k = 2
输出：0
解释：
这是题目描述中的例子。
对于每个满足 2 <= i <= 5 的下标 i ，有 arr[i-2] <= arr[i] 。
由于给定数组已经是 K 递增的，我们不需要进行任何操作。
```
 **示例 3：** 

```
输入：arr = [4,1,5,2,6,2], k = 3
输出：2
解释：
下标 3 和 5 是仅有的 3 <= i <= 5 且不满足 arr[i-3] <= arr[i] 的下标。
将数组变成 K 递增的方法之一是将 arr[3] 变为 4 ，且将 arr[5] 变成 5 。
数组变为 [4,1,5,4,6,5] 。
可能有其他方法将数组变为 K 递增的，但没有任何一种方法需要的操作次数小于 2 次。

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `1 <= arr[i], k <= arr.length` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 2117.一个区间内所有数乘积的缩写
[https://leetcode-cn.com/problems/abbreviating-the-product-of-a-range](https://leetcode-cn.com/problems/abbreviating-the-product-of-a-range) 
## 原题
给你两个正整数 `left` 和 `right` ，满足 `left <= right` 。请你计算 **闭区间** `[left, right]` 中所有整数的 **乘积** 。

由于乘积可能非常大，你需要将它按照以下步骤 **缩写** ：
- 统计乘积中 **后缀** 0 的数目，并 **移除** 这些 0 ，将这个数目记为 `C` 。

	
- 比方说， `1000` 中有 `3` 个后缀 0 ， `546` 中没有后缀 0 。
	
	
- 将乘积中剩余数字的位数记为 `d` 。如果 `d > 10` ，那么将乘积表示为 ````
...<suf>` 的形式，其中 ````
` 表示乘积最 **开始** 的 `5` 个数位， `<suf>` 表示删除后缀 0 **之后** 结尾的 `5` 个数位。如果 `d <= 10` ，我们不对它做修改。
	
- 比方说，我们将 `1234567654321` 表示为 `12345...54321` ，但是 `1234567` 仍然表示为 `1234567` 。
	
	
- 最后，将乘积表示为 **字符串** `"```
...<suf>eC"` 。
	
- 比方说， `12345678987600000` 被表示为 `"12345...89876e5"` 。
	
	
请你返回一个字符串，表示 **闭区间** `[left, right]` 中所有整数 **乘积** 的 **缩写** 。

 

 **示例 1：** 

```

输入：left = 1, right = 4
输出："24e0"
解释：
乘积为 1 × 2 × 3 × 4 = 24 。
由于没有后缀 0 ，所以 24 保持不变，缩写的结尾为 "e0" 。
因为乘积的结果是 2 位数，小于 10 ，所欲我们不进一步将它缩写。
所以，最终将乘积表示为 "24e0" 。

```
 **示例 2：** 

```

输入：left = 2, right = 11
输出："399168e2"
解释：乘积为 39916800 。
有 2 个后缀 0 ，删除后得到 399168 。缩写的结尾为 "e2" 。 
删除后缀 0 后是 6 位数，不需要进一步缩写。 
所以，最终将乘积表示为 "399168e2" 。

```
 **示例 3：** 

```

输入：left = 371, right = 375
输出："7219856259e3"
解释：乘积为 7219856259000 。

```
 

 **提示：** 
-  `1 <= left <= right <= 10^4` 
 
**标签**
`数学` 


## 
```python

```
>
# 2119.反转两次的数字
[https://leetcode-cn.com/problems/a-number-after-a-double-reversal](https://leetcode-cn.com/problems/a-number-after-a-double-reversal) 
## 原题
 **反转** 一个整数意味着倒置它的所有位。
- 例如，反转 `2021` 得到 `1202` 。反转 `12300` 得到 `321` ， **不保留前导零** 。
给你一个整数 `num` ， **反转** `num` 得到 `reversed1` ， **接着反转** `reversed1` 得到 `reversed2` 。如果 `reversed2` 等于 `num` ，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```
输入：num = 526
输出：true
解释：反转 num 得到 625 ，接着反转 625 得到 526 ，等于 num 。

```
 **示例 2：** 

```
输入：num = 1800
输出：false
解释：反转 num 得到 81 ，接着反转 81 得到 18 ，不等于 num 。 
```
 **示例 3：** 

```
输入：num = 0
输出：true
解释：反转 num 得到 0 ，接着反转 0 得到 0 ，等于 num 。

```
 

 **提示：** 
-  `0 <= num <= 10^6` 
 
**标签**
`数学` 


## 
```python

```
>
# 2120.执行所有后缀指令
[https://leetcode-cn.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid](https://leetcode-cn.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid) 
## 原题
现有一个 `n x n` 大小的网格，左上角单元格坐标 `(0, 0)` ，右下角单元格坐标 `(n - 1, n - 1)` 。给你整数 `n` 和一个整数数组 `startPos` ，其中 `startPos = [start<sub>row</sub>, start<sub>col</sub>]` 表示机器人最开始在坐标为 `(start<sub>row</sub>, start<sub>col</sub>)` 的单元格上。

另给你一个长度为 `m` 、下标从 **0** 开始的字符串 `s` ，其中 `s[i]` 是对机器人的第 `i` 条指令： `'L'` （向左移动）， `'R'` （向右移动）， `'U'` （向上移动）和 `'D'` （向下移动）。

机器人可以从 `s` 中的任一第 `i` 条指令开始执行。它将会逐条执行指令直到 `s` 的末尾，但在满足下述条件之一时，机器人将会停止：
- 下一条指令将会导致机器人移动到网格外。
- 没有指令可以执行。
返回一个长度为 `m` 的数组 `answer` ，其中 `answer[i]` 是机器人从第 `i` 条指令 **开始** ，可以执行的 **指令数目** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/09/1.png" style="width: 145px; height: 142px;" />

```

输入：n = 3, startPos = [0,1], s = "RRDDLU"
输出：[1,5,4,3,1,0]
解释：机器人从 startPos 出发，并从第 i 条指令开始执行：
- 0: "RRDDLU" 在移动到网格外之前，只能执行一条 "R" 指令。
- 1:  "RDDLU" 可以执行全部五条指令，机器人仍在网格内，最终到达 (0, 0) 。
- 2:   "DDLU" 可以执行全部四条指令，机器人仍在网格内，最终到达 (0, 0) 。
- 3:    "DLU" 可以执行全部三条指令，机器人仍在网格内，最终到达 (0, 0) 。
- 4:     "LU" 在移动到网格外之前，只能执行一条 "L" 指令。
- 5:      "U" 如果向上移动，将会移动到网格外。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/09/2.png" style="width: 106px; height: 103px;" />

```

输入：n = 2, startPos = [1,1], s = "LURD"
输出：[4,1,0,0]
解释：
- 0: "LURD"
- 1:  "URD"
- 2:   "RD"
- 3:    "D"

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/09/3.png" style="width: 67px; height: 64px;" />

```

输入：n = 1, startPos = [0,0], s = "LRUD"
输出：[0,0,0,0]
解释：无论机器人从哪条指令开始执行，都会移动到网格外。

```
 

 **提示：** 
-  `m == s.length` 
-  `1 <= n, m <= 500` 
-  `startPos.length == 2` 
-  `0 <= start<sub>row</sub>, start<sub>col</sub> < n` 
-  `s` 由 `'L'` 、 `'R'` 、 `'U'` 和 `'D'` 组成
 
**标签**
`字符串` `模拟` 


## 
```python

```
>
# 2122.还原原数组
[https://leetcode-cn.com/problems/recover-the-original-array](https://leetcode-cn.com/problems/recover-the-original-array) 
## 原题
Alice 有一个下标从 **0** 开始的数组 `arr` ，由 `n` 个正整数组成。她会选择一个任意的 **正整数** `k` 并按下述方式创建两个下标从 **0** 开始的新整数数组 `lower` 和 `higher` ：
- 对每个满足 `0 <= i < n` 的下标 `i` ， `lower[i] = arr[i] - k` 
- 对每个满足 `0 <= i < n` 的下标 `i` ， `higher[i] = arr[i] + k` 
不幸地是，Alice 丢失了全部三个数组。但是，她记住了在数组 `lower` 和 `higher` 中出现的整数，但不知道每个整数属于哪个数组。请你帮助 Alice 还原原数组。

给你一个由 2n 个整数组成的整数数组 `nums` ，其中 **恰好** `n` 个整数出现在 `lower` ，剩下的出现在 `higher` ，还原并返回 **原数组** `arr` 。如果出现答案不唯一的情况，返回 **任一** 有效数组。

 **注意：** 生成的测试用例保证存在 **至少一个** 有效数组 `arr` 。

 

 **示例 1：** 

```
输入：nums = [2,10,6,4,8,12]
输出：[3,7,11]
解释：
如果 arr = [3,7,11] 且 k = 1 ，那么 lower = [2,6,10] 且 higher = [4,8,12] 。
组合 lower 和 higher 得到 [2,6,10,4,8,12] ，这是 nums 的一个排列。
另一个有效的数组是 arr = [5,7,9] 且 k = 3 。在这种情况下，lower = [2,4,6] 且 higher = [8,10,12] 。

```
 **示例 2：** 

```
输入：nums = [1,1,3,3]
输出：[2,2]
解释：
如果 arr = [2,2] 且 k = 1 ，那么 lower = [1,1] 且 higher = [3,3] 。
组合 lower 和 higher 得到 [1,1,3,3] ，这是 nums 的一个排列。
注意，数组不能是 [1,3] ，因为在这种情况下，获得 [1,1,3,3] 唯一可行的方案是 k = 0 。
这种方案是无效的，k 必须是一个正整数。

```
 **示例 3：** 

```
输入：nums = [5,435]
输出：[220]
解释：
唯一可行的组合是 arr = [220] 且 k = 215 。在这种情况下，lower = [5] 且 higher = [435] 。
```
 

 **提示：** 
-  `2 * n == nums.length` 
-  `1 <= n <= 1000` 
-  `1 <= nums[i] <= 10^9` 
- 生成的测试用例保证存在 **至少一个** 有效数组 `arr` 
 
**标签**
`数组` `哈希表` `枚举` `排序` 


## 
```python

```
>
# 2126.摧毁小行星
[https://leetcode-cn.com/problems/destroying-asteroids](https://leetcode-cn.com/problems/destroying-asteroids) 
## 原题
给你一个整数 `mass` ，它表示一颗行星的初始质量。再给你一个整数数组 `asteroids` ，其中 `asteroids[i]` 是第 `i` 颗小行星的质量。

你可以按 **任意顺序** 重新安排小行星的顺序，然后让行星跟它们发生碰撞。如果行星碰撞时的质量 **大于等于** 小行星的质量，那么小行星被 **摧毁** ，并且行星会 **获得** 这颗小行星的质量。否则，行星将被摧毁。

如果所有小行星 **都** 能被摧毁，请返回 `true` ，否则返回 `false` 。

 

 **示例 1：** 

```
输入：mass = 10, asteroids = [3,9,19,5,21]
输出：true
解释：一种安排小行星的方式为 [9,19,5,3,21] ：
- 行星与质量为 9 的小行星碰撞。新的行星质量为：10 + 9 = 19
- 行星与质量为 19 的小行星碰撞。新的行星质量为：19 + 19 = 38
- 行星与质量为 5 的小行星碰撞。新的行星质量为：38 + 5 = 43
- 行星与质量为 3 的小行星碰撞。新的行星质量为：43 + 3 = 46
- 行星与质量为 21 的小行星碰撞。新的行星质量为：46 + 21 = 67
所有小行星都被摧毁。

```
 **示例 2：** 

```
输入：mass = 5, asteroids = [4,9,23,4]
输出：false
解释：
行星无论如何没法获得足够质量去摧毁质量为 23 的小行星。
行星把别的小行星摧毁后，质量为 5 + 4 + 9 + 4 = 22 。
它比 23 小，所以无法摧毁最后一颗小行星。
```
 

 **提示：** 
-  `1 <= mass <= 10^5` 
-  `1 <= asteroids.length <= 10^5` 
-  `1 <= asteroids[i] <= 10^5` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 2127.参加会议的最多员工数
[https://leetcode-cn.com/problems/maximum-employees-to-be-invited-to-a-meeting](https://leetcode-cn.com/problems/maximum-employees-to-be-invited-to-a-meeting) 
## 原题
一个公司准备组织一场会议，邀请名单上有 `n` 位员工。公司准备了一张 **圆形** 的桌子，可以坐下 **任意数目** 的员工。

员工编号为 `0` 到 `n - 1` 。每位员工都有一位 **喜欢** 的员工，每位员工 **当且仅当** 他被安排在喜欢员工的旁边，他才会参加会议。每位员工喜欢的员工 **不会** 是他自己。

给你一个下标从 **0** 开始的整数数组 `favorite` ，其中 `favorite[i]` 表示第 `i` 位员工喜欢的员工。请你返回参加会议的 **最多员工数目** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/14/ex1.png" style="width: 236px; height: 195px;">

```
输入：favorite = [2,2,1,2]
输出：3
解释：
上图展示了公司邀请员工 0，1 和 2 参加会议以及他们在圆桌上的座位。
没办法邀请所有员工参与会议，因为员工 2 没办法同时坐在 0，1 和 3 员工的旁边。
注意，公司也可以邀请员工 1，2 和 3 参加会议。
所以最多参加会议的员工数目为 3 。

```
 **示例 2：** 

```
输入：favorite = [1,2,0]
输出：3
解释：
每个员工都至少是另一个员工喜欢的员工。所以公司邀请他们所有人参加会议的前提是所有人都参加了会议。
座位安排同图 1 所示：
- 员工 0 坐在员工 2 和 1 之间。
- 员工 1 坐在员工 0 和 2 之间。
- 员工 2 坐在员工 1 和 0 之间。
参与会议的最多员工数目为 3 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/14/ex2.png" style="width: 219px; height: 220px;">

```
输入：favorite = [3,0,1,4,1]
输出：4
解释：
上图展示了公司可以邀请员工 0，1，3 和 4 参加会议以及他们在圆桌上的座位。
员工 2 无法参加，因为他喜欢的员工 0 旁边的座位已经被占领了。
所以公司只能不邀请员工 2 。
参加会议的最多员工数目为 4 。

```
 

 **提示：** 
-  `n == favorite.length` 
-  `2 <= n <= 10^5` 
-  `0 <= favorite[i] <= n - 1` 
-  `favorite[i] != i` 
 
**标签**
`深度优先搜索` `图` `拓扑排序` 


## 
```python

```
>
# 2132.用邮票贴满网格图
[https://leetcode-cn.com/problems/stamping-the-grid](https://leetcode-cn.com/problems/stamping-the-grid) 
## 原题
给你一个 `m x n` 的二进制矩阵 `grid` ，每个格子要么为 `0` （空）要么为 `1` （被占据）。

给你邮票的尺寸为 `stampHeight x stampWidth` 。我们想将邮票贴进二进制矩阵中，且满足以下 **限制** 和 **要求** ：
- 覆盖所有 **空** 格子。
- 不覆盖任何 **被占据** 的格子。
- 我们可以放入任意数目的邮票。
- 邮票可以相互有 **重叠** 部分。
- 邮票不允许 **旋转** 。
- 邮票必须完全在矩阵 **内** 。
如果在满足上述要求的前提下，可以放入邮票，请返回 `true` ，否则返回<i> </i> `false` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/ex1.png" style="width: 180px; height: 237px;">

```
输入：grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3
输出：true
解释：我们放入两个有重叠部分的邮票（图中标号为 1 和 2），它们能覆盖所有与空格子。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/11/03/ex2.png" style="width: 170px; height: 179px;">

```
输入：grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2 
输出：false 
解释：没办法放入邮票覆盖所有的空格子，且邮票不超出网格图以外。

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[r].length` 
-  `1 <= m, n <= 10^5` 
-  `1 <= m * n <= 2 * 10^5` 
-  `grid[r][c]` 要么是 `0` ，要么是 `1` 。
-  `1 <= stampHeight, stampWidth <= 10^5` 
 
**标签**
`贪心` `数组` `矩阵` `前缀和` 


## 
```python

```
>
# 2136.全部开花的最早一天
[https://leetcode-cn.com/problems/earliest-possible-day-of-full-bloom](https://leetcode-cn.com/problems/earliest-possible-day-of-full-bloom) 
## 原题
你有 `n` 枚花的种子。每枚种子必须先种下，才能开始生长、开花。播种需要时间，种子的生长也是如此。给你两个下标从 **0** 开始的整数数组 `plantTime` 和 `growTime` ，每个数组的长度都是 `n` ：
-  `plantTime[i]` 是 **播种** 第 `i` 枚种子所需的 **完整天数** 。每天，你只能为播种某一枚种子而劳作。 **无须** 连续几天都在种同一枚种子，但是种子播种必须在你工作的天数达到 `plantTime[i]` 之后才算完成。
-  `growTime[i]` 是第 `i` 枚种子完全种下后生长所需的 **完整天数** 。在它生长的最后一天 **之后** ，将会开花并且永远 **绽放** 。
从第 `0` 开始，你可以按 **任意** 顺序播种种子。

返回所有种子都开花的 **最早** 一天是第几天。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/21/1.png" style="width: 453px; height: 149px;">
```
输入：plantTime = [1,4,3], growTime = [2,3,1]
输出：9
解释：灰色的花盆表示播种的日子，彩色的花盆表示生长的日子，花朵表示开花的日子。
一种最优方案是：
第 0 天，播种第 0 枚种子，种子生长 2 整天。并在第 3 天开花。
第 1、2、3、4 天，播种第 1 枚种子。种子生长 3 整天，并在第 8 天开花。
第 5、6、7 天，播种第 2 枚种子。种子生长 1 整天，并在第 9 天开花。
因此，在第 9 天，所有种子都开花。 

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/12/21/2.png" style="width: 454px; height: 184px;">
```
输入：plantTime = [1,2,3,2], growTime = [2,1,2,1]
输出：9
解释：灰色的花盆表示播种的日子，彩色的花盆表示生长的日子，花朵表示开花的日子。 
一种最优方案是：
第 1 天，播种第 0 枚种子，种子生长 2 整天。并在第 4 天开花。
第 0、3 天，播种第 1 枚种子。种子生长 1 整天，并在第 5 天开花。
第 2、4、5 天，播种第 2 枚种子。种子生长 2 整天，并在第 8 天开花。
第 6、7 天，播种第 3 枚种子。种子生长 1 整天，并在第 9 天开花。
因此，在第 9 天，所有种子都开花。 

```
 **示例 3：** 

```
输入：plantTime = [1], growTime = [1]
输出：2
解释：第 0 天，播种第 0 枚种子。种子需要生长 1 整天，然后在第 2 天开花。
因此，在第 2 天，所有种子都开花。

```
 

 **提示：** 
-  `n == plantTime.length == growTime.length` 
-  `1 <= n <= 10^5` 
-  `1 <= plantTime[i], growTime[i] <= 10^4` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 2139.得到目标值的最少行动次数
[https://leetcode-cn.com/problems/minimum-moves-to-reach-target-score](https://leetcode-cn.com/problems/minimum-moves-to-reach-target-score) 
## 原题
你正在玩一个整数游戏。从整数 `1` 开始，期望得到整数 `target` 。

在一次行动中，你可以做下述两种操作之一：
-  **递增** ，将当前整数的值加 1（即， `x = x + 1` ）。
-  **加倍** ，使当前整数的值翻倍（即， `x = 2 * x` ）。
在整个游戏过程中，你可以使用 **递增** 操作 **任意** 次数。但是只能使用 **加倍** 操作 **至多** `maxDoubles` 次。

给你两个整数 `target` 和 `maxDoubles` ，返回从 1 开始得到 `target` 需要的最少行动次数。

 

 **示例 1：** 

```
输入：target = 5, maxDoubles = 0
输出：4
解释：一直递增 1 直到得到 target 。

```
 **示例 2：** 

```
输入：target = 19, maxDoubles = 2
输出：7
解释：最初，x = 1 。
递增 3 次，x = 4 。
加倍 1 次，x = 8 。
递增 1 次，x = 9 。
加倍 1 次，x = 18 。
递增 1 次，x = 19 。

```
 **示例 3：** 

```
输入：target = 10, maxDoubles = 4
输出：4
解释：
最初，x = 1 。 
递增 1 次，x = 2 。 
加倍 1 次，x = 4 。 
递增 1 次，x = 5 。 
加倍 1 次，x = 10 。 

```
 

 **提示：** 
-  `1 <= target <= 10^9` 
-  `0 <= maxDoubles <= 100` 
 
**标签**
`贪心` `数学` 


## 
```python

```
>
# 2141.同时运行 N 台电脑的最长时间
[https://leetcode-cn.com/problems/maximum-running-time-of-n-computers](https://leetcode-cn.com/problems/maximum-running-time-of-n-computers) 
## 原题
你有 `n` 台电脑。给你整数 `n` 和一个下标从 **0** 开始的整数数组 `batteries` ，其中第 `i` 个电池可以让一台电脑 **运行** `batteries[i]` 分钟。你想使用这些电池让 **全部** `n` 台电脑 <b>同时</b> 运行。

一开始，你可以给每台电脑连接 **至多一个电池** 。然后在任意整数时刻，你都可以将一台电脑与它的电池断开连接，并连接另一个电池，你可以进行这个操作 **任意次** 。新连接的电池可以是一个全新的电池，也可以是别的电脑用过的电池。断开连接和连接新的电池不会花费任何时间。

注意，你不能给电池充电。

请你返回你可以让 `n` 台电脑同时运行的 **最长** 分钟数。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2022/01/06/example1-fit.png" style="width: 762px; height: 150px;">

```
输入：n = 2, batteries = [3,3,3]
输出：4
解释：
一开始，将第一台电脑与电池 0 连接，第二台电脑与电池 1 连接。
2 分钟后，将第二台电脑与电池 1 断开连接，并连接电池 2 。注意，电池 0 还可以供电 1 分钟。
在第 3 分钟结尾，你需要将第一台电脑与电池 0 断开连接，然后连接电池 1 。
在第 4 分钟结尾，电池 1 也被耗尽，第一台电脑无法继续运行。
我们最多能同时让两台电脑同时运行 4 分钟，所以我们返回 4 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2022/01/06/example2.png" style="width: 629px; height: 150px;">

```
输入：n = 2, batteries = [1,1,1,1]
输出：2
解释：
一开始，将第一台电脑与电池 0 连接，第二台电脑与电池 2 连接。
一分钟后，电池 0 和电池 2 同时耗尽，所以你需要将它们断开连接，并将电池 1 和第一台电脑连接，电池 3 和第二台电脑连接。
1 分钟后，电池 1 和电池 3 也耗尽了，所以两台电脑都无法继续运行。
我们最多能让两台电脑同时运行 2 分钟，所以我们返回 2 。

```
 

 **提示：** 
-  `1 <= n <= batteries.length <= 10^5` 
-  `1 <= batteries[i] <= 10^9` 
 
**标签**
`贪心` `数组` `二分查找` `排序` 


## 
```python

```
>
# 2145.统计隐藏数组数目
[https://leetcode-cn.com/problems/count-the-hidden-sequences](https://leetcode-cn.com/problems/count-the-hidden-sequences) 
## 原题
给你一个下标从 **0** 开始且长度为 `n` 的整数数组 `differences` ，它表示一个长度为 `n + 1` 的 **隐藏** 数组 **相邻** 元素之间的 **差值** 。更正式的表述为：我们将隐藏数组记作 `hidden` ，那么 `differences[i] = hidden[i + 1] - hidden[i]` 。

同时给你两个整数 `lower` 和 `upper` ，它们表示隐藏数组中所有数字的值都在 **闭** 区间 `[lower, upper]` 之间。
- 比方说， `differences = [1, -3, 4]` ， `lower = 1` ， `upper = 6` ，那么隐藏数组是一个长度为 `4` 且所有值都在 `1` 和 `6` （包含两者）之间的数组。

	
-  `[3, 4, 1, 5]` 和 `[4, 5, 2, 6]` 都是符合要求的隐藏数组。
-  `[5, 6, 3, 7]` 不符合要求，因为它包含大于 `6` 的元素。
-  `[1, 2, 3, 4]` 不符合要求，因为相邻元素的差值不符合给定数据。
	
	
请你返回 **符合** 要求的隐藏数组的数目。如果没有符合要求的隐藏数组，请返回 `0` 。

 

 **示例 1：** 

```
输入：differences = [1,-3,4], lower = 1, upper = 6
输出：2
解释：符合要求的隐藏数组为：
- [3, 4, 1, 5]
- [4, 5, 2, 6]
所以返回 2 。

```
 **示例 2：** 

```
输入：differences = [3,-4,5,1,-2], lower = -4, upper = 5
输出：4
解释：符合要求的隐藏数组为：
- [-3, 0, -4, 1, 2, 0]
- [-2, 1, -3, 2, 3, 1]
- [-1, 2, -2, 3, 4, 2]
- [0, 3, -1, 4, 5, 3]
所以返回 4 。

```
 **示例 3：** 

```
输入：differences = [4,-7,2], lower = 3, upper = 6
输出：0
解释：没有符合要求的隐藏数组，所以返回 0 。

```
 

 **提示：** 
-  `n == differences.length` 
-  `1 <= n <= 10^5` 
-  `-10^5 <= differences[i] <= 10^5` 
-  `-10^5 <= lower <= upper <= 10^5` 
 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 2147.分隔长廊的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-divide-a-long-corridor](https://leetcode-cn.com/problems/number-of-ways-to-divide-a-long-corridor) 
## 原题
在一个图书馆的长廊里，有一些座位和装饰植物排成一列。给你一个下标从 **0** 开始，长度为 `n` 的字符串 `corridor` ，它包含字母 `'S'` 和 `'P'` ，其中每个 `'S'` 表示一个座位，每个 `'P'` 表示一株植物。

在下标 `0` 的左边和下标 `n - 1` 的右边 **已经** 分别各放了一个屏风。你还需要额外放置一些屏风。每一个位置 `i - 1` 和 `i` 之间（ `1 <= i <= n - 1` ），至多能放一个屏风。

请你将走廊用屏风划分为若干段，且每一段内都 **恰好有两个座位** ，而每一段内植物的数目没有要求。可能有多种划分方案，如果两个方案中有任何一个屏风的位置不同，那么它们被视为 **不同** 方案。

请你返回划分走廊的方案数。由于答案可能很大，请你返回它对 `10^9 + 7` **取余** 的结果。如果没有任何方案，请返回 `0` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/04/1.png" style="width: 410px; height: 199px;">

```
输入：corridor = "SSPPSPS"
输出：3
解释：总共有 3 种不同分隔走廊的方案。
上图中黑色的竖线表示已经放置好的屏风。
上图每种方案中，每一段都恰好有 两个 座位。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/04/2.png" style="width: 357px; height: 68px;">

```
输入：corridor = "PPSPSP"
输出：1
解释：只有 1 种分隔走廊的方案，就是不放置任何屏风。
放置任何的屏风都会导致有一段无法恰好有 2 个座位。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/12/3.png" style="width: 115px; height: 68px;">

```
输入：corridor = "S"
输出：0
解释：没有任何方案，因为总是有一段无法恰好有 2 个座位。

```
 

 **提示：** 
-  `n == corridor.length` 
-  `1 <= n <= 10^5` 
-  `corridor[i]` 要么是 `'S'` ，要么是 `'P'` 。
 
**标签**
`数学` `字符串` `动态规划` 


## 
```python

```
>
# 2148.元素计数
[https://leetcode-cn.com/problems/count-elements-with-strictly-smaller-and-greater-elements](https://leetcode-cn.com/problems/count-elements-with-strictly-smaller-and-greater-elements) 
## 原题
给你一个整数数组 `nums` ，统计并返回在 `nums` 中同时至少具有一个严格较小元素和一个严格较大元素的元素数目。

 

 **示例 1：** 

```

输入：nums = [11,7,2,15]
输出：2
解释：元素 7 ：严格较小元素是元素 2 ，严格较大元素是元素 11 。
元素 11 ：严格较小元素是元素 7 ，严格较大元素是元素 15 。
总计有 2 个元素都满足在 nums 中同时存在一个严格较小元素和一个严格较大元素。

```
 **示例 2：** 

```

输入：nums = [-3,3,3,90]
输出：2
解释：元素 3 ：严格较小元素是元素 -3 ，严格较大元素是元素 90 。
由于有两个元素的值为 3 ，总计有 2 个元素都满足在 nums 中同时存在一个严格较小元素和一个严格较大元素。

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `-10^5 <= nums[i] <= 10^5` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 2150.找出数组中的所有孤独数字
[https://leetcode-cn.com/problems/find-all-lonely-numbers-in-the-array](https://leetcode-cn.com/problems/find-all-lonely-numbers-in-the-array) 
## 原题
给你一个整数数组 `nums` 。如果数字 `x` 在数组中仅出现 **一次** ，且没有 **相邻** 数字（即， `x + 1` 和 `x - 1` ）出现在数组中，则认为数字 `x` 是 **孤独数字** 。

返回 `nums` 中的 **所有** 孤独数字。你可以按 **任何顺序** 返回答案。

 

 **示例 1：** 

```
输入：nums = [10,6,5,8]
输出：[10,8]
解释：
- 10 是一个孤独数字，因为它只出现一次，并且 9 和 11 没有在 nums 中出现。
- 8 是一个孤独数字，因为它只出现一次，并且 7 和 9 没有在 nums 中出现。
- 5 不是一个孤独数字，因为 6 出现在 nums 中，反之亦然。
因此，nums 中的孤独数字是 [10, 8] 。
注意，也可以返回 [8, 10] 。

```
 **示例 2：** 

```
输入：nums = [1,3,5,3]
输出：[1,5]
解释：
- 1 是一个孤独数字，因为它只出现一次，并且 0 和 2 没有在 nums 中出现。
- 5 是一个孤独数字，因为它只出现一次，并且 4 和 6 没有在 nums 中出现。
- 3 不是一个孤独数字，因为它出现两次。
因此，nums 中的孤独数字是 [1, 5] 。
注意，也可以返回 [5, 1] 。
```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^6` 
 
**标签**
`数组` `哈希表` `计数` 


## 
```python

```
>
# 2151.基于陈述统计最多好人数
[https://leetcode-cn.com/problems/maximum-good-people-based-on-statements](https://leetcode-cn.com/problems/maximum-good-people-based-on-statements) 
## 原题
游戏中存在两种角色：
-  **好人** ：该角色只说真话。
-  **坏人** ：该角色可能说真话，也可能说假话。
给你一个下标从 **0** 开始的二维整数数组 `statements` ，大小为 `n x n` ，表示 `n` 个玩家对彼此角色的陈述。具体来说， `statements[i][j]` 可以是下述值之一：
-  `0` 表示 `i` 的陈述认为 `j` 是 **坏人** 。
-  `1` 表示 `i` 的陈述认为 `j` 是 **好人** 。
-  `2` 表示 `i` 没有对 `j` 作出陈述。
另外，玩家不会对自己进行陈述。形式上，对所有 `0 <= i < n` ，都有 `statements[i][i] = 2` 。

根据这 `n` 个玩家的陈述，返回可以认为是 **好人** 的 **最大** 数目。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/15/logic1.jpg" style="width: 600px; height: 262px;">
```
输入：statements = [[2,1,2],[1,2,2],[2,0,2]]
输出：2
解释：每个人都做一条陈述。
- 0 认为 1 是好人。
- 1 认为 0 是好人。
- 2 认为 1 是坏人。
以 2 为突破点。
- 假设 2 是一个好人：
    - 基于 2 的陈述，1 是坏人。
    - 那么可以确认 1 是坏人，2 是好人。
    - 基于 1 的陈述，由于 1 是坏人，那么他在陈述时可能：
        - 说真话。在这种情况下会出现矛盾，所以假设无效。
        - 说假话。在这种情况下，0 也是坏人并且在陈述时说假话。
    - 在认为 2 是好人的情况下，这组玩家中只有一个好人。
- 假设 2 是一个坏人：
    - 基于 2 的陈述，由于 2 是坏人，那么他在陈述时可能：
        - 说真话。在这种情况下，0 和 1 都是坏人。
            - 在认为 2 是坏人但说真话的情况下，这组玩家中没有一个好人。
        - 说假话。在这种情况下，1 是好人。
            - 由于 1 是好人，0 也是好人。
            - 在认为 2 是坏人且说假话的情况下，这组玩家中有两个好人。
在最佳情况下，至多有两个好人，所以返回 2 。
注意，能得到此结论的方法不止一种。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2022/01/15/logic2.jpg" style="width: 600px; height: 262px;">
```
输入：statements = [[2,0],[0,2]]
输出：1
解释：每个人都做一条陈述。
- 0 认为 1 是坏人。
- 1 认为 0 是坏人。
以 0 为突破点。
- 假设 0 是一个好人：
    - 基于与 0 的陈述，1 是坏人并说假话。
    - 在认为 0 是好人的情况下，这组玩家中只有一个好人。
- 假设 0 是一个坏人：
    - 基于 0 的陈述，由于 0 是坏人，那么他在陈述时可能：
        - 说真话。在这种情况下，0 和 1 都是坏人。
            - 在认为 0 是坏人但说真话的情况下，这组玩家中没有一个好人。
        - 说假话。在这种情况下，1 是好人。
            - 在认为 0 是坏人且说假话的情况下，这组玩家中只有一个好人。
在最佳情况下，至多有一个好人，所以返回 1 。 
注意，能得到此结论的方法不止一种。

```
 

 **提示：** 
-  `n == statements.length == statements[i].length` 
-  `2 <= n <= 15` 
-  `statements[i][j]` 的值为 `0` 、 `1` 或 `2` 
-  `statements[i][i] == 2` 
 
**标签**
`位运算` `数组` `回溯` `枚举` 


## 
```python

```
>
# 2154.将找到的值乘以 2
[https://leetcode-cn.com/problems/keep-multiplying-found-values-by-two](https://leetcode-cn.com/problems/keep-multiplying-found-values-by-two) 
## 原题
给你一个整数数组 `nums` ，另给你一个整数 `original` ，这是需要在 `nums` 中搜索的第一个数字。

接下来，你需要按下述步骤操作：
- 如果在 `nums` 中找到 `original` ，将 `original` **乘以** 2 ，得到新 `original` （即，令 `original = 2 * original` ）。
- 否则，停止这一过程。
- 只要能在数组中找到新 `original` ，就对新 `original` 继续 **重复** 这一过程 **。** 
返回 `original` 的 **最终** 值。

 

 **示例 1：** 

```

输入：nums = [5,3,6,1,12], original = 3
输出：24
解释： 
- 3 能在 nums 中找到。3 * 2 = 6 。
- 6 能在 nums 中找到。6 * 2 = 12 。
- 12 能在 nums 中找到。12 * 2 = 24 。
- 24 不能在 nums 中找到。因此，返回 24 。

```
 **示例 2：** 

```

输入：nums = [2,7,9], original = 4
输出：4
解释：
- 4 不能在 nums 中找到。因此，返回 4 。

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `1 <= nums[i], original <= 1000` 
 
**标签**
`数组` `哈希表` `排序` `模拟` 


## 
```python

```
>
# 2156.查找给定哈希值的子串
[https://leetcode-cn.com/problems/find-substring-with-given-hash-value](https://leetcode-cn.com/problems/find-substring-with-given-hash-value) 
## 原题
给定整数 `p` 和 `m` ，一个长度为 `k` 且下标从 **0** 开始的字符串 `s` 的哈希值按照如下函数计算：
-  `hash(s, p, m) = (val(s[0]) * p^0 + val(s[1]) * p^1 + ... + val(s[k-1]) * p^k-1) mod m` .
其中 `val(s[i])` 表示 `s[i]` 在字母表中的下标，从 `val('a') = 1` 到 `val('z') = 26` 。

给你一个字符串 `s` 和整数 `power` ， `modulo` ， `k` 和 `hashValue` 。请你返回 `s` 中 **第一个** 长度为 `k` 的 **子串** `sub` ，满足 `hash(sub, power, modulo) == hashValue` 。

测试数据保证一定 **存在** 至少一个这样的子串。

 **子串** 定义为一个字符串中连续非空字符组成的序列。

 

 **示例 1：** 

```
输入：s = "leetcode", power = 7, modulo = 20, k = 2, hashValue = 0
输出："ee"
解释："ee" 的哈希值为 hash("ee", 7, 20) = (5 * 1 + 5 * 7) mod 20 = 40 mod 20 = 0 。
"ee" 是长度为 2 的第一个哈希值为 0 的子串，所以我们返回 "ee" 。

```
 **示例 2：** 

```
输入：s = "fbxzaad", power = 31, modulo = 100, k = 3, hashValue = 32
输出："fbx"
解释："fbx" 的哈希值为 hash("fbx", 31, 100) = (6 * 1 + 2 * 31 + 24 * 31^2) mod 100 = 23132 mod 100 = 32 。
"bxz" 的哈希值为 hash("bxz", 31, 100) = (2 * 1 + 24 * 31 + 26 * 31^2) mod 100 = 25732 mod 100 = 32 。
"fbx" 是长度为 3 的第一个哈希值为 32 的子串，所以我们返回 "fbx" 。
注意，"bxz" 的哈希值也为 32 ，但是它在字符串中比 "fbx" 更晚出现。

```
 

 **提示：** 
-  `1 <= k <= s.length <= 2 * 10^4` 
-  `1 <= power, modulo <= 10^9` 
-  `0 <= hashValue < modulo` 
-  `s` 只包含小写英文字母。
- 测试数据保证一定 **存在** 满足条件的子串。
 
**标签**
`字符串` `滑动窗口` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 2157.字符串分组
[https://leetcode-cn.com/problems/groups-of-strings](https://leetcode-cn.com/problems/groups-of-strings) 
## 原题
给你一个下标从 **0** 开始的字符串数组 `words` 。每个字符串都只包含 **小写英文字母** 。 `words` 中任意一个子串中，每个字母都至多只出现一次。

如果通过以下操作之一，我们可以从 `s1` 的字母集合得到 `s2` 的字母集合，那么我们称这两个字符串为 **关联的** ：
- 往 `s1` 的字母集合中添加一个字母。
- 从 `s1` 的字母集合中删去一个字母。
- 将 `s1` 中的一个字母替换成另外任意一个字母（也可以替换为这个字母本身）。
数组 `words` 可以分为一个或者多个无交集的 **组** 。如果一个字符串与另一个字符串关联，那么它们应当属于同一个组。

注意，你需要确保分好组后，一个组内的任一字符串与其他组的字符串都不关联。可以证明在这个条件下，分组方案是唯一的。

请你返回一个长度为 `2` 的数组 `ans` ：
-  `ans[0]` 是 `words` 分组后的 **总组数** 。
-  `ans[1]` 是字符串数目最多的组所包含的字符串数目。
 

 **示例 1：** 

```

输入：words = ["a","b","ab","cde"]
输出：[2,3]
解释：
- words[0] 可以得到 words[1] （将 'a' 替换为 'b'）和 words[2] （添加 'b'）。所以 words[0] 与 words[1] 和 words[2] 关联。
- words[1] 可以得到 words[0] （将 'b' 替换为 'a'）和 words[2] （添加 'a'）。所以 words[1] 与 words[0] 和 words[2] 关联。
- words[2] 可以得到 words[0] （删去 'b'）和 words[1] （删去 'a'）。所以 words[2] 与 words[0] 和 words[1] 关联。
- words[3] 与 words 中其他字符串都不关联。
所以，words 可以分成 2 个组 ["a","b","ab"] 和 ["cde"] 。最大的组大小为 3 。

```
 **示例 2：** 

```

输入：words = ["a","ab","abc"]
输出：[1,3]
解释：
- words[0] 与 words[1] 关联。
- words[1] 与 words[0] 和 words[2] 关联。
- words[2] 与 words[1] 关联。
由于所有字符串与其他字符串都关联，所以它们全部在同一个组内。
所以最大的组大小为 3 。

```
 

 **提示：** 
-  `1 <= words.length <= 2 * 10^4` 
-  `1 <= words[i].length <= 26` 
-  `words[i]` 只包含小写英文字母。
-  `words[i]` 中每个字母最多只出现一次。
 
**标签**
`位运算` `并查集` `字符串` 


## 
```python

```
>
# 2160.拆分数位后四位数字的最小和
[https://leetcode-cn.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits](https://leetcode-cn.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits) 
## 原题
给你一个四位 **正** 整数 `num` 。请你使用 `num` 中的 **数位** ，将 `num` 拆成两个新的整数 `new1` 和 `new2` 。 `new1` 和 `new2` 中可以有 **前导 0** ，且 `num` 中 **所有** 数位都必须使用。
- 比方说，给你 `num = 2932` ，你拥有的数位包括：两个 `2` ，一个 `9` 和一个 `3` 。一些可能的 `[new1, new2]` 数对为 `[22, 93]` ， `[23, 92]` ， `[223, 9]` 和 `[2, 329]` 。
请你返回可以得到的 `new1` 和 `new2` 的 **最小** 和。

 

 **示例 1：** 

```
输入：num = 2932
输出：52
解释：可行的 [new1, new2] 数对为 [29, 23] ，[223, 9] 等等。
最小和为数对 [29, 23] 的和：29 + 23 = 52 。

```
 **示例 2：** 

```
输入：num = 4009
输出：13
解释：可行的 [new1, new2] 数对为 [0, 49] ，[490, 0] 等等。
最小和为数对 [4, 9] 的和：4 + 9 = 13 。

```
 

 **提示：** 
-  `1000 <= num <= 9999` 
 
**标签**
`贪心` `数学` `排序` 


## 
```python

```
>
# 2161.根据给定数字划分数组
[https://leetcode-cn.com/problems/partition-array-according-to-given-pivot](https://leetcode-cn.com/problems/partition-array-according-to-given-pivot) 
## 原题
给你一个下标从 **0** 开始的整数数组 `nums` 和一个整数 `pivot` 。请你将 `nums` 重新排列，使得以下条件均成立：
- 所有小于 `pivot` 的元素都出现在所有大于 `pivot` 的元素 **之前** 。
- 所有等于 `pivot` 的元素都出现在小于和大于 `pivot` 的元素 **中间** 。
- 小于 `pivot` 的元素之间和大于 `pivot` 的元素之间的 **相对顺序** 不发生改变。
	
- 更正式的，考虑每一对 `p<sub>i</sub>` ， `p<sub>j</sub>` ， `p<sub>i</sub>` 是初始时位置 `i` 元素的新位置， `p<sub>j</sub>` 是初始时位置 `j` 元素的新位置。对于小于 `pivot` 的元素，如果 `i < j` 且 `nums[i] < pivot` 和 `nums[j] < pivot` 都成立，那么 `p<sub>i</sub> < p<sub>j</sub>` 也成立。类似的，对于大于 `pivot` 的元素，如果 `i < j` 且 `nums[i] > pivot` 和 `nums[j] > pivot` 都成立，那么 `p<sub>i</sub> < p<sub>j</sub>` 。
	
	
请你返回重新排列 `nums` 数组后的结果数组。

 

 **示例 1：** 

```
输入：nums = [9,12,5,10,14,3,10], pivot = 10
输出：[9,5,3,10,10,12,14]
解释：
元素 9 ，5 和 3 小于 pivot ，所以它们在数组的最左边。
元素 12 和 14 大于 pivot ，所以它们在数组的最右边。
小于 pivot 的元素的相对位置和大于 pivot 的元素的相对位置分别为 [9, 5, 3] 和 [12, 14] ，它们在结果数组中的相对顺序需要保留。

```
 **示例 2：** 

```
输入：nums = [-3,4,3,2], pivot = 2
输出：[-3,2,4,3]
解释：
元素 -3 小于 pivot ，所以在数组的最左边。
元素 4 和 3 大于 pivot ，所以它们在数组的最右边。
小于 pivot 的元素的相对位置和大于 pivot 的元素的相对位置分别为 [-3] 和 [4, 3] ，它们在结果数组中的相对顺序需要保留。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-10^6 <= nums[i] <= 10^6` 
-  `pivot` 等于 `nums` 中的一个元素。
 
**标签**
`数组` `双指针` `模拟` 


## 
```python

```
>
# 2162.设置时间的最少代价
[https://leetcode-cn.com/problems/minimum-cost-to-set-cooking-time](https://leetcode-cn.com/problems/minimum-cost-to-set-cooking-time) 
## 原题
常见的微波炉可以设置加热时间，且加热时间满足以下条件：
- 至少为 `1` 秒钟。
- 至多为 `99` 分 `99` 秒。
你可以 **最多** 输入 **4 个数字** 来设置加热时间。如果你输入的位数不足 4 位，微波炉会自动加 **前缀** **0** 来补足 4 位。微波炉会将设置好的四位数中， **前** 两位当作分钟数， **后** 两位当作秒数。它们所表示的总时间就是加热时间。比方说：
- 你输入 `9` `5` `4` （三个数字），被自动补足为 `0954` ，并表示 `9` 分 `54` 秒。
- 你输入 `0` `0` `0` `8` （四个数字），表示 `0` 分 `8` 秒。
- 你输入 `8` `0` `9` `0` ，表示 `80` 分 `90` 秒。
- 你输入 `8` `1` `3` `0` ，表示 `81` 分 `30` 秒。
给你整数 `startAt` ， `moveCost` ， `pushCost` 和 `targetSeconds` 。 **一开始** ，你的手指在数字 `startAt` 处。将手指移到 **任何其他数字** ，需要花费 `moveCost` 的单位代价。 **每** 输入你手指所在位置的数字一次，需要花费 `pushCost` 的单位代价。

要设置 `targetSeconds` 秒的加热时间，可能会有多种设置方法。你想要知道这些方法中，总代价最小为多少。

请你能返回设置 `targetSeconds` 秒钟加热时间需要花费的最少代价。

请记住，虽然微波炉的秒数最多可以设置到 `99` 秒，但一分钟等于 `60` 秒。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/30/1.png" style="width: 506px; height: 210px;">

```
输入：startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600
输出：6
解释：以下为设置加热时间的所有方法。
- 1 0 0 0 ，表示 10 分 0 秒。
  手指一开始就在数字 1 处，输入 1 （代价为 1），移到 0 处（代价为 2），输入 0（代价为 1），输入 0（代价为 1），输入 0（代价为 1）。
  总代价为：1 + 2 + 1 + 1 + 1 = 6 。这是所有方案中的最小代价。
- 0 9 6 0，表示 9 分 60 秒。它也表示 600 秒。
  手指移到 0 处（代价为 2），输入 0 （代价为 1），移到 9 处（代价为 2），输入 9（代价为 1），移到 6 处（代价为 2），输入 6（代价为 1），移到 0 处（代价为 2），输入 0（代价为 1）。
  总代价为：2 + 1 + 2 + 1 + 2 + 1 + 2 + 1 = 12 。
- 9 6 0，微波炉自动补全为 0960 ，表示 9 分 60 秒。
  手指移到 9 处（代价为 2），输入 9 （代价为 1），移到 6 处（代价为 2），输入 6（代价为 1），移到 0 处（代价为 2），输入 0（代价为 1）。
  总代价为：2 + 1 + 2 + 1 + 2 + 1 = 9 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/12/30/2.png" style="width: 505px; height: 73px;">

```
输入：startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76
输出：6
解释：最优方案为输入两个数字 7 6，表示 76 秒。
手指移到 7 处（代价为 1），输入 7 （代价为 2），移到 6 处（代价为 1），输入 6（代价为 2）。总代价为：1 + 2 + 1 + 2 = 6
其他可行方案为 0076 ，076 ，0116 和 116 ，但是它们的代价都比 6 大。

```
 

 **提示：** 
-  `0 <= startAt <= 9` 
-  `1 <= moveCost, pushCost <= 10^5` 
-  `1 <= targetSeconds <= 6039` 
 
**标签**
`数学` `枚举` 


## 
```python

```
>
# 2164.对奇偶下标分别排序
[https://leetcode-cn.com/problems/sort-even-and-odd-indices-independently](https://leetcode-cn.com/problems/sort-even-and-odd-indices-independently) 
## 原题
给你一个下标从 **0** 开始的整数数组 `nums` 。根据下述规则重排 `nums` 中的值：
- 按 **非递增** 顺序排列 `nums` **奇数下标** 上的所有值。

	
- 举个例子，如果排序前 `nums = [4, ***1*** ,2, ***3*** ]` ，对奇数下标的值排序后变为 `[4, ***3*** ,2, ***1*** ]` 。奇数下标 `1` 和 `3` 的值按照非递增顺序重排。
	
	
- 按 **非递减** 顺序排列 `nums` **偶数下标** 上的所有值。
	
- 举个例子，如果排序前 `nums = [ ***4*** ,1, ***2*** ,3]` ，对偶数下标的值排序后变为 `[ ***2*** ,1, ***4*** ,3]` 。偶数下标 `0` 和 `2` 的值按照非递减顺序重排。
	
	
返回重排 `nums` 的值之后形成的数组。

 

 **示例 1：** 

```

输入：nums = [4,1,2,3]
输出：[2,3,4,1]
解释：
首先，按非递增顺序重排奇数下标（1 和 3）的值。
所以，nums 从 [4,1,2,3] 变为 [4,3,2,1] 。
然后，按非递减顺序重排偶数下标（0 和 2）的值。
所以，nums 从 [4,1,2,3] 变为 [2,3,4,1] 。
因此，重排之后形成的数组是 [2,3,4,1] 。

```
 **示例 2：** 

```

输入：nums = [2,1]
输出：[2,1]
解释：
由于只有一个奇数下标和一个偶数下标，所以不会发生重排。
形成的结果数组是 [2,1] ，和初始数组一样。 

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `1 <= nums[i] <= 100` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 2165.重排数字的最小值
[https://leetcode-cn.com/problems/smallest-value-of-the-rearranged-number](https://leetcode-cn.com/problems/smallest-value-of-the-rearranged-number) 
## 原题
给你一个整数 `num` 。 **重排** `num` 中的各位数字，使其值 **最小化** 且不含 **任何** 前导零。

返回不含前导零且值最小的重排数字。

注意，重排各位数字后， `num` 的符号不会改变。

 

 **示例 1：** 

```
输入：num = 310
输出：103
解释：310 中各位数字的可行排列有：013、031、103、130、301、310 。
不含任何前导零且值最小的重排数字是 103 。

```
 **示例 2：** 

```
输入：num = -7605
输出：-7650
解释：-7605 中各位数字的部分可行排列为：-7650、-6705、-5076、-0567。
不含任何前导零且值最小的重排数字是 -7650 。
```
 

 **提示：** 
-  `-10^15 <= num <= 10^15` 
 
**标签**
`数学` `排序` 


## 
```python

```
>
# 2166.设计位集
[https://leetcode-cn.com/problems/design-bitset](https://leetcode-cn.com/problems/design-bitset) 
## 原题
 **位集 Bitset** 是一种能以紧凑形式存储位的数据结构。

请你实现 `Bitset` 类。
-  `Bitset(int size)` 用 `size` 个位初始化 Bitset ，所有位都是 `0` 。
-  `void fix(int idx)` 将下标为 `idx` 的位上的值更新为 `1` 。如果值已经是 `1` ，则不会发生任何改变。
-  `void unfix(int idx)` 将下标为 `idx` 的位上的值更新为 `0` 。如果值已经是 `0` ，则不会发生任何改变。
-  `void flip()` 翻转 Bitset 中每一位上的值。换句话说，所有值为 `0` 的位将会变成 `1` ，反之亦然。
-  `boolean all()` 检查 Bitset 中 **每一位** 的值是否都是 `1` 。如果满足此条件，返回 `true` ；否则，返回 `false` 。
-  `boolean one()` 检查 Bitset 中 是否 **至少一位** 的值是 `1` 。如果满足此条件，返回 `true` ；否则，返回 `false` 。
-  `int count()` 返回 Bitset 中值为 1 的位的 **总数** 。
-  `String toString()` 返回 Bitset 的当前组成情况。注意，在结果字符串中，第 `i` 个下标处的字符应该与 Bitset 中的第 `i` 位一致。
 

 **示例：** 

```

输入
["Bitset", "fix", "fix", "flip", "all", "unfix", "flip", "one", "unfix", "count", "toString"]
[[5], [3], [1], [], [], [0], [], [], [0], [], []]
输出
[null, null, null, null, false, null, null, true, null, 2, "01010"]

解释
Bitset bs = new Bitset(5); // bitset = "00000".
bs.fix(3);     // 将 idx = 3 处的值更新为 1 ，此时 bitset = "00010" 。
bs.fix(1);     // 将 idx = 1 处的值更新为 1 ，此时 bitset = "01010" 。
bs.flip();     // 翻转每一位上的值，此时 bitset = "10101" 。
bs.all();      // 返回 False ，bitset 中的值不全为 1 。
bs.unfix(0);   // 将 idx = 0 处的值更新为 0 ，此时 bitset = "00101" 。
bs.flip();     // 翻转每一位上的值，此时 bitset = "11010" 。
bs.one();      // 返回 True ，至少存在一位的值为 1 。
bs.unfix(0);   // 将 idx = 0 处的值更新为 0 ，此时 bitset = "01010" 。
bs.count();    // 返回 2 ，当前有 2 位的值为 1 。
bs.toString(); // 返回 "01010" ，即 bitset 的当前组成情况。

```
 

 **提示：** 
-  `1 <= size <= 10^5` 
-  `0 <= idx <= size - 1` 
- 至多调用 `fix` 、 `unfix` 、 `flip` 、 `all` 、 `one` 、 `count` 和 `toString` 方法 **总共** `10^5` 次
- 至少调用 `all` 、 `one` 、 `count` 或 `toString` 方法一次
- 至多调用 `toString` 方法 `5` 次
 
**标签**
`设计` `数组` `哈希表` 


## 
```python

```
>
# 2167.移除所有载有违禁货物车厢所需的最少时间
[https://leetcode-cn.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods](https://leetcode-cn.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods) 
## 原题
给你一个下标从 **0** 开始的二进制字符串 `s` ，表示一个列车车厢序列。 `s[i] = '0'` 表示第 `i` 节车厢 **不** 含违禁货物，而 `s[i] = '1'` 表示第 `i` 节车厢含违禁货物。

作为列车长，你需要清理掉所有载有违禁货物的车厢。你可以不限次数执行下述三种操作中的任意一个：
- 从列车 **左** 端移除一节车厢（即移除 `s[0]` ），用去 1 单位时间。
- 从列车 **右** 端移除一节车厢（即移除 `s[s.length - 1]` ），用去 1 单位时间。
- 从列车车厢序列的 **任意位置** 移除一节车厢，用去 2 单位时间。
返回移除所有载有违禁货物车厢所需要的 **最少** 单位时间数。

注意，空的列车车厢序列视为没有车厢含违禁货物。

 

 **示例 1：** 

```

输入：s = "1100101"
输出：5
解释：
一种从序列中移除所有载有违禁货物的车厢的方法是：
- 从左端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
- 从右端移除一节车厢 1 次。所用时间是 1 。
- 移除序列中间位置载有违禁货物的车厢。所用时间是 2 。
总时间是 2 + 1 + 2 = 5 。

一种替代方法是：
- 从左端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
- 从右端移除一节车厢 3 次。所用时间是 3 * 1 = 3 。
总时间也是 2 + 3 = 5 。

5 是移除所有载有违禁货物的车厢所需要的最少单位时间数。
没有其他方法能够用更少的时间移除这些车厢。
```
 **示例 2：** 

```

输入：s = "0010"
输出：2
解释：
一种从序列中移除所有载有违禁货物的车厢的方法是：
- 从左端移除一节车厢 3 次。所用时间是 3 * 1 = 3 。
总时间是 3.

另一种从序列中移除所有载有违禁货物的车厢的方法是：
- 移除序列中间位置载有违禁货物的车厢。所用时间是 2 。
总时间是 2.

另一种从序列中移除所有载有违禁货物的车厢的方法是：
- 从右端移除一节车厢 2 次。所用时间是 2 * 1 = 2 。
总时间是 2.

2 是移除所有载有违禁货物的车厢所需要的最少单位时间数。
没有其他方法能够用更少的时间移除这些车厢。
```
 

 **提示：** 
-  `1 <= s.length <= 2 * 10^5` 
-  `s[i]` 为 `'0'` 或 `'1'` 
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 2169.得到 0 的操作数
[https://leetcode-cn.com/problems/count-operations-to-obtain-zero](https://leetcode-cn.com/problems/count-operations-to-obtain-zero) 
## 原题
给你两个 **非负** 整数 `num1` 和 `num2` 。

每一步 **操作** 中，如果 `num1 >= num2` ，你必须用 `num1` 减 `num2` ；否则，你必须用 `num2` 减 `num1` 。
- 例如， `num1 = 5` 且 `num2 = 4` ，应该用 `num1` 减 `num2` ，因此，得到 `num1 = 1` 和 `num2 = 4` 。然而，如果 `num1 = 4` 且 `num2 = 5` ，一步操作后，得到 `num1 = 4` 和 `num2 = 1` 。
返回使 `num1 = 0` 或 `num2 = 0` 的 **操作数** 。

 

 **示例 1：** 

```

输入：num1 = 2, num2 = 3
输出：3
解释：
- 操作 1 ：num1 = 2 ，num2 = 3 。由于 num1 < num2 ，num2 减 num1 得到 num1 = 2 ，num2 = 3 - 2 = 1 。
- 操作 2 ：num1 = 2 ，num2 = 1 。由于 num1 > num2 ，num1 减 num2 。
- 操作 3 ：num1 = 1 ，num2 = 1 。由于 num1 == num2 ，num1 减 num2 。
此时 num1 = 0 ，num2 = 1 。由于 num1 == 0 ，不需要再执行任何操作。
所以总操作数是 3 。

```
 **示例 2：** 

```

输入：num1 = 10, num2 = 10
输出：1
解释：
- 操作 1 ：num1 = 10 ，num2 = 10 。由于 num1 == num2 ，num1 减 num2 得到 num1 = 10 - 10 = 0 。
此时 num1 = 0 ，num2 = 10 。由于 num1 == 0 ，不需要再执行任何操作。
所以总操作数是 1 。

```
 

 **提示：** 
-  `0 <= num1, num2 <= 10^5` 
 
**标签**
`数学` `模拟` 


## 
```python

```
>
# 2172.数组的最大与和
[https://leetcode-cn.com/problems/maximum-and-sum-of-array](https://leetcode-cn.com/problems/maximum-and-sum-of-array) 
## 原题
给你一个长度为 `n` 的整数数组 `nums` 和一个整数 `numSlots` ，满足 `2 * numSlots >= n` 。总共有 `numSlots` 个篮子，编号为 `1` 到 `numSlots` 。

你需要把所有 `n` 个整数分到这些篮子中，且每个篮子 **至多** 有 2 个整数。一种分配方案的 **与和** 定义为每个数与它所在篮子编号的 **按位与运算** 结果之和。
- 比方说，将数字 `[1, 3]` 放入篮子 ** *`1`* ** 中， `[4, 6]` 放入篮子 ** *`2`* ** 中，这个方案的与和为 `(1 AND ** *1* ** ) + (3 AND ** *1* ** ) + (4 AND ***2*** ) + (6 AND ***2*** ) = 1 + 1 + 0 + 2 = 4` 。
请你返回将 `nums` 中所有数放入 `numSlots` 个篮子中的最大与和。

 

 **示例 1：** 

```
输入：nums = [1,2,3,4,5,6], numSlots = 3
输出：9
解释：一个可行的方案是 [1, 4] 放入篮子 1 中，[2, 6] 放入篮子 2 中，[3, 5] 放入篮子 3 中。
最大与和为 (1 AND 1) + (4 AND 1) + (2 AND 2) + (6 AND 2) + (3 AND 3) + (5 AND 3) = 1 + 0 + 2 + 2 + 3 + 1 = 9 。

```
 **示例 2：** 

```
输入：nums = [1,3,10,4,7,1], numSlots = 9
输出：24
解释：一个可行的方案是 [1, 1] 放入篮子 1 中，[3] 放入篮子 3 中，[4] 放入篮子 4 中，[7] 放入篮子 7 中，[10] 放入篮子 9 中。
最大与和为 (1 AND 1) + (1 AND 1) + (3 AND 3) + (4 AND 4) + (7 AND 7) + (10 AND 9) = 1 + 1 + 3 + 4 + 7 + 8 = 24 。
注意，篮子 2 ，5 ，6 和 8 是空的，这是允许的。

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= numSlots <= 9` 
-  `1 <= n <= 2 * numSlots` 
-  `1 <= nums[i] <= 15` 
 
**标签**
`位运算` `数组` `动态规划` `状态压缩` 


## 
```python

```
>
