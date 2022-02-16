# 401.二进制手表
[https://leetcode-cn.com/problems/binary-watch](https://leetcode-cn.com/problems/binary-watch) 
## 原题
二进制手表顶部有 4 个 LED 代表 **小时（0-11）** ，底部的 6 个 LED 代表 **分钟（0-59）** 。每个 LED 代表一个 0 或 1，最低位在右侧。
- 例如，下面的二进制手表读取 `"3:25"` 。
<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/03/29/binary_clock_samui_moon.jpg" style="height: 300px; width" />

<small> *（图源：<a href="https://commons.m.wikimedia.org/wiki/File:Binary_clock_samui_moon.jpg">WikiMedia - Binary clock samui moon.jpg</a> ，许可协议：<a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)</a> ）* </small>

给你一个整数 `turnedOn` ，表示当前亮着的 LED 的数量，返回二进制手表可以表示的所有可能时间。你可以 **按任意顺序** 返回答案。

小时不会以零开头：
- 例如， `"01:00"` 是无效的时间，正确的写法应该是 `"1:00"` 。
分钟必须由两位数组成，可能会以零开头：
- 例如， `"10:2"` 是无效的时间，正确的写法应该是 `"10:02"` 。
 

 **示例 1：** 

```

输入：turnedOn = 1
输出：["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

```
 **示例 2：** 

```

输入：turnedOn = 9
输出：[]

```
 

 **提示：** 
-  `0 <= turnedOn <= 10` 
 
**标签**
`位运算` `回溯` 


