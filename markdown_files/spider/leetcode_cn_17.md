# 1701.平均等待时间
[https://leetcode-cn.com/problems/average-waiting-time](https://leetcode-cn.com/problems/average-waiting-time) 
## 原题
有一个餐厅，只有一位厨师。你有一个顾客数组  `customers`  ，其中  `customers[i] = [arrival<sub>i</sub>, time<sub>i</sub>]`  ：
-  `arrival<sub>i</sub>`  是第  `i`  位顾客到达的时间，到达时间按 **非递减** 顺序排列。
-  `time<sub>i</sub>`  是给第 `i`  位顾客做菜需要的时间。
当一位顾客到达时，他将他的订单给厨师，厨师一旦空闲的时候就开始做这位顾客的菜。每位顾客会一直等待到厨师完成他的订单。厨师同时只能做一个人的订单。厨师会严格按照 **订单给他的顺序**  做菜。

请你返回所有顾客需要等待的 **平均 ** 时间。与标准答案误差在  `10^-5`  范围以内，都视为正确结果。

 

 **示例 1：** 

```

输入：customers = [[1,2],[2,5],[4,3]]
输出：5.00000
解释：
1) 第一位顾客在时刻 1 到达，厨师拿到他的订单并在时刻 1 立马开始做菜，并在时刻 3 完成，第一位顾客等待时间为 3 - 1 = 2 。
2) 第二位顾客在时刻 2 到达，厨师在时刻 3 开始为他做菜，并在时刻 8 完成，第二位顾客等待时间为 8 - 2 = 6 。
3) 第三位顾客在时刻 4 到达，厨师在时刻 8 开始为他做菜，并在时刻 11 完成，第三位顾客等待时间为 11 - 4 = 7 。
平均等待时间为 (2 + 6 + 7) / 3 = 5 。

```
 **示例 2：** 

```

输入：customers = [[5,2],[5,4],[10,3],[20,1]]
输出：3.25000
解释：
1) 第一位顾客在时刻 5 到达，厨师拿到他的订单并在时刻 5 立马开始做菜，并在时刻 7 完成，第一位顾客等待时间为 7 - 5 = 2 。
2) 第二位顾客在时刻 5 到达，厨师在时刻 7 开始为他做菜，并在时刻 11 完成，第二位顾客等待时间为 11 - 5 = 6 。
3) 第三位顾客在时刻 10 到达，厨师在时刻 11 开始为他做菜，并在时刻 14 完成，第三位顾客等待时间为 14 - 10 = 4 。
4) 第四位顾客在时刻 20 到达，厨师拿到他的订单并在时刻 20 立马开始做菜，并在时刻 21 完成，第四位顾客等待时间为 21 - 20 = 1 。
平均等待时间为 (2 + 6 + 4 + 1) / 4 = 3.25 。

```
 

 **提示：** 
-  `1 <= customers.length <= 10^5` 
-  `1 <= arrival<sub>i</sub>, time<sub>i</sub> <= 10^4` 
-  `arrival<sub>i </sub><= arrival<sub>i+1</sub>` 
 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 1702.修改后的最大二进制字符串
[https://leetcode-cn.com/problems/maximum-binary-string-after-change](https://leetcode-cn.com/problems/maximum-binary-string-after-change) 
## 原题
给你一个二进制字符串  `binary`  ，它仅有  `0`  或者  `1`  组成。你可以使用下面的操作任意次对它进行修改：
- 操作 1 ：如果二进制串包含子字符串  `"00"`  ，你可以用  `"10"`  将其替换。

	
- 比方说，  `" **00** 010" -> " **10** 010"` 
	
	
- 操作 2 ：如果二进制串包含子字符串  `"10"`  ，你可以用  `"01"`  将其替换。
	
- 比方说，  `"000 **10** " -> "000 **01** "` 
	
	
请你返回执行上述操作任意次以后能得到的 **最大二进制字符串**  。如果二进制字符串 `x`  对应的十进制数字大于二进制字符串 `y`  对应的十进制数字，那么我们称二进制字符串 * * `x` * * 大于二进制字符串 * * `y` * * 。

 

 **示例 1：** 

```

输入：binary = "000110"
输出："111011"
解释：一个可行的转换为：
"000110" -> "000101" 
"000101" -> "100101" 
"100101" -> "110101" 
"110101" -> "110011" 
"110011" -> "111011"

```
 **示例 2：** 

```

输入：binary = "01"
输出："01"
解释："01" 没办法进行任何转换。

```
 

 **提示：** 
-  `1 <= binary.length <= 10^5` 
-  `binary` 仅包含  `'0'` 和  `'1'` 。
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 1703.得到连续 K 个 1 的最少相邻交换次数
[https://leetcode-cn.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones](https://leetcode-cn.com/problems/minimum-adjacent-swaps-for-k-consecutive-ones) 
## 原题
给你一个整数数组  `nums`  和一个整数  `k`  。  `nums` 仅包含  `0`  和  `1`  。每一次移动，你可以选择 **相邻**  两个数字并将它们交换。

请你返回使  `nums`  中包含  `k`  个 **连续 ** `1`  的 **最少**  交换次数。

 

 **示例 1：** 

```
输入：nums = [1,0,0,1,0,1], k = 2
输出：1
解释：在第一次操作时，nums 可以变成 [1,0,0,0,1,1] 得到连续两个 1 。

```
 **示例 2：** 

```
输入：nums = [1,0,0,0,0,0,1,1], k = 3
输出：5
解释：通过 5 次操作，最左边的 1 可以移到右边直到 nums 变为 [0,0,0,0,0,1,1,1] 。

```
 **示例 3：** 

```
输入：nums = [1,1,0,1], k = 2
输出：0
解释：nums 已经有连续 2 个 1 了。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `nums[i]` 要么是  `0`  ，要么是  `1`  。
-  `1 <= k <= sum(nums)` 
 
**标签**
`贪心` `数组` `前缀和` `滑动窗口` 


## 
```python

```
>
# 1704.判断字符串的两半是否相似
[https://leetcode-cn.com/problems/determine-if-string-halves-are-alike](https://leetcode-cn.com/problems/determine-if-string-halves-are-alike) 
## 原题
给你一个偶数长度的字符串 `s` 。将其拆分成长度相同的两半，前一半为 `a` ，后一半为 `b` 。

两个字符串 **相似** 的前提是它们都含有相同数目的元音（ `'a'` ， `'e'` ， `'i'` ， `'o'` ， `'u'` ， `'A'` ， `'E'` ， `'I'` ， `'O'` ， `'U'` ）。注意， `s` 可能同时含有大写和小写字母。

如果 `a` 和 `b` 相似，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```
输入：s = "book"
输出：true
解释：a = "bo" 且 b = "ok" 。a 中有 1 个元音，b 也有 1 个元音。所以，a 和 b 相似。

```
 **示例 2：** 

```
输入：s = "textbook"
输出：false
解释：a = "text" 且 b = "book" 。a 中有 1 个元音，b 中有 2 个元音。因此，a 和 b 不相似。
注意，元音 o 在 b 中出现两次，记为 2 个。

```
 **示例 3：** 

```
输入：s = "MerryChristmas"
输出：false

```
 **示例 4：** 

```
输入：s = "AbCdEfGh"
输出：true

```
 

 **提示：** 
-  `2 <= s.length <= 1000` 
-  `s.length` 是偶数
-  `s` 由 **大写和小写** 字母组成
 
**标签**
`字符串` `计数` 


## 
```python

```
>
# 1705.吃苹果的最大数目
[https://leetcode-cn.com/problems/maximum-number-of-eaten-apples](https://leetcode-cn.com/problems/maximum-number-of-eaten-apples) 
## 原题
有一棵特殊的苹果树，一连 `n` 天，每天都可以长出若干个苹果。在第 `i` 天，树上会长出 `apples[i]` 个苹果，这些苹果将会在 `days[i]` 天后（也就是说，第 `i + days[i]` 天时）腐烂，变得无法食用。也可能有那么几天，树上不会长出新的苹果，此时用 `apples[i] == 0` 且 `days[i] == 0` 表示。

你打算每天 **最多** 吃一个苹果来保证营养均衡。注意，你可以在这 `n` 天之后继续吃苹果。

给你两个长度为 `n` 的整数数组 `days` 和 `apples` ，返回你可以吃掉的苹果的最大数目 *。* 

 

 **示例 1：** 

```
输入：apples = [1,2,3,5,2], days = [3,2,1,4,2]
输出：7
解释：你可以吃掉 7 个苹果：
- 第一天，你吃掉第一天长出来的苹果。
- 第二天，你吃掉一个第二天长出来的苹果。
- 第三天，你吃掉一个第二天长出来的苹果。过了这一天，第三天长出来的苹果就已经腐烂了。
- 第四天到第七天，你吃的都是第四天长出来的苹果。

```
 **示例 2：** 

```
输入：apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
输出：5
解释：你可以吃掉 5 个苹果：
- 第一天到第三天，你吃的都是第一天长出来的苹果。
- 第四天和第五天不吃苹果。
- 第六天和第七天，你吃的都是第六天长出来的苹果。

```
 

 **提示：** 
-  `apples.length == n` 
-  `days.length == n` 
-  `1 <= n <= 2 * 10^4` 
-  `0 <= apples[i], days[i] <= 2 * 10^4` 
- 只有在 `apples[i] = 0` 时， `days[i] = 0` 才成立
 
**标签**
`贪心` `数组` `堆（优先队列）` 


## 
```python

```
>
# 1706.球会落何处
[https://leetcode-cn.com/problems/where-will-the-ball-fall](https://leetcode-cn.com/problems/where-will-the-ball-fall) 
## 原题
用一个大小为 `m x n` 的二维网格 `grid` 表示一个箱子。你有 `n` 颗球。箱子的顶部和底部都是开着的。

箱子中的每个单元格都有一个对角线挡板，跨过单元格的两个角，可以将球导向左侧或者右侧。
- 将球导向右侧的挡板跨过左上角和右下角，在网格中用 `1` 表示。
- 将球导向左侧的挡板跨过右上角和左下角，在网格中用 `-1` 表示。
在箱子每一列的顶端各放一颗球。每颗球都可能卡在箱子里或从底部掉出来。如果球恰好卡在两块挡板之间的 "V" 形图案，或者被一块挡导向到箱子的任意一侧边上，就会卡住。

返回一个大小为 `n` 的数组 `answer` ，其中 `answer[i]` 是球放在顶部的第 `i` 列后从底部掉出来的那一列对应的下标，如果球卡在盒子里，则返回 `-1` 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/12/26/ball.jpg" style="width: 500px; height: 385px;" />** 

```

输入：grid = [[1,1,1,-1,-1],[1,1,1,-1,-1],[-1,-1,-1,1,1],[1,1,1,1,-1],[-1,-1,-1,-1,-1]]
输出：[1,-1,-1,-1,-1]
解释：示例如图：
b0 球开始放在第 0 列上，最终从箱子底部第 1 列掉出。
b1 球开始放在第 1 列上，会卡在第 2、3 列和第 1 行之间的 "V" 形里。
b2 球开始放在第 2 列上，会卡在第 2、3 列和第 0 行之间的 "V" 形里。
b3 球开始放在第 3 列上，会卡在第 2、3 列和第 0 行之间的 "V" 形里。
b4 球开始放在第 4 列上，会卡在第 2、3 列和第 1 行之间的 "V" 形里。

```
 **示例 2：** 

```

输入：grid = [[-1]]
输出：[-1]
解释：球被卡在箱子左侧边上。

```
 **示例 3：** 

```

输入：grid = [[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1],[1,1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]
输出：[0,1,2,3,4,-1]

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 100` 
-  `grid[i][j]` 为 `1` 或 `-1` 
 
**标签**
`深度优先搜索` `数组` `动态规划` `矩阵` `模拟` 


## 
```python

```
>
# 1707.与数组中元素的最大异或值
[https://leetcode-cn.com/problems/maximum-xor-with-an-element-from-array](https://leetcode-cn.com/problems/maximum-xor-with-an-element-from-array) 
## 原题
给你一个由非负整数组成的数组 `nums` 。另有一个查询数组 `queries` ，其中 `queries[i] = [x<sub>i</sub>, m<sub>i</sub>]` 。

第 `i` 个查询的答案是 `x<sub>i</sub>` 和任何 `nums` 数组中不超过 `m<sub>i</sub>` 的元素按位异或（ `XOR` ）得到的最大值。换句话说，答案是 `max(nums[j] XOR x<sub>i</sub>)` ，其中所有 `j` 均满足 `nums[j] <= m<sub>i</sub>` 。如果 `nums` 中的所有元素都大于 `m<sub>i</sub>` ，最终答案就是 `-1` 。

返回一个整数数组 `answer` 作为查询的答案，其中 `answer.length == queries.length` 且 `answer[i]` 是第 `i` 个查询的答案。

 

 **示例 1：** 

```
输入：nums = [0,1,2,3,4], queries = [[3,1],[1,3],[5,6]]
输出：[3,3,7]
解释：
1) 0 和 1 是仅有的两个不超过 1 的整数。0 XOR 3 = 3 而 1 XOR 3 = 2 。二者中的更大值是 3 。
2) 1 XOR 2 = 3.
3) 5 XOR 2 = 7.

```
 **示例 2：** 

```
输入：nums = [5,2,4,6,6,3], queries = [[12,4],[8,1],[6,3]]
输出：[15,-1,5]

```
 

 **提示：** 
-  `1 <= nums.length, queries.length <= 10^5` 
-  `queries[i].length == 2` 
-  `0 <= nums[j], x<sub>i</sub>, m<sub>i</sub> <= 10^9` 
 
**标签**
`位运算` `字典树` `数组` 


## 
```python

```
>
# 1708.长度为 K 的最大子数组
[https://leetcode-cn.com/problems/largest-subarray-length-k](https://leetcode-cn.com/problems/largest-subarray-length-k) 
## 原题

 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1709.访问日期之间最大的空档期
[https://leetcode-cn.com/problems/biggest-window-between-visits](https://leetcode-cn.com/problems/biggest-window-between-visits) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1710.卡车上的最大单元数
[https://leetcode-cn.com/problems/maximum-units-on-a-truck](https://leetcode-cn.com/problems/maximum-units-on-a-truck) 
## 原题
请你将一些箱子装在 **一辆卡车** 上。给你一个二维数组 `boxTypes` ，其中 `boxTypes[i] = [numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub>]` ：
-  `numberOfBoxes<sub>i</sub>` 是类型 `i` 的箱子的数量。
-  `numberOfUnitsPerBox<sub>i</sub>` <sub> </sub>是类型 `i`  每个箱子可以装载的单元数量。
整数 `truckSize` 表示卡车上可以装载 **箱子** 的 **最大数量** 。只要箱子数量不超过 `truckSize` ，你就可以选择任意箱子装到卡车上。

返回卡车可以装载  **单元** 的 **最大** 总数 *。* 

 

 **示例 1：** 

```

输入：boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
输出：8
解释：箱子的情况如下：
- 1 个第一类的箱子，里面含 3 个单元。
- 2 个第二类的箱子，每个里面含 2 个单元。
- 3 个第三类的箱子，每个里面含 1 个单元。
可以选择第一类和第二类的所有箱子，以及第三类的一个箱子。
单元总数 = (1 * 3) + (2 * 2) + (1 * 1) = 8
```
 **示例 2：** 

```

输入：boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
输出：91

```
 

 **提示：** 
-  `1 <= boxTypes.length <= 1000` 
-  `1 <= numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub> <= 1000` 
-  `1 <= truckSize <= 10^6` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1711.大餐计数
[https://leetcode-cn.com/problems/count-good-meals](https://leetcode-cn.com/problems/count-good-meals) 
## 原题
 **大餐** 是指 **恰好包含两道不同餐品** 的一餐，其美味程度之和等于 2 的幂。

你可以搭配 **任意** 两道餐品做一顿大餐。

给你一个整数数组 `deliciousness` ，其中 `deliciousness[i]` 是第 `i^​​​​​​​​​​` ​​​​ 道餐品的美味程度，返回你可以用数组中的餐品做出的不同 **大餐** 的数量。结果需要对 `10^9 + 7` 取余。

注意，只要餐品下标不同，就可以认为是不同的餐品，即便它们的美味程度相同。

 

 **示例 1：** 

```

输入：deliciousness = [1,3,5,7,9]
输出：4
解释：大餐的美味程度组合为 (1,3) 、(1,7) 、(3,5) 和 (7,9) 。
它们各自的美味程度之和分别为 4 、8 、8 和 16 ，都是 2 的幂。

```
 **示例 2：** 

```

输入：deliciousness = [1,1,1,3,3,3,7]
输出：15
解释：大餐的美味程度组合为 3 种 (1,1) ，9 种 (1,3) ，和 3 种 (1,7) 。
```
 

 **提示：** 
-  `1 <= deliciousness.length <= 10^5` 
-  `0 <= deliciousness[i] <= 2^20` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1712.将数组分成三个子数组的方案数
[https://leetcode-cn.com/problems/ways-to-split-array-into-three-subarrays](https://leetcode-cn.com/problems/ways-to-split-array-into-three-subarrays) 
## 原题
我们称一个分割整数数组的方案是 **好的**  ，当它满足：
- 数组被分成三个 **非空**  连续子数组，从左至右分别命名为  `left`  ，  `mid`  ，  `right`  。
-  `left`  中元素和小于等于  `mid`  中元素和， `mid`  中元素和小于等于  `right`  中元素和。
给你一个 **非负** 整数数组  `nums`  ，请你返回  **好的** 分割 `nums`  方案数目。由于答案可能会很大，请你将结果对 `10^9 + 7`  取余后返回。

 

 **示例 1：** 

```

输入：nums = [1,1,1]
输出：1
解释：唯一一种好的分割方案是将 nums 分成 [1] [1] [1] 。
```
 **示例 2：** 

```

输入：nums = [1,2,2,2,5,0]
输出：3
解释：nums 总共有 3 种好的分割方案：
[1] [2] [2,2,5,0]
[1] [2,2] [2,5,0]
[1,2] [2,2] [5,0]

```
 **示例 3：** 

```

输入：nums = [3,2,1]
输出：0
解释：没有好的分割方案。
```
 

 **提示：** 
-  `3 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^4` 
 
**标签**
`数组` `双指针` `二分查找` `前缀和` 


## 
```python

```
>
# 1713.得到子序列的最少操作次数
[https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence](https://leetcode-cn.com/problems/minimum-operations-to-make-a-subsequence) 
## 原题
给你一个数组  `target`  ，包含若干 **互不相同**  的整数，以及另一个整数数组  `arr`  ， `arr`   **可能** 包含重复元素。

每一次操作中，你可以在 `arr`  的任意位置插入任一整数。比方说，如果  `arr = [1,4,1,2]`  ，那么你可以在中间添加 `3`  得到  `[1,4, **3** ,1,2]`  。你可以在数组最开始或最后面添加整数。

请你返回 **最少**  操作次数，使得 * * `target` * * 成为  `arr`  的一个子序列。

一个数组的 **子序列**  指的是删除原数组的某些元素（可能一个元素都不删除），同时不改变其余元素的相对顺序得到的数组。比方说， `[2,7,4]`  是  `[4, **2** ,3, **7** ,2,1, **4** ]`  的子序列（加粗元素），但  `[2,4,2]`  不是子序列。

 

 **示例 1：** 

```
输入：target = [5,1,3], arr = [9,4,2,3,4]
输出：2
解释：你可以添加 5 和 1 ，使得 arr 变为 [5,9,4,1,2,3,4] ，target 为 arr 的子序列。

```
 **示例 2：** 

```
输入：target = [6,4,8,1,3,2], arr = [4,7,6,2,3,8,6,1]
输出：3

```
 

 **提示：** 
-  `1 <= target.length, arr.length <= 10^5` 
-  `1 <= target[i], arr[i] <= 10^9` 
-  `target`  不包含任何重复元素。
 
**标签**
`贪心` `数组` `哈希表` `二分查找` 


## 
```python

```
>
# 1714.数组中特殊等间距元素的和
[https://leetcode-cn.com/problems/sum-of-special-evenly-spaced-elements-in-array](https://leetcode-cn.com/problems/sum-of-special-evenly-spaced-elements-in-array) 
## 原题

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1715.苹果和橘子的个数
[https://leetcode-cn.com/problems/count-apples-and-oranges](https://leetcode-cn.com/problems/count-apples-and-oranges) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1716.计算力扣银行的钱
[https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank](https://leetcode-cn.com/problems/calculate-money-in-leetcode-bank) 
## 原题
Hercy 想要为购买第一辆车存钱。他 **每天** 都往力扣银行里存钱。

最开始，他在周一的时候存入 `1`  块钱。从周二到周日，他每天都比前一天多存入 `1`  块钱。在接下来每一个周一，他都会比 **前一个周一** 多存入 `1`  块钱。<span style=""> </span>

给你  `n`  ，请你返回在第 `n`  天结束的时候他在力扣银行总共存了多少块钱。

 

 **示例 1：** 

```
输入：n = 4
输出：10
解释：第 4 天后，总额为 1 + 2 + 3 + 4 = 10 。

```
 **示例 2：** 

```
输入：n = 10
输出：37
解释：第 10 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37 。注意到第二个星期一，Hercy 存入 2 块钱。

```
 **示例 3：** 

```
输入：n = 20
输出：96
解释：第 20 天后，总额为 (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96 。

```
 

 **提示：** 
-  `1 <= n <= 1000` 
 
**标签**
`数学` 


## 
```python

```
>
# 1717.删除子字符串的最大得分
[https://leetcode-cn.com/problems/maximum-score-from-removing-substrings](https://leetcode-cn.com/problems/maximum-score-from-removing-substrings) 
## 原题
给你一个字符串  `s`  和两个整数  `x` 和  `y`  。你可以执行下面两种操作任意次。
- 删除子字符串  `"ab"`  并得到  `x`  分。

	
- 比方说，从  `"c **ab** xbae"`  删除 `ab`  ，得到  `"cxbae"`  。
	
	
- 删除子字符串 `"ba"`  并得到  `y`  分。
	
- 比方说，从  `"cabx **ba** e"`  删除 `ba`  ，得到  `"cabxe"`  。
	
	
请返回对 `s`  字符串执行上面操作若干次能得到的最大得分。

 

 **示例 1：** 

```
输入：s = "cdbcbbaaabab", x = 4, y = 5
输出：19
解释：
- 删除 "cdbcbbaaabab" 中加粗的 "ba" ，得到 s = "cdbcbbaaab" ，加 5 分。
- 删除 "cdbcbbaaab" 中加粗的 "ab" ，得到 s = "cdbcbbaa" ，加 4 分。
- 删除 "cdbcbbaa" 中加粗的 "ba" ，得到 s = "cdbcba" ，加 5 分。
- 删除 "cdbcba" 中加粗的 "ba" ，得到 s = "cdbc" ，加 5 分。
总得分为 5 + 4 + 5 + 5 = 19 。
```
 **示例 2：** 

```
输入：s = "aabbaaxybbaabb", x = 5, y = 4
输出：20

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `1 <= x, y <= 10^4` 
-  `s`  只包含小写英文字母。
 
**标签**
`栈` `贪心` `字符串` 


## 
```python

```
>
# 1718.构建字典序最大的可行序列
[https://leetcode-cn.com/problems/construct-the-lexicographically-largest-valid-sequence](https://leetcode-cn.com/problems/construct-the-lexicographically-largest-valid-sequence) 
## 原题
给你一个整数  `n`  ，请你找到满足下面条件的一个序列：
- 整数  `1`  在序列中只出现一次。
-  `2`  到  `n`  之间每个整数都恰好出现两次。
- 对于每个  `2`  到  `n`  之间的整数  `i`  ，两个  `i`  之间出现的距离恰好为  `i`  。
序列里面两个数 `a[i]`  和 `a[j]`  之间的 **距离**  ，我们定义为它们下标绝对值之差  `|j - i|`  。

请你返回满足上述条件中  **字典序最大**  的序列。题目保证在给定限制条件下，一定存在解。

一个序列  `a`  被认为比序列  `b`  （两者长度相同）字典序更大的条件是：  `a` 和  `b`  中第一个不一样的数字处， `a`  序列的数字比  `b`  序列的数字大。比方说， `[0,1,9,0]`  比  `[0,1,5,6]`  字典序更大，因为第一个不同的位置是第三个数字，且  `9`  比  `5`  大。

 

 **示例 1：** 

```
输入：n = 3
输出：[3,1,2,3,2]
解释：[2,3,2,1,3] 也是一个可行的序列，但是 [3,1,2,3,2] 是字典序最大的序列。

```
 **示例 2：** 

```
输入：n = 5
输出：[5,3,1,4,3,5,2,4,2]

```
 

 **提示：** 
-  `1 <= n <= 20` 
 
**标签**
`数组` `回溯` 


## 
```python

```
>
# 1719.重构一棵树的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree](https://leetcode-cn.com/problems/number-of-ways-to-reconstruct-a-tree) 
## 原题
给你一个数组  `pairs` ，其中  `pairs[i] = [x<sub>i</sub>, y<sub>i</sub>]`  ，并且满足：
-  `pairs`  中没有重复元素
-  `x<sub>i</sub> < y<sub>i</sub>` 
令  `ways`  为满足下面条件的有根树的方案数：
- 树所包含的所有节点值都在 `pairs`  中。
- 一个数对  `[x<sub>i</sub>, y<sub>i</sub>]` 出现在  `pairs`  中  **当且仅当** ** ** `x<sub>i</sub>`  是  `y<sub>i</sub>`  的祖先或者  `y<sub>i</sub>`  是  `x<sub>i</sub>` <sub> </sub>的祖先。
-  **注意：** 构造出来的树不一定是二叉树。
两棵树被视为不同的方案当存在至少一个节点在两棵树中有不同的父节点。

请你返回：
- 如果  `ways == 0`  ，返回  `0`  。
- 如果  `ways == 1`  ，返回 `1`  。
- 如果  `ways > 1`  ，返回  `2`  。
一棵 **有根树**  指的是只有一个根节点的树，所有边都是从根往外的方向。

我们称从根到一个节点路径上的任意一个节点（除去节点本身）都是该节点的 **祖先**  。根节点没有祖先。

 

 **示例 1：** 
<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/09/trees2.png" style="width: 208px; height: 221px;" />
```

输入：pairs = [[1,2],[2,3]]
输出：1
解释：如上图所示，有且只有一个符合规定的有根树。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/09/tree.png" style="width: 234px; height: 241px;" />
```

输入：pairs = [[1,2],[2,3],[1,3]]
输出：2
解释：有多个符合规定的有根树，其中三个如上图所示。

```
 **示例 3：** 

```

输入：pairs = [[1,2],[2,3],[2,4],[1,5]]
输出：0
解释：没有符合规定的有根树。
```
 

 **提示：** 
-  `1 <= pairs.length <= 10^5` 
-  `1 <= x<sub>i </sub>< y<sub>i</sub> <= 500` 
-  `pairs`  中的元素互不相同。
 
**标签**
`树` `图` `拓扑排序` 


## 
```python

```
>
# 1720.解码异或后的数组
[https://leetcode-cn.com/problems/decode-xored-array](https://leetcode-cn.com/problems/decode-xored-array) 
## 原题
 **未知** 整数数组 `arr` 由 `n` 个非负整数组成。

经编码后变为长度为 `n - 1` 的另一个整数数组 `encoded` ，其中 `encoded[i] = arr[i] XOR arr[i + 1]` 。例如， `arr = [1,0,2,1]` 经编码后得到 `encoded = [1,2,3]` 。

给你编码后的数组 `encoded` 和原数组 `arr` 的第一个元素 `first` （ `arr[0]` ）。

请解码返回原数组 `arr` 。可以证明答案存在并且是唯一的。

 

 **示例 1：** 

```

输入：encoded = [1,2,3], first = 1
输出：[1,0,2,1]
解释：若 arr = [1,0,2,1] ，那么 first = 1 且 encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]

```
 **示例 2：** 

```

输入：encoded = [6,2,7,3], first = 4
输出：[4,2,0,7,4]

```
 

 **提示：** 
-  `2 <= n <= 10^4` 
-  `encoded.length == n - 1` 
-  `0 <= encoded[i] <= 10^5` 
-  `0 <= first <= 10^5` 
 
**标签**
`位运算` `数组` 


## 
```python

```
>
# 1721.交换链表中的节点
[https://leetcode-cn.com/problems/swapping-nodes-in-a-linked-list](https://leetcode-cn.com/problems/swapping-nodes-in-a-linked-list) 
## 原题
给你链表的头节点 `head` 和一个整数 `k` 。

 **交换** 链表正数第 `k` 个节点和倒数第 `k` 个节点的值后，返回链表的头节点（链表 **从 1 开始索引** ）。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/10/linked1.jpg" style="width: 722px; height: 202px;" />
```

输入：head = [1,2,3,4,5], k = 2
输出：[1,4,3,2,5]

```
 **示例 2：** 

```

输入：head = [7,9,6,6,7,8,3,0,9,5], k = 5
输出：[7,9,6,6,8,7,3,0,9,5]

```
 **示例 3：** 

```

输入：head = [1], k = 1
输出：[1]

```
 **示例 4：** 

```

输入：head = [1,2], k = 1
输出：[2,1]

```
 **示例 5：** 

```

输入：head = [1,2,3], k = 2
输出：[1,2,3]

```
 

 **提示：** 
- 链表中节点的数目是 `n` 
-  `1 <= k <= n <= 10^5` 
-  `0 <= Node.val <= 100` 
 
**标签**
`链表` `双指针` 


## 
```python

```
>
# 1722.执行交换操作后的最小汉明距离
[https://leetcode-cn.com/problems/minimize-hamming-distance-after-swap-operations](https://leetcode-cn.com/problems/minimize-hamming-distance-after-swap-operations) 
## 原题
给你两个整数数组 `source` 和 `target` ，长度都是 `n` 。还有一个数组 `allowedSwaps` ，其中每个 `allowedSwaps[i] = [a<sub>i</sub>, b<sub>i</sub>]` 表示你可以交换数组 `source` 中下标为 `a<sub>i</sub>` 和 `b<sub>i</sub>` （ **下标从 0 开始** ）的两个元素。注意，你可以按 **任意** 顺序 **多次** 交换一对特定下标指向的元素。

相同长度的两个数组  `source` 和 `target` 间的 **汉明距离** 是元素不同的下标数量。形式上，其值等于满足  `source[i] != target[i]` （ **下标从 0 开始** ）的下标 `i` （ `0 <= i <= n-1` ）的数量。

在对数组 `source` 执行 **任意** 数量的交换操作后，返回 `source` 和 `target` 间的 **最小汉明距离** 。

 

 **示例 1：** 

```
输入：source = [1,2,3,4], target = [2,1,4,5], allowedSwaps = [[0,1],[2,3]]
输出：1
解释：source 可以按下述方式转换：
- 交换下标 0 和 1 指向的元素：source = [2,1,3,4]
- 交换下标 2 和 3 指向的元素：source = [2,1,4,3]
source 和 target 间的汉明距离是 1 ，二者有 1 处元素不同，在下标 3 。

```
 **示例 2：** 

```
输入：source = [1,2,3,4], target = [1,3,2,4], allowedSwaps = []
输出：2
解释：不能对 source 执行交换操作。
source 和 target 间的汉明距离是 2 ，二者有 2 处元素不同，在下标 1 和下标 2 。
```
 **示例 3：** 

```
输入：source = [5,1,2,4,3], target = [1,5,4,2,3], allowedSwaps = [[0,4],[4,2],[1,3],[1,4]]
输出：0

```
 

 **提示：** 
-  `n == source.length == target.length` 
-  `1 <= n <= 10^5` 
-  `1 <= source[i], target[i] <= 10^5` 
-  `0 <= allowedSwaps.length <= 10^5` 
-  `allowedSwaps[i].length == 2` 
-  `0 <= a<sub>i</sub>, b<sub>i</sub> <= n - 1` 
-  `a<sub>i</sub> != b<sub>i</sub>` 
 
**标签**
`深度优先搜索` `并查集` `数组` 


## 
```python

```
>
# 1723.完成所有工作的最短时间
[https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs](https://leetcode-cn.com/problems/find-minimum-time-to-finish-all-jobs) 
## 原题
给你一个整数数组 `jobs` ，其中 `jobs[i]` 是完成第 `i` 项工作要花费的时间。

请你将这些工作分配给 `k` 位工人。所有工作都应该分配给工人，且每项工作只能分配给一位工人。工人的 **工作时间** 是完成分配给他们的所有工作花费时间的总和。请你设计一套最佳的工作分配方案，使工人的 **最大工作时间** 得以 **最小化** 。

返回分配方案中尽可能 **最小** 的 **最大工作时间** 。

 

 **示例 1：** 

```

输入：jobs = [3,2,3], k = 3
输出：3
解释：给每位工人分配一项工作，最大工作时间是 3 。

```
 **示例 2：** 

```

输入：jobs = [1,2,4,7,8], k = 2
输出：11
解释：按下述方式分配工作：
1 号工人：1、2、8（工作时间 = 1 + 2 + 8 = 11）
2 号工人：4、7（工作时间 = 4 + 7 = 11）
最大工作时间是 11 。
```
 

 **提示：** 
-  `1 <= k <= jobs.length <= 12` 
-  `1 <= jobs[i] <= 10^7` 
 
**标签**
`位运算` `数组` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 1724.检查边长度限制的路径是否存在 II
[https://leetcode-cn.com/problems/checking-existence-of-edge-length-limited-paths-ii](https://leetcode-cn.com/problems/checking-existence-of-edge-length-limited-paths-ii) 
## 原题

 
**标签**
`并查集` `图` `最小生成树` 


## 
```python

```
>
# 1725.可以形成最大正方形的矩形数目
[https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square](https://leetcode-cn.com/problems/number-of-rectangles-that-can-form-the-largest-square) 
## 原题
给你一个数组 `rectangles` ，其中 `rectangles[i] = [l<sub>i</sub>, w<sub>i</sub>]` 表示第 `i` 个矩形的长度为 `l<sub>i</sub>` 、宽度为 `w<sub>i</sub>` 。

如果存在 `k` 同时满足 `k <= l<sub>i</sub>` 和 `k <= w<sub>i</sub>` ，就可以将第 `i` 个矩形切成边长为 `k` 的正方形。例如，矩形 `[4,6]` 可以切成边长最大为 `4` 的正方形。

设 `maxLen` 为可以从矩形数组  `rectangles` 切分得到的 **最大正方形** 的边长。

请你统计有多少个矩形能够切出边长为 `maxLen` 的正方形，并返回矩形 **数目** 。

 

 **示例 1：** 

```

输入：rectangles = [[5,8],[3,9],[5,12],[16,5]]
输出：3
解释：能从每个矩形中切出的最大正方形边长分别是 [5,3,5,5] 。
最大正方形的边长为 5 ，可以由 3 个矩形切分得到。

```
 **示例 2：** 

```

输入：rectangles = [[2,3],[3,7],[4,3],[3,7]]
输出：3

```
 

 **提示：** 
-  `1 <= rectangles.length <= 1000` 
-  `rectangles[i].length == 2` 
-  `1 <= l<sub>i</sub>, w<sub>i</sub> <= 10^9` 
-  `l<sub>i</sub> != w<sub>i</sub>` 
 
**标签**
`数组` 


## 
```python

```
>
# 1726.同积元组
[https://leetcode-cn.com/problems/tuple-with-same-product](https://leetcode-cn.com/problems/tuple-with-same-product) 
## 原题
给你一个由 **不同** 正整数组成的数组 `nums` ，请你返回满足  `a * b = c * d` 的元组 `(a, b, c, d)` 的数量。其中 `a` 、 `b` 、 `c` 和 `d` 都是 `nums` 中的元素，且 `a != b != c != d` 。

 

 **示例 1：** 

```

输入：nums = [2,3,4,6]
输出：8
解释：存在 8 个满足题意的元组：
(2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
(3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)

```
 **示例 2：** 

```

输入：nums = [1,2,4,5,10]
输出：16
解释：存在 16 个满足题意的元组：
(1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
(2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
(2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,4,5)
(4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)

```
 **示例 3：** 

```

输入：nums = [2,3,4,6,8,12]
输出：40

```
 **示例 4：** 

```

输入：nums = [2,3,5,7]
输出：0

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `1 <= nums[i] <= 10^4` 
-  `nums` 中的所有元素 **互不相同** 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1727.重新排列后的最大子矩阵
[https://leetcode-cn.com/problems/largest-submatrix-with-rearrangements](https://leetcode-cn.com/problems/largest-submatrix-with-rearrangements) 
## 原题
给你一个二进制矩阵  `matrix`  ，它的大小为  `m x n`  ，你可以将 `matrix`  中的 **列**  按任意顺序重新排列。

请你返回最优方案下将 `matrix`  重新排列后，全是 `1`  的子矩阵面积。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/17/screenshot-2020-12-30-at-40536-pm.png" style="width: 300px; height: 144px;" />** 

```

输入：matrix = [[0,0,1],[1,1,1],[1,0,1]]
输出：4
解释：你可以按照上图方式重新排列矩阵的每一列。
最大的全 1 子矩阵是上图中加粗的部分，面积为 4 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/17/screenshot-2020-12-30-at-40852-pm.png" style="width: 500px; height: 62px;" />

```

输入：matrix = [[1,0,1,0,1]]
输出：3
解释：你可以按照上图方式重新排列矩阵的每一列。
最大的全 1 子矩阵是上图中加粗的部分，面积为 3 。

```
 **示例 3：** 

```

输入：matrix = [[1,1,0],[1,0,1]]
输出：2
解释：由于你只能整列整列重新排布，所以没有比面积为 2 更大的全 1 子矩形。
```
 **示例 4：** 

```

输入：matrix = [[0,0],[0,0]]
输出：0
解释：由于矩阵中没有 1 ，没有任何全 1 的子矩阵，所以面积为 0 。
```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m * n <= 10^5` 
-  `matrix[i][j]`  要么是  `0`  ，要么是  `1` 。
 
**标签**
`贪心` `数组` `矩阵` `排序` 


## 
```python

```
>
# 1728.猫和老鼠 II
[https://leetcode-cn.com/problems/cat-and-mouse-ii](https://leetcode-cn.com/problems/cat-and-mouse-ii) 
## 原题
一只猫和一只老鼠在玩一个叫做猫和老鼠的游戏。

它们所处的环境设定是一个  `rows x cols`  的方格 `grid`  ，其中每个格子可能是一堵墙、一块地板、一位玩家（猫或者老鼠）或者食物。
- 玩家由字符  `'C'`  （代表猫）和  `'M'`  （代表老鼠）表示。
- 地板由字符  `'.'`  表示，玩家可以通过这个格子。
- 墙用字符  `'#'`  表示，玩家不能通过这个格子。
- 食物用字符  `'F'`  表示，玩家可以通过这个格子。
- 字符  `'C'`  ，  `'M'`  和  `'F'`  在  `grid`  中都只会出现一次。
猫和老鼠按照如下规则移动：
- 老鼠 **先移动**  ，然后两名玩家轮流移动。
- 每一次操作时，猫和老鼠可以跳到上下左右四个方向之一的格子，他们不能跳过墙也不能跳出  `grid`  。
-  `catJump` 和  `mouseJump`  是猫和老鼠分别跳一次能到达的最远距离，它们也可以跳小于最大距离的长度。
- 它们可以停留在原地。
- 老鼠可以跳跃过猫的位置。
游戏有 4 种方式会结束：
- 如果猫跟老鼠处在相同的位置，那么猫获胜。
- 如果猫先到达食物，那么猫获胜。
- 如果老鼠先到达食物，那么老鼠获胜。
- 如果老鼠不能在 1000 次操作以内到达食物，那么猫获胜。
给你  `rows x cols`  的矩阵  `grid`  和两个整数  `catJump`  和  `mouseJump`  ，双方都采取最优策略，如果老鼠获胜，那么请你返回  `true`  ，否则返回 `false`  。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/17/sample_111_1955.png" style="width: 580px; height: 239px;" />** 

```

输入：grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
输出：true
解释：猫无法抓到老鼠，也没法比老鼠先到达食物。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/17/sample_2_1955.png" style="width: 580px; height: 175px;" />

```

输入：grid = ["M.C...F"], catJump = 1, mouseJump = 4
输出：true

```
 **示例 3：** 

```

输入：grid = ["M.C...F"], catJump = 1, mouseJump = 3
输出：false

```
 **示例 4：** 

```

输入：grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
输出：false

```
 **示例 5：** 

```

输入：grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1
输出：true

```
 

 **提示：** 
-  `rows == grid.length` 
-  `cols = grid[i].length` 
-  `1 <= rows, cols <= 8` 
-  `grid[i][j]` 只包含字符  `'C'`  ， `'M'`  ， `'F'`  ， `'.'`  和  `'#'`  。
-  `grid`  中只包含一个  `'C'`  ， `'M'`  和  `'F'`  。
-  `1 <= catJump, mouseJump <= 8` 
 
**标签**
`广度优先搜索` `图` `记忆化搜索` `数学` `动态规划` `博弈` 


## 
```python

```
>
# 1729.求关注者的数量
[https://leetcode-cn.com/problems/find-followers-count](https://leetcode-cn.com/problems/find-followers-count) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1730.获取食物的最短路径
[https://leetcode-cn.com/problems/shortest-path-to-get-food](https://leetcode-cn.com/problems/shortest-path-to-get-food) 
## 原题

 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 1731.每位经理的下属员工数量
[https://leetcode-cn.com/problems/the-number-of-employees-which-report-to-each-employee](https://leetcode-cn.com/problems/the-number-of-employees-which-report-to-each-employee) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1732.找到最高海拔
[https://leetcode-cn.com/problems/find-the-highest-altitude](https://leetcode-cn.com/problems/find-the-highest-altitude) 
## 原题
有一个自行车手打算进行一场公路骑行，这条路线总共由  `n + 1`  个不同海拔的点组成。自行车手从海拔为 `0`  的点  `0`  开始骑行。

给你一个长度为 `n`  的整数数组  `gain`  ，其中 `gain[i]`  是点 `i`  和点 `i + 1`  的 **净海拔高度差** （ `0 <= i < n` ）。请你返回 **最高点的海拔** 。

 

 **示例 1：** 

```

输入：gain = [-5,1,5,0,-7]
输出：1
解释：海拔高度依次为 [0,-5,-4,1,1,-6] 。最高海拔为 1 。

```
 **示例 2：** 

```

输入：gain = [-4,-3,-2,-1,4,3,2]
输出：0
解释：海拔高度依次为 [0,-4,-7,-9,-10,-6,-3,-1] 。最高海拔为 0 。

```
 

 **提示：** 
-  `n == gain.length` 
-  `1 <= n <= 100` 
-  `-100 <= gain[i] <= 100` 
 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 1733.需要教语言的最少人数
[https://leetcode-cn.com/problems/minimum-number-of-people-to-teach](https://leetcode-cn.com/problems/minimum-number-of-people-to-teach) 
## 原题
在一个由  `m`  个用户组成的社交网络里，我们获取到一些用户之间的好友关系。两个用户之间可以相互沟通的条件是他们都掌握同一门语言。

给你一个整数  `n`  ，数组  `languages`  和数组  `friendships`  ，它们的含义如下：
- 总共有  `n`  种语言，编号从  `1` 到  `n`  。
-  `languages[i]`  是第 `i`  位用户掌握的语言集合。
-  `friendships[i] = [u<sub>​​​​​​i</sub>​​​, v<sub>​​​​​​i</sub>]`  表示  `u^​​​​​<sub>​​​​​​i</sub>` ​​​​​ 和  `v<sub>i</sub>`  为好友关系。
你可以选择 **一门**  语言并教会一些用户，使得所有好友之间都可以相互沟通。请返回你 **最少**  需要教会多少名用户。
请注意，好友关系没有传递性，也就是说如果  `x` 和  `y`  是好友，且  `y`  和  `z`  是好友，  `x` 和  `z`  不一定是好友。

 

 **示例 1：** 

```

输入：n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
输出：1
解释：你可以选择教用户 1 第二门语言，也可以选择教用户 2 第一门语言。

```
 **示例 2：** 

```

输入：n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
输出：2
解释：教用户 1 和用户 3 第三门语言，需要教 2 名用户。

```
 

 **提示：** 
-  `2 <= n <= 500` 
-  `languages.length == m` 
-  `1 <= m <= 500` 
-  `1 <= languages[i].length <= n` 
-  `1 <= languages[i][j] <= n` 
-  `1 <= u<sub>​​​​​​i</sub> < v<sub>​​​​​​i</sub> <= languages.length` 
-  `1 <= friendships.length <= 500` 
- 所有的好友关系  `(u<sub>​​​​​i, </sub>v<sub>​​​​​​i</sub>)`  都是唯一的。
-  `languages[i]`  中包含的值互不相同。
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1734.解码异或后的排列
[https://leetcode-cn.com/problems/decode-xored-permutation](https://leetcode-cn.com/problems/decode-xored-permutation) 
## 原题
给你一个整数数组  `perm`  ，它是前  `n`  个正整数的排列，且  `n`  是个 **奇数**  。

它被加密成另一个长度为 `n - 1`  的整数数组  `encoded`  ，满足  `encoded[i] = perm[i] XOR perm[i + 1]`  。比方说，如果  `perm = [1,3,2]`  ，那么  `encoded = [2,1]`  。

给你  `encoded`  数组，请你返回原始数组  `perm`  。题目保证答案存在且唯一。

 

 **示例 1：** 

```
输入：encoded = [3,1]
输出：[1,2,3]
解释：如果 perm = [1,2,3] ，那么 encoded = [1 XOR 2,2 XOR 3] = [3,1]

```
 **示例 2：** 

```
输入：encoded = [6,5,4,6]
输出：[2,4,1,5,3]

```
 

 **提示：** 
-  `3 <= n < 10^5` 
-  `n`  是奇数。
-  `encoded.length == n - 1` 
 
**标签**
`位运算` `数组` 


## 
```python

```
>
# 1735.生成乘积数组的方案数
[https://leetcode-cn.com/problems/count-ways-to-make-array-with-product](https://leetcode-cn.com/problems/count-ways-to-make-array-with-product) 
## 原题
给你一个二维整数数组  `queries`  ，其中 `queries[i] = [n<sub>i</sub>, k<sub>i</sub>]` 。第  `i`  个查询  `queries[i]` 要求构造长度为  `n<sub>i</sub>` 、每个元素都是正整数的数组，且满足所有元素的乘积为  `k<sub>i</sub>` <sub> </sub>，请你找出有多少种可行的方案。由于答案可能会很大，方案数需要对 `10^9 + 7`   **取余** 。

请你返回一个整数数组 * * `answer` ，满足 * * `answer.length == queries.length`  ，其中 * * `answer[i]` 是第 * * `i`  个查询的结果。

 

 **示例 1：** 

```

输入：queries = [[2,6],[5,1],[73,660]]
输出：[4,1,50734910]
解释：每个查询之间彼此独立。
[2,6]：总共有 4 种方案得到长度为 2 且乘积为 6 的数组：[1,6]，[2,3]，[3,2]，[6,1]。
[5,1]：总共有 1 种方案得到长度为 5 且乘积为 1 的数组：[1,1,1,1,1]。
[73,660]：总共有 1050734917 种方案得到长度为 73 且乘积为 660 的数组。1050734917 对 10^9 + 7 取余得到 50734910 。

```
 **示例 2 ：** 

```

输入：queries = [[1,1],[2,2],[3,3],[4,4],[5,5]]
输出：[1,2,3,10,5]

```
 

 **提示：** 
-  `1 <= queries.length <= 10^4` 
-  `1 <= n<sub>i</sub>, k<sub>i</sub> <= 10^4` 
 
**标签**
`数组` `数学` `动态规划` 


## 
```python

```
>
# 1736.替换隐藏数字得到的最晚时间
[https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits](https://leetcode-cn.com/problems/latest-time-by-replacing-hidden-digits) 
## 原题
给你一个字符串 `time` ，格式为 `hh:mm` （小时：分钟），其中某几位数字被隐藏（用 `?` 表示）。

有效的时间为 `00:00` 到 `23:59` 之间的所有时间，包括 `00:00` 和 `23:59` 。

替换  `time` 中隐藏的数字，返回你可以得到的最晚有效时间。

 

 **示例 1：** 

```

输入：time = "2?:?0"
输出："23:50"
解释：以数字 '2' 开头的最晚一小时是 23 ，以 '0' 结尾的最晚一分钟是 50 。

```
 **示例 2：** 

```

输入：time = "0?:3?"
输出："09:39"

```
 **示例 3：** 

```

输入：time = "1?:22"
输出："19:22"

```
 

 **提示：** 
-  `time` 的格式为 `hh:mm` 
- 题目数据保证你可以由输入的字符串生成有效的时间
 
**标签**
`字符串` 


## 
```python

```
>
# 1737.满足三条件之一需改变的最少字符数
[https://leetcode-cn.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions](https://leetcode-cn.com/problems/change-minimum-characters-to-satisfy-one-of-three-conditions) 
## 原题
给你两个字符串 `a` 和 `b` ，二者均由小写字母组成。一步操作中，你可以将 `a` 或 `b` 中的 **任一字符** 改变为 **任一小写字母** 。

操作的最终目标是满足下列三个条件 **之一** ：
-  `a` 中的 **每个字母** 在字母表中 **严格小于** `b` 中的 **每个字母** 。
-  `b` 中的 **每个字母** 在字母表中 **严格小于** `a` 中的 **每个字母** 。
-  `a` 和 `b` **都** 由 **同一个** 字母组成。
返回达成目标所需的 **最少** 操作数 *。* 

 

 **示例 1：** 

```
输入：a = "aba", b = "caa"
输出：2
解释：满足每个条件的最佳方案分别是：
1) 将 b 变为 "ccc"，2 次操作，满足 a 中的每个字母都小于 b 中的每个字母；
2) 将 a 变为 "bbb" 并将 b 变为 "aaa"，3 次操作，满足 b 中的每个字母都小于 a 中的每个字母；
3) 将 a 变为 "aaa" 并将 b 变为 "aaa"，2 次操作，满足 a 和 b 由同一个字母组成。
最佳的方案只需要 2 次操作（满足条件 1 或者条件 3）。

```
 **示例 2：** 

```
输入：a = "dabadd", b = "cda"
输出：3
解释：满足条件 1 的最佳方案是将 b 变为 "eee" 。

```
 

 **提示：** 
-  `1 <= a.length, b.length <= 10^5` 
-  `a` 和 `b` 只由小写字母组成
 
**标签**
`哈希表` `字符串` `计数` `前缀和` 


## 
```python

```
>
# 1738.找出第 K 大的异或坐标值
[https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value](https://leetcode-cn.com/problems/find-kth-largest-xor-coordinate-value) 
## 原题
给你一个二维矩阵 `matrix` 和一个整数 `k` ，矩阵大小为  `m x n` 由非负整数组成。

矩阵中坐标 `(a, b)` 的 **值** 可由对所有满足 `0 <= i <= a < m` 且 `0 <= j <= b < n` 的元素 `matrix[i][j]` （ **下标从 0 开始计数** ）执行异或运算得到。

请你找出  `matrix` 的所有坐标中第 `k` 大的值（ ** `k` 的值从 1 开始计数** ）。

 

 **示例 1：** 

```
输入：matrix = [[5,2],[1,6]], k = 1
输出：7
解释：坐标 (0,1) 的值是 5 XOR 2 = 7 ，为最大的值。
```
 **示例 2：** 

```
输入：matrix = [[5,2],[1,6]], k = 2
输出：5
解释：坐标 (0,0) 的值是 5 = 5 ，为第 2 大的值。
```
 **示例 3：** 

```
输入：matrix = [[5,2],[1,6]], k = 3
输出：4
解释：坐标 (1,0) 的值是 5 XOR 1 = 4 ，为第 3 大的值。
```
 **示例 4：** 

```
输入：matrix = [[5,2],[1,6]], k = 4
输出：0
解释：坐标 (1,1) 的值是 5 XOR 2 XOR 1 XOR 6 = 0 ，为第 4 大的值。
```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m, n <= 1000` 
-  `0 <= matrix[i][j] <= 10^6` 
-  `1 <= k <= m * n` 
 
**标签**
`位运算` `数组` `分治` `矩阵` `前缀和` `快速选择` `堆（优先队列）` 


## 
```python

```
>
# 1739.放置盒子
[https://leetcode-cn.com/problems/building-boxes](https://leetcode-cn.com/problems/building-boxes) 
## 原题
有一个立方体房间，其长度、宽度和高度都等于 `n` 个单位。请你在房间里放置 `n` 个盒子，每个盒子都是一个单位边长的立方体。放置规则如下：
- 你可以把盒子放在地板上的任何地方。
- 如果盒子 `x` 需要放置在盒子 `y` 的顶部，那么盒子 `y` 竖直的四个侧面都 **必须** 与另一个盒子或墙相邻。
给你一个整数 `n` ，返回接触地面的盒子的 **最少** 可能数量 *。* 

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/24/3-boxes.png" style="width: 135px; height: 143px;" />

```

输入：n = 3
输出：3
解释：上图是 3 个盒子的摆放位置。
这些盒子放在房间的一角，对应左侧位置。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/24/4-boxes.png" style="width: 135px; height: 179px;" />

```

输入：n = 4
输出：3
解释：上图是 3 个盒子的摆放位置。
这些盒子放在房间的一角，对应左侧位置。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/24/10-boxes.png" style="width: 271px; height: 257px;" />

```

输入：n = 10
输出：6
解释：上图是 10 个盒子的摆放位置。
这些盒子放在房间的一角，对应后方位置。
```
 

 **提示：** 
-  `1 <= n <= 10^9` 
 
**标签**
`贪心` `数学` `二分查找` 


## 
```python

```
>
# 1740.找到二叉树中的距离
[https://leetcode-cn.com/problems/find-distance-in-a-binary-tree](https://leetcode-cn.com/problems/find-distance-in-a-binary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `哈希表` `二叉树` 


## 
```python

```
>
# 1741.查找每个员工花费的总时间
[https://leetcode-cn.com/problems/find-total-time-spent-by-each-employee](https://leetcode-cn.com/problems/find-total-time-spent-by-each-employee) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1742.盒子中小球的最大数量
[https://leetcode-cn.com/problems/maximum-number-of-balls-in-a-box](https://leetcode-cn.com/problems/maximum-number-of-balls-in-a-box) 
## 原题
你在一家生产小球的玩具厂工作，有 `n` 个小球，编号从 `lowLimit` 开始，到 `highLimit` 结束（包括 `lowLimit` 和  `highLimit` ，即  `n == highLimit - lowLimit + 1` ）。另有无限数量的盒子，编号从 `1` 到 `infinity` 。

你的工作是将每个小球放入盒子中，其中盒子的编号应当等于小球编号上每位数字的和。例如，编号 `321` 的小球应当放入编号 `3 + 2 + 1 = 6` 的盒子，而编号 `10` 的小球应当放入编号 `1 + 0 = 1` 的盒子。

给你两个整数 `lowLimit` 和 `highLimit` ，返回放有最多小球的盒子中的小球数量 *。* 如果有多个盒子都满足放有最多小球，只需返回其中任一盒子的小球数量。

 

 **示例 1：** 

```

输入：lowLimit = 1, highLimit = 10
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
小球数量：2 1 1 1 1 1 1 1 1 0  0  ...
编号 1 的盒子放有最多小球，小球数量为 2 。
```
 **示例 2：** 

```

输入：lowLimit = 5, highLimit = 15
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 ...
小球数量：1 1 1 1 2 2 1 1 1 0  0  ...
编号 5 和 6 的盒子放有最多小球，每个盒子中的小球数量都是 2 。

```
 **示例 3：** 

```

输入：lowLimit = 19, highLimit = 28
输出：2
解释：
盒子编号：1 2 3 4 5 6 7 8 9 10 11 12 ...
小球数量：0 1 1 1 1 1 1 1 1 2  0  0  ...
编号 10 的盒子放有最多小球，小球数量为 2 。

```
 

 **提示：** 
-  `1 <= lowLimit <= highLimit <= 10^5` 
 
**标签**
`哈希表` `数学` `计数` 


## 
```python

```
>
# 1743.从相邻元素对还原数组
[https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs](https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs) 
## 原题
存在一个由 `n` 个不同元素组成的整数数组 `nums` ，但你已经记不清具体内容。好在你还记得 `nums` 中的每一对相邻元素。

给你一个二维整数数组 `adjacentPairs` ，大小为 `n - 1` ，其中每个 `adjacentPairs[i] = [u<sub>i</sub>, v<sub>i</sub>]` 表示元素 `u<sub>i</sub>` 和 `v<sub>i</sub>` 在 `nums` 中相邻。

题目数据保证所有由元素 `nums[i]` 和 `nums[i+1]` 组成的相邻元素对都存在于 `adjacentPairs` 中，存在形式可能是 `[nums[i], nums[i+1]]` ，也可能是 `[nums[i+1], nums[i]]` 。这些相邻元素对可以 **按任意顺序** 出现。

返回 **原始数组**  `nums` 。如果存在多种解答，返回 **其中任意一个** 即可。

 

 **示例 1：** 

```

输入：adjacentPairs = [[2,1],[3,4],[3,2]]
输出：[1,2,3,4]
解释：数组的所有相邻元素对都在 adjacentPairs 中。
特别要注意的是，adjacentPairs[i] 只表示两个元素相邻，并不保证其 左-右 顺序。

```
 **示例 2：** 

```

输入：adjacentPairs = [[4,-2],[1,4],[-3,1]]
输出：[-2,4,1,-3]
解释：数组中可能存在负数。
另一种解答是 [-3,1,4,-2] ，也会被视作正确答案。

```
 **示例 3：** 

```

输入：adjacentPairs = [[100000,-100000]]
输出：[100000,-100000]

```
 

 **提示：** 
-  `nums.length == n` 
-  `adjacentPairs.length == n - 1` 
-  `adjacentPairs[i].length == 2` 
-  `2 <= n <= 10^5` 
-  `-10^5 <= nums[i], u<sub>i</sub>, v<sub>i</sub> <= 10^5` 
- 题目数据保证存在一些以  `adjacentPairs` 作为元素对的数组 `nums` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1744.你能在你最喜欢的那天吃到你最喜欢的糖果吗？
[https://leetcode-cn.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day](https://leetcode-cn.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day) 
## 原题
给你一个下标从 **0** 开始的正整数数组  `candiesCount`  ，其中  `candiesCount[i]`  表示你拥有的第  `i`  类糖果的数目。同时给你一个二维数组  `queries`  ，其中  `queries[i] = [favoriteType<sub>i</sub>, favoriteDay<sub>i</sub>, dailyCap<sub>i</sub>]`  。

你按照如下规则进行一场游戏：
- 你从第  `**0**` ** ** 天开始吃糖果。
- 你在吃完 **所有**  第 `i - 1`  类糖果之前， **不能**  吃任何一颗第 `i`  类糖果。
- 在吃完所有糖果之前，你必须每天 **至少**  吃 **一颗**  糖果。
请你构建一个布尔型数组  `answer`  ，用以给出 `queries` 中每一项的对应答案。此数组满足：
-  `answer.length == queries.length` 。 `answer[i]` 是 `queries[i]` 的答案。
-  `answer[i]` 为  `true`  的条件是：在每天吃 **不超过** `dailyCap<sub>i</sub>` <sub> </sub>颗糖果的前提下，你可以在第  `favoriteDay<sub>i</sub>`  天吃到第  `favoriteType<sub>i</sub>`  类糖果；否则 `answer[i]`  为 `false`  。
注意，只要满足上面 3 条规则中的第二条规则，你就可以在同一天吃不同类型的糖果。

请你返回得到的数组 * * `answer`  。

 

 **示例 1：** 

```

输入：candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]
输出：[true,false,true]
提示：
1- 在第 0 天吃 2 颗糖果(类型 0），第 1 天吃 2 颗糖果（类型 0），第 2 天你可以吃到类型 0 的糖果。
2- 每天你最多吃 4 颗糖果。即使第 0 天吃 4 颗糖果（类型 0），第 1 天吃 4 颗糖果（类型 0 和类型 1），你也没办法在第 2 天吃到类型 4 的糖果。换言之，你没法在每天吃 4 颗糖果的限制下在第 2 天吃到第 4 类糖果。
3- 如果你每天吃 1 颗糖果，你可以在第 13 天吃到类型 2 的糖果。

```
 **示例 2：** 

```

输入：candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]
输出：[false,true,true,false,false]

```
 

 **提示：** 
-  `1 <= candiesCount.length <= 10^5` 
-  `1 <= candiesCount[i] <= 10^5` 
-  `1 <= queries.length <= 10^5` 
-  `queries[i].length == 3` 
-  `0 <= favoriteType<sub>i</sub> < candiesCount.length` 
-  `0 <= favoriteDay<sub>i</sub> <= 10^9` 
-  `1 <= dailyCap<sub>i</sub> <= 10^9` 
 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 1745.回文串分割 IV
[https://leetcode-cn.com/problems/palindrome-partitioning-iv](https://leetcode-cn.com/problems/palindrome-partitioning-iv) 
## 原题
给你一个字符串  `s`  ，如果可以将它分割成三个  **非空**  回文子字符串，那么返回  `true`  ，否则返回  `false`  。

当一个字符串正着读和反着读是一模一样的，就称其为 **回文字符串** 。

 

 **示例 1：** 

```

输入：s = "abcbdd"
输出：true
解释："abcbdd" = "a" + "bcb" + "dd"，三个子字符串都是回文的。

```
 **示例 2：** 

```

输入：s = "bcbddxy"
输出：false
解释：s 没办法被分割成 3 个回文子字符串。

```
 

 **提示：** 
-  `3 <= s.length <= 2000` 
-  `s` ​​​​​​ 只包含小写英文字母。
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1746.经过一次操作后的最大子数组和
[https://leetcode-cn.com/problems/maximum-subarray-sum-after-one-operation](https://leetcode-cn.com/problems/maximum-subarray-sum-after-one-operation) 
## 原题

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1747.应该被禁止的Leetflex账户
[https://leetcode-cn.com/problems/leetflex-banned-accounts](https://leetcode-cn.com/problems/leetflex-banned-accounts) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1748.唯一元素的和
[https://leetcode-cn.com/problems/sum-of-unique-elements](https://leetcode-cn.com/problems/sum-of-unique-elements) 
## 原题
给你一个整数数组  `nums`  。数组中唯一元素是那些只出现  **恰好一次**  的元素。

请你返回 `nums`  中唯一元素的 **和**  。

 

 **示例 1：** 

```
输入：nums = [1,2,3,2]
输出：4
解释：唯一元素为 [1,3] ，和为 4 。

```
 **示例 2：** 

```
输入：nums = [1,1,1,1,1]
输出：0
解释：没有唯一元素，和为 0 。

```
 **示例 3 ：** 

```
输入：nums = [1,2,3,4,5]
输出：15
解释：唯一元素为 [1,2,3,4,5] ，和为 15 。

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `1 <= nums[i] <= 100` 
 
**标签**
`数组` `哈希表` `计数` 


## 
```python

```
>
# 1749.任意子数组和的绝对值的最大值
[https://leetcode-cn.com/problems/maximum-absolute-sum-of-any-subarray](https://leetcode-cn.com/problems/maximum-absolute-sum-of-any-subarray) 
## 原题
给你一个整数数组  `nums`  。一个子数组  `[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]`  的 **和的绝对值**  为  `abs(nums<sub>l</sub> + nums<sub>l+1</sub> + ... + nums<sub>r-1</sub> + nums<sub>r</sub>)`  。

请你找出 `nums`  中 **和的绝对值** 最大的任意子数组（<b>可能为空</b>），并返回该 **最大值**  。

 `abs(x)`  定义如下：
- 如果  `x`  是负整数，那么  `abs(x) = -x`  。
- 如果  `x`  是非负整数，那么  `abs(x) = x`  。
 

 **示例 1：** 

```

输入：nums = [1,-3,2,3,-4]
输出：5
解释：子数组 [2,3] 和的绝对值最大，为 abs(2+3) = abs(5) = 5 。

```
 **示例 2：** 

```

输入：nums = [2,-5,1,-4,3,-2]
输出：8
解释：子数组 [-5,1,-4] 和的绝对值最大，为 abs(-5+1-4) = abs(-8) = 8 。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-10^4 <= nums[i] <= 10^4` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1750.删除字符串两端相同字符后的最短长度
[https://leetcode-cn.com/problems/minimum-length-of-string-after-deleting-similar-ends](https://leetcode-cn.com/problems/minimum-length-of-string-after-deleting-similar-ends) 
## 原题
给你一个只包含字符 `'a'` ， `'b'`  和 `'c'`  的字符串  `s`  ，你可以执行下面这个操作（5 个步骤）任意次：
- 选择字符串 `s`  一个 **非空** 的前缀，这个前缀的所有字符都相同。
- 选择字符串 `s`  一个 **非空** 的后缀，这个后缀的所有字符都相同。
- 前缀和后缀在字符串中任意位置都不能有交集。
- 前缀和后缀包含的所有字符都要相同。
- 同时删除前缀和后缀。
请你返回对字符串 `s`  执行上面操作任意次以后（可能 0 次），能得到的 **最短长度**  。

 

 **示例 1：** 

```

输入：s = "ca"
输出：2
解释：你没法删除任何一个字符，所以字符串长度仍然保持不变。

```
 **示例 2：** 

```

输入：s = "cabaabac"
输出：0
解释：最优操作序列为：
- 选择前缀 "c" 和后缀 "c" 并删除它们，得到 s = "abaaba" 。
- 选择前缀 "a" 和后缀 "a" 并删除它们，得到 s = "baab" 。
- 选择前缀 "b" 和后缀 "b" 并删除它们，得到 s = "aa" 。
- 选择前缀 "a" 和后缀 "a" 并删除它们，得到 s = "" 。
```
 **示例 3：** 

```

输入：s = "aabccabba"
输出：3
解释：最优操作序列为：
- 选择前缀 "aa" 和后缀 "a" 并删除它们，得到 s = "bccabb" 。
- 选择前缀 "b" 和后缀 "bb" 并删除它们，得到 s = "cca" 。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s`  只包含字符  `'a'` ， `'b'`  和  `'c'`  。
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 1751.最多可以参加的会议数目 II
[https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended-ii](https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended-ii) 
## 原题
给你一个  `events`  数组，其中  `events[i] = [startDay<sub>i</sub>, endDay<sub>i</sub>, value<sub>i</sub>]`  ，表示第  `i`  个会议在  `startDay<sub>i</sub>` <sub> </sub>天开始，第  `endDay<sub>i</sub>`  天结束，如果你参加这个会议，你能得到价值  `value<sub>i</sub>`  。同时给你一个整数  `k`  表示你能参加的最多会议数目。

你同一时间只能参加一个会议。如果你选择参加某个会议，那么你必须 **完整**  地参加完这个会议。会议结束日期是包含在会议内的，也就是说你不能同时参加一个开始日期与另一个结束日期相同的两个会议。

请你返回能得到的会议价值  **最大和**  。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/06/screenshot-2021-01-11-at-60048-pm.png" style="width: 400px; height: 103px;" />

```

输入：events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
输出：7
解释：选择绿色的活动会议 0 和 1，得到总价值和为 4 + 3 = 7 。
```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/06/screenshot-2021-01-11-at-60150-pm.png" style="width: 400px; height: 103px;" />

```

输入：events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
输出：10
解释：参加会议 2 ，得到价值和为 10 。
你没法再参加别的会议了，因为跟会议 2 有重叠。你 不 需要参加满 k 个会议。
```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/06/screenshot-2021-01-11-at-60703-pm.png" style="width: 400px; height: 126px;" />** 

```

输入：events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
输出：9
解释：尽管会议互不重叠，你只能参加 3 个会议，所以选择价值最大的 3 个会议。
```
 

 **提示：** 
-  `1 <= k <= events.length` 
-  `1 <= k * events.length <= 10^6` 
-  `1 <= startDay<sub>i</sub> <= endDay<sub>i</sub> <= 10^9` 
-  `1 <= value<sub>i</sub> <= 10^6` 
 
**标签**
`数组` `二分查找` `动态规划` 


## 
```python

```
>
# 1752.检查数组是否经排序和轮转得到
[https://leetcode-cn.com/problems/check-if-array-is-sorted-and-rotated](https://leetcode-cn.com/problems/check-if-array-is-sorted-and-rotated) 
## 原题
给你一个数组 `nums` 。 `nums` 的源数组中，所有元素与 `nums` 相同，但按非递减顺序排列。

如果  `nums` 能够由源数组轮转若干位置（包括 0 个位置）得到，则返回 `true` ；否则，返回 `false` 。

源数组中可能存在 **重复项** 。

 **注意：** 我们称数组 `A` 在轮转 `x` 个位置后得到长度相同的数组 `B` ，当它们满足 `A[i] == B[(i+x) % A.length]` ，其中 `%` 为取余运算。

 

 **示例 1：** 

```

输入：nums = [3,4,5,1,2]
输出：true
解释：[1,2,3,4,5] 为有序的源数组。
可以轮转 x = 3 个位置，使新数组从值为 3 的元素开始：[3,4,5,1,2] 。

```
 **示例 2：** 

```

输入：nums = [2,1,3,4]
输出：false
解释：源数组无法经轮转得到 nums 。

```
 **示例 3：** 

```

输入：nums = [1,2,3]
输出：true
解释：[1,2,3] 为有序的源数组。
可以轮转 x = 0 个位置（即不轮转）得到 nums 。

```
 **示例 4：** 

```

输入：nums = [1,1,1]
输出：true
解释：[1,1,1] 为有序的源数组。
轮转任意个位置都可以得到 nums 。

```
 **示例 5：** 

```

输入：nums = [2,1]
输出：true
解释：[1,2] 为有序的源数组。
可以轮转 x = 5 个位置，使新数组从值为 2 的元素开始：[2,1] 。

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `1 <= nums[i] <= 100` 
 
**标签**
`数组` 


## 
```python

```
>
# 1753.移除石子的最大得分
[https://leetcode-cn.com/problems/maximum-score-from-removing-stones](https://leetcode-cn.com/problems/maximum-score-from-removing-stones) 
## 原题
你正在玩一个单人游戏，面前放置着大小分别为 `a` ​​​​​​、 `b` 和 `c` ​​​​​​ 的 **三堆** 石子。

每回合你都要从两个 **不同的非空堆** 中取出一颗石子，并在得分上加 `1` 分。当存在 **两个或更多** 的空堆时，游戏停止。

给你三个整数 `a` 、 `b` 和 `c` ，返回可以得到的 **最大分数** 。
 

 **示例 1：** 

```

输入：a = 2, b = 4, c = 6
输出：6
解释：石子起始状态是 (2, 4, 6) ，最优的一组操作是：
- 从第一和第三堆取，石子状态现在是 (1, 4, 5)
- 从第一和第三堆取，石子状态现在是 (0, 4, 4)
- 从第二和第三堆取，石子状态现在是 (0, 3, 3)
- 从第二和第三堆取，石子状态现在是 (0, 2, 2)
- 从第二和第三堆取，石子状态现在是 (0, 1, 1)
- 从第二和第三堆取，石子状态现在是 (0, 0, 0)
总分：6 分 。

```
 **示例 2：** 

```

输入：a = 4, b = 4, c = 6
输出：7
解释：石子起始状态是 (4, 4, 6) ，最优的一组操作是：
- 从第一和第二堆取，石子状态现在是 (3, 3, 6)
- 从第一和第三堆取，石子状态现在是 (2, 3, 5)
- 从第一和第三堆取，石子状态现在是 (1, 3, 4)
- 从第一和第三堆取，石子状态现在是 (0, 3, 3)
- 从第二和第三堆取，石子状态现在是 (0, 2, 2)
- 从第二和第三堆取，石子状态现在是 (0, 1, 1)
- 从第二和第三堆取，石子状态现在是 (0, 0, 0)
总分：7 分 。

```
 **示例 3：** 

```

输入：a = 1, b = 8, c = 8
输出：8
解释：最优的一组操作是连续从第二和第三堆取 8 回合，直到将它们取空。
注意，由于第二和第三堆已经空了，游戏结束，不能继续从第一堆中取石子。

```
 

 **提示：** 
-  `1 <= a, b, c <= 10^5` 
 
**标签**
`贪心` `数学` `堆（优先队列）` 


## 
```python

```
>
# 1754.构造字典序最大的合并字符串
[https://leetcode-cn.com/problems/largest-merge-of-two-strings](https://leetcode-cn.com/problems/largest-merge-of-two-strings) 
## 原题
给你两个字符串 `word1` 和 `word2` 。你需要按下述方式构造一个新字符串 `merge` ：如果 `word1` 或 `word2` 非空，选择 **下面选项之一** 继续操作：
- 如果 `word1` 非空，将 `word1` 中的第一个字符附加到 `merge` 的末尾，并将其从 `word1` 中移除。

	
- 例如， `word1 = "abc"` 且 `merge = "dv"` ，在执行此选项操作之后， `word1 = "bc"` ，同时 `merge = "dva"` 。
	
	
- 如果 `word2` 非空，将 `word2` 中的第一个字符附加到 `merge` 的末尾，并将其从 `word2` 中移除。
	
- 例如， `word2 = "abc"` 且 `merge = ""` ，在执行此选项操作之后， `word2 = "bc"` ，同时 `merge = "a"` 。
	
	
返回你可以构造的字典序 **最大** 的合并字符串 `merge` *。* 

长度相同的两个字符串 `a` 和 `b` 比较字典序大小，如果在 `a` 和 `b` 出现不同的第一个位置， `a` 中字符在字母表中的出现顺序位于 `b` 中相应字符之后，就认为字符串 `a` 按字典序比字符串 `b` 更大。例如， `"abcd"` 按字典序比 `"abcc"` 更大，因为两个字符串出现不同的第一个位置是第四个字符，而 `d` 在字母表中的出现顺序位于 `c` 之后。

 

 **示例 1：** 

```

输入：word1 = "cabaa", word2 = "bcaaa"
输出："cbcabaaaaa"
解释：构造字典序最大的合并字符串，可行的一种方法如下所示：
- 从 word1 中取第一个字符：merge = "c"，word1 = "abaa"，word2 = "bcaaa"
- 从 word2 中取第一个字符：merge = "cb"，word1 = "abaa"，word2 = "caaa"
- 从 word2 中取第一个字符：merge = "cbc"，word1 = "abaa"，word2 = "aaa"
- 从 word1 中取第一个字符：merge = "cbca"，word1 = "baa"，word2 = "aaa"
- 从 word1 中取第一个字符：merge = "cbcab"，word1 = "aa"，word2 = "aaa"
- 将 word1 和 word2 中剩下的 5 个 a 附加到 merge 的末尾。

```
 **示例 2：** 

```

输入：word1 = "abcabc", word2 = "abdcaba"
输出："abdcabcabcaba"

```
 

 **提示：** 
-  `1 <= word1.length, word2.length <= 3000` 
-  `word1` 和 `word2` 仅由小写英文组成
 
**标签**
`贪心` `双指针` `字符串` 


## 
```python

```
>
# 1755.最接近目标值的子序列和
[https://leetcode-cn.com/problems/closest-subsequence-sum](https://leetcode-cn.com/problems/closest-subsequence-sum) 
## 原题
给你一个整数数组 `nums` 和一个目标值 `goal` 。

你需要从 `nums` 中选出一个子序列，使子序列元素总和最接近 `goal` 。也就是说，如果子序列元素和为 `sum` ，你需要 **最小化绝对差** `abs(sum - goal)` 。

返回 `abs(sum - goal)` 可能的 **最小值** 。

注意，数组的子序列是通过移除原始数组中的某些元素（可能全部或无）而形成的数组。

 

 **示例 1：** 

```
输入：nums = [5,-7,3,5], goal = 6
输出：0
解释：选择整个数组作为选出的子序列，元素和为 6 。
子序列和与目标值相等，所以绝对差为 0 。

```
 **示例 2：** 

```
输入：nums = [7,-9,15,-2], goal = -5
输出：1
解释：选出子序列 [7,-9,-2] ，元素和为 -4 。
绝对差为 abs(-4 - (-5)) = abs(1) = 1 ，是可能的最小值。

```
 **示例 3：** 

```
输入：nums = [1,2,3], goal = -7
输出：7

```
 

 **提示：** 
-  `1 <= nums.length <= 40` 
-  `-10^7 <= nums[i] <= 10^7` 
-  `-10^9 <= goal <= 10^9` 
 
**标签**
`位运算` `数组` `双指针` `动态规划` `状态压缩` 


## 
```python

```
>
# 1756.设计最近使用（MRU）队列
[https://leetcode-cn.com/problems/design-most-recently-used-queue](https://leetcode-cn.com/problems/design-most-recently-used-queue) 
## 原题

 
**标签**
`栈` `设计` `树状数组` `数组` `哈希表` `有序集合` 


## 
```python

```
>
# 1757.可回收且低脂的产品
[https://leetcode-cn.com/problems/recyclable-and-low-fat-products](https://leetcode-cn.com/problems/recyclable-and-low-fat-products) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1758.生成交替二进制字符串的最少操作数
[https://leetcode-cn.com/problems/minimum-changes-to-make-alternating-binary-string](https://leetcode-cn.com/problems/minimum-changes-to-make-alternating-binary-string) 
## 原题
给你一个仅由字符 `'0'` 和 `'1'` 组成的字符串 `s` 。一步操作中，你可以将任一 `'0'` 变成 `'1'` ，或者将 `'1'` 变成 `'0'` 。

 **交替字符串** 定义为：如果字符串中不存在相邻两个字符相等的情况，那么该字符串就是交替字符串。例如，字符串 `"010"` 是交替字符串，而字符串 `"0100"` 不是。

返回使 `s` 变成 **交替字符串** 所需的 **最少** 操作数。

 

 **示例 1：** 

```
输入：s = "0100"
输出：1
解释：如果将最后一个字符变为 '1' ，s 就变成 "0101" ，即符合交替字符串定义。

```
 **示例 2：** 

```
输入：s = "10"
输出：0
解释：s 已经是交替字符串。

```
 **示例 3：** 

```
输入：s = "1111"
输出：2
解释：需要 2 步操作得到 "0101" 或 "1010" 。

```
 

 **提示：** 
-  `1 <= s.length <= 10^4` 
-  `s[i]` 是 `'0'` 或 `'1'` 
 
**标签**
`字符串` 


## 
```python

```
>
# 1759.统计同构子字符串的数目
[https://leetcode-cn.com/problems/count-number-of-homogenous-substrings](https://leetcode-cn.com/problems/count-number-of-homogenous-substrings) 
## 原题
给你一个字符串 `s` ，返回 `s` 中 **同构子字符串** 的数目。由于答案可能很大，只需返回对 `10^9 + 7` **取余** 后的结果。

 **同构字符串** 的定义为：如果一个字符串中的所有字符都相同，那么该字符串就是同构字符串。

 **子字符串** 是字符串中的一个连续字符序列。

 

 **示例 1：** 

```
输入：s = "abbcccaa"
输出：13
解释：同构子字符串如下所列：
"a"   出现 3 次。
"aa"  出现 1 次。
"b"   出现 2 次。
"bb"  出现 1 次。
"c"   出现 3 次。
"cc"  出现 2 次。
"ccc" 出现 1 次。
3 + 1 + 2 + 1 + 3 + 2 + 1 = 13
```
 **示例 2：** 

```
输入：s = "xy"
输出：2
解释：同构子字符串是 "x" 和 "y" 。
```
 **示例 3：** 

```
输入：s = "zzzzz"
输出：15

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s` 由小写字符串组成
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 1760.袋子里最少数目的球
[https://leetcode-cn.com/problems/minimum-limit-of-balls-in-a-bag](https://leetcode-cn.com/problems/minimum-limit-of-balls-in-a-bag) 
## 原题
给你一个整数数组  `nums`  ，其中  `nums[i]`  表示第  `i`  个袋子里球的数目。同时给你一个整数  `maxOperations`  。

你可以进行如下操作至多  `maxOperations`  次：
- 选择任意一个袋子，并将袋子里的球分到 2 个新的袋子中，每个袋子里都有 **正整数**  个球。

	
- 比方说，一个袋子里有  `5`  个球，你可以把它们分到两个新袋子里，分别有 `1`  个和 `4`  个球，或者分别有 `2`  个和 `3`  个球。
	
	
你的开销是单个袋子里球数目的 **最大值**  ，你想要 **最小化**  开销。

请你返回进行上述操作后的最小开销。

 

 **示例 1：** 

```

输入：nums = [9], maxOperations = 2
输出：3
解释：
- 将装有 9 个球的袋子分成装有 6 个和 3 个球的袋子。[9] -> [6,3] 。
- 将装有 6 个球的袋子分成装有 3 个和 3 个球的袋子。[6,3] -> [3,3,3] 。
装有最多球的袋子里装有 3 个球，所以开销为 3 并返回 3 。

```
 **示例 2：** 

```

输入：nums = [2,4,8,2], maxOperations = 4
输出：2
解释：
- 将装有 8 个球的袋子分成装有 4 个和 4 个球的袋子。[2,4,8,2] -> [2,4,4,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,4,4,4,2] -> [2,2,2,4,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,4,4,2] -> [2,2,2,2,2,4,2] 。
- 将装有 4 个球的袋子分成装有 2 个和 2 个球的袋子。[2,2,2,2,2,4,2] -> [2,2,2,2,2,2,2,2] 。
装有最多球的袋子里装有 2 个球，所以开销为 2 并返回 2 。

```
 **示例 3：** 

```

输入：nums = [7,17], maxOperations = 2
输出：7

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= maxOperations, nums[i] <= 10^9` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 1761.一个图中连通三元组的最小度数
[https://leetcode-cn.com/problems/minimum-degree-of-a-connected-trio-in-a-graph](https://leetcode-cn.com/problems/minimum-degree-of-a-connected-trio-in-a-graph) 
## 原题
给你一个无向图，整数 `n`  表示图中节点的数目， `edges`  数组表示图中的边，其中  `edges[i] = [u<sub>i</sub>, v<sub>i</sub>]`  ，表示  `u<sub>i</sub>` 和  `v<sub>i</sub>` <sub> </sub>之间有一条无向边。

一个 **连通三元组**  指的是 **三个**  节点组成的集合且这三个点之间 **两两**  有边。

 **连通三元组的度数**  是所有满足此条件的边的数目：一个顶点在这个三元组内，而另一个顶点不在这个三元组内。

请你返回所有连通三元组中度数的 **最小值**  ，如果图中没有连通三元组，那么返回 `-1`  。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/14/trios1.png" style="width: 388px; height: 164px;" />
```

输入：n = 6, edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
输出：3
解释：只有一个三元组 [1,2,3] 。构成度数的边在上图中已被加粗。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/14/trios2.png" style="width: 388px; height: 164px;" />
```

输入：n = 7, edges = [[1,3],[4,1],[4,3],[2,5],[5,6],[6,7],[7,5],[2,6]]
输出：0
解释：有 3 个三元组：
1) [1,4,3]，度数为 0 。
2) [2,5,6]，度数为 2 。
3) [5,6,7]，度数为 2 。

```
 

 **提示：** 
-  `2 <= n <= 400` 
-  `edges[i].length == 2` 
-  `1 <= edges.length <= n * (n-1) / 2` 
-  `1 <= u<sub>i</sub>, v<sub>i</sub> <= n` 
-  `u<sub>i </sub>!= v<sub>i</sub>` 
- 图中没有重复的边。
 
**标签**
`图` 


## 
```python

```
>
# 1762.能看到海景的建筑物
[https://leetcode-cn.com/problems/buildings-with-an-ocean-view](https://leetcode-cn.com/problems/buildings-with-an-ocean-view) 
## 原题

 
**标签**
`栈` `数组` `单调栈` 


## 
```python

```
>
# 1763.最长的美好子字符串
[https://leetcode-cn.com/problems/longest-nice-substring](https://leetcode-cn.com/problems/longest-nice-substring) 
## 原题
当一个字符串 `s`  包含的每一种字母的大写和小写形式 **同时**  出现在 `s`  中，就称这个字符串  `s`  是 **美好** 字符串。比方说， `"abABB"`  是美好字符串，因为  `'A'` 和  `'a'`  同时出现了，且  `'B'` 和  `'b'`  也同时出现了。然而， `"abA"`  不是美好字符串因为  `'b'`  出现了，而  `'B'`  没有出现。

给你一个字符串  `s`  ，请你返回  `s`  最长的  **美好子字符串**  。如果有多个答案，请你返回  **最早**  出现的一个。如果不存在美好子字符串，请你返回一个空字符串。

 

 **示例 1：** 

```

输入：s = "YazaAay"
输出："aAa"
解释："aAa" 是一个美好字符串，因为这个子串中仅含一种字母，其小写形式 'a' 和大写形式 'A' 也同时出现了。
"aAa" 是最长的美好子字符串。

```
 **示例 2：** 

```

输入：s = "Bb"
输出："Bb"
解释："Bb" 是美好字符串，因为 'B' 和 'b' 都出现了。整个字符串也是原字符串的子字符串。
```
 **示例 3：** 

```

输入：s = "c"
输出：""
解释：没有美好子字符串。
```
 **示例 4：** 

```

输入：s = "dDzeE"
输出："dD"
解释："dD" 和 "eE" 都是最长美好子字符串。
由于有多个美好子字符串，返回 "dD" ，因为它出现得最早。
```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `s`  只包含大写和小写英文字母。
 
**标签**
`位运算` `哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
# 1764.通过连接另一个数组的子数组得到一个数组
[https://leetcode-cn.com/problems/form-array-by-concatenating-subarrays-of-another-array](https://leetcode-cn.com/problems/form-array-by-concatenating-subarrays-of-another-array) 
## 原题
给你一个长度为 `n`  的二维整数数组  `groups`  ，同时给你一个整数数组  `nums`  。

你是否可以从 `nums`  中选出 `n`  个 **不相交** 的子数组，使得第 `i`  个子数组与 `groups[i]`  （下标从 **0**  开始）完全相同，且如果  `i > 0`  ，那么第  `(i-1)`  个子数组在 `nums`  中出现的位置在第 `i`  个子数组前面。（也就是说，这些子数组在 `nums`  中出现的顺序需要与 `groups` 顺序相同）

如果你可以找出这样的 `n` 个子数组，请你返回  `true` ，否则返回  `false`  。

如果不存在下标为 `k`  的元素 `nums[k]`  属于不止一个子数组，就称这些子数组是 **不相交** 的。子数组指的是原数组中连续元素组成的一个序列。

 

 **示例 1：** 

```

输入：groups = [[1,-1,-1],[3,-2,0]], nums = [1,-1,0,1,-1,-1,3,-2,0]
输出：true
解释：你可以分别在 nums 中选出第 0 个子数组 [1,-1,0,1,-1,-1,3,-2,0] 和第 1 个子数组 [1,-1,0,1,-1,-1,3,-2,0] 。
这两个子数组是不相交的，因为它们没有任何共同的元素。

```
 **示例 2：** 

```

输入：groups = [[10,-2],[1,2,3,4]], nums = [1,2,3,4,10,-2]
输出：false
解释：选择子数组 [1,2,3,4,10,-2] 和 [1,2,3,4,10,-2] 是不正确的，因为它们出现的顺序与 groups 中顺序不同。
[10,-2] 必须出现在 [1,2,3,4] 之前。

```
 **示例 3：** 

```

输入：groups = [[1,2,3],[3,4]], nums = [7,7,1,2,3,4,7,7]
输出：false
解释：选择子数组 [7,7,1,2,3,4,7,7] 和 [7,7,1,2,3,4,7,7] 是不正确的，因为它们不是不相交子数组。
它们有一个共同的元素 nums[4] （下标从 0 开始）。

```
 

 **提示：** 
-  `groups.length == n` 
-  `1 <= n <= 10^3` 
-  `1 <= groups[i].length, sum(groups[i].length) <= 10^<span style="">3</span>` 
-  `1 <= nums.length <= 10^3` 
-  `-10^7 <= groups[i][j], nums[k] <= 10^7` 
 
**标签**
`贪心` `数组` `字符串匹配` 


## 
```python

```
>
# 1765.地图中的最高点
[https://leetcode-cn.com/problems/map-of-highest-peak](https://leetcode-cn.com/problems/map-of-highest-peak) 
## 原题
给你一个大小为 `m x n` 的整数矩阵 `isWater` ，它代表了一个由 **陆地** 和 **水域** 单元格组成的地图。
- 如果 `isWater[i][j] == 0` ，格子 `(i, j)` 是一个 **陆地** 格子。
- 如果 `isWater[i][j] == 1` ，格子 `(i, j)` 是一个 **水域** 格子。
你需要按照如下规则给每个单元格安排高度：
- 每个格子的高度都必须是非负的。
- 如果一个格子是 **水域** ，那么它的高度必须为 `0` 。
- 任意相邻的格子高度差 **至多** 为 `1` 。当两个格子在正东、南、西、北方向上相互紧挨着，就称它们为相邻的格子。（也就是说它们有一条公共边）
找到一种安排高度的方案，使得矩阵中的最高高度值 **最大** 。

请你返回一个大小为 `m x n` 的整数矩阵 `height` ，其中 `height[i][j]` 是格子 `(i, j)` 的高度。如果有多种解法，请返回 **任意一个** 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82045-am.png" style="width: 220px; height: 219px;" />** 

```

输入：isWater = [[0,1],[0,0]]
输出：[[1,0],[2,1]]
解释：上图展示了给各个格子安排的高度。
蓝色格子是水域格，绿色格子是陆地格。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode.com/uploads/2021/01/10/screenshot-2021-01-11-at-82050-am.png" style="width: 300px; height: 296px;" />** 

```

输入：isWater = [[0,0,1],[1,0,0],[0,0,0]]
输出：[[1,1,0],[0,1,1],[1,2,2]]
解释：所有安排方案中，最高可行高度为 2 。
任意安排方案中，只要最高高度为 2 且符合上述规则的，都为可行方案。

```
 

 **提示：** 
-  `m == isWater.length` 
-  `n == isWater[i].length` 
-  `1 <= m, n <= 1000` 
-  `isWater[i][j]` 要么是 `0` ，要么是 `1` 。
- 至少有 **1** 个水域格子。
 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 1766.互质树
[https://leetcode-cn.com/problems/tree-of-coprimes](https://leetcode-cn.com/problems/tree-of-coprimes) 
## 原题
给你一个 `n`  个节点的树（也就是一个无环连通无向图），节点编号从 `0`  到 `n - 1`  ，且恰好有 `n - 1`  条边，每个节点有一个值。树的 **根节点**  为 0 号点。

给你一个整数数组  `nums`  和一个二维数组  `edges`  来表示这棵树。 `nums[i]`  表示第  `i`  个点的值， `edges[j] = [u<sub>j</sub>, v<sub>j</sub>]`  表示节点  `u<sub>j</sub>`  和节点  `v<sub>j</sub>`  在树中有一条边。

当  `gcd(x, y) == 1`  ，我们称两个数  `x` 和  `y`  是 **互质的**  ，其中  `gcd(x, y)`  是 `x`  和 `y`  的 **最大公约数**  。

从节点  `i`  到 **根**  最短路径上的点都是节点 `i`  的祖先节点。一个节点 **不是** 它自己的祖先节点。

请你返回一个大小为 `n`  的数组 `ans`  ，其中 * * `ans[i]` 是离节点  `i`  最近的祖先节点且满足 * * `nums[i]` 和 * * `nums[ans[i]]`  是 **互质的**  ，如果不存在这样的祖先节点， `ans[i]`  为 `-1`  。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/20/untitled-diagram.png" style="width: 191px; height: 281px;" />** 

```

输入：nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
输出：[-1,0,0,1]
解释：上图中，每个节点的值在括号中表示。
- 节点 0 没有互质祖先。
- 节点 1 只有一个祖先节点 0 。它们的值是互质的（gcd(2,3) == 1）。
- 节点 2 有两个祖先节点，分别是节点 1 和节点 0 。节点 1 的值与它的值不是互质的（gcd(3,3) == 3）但节点 0 的值是互质的(gcd(2,3) == 1)，所以节点 0 是最近的符合要求的祖先节点。
- 节点 3 有两个祖先节点，分别是节点 1 和节点 0 。它与节点 1 互质（gcd(3,2) == 1），所以节点 1 是离它最近的符合要求的祖先节点。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/02/20/untitled-diagram1.png" style="width: 441px; height: 291px;" />

```

输入：nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
输出：[-1,0,-1,0,0,0,-1]

```
 

 **提示：** 
-  `nums.length == n` 
-  `1 <= nums[i] <= 50` 
-  `1 <= n <= 10^5` 
-  `edges.length == n - 1` 
-  `edges[j].length == 2` 
-  `0 <= u<sub>j</sub>, v<sub>j</sub> < n` 
-  `u<sub>j</sub> != v<sub>j</sub>` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `数学` 


## 
```python

```
>
# 1767.寻找没有被执行的任务对
[https://leetcode-cn.com/problems/find-the-subtasks-that-did-not-execute](https://leetcode-cn.com/problems/find-the-subtasks-that-did-not-execute) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1768.交替合并字符串
[https://leetcode-cn.com/problems/merge-strings-alternately](https://leetcode-cn.com/problems/merge-strings-alternately) 
## 原题
给你两个字符串 `word1` 和 `word2` 。请你从 `word1` 开始，通过交替添加字母来合并字符串。如果一个字符串比另一个字符串长，就将多出来的字母追加到合并后字符串的末尾。

返回 **合并后的字符串** 。

 

 **示例 1：** 

```

输入：word1 = "abc", word2 = "pqr"
输出："apbqcr"
解释：字符串合并情况如下所示：
word1：  a   b   c
word2：    p   q   r
合并后：  a p b q c r

```
 **示例 2：** 

```

输入：word1 = "ab", word2 = "pqrs"
输出："apbqrs"
解释：注意，word2 比 word1 长，"rs" 需要追加到合并后字符串的末尾。
word1：  a   b 
word2：    p   q   r   s
合并后：  a p b q   r   s

```
 **示例 3：** 

```

输入：word1 = "abcd", word2 = "pq"
输出："apbqcd"
解释：注意，word1 比 word2 长，"cd" 需要追加到合并后字符串的末尾。
word1：  a   b   c   d
word2：    p   q 
合并后：  a p b q c   d

```
 

 **提示：** 
-  `1 <= word1.length, word2.length <= 100` 
-  `word1` 和 `word2` 由小写英文字母组成
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 1769.移动所有球到每个盒子所需的最小操作数
[https://leetcode-cn.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box](https://leetcode-cn.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box) 
## 原题
有 `n` 个盒子。给你一个长度为 `n` 的二进制字符串 `boxes` ，其中 `boxes[i]` 的值为 `'0'` 表示第 `i` 个盒子是 **空** 的，而 `boxes[i]` 的值为 `'1'` 表示盒子里有 **一个** 小球。

在一步操作中，你可以将 **一个** 小球从某个盒子移动到一个与之相邻的盒子中。第 `i` 个盒子和第 `j` 个盒子相邻需满足 `abs(i - j) == 1` 。注意，操作执行后，某些盒子中可能会存在不止一个小球。

返回一个长度为 `n` 的数组 `answer` ，其中 `answer[i]` 是将所有小球移动到第 `i` 个盒子所需的 **最小** 操作数。

每个 `answer[i]` 都需要根据盒子的 **初始状态** 进行计算。

 

 **示例 1：** 

```
输入：boxes = "110"
输出：[1,1,3]
解释：每个盒子对应的最小操作数如下：
1) 第 1 个盒子：将一个小球从第 2 个盒子移动到第 1 个盒子，需要 1 步操作。
2) 第 2 个盒子：将一个小球从第 1 个盒子移动到第 2 个盒子，需要 1 步操作。
3) 第 3 个盒子：将一个小球从第 1 个盒子移动到第 3 个盒子，需要 2 步操作。将一个小球从第 2 个盒子移动到第 3 个盒子，需要 1 步操作。共计 3 步操作。

```
 **示例 2：** 

```
输入：boxes = "001011"
输出：[11,8,5,4,3,4]
```
 

 **提示：** 
-  `n == boxes.length` 
-  `1 <= n <= 2000` 
-  `boxes[i]` 为 `'0'` 或 `'1'` 
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 1770.执行乘法运算的最大分数
[https://leetcode-cn.com/problems/maximum-score-from-performing-multiplication-operations](https://leetcode-cn.com/problems/maximum-score-from-performing-multiplication-operations) 
## 原题
给你两个长度分别 `n` 和 `m` 的整数数组 `nums` 和 `multipliers` **** ，其中 `n >= m` ，数组下标 **从 1 开始** 计数。

初始时，你的分数为 `0` 。你需要执行恰好 `m` 步操作。在第 `i` 步操作（ **从 1 开始** 计数）中，需要：
- 选择数组 `nums` **开头处或者末尾处** 的整数 `x` 。
- 你获得 `multipliers[i] * x` 分，并累加到你的分数中。
- 将 `x` 从数组 `nums` 中移除。
在执行 `m` 步操作后，返回 **最大** 分数 *。* 

 

 **示例 1：** 

```
输入：nums = [1,2,3], multipliers = [3,2,1]
输出：14
解释：一种最优解决方案如下：
- 选择末尾处的整数 3 ，[1,2,3] ，得 3 * 3 = 9 分，累加到分数中。
- 选择末尾处的整数 2 ，[1,2] ，得 2 * 2 = 4 分，累加到分数中。
- 选择末尾处的整数 1 ，[1] ，得 1 * 1 = 1 分，累加到分数中。
总分数为 9 + 4 + 1 = 14 。
```
 **示例 2：** 

```
输入：nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
输出：102
解释：一种最优解决方案如下：
- 选择开头处的整数 -5 ，[-5,-3,-3,-2,7,1] ，得 -5 * -10 = 50 分，累加到分数中。
- 选择开头处的整数 -3 ，[-3,-3,-2,7,1] ，得 -3 * -5 = 15 分，累加到分数中。
- 选择开头处的整数 -3 ，[-3,-2,7,1] ，得 -3 * 3 = -9 分，累加到分数中。
- 选择末尾处的整数 1 ，[-2,7,1] ，得 1 * 4 = 4 分，累加到分数中。
- 选择末尾处的整数 7 ，[-2,7] ，得 7 * 6 = 42 分，累加到分数中。
总分数为 50 + 15 - 9 + 4 + 42 = 102 。

```
 

 **提示：** 
-  `n == nums.length` 
-  `m == multipliers.length` 
-  `1 <= m <= 10^3` 
-  `m <= n <= 10^5` `` 
-  `-1000 <= nums[i], multipliers[i] <= 1000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1771.由子序列构造的最长回文串的长度
[https://leetcode-cn.com/problems/maximize-palindrome-length-from-subsequences](https://leetcode-cn.com/problems/maximize-palindrome-length-from-subsequences) 
## 原题
给你两个字符串 `word1` 和 `word2` ，请你按下述方法构造一个字符串：
- 从 `word1` 中选出某个 **非空** 子序列 `subsequence1` 。
- 从 `word2` 中选出某个 **非空** 子序列 `subsequence2` 。
- 连接两个子序列 `subsequence1 + subsequence2` ，得到字符串。
返回可按上述方法构造的最长 **回文串** 的 **长度** 。如果无法构造回文串，返回 `0` 。

字符串 `s` 的一个 **子序列** 是通过从 `s` 中删除一些（也可能不删除）字符而不更改其余字符的顺序生成的字符串。

 **回文串** 是正着读和反着读结果一致的字符串。

 

 **示例 1：** 

```
输入：word1 = "cacb", word2 = "cbba"
输出：5
解释：从 word1 中选出 "ab" ，从 word2 中选出 "cba" ，得到回文串 "abcba" 。
```
 **示例 2：** 

```
输入：word1 = "ab", word2 = "ab"
输出：3
解释：从 word1 中选出 "ab" ，从 word2 中选出 "a" ，得到回文串 "aba" 。
```
 **示例 3：** 

```
输入：word1 = "aa", word2 = "bb"
输出：0
解释：无法按题面所述方法构造回文串，所以返回 0 。
```
 

 **提示：** 
-  `1 <= word1.length, word2.length <= 1000` 
-  `word1` 和 `word2` 由小写英文字母组成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1772.按受欢迎程度排列功能
[https://leetcode-cn.com/problems/sort-features-by-popularity](https://leetcode-cn.com/problems/sort-features-by-popularity) 
## 原题

 
**标签**
`数组` `哈希表` `字符串` `排序` 


## 
```python

```
>
# 1773.统计匹配检索规则的物品数量
[https://leetcode-cn.com/problems/count-items-matching-a-rule](https://leetcode-cn.com/problems/count-items-matching-a-rule) 
## 原题
给你一个数组 `items` ，其中  `items[i] = [type<sub>i</sub>, color<sub>i</sub>, name<sub>i</sub>]` ，描述第 `i` 件物品的类型、颜色以及名称。

另给你一条由两个字符串  `ruleKey` 和 `ruleValue` 表示的检索规则。

如果第 `i` 件物品能满足下述条件之一，则认为该物品与给定的检索规则 **匹配** ：
-  `ruleKey == "type"` 且 `ruleValue == type<sub>i</sub>` 。
-  `ruleKey == "color"` 且 `ruleValue == color<sub>i</sub>` 。
-  `ruleKey == "name"` 且 `ruleValue == name<sub>i</sub>` 。
统计并返回 **匹配检索规则的物品数量** 。

 

 **示例 1：** 

```

输入：items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
输出：1
解释：只有一件物品匹配检索规则，这件物品是 ["computer","silver","lenovo"] 。

```
 **示例 2：** 

```

输入：items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"
输出：2
解释：只有两件物品匹配检索规则，这两件物品分别是 ["phone","blue","pixel"] 和 ["phone","gold","iphone"] 。注意，["computer","silver","phone"] 未匹配检索规则。
```
 

 **提示：** 
-  `1 <= items.length <= 10^4` 
-  `1 <= type<sub>i</sub>.length, color<sub>i</sub>.length, name<sub>i</sub>.length, ruleValue.length <= 10` 
-  `ruleKey` 等于 `"type"` 、 `"color"` 或 `"name"` 
- 所有字符串仅由小写字母组成
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 1774.最接近目标价格的甜点成本
[https://leetcode-cn.com/problems/closest-dessert-cost](https://leetcode-cn.com/problems/closest-dessert-cost) 
## 原题
你打算做甜点，现在需要购买配料。目前共有 `n` 种冰激凌基料和 `m` 种配料可供选购。而制作甜点需要遵循以下几条规则：
- 必须选择 **一种** 冰激凌基料。
- 可以添加 **一种或多种** 配料，也可以不添加任何配料。
- 每种类型的配料 **最多两份** 。
给你以下三个输入：
-  `baseCosts` ，一个长度为 `n` 的整数数组，其中每个 `baseCosts[i]` 表示第 `i` 种冰激凌基料的价格。
-  `toppingCosts` ，一个长度为 `m` 的整数数组，其中每个 `toppingCosts[i]` 表示 **一份** 第 `i` 种冰激凌配料的价格。
-  `target` ，一个整数，表示你制作甜点的目标价格。
你希望自己做的甜点总成本尽可能接近目标价格 `target` 。

返回最接近 `target` 的甜点成本。如果有多种方案，返回  **成本相对较低** 的一种。

 

 **示例 1：** 

```

输入：baseCosts = [1,7], toppingCosts = [3,4], target = 10
输出：10
解释：考虑下面的方案组合（所有下标均从 0 开始）：
- 选择 1 号基料：成本 7
- 选择 1 份 0 号配料：成本 1 x 3 = 3
- 选择 0 份 1 号配料：成本 0 x 4 = 0
总成本：7 + 3 + 0 = 10 。

```
 **示例 2：** 

```

输入：baseCosts = [2,3], toppingCosts = [4,5,100], target = 18
输出：17
解释：考虑下面的方案组合（所有下标均从 0 开始）：
- 选择 1 号基料：成本 3
- 选择 1 份 0 号配料：成本 1 x 4 = 4
- 选择 2 份 1 号配料：成本 2 x 5 = 10
- 选择 0 份 2 号配料：成本 0 x 100 = 0
总成本：3 + 4 + 10 + 0 = 17 。不存在总成本为 18 的甜点制作方案。

```
 **示例 3：** 

```

输入：baseCosts = [3,10], toppingCosts = [2,5], target = 9
输出：8
解释：可以制作总成本为 8 和 10 的甜点。返回 8 ，因为这是成本更低的方案。

```
 **示例 4：** 

```

输入：baseCosts = [10], toppingCosts = [1], target = 1
输出：10
解释：注意，你可以选择不添加任何配料，但你必须选择一种基料。
```
 

 **提示：** 
-  `n == baseCosts.length` 
-  `m == toppingCosts.length` 
-  `1 <= n, m <= 10` 
-  `1 <= baseCosts[i], toppingCosts[i] <= 10^4` 
-  `1 <= target <= 10^4` 
 
**标签**
`数组` `动态规划` `回溯` 


## 
```python

```
>
# 1775.通过最少操作次数使数组的和相等
[https://leetcode-cn.com/problems/equal-sum-arrays-with-minimum-number-of-operations](https://leetcode-cn.com/problems/equal-sum-arrays-with-minimum-number-of-operations) 
## 原题
给你两个长度可能不等的整数数组  `nums1` 和  `nums2`  。两个数组中的所有值都在  `1`  到  `6`  之间（包含  `1`  和  `6` ）。

每次操作中，你可以选择 **任意**  数组中的任意一个整数，将它变成 `1`  到 `6`  之间 **任意**  的值（包含 `1`  和 `<span style="">6</span>` ）。

请你返回使 `nums1`  中所有数的和与  `nums2`  中所有数的和相等的最少操作次数。如果无法使两个数组的和相等，请返回 `-1`  。

 

 **示例 1：** 

```
输入：nums1 = [1,2,3,4,5,6], nums2 = [1,1,2,2,2,2]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums2[0] 变为 6 。 nums1 = [1,2,3,4,5,6], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[5] 变为 1 。 nums1 = [1,2,3,4,5,1], nums2 = [6,1,2,2,2,2] 。
- 将 nums1[2] 变为 2 。 nums1 = [1,2,2,4,5,1], nums2 = [6,1,2,2,2,2] 。

```
 **示例 2：** 

```
输入：nums1 = [1,1,1,1,1,1,1], nums2 = [6]
输出：-1
解释：没有办法减少 nums1 的和或者增加 nums2 的和使二者相等。

```
 **示例 3：** 

```
输入：nums1 = [6,6], nums2 = [1]
输出：3
解释：你可以通过 3 次操作使 nums1 中所有数的和与 nums2 中所有数的和相等。以下数组下标都从 0 开始。
- 将 nums1[0] 变为 2 。 nums1 = [2,6], nums2 = [1] 。
- 将 nums1[1] 变为 2 。 nums1 = [2,2], nums2 = [1] 。
- 将 nums2[0] 变为 4 。 nums1 = [2,2], nums2 = [4] 。

```
 

 **提示：** 
-  `1 <= nums1.length, nums2.length <= 10^5` 
-  `1 <= nums1[i], nums2[i] <= 6` 
 
**标签**
`贪心` `数组` `哈希表` `计数` 


## 
```python

```
>
# 1776.车队 II
[https://leetcode-cn.com/problems/car-fleet-ii](https://leetcode-cn.com/problems/car-fleet-ii) 
## 原题
在一条单车道上有 `n`  辆车，它们朝着同样的方向行驶。给你一个长度为 `n`  的数组 `cars`  ，其中  `cars[i] = [position<sub>i</sub>, speed<sub>i</sub>]`  ，它表示：
-  `position<sub>i</sub>`  是第 `i`  辆车和道路起点之间的距离（单位：米）。题目保证  `position<sub>i</sub> < position<sub>i+1</sub>` <sub> </sub>。
-  `speed<sub>i</sub>`  是第 `i`  辆车的初始速度（单位：米/秒）。
简单起见，所有车子可以视为在数轴上移动的点。当两辆车占据同一个位置时，我们称它们相遇了。一旦两辆车相遇，它们会合并成一个车队，这个车队里的车有着同样的位置和相同的速度，速度为这个车队里  **最慢**  一辆车的速度。

请你返回一个数组  `answer`  ，其中  `answer[i]`  是第 `i`  辆车与下一辆车相遇的时间（单位：秒），如果这辆车不会与下一辆车相遇，则 `answer[i]`  为 `-1`  。答案精度误差需在 `10^-5`  以内。

 

 **示例 1：** 

```

输入：cars = [[1,2],[2,1],[4,3],[7,2]]
输出：[1.00000,-1.00000,3.00000,-1.00000]
解释：经过恰好 1 秒以后，第一辆车会与第二辆车相遇，并形成一个 1 m/s 的车队。经过恰好 3 秒以后，第三辆车会与第四辆车相遇，并形成一个 2 m/s 的车队。

```
 **示例 2：** 

```

输入：cars = [[3,4],[5,4],[6,3],[9,1]]
输出：[2.00000,1.00000,1.50000,-1.00000]

```
 

 **提示：** 
-  `1 <= cars.length <= 10^5` 
-  `1 <= position<sub>i</sub>, speed<sub>i</sub> <= 10^6` 
-  `position<sub>i</sub> < position<sub>i+1</sub>` 
 
**标签**
`栈` `数组` `数学` `单调栈` `堆（优先队列）` 


## 
```python

```
>
# 1777.每家商店的产品价格
[https://leetcode-cn.com/problems/products-price-for-each-store](https://leetcode-cn.com/problems/products-price-for-each-store) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1778.未知网格中的最短路径
[https://leetcode-cn.com/problems/shortest-path-in-a-hidden-grid](https://leetcode-cn.com/problems/shortest-path-in-a-hidden-grid) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `图` `交互` 


## 
```python

```
>
# 1779.找到最近的有相同 X 或 Y 坐标的点
[https://leetcode-cn.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate](https://leetcode-cn.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate) 
## 原题
给你两个整数 `x` 和 `y` ，表示你在一个笛卡尔坐标系下的 `(x, y)` 处。同时，在同一个坐标系下给你一个数组 `points` ，其中 `points[i] = [a<sub>i</sub>, b<sub>i</sub>]` 表示在 `(a<sub>i</sub>, b<sub>i</sub>)` 处有一个点。当一个点与你所在的位置有相同的 `x` 坐标或者相同的 `y` 坐标时，我们称这个点是 <b>有效的</b> 。

请返回距离你当前位置 **曼哈顿距离** 最近的 **有效** 点的下标（下标从 **0** 开始）。如果有多个最近的有效点，请返回下标 **最小** 的一个。如果没有有效点，请返回 `-1` 。

两个点 `(x<sub>1</sub>, y<sub>1</sub>)` 和 `(x<sub>2</sub>, y<sub>2</sub>)` 之间的 **曼哈顿距离** 为 `abs(x<sub>1</sub> - x<sub>2</sub>) + abs(y<sub>1</sub> - y<sub>2</sub>)` 。

 

 **示例 1：** 

```

输入：x = 3, y = 4, points = [[1,2],[3,1],[2,4],[2,3],[4,4]]
输出：2
解释：所有点中，[3,1]，[2,4] 和 [4,4] 是有效点。有效点中，[2,4] 和 [4,4] 距离你当前位置的曼哈顿距离最小，都为 1 。[2,4] 的下标最小，所以返回 2 。
```
 **示例 2：** 

```

输入：x = 3, y = 4, points = [[3,4]]
输出：0
提示：答案可以与你当前所在位置坐标相同。
```
 **示例 3：** 

```

输入：x = 3, y = 4, points = [[2,3]]
输出：-1
解释：没有 有效点。
```
 

 **提示：** 
-  `1 <= points.length <= 10^4` 
-  `points[i].length == 2` 
-  `1 <= x, y, a<sub>i</sub>, b<sub>i</sub> <= 10^4` 
 
**标签**
`数组` 


## 
```python

```
>
# 1780.判断一个数字是否可以表示成三的幂的和
[https://leetcode-cn.com/problems/check-if-number-is-a-sum-of-powers-of-three](https://leetcode-cn.com/problems/check-if-number-is-a-sum-of-powers-of-three) 
## 原题
给你一个整数  `n`  ，如果你可以将  `n`  表示成若干个不同的三的幂之和，请你返回  `true`  ，否则请返回 `false`  。

对于一个整数 `y`  ，如果存在整数 `x`  满足 `y == 3^x`  ，我们称这个整数 `y`  是三的幂。

 

 **示例 1：** 

```
输入：n = 12
输出：true
解释：12 = 3^1 + 3^2

```
 **示例 2：** 

```
输入：n = 91
输出：true
解释：91 = 3^0 + 3^2 + 3^4

```
 **示例 3：** 

```
输入：n = 21
输出：false

```
 

 **提示：** 
-  `1 <= n <= 10^7` 
 
**标签**
`数学` 


## 
```python

```
>
# 1781.所有子字符串美丽值之和
[https://leetcode-cn.com/problems/sum-of-beauty-of-all-substrings](https://leetcode-cn.com/problems/sum-of-beauty-of-all-substrings) 
## 原题
一个字符串的 **美丽值**  定义为：出现频率最高字符与出现频率最低字符的出现次数之差。
- 比方说， `"abaacc"`  的美丽值为  `3 - 1 = 2`  。
给你一个字符串  `s`  ，请你返回它所有子字符串的  **美丽值**  之和。

 

 **示例 1：** 

```

输入：s = "aabcb"
输出：5
解释：美丽值不为零的字符串包括 ["aab","aabc","aabcb","abcb","bcb"] ，每一个字符串的美丽值都为 1 。
```
 **示例 2：** 

```

输入：s = "aabcbaa"
输出：17

```
 

 **提示：** 
-  `1 <= s.length <=^ 500` 
-  `s`  只包含小写英文字母。
 
**标签**
`哈希表` `字符串` `计数` 


## 
```python

```
>
# 1782.统计点对的数目
[https://leetcode-cn.com/problems/count-pairs-of-nodes](https://leetcode-cn.com/problems/count-pairs-of-nodes) 
## 原题
给你一个无向图，无向图由整数  `n`   ，表示图中节点的数目，和  `edges`  组成，其中  `edges[i] = [u<sub>i</sub>, v<sub>i</sub>]`  表示  `u<sub>i</sub>` 和  `v<sub>i</sub>` <sub> </sub>之间有一条无向边。同时给你一个代表查询的整数数组  `queries`  。

第 `j` 个查询的答案是满足如下条件的点对 `(a, b)` 的数目：
-  `a < b` 
-  `cnt`  是与 `a`   **或者 ** `b`  相连的边的数目，且 `cnt`   **严格大于 ** `queries[j]`  。
请你返回一个数组  `answers`  ，其中  `answers.length == queries.length` 且  `answers[j]`  是第 `j`  个查询的答案。

请注意，图中可能会有 **重复边**  。

 

 **示例 1：** 
<img alt="" src="https://pic.leetcode-cn.com/1614828447-GMnLVg-image.png" style="width: 310px; height: 278px;" />
```

输入：n = 4, edges = [[1,2],[2,4],[1,3],[2,3],[2,1]], queries = [2,3]
输出：[6,5]
解释：每个点对中，与至少一个点相连的边的数目如上图所示。

```
 **示例 2：** 

```

输入：n = 5, edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]], queries = [1,2,3,4,5]
输出：[10,10,9,8,6]

```
 

 **提示：** 
-  `2 <= n <= 2 * 10^4` 
-  `1 <= edges.length <= 10^5` 
-  `1 <= u<sub>i</sub>, v<sub>i</sub> <= n` 
-  `u<sub>i </sub>!= v<sub>i</sub>` 
-  `1 <= queries.length <= 20` 
-  `0 <= queries[j] < edges.length` 
 
**标签**
`图` `双指针` `二分查找` 


## 
```python

```
>
# 1783.大满贯数量
[https://leetcode-cn.com/problems/grand-slam-titles](https://leetcode-cn.com/problems/grand-slam-titles) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1784.检查二进制字符串字段
[https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones](https://leetcode-cn.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones) 
## 原题
给你一个二进制字符串 `s` ，该字符串 **不含前导零** 。

如果 `s` 包含 **零个或一个由连续的 `'1'` 组成的字段** ，返回 `true` ​​​ 。否则，返回 `false` 。

 

 **示例 1：** 

```

输入：s = "1001"
输出：false
解释：字符串中的 1 没有形成一个连续字段。

```
 **示例 2：** 

```

输入：s = "110"
输出：true
```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `s[i]` ​​​​ 为 `'0'` 或 `'1'` 
-  `s[0]` 为 `'1'` 
 
**标签**
`字符串` 


## 
```python

```
>
# 1785.构成特定和需要添加的最少元素
[https://leetcode-cn.com/problems/minimum-elements-to-add-to-form-a-given-sum](https://leetcode-cn.com/problems/minimum-elements-to-add-to-form-a-given-sum) 
## 原题
给你一个整数数组 `nums` ，和两个整数 `limit` 与 `goal` 。数组 `nums` 有一条重要属性： `abs(nums[i]) <= limit` 。

返回使数组元素总和等于 `goal` 所需要向数组中添加的 **最少元素数量** ，添加元素 **不应改变** 数组中 `abs(nums[i]) <= limit` 这一属性。

注意，如果 `x >= 0` ，那么 `abs(x)` 等于 `x` ；否则，等于 `-x` 。

 

 **示例 1：** 

```

输入：nums = [1,-1,1], limit = 3, goal = -4
输出：2
解释：可以将 -2 和 -3 添加到数组中，数组的元素总和变为 1 - 1 + 1 - 2 - 3 = -4 。

```
 **示例 2：** 

```

输入：nums = [1,-10,9,1], limit = 100, goal = 0
输出：1

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= limit <= 10^6` 
-  `-limit <= nums[i] <= limit` 
-  `-10^9 <= goal <= 10^9` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1786.从第一个节点出发到最后一个节点的受限路径数
[https://leetcode-cn.com/problems/number-of-restricted-paths-from-first-to-last-node](https://leetcode-cn.com/problems/number-of-restricted-paths-from-first-to-last-node) 
## 原题
现有一个加权无向连通图。给你一个正整数 `n` ，表示图中有 `n` 个节点，并按从 `1` 到 `n` 给节点编号；另给你一个数组 `edges` ，其中每个 `edges[i] = [u<sub>i</sub>, v<sub>i</sub>, weight<sub>i</sub>]` 表示存在一条位于节点 `u<sub>i</sub>` 和 `v<sub>i</sub>` 之间的边，这条边的权重为 `weight<sub>i</sub>` 。

从节点 `start` 出发到节点 `end` 的路径是一个形如 `[z<sub>0</sub>, z<sub>1</sub>,<sub> </sub>z<sub>2</sub>, ..., z<sub>k</sub>]` 的节点序列，满足 `z<sub>0 </sub>= start` 、 `z<sub>k</sub> = end` 且在所有符合 `0 <= i <= k-1` 的节点 `z<sub>i</sub>` 和 `z<sub>i+1</sub>` 之间存在一条边。

路径的距离定义为这条路径上所有边的权重总和。用 `distanceToLastNode(x)` 表示节点 `n` 和 `x` 之间路径的最短距离。 **受限路径** 为满足 `distanceToLastNode(z<sub>i</sub>) > distanceToLastNode(z<sub>i+1</sub>)` 的一条路径，其中 `0 <= i <= k-1` 。

返回从节点 `1` 出发到节点 `n` 的 **受限路径数** 。由于数字可能很大，请返回对 `10^9 + 7` **取余** 的结果。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/03/07/restricted_paths_ex1.png" style="width: 351px; height: 341px;" />
```

输入：n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]
输出：3
解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。三条受限路径分别是：
1) 1 --> 2 --> 5
2) 1 --> 2 --> 3 --> 5
3) 1 --> 3 --> 5

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/03/07/restricted_paths_ex22.png" style="width: 356px; height: 401px;" />
```

输入：n = 7, edges = [[1,3,1],[4,1,2],[7,3,4],[2,5,3],[5,6,1],[6,7,2],[7,5,3],[2,6,4]]
输出：1
解释：每个圆包含黑色的节点编号和蓝色的 distanceToLastNode 值。唯一一条受限路径是：1 --> 3 --> 7 。
```
 

 **提示：** 
-  `1 <= n <= 2 * 10^4` 
-  `n - 1 <= edges.length <= 4 * 10^4` 
-  `edges[i].length == 3` 
-  `1 <= u<sub>i</sub>, v<sub>i</sub> <= n` 
-  `u<sub>i </sub>!= v<sub>i</sub>` 
-  `1 <= weight<sub>i</sub> <= 10^5` 
- 任意两个节点之间至多存在一条边
- 任意两个节点之间至少存在一条路径
 
**标签**
`图` `拓扑排序` `动态规划` `最短路` `堆（优先队列）` 


## 
```python

```
>
# 1787.使所有区间的异或结果为零
[https://leetcode-cn.com/problems/make-the-xor-of-all-segments-equal-to-zero](https://leetcode-cn.com/problems/make-the-xor-of-all-segments-equal-to-zero) 
## 原题
给你一个整数数组 `nums` ​​​ 和一个整数 `k` ​​​​​ 。区间 `[left, right]` （ `left <= right` ）的 **异或结果** 是对下标位于  `left` 和 `right` （包括 `left` 和 `right` ）之间所有元素进行 `XOR` 运算的结果： `nums[left] XOR nums[left+1] XOR ... XOR nums[right]` 。

返回数组中 **要更改的最小元素数** ，以使所有长度为 `k` 的区间异或结果等于零。

 

 **示例 1：** 

```

输入：nums = [1,2,0,3,0], k = 1
输出：3
解释：将数组 [1,2,0,3,0] 修改为 [0,0,0,0,0]

```
 **示例 2：** 

```

输入：nums = [3,4,5,2,1,7,3,4,7], k = 3
输出：3
解释：将数组 [3,4,5,2,1,7,3,4,7] 修改为 [3,4,7,3,4,7,3,4,7]

```
 **示例 3：** 

```

输入：nums = [1,2,4,1,2,5,1,2,6], k = 3
输出：3
解释：将数组[1,2,4,1,2,5,1,2,6] 修改为 [1,2,3,1,2,3,1,2,3]
```
 

 **提示：** 
-  `1 <= k <= nums.length <= 2000` 
-  `​​​​​​0 <= nums[i] < 2^10` 
 
**标签**
`位运算` `数组` `动态规划` 


## 
```python

```
>
# 1788.最大化花园的美观度
[https://leetcode-cn.com/problems/maximize-the-beauty-of-the-garden](https://leetcode-cn.com/problems/maximize-the-beauty-of-the-garden) 
## 原题

 
**标签**
`贪心` `数组` `前缀和` 


## 
```python

```
>
# 1789.员工的直属部门
[https://leetcode-cn.com/problems/primary-department-for-each-employee](https://leetcode-cn.com/problems/primary-department-for-each-employee) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1790.仅执行一次字符串交换能否使两个字符串相等
[https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal](https://leetcode-cn.com/problems/check-if-one-string-swap-can-make-strings-equal) 
## 原题
给你长度相等的两个字符串 `s1` 和 `s2` 。一次 **字符串交换** 操作的步骤如下：选出某个字符串中的两个下标（不必不同），并交换这两个下标所对应的字符。

如果对 **其中一个字符串** 执行 **最多一次字符串交换** 就可以使两个字符串相等，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```
输入：s1 = "bank", s2 = "kanb"
输出：true
解释：例如，交换 s2 中的第一个和最后一个字符可以得到 "bank"

```
 **示例 2：** 

```
输入：s1 = "attack", s2 = "defend"
输出：false
解释：一次字符串交换无法使两个字符串相等

```
 **示例 3：** 

```
输入：s1 = "kelb", s2 = "kelb"
输出：true
解释：两个字符串已经相等，所以不需要进行字符串交换

```
 **示例 4：** 

```
输入：s1 = "abcd", s2 = "dcba"
输出：false

```
 

 **提示：** 
-  `1 <= s1.length, s2.length <= 100` 
-  `s1.length == s2.length` 
-  `s1` 和 `s2` 仅由小写英文字母组成
 
**标签**
`哈希表` `字符串` `计数` 


## 
```python

```
>
# 1791.找出星型图的中心节点
[https://leetcode-cn.com/problems/find-center-of-star-graph](https://leetcode-cn.com/problems/find-center-of-star-graph) 
## 原题
有一个无向的 **星型** 图，由 `n` 个编号从 `1` 到 `n` 的节点组成。星型图有一个 **中心** 节点，并且恰有 `n - 1` 条边将中心节点与其他每个节点连接起来。

给你一个二维整数数组 `edges` ，其中  `edges[i] = [u<sub>i</sub>, v<sub>i</sub>]` 表示在节点 `u<sub>i</sub>` 和 `v<sub>i</sub>` 之间存在一条边。请你找出并返回  `edges` 所表示星型图的中心节点。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/03/14/star_graph.png" style="width: 331px; height: 321px;" />
```

输入：edges = [[1,2],[2,3],[4,2]]
输出：2
解释：如上图所示，节点 2 与其他每个节点都相连，所以节点 2 是中心节点。

```
 **示例 2：** 

```

输入：edges = [[1,2],[5,1],[1,3],[1,4]]
输出：1

```
 

 **提示：** 
-  `3 <= n <= 10^5` 
-  `edges.length == n - 1` 
-  `edges[i].length == 2` 
-  `1 <= u<sub>i,</sub> v<sub>i</sub> <= n` 
-  `u<sub>i</sub> != v<sub>i</sub>` 
- 题目数据给出的 `edges` 表示一个有效的星型图
 
**标签**
`图` 


## 
```python

```
>
# 1792.最大平均通过率
[https://leetcode-cn.com/problems/maximum-average-pass-ratio](https://leetcode-cn.com/problems/maximum-average-pass-ratio) 
## 原题
一所学校里有一些班级，每个班级里有一些学生，现在每个班都会进行一场期末考试。给你一个二维数组 `classes`  ，其中  `classes[i] = [pass<sub>i</sub>, total<sub>i</sub>]`  ，表示你提前知道了第  `i`  个班级总共有  `total<sub>i</sub>`  个学生，其中只有  `pass<sub>i</sub>`  个学生可以通过考试。

给你一个整数  `extraStudents`  ，表示额外有  `extraStudents`  个聪明的学生，他们 **一定**  能通过任何班级的期末考。你需要给这  `extraStudents`  个学生每人都安排一个班级，使得 **所有**  班级的 **平均**  通过率 **最大**  。

一个班级的  **通过率**  等于这个班级通过考试的学生人数除以这个班级的总人数。 **平均通过率**  是所有班级的通过率之和除以班级数目。

请你返回在安排这 `<span style="">extraStudents</span>` 个学生去对应班级后的 **最大**  平均通过率。与标准答案误差范围在  `10^-5`  以内的结果都会视为正确结果。

 

 **示例 1：** 

```

输入：classes = [[1,2],[3,5],[2,2]], extraStudents = 2
输出：0.78333
解释：你可以将额外的两个学生都安排到第一个班级，平均通过率为 (3/4 + 3/5 + 2/2) / 3 = 0.78333 。

```
 **示例 2：** 

```

输入：classes = [[2,4],[3,9],[4,5],[2,10]], extraStudents = 4
输出：0.53485

```
 

 **提示：** 
-  `1 <= classes.length <= 10^5` 
-  `classes[i].length == 2` 
-  `1 <= pass<sub>i</sub> <= total<sub>i</sub> <= 10^5` 
-  `1 <= extraStudents <= 10^5` 
 
**标签**
`贪心` `数组` `堆（优先队列）` 


## 
```python

```
>
# 1793.好子数组的最大分数
[https://leetcode-cn.com/problems/maximum-score-of-a-good-subarray](https://leetcode-cn.com/problems/maximum-score-of-a-good-subarray) 
## 原题
给你一个整数数组  `nums`   **（下标从 0 开始）** 和一个整数  `k`  。

一个子数组 `(i, j)`  的 **分数**  定义为  `min(nums[i], nums[i+1], ..., nums[j]) * (j - i + 1)`  。一个  **好**  子数组的两个端点下标需要满足  `i <= k <= j`  。

请你返回 **好**  子数组的最大可能 **分数**  。

 

 **示例 1：** 

```
输入：nums = [1,4,3,7,4,5], k = 3
输出：15
解释：最优子数组的左右端点下标是 (1, 5) ，分数为 min(4,3,7,4,5) * (5-1+1) = 3 * 5 = 15 。

```
 **示例 2：** 

```
输入：nums = [5,5,4,5,4,1,1,1], k = 0
输出：20
解释：最优子数组的左右端点下标是 (0, 4) ，分数为 min(5,5,4,5,4) * (4-0+1) = 4 * 5 = 20 。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 2 * 10^4` 
-  `0 <= k < nums.length` 
 
**标签**
`栈` `数组` `双指针` `二分查找` `单调栈` 


## 
```python

```
>
# 1794.统计距离最小的子串对个数
[https://leetcode-cn.com/problems/count-pairs-of-equal-substrings-with-minimum-difference](https://leetcode-cn.com/problems/count-pairs-of-equal-substrings-with-minimum-difference) 
## 原题

 
**标签**
`贪心` `哈希表` `字符串` 


## 
```python

```
>
# 1795.每个产品在不同商店的价格
[https://leetcode-cn.com/problems/rearrange-products-table](https://leetcode-cn.com/problems/rearrange-products-table) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1796.字符串中第二大的数字
[https://leetcode-cn.com/problems/second-largest-digit-in-a-string](https://leetcode-cn.com/problems/second-largest-digit-in-a-string) 
## 原题
给你一个混合字符串  `s`  ，请你返回 `s`  中 **第二大** 的数字，如果不存在第二大的数字，请你返回 `-1`  。

 **混合字符串** 由小写英文字母和数字组成。

 

 **示例 1：** 

```

输入：s = "dfa12321afd"
输出：2
解释：出现在 s 中的数字包括 [1, 2, 3] 。第二大的数字是 2 。

```
 **示例 2：** 

```

输入：s = "abc1111"
输出：-1
解释：出现在 s 中的数字只包含 [1] 。没有第二大的数字。

```
 

 **提示：** 
-  `1 <= s.length <= 500` 
-  `s`  只包含小写英文字母和（或）数字。
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1797.设计一个验证系统
[https://leetcode-cn.com/problems/design-authentication-manager](https://leetcode-cn.com/problems/design-authentication-manager) 
## 原题
你需要设计一个包含验证码的验证系统。每一次验证中，用户会收到一个新的验证码，这个验证码在 `currentTime`  时刻之后 `timeToLive`  秒过期。如果验证码被更新了，那么它会在 `currentTime`  （可能与之前的 `currentTime`  不同）时刻延长  `timeToLive`  秒。

请你实现  `AuthenticationManager`  类：
-  `AuthenticationManager(int timeToLive)`  构造  `AuthenticationManager`  并设置  `timeToLive`  参数。
-  `generate(string tokenId, int currentTime)`  给定 `tokenId`  ，在当前时间  `currentTime` 生成一个新的验证码。
-  `renew(string tokenId, int currentTime)`  将给定 `tokenId`  且 **未过期**  的验证码在 `currentTime`  时刻更新。如果给定  `tokenId`  对应的验证码不存在或已过期，请你忽略该操作，不会有任何更新操作发生。
-  `countUnexpiredTokens(int currentTime)`  请返回在给定  `currentTime`  时刻， **未过期**  的验证码数目。
如果一个验证码在时刻  `t`  过期，且另一个操作恰好在时刻  `t`  发生（ `renew`  或者  `countUnexpiredTokens`  操作），过期事件  **优先于**  其他操作。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/copy-of-pc68_q2.png" style="width: 500px; height: 287px;" />
```

输入：
["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew", "countUnexpiredTokens"]
[[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
输出：
[null, null, null, 1, null, null, null, 0]

解释：
AuthenticationManager authenticationManager = new AuthenticationManager(5); // 构造 AuthenticationManager ，设置 timeToLive = 5 秒。
authenticationManager.renew("aaa", 1); // 时刻 1 时，没有验证码的 tokenId 为 "aaa" ，没有验证码被更新。
authenticationManager.generate("aaa", 2); // 时刻 2 时，生成一个 tokenId 为 "aaa" 的新验证码。
authenticationManager.countUnexpiredTokens(6); // 时刻 6 时，只有 tokenId 为 "aaa" 的验证码未过期，所以返回 1 。
authenticationManager.generate("bbb", 7); // 时刻 7 时，生成一个 tokenId 为 "bbb" 的新验证码。
authenticationManager.renew("aaa", 8); // tokenId 为 "aaa" 的验证码在时刻 7 过期，且 8 >= 7 ，所以时刻 8 的renew 操作被忽略，没有验证码被更新。
authenticationManager.renew("bbb", 10); // tokenId 为 "bbb" 的验证码在时刻 10 没有过期，所以 renew 操作会执行，该 token 将在时刻 15 过期。
authenticationManager.countUnexpiredTokens(15); // tokenId 为 "bbb" 的验证码在时刻 15 过期，tokenId 为 "aaa" 的验证码在时刻 7 过期，所有验证码均已过期，所以返回 0 。

```
 

 **提示：** 
-  `1 <= timeToLive <= 10^8` 
-  `1 <= currentTime <= 10^8` 
-  `1 <= tokenId.length <= 5` 
-  `tokenId`  只包含小写英文字母。
- 所有  `generate`  函数的调用都会包含独一无二的  `tokenId`  值。
- 所有函数调用中， `currentTime`  的值 **严格递增**  。
- 所有函数的调用次数总共不超过  `2000`  次。
 
**标签**
`设计` `哈希表` 


## 
```python

```
>
# 1798.你能构造出连续值的最大数目
[https://leetcode-cn.com/problems/maximum-number-of-consecutive-values-you-can-make](https://leetcode-cn.com/problems/maximum-number-of-consecutive-values-you-can-make) 
## 原题
给你一个长度为 `n`  的整数数组  `coins`  ，它代表你拥有的  `n`  个硬币。第  `i`  个硬币的值为  `coins[i]`  。如果你从这些硬币中选出一部分硬币，它们的和为  `x`  ，那么称，你可以  **构造**  出  `x`  。

请返回从 `0`  开始（ **包括**   `0`  ），你最多能  **构造**  出多少个连续整数。

你可能有多个相同值的硬币。

 

 **示例 1：** 

```

输入：coins = [1,3]
输出：2
解释：你可以得到以下这些值：
- 0：什么都不取 []
- 1：取 [1]
从 0 开始，你可以构造出 2 个连续整数。
```
 **示例 2：** 

```

输入：coins = [1,1,1,4]
输出：8
解释：你可以得到以下这些值：
- 0：什么都不取 []
- 1：取 [1]
- 2：取 [1,1]
- 3：取 [1,1,1]
- 4：取 [4]
- 5：取 [4,1]
- 6：取 [4,1,1]
- 7：取 [4,1,1,1]
从 0 开始，你可以构造出 8 个连续整数。
```
 **示例 3：** 

```

输入：nums = [1,4,10,3,1]
输出：20
```
 

 **提示：** 
-  `coins.length == n` 
-  `1 <= n <= 4 * 10^4` 
-  `1 <= coins[i] <= 4 * 10^4` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1799.N 次操作后的最大分数和
[https://leetcode-cn.com/problems/maximize-score-after-n-operations](https://leetcode-cn.com/problems/maximize-score-after-n-operations) 
## 原题
给你  `nums`  ，它是一个大小为  `2 * n`  的正整数数组。你必须对这个数组执行 `n`  次操作。

在第  `i`  次操作时（操作编号从 **1**  开始），你需要：
- 选择两个元素  `x` 和  `y`  。
- 获得分数  `i * gcd(x, y)`  。
- 将  `x`  和  `y` 从  `nums`  中删除。
请你返回 `n`  次操作后你能获得的分数和最大为多少。

函数  `gcd(x, y)`  是  `x` 和  `y`  的最大公约数。

 

 **示例 1：** 

```
输入：nums = [1,2]
输出：1
解释：最优操作是：
(1 * gcd(1, 2)) = 1

```
 **示例 2：** 

```
输入：nums = [3,4,6,8]
输出：11
解释：最优操作是：
(1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11

```
 **示例 3：** 

```
输入：nums = [1,2,3,4,5,6]
输出：14
解释：最优操作是：
(1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14

```
 

 **提示：** 
-  `1 <= n <= 7` 
-  `nums.length == 2 * n` 
-  `1 <= nums[i] <= 10^6` 
 
**标签**
`位运算` `数组` `数学` `动态规划` `回溯` `状态压缩` `数论` 


## 
```python

```
>
# 1800.最大升序子数组和
[https://leetcode-cn.com/problems/maximum-ascending-subarray-sum](https://leetcode-cn.com/problems/maximum-ascending-subarray-sum) 
## 原题
给你一个正整数组成的数组 `nums` ，返回 `nums` 中一个 **升序** 子数组的最大可能元素和。

子数组是数组中的一个连续数字序列。

已知子数组 `[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]` ，若对所有 `i` （ `l <= i < r` ）， `nums<sub>i </sub> < nums<sub>i+1</sub>` 都成立，则称这一子数组为 **升序** 子数组。注意，大小为 `1` 的子数组也视作 **升序** 子数组。

 

 **示例 1：** 

```

输入：nums = [10,20,30,5,10,50]
输出：65
解释：[5,10,50] 是元素和最大的升序子数组，最大元素和为 65 。

```
 **示例 2：** 

```

输入：nums = [10,20,30,40,50]
输出：150
解释：[10,20,30,40,50] 是元素和最大的升序子数组，最大元素和为 150 。 

```
 **示例 3：** 

```

输入：nums = [12,17,15,13,10,11,12]
输出：33
解释：[10,11,12] 是元素和最大的升序子数组，最大元素和为 33 。 

```
 **示例 4：** 

```

输入：nums = [100,10,1]
输出：100

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `1 <= nums[i] <= 100` 
 
**标签**
`数组` 


## 
```python

```
>