## 
```python

```
>
# 402.移掉 K 位数字
[https://leetcode-cn.com/problems/remove-k-digits](https://leetcode-cn.com/problems/remove-k-digits) 
## 原题
给你一个以字符串表示的非负整数  `num` 和一个整数 `k` ，移除这个数中的 `k` 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。
 

 **示例 1 ：** 

```

输入：num = "1432219", k = 3
输出："1219"
解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。

```
 **示例 2 ：** 

```

输入：num = "10200", k = 1
输出："200"
解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。

```
 **示例 3 ：** 

```

输入：num = "10", k = 2
输出："0"
解释：从原数字移除所有的数字，剩余为空就是 0 。

```
 

 **提示：** 
-  `1 <= k <= num.length <= 10^5` 
-  `num` 仅由若干位数字（0 - 9）组成
- 除了 **0** 本身之外， `num` 不含任何前导零
 
**标签**
`栈` `贪心` `字符串` `单调栈` 


## 
```python

```
>
# 403.青蛙过河
[https://leetcode-cn.com/problems/frog-jump](https://leetcode-cn.com/problems/frog-jump) 
## 原题
一只青蛙想要过河。 假定河流被等分为若干个单元格，并且在每一个单元格内都有可能放有一块石子（也有可能没有）。 青蛙可以跳上石子，但是不可以跳入水中。

给你石子的位置列表 `stones` （用单元格序号 **升序** 表示）， 请判定青蛙能否成功过河（即能否在最后一步跳至最后一块石子上）。开始时， 青蛙默认已站在第一块石子上，并可以假定它第一步只能跳跃 `1` 个单位（即只能从单元格 1 跳至单元格 2 ）。

如果青蛙上一步跳跃了 `k` 个单位，那么它接下来的跳跃距离只能选择为 `k - 1` 、 `k` 或 `k + 1` 个单位。 另请注意，青蛙只能向前方（终点的方向）跳跃。

 

 **示例 1：** 

```

输入：stones = [0,1,3,5,6,8,12,17]
输出：true
解释：青蛙可以成功过河，按照如下方案跳跃：跳 1 个单位到第 2 块石子, 然后跳 2 个单位到第 3 块石子, 接着 跳 2 个单位到第 4 块石子, 然后跳 3 个单位到第 6 块石子, 跳 4 个单位到第 7 块石子, 最后，跳 5 个单位到第 8 个石子（即最后一块石子）。
```
 **示例 2：** 

```

输入：stones = [0,1,2,3,4,8,9,11]
输出：false
解释：这是因为第 5 和第 6 个石子之间的间距太大，没有可选的方案供青蛙跳跃过去。
```
 

 **提示：** 
-  `2 <= stones.length <= 2000` 
-  `0 <= stones[i] <= 2^31 - 1` 
-  `stones[0] == 0` 
-  `stones` 按严格升序排列
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 404.左叶子之和
[https://leetcode-cn.com/problems/sum-of-left-leaves](https://leetcode-cn.com/problems/sum-of-left-leaves) 
## 原题
给定二叉树的根节点 `root` ，返回所有左叶子之和。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/04/08/leftsum-tree.jpg" />

```

输入: root = [3,9,20,null,null,15,7] 
输出: 24 
解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24

```
 **示例 2:** 

```

输入: root = [1]
输出: 0

```
 

 **提示:** 
- 节点数在 `[1, 1000]` 范围内
-  `-1000 <= Node.val <= 1000` 
 

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 405.数字转换为十六进制数
[https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal](https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal) 
## 原题
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 <a href="https://baike.baidu.com/item/%E8%A1%A5%E7%A0%81/6854613?fr=aladdin">补码运算</a> 方法。

 **注意:** 
- 十六进制中所有字母( `a-f` )都必须是小写。
- 十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符 `';0';` 来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
- 给定的数确保在32位有符号整数范围内。
-  **不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。** 
 **示例 1：** 

```

输入:
26

输出:
"1a"

```
 **示例 2：** 

```

输入:
-1

输出:
"ffffffff"

```
 
**标签**
`位运算` `数学` 


## 
```python

```
>
# 406.根据身高重建队列
[https://leetcode-cn.com/problems/queue-reconstruction-by-height](https://leetcode-cn.com/problems/queue-reconstruction-by-height) 
## 原题
假设有打乱顺序的一群人站成一个队列，数组 `people` 表示队列中一些人的属性（不一定按顺序）。每个 `people[i] = [h<sub>i</sub>, k<sub>i</sub>]` 表示第 `i` 个人的身高为 `h<sub>i</sub>` ，前面 **正好** 有 `k<sub>i</sub>` <sub> </sub>个身高大于或等于 `h<sub>i</sub>` 的人。

请你重新构造并返回输入数组  `people` 所表示的队列。返回的队列应该格式化为数组 `queue` ，其中 `queue[j] = [h<sub>j</sub>, k<sub>j</sub>]` 是队列中第 `j` 个人的属性（ `queue[0]` 是排在队列前面的人）。

 
 **示例 1：** 

```

输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
解释：
编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。

```
 **示例 2：** 

```

输入：people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
输出：[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

```
 

 **提示：** 
-  `1 <= people.length <= 2000` 
-  `0 <= h<sub>i</sub> <= 10^6` 
-  `0 <= k<sub>i</sub> < people.length` 
- 题目数据确保队列可以被重建
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 407.接雨水 II
[https://leetcode-cn.com/problems/trapping-rain-water-ii](https://leetcode-cn.com/problems/trapping-rain-water-ii) 
## 原题
给你一个 `m x n` 的矩阵，其中的值均为非负整数，代表二维高度图每个单元的高度，请计算图中形状最多能接多少体积的雨水。

 

 **示例 1:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap1-3d.jpg" />

```

输入: heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
输出: 4
解释: 下雨后，雨水将会被上图蓝色的方块中。总的接雨水量为1+2+1=4。

```
 **示例 2:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/trap2-3d.jpg" />

```

输入: heightMap = [[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]
输出: 10

```
 

 **提示:** 
-  `m == heightMap.length` 
-  `n == heightMap[i].length` 
-  `1 <= m, n <= 200` 
-  `0 <= heightMap[i][j] <= 2 * 10^4` 
 

 
**标签**
`广度优先搜索` `数组` `矩阵` `堆（优先队列）` 


## 
```python

```
>
# 408.有效单词缩写
[https://leetcode-cn.com/problems/valid-word-abbreviation](https://leetcode-cn.com/problems/valid-word-abbreviation) 
## 原题

 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 409.最长回文串
[https://leetcode-cn.com/problems/longest-palindrome](https://leetcode-cn.com/problems/longest-palindrome) 
## 原题
给定一个包含大写字母和小写字母的字符串<meta charset="UTF-8" /> `s` ，返回 *通过这些字母构造成的 **最长的回文串*** 。

在构造过程中，请注意 **区分大小写** 。比如 `"Aa"` 不能当做一个回文字符串。

 

 **示例 1:** 

```

输入:s = "abccccdd"
输出:7
解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。

```
 **示例 2:** 

```

输入:s = "a"
输入:1

```
 **示例 3:** 

```

输入:s = "bb"
输入: 2

```
 

 **提示:** 
-  `1 <= s.length <= 2000` 
-  `s` 只能由小写和/或大写英文字母组成
 
**标签**
`贪心` `哈希表` `字符串` 


## 
```python

```
>
# 410.分割数组的最大值
[https://leetcode-cn.com/problems/split-array-largest-sum](https://leetcode-cn.com/problems/split-array-largest-sum) 
## 原题
给定一个非负整数数组 `nums` 和一个整数 `m` ，你需要将这个数组分成 `m` 个非空的连续子数组。

设计一个算法使得这 `m` 个子数组各自和的最大值最小。

 

 **示例 1：** 

```

输入：nums = [7,2,5,10,8], m = 2
输出：18
解释：
一共有四种方法将 nums 分割为 2 个子数组。 
其中最好的方式是将其分为 [7,2,5] 和 [10,8] 。
因为此时这两个子数组各自的和的最大值为18，在所有情况中最小。
```
 **示例 2：** 

```

输入：nums = [1,2,3,4,5], m = 2
输出：9

```
 **示例 3：** 

```

输入：nums = [1,4,4], m = 3
输出：4

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `0 <= nums[i] <= 10^6` 
-  `1 <= m <= min(50, nums.length)` 
 
**标签**
`贪心` `数组` `二分查找` `动态规划` 


## 
```python

```
>
# 411.最短独占单词缩写
[https://leetcode-cn.com/problems/minimum-unique-word-abbreviation](https://leetcode-cn.com/problems/minimum-unique-word-abbreviation) 
## 原题

 
**标签**
`位运算` `字符串` `回溯` 


## 
```python

```
>
# 412.Fizz Buzz
[https://leetcode-cn.com/problems/fizz-buzz](https://leetcode-cn.com/problems/fizz-buzz) 
## 原题
给你一个整数 `n` ，找出从 `1` 到 `n` 各个整数的 Fizz Buzz 表示，并用字符串数组 `answer` （ **下标从 1 开始** ）返回结果，其中：
-  `answer[i] == "FizzBuzz"` 如果 `i` 同时是 `3` 和 `5` 的倍数。
-  `answer[i] == "Fizz"` 如果 `i` 是 `3` 的倍数。
-  `answer[i] == "Buzz"` 如果 `i` 是 `5` 的倍数。
-  `answer[i] == i` （以字符串形式）如果上述条件全不满足。
 

 **示例 1：** 

```

输入：n = 3
输出：["1","2","Fizz"]

```
 **示例 2：** 

```

输入：n = 5
输出：["1","2","Fizz","4","Buzz"]

```
 **示例 3：** 

```

输入：n = 15
输出：["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
```
 

 **提示：** 
-  `1 <= n <= 10^4` 
 
**标签**
`数学` `字符串` `模拟` 


## 
```python

```
>
# 413.等差数列划分
[https://leetcode-cn.com/problems/arithmetic-slices](https://leetcode-cn.com/problems/arithmetic-slices) 
## 原题
如果一个数列 **至少有三个元素** ，并且任意两个相邻元素之差相同，则称该数列为等差数列。
- 例如， `[1,3,5,7,9]` 、 `[7,7,7,7]` 和 `[3,-1,-5,-9]` 都是等差数列。
给你一个整数数组 `nums` ，返回数组 `nums` 中所有为等差数组的 **子数组** 个数。

 **子数组** 是数组中的一个连续序列。

 

 **示例 1：** 

```

输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。

```
 **示例 2：** 

```

输入：nums = [1]
输出：0

```
 

 **提示：** 
-  `1 <= nums.length <= 5000` 
-  `-1000 <= nums[i] <= 1000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 414.第三大的数
[https://leetcode-cn.com/problems/third-maximum-number](https://leetcode-cn.com/problems/third-maximum-number) 
## 原题
给你一个非空数组，返回此数组中 **第三大的数** 。如果不存在，则返回数组中最大的数。

 

 **示例 1：** 

```

输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。
```
 **示例 2：** 

```

输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。

```
 **示例 3：** 

```

输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
 

 **进阶：** 你能设计一个时间复杂度 `O(n)` 的解决方案吗？

 
**标签**
`数组` `排序` 


## 
```python

```
>
# 415.字符串相加
[https://leetcode-cn.com/problems/add-strings](https://leetcode-cn.com/problems/add-strings) 
## 原题
给定两个字符串形式的非负整数 `num1` 和 `num2` ，计算它们的和并同样以字符串形式返回。

你不能使用任何內建的用于处理大整数的库（比如 `BigInteger` ）， 也不能直接将输入的字符串转换为整数形式。

 

 **示例 1：** 

```

输入：num1 = "11", num2 = "123"
输出："134"

```
 **示例 2：** 

```

输入：num1 = "456", num2 = "77"
输出："533"

```
 **示例 3：** 

```

输入：num1 = "0", num2 = "0"
输出："0"

```
 

 

 **提示：** 
-  `1 <= num1.length, num2.length <= 10^4` 
-  `num1` 和 `num2` 都只包含数字 `0-9` 
-  `num1` 和 `num2` 都不包含任何前导零
 
**标签**
`数学` `字符串` `模拟` 


## 
```python

```
>
# 416.分割等和子集
[https://leetcode-cn.com/problems/partition-equal-subset-sum](https://leetcode-cn.com/problems/partition-equal-subset-sum) 
## 原题
给你一个 **只包含正整数** 的 **非空** 数组  `nums` 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

 

 **示例 1：** 

```

输入：nums = [1,5,11,5]
输出：true
解释：数组可以分割成 [1, 5, 5] 和 [11] 。
```
 **示例 2：** 

```

输入：nums = [1,2,3,5]
输出：false
解释：数组不能分割成两个元素和相等的子集。

```
 

 **提示：** 
-  `1 <= nums.length <= 200` 
-  `1 <= nums[i] <= 100` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 417.太平洋大西洋水流问题
[https://leetcode-cn.com/problems/pacific-atlantic-water-flow](https://leetcode-cn.com/problems/pacific-atlantic-water-flow) 
## 原题
有一个 `m × n` 的长方形岛屿，与 **太平洋** 和 **大西洋** 相邻。 **“太平洋”** 处于大陆的左边界和上边界，而 **“大西洋”** 处于大陆的右边界和下边界。

这个岛被分割成一个个方格网格。给定一个 `m x n` 的整数矩阵 `heights` ， `heights[r][c]` 表示坐标 `(r, c)` 上单元格 **高于海平面的高度** 。

岛上雨水较多，如果相邻小区的高度 **小于或等于** 当前小区的高度，雨水可以直接向北、南、东、西流向相邻小区。水可以从海洋附近的任何细胞流入海洋。

返回 *网格坐标 `result` 的 **2D列表** ，其中 `result[i] = [r<sub>i</sub>, c<sub>i</sub>]` 表示雨水可以从单元格 `(ri, ci)` 流向 **太平洋和大西洋*** 。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg" />

```

输入: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
输出: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

```
 **示例 2：** 

```

输入: heights = [[2,1],[1,2]]
输出: [[0,0],[0,1],[1,0],[1,1]]

```
 

 **提示：** 
-  `m == heights.length` 
-  `n == heights[r].length` 
-  `1 <= m, n <= 200` 
-  `0 <= heights[r][c] <= 10^5` 
 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 418.屏幕可显示句子的数量
[https://leetcode-cn.com/problems/sentence-screen-fitting](https://leetcode-cn.com/problems/sentence-screen-fitting) 
## 原题

 
**标签**
`字符串` `动态规划` `模拟` 


## 
```python

```
>
# 419.甲板上的战舰
[https://leetcode-cn.com/problems/battleships-in-a-board](https://leetcode-cn.com/problems/battleships-in-a-board) 
## 原题
给你一个大小为 `m x n` 的矩阵 `board` 表示甲板，其中，每个单元格可以是一艘战舰 `'X'` 或者是一个空位 `'.'` ，返回在甲板 `board` 上放置的 **战舰** 的数量。

 **战舰** 只能水平或者垂直放置在 `board` 上。换句话说，战舰只能按 `1 x k` （ `1` 行， `k` 列）或 `k x 1` （ `k` 行， `1` 列）的形状建造，其中 `k` 可以是任意大小。两艘战舰之间至少有一个水平或垂直的空位分隔 （即没有相邻的战舰）。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/10/battelship-grid.jpg" style="width: 333px; height: 333px;" />
```

输入：board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
输出：2

```
 **示例 2：** 

```

输入：board = [["."]]
输出：0

```
 

 **提示：** 
-  `m == board.length` 
-  `n == board[i].length` 
-  `1 <= m, n <= 200` 
-  `board[i][j]` 是 `'.'` 或 `'X'` 
 

 **进阶：** 你可以实现一次扫描算法，并只使用 **** `O(1)` **** 额外空间，并且不修改 `board` 的值来解决这个问题吗？

 
**标签**
`深度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 420.强密码检验器
[https://leetcode-cn.com/problems/strong-password-checker](https://leetcode-cn.com/problems/strong-password-checker) 
## 原题
 
如果一个密码满足下述所有条件，则认为这个密码是强密码：
- 由至少 `6` 个，至多 `20` 个字符组成。
- 至少包含 **一个小写** 字母， **一个大写** 字母，和 **一个数字** 。
- 同一字符 **不能** 连续出现三次 (比如 `"...aaa..."` 是不允许的, 但是 `"...aa...a..."` 如果满足其他条件也可以算是强密码)。
给你一个字符串 `password` ，返回 *将 `password` 修改到满足强密码条件需要的最少修改步数。如果 `password` 已经是强密码，则返回 `0` 。* 

在一步修改操作中，你可以：
- 插入一个字符到 `password` ，
- 从 `password` 中删除一个字符，或
- 用另一个字符来替换 `password` 中的某个字符。
 

 **示例 1：** 

```

输入：password = "a"
输出：5

```
 **示例 2：** 

```

输入：password = "aA1"
输出：3

```
 **示例 3：** 

```

输入：password = "1337C0d3"
输出：0

```
 

 **提示：** 
-  `1 <= password.length <= 50` 
-  `password` 由字母、数字、点 `'.'` 或者感叹号 `'!'` 
 
**标签**
`贪心` `字符串` `堆（优先队列）` 


## 
```python

```
>
# 421.数组中两个数的最大异或值
[https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array](https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array) 
## 原题
给你一个整数数组 `nums` ，返回 `nums[i] XOR nums[j]` 的最大运算结果，其中 `0 ≤ i ≤ j < n` 。

 **进阶：** 你可以在 `O(n)` 的时间解决这个问题吗？

 
 **示例 1：** 

```

输入：nums = [3,10,5,25,2,8]
输出：28
解释：最大运算结果是 5 XOR 25 = 28.
```
 **示例 2：** 

```

输入：nums = [0]
输出：0

```
 **示例 3：** 

```

输入：nums = [2,4]
输出：6

```
 **示例 4：** 

```

输入：nums = [8,10,2]
输出：10

```
 **示例 5：** 

```

输入：nums = [14,70,53,83,49,91,36,80,92,51,66,70]
输出：127

```
 

 **提示：** 
-  `1 <= nums.length <= 2 * 10^4` 
-  `0 <= nums[i] <= 2^31 - 1` 
 
**标签**
`位运算` `字典树` `数组` `哈希表` 


## 
```python

```
>
# 422.有效的单词方块
[https://leetcode-cn.com/problems/valid-word-square](https://leetcode-cn.com/problems/valid-word-square) 
## 原题

 
**标签**
`数组` `矩阵` 


## 
```python

```
>
# 423.从英文中重建数字
[https://leetcode-cn.com/problems/reconstruct-original-digits-from-english](https://leetcode-cn.com/problems/reconstruct-original-digits-from-english) 
## 原题
给你一个字符串 `s` ，其中包含字母顺序打乱的用英文单词表示的若干数字（ `0-9` ）。按 **升序** 返回原始的数字。

 

 **示例 1：** 

```

输入：s = "owoztneoer"
输出："012"

```
 **示例 2：** 

```

输入：s = "fviefuro"
输出："45"

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s[i]` 为 `["e","g","f","i","h","o","n","s","r","u","t","w","v","x","z"]` 这些字符之一
-  `s` 保证是一个符合题目要求的字符串
 
**标签**
`哈希表` `数学` `字符串` 


## 
```python

```
>
# 424.替换后的最长重复字符
[https://leetcode-cn.com/problems/longest-repeating-character-replacement](https://leetcode-cn.com/problems/longest-repeating-character-replacement) 
## 原题
给定一个字符串 `s` 和一个整数 `k` 。您可以选择字符串中的任意字符，并将其更改为任何其他大写英文字符。该操作最多可执行 `k` 次。

在执行上述操作后，返回 *包含相同字母的最长子字符串的长度* 。

 

 **示例 1：** 

```

输入：s = "ABAB", k = 2
输出：4
解释：用两个'A'替换为两个'B',反之亦然。

```
 **示例 2：** 

```

输入：s = "AABABBA", k = 1
输出：4
解释：
将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
子串 "BBBB" 有最长重复字母, 答案为 4。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s` 由小写英文字母组成
-  `0 <= k <= s.length` 
 
**标签**
`哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
# 425.单词方块
[https://leetcode-cn.com/problems/word-squares](https://leetcode-cn.com/problems/word-squares) 
## 原题

 
**标签**
`字典树` `数组` `字符串` `回溯` 


## 
```python

```
>
# 426.将二叉搜索树转化为排序的双向链表
[https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list](https://leetcode-cn.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list) 
## 原题

 
**标签**
`栈` `树` `深度优先搜索` `二叉搜索树` `链表` `二叉树` `双向链表` 


## 
```python

```
>
# 427.建立四叉树
[https://leetcode-cn.com/problems/construct-quad-tree](https://leetcode-cn.com/problems/construct-quad-tree) 
## 原题
给你一个 `n * n` 矩阵 `grid` ，矩阵由若干 `0` 和 `1` 组成。请你用四叉树表示该矩阵 `grid` 。

你需要返回能表示矩阵的 四叉树 的根结点。

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
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/new_top.png" style="height: 181px; width: 777px;">

如果你想了解更多关于四叉树的内容，可以参考 <a href="https://en.wikipedia.org/wiki/Quadtree">wiki</a> 。

 **四叉树格式：** 

输出为使用层序遍历后四叉树的序列化形式，其中 `null` 表示路径终止符，其下面不存在节点。

它与二叉树的序列化非常相似。唯一的区别是节点以列表形式表示 `[isLeaf, val]` 。

如果 `isLeaf` 或者 `val` 的值为 True ，则表示它在列表 `[isLeaf, val]` 中的值为 **1** ；如果 `isLeaf` 或者 `val` 的值为 False ，则表示值为 **0** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/11/grid1.png" style="height: 99px; width: 777px;">

```
输入：grid = [[0,1],[1,0]]
输出：[[0,1],[1,0],[1,1],[1,1],[1,0]]
解释：此示例的解释如下：
请注意，在下面四叉树的图示中，0 表示 false，1 表示 True 。
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e1tree.png" style="height: 186px; width: 777px;">

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e2mat.png" style="height: 343px; width: 777px;">

```
输入：grid = [[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0],[1,1,1,1,0,0,0,0]]
输出：[[0,1],[1,1],[0,1],[1,1],[1,0],null,null,null,null,[1,0],[1,0],[1,1],[1,1]]
解释：网格中的所有值都不相同。我们将网格划分为四个子网格。
topLeft，bottomLeft 和 bottomRight 均具有相同的值。
topRight 具有不同的值，因此我们将其再分为 4 个子网格，这样每个子网格都具有相同的值。
解释如下图所示：
<img alt="" src="https://assets.leetcode.com/uploads/2020/02/12/e2tree.png" style="height: 328px; width: 777px;">

```
 **示例 3：** 

```
输入：grid = [[1,1],[1,1]]
输出：[[1,1]]

```
 **示例 4：** 

```
输入：grid = [[0]]
输出：[[1,0]]

```
 **示例 5：** 

```
输入：grid = [[1,1,0,0],[1,1,0,0],[0,0,1,1],[0,0,1,1]]
输出：[[0,1],[1,1],[1,0],[1,0],[1,1]]

```
 

 **提示：** 
-  `n == grid.length == grid[i].length` 
-  `n == 2^x` 其中 `0 <= x <= 6` 
 
**标签**
`树` `数组` `分治` `矩阵` 


## 
```python

```
>
# 428.序列化和反序列化 N 叉树
[https://leetcode-cn.com/problems/serialize-and-deserialize-n-ary-tree](https://leetcode-cn.com/problems/serialize-and-deserialize-n-ary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `字符串` 


## 
```python

```
>
# 429.N 叉树的层序遍历
[https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal) 
## 原题
给定一个 N 叉树，返回其节点值的 *层序遍历* 。（即从左到右，逐层遍历）。

树的序列化输入是用层序遍历，每组子节点都由 null 值分隔（参见示例）。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" style="width: 100%; max-width: 300px;" />

```

输入：root = [1,null,3,2,4,null,5,6]
输出：[[1],[3,2,4],[5,6]]

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" style="width: 296px; height: 241px;" />

```

输入：root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
输出：[[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]

```
 

 **提示：** 
- 树的高度不会超过  `1000` 
- 树的节点总数在 `[0, 10^4]` 之间
 
**标签**
`树` `广度优先搜索` 


## 
```python

```
>
# 430.扁平化多级双向链表
[https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list](https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list) 
## 原题
你会得到一个双链表，其中包含的节点有一个下一个指针、一个前一个指针和一个额外的 **子指针** 。这个子指针可能指向一个单独的双向链表，也包含这些特殊的节点。这些子列表可以有一个或多个自己的子列表，以此类推，以生成如下面的示例所示的 **多层数据结构** 。

给定链表的头节点 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">head</span></span></font></font> ，将链表 **扁平化** ，以便所有节点都出现在单层双链表中。让 `curr` 是一个带有子列表的节点。子列表中的节点应该出现在 **扁平化列表** 中的 `curr` **之后** 和 `curr.next` **之前** 。

返回 *扁平列表的 `head` 。列表中的节点必须将其 **所有** 子指针设置为 `null` 。* 

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/11/09/flatten11.jpg" style="height:339px; width:700px" />

```

输入：head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
输出：[1,2,3,7,8,11,12,9,10,4,5,6]
解释：输入的多级列表如上图所示。
扁平化后的链表如下图：
<img src="https://assets.leetcode.com/uploads/2021/11/09/flatten12.jpg" style="height:69px; width:1000px" />

```
 **示例 2：** 

<img src="https://assets.leetcode.com/uploads/2021/11/09/flatten2.1jpg" style="height:200px; width:200px" />

```

输入：head = [1,2,null,3]
输出：[1,3,2]
解释：输入的多级列表如上图所示。
扁平化后的链表如下图：
<img src="https://assets.leetcode.com/uploads/2021/11/24/list.jpg" style="height:87px; width:300px" />

```
 **示例 3：** 

```

输入：head = []
输出：[]
说明：输入中可能存在空列表。

```
 

 **提示：** 
- 节点数目不超过 `1000` 
-  `1 <= Node.val <= 10^5` 
 

 **如何表示测试用例中的多级链表？** 

以 **示例 1** 为例：

```

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
```
序列化其中的每一级之后：

```

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]

```
为了将每一级都序列化到一起，我们需要每一级中添加值为 null 的元素，以表示没有节点连接到上一级的上级节点。

```

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]

```
合并所有序列化结果，并去除末尾的 null 。

```

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]

```
 
**标签**
`深度优先搜索` `链表` `双向链表` 


## 
```python

```
>
# 431.将 N 叉树编码为二叉树
[https://leetcode-cn.com/problems/encode-n-ary-tree-to-binary-tree](https://leetcode-cn.com/problems/encode-n-ary-tree-to-binary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `设计` `二叉树` 


## 
```python

```
>
# 432.全 O(1) 的数据结构
[https://leetcode-cn.com/problems/all-oone-data-structure](https://leetcode-cn.com/problems/all-oone-data-structure) 
## 原题
请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。

实现 `AllOne` 类：
-  `AllOne()` 初始化数据结构的对象。
-  `inc(String key)` 字符串 `key` 的计数增加 `1` 。如果数据结构中尚不存在 `key` ，那么插入计数为 `1` 的 `key` 。
-  `dec(String key)` 字符串 `key` 的计数减少 `1` 。如果 `key` 的计数在减少后为 `0` ，那么需要将这个 `key` 从数据结构中删除。测试用例保证：在减少计数前， `key` 存在于数据结构中。
-  `getMaxKey()` 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 `""` 。
-  `getMinKey()` 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 `""` 。
 

 **示例：** 

```

输入
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
输出
[null, null, null, "hello", "hello", null, "hello", "leet"]

解释
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "hello"
allOne.inc("leet");
allOne.getMaxKey(); // 返回 "hello"
allOne.getMinKey(); // 返回 "leet"

```
 

 **提示：** 
-  `1 <= key.length <= 10` 
-  `key` 由小写英文字母组成
- 测试用例保证：在每次调用 `dec` 时，数据结构中总存在 `key` 
- 最多调用 `inc` 、 `dec` 、 `getMaxKey` 和 `getMinKey` 方法 `5 * 10^4` 次
 
**标签**
`设计` `哈希表` `链表` `双向链表` 


## 
```python

```
>
# 433.最小基因变化
[https://leetcode-cn.com/problems/minimum-genetic-mutation](https://leetcode-cn.com/problems/minimum-genetic-mutation) 
## 原题
一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 `"A"` , `"C"` , `"G"` , `"T"` 中的任意一个。

假设我们要调查一个基因序列的变化。 **一次** 基因变化意味着这个基因序列中的 **一个** 字符发生了变化。

例如，基因序列由 `"AACCGGTT"`  变化至  `"AACCGGTA" ` 即发生了一次基因变化。

与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。

现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变化次数。如果无法实现目标变化，请返回 -1。

 **注意：** 
- 起始基因序列默认是合法的，但是它并不一定会出现在基因库中。
- 如果一个起始基因序列需要多次变化，那么它每一次变化之后的基因序列都必须是合法的。
- 假定起始基因序列与目标基因序列是不一样的。
 

 **示例 1：** 

```

start: "AACCGGTT"
end:   "AACCGGTA"
bank: ["AACCGGTA"]

返回值: 1

```
 **示例 2：** 

```

start: "AACCGGTT"
end:   "AAACGGTA"
bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]

返回值: 2

```
 **示例 3：** 

```

start: "AAAAACCC"
end:   "AACCCCCC"
bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]

返回值: 3

```
 
**标签**
`广度优先搜索` `哈希表` `字符串` 


## 
```python

```
>
# 434.字符串中的单词数
[https://leetcode-cn.com/problems/number-of-segments-in-a-string](https://leetcode-cn.com/problems/number-of-segments-in-a-string) 
## 原题
统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。

请注意，你可以假定字符串里不包括任何不可打印的字符。

 **示例:** 

```
输入: "Hello, my name is John"
输出: 5
解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。

```
 
**标签**
`字符串` 


## 
```python

```
>
# 435.无重叠区间
[https://leetcode-cn.com/problems/non-overlapping-intervals](https://leetcode-cn.com/problems/non-overlapping-intervals) 
## 原题
给定一个区间的集合 `intervals` ，其中 `intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]` 。返回 *需要移除区间的最小数量，使剩余区间互不重叠* 。

 

 **示例 1:** 

```

输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
输出: 1
解释: 移除 [1,3] 后，剩下的区间没有重叠。

```
 **示例 2:** 

```

输入: intervals = [ [1,2], [1,2], [1,2] ]
输出: 2
解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。

```
 **示例 3:** 

```

输入: intervals = [ [1,2], [2,3] ]
输出: 0
解释: 你不需要移除任何区间，因为它们已经是无重叠的了。

```
 

 **提示:** 
-  `1 <= intervals.length <= 10^5` 
-  `intervals[i].length == 2` 
-  `-5 * 10^4 <= start<sub>i</sub> < end<sub>i</sub> <= 5 * 10^4` 
 
**标签**
`贪心` `数组` `动态规划` `排序` 


## 
```python

```
>
# 436.寻找右区间
[https://leetcode-cn.com/problems/find-right-interval](https://leetcode-cn.com/problems/find-right-interval) 
## 原题
给你一个区间数组 `intervals` ，其中 `intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]` ，且每个 `start<sub>i</sub>` 都 **不同** 。

区间 `i` 的 **右侧区间** 可以记作区间 `j` ，并满足 `start<sub>j</sub>` `>= end<sub>i</sub>` ，且 `start<sub>j</sub>` **最小化** 。

返回一个由每个区间 `i` 的 **右侧区间** 的最小起始位置组成的数组。如果某个区间 `i` 不存在对应的 **右侧区间** ，则下标 `i` 处的值设为 `-1` 。
 

 **示例 1：** 

```

输入：intervals = [[1,2]]
输出：[-1]
解释：集合中只有一个区间，所以输出-1。

```
 **示例 2：** 

```

输入：intervals = [[3,4],[2,3],[1,2]]
输出：[-1,0,1]
解释：对于 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间[3,4]具有最小的“右”起点;
对于 [1,2] ，区间[2,3]具有最小的“右”起点。

```
 **示例 3：** 

```

输入：intervals = [[1,4],[2,3],[3,4]]
输出：[-1,2,-1]
解释：对于区间 [1,4] 和 [3,4] ，没有满足条件的“右侧”区间。
对于 [2,3] ，区间 [3,4] 有最小的“右”起点。

```
 

 **提示：** 
-  `1 <= intervals.length <= 2 * 10^4` 
-  `intervals[i].length == 2` 
-  `-10^6 <= start<sub>i</sub> <= end<sub>i</sub> <= 10^6` 
- 每个间隔的起点都 **不相同** 
 
**标签**
`数组` `二分查找` `排序` 


## 
```python

```
>
# 437.路径总和 III
[https://leetcode-cn.com/problems/path-sum-iii](https://leetcode-cn.com/problems/path-sum-iii) 
## 原题
给定一个二叉树的根节点 `root`  ，和一个整数 `targetSum` ，求该二叉树里节点值之和等于 `targetSum` 的 **路径** 的数目。

 **路径** 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/04/09/pathsum3-1-tree.jpg" style="width: 452px; " />

```

输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有 3 条，如图所示。

```
 **示例 2：** 

```

输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3

```
 

 **提示:** 
- 二叉树的节点个数的范围是 `[0,1000]` 
- <meta charset="UTF-8" /> `-10^9 <= Node.val <= 10^9`  
-  `-1000 <= targetSum <= 1000`  
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 438.找到字符串中所有字母异位词
[https://leetcode-cn.com/problems/find-all-anagrams-in-a-string](https://leetcode-cn.com/problems/find-all-anagrams-in-a-string) 
## 原题
给定两个字符串 `s` 和 `p` ，找到 `s` **** 中所有 `p` **** 的 **异位词** 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

 **异位词** 指由相同字母重排列形成的字符串（包括相同的字符串）。

 

 **示例 1:** 

```

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

```
 **示例 2:** 

```

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。

```
 

 **提示:** 
-  `1 <= s.length, p.length <= 3 * 10^4` 
-  `s` 和 `p` 仅包含小写字母
 
**标签**
`哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
# 439.三元表达式解析器
[https://leetcode-cn.com/problems/ternary-expression-parser](https://leetcode-cn.com/problems/ternary-expression-parser) 
## 原题

 
**标签**
`栈` `递归` `字符串` 


## 
```python

```
>
# 440.字典序的第K小数字
[https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order](https://leetcode-cn.com/problems/k-th-smallest-in-lexicographical-order) 
## 原题
给定整数 `n` 和 `k` ，返回 `[1, n]` 中字典序第 `k` 小的数字。

 

 **示例 1:** 

```

输入: n = 13, k = 2
输出: 10
解释: 字典序的排列是 [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]，所以第二小的数字是 10。

```
 **示例 2:** 

```

输入: n = 1, k = 1
输出: 1

```
 

 **提示:** 
-  `1 <= k <= n <= 10^9` 
 
**标签**
`字典树` 


## 
```python

```
>
# 441.排列硬币
[https://leetcode-cn.com/problems/arranging-coins](https://leetcode-cn.com/problems/arranging-coins) 
## 原题
你总共有 `n` 枚硬币，并计划将它们按阶梯状排列。对于一个由 `k` 行组成的阶梯，其第 `i` 行必须正好有 `i` 枚硬币。阶梯的最后一行 **可能** 是不完整的。

给你一个数字 `n` ，计算并返回可形成 **完整阶梯行** 的总行数。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/arrangecoins1-grid.jpg" style="width: 253px; height: 253px;" />
```

输入：n = 5
输出：2
解释：因为第三行不完整，所以返回 2 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/09/arrangecoins2-grid.jpg" style="width: 333px; height: 333px;" />
```

输入：n = 8
输出：3
解释：因为第四行不完整，所以返回 3 。

```
 

 **提示：** 
-  `1 <= n <= 2^31 - 1` 
 
**标签**
`数学` `二分查找` 


## 
```python

```
>
# 442.数组中重复的数据
[https://leetcode-cn.com/problems/find-all-duplicates-in-an-array](https://leetcode-cn.com/problems/find-all-duplicates-in-an-array) 
## 原题
给你一个长度为 `n` 的整数数组 `nums` ，其中 `nums` 的所有整数都在范围 `[1, n]` 内，且每个整数出现 **一次** 或 **两次** 。请你找出所有出现 **两次** 的整数，并以数组形式返回。

你必须设计并实现一个时间复杂度为 `O(n)` 且仅使用常量额外空间的算法解决此问题。

 

 **示例 1：** 

```

输入：nums = [4,3,2,7,8,2,3,1]
输出：[2,3]

```
 **示例 2：** 

```

输入：nums = [1,1,2]
输出：[1]

```
 **示例 3：** 

```

输入：nums = [1]
输出：[]

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 10^5` 
-  `1 <= nums[i] <= n` 
-  `nums` 中的每个元素出现 **一次** 或 **两次** 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 443.压缩字符串
[https://leetcode-cn.com/problems/string-compression](https://leetcode-cn.com/problems/string-compression) 
## 原题
给你一个字符数组 `chars` ，请使用下述算法压缩：

从一个空字符串 `s` 开始。对于 `chars` 中的每组 **连续重复字符** ：
- 如果这一组长度为 `1` ，则将字符追加到 `s` 中。
- 否则，需要向 `s` 追加字符，后跟这一组的长度。
压缩后得到的字符串 `s` **不应该直接返回** ，需要转储到字符数组 `chars` 中。需要注意的是，如果组长度为 `10` 或 `10` 以上，则在 `chars` 数组中会被拆分为多个字符。

请在 **修改完输入数组后** ，返回该数组的新长度。

你必须设计并实现一个只使用常量额外空间的算法来解决此问题。

 

 **示例 1：** 

```

输入：chars = ["a","a","b","b","c","c","c"]
输出：返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
解释：
"aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。

```
 **示例 2：** 

```

输入：chars = ["a"]
输出：返回 1 ，输入数组的前 1 个字符应该是：["a"]
解释：
没有任何字符串被替代。

```
 **示例 3：** 

```

输入：chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
输出：返回 4 ，输入数组的前 4 个字符应该是：["a","b","1","2"]。
解释：
由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
注意每个数字在数组中都有它自己的位置。

```
 

 **提示：** 
-  `1 <= chars.length <= 2000` 
-  `chars[i]` 可以是小写英文字母、大写英文字母、数字或符号
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 444.序列重建
[https://leetcode-cn.com/problems/sequence-reconstruction](https://leetcode-cn.com/problems/sequence-reconstruction) 
## 原题

 
**标签**
`图` `拓扑排序` `数组` 


## 
```python

```
>
# 445.两数相加 II
[https://leetcode-cn.com/problems/add-two-numbers-ii](https://leetcode-cn.com/problems/add-two-numbers-ii) 
## 原题
给你两个 **非空** 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

 

 **示例1：** 

<img alt="" src="https://pic.leetcode-cn.com/1626420025-fZfzMX-image.png" style="width: 302px; " />

```

输入：l1 = [7,2,4,3], l2 = [5,6,4]
输出：[7,8,0,7]

```
 **示例2：** 

```

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[8,0,7]

```
 **示例3：** 

```

输入：l1 = [0], l2 = [0]
输出：[0]

```
 

 **提示：** 
- 链表的长度范围为 `[1, 100]` 
-  `0 <= node.val <= 9` 
- 输入数据保证链表代表的数字无前导 0
 

 **进阶：** 如果输入链表不能翻转该如何解决？

 
**标签**
`栈` `链表` `数学` 


## 
```python

```
>
# 446.等差数列划分 II - 子序列
[https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence](https://leetcode-cn.com/problems/arithmetic-slices-ii-subsequence) 
## 原题
给你一个整数数组 `nums` ，返回 `nums` 中所有 **等差子序列** 的数目。

如果一个序列中 **至少有三个元素** ，并且任意两个相邻元素之差相同，则称该序列为等差序列。
- 例如， `[1, 3, 5, 7, 9]` 、 `[7, 7, 7, 7]` 和 `[3, -1, -5, -9]` 都是等差序列。
- 再例如， `[1, 1, 2, 5, 7]` 不是等差序列。
数组中的子序列是从数组中删除一些元素（也可能不删除）得到的一个序列。
- 例如， `[2,5,10]` 是 `[1,2,1, ***2*** ,4,1, ** *5* ** , ***10*** ]` 的一个子序列。
题目数据保证答案是一个 **32-bit** 整数。

 

 **示例 1：** 

```

输入：nums = [2,4,6,8,10]
输出：7
解释：所有的等差子序列为：
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]

```
 **示例 2：** 

```

输入：nums = [7,7,7,7,7]
输出：16
解释：数组中的任意子序列都是等差子序列。

```
 

 **提示：** 
-  `1  <= nums.length <= 1000` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 447.回旋镖的数量
[https://leetcode-cn.com/problems/number-of-boomerangs](https://leetcode-cn.com/problems/number-of-boomerangs) 
## 原题
给定平面上 `n` 对 **互不相同** 的点 `points` ，其中 `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` 。 **回旋镖** 是由点 `(i, j, k)` 表示的元组 ，其中 `i` 和 `j` 之间的距离和 `i` 和 `k` 之间的欧式距离相等（ **需要考虑元组的顺序** ）。

返回平面上所有回旋镖的数量。
 

 **示例 1：** 

```

输入：points = [[0,0],[1,0],[2,0]]
输出：2
解释：两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]

```
 **示例 2：** 

```

输入：points = [[1,1],[2,2],[3,3]]
输出：2

```
 **示例 3：** 

```

输入：points = [[1,1]]
输出：0

```
 

 **提示：** 
-  `n == points.length` 
-  `1 <= n <= 500` 
-  `points[i].length == 2` 
-  `-10^4 <= x<sub>i</sub>, y<sub>i</sub> <= 10^4` 
- 所有点都 **互不相同** 
 
**标签**
`数组` `哈希表` `数学` 


## 
```python

```
>
# 448.找到所有数组中消失的数字
[https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array](https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array) 
## 原题
给你一个含 `n` 个整数的数组 `nums` ，其中 `nums[i]` 在区间 `[1, n]` 内。请你找出所有在 `[1, n]` 范围内但没有出现在 `nums` 中的数字，并以数组的形式返回结果。

 

 **示例 1：** 

```

输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]

```
 **示例 2：** 

```

输入：nums = [1,1]
输出：[2]

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 10^5` 
-  `1 <= nums[i] <= n` 
 **进阶：** 你能在不使用额外空间且时间复杂度为 `O(n)` 的情况下解决这个问题吗? 你可以假定返回的数组不算在额外空间内。

 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 449.序列化和反序列化二叉搜索树
[https://leetcode-cn.com/problems/serialize-and-deserialize-bst](https://leetcode-cn.com/problems/serialize-and-deserialize-bst) 
## 原题
序列化是将数据结构或对象转换为一系列位的过程，以便它可以存储在文件或内存缓冲区中，或通过网络连接链路传输，以便稍后在同一个或另一个计算机环境中重建。

设计一个算法来序列化和反序列化 **二叉搜索树** 。 对序列化/反序列化算法的工作方式没有限制。 您只需确保二叉搜索树可以序列化为字符串，并且可以将该字符串反序列化为最初的二叉搜索树。

 **编码的字符串应尽可能紧凑。** 

 

 **示例 1：** 

```

输入：root = [2,1,3]
输出：[2,1,3]

```
 **示例 2：** 

```

输入：root = []
输出：[]

```
 

 **提示：** 
- 树中节点数范围是 `[0, 10^4]` 
-  `0 <= Node.val <= 10^4` 
- 题目数据 **保证** 输入的树是一棵二叉搜索树。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `设计` `二叉搜索树` `字符串` `二叉树` 


## 
```python

```
>
# 450.删除二叉搜索树中的节点
[https://leetcode-cn.com/problems/delete-node-in-a-bst](https://leetcode-cn.com/problems/delete-node-in-a-bst) 
## 原题
给定一个二叉搜索树的根节点 **root** 和一个值 **key** ，删除二叉搜索树中的 **key** 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：
- 首先找到需要删除的节点；
- 如果找到了，删除它。
 

 **示例 1:** 

<img src="https://assets.leetcode.com/uploads/2020/09/04/del_node_1.jpg" style="width: 800px;" />

```

输入：root = [5,3,6,2,4,null,7], key = 3
输出：[5,4,6,2,null,null,7]
解释：给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。
一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。
另一个正确答案是 [5,2,6,null,4,null,7]。

<img src="https://assets.leetcode.com/uploads/2020/09/04/del_node_supp.jpg" style="width: 350px;" />

```
 **示例 2:** 

```

输入: root = [5,3,6,2,4,null,7], key = 0
输出: [5,3,6,2,4,null,7]
解释: 二叉树不包含值为 0 的节点

```
 **示例 3:** 

```

输入: root = [], key = 0
输出: []
```
 

 **提示:** 
- 节点数的范围 `[0, 10^4]` .
-  `-10^5 <= Node.val <= 10^5` 
- 节点值唯一
-  `root` 是合法的二叉搜索树
-  `-10^5 <= key <= 10^5` 
 

 **进阶：** 要求算法时间复杂度为 O(h)，h 为树的高度。

 
**标签**
`树` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 451.根据字符出现频率排序
[https://leetcode-cn.com/problems/sort-characters-by-frequency](https://leetcode-cn.com/problems/sort-characters-by-frequency) 
## 原题
给定一个字符串，请将字符串里的字符按照出现的频率降序排列。

 **示例 1:** 

```

输入:
"tree"

输出:
"eert"

解释:
';e';出现两次，';r';和';t';都只出现一次。
因此';e';必须出现在';r';和';t';之前。此外，"eetr"也是一个有效的答案。

```
 **示例 2:** 

```

输入:
"cccaaa"

输出:
"cccaaa"

解释:
';c';和';a';都出现三次。此外，"aaaccc"也是有效的答案。
注意"cacaca"是不正确的，因为相同的字母必须放在一起。

```
 **示例 3:** 

```

输入:
"Aabb"

输出:
"bbAa"

解释:
此外，"bbaA"也是一个有效的答案，但"Aabb"是不正确的。
注意';A';和';a';被认为是两种不同的字符。

```
 
**标签**
`哈希表` `字符串` `桶排序` `计数` `排序` `堆（优先队列）` 


## 
```python

```
>
# 452.用最少数量的箭引爆气球
[https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons](https://leetcode-cn.com/problems/minimum-number-of-arrows-to-burst-balloons) 
## 原题
在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。

一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 `x` <sub> `start` ，</sub> `x` <sub> `end` ，</sub> 且满足   `x<sub>start</sub> ≤ x ≤ x` <sub> `end` ，</sub>则该气球会被引爆<sub>。</sub>可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

给你一个数组 `points` ，其中 `points [i] = [x<sub>start</sub>,x<sub>end</sub>]` ，返回引爆所有气球所必须射出的最小弓箭数。
 

 **示例 1：** 

```

输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球
```
 **示例 2：** 

```

输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4

```
 **示例 3：** 

```

输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2

```
 **示例 4：** 

```

输入：points = [[1,2]]
输出：1

```
 **示例 5：** 

```

输入：points = [[2,3],[2,3]]
输出：1

```
 

 **提示：** 
-  `1 <= points.length <= 10^4` 
-  `points[i].length == 2` 
-  `-2^31 <= x<sub>start</sub> < x<sub>end</sub> <= 2^31 - 1` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 453.最小操作次数使数组元素相等
[https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements](https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements) 
## 原题
给你一个长度为 `n` 的整数数组，每次操作将会使 `n - 1` 个元素增加 `1` 。返回让数组所有元素相等的最小操作次数。

 

 **示例 1：** 

```

输入：nums = [1,2,3]
输出：3
解释：
只需要3次操作（注意每次操作会增加两个元素的值）：
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

```
 **示例 2：** 

```

输入：nums = [1,1,1]
输出：0

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= nums.length <= 10^5` 
-  `-10^9 <= nums[i] <= 10^9` 
- 答案保证符合 **32-bit** 整数
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 454.四数相加 II
[https://leetcode-cn.com/problems/4sum-ii](https://leetcode-cn.com/problems/4sum-ii) 
## 原题
给你四个整数数组 `nums1` 、 `nums2` 、 `nums3` 和 `nums4` ，数组长度都是 `n` ，请你计算有多少个元组 `(i, j, k, l)` 能满足：
-  `0 <= i, j, k, l < n` 
-  `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0` 
 

 **示例 1：** 

```

输入：nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
输出：2
解释：
两个元组如下：
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0

```
 **示例 2：** 

```

输入：nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
输出：1

```
 

 **提示：** 
-  `n == nums1.length` 
-  `n == nums2.length` 
-  `n == nums3.length` 
-  `n == nums4.length` 
-  `1 <= n <= 200` 
-  `-2^28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2^28` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 455.分发饼干
[https://leetcode-cn.com/problems/assign-cookies](https://leetcode-cn.com/problems/assign-cookies) 
## 原题
假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。

对每个孩子 `i` ，都有一个胃口值  `g[i]` <sub>，</sub>这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 `j` ，都有一个尺寸 `s[j]` <sub> </sub>。如果 `s[j] >= g[i]` ，我们可以将这个饼干 `j` 分配给孩子 `i` ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。
 

 **示例 1:** 

```

输入: g = [1,2,3], s = [1,1]
输出: 1
解释: 
你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
所以你应该输出1。

```
 **示例 2:** 

```

输入: g = [1,2], s = [1,2,3]
输出: 2
解释: 
你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
你拥有的饼干数量和尺寸都足以让所有孩子满足。
所以你应该输出2.

```
 

 **提示：** 
-  `1 <= g.length <= 3 * 10^4` 
-  `0 <= s.length <= 3 * 10^4` 
-  `1 <= g[i], s[j] <= 2^31 - 1` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 456.132 模式
[https://leetcode-cn.com/problems/132-pattern](https://leetcode-cn.com/problems/132-pattern) 
## 原题
给你一个整数数组 `nums` ，数组中共有 `n` 个整数。 **132 模式的子序列** 由三个整数 `nums[i]` 、 `nums[j]` 和 `nums[k]` 组成，并同时满足： `i < j < k` 和 `nums[i] < nums[k] < nums[j]` 。

如果 `nums` 中存在 **132 模式的子序列** ，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：nums = [1,2,3,4]
输出：false
解释：序列中不存在 132 模式的子序列。

```
 **示例 2：** 

```

输入：nums = [3,1,4,2]
输出：true
解释：序列中有 1 个 132 模式的子序列： [1, 4, 2] 。

```
 **示例 3：** 

```

输入：nums = [-1,3,2,0]
输出：true
解释：序列中有 3 个 132 模式的的子序列：[-1, 3, 2]、[-1, 3, 0] 和 [-1, 2, 0] 。

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 2 * 10^5` 
-  `-10^9 <= nums[i] <= 10^9` 
 
**标签**
`栈` `数组` `二分查找` `有序集合` `单调栈` 


## 
```python

```
>
# 457.环形数组是否存在循环
[https://leetcode-cn.com/problems/circular-array-loop](https://leetcode-cn.com/problems/circular-array-loop) 
## 原题
存在一个不含 `0` 的 **环形** 数组 `nums` ，每个 `nums[i]` 都表示位于下标 `i` 的角色应该向前或向后移动的下标个数：
- 如果 `nums[i]` 是正数， **向前** （下标递增方向）移动 `|nums[i]|` 步
- 如果 `nums[i]` 是负数， **向后** （下标递减方向）移动 `|nums[i]|` 步
因为数组是 **环形** 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。

数组中的 **循环** 由长度为 `k` 的下标序列 `seq` 标识：
- 遵循上述移动规则将导致一组重复下标序列 `seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...` 
- 所有 `nums[seq[j]]` 应当不是 **全正** 就是 **全负** 
-  `k > 1` 
如果 `nums` 中存在循环，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：nums = [2,-1,1,2,2]
输出：true
解释：存在循环，按下标 0 -> 2 -> 3 -> 0 。循环长度为 3 。

```
 **示例 2：** 

```

输入：nums = [-1,2]
输出：false
解释：按下标 1 -> 1 -> 1 ... 的运动无法构成循环，因为循环的长度为 1 。根据定义，循环的长度必须大于 1 。

```
 **示例 3:** 

```

输入：nums = [-2,1,-1,-2,-2]
输出：false
解释：按下标 1 -> 2 -> 1 -> ... 的运动无法构成循环，因为 nums[1] 是正数，而 nums[2] 是负数。
所有 nums[seq[j]] 应当不是全正就是全负。
```
 

 **提示：** 
-  `1 <= nums.length <= 5000` 
-  `-1000 <= nums[i] <= 1000` 
-  `nums[i] != 0` 
 

 **进阶：** 你能设计一个时间复杂度为 `O(n)` 且额外空间复杂度为 `O(1)` 的算法吗？

 
**标签**
`数组` `哈希表` `双指针` 


## 
```python

```
>
# 458.可怜的小猪
[https://leetcode-cn.com/problems/poor-pigs](https://leetcode-cn.com/problems/poor-pigs) 
## 原题
有 `buckets` 桶液体，其中 **正好有一桶** 含有毒药，其余装的都是水。它们从外观看起来都一样。为了弄清楚哪只水桶含有毒药，你可以喂一些猪喝，通过观察猪是否会死进行判断。不幸的是，你只有 `minutesToTest` 分钟时间来确定哪桶液体是有毒的。

喂猪的规则如下：
- 选择若干活猪进行喂养
- 可以允许小猪同时饮用任意数量的桶中的水，并且该过程不需要时间。
- 小猪喝完水后，必须有 `minutesToDie` 分钟的冷却时间。在这段时间里，你只能观察，而不允许继续喂猪。
- 过了 `minutesToDie` 分钟后，所有喝到毒药的猪都会死去，其他所有猪都会活下来。
- 重复这一过程，直到时间用完。
给你桶的数目 `buckets` ， `minutesToDie` 和 `minutesToTest` ，返回 *在规定时间内判断哪个桶有毒所需的 **最小** 猪数* 。

 

 **示例 1：** 

```

输入：buckets = 1000, minutesToDie = 15, minutesToTest = 60
输出：5

```
 **示例 2：** 

```

输入：buckets = 4, minutesToDie = 15, minutesToTest = 15
输出：2

```
 **示例 3：** 

```

输入：buckets = 4, minutesToDie = 15, minutesToTest = 30
输出：2

```
 

 **提示：** 
-  `1 <= buckets <= 1000` 
-  `1 <= minutesToDie <= minutesToTest <= 100` 
 
**标签**
`数学` `动态规划` `组合数学` 


## 
```python

```
>
# 459.重复的子字符串
[https://leetcode-cn.com/problems/repeated-substring-pattern](https://leetcode-cn.com/problems/repeated-substring-pattern) 
## 原题
给定一个非空的字符串<meta charset="UTF-8" /> `s` ，检查是否可以通过由它的一个子串重复多次构成。

 

 **示例 1:** 

```

输入: s = "abab"
输出: true
解释: 可由子串 "ab" 重复两次构成。

```
 **示例 2:** 

```

输入: s = "aba"
输出: false

```
 **示例 3:** 

```

输入: s = "abcabcabcabc"
输出: true
解释: 可由子串 "abc" 重复四次构成。 (或子串 "abcabc" 重复两次构成。)

```
 

<b>提示：</b>

<meta charset="UTF-8" />
-  `1 <= s.length <= 10^4` 
-  `s` 由小写英文字母组成
 
**标签**
`字符串` `字符串匹配` 


## 
```python

```
>
# 460.LFU 缓存
[https://leetcode-cn.com/problems/lfu-cache](https://leetcode-cn.com/problems/lfu-cache) 
## 原题
请你为 <a href="https://baike.baidu.com/item/%E7%BC%93%E5%AD%98%E7%AE%97%E6%B3%95">最不经常使用（LFU）</a>缓存算法设计并实现数据结构。

实现 `LFUCache` 类：
-  `LFUCache(int capacity)` - 用数据结构的容量 `capacity` 初始化对象
-  `int get(int key)` - 如果键 `key` 存在于缓存中，则获取键的值，否则返回 `-1` 。
-  `void put(int key, int value)` - 如果键 `key` 已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量 `capacity` 时，则应该在插入新项之前，移除最不经常使用的项。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 **最近最久未使用** 的键。
为了确定最不常使用的键，可以为缓存中的每个键维护一个 **使用计数器** 。使用计数最小的键是最久未使用的键。

当一个键首次插入到缓存中时，它的使用计数器被设置为 `1` (由于 put 操作)。对缓存中的键执行 `get` 或 `put` 操作，使用计数器的值将会递增。

函数 `get` 和 `put` 必须以 `O(1)` 的平均时间复杂度运行。

 

 **示例：** 

```

输入：
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
输出：
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

解释：
// cnt(x) = 键 x 的使用计数
// cache=[] 将显示最后一次使用的顺序（最左边的元素是最近的）
LFUCache lfu = new LFUCache(2);
lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
lfu.get(1);      // 返回 1
                 // cache=[1,2], cnt(2)=1, cnt(1)=2
lfu.put(3, 3);   // 去除键 2 ，因为 cnt(2)=1 ，使用计数最小
                 // cache=[3,1], cnt(3)=1, cnt(1)=2
lfu.get(2);      // 返回 -1（未找到）
lfu.get(3);      // 返回 3
                 // cache=[3,1], cnt(3)=2, cnt(1)=2
lfu.put(4, 4);   // 去除键 1 ，1 和 3 的 cnt 相同，但 1 最久未使用
                 // cache=[4,3], cnt(4)=1, cnt(3)=2
lfu.get(1);      // 返回 -1（未找到）
lfu.get(3);      // 返回 3
                 // cache=[3,4], cnt(4)=1, cnt(3)=3
lfu.get(4);      // 返回 4
                 // cache=[3,4], cnt(4)=2, cnt(3)=3
```
 

 **提示：** 
-  `0 <= capacity <= 10^4` 
-  `0 <= key <= 10^5` 
-  `0 <= value <= 10^9` 
- 最多调用 `2 * 10^5` 次 `get` 和 `put` 方法
 
**标签**
`设计` `哈希表` `链表` `双向链表` 


## 
```python

```
>
# 461.汉明距离
[https://leetcode-cn.com/problems/hamming-distance](https://leetcode-cn.com/problems/hamming-distance) 
## 原题
两个整数之间的 <a href="https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E8%B7%9D%E7%A6%BB">汉明距离</a> 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 `x` 和 `y` ，计算并返回它们之间的汉明距离。

 

 **示例 1：** 

```

输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。

```
 **示例 2：** 

```

输入：x = 3, y = 1
输出：1

```
 

 **提示：** 
-  `0 <= x, y <= 2^31 - 1` 
 
**标签**
`位运算` 


## 
```python

```
>
# 462.最少移动次数使数组元素相等 II
[https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii](https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements-ii) 
## 原题
给定一个非空整数数组，找到使所有数组元素相等所需的最小移动数，其中每次移动可将选定的一个元素加1或减1。 您可以假设数组的长度最多为10000。

 **例如:** 

```

输入:
[1,2,3]

输出:
2

说明：
只有两个动作是必要的（记得每一步仅可使其中一个元素加1或减1）： 

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

```
 
**标签**
`数组` `数学` `排序` 


## 
```python

```
>
# 463.岛屿的周长
[https://leetcode-cn.com/problems/island-perimeter](https://leetcode-cn.com/problems/island-perimeter) 
## 原题
给定一个 `row x col` 的二维网格地图 `grid` ，其中： `grid[i][j] = 1` 表示陆地， `grid[i][j] = 0` 表示水域。

网格中的格子 **水平和垂直** 方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

 

 **示例 1：** 

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/island.png" />

```

输入：grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
输出：16
解释：它的周长是上面图片中的 16 个黄色的边
```
 **示例 2：** 

```

输入：grid = [[1]]
输出：4

```
 **示例 3：** 

```

输入：grid = [[1,0]]
输出：4

```
 

 **提示：** 
-  `row == grid.length` 
-  `col == grid[i].length` 
-  `1 <= row, col <= 100` 
-  `grid[i][j]` 为 `0` 或 `1` 
 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 464.我能赢吗
[https://leetcode-cn.com/problems/can-i-win](https://leetcode-cn.com/problems/can-i-win) 
## 原题
在 "100 game" 这个游戏中，两名玩家轮流选择从 `1` 到 `10` 的任意整数，累计整数和，先使得累计整数和 **达到或超过** 100 的玩家，即为胜者。

如果我们将游戏规则改为 “玩家 **不能** 重复使用整数” 呢？

例如，两个玩家可以轮流从公共整数池中抽取从 1 到 15 的整数（不放回），直到累计整数和 >= 100。

给定两个整数 `maxChoosableInteger` （整数池中可选择的最大数）和 `desiredTotal` （累计和），若先出手的玩家是否能稳赢则返回 `true` ，否则返回 `false` 。假设两位玩家游戏时都表现 **最佳** 。

 

 **示例 1：** 

```

输入：maxChoosableInteger = 10, desiredTotal = 11
输出：false
解释：
无论第一个玩家选择哪个整数，他都会失败。
第一个玩家可以选择从 1 到 10 的整数。
如果第一个玩家选择 1，那么第二个玩家只能选择从 2 到 10 的整数。
第二个玩家可以通过选择整数 10（那么累积和为 11 >= desiredTotal），从而取得胜利.
同样地，第一个玩家选择任意其他整数，第二个玩家都会赢。

```
 **示例 2:** 

```

输入：maxChoosableInteger = 10, desiredTotal = 0
输出：true

```
 **示例 3:** 

```

输入：maxChoosableInteger = 10, desiredTotal = 1
输出：true

```
 

 **提示:** 
-  `1 <= maxChoosableInteger <= 20` 
-  `0 <= desiredTotal <= 300` 
 
**标签**
`位运算` `记忆化搜索` `数学` `动态规划` `状态压缩` `博弈` 


## 
```python

```
>
# 465.最优账单平衡
[https://leetcode-cn.com/problems/optimal-account-balancing](https://leetcode-cn.com/problems/optimal-account-balancing) 
## 原题

 
**标签**
`数组` `回溯` 


## 
```python

```
>
# 466.统计重复个数
[https://leetcode-cn.com/problems/count-the-repetitions](https://leetcode-cn.com/problems/count-the-repetitions) 
## 原题
定义 `str = [s, n]` 表示 `str` 由 `n` 个字符串 `s` 连接构成。
- 例如， `str == ["abc", 3] =="abcabcabc"` 。
如果可以从 `s2` <sub> </sub>中删除某些字符使其变为 `s1` ，则称字符串 `s1` <sub> </sub>可以从字符串 `s2` 获得。
- 例如，根据定义， `s1 = "abc"` 可以从 `s2 = "ab ***dbe*** c"` 获得，仅需要删除加粗且用斜体标识的字符。
现在给你两个字符串 `s1`  和 `s2` 和两个整数 `n1` 和 `n2` 。由此构造得到两个字符串，其中 `str1 = [s1, n1]` 、 `str2 = [s2, n2]` 。

请你找出一个最大整数 `m` ，以满足 `str = [str2, m]` 可以从 `str1`  获得。

 

 **示例 1：** 

```

输入：s1 = "acb", n1 = 4, s2 = "ab", n2 = 2
输出：2

```
 **示例 2：** 

```

输入：s1 = "acb", n1 = 1, s2 = "acb", n2 = 1
输出：1

```
 

 **提示：** 
-  `1 <= s1.length, s2.length <= 100` 
-  `s1` 和 `s2` 由小写英文字母组成
-  `1 <= n1, n2 <= 10^6` 
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 467.环绕字符串中唯一的子字符串
[https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string](https://leetcode-cn.com/problems/unique-substrings-in-wraparound-string) 
## 原题
把字符串 `s` 看作是 `“abcdefghijklmnopqrstuvwxyz”` 的无限环绕字符串，所以 `s` 看起来是这样的：
-  `"...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd...."` . 
现在给定另一个字符串 `p` 。返回 *`s` 中 **唯一** 的 `p` 的 **非空子串** 的数量* 。 

 

 **示例 1:** 

```

输入: p = "a"
输出: 1
解释: 字符串 s 中只有一个"a"子字符。

```
 **示例 2:** 

```

输入: p = "cac"
输出: 2
解释: 字符串 s 中的字符串“cac”只有两个子串“a”、“c”。.

```
 **示例 3:** 

```

输入: p = "zab"
输出: 6
解释: 在字符串 s 中有六个子串“z”、“a”、“b”、“za”、“ab”、“zab”。

```
 

 **提示:** 
-  `1 <= p.length <= 10^5` 
-  `p` 由小写英文字母构成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 468.验证IP地址
[https://leetcode-cn.com/problems/validate-ip-address](https://leetcode-cn.com/problems/validate-ip-address) 
## 原题
给定一个字符串 `queryIP` 。如果是有效的 IPv4 地址，返回 `"IPv4"` ；如果是有效的 IPv6 地址，返回 `"IPv6"` ；如果不是上述类型的 IP 地址，返回 `"Neither"` 。

 **有效的IPv4地址** 是 `“x1.x2.x3.x4”` 形式的IP地址。 其中 `0 <= x<sub>i</sub> <= 255` 且 `x<sub>i</sub>` **不能包含** 前导零。例如: `“192.168.1.1”` 、 `“192.168.1.0”` 为有效IPv4地址， `“192.168.01.1”` 为无效IPv4地址; `“192.168.1.00”` 、 `“192.168@1.1”` 为无效IPv4地址。

 **一个有效的IPv6地址** 是一个格式为 `“x1:x2:x3:x4:x5:x6:x7:x8”` 的IP地址，其中:
-  `1 <= x<sub>i</sub>.length <= 4` 
-  `x<sub>i</sub>` 是一个 **十六进制字符串** ，可以包含数字、小写英文字母( `'a'` 到 `'f'` )和大写英文字母( `'A'` 到 `'F'` )。
- 在 `x<sub>i</sub>` 中允许前导零。
比如， `2001:0db8:85a3::8A2E:0370:7334` 和 `2001:db8:85a3:0:0:8A2E:0370:7334` 是有效的 IPv6 地址。而 `2001:0db8:85a3::8A2E:037j:7334` 和 `02001:0db8:85a3:0000:0000:8a2e:0370:7334` 是无效的。

 

 **示例 1：** 

```

输入：queryIP = "172.16.254.1"
输出："IPv4"
解释：有效的 IPv4 地址，返回 "IPv4"

```
 **示例 2：** 

```

输入：queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
输出："IPv6"
解释：有效的 IPv6 地址，返回 "IPv6"

```
 **示例 3：** 

```

输入：queryIP = "256.256.256.256"
输出："Neither"
解释：既不是 IPv4 地址，又不是 IPv6 地址

```
 

 **提示：** 
-  `queryIP` 仅由英文字母，数字，字符 `'.'` 和 `':'` 组成。
 
**标签**
`字符串` 


## 
```python

```
>
# 469.凸多边形
[https://leetcode-cn.com/problems/convex-polygon](https://leetcode-cn.com/problems/convex-polygon) 
## 原题

 
**标签**
`几何` `数学` 


## 
```python

```
>
# 470.用 Rand7() 实现 Rand10()
[https://leetcode-cn.com/problems/implement-rand10-using-rand7](https://leetcode-cn.com/problems/implement-rand10-using-rand7) 
## 原题
给定方法 `rand7` 可生成 `[1,7]` 范围内的均匀随机整数，试写一个方法 `rand10` 生成 `[1,10]` 范围内的均匀随机整数。

你只能调用 `rand7()` 且不能调用其他方法。请不要使用系统的 `Math.random()` 方法。
每个测试用例将有一个内部参数 `n` ，即你实现的函数 `rand10()` 在测试时将被调用的次数。请注意，这不是传递给 `rand10()` 的参数。

 

 **示例 1:** 

```

输入: 1
输出: [2]

```
 **示例 2:** 

```

输入: 2
输出: [2,8]

```
 **示例 3:** 

```

输入: 3
输出: [3,8,10]

```
 

 **提示:** 
-  `1 <= n <= 10^5` 
 

 **进阶:** 
-  `rand7()` 调用次数的 <a href="https://en.wikipedia.org/wiki/Expected_value" target="_blank">期望值</a> 是多少 ?
- 你能否尽量少调用 `rand7()` ?
 
**标签**
`数学` `拒绝采样` `概率与统计` `随机化` 


## 
```python

```
>
# 471.编码最短长度的字符串
[https://leetcode-cn.com/problems/encode-string-with-shortest-length](https://leetcode-cn.com/problems/encode-string-with-shortest-length) 
## 原题

 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 472.连接词
[https://leetcode-cn.com/problems/concatenated-words](https://leetcode-cn.com/problems/concatenated-words) 
## 原题
给你一个 **不含重复** 单词的字符串数组 `words` ，请你找出并返回 `words` 中的所有 **连接词** 。

 **连接词** 定义为：一个完全由给定数组中的至少两个较短单词组成的字符串。

 

 **示例 1：** 

```

输入：words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
输出：["catsdogcats","dogcatsdog","ratcatdogcat"]
解释："catsdogcats" 由 "cats", "dog" 和 "cats" 组成; 
     "dogcatsdog" 由 "dog", "cats" 和 "dog" 组成; 
     "ratcatdogcat" 由 "rat", "cat", "dog" 和 "cat" 组成。

```
 **示例 2：** 

```

输入：words = ["cat","dog","catdog"]
输出：["catdog"]
```
 

 **提示：** 
-  `1 <= words.length <= 10^4` 
-  `0 <= words[i].length <= 1000` 
-  `words[i]` 仅由小写字母组成
-  `0 <= sum(words[i].length) <= 10^5` 
 
**标签**
`深度优先搜索` `字典树` `数组` `字符串` `动态规划` 


## 
```python

```
>
# 473.火柴拼正方形
[https://leetcode-cn.com/problems/matchsticks-to-square](https://leetcode-cn.com/problems/matchsticks-to-square) 
## 原题
你将得到一个整数数组 `matchsticks` ，其中 `matchsticks[i]` 是第 `i` 个火柴棒的长度。你要用 **所有的火柴棍** 拼成一个正方形。你 **不能折断** 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 **使用一次** 。

如果你能使这个正方形，则返回 `true` ，否则返回 `false` 。

 

 **示例 1:** 

<img src="https://assets.leetcode.com/uploads/2021/04/09/matchsticks1-grid.jpg" />

```

输入: matchsticks = [1,1,2,2,2]
输出: true
解释: 能拼成一个边长为2的正方形，每边两根火柴。

```
 **示例 2:** 

```

输入: matchsticks = [3,3,3,3,4]
输出: false
解释: 不能用所有火柴拼成一个正方形。

```
 

 **提示:** 
-  `1 <= matchsticks.length <= 15` 
-  `1 <= matchsticks[i] <= 10^8` 
 
**标签**
`位运算` `数组` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 474.一和零
[https://leetcode-cn.com/problems/ones-and-zeroes](https://leetcode-cn.com/problems/ones-and-zeroes) 
## 原题
给你一个二进制字符串数组 `strs` 和两个整数 `m` 和 `n` 。
<p class="MachineTrans-lang-zh-CN">请你找出并返回 `strs` 的最大子集的长度，该子集中 **最多** 有 `m` 个 `0` 和 `n` 个 `1` 。

<p class="MachineTrans-lang-zh-CN">如果 `x` 的所有元素也是 `y` 的元素，集合 `x` 是集合 `y` 的 **子集** 。
 

 **示例 1：** 

```

输入：strs = ["10", "0001", "111001", "1", "0"], m = 5, n = 3
输出：4
解释：最多有 5 个 0 和 3 个 1 的最大子集是 {"10","0001","1","0"} ，因此答案是 4 。
其他满足题意但较小的子集包括 {"0001","1"} 和 {"10","1","0"} 。{"111001"} 不满足题意，因为它含 4 个 1 ，大于 n 的值 3 。

```
 **示例 2：** 

```

输入：strs = ["10", "0", "1"], m = 1, n = 1
输出：2
解释：最大的子集是 {"0", "1"} ，所以答案是 2 。

```
 

 **提示：** 
-  `1 <= strs.length <= 600` 
-  `1 <= strs[i].length <= 100` 
-  `strs[i]` 仅由 `'0'` 和 `'1'` 组成
-  `1 <= m, n <= 100` 
 
**标签**
`数组` `字符串` `动态规划` 


## 
```python

```
>
# 475.供暖器
[https://leetcode-cn.com/problems/heaters](https://leetcode-cn.com/problems/heaters) 
## 原题
冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。

在加热器的加热半径范围内的每个房屋都可以获得供暖。

现在，给出位于一条水平线上的房屋  `houses` 和供暖器  `heaters` 的位置，请你找出并返回可以覆盖所有房屋的最小加热半径。

 **说明** ：所有供暖器都遵循你的半径标准，加热的半径也一样。

 

 **示例 1:** 

```

输入: houses = [1,2,3], heaters = [2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。

```
 **示例 2:** 

```

输入: houses = [1,2,3,4], heaters = [1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。

```
 **示例 3：** 

```

输入：houses = [1,5], heaters = [2]
输出：3

```
 

 **提示：** 
-  `1 <= houses.length, heaters.length <= 3 * 10^4` 
-  `1 <= houses[i], heaters[i] <= 10^9` 
 
**标签**
`数组` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 476.数字的补数
[https://leetcode-cn.com/problems/number-complement](https://leetcode-cn.com/problems/number-complement) 
## 原题
对整数的二进制表示取反（ `0` 变 `1` ， `1` 变 `0` ）后，再转换为十进制表示，可以得到这个整数的补数。
- 例如，整数 `5` 的二进制表示是 `"101"` ，取反后得到 `"010"` ，再转回十进制表示得到补数 `2` 。
给你一个整数 `num` ，输出它的补数。

 
 **示例 1：** 

```

输入：num = 5
输出：2
解释：5 的二进制表示为 101（没有前导零位），其补数为 010。所以你需要输出 2 。

```
 **示例 2：** 

```

输入：num = 1
输出：0
解释：1 的二进制表示为 1（没有前导零位），其补数为 0。所以你需要输出 0 。

```
 

 **提示：** 
-  `1 <= num < 2^31` 
 

 **注意：** 本题与 1009 <a href="https://leetcode-cn.com/problems/complement-of-base-10-integer/">https://leetcode-cn.com/problems/complement-of-base-10-integer/</a> 相同

 
**标签**
`位运算` 


## 
```python

```
>
# 477.汉明距离总和
[https://leetcode-cn.com/problems/total-hamming-distance](https://leetcode-cn.com/problems/total-hamming-distance) 
## 原题
两个整数的 <a href="https://baike.baidu.com/item/%E6%B1%89%E6%98%8E%E8%B7%9D%E7%A6%BB/475174?fr=aladdin">汉明距离</a> 指的是这两个数字的二进制数对应位不同的数量。

给你一个整数数组 `nums` ，请你计算并返回 `nums` 中任意两个数之间 **汉明距离的总和** 。

 

 **示例 1：** 

```

输入：nums = [4,14,2]
输出：6
解释：在二进制表示中，4 表示为 0100 ，14 表示为 1110 ，2表示为 0010 。（这样表示是为了体现后四位之间关系）
所以答案为：
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = 2 + 2 + 2 = 6

```
 **示例 2：** 

```

输入：nums = [4,14,4]
输出：4

```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `0 <= nums[i] <= 10^9` 
- 给定输入的对应答案符合 **32-bit** 整数范围
 
**标签**
`位运算` `数组` `数学` 


## 
```python

```
>
# 478.在圆内随机生成点
[https://leetcode-cn.com/problems/generate-random-point-in-a-circle](https://leetcode-cn.com/problems/generate-random-point-in-a-circle) 
## 原题
给定圆的半径和圆心的位置，实现函数 `randPoint` ，在圆中产生均匀随机点。

实现 `Solution` 类:
-  `Solution(double radius, double x_center, double y_center)` 用圆的半径 `radius` 和圆心的位置 `(x_center, y_center)` 初始化对象
-  `randPoint()` 返回圆内的一个随机点。圆周上的一点被认为在圆内。答案作为数组返回 `[x, y]` 。
 

 **示例 1：** 

```

输入: 
["Solution","randPoint","randPoint","randPoint"]
[[1.0, 0.0, 0.0], [], [], []]
输出: [null, [-0.02493, -0.38077], [0.82314, 0.38945], [0.36572, 0.17248]]
解释:
Solution solution = new Solution(1.0, 0.0, 0.0);
solution.randPoint ();//返回[-0.02493，-0.38077]
solution.randPoint ();//返回[0.82314,0.38945]
solution.randPoint ();//返回[0.36572,0.17248]
```
 

 **提示：** 
-  `0 < radius <= 10^8` 
-  `-10^7 <= x_center, y_center <= 10^7` 
-  `randPoint` 最多被调用 `3 * 10^4` 次
 
**标签**
`几何` `数学` `拒绝采样` `随机化` 


## 
```python

```
>
# 479.最大回文数乘积
[https://leetcode-cn.com/problems/largest-palindrome-product](https://leetcode-cn.com/problems/largest-palindrome-product) 
## 原题
给定一个整数 n ，返回 *可表示为两个 `n` 位整数乘积的 **最大回文整数*** 。因为答案可能非常大，所以返回它对 `1337` **取余** 。

 

 **示例 1:** 

```

输入：n = 2
输出：987
解释：99 x 91 = 9009, 9009 % 1337 = 987

```
 **示例 2:** 

```

输入： n = 1
输出： 9

```
 

 **提示:** 
-  `1 <= n <= 8` 
 
**标签**
`数学` 


## 
```python

```
>
# 480.滑动窗口中位数
[https://leetcode-cn.com/problems/sliding-window-median](https://leetcode-cn.com/problems/sliding-window-median) 
## 原题
中位数是有序序列最中间的那个数。如果序列的长度是偶数，则没有最中间的数；此时中位数是最中间的两个数的平均数。

例如：
-  `[2,3,4]` ，中位数是  `3` 
-  `[2,3]` ，中位数是 `(2 + 3) / 2 = 2.5` 
给你一个数组 *nums* ，有一个长度为 *k* 的窗口从最左端滑动到最右端。窗口中有 *k* 个数，每次窗口向右移动 *1* 位。你的任务是找出每次窗口移动后得到的新窗口中元素的中位数，并输出由它们组成的数组。

 

 **示例：** 

给出  *nums* = `[1,3,-1,-3,5,3,6,7]` ，以及  *k* = 3。

```

窗口位置                      中位数
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7      -1
 1  3 [-1  -3  5] 3  6  7      -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6

```
 因此，返回该滑动窗口的中位数数组  `[1,-1,-1,3,5,6]` 。

 

 **提示：** 
- 你可以假设  `k`  始终有效，即： `k` 始终小于等于输入的非空数组的元素个数。
- 与真实值误差在 `10 ^ -5` 以内的答案将被视作正确答案。
 
**标签**
`数组` `哈希表` `滑动窗口` `堆（优先队列）` 


## 
```python

```
>
# 481.神奇字符串
[https://leetcode-cn.com/problems/magical-string](https://leetcode-cn.com/problems/magical-string) 
## 原题
神奇字符串 `s` 仅由 `'1'` 和 `'2'` 组成，并需要遵守下面的规则：
- 神奇字符串 s 的神奇之处在于，串联字符串中 `'1'` 和 `'2'` 的连续出现次数可以生成该字符串。
 `s` 的前几个元素是 `s = "1221121221221121122……"` 。如果将 `s` 中连续的若干 `1` 和 `2` 进行分组，可以得到 `"1 22 11 2 1 22 1 22 11 2 11 22 ......"` 。每组中 `1` 或者 `2` 的出现次数分别是 `"1 2 2 1 1 2 1 2 2 1 2 2 ......"` 。上面的出现次数正是 `s` 自身。

给你一个整数 `n` ，返回在神奇字符串 `s` 的前 `n` 个数字中 `1` 的数目。

 

 **示例 1：** 

```

输入：n = 6
输出：3
解释：神奇字符串 s 的前 6 个元素是 “122112”，它包含三个 1，因此返回 3 。 

```
 **示例 2：** 

```

输入：n = 1
输出：1

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 482.密钥格式化
[https://leetcode-cn.com/problems/license-key-formatting](https://leetcode-cn.com/problems/license-key-formatting) 
## 原题
给定一个许可密钥字符串 `s` ，仅由字母、数字字符和破折号组成。字符串由 `n` 个破折号分成 `n + 1` 组。你也会得到一个整数 `k` 。

我们想要重新格式化字符串 `s` ，使每一组包含 `k` 个字符，除了第一组，它可以比 `k` 短，但仍然必须包含至少一个字符。此外，两组之间必须插入破折号，并且应该将所有小写字母转换为大写字母。

返回 *重新格式化的许可密钥* 。

 

 **示例 1：** 

```

输入：S = "5F3Z-2e-9-w", k = 4
输出："5F3Z-2E9W"
解释：字符串 S 被分成了两个部分，每部分 4 个字符；
     注意，两个额外的破折号需要删掉。

```
 **示例 2：** 

```

输入：S = "2-5g-3-J", k = 2
输出："2-5G-3J"
解释：字符串 S 被分成了 3 个部分，按照前面的规则描述，第一部分的字符可以少于给定的数量，其余部分皆为 2 个字符。

```
 

 **提示:** 
-  `1 <= s.length <= 10^5` 
-  `s` 只包含字母、数字和破折号 `'-'` .
-  `1 <= k <= 10^4` 
 
**标签**
`字符串` 


## 
```python

```
>
# 483.最小好进制
[https://leetcode-cn.com/problems/smallest-good-base](https://leetcode-cn.com/problems/smallest-good-base) 
## 原题
以字符串的形式给出 `n` , 以字符串的形式返回 *`n` 的最小 **好进制*** 。

如果 `n` 的 `k(k>=2)` 进制数的所有数位全为1，则称 `k(k>=2)` 是 `n` 的一个 **好进制** 。

 

 **示例 1：** 

```

输入：n = "13"
输出："3"
解释：13 的 3 进制是 111。

```
 **示例 2：** 

```

输入：n = "4681"
输出："8"
解释：4681 的 8 进制是 11111。

```
 **示例 3：** 

```

输入：n = "1000000000000000000"
输出："999999999999999999"
解释：1000000000000000000 的 999999999999999999 进制是 11。

```
 

 **提示：** 
-  `n` 的取值范围是 `[3, 10^18]` 
-  `n` 没有前导 0
 
**标签**
`数学` `二分查找` 


## 
```python

```
>
# 484.寻找排列
[https://leetcode-cn.com/problems/find-permutation](https://leetcode-cn.com/problems/find-permutation) 
## 原题

 
**标签**
`栈` `贪心` `数组` 


## 
```python

```
>
# 485.最大连续 1 的个数
[https://leetcode-cn.com/problems/max-consecutive-ones](https://leetcode-cn.com/problems/max-consecutive-ones) 
## 原题
给定一个二进制数组 `nums` ， 计算其中最大连续 `1` 的个数。

 

 **示例 1：** 

```

输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.

```
 **示例 2:** 

```

输入：nums = [1,0,1,1,0,1]
输出：2

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `nums[i]` 不是 `0` 就是 `1` .
 
**标签**
`数组` 


## 
```python

```
>
# 486.预测赢家
[https://leetcode-cn.com/problems/predict-the-winner](https://leetcode-cn.com/problems/predict-the-winner) 
## 原题
给你一个整数数组 `nums` 。玩家 1 和玩家 2 基于这个数组设计了一个游戏。

玩家 1 和玩家 2 轮流进行自己的回合，玩家 1 先手。开始时，两个玩家的初始分值都是 `0` 。每一回合，玩家从数组的任意一端取一个数字（即， `nums[0]` 或 `nums[nums.length - 1]` ），取到的数字将会从数组中移除（数组长度减 `1` ）。玩家选中的数字将会加到他的得分上。当数组中没有剩余数字可取时，游戏结束。

如果玩家 1 能成为赢家，返回 `true` 。如果两个玩家得分相等，同样认为玩家 1 是游戏的赢家，也返回 `true` 。你可以假设每个玩家的玩法都会使他的分数最大化。

 

 **示例 1：** 

```

输入：nums = [1,5,2]
输出：false
解释：一开始，玩家 1 可以从 1 和 2 中进行选择。
如果他选择 2（或者 1 ），那么玩家 2 可以从 1（或者 2 ）和 5 中进行选择。如果玩家 2 选择了 5 ，那么玩家 1 则只剩下 1（或者 2 ）可选。 
所以，玩家 1 的最终分数为 1 + 2 = 3，而玩家 2 为 5 。
因此，玩家 1 永远不会成为赢家，返回 false 。
```
 **示例 2：** 

```

输入：nums = [1,5,233,7]
输出：true
解释：玩家 1 一开始选择 1 。然后玩家 2 必须从 5 和 7 中进行选择。无论玩家 2 选择了哪个，玩家 1 都可以选择 233 。
最终，玩家 1（234 分）比玩家 2（12 分）获得更多的分数，所以返回 true，表示玩家 1 可以成为赢家。
```
 

 **提示：** 
-  `1 <= nums.length <= 20` 
-  `0 <= nums[i] <= 10^7` 
 
**标签**
`递归` `数组` `数学` `动态规划` `博弈` 


## 
```python

```
>
# 487.最大连续1的个数 II
[https://leetcode-cn.com/problems/max-consecutive-ones-ii](https://leetcode-cn.com/problems/max-consecutive-ones-ii) 
## 原题

 
**标签**
`数组` `动态规划` `滑动窗口` 


## 
```python

```
>
# 488.祖玛游戏
[https://leetcode-cn.com/problems/zuma-game](https://leetcode-cn.com/problems/zuma-game) 
## 原题
你正在参与祖玛游戏的一个变种。

在这个祖玛游戏变体中，桌面上有 **一排** 彩球，每个球的颜色可能是：红色 `'R'` 、黄色 `'Y'` 、蓝色 `'B'` 、绿色 `'G'` 或白色 `'W'` 。你的手中也有一些彩球。

你的目标是 **清空** 桌面上所有的球。每一回合：
- 从你手上的彩球中选出 **任意一颗** ，然后将其插入桌面上那一排球中：两球之间或这一排球的任一端。
- 接着，如果有出现 **三个或者三个以上** 且 **颜色相同** 的球相连的话，就把它们移除掉。
	
- 如果这种移除操作同样导致出现三个或者三个以上且颜色相同的球相连，则可以继续移除这些球，直到不再满足移除条件。
	
	
- 如果桌面上所有球都被移除，则认为你赢得本场游戏。
- 重复这个过程，直到你赢了游戏或者手中没有更多的球。
给你一个字符串 `board` ，表示桌面上最开始的那排球。另给你一个字符串 `hand` ，表示手里的彩球。请你按上述操作步骤移除掉桌上所有球，计算并返回所需的 **最少** 球数。如果不能移除桌上所有的球，返回 `-1` 。

 

 **示例 1：** 

```

输入：board = "WRRBBW", hand = "RB"
输出：-1
解释：无法移除桌面上的所有球。可以得到的最好局面是：
- 插入一个 'R' ，使桌面变为 WRRRBBW 。WRRRBBW -> WBBW
- 插入一个 'B' ，使桌面变为 WBBBW 。WBBBW -> WW
桌面上还剩着球，没有其他球可以插入。
```
 **示例 2：** 

```

输入：board = "WWRRBBWW", hand = "WRBRW"
输出：2
解释：要想清空桌面上的球，可以按下述步骤：
- 插入一个 'R' ，使桌面变为 WWRRRBBWW 。WWRRRBBWW -> WWBBWW
- 插入一个 'B' ，使桌面变为 WWBBBWW 。WWBBBWW -> WWWW -> empty
只需从手中出 2 个球就可以清空桌面。

```
 **示例 3：** 

```

输入：board = "G", hand = "GGGGG"
输出：2
解释：要想清空桌面上的球，可以按下述步骤：
- 插入一个 'G' ，使桌面变为 GG 。
- 插入一个 'G' ，使桌面变为 GGG 。GGG -> empty
只需从手中出 2 个球就可以清空桌面。

```
 **示例 4：** 

```

输入：board = "RBYYBBRRB", hand = "YRBGB"
输出：3
解释：要想清空桌面上的球，可以按下述步骤：
- 插入一个 'Y' ，使桌面变为 RBYYYBBRRB 。RBYYYBBRRB -> RBBBRRB -> RRRB -> B
- 插入一个 'B' ，使桌面变为 BB 。
- 插入一个 'B' ，使桌面变为 BBB 。BBB -> empty
只需从手中出 3 个球就可以清空桌面。

```
 

 **提示：** 
-  `1 <= board.length <= 16` 
-  `1 <= hand.length <= 5` 
-  `board` 和 `hand` 由字符 `'R'` 、 `'Y'` 、 `'B'` 、 `'G'` 和 `'W'` 组成
- 桌面上一开始的球中，不会有三个及三个以上颜色相同且连着的球
 
**标签**
`广度优先搜索` `记忆化搜索` `字符串` `动态规划` 


## 
```python

```
>
# 489.扫地机器人
[https://leetcode-cn.com/problems/robot-room-cleaner](https://leetcode-cn.com/problems/robot-room-cleaner) 
## 原题

 
**标签**
`回溯` `交互` 


## 
```python

```
>
# 490.迷宫
[https://leetcode-cn.com/problems/the-maze](https://leetcode-cn.com/problems/the-maze) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `图` 


## 
```python

```
>
# 491.递增子序列
[https://leetcode-cn.com/problems/increasing-subsequences](https://leetcode-cn.com/problems/increasing-subsequences) 
## 原题
给你一个整数数组 `nums` ，找出并返回所有该数组中不同的递增子序列，递增子序列中 **至少有两个元素** 。你可以按 **任意顺序** 返回答案。

数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。

 

 **示例 1：** 

```

输入：nums = [4,6,7,7]
输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]

```
 **示例 2：** 

```

输入：nums = [4,4,3,2,1]
输出：[[4,4]]

```
 

 **提示：** 
-  `1 <= nums.length <= 15` 
-  `-100 <= nums[i] <= 100` 
 
**标签**
`位运算` `数组` `哈希表` `回溯` 


## 
```python

```
>
# 492.构造矩形
[https://leetcode-cn.com/problems/construct-the-rectangle](https://leetcode-cn.com/problems/construct-the-rectangle) 
## 原题
作为一位web开发者， 懂得怎样去规划一个页面的尺寸是很重要的。 所以，现给定一个具体的矩形页面面积，你的任务是设计一个长度为 L 和宽度为 W 且满足以下要求的矩形的页面。要求：
- 你设计的矩形页面必须等于给定的目标面积。
- 宽度 `W` 不应大于长度 `L` ，换言之，要求 `L >= W` 。
- 长度 `L` 和宽度 `W` 之间的差距应当尽可能小。
返回一个 *数组* `[L, W]` ，其中 *`L` 和 `W` 是你按照顺序设计的网页的长度和宽度* 。<br />
 

 **示例1：** 

```

输入: 4
输出: [2, 2]
解释: 目标面积是 4， 所有可能的构造方案有 [1,4], [2,2], [4,1]。
但是根据要求2，[1,4] 不符合要求; 根据要求3，[2,2] 比 [4,1] 更能符合要求. 所以输出长度 L 为 2， 宽度 W 为 2。

```
 **示例 2:** 

```

输入: area = 37
输出: [37,1]

```
 **示例 3:** 

```

输入: area = 122122
输出: [427,286]

```
 

 **提示:** 
-  `1 <= area <= 10^7` 
 
**标签**
`数学` 


## 
```python

```
>
# 493.翻转对
[https://leetcode-cn.com/problems/reverse-pairs](https://leetcode-cn.com/problems/reverse-pairs) 
## 原题
给定一个数组 `nums` ，如果 `i < j` 且 `nums[i] > 2*nums[j]` 我们就将 `(i, j)` 称作一个 ** *重要翻转对* ** 。

你需要返回给定数组中的重要翻转对的数量。

 **示例 1:** 

```

输入: [1,3,2,3,1]
输出: 2

```
 **示例 2:** 

```

输入: [2,4,3,5,1]
输出: 3

```
 **注意:** 
- 给定数组的长度不会超过 `50000` 。
- 输入数组中的所有数字都在32位整数的表示范围内。
 
**标签**
`树状数组` `线段树` `数组` `二分查找` `分治` `有序集合` `归并排序` 


## 
```python

```
>
# 494.目标和
[https://leetcode-cn.com/problems/target-sum](https://leetcode-cn.com/problems/target-sum) 
## 原题
给你一个整数数组 `nums` 和一个整数 `target` 。

向数组中的每个整数前添加  `'+'` 或 `'-'` ，然后串联起所有整数，可以构造一个 **表达式** ：
- 例如， `nums = [2, 1]` ，可以在 `2` 之前添加 `'+'` ，在 `1` 之前添加 `'-'` ，然后串联起来得到表达式 `"+2-1"` 。
返回可以通过上述方法构造的、运算结果等于 `target` 的不同 **表达式** 的数目。

 

 **示例 1：** 

```

输入：nums = [1,1,1,1,1], target = 3
输出：5
解释：一共有 5 种方法让最终目标和为 3 。
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3

```
 **示例 2：** 

```

输入：nums = [1], target = 1
输出：1

```
 

 **提示：** 
-  `1 <= nums.length <= 20` 
-  `0 <= nums[i] <= 1000` 
-  `0 <= sum(nums[i]) <= 1000` 
-  `-1000 <= target <= 1000` 
 
**标签**
`数组` `动态规划` `回溯` 


## 
```python

```
>
# 495.提莫攻击
[https://leetcode-cn.com/problems/teemo-attacking](https://leetcode-cn.com/problems/teemo-attacking) 
## 原题
在《英雄联盟》的世界中，有一个叫 “提莫” 的英雄。他的攻击可以让敌方英雄艾希（编者注：寒冰射手）进入中毒状态。

当提莫攻击艾希，艾希的中毒状态正好持续 `duration` 秒。

正式地讲，提莫在 `t` 发起发起攻击意味着艾希在时间区间 `[t, t + duration - 1]` （含 `t` 和 `t + duration - 1` ）处于中毒状态。如果提莫在中毒影响结束 **前** 再次攻击，中毒状态计时器将会 **重置** ，在新的攻击之后，中毒影响将会在 `duration` 秒后结束。

给你一个 **非递减** 的整数数组 `timeSeries` ，其中 `timeSeries[i]` 表示提莫在 `timeSeries[i]` 秒时对艾希发起攻击，以及一个表示中毒持续时间的整数 `duration` 。

返回艾希处于中毒状态的 **总** 秒数。
 

 **示例 1：** 

```

输入：timeSeries = [1,4], duration = 2
输出：4
解释：提莫攻击对艾希的影响如下：
- 第 1 秒，提莫攻击艾希并使其立即中毒。中毒状态会维持 2 秒，即第 1 秒和第 2 秒。
- 第 4 秒，提莫再次攻击艾希，艾希中毒状态又持续 2 秒，即第 4 秒和第 5 秒。
艾希在第 1、2、4、5 秒处于中毒状态，所以总中毒秒数是 4 。
```
 **示例 2：** 

```

输入：timeSeries = [1,2], duration = 2
输出：3
解释：提莫攻击对艾希的影响如下：
- 第 1 秒，提莫攻击艾希并使其立即中毒。中毒状态会维持 2 秒，即第 1 秒和第 2 秒。
- 第 2 秒，提莫再次攻击艾希，并重置中毒计时器，艾希中毒状态需要持续 2 秒，即第 2 秒和第 3 秒。
艾希在第 1、2、3 秒处于中毒状态，所以总中毒秒数是 3 。

```
 

 **提示：** 
-  `1 <= timeSeries.length <= 10^4` 
-  `0 <= timeSeries[i], duration <= 10^7` 
-  `timeSeries` 按 **非递减** 顺序排列
 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 496.下一个更大元素 I
[https://leetcode-cn.com/problems/next-greater-element-i](https://leetcode-cn.com/problems/next-greater-element-i) 
## 原题
 `nums1` 中数字 `x` 的 **下一个更大元素** 是指 `x` 在 `nums2` 中对应位置 **右侧** 的 **第一个** 比 `x` **** 大的元素。

给你两个 **没有重复元素** 的数组 `nums1` 和 `nums2` ，下标从 **0** 开始计数，其中 `nums1` 是 `nums2` 的子集。

对于每个 `0 <= i < nums1.length` ，找出满足 `nums1[i] == nums2[j]` 的下标 `j` ，并且在 `nums2` 确定 `nums2[j]` 的 **下一个更大元素** 。如果不存在下一个更大元素，那么本次查询的答案是 `-1` 。

返回一个长度为 `nums1.length` 的数组 `ans` 作为答案，满足 `ans[i]` 是如上所述的 **下一个更大元素** 。

 

 **示例 1：** 

```

输入：nums1 = [4,1,2], nums2 = [1,3,4,2].
输出：[-1,3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 4 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
- 1 ，用加粗斜体标识，nums2 = [1,3,4,2]。下一个更大元素是 3 。
- 2 ，用加粗斜体标识，nums2 = [1,3,4,2]。不存在下一个更大元素，所以答案是 -1 。
```
 **示例 2：** 

```

输入：nums1 = [2,4], nums2 = [1,2,3,4].
输出：[3,-1]
解释：nums1 中每个值的下一个更大元素如下所述：
- 2 ，用加粗斜体标识，nums2 = [1,2,3,4]。下一个更大元素是 3 。
- 4 ，用加粗斜体标识，nums2 = [1,2,3,4]。不存在下一个更大元素，所以答案是 -1 。

```
 

 **提示：** 
-  `1 <= nums1.length <= nums2.length <= 1000` 
-  `0 <= nums1[i], nums2[i] <= 10^4` 
-  `nums1` 和 `nums2` 中所有整数 **互不相同** 
-  `nums1` 中的所有整数同样出现在 `nums2` 中
 

 **进阶：** 你可以设计一个时间复杂度为 `O(nums1.length + nums2.length)` 的解决方案吗？

 
**标签**
`栈` `数组` `哈希表` `单调栈` 


## 
```python

```
>
# 497.非重叠矩形中的随机点
[https://leetcode-cn.com/problems/random-point-in-non-overlapping-rectangles](https://leetcode-cn.com/problems/random-point-in-non-overlapping-rectangles) 
## 原题
给定一个由非重叠的轴对齐矩形的数组 `rects` ，其中 `rects[i] = [ai, bi, xi, yi]` 表示 `(ai, bi)` 是第 `i` 个矩形的左下角点， `(xi, yi)` 是第 `i` 个矩形的右上角角点。设计一个算法来挑选一个随机整数点内的空间所覆盖的一个给定的矩形。矩形周长上的一个点包含在矩形覆盖的空间中。

在一个给定的矩形覆盖的空间内任何整数点都有可能被返回。

 **请注意** ，整数点是具有整数坐标的点。

实现 `Solution` 类:
-  `Solution(int[][] rects)` 用给定的矩形数组 `rects` 初始化对象。
-  `int[] pick()` 返回一个随机的整数点 `[u, v]` 在给定的矩形所覆盖的空间内。
 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/07/24/lc-pickrandomrec.jpg" style="height: 539px; width: 419px;" />

```

输入: 
["Solution","pick","pick","pick","pick","pick"]
[[[[-2,-2,-1,-1],[1,0,3,0]]],[],[],[],[],[]]
输出: 
[null,[-1,-2],[2,0],[-2,-1],[3,0],[-2,-2]

解释：
Solution solution = new Solution([[-2, -2, 1, 1], [2, 2, 4, 6]]);
solution.pick(); // 返回 [1, -2]
solution.pick(); // 返回 [1, -1]
solution.pick(); // 返回 [-1, -2]
solution.pick(); // 返回 [-2, -2]
solution.pick(); // 返回 [0, 0]
```
 

 **提示：** 
-  `1 <= rects.length <= 100` 
-  `rects[i].length == 4` 
-  `-10^9 <= a<sub>i</sub> < x<sub>i</sub> <= 10^9` 
-  `-10^9 <= b<sub>i</sub> < y<sub>i</sub> <= 10^9` 
-  `x<sub>i</sub> - a<sub>i</sub> <= 2000` 
-  `y<sub>i</sub> - b<sub>i</sub> <= 2000` 
- 所有的矩形不重叠。
-  `pick` 最多被调用 `10^4` 次。
 

 
**标签**
`水塘抽样` `数学` `二分查找` `有序集合` `前缀和` `随机化` 


## 
```python

```
>
# 498.对角线遍历
[https://leetcode-cn.com/problems/diagonal-traverse](https://leetcode-cn.com/problems/diagonal-traverse) 
## 原题
给你一个大小为 `m x n` 的矩阵 `mat` ，请以对角线遍历的顺序，用一个数组返回这个矩阵中的所有元素。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/10/diag1-grid.jpg" style="width: 334px; height: 334px;" />
```

输入：mat = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,4,7,5,3,6,8,9]

```
 **示例 2：** 

```

输入：mat = [[1,2],[3,4]]
输出：[1,2,3,4]

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat[i].length` 
-  `1 <= m, n <= 10^4` 
-  `1 <= m * n <= 10^4` 
-  `-10^5 <= mat[i][j] <= 10^5` 
 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 499.迷宫 III
[https://leetcode-cn.com/problems/the-maze-iii](https://leetcode-cn.com/problems/the-maze-iii) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `图` `最短路` `堆（优先队列）` 


## 
```python

```
>
# 500.键盘行
[https://leetcode-cn.com/problems/keyboard-row](https://leetcode-cn.com/problems/keyboard-row) 
## 原题
给你一个字符串数组 `words` ，只返回可以使用在 **美式键盘** 同一行的字母打印出来的单词。键盘如下图所示。

 **美式键盘** 中：
- 第一行由字符 `"qwertyuiop"` 组成。
- 第二行由字符 `"asdfghjkl"` 组成。
- 第三行由字符 `"zxcvbnm"` 组成。
<img alt="American keyboard" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/keyboard.png" style="width: 100%; max-width: 600px" />

 

 **示例 1：** 

```

输入：words = ["Hello","Alaska","Dad","Peace"]
输出：["Alaska","Dad"]

```
 **示例 2：** 

```

输入：words = ["omk"]
输出：[]

```
 **示例 3：** 

```

输入：words = ["adsdf","sfd"]
输出：["adsdf","sfd"]

```
 

 **提示：** 
-  `1 <= words.length <= 20` 
-  `1 <= words[i].length <= 100` 
-  `words[i]` 由英文字母（小写和大写字母）组成
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
