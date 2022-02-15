# 1001.网格照明
[https://leetcode-cn.com/problems/grid-illumination](https://leetcode-cn.com/problems/grid-illumination) 
## 原题
在大小为 `n x n` 的网格 `grid` 上，每个单元格都有一盏灯，最初灯都处于 **关闭** 状态。

给你一个由灯的位置组成的二维数组 `lamps` ，其中 `lamps[i] = [row<sub>i</sub>, col<sub>i</sub>]` 表示 **打开** 位于 `grid[row<sub>i</sub>][col<sub>i</sub>]` 的灯。即便同一盏灯可能在 `lamps` 中多次列出，不会影响这盏灯处于 **打开** 状态。

当一盏灯处于打开状态，它将会照亮 **自身所在单元格** 以及同一 **行** 、同一 **列** 和两条 **对角线** 上的 **所有其他单元格** 。

另给你一个二维数组 `queries` ，其中 `queries[j] = [row<sub>j</sub>, col<sub>j</sub>]` 。对于第 `j` 个查询，如果单元格 `[row<sub>j</sub>, col<sub>j</sub>]` 是被照亮的，则查询结果为 `1` ，否则为 `0` 。在第 `j` 次查询之后 [按照查询的顺序] ， **关闭** 位于单元格 `grid[row<sub>j</sub>][col<sub>j</sub>]` 上及相邻 8 个方向上（与单元格 `grid[row<sub>i</sub>][col<sub>i</sub>]` 共享角或边）的任何灯。

返回一个整数数组 `ans` 作为答案， `ans[j]` 应等于第 `j` 次查询 `queries[j]` 的结果， `1` 表示照亮， `0` 表示未照亮。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_1.jpg" style="height: 209px; width: 750px;" />
```

输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
输出：[1,0]
解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。第 0 次查询检查 grid[1][1] 是否被照亮（蓝色方框）。该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_step1.jpg" style="height: 218px; width: 500px;" />
第 1 次查询检查 grid[1][0] 是否被照亮（蓝色方框）。该单元格没有被照亮，所以 ans[1] = 0 。然后，关闭红色矩形中的所有灯。
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_step2.jpg" style="height: 219px; width: 500px;" />

```
 **示例 2：** 

```

输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
输出：[1,1]

```
 **示例 3：** 

```

输入：n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
输出：[1,1,0]

```
 

 **提示：** 
-  `1 <= n <= 10^9` 
-  `0 <= lamps.length <= 20000` 
-  `0 <= queries.length <= 20000` 
-  `lamps[i].length == 2` 
-  `0 <= row<sub>i</sub>, col<sub>i</sub> < n` 
-  `queries[j].length == 2` 
-  `0 <= row<sub>j</sub>, col<sub>j</sub> < n` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1002.查找共用字符
[https://leetcode-cn.com/problems/find-common-characters](https://leetcode-cn.com/problems/find-common-characters) 
## 原题
给你一个字符串数组 `words` ，请你找出所有在 `words` 的每个字符串中都出现的共用字符（ **包括重复字符** ），并以数组形式返回。你可以按 **任意顺序** 返回答案。
 

 **示例 1：** 

```

输入：words = ["bella","label","roller"]
输出：["e","l","l"]

```
 **示例 2：** 

```

输入：words = ["cool","lock","cook"]
输出：["c","o"]

```
 

 **提示：** 
-  `1 <= words.length <= 100` 
-  `1 <= words[i].length <= 100` 
-  `words[i]` 由小写英文字母组成
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 1003.检查替换后的词是否有效
[https://leetcode-cn.com/problems/check-if-word-is-valid-after-substitutions](https://leetcode-cn.com/problems/check-if-word-is-valid-after-substitutions) 
## 原题
给你一个字符串 `s` ，请你判断它是否 **有效** 。
字符串 `s` **有效** 需要满足：假设开始有一个空字符串 `t = ""` ，你可以执行 **任意次** 下述操作将 **** `t` **转换为** `s` ：
- 将字符串 `"abc"` 插入到 `t` 中的任意位置。形式上， `t` 变为 `t<sub>left</sub> + "abc" + t<sub>right</sub>` ，其中 `t == t<sub>left</sub> + t<sub>right</sub>` 。注意， `t<sub>left</sub>` 和 `t<sub>right</sub>` 可能为 **空** 。
如果字符串 `s` 有效，则返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：s = "aabcbc"
输出：true
解释：
"" -> "abc" -> "aabcbc"
因此，"aabcbc" 有效。
```
 **示例 2：** 

```

输入：s = "abcabcababcc"
输出：true
解释：
"" -> "abc" -> "abcabc" -> "abcabcabc" -> "abcabcababcc"
因此，"abcabcababcc" 有效。
```
 **示例 3：** 

```

输入：s = "abccba"
输出：false
解释：执行操作无法得到 "abccba" 。
```
 **示例 4：** 

```

输入：s = "cababc"
输出：false
解释：执行操作无法得到 "cababc" 。
```
 

 **提示：** 
-  `1 <= s.length <= 2 * 10^4` 
-  `s` 由字母 `'a'` 、 `'b'` 和 `'c'` 组成
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 1004.最大连续1的个数 III
[https://leetcode-cn.com/problems/max-consecutive-ones-iii](https://leetcode-cn.com/problems/max-consecutive-ones-iii) 
## 原题
给定一个二进制数组 `nums` 和一个整数 `<font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">k</span></span></font></font>` ，如果可以翻转最多 `<font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">k</span></span></font></font>` 个 `0` ，则返回 *数组中连续 `1` 的最大个数* 。

 

 **示例 1：** 

```

输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
输出：6
解释：[1,1,1,0,0,1,1,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 6。
```
 **示例 2：** 

```

输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
输出：10
解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
粗体数字从 0 翻转到 1，最长的子数组长度为 10。
```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `nums[i]` 不是 `0` 就是 `1` 
-  `0 <= k <= nums.length` 
 
**标签**
`数组` `二分查找` `前缀和` `滑动窗口` 


## 
```python

```
>
# 1005.K 次取反后最大化的数组和
[https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations](https://leetcode-cn.com/problems/maximize-sum-of-array-after-k-negations) 
## 原题
给你一个整数数组 `nums` 和一个整数 `k` ，按以下方法修改该数组：
- 选择某个下标 `i` 并将 `nums[i]` 替换为 `-nums[i]` 。
重复这个过程恰好 `k` 次。可以多次选择同一个下标 `i` 。

以这种方式修改数组后，返回数组 **可能的最大和** 。

 

 **示例 1：** 

```

输入：nums = [4,2,3], k = 1
输出：5
解释：选择下标 1 ，nums 变为 [4,-2,3] 。

```
 **示例 2：** 

```

输入：nums = [3,-1,0,2], k = 3
输出：6
解释：选择下标 (1, 2, 2) ，nums 变为 [3,1,0,2] 。

```
 **示例 3：** 

```

输入：nums = [2,-3,-1,5,-4], k = 2
输出：13
解释：选择下标 (1, 4) ，nums 变为 [2,3,-1,5,4] 。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `-100 <= nums[i] <= 100` 
-  `1 <= k <= 10^4` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1006.笨阶乘
[https://leetcode-cn.com/problems/clumsy-factorial](https://leetcode-cn.com/problems/clumsy-factorial) 
## 原题
通常，正整数 `n` 的阶乘是所有小于或等于 `n` 的正整数的乘积。例如， `factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1` 。

相反，我们设计了一个笨阶乘 `clumsy` ：在整数的递减序列中，我们以一个固定顺序的操作符序列来依次替换原有的乘法操作符：乘法(*)，除法(/)，加法(+)和减法(-)。

例如， `clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1` 。然而，这些运算仍然使用通常的算术运算顺序：我们在任何加、减步骤之前执行所有的乘法和除法步骤，并且按从左到右处理乘法和除法步骤。

另外，我们使用的除法是地板除法（ *floor division* ），所以 `10 * 9 / 8` 等于 `11` 。这保证结果是一个整数。

实现上面定义的笨函数：给定一个整数 `N` ，它返回 `N` 的笨阶乘。

 

 **示例 1：** 

```
输入：4
输出：7
解释：7 = 4 * 3 / 2 + 1

```
 **示例 2：** 

```
输入：10
输出：12
解释：12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

```
 

 **提示：** 
-  `1 <= N <= 10000` 
-  `-2^31 <= answer <= 2^31 - 1` （答案保证符合 32 位整数。）
 
**标签**
`栈` `数学` `模拟` 


## 
```python

```
>
# 1007.行相等的最少多米诺旋转
[https://leetcode-cn.com/problems/minimum-domino-rotations-for-equal-row](https://leetcode-cn.com/problems/minimum-domino-rotations-for-equal-row) 
## 原题
在一排多米诺骨牌中， `A[i]` 和 `B[i]` 分别代表第 i 个多米诺骨牌的上半部分和下半部分。（一个多米诺是两个从 1 到 6 的数字同列平铺形成的 &mdash;&mdash; 该平铺的每一半上都有一个数字。）

我们可以旋转第 `i` 张多米诺，使得 `A[i]` 和 `B[i]` 的值交换。

返回能使 `A` 中所有值或者 `B` 中所有值都相同的最小旋转次数。

如果无法做到，返回 `-1` .

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/03/08/domino.png" style="height: 161px; width: 200px;">

```
输入：A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
输出：2
解释：
图一表示：在我们旋转之前， A 和 B 给出的多米诺牌。
如果我们旋转第二个和第四个多米诺骨牌，我们可以使上面一行中的每个值都等于 2，如图二所示。

```
 **示例 2：** 

```
输入：A = [3,5,1,2,3], B = [3,6,3,3,4]
输出：-1
解释：
在这种情况下，不可能旋转多米诺牌使一行的值相等。

```
 

 **提示：** 
-  `1 <= A[i], B[i] <= 6` 
-  `2 <= A.length == B.length <= 20000` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1008.前序遍历构造二叉搜索树
[https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal](https://leetcode-cn.com/problems/construct-binary-search-tree-from-preorder-traversal) 
## 原题
给定一个整数数组，它表示BST(即 **二叉搜索树** )的 **先** **序遍历** ，构造树并返回其根。

 **保证** 对于给定的测试用例，总是有可能找到具有给定需求的二叉搜索树。

 **二叉搜索树** 是一棵二叉树，其中每个节点， `Node.left` 的任何后代的值 **严格小于** `Node.val` , `Node.right` 的任何后代的值 **严格大于** `Node.val` 。

二叉树的 **前序遍历** 首先显示节点的值，然后遍历 `Node.left` ，最后遍历 `Node.right` 。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2019/03/06/1266.png" />

```

输入：preorder = [8,5,1,7,10,12]
输出：[8,5,10,1,7,null,12]

```
 **示例 2:** 

```

输入: preorder = [1,3]
输出: [1,null,3]

```
 

 **提示：** 
-  `1 <= preorder.length <= 100` 
-  `1 <= preorder[i] <= 10^8` 
-  `preorder` 中的值 **互不相同** 
 

 
**标签**
`栈` `树` `二叉搜索树` `数组` `二叉树` `单调栈` 


## 
```python

```
>
# 1009.十进制整数的反码
[https://leetcode-cn.com/problems/complement-of-base-10-integer](https://leetcode-cn.com/problems/complement-of-base-10-integer) 
## 原题
每个非负整数 `N` 都有其二进制表示。例如， `5` 可以被表示为二进制 `"101"` ， `11` 可以用二进制 `"1011"` 表示，依此类推。注意，除 `N = 0` 外，任何二进制表示中都不含前导零。

二进制的反码表示是将每个 `1` 改为 `0` 且每个 `0` 变为 `1` 。例如，二进制数 `"101"` 的二进制反码为 `"010"` 。

给你一个十进制数 `N` ，请你返回其二进制表示的反码所对应的十进制整数。

 
 **示例 1：** 

```
输入：5
输出：2
解释：5 的二进制表示为 "101"，其二进制反码为 "010"，也就是十进制中的 2 。

```
 **示例 2：** 

```
输入：7
输出：0
解释：7 的二进制表示为 "111"，其二进制反码为 "000"，也就是十进制中的 0 。

```
 **示例 3：** 

```
输入：10
输出：5
解释：10 的二进制表示为 "1010"，其二进制反码为 "0101"，也就是十进制中的 5 。

```
 

 **提示：** 
-  `0 <= N < 10^9` 
- 本题与 476：<a href="https://leetcode-cn.com/problems/number-complement/">https://leetcode-cn.com/problems/number-complement/</a> 相同
 
**标签**
`位运算` 


## 
```python

```
>
# 1010.总持续时间可被 60 整除的歌曲
[https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60](https://leetcode-cn.com/problems/pairs-of-songs-with-total-durations-divisible-by-60) 
## 原题
在歌曲列表中，第 `i` 首歌曲的持续时间为 `time[i]` 秒。

返回其总持续时间（以秒为单位）可被 `60` 整除的歌曲对的数量。形式上，我们希望下标数字 `i` 和 `j` 满足 `i < j` 且有 `(time[i] + time[j]) % 60 == 0` 。

 

 **示例 1：** 

```

输入：time = [30,20,150,100,40]
输出：3
解释：这三对的总持续时间可被 60 整除：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60

```
 **示例 2：** 

```

输入：time = [60,60,60]
输出：3
解释：所有三对的总持续时间都是 120，可以被 60 整除。

```
 

 **提示：** 
-  `1 <= time.length <= 6 * 10^4` 
-  `1 <= time[i] <= 500` 
 
**标签**
`数组` `哈希表` `计数` 


## 
```python

```
>
# 1011.在 D 天内送达包裹的能力
[https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days](https://leetcode-cn.com/problems/capacity-to-ship-packages-within-d-days) 
## 原题
传送带上的包裹必须在 `days` 天内从一个港口运送到另一个港口。

传送带上的第 `i` 个包裹的重量为 `weights[i]` 。每一天，我们都会按给出重量（ `weights` ）的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 `days` 天内将传送带上的所有包裹送达的船的最低运载能力。

 

 **示例 1：** 

```

输入：weights = [1,2,3,4,5,6,7,8,9,10], days = 5
输出：15
解释：
船舶最低载重 15 就能够在 5 天内送达所有包裹，如下所示：
第 1 天：1, 2, 3, 4, 5
第 2 天：6, 7
第 3 天：8
第 4 天：9
第 5 天：10

请注意，货物必须按照给定的顺序装运，因此使用载重能力为 14 的船舶并将包装分成 (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) 是不允许的。 

```
 **示例 2：** 

```

输入：weights = [3,2,2,4,1,4], days = 3
输出：6
解释：
船舶最低载重 6 就能够在 3 天内送达所有包裹，如下所示：
第 1 天：3, 2
第 2 天：2, 4
第 3 天：1, 4

```
 **示例 3：** 

```

输入：weights = [1,2,3,1,1], D = 4
输出：3
解释：
第 1 天：1
第 2 天：2
第 3 天：3
第 4 天：1, 1

```
 

 **提示：** 
-  `1 <= days <= weights.length <= 5 * 10^4` 
-  `1 <= weights[i] <= 500` 
 
**标签**
`贪心` `数组` `二分查找` 


## 
```python

```
>
# 1012.至少有 1 位重复的数字
[https://leetcode-cn.com/problems/numbers-with-repeated-digits](https://leetcode-cn.com/problems/numbers-with-repeated-digits) 
## 原题
给定正整数 `n` ，返回在 `[1, n]` 范围内具有 **至少 1 位** 重复数字的正整数的个数。

 

 **示例 1：** 

```

输入：n = 20
输出：1
解释：具有至少 1 位重复数字的正数（<= 20）只有 11 。

```
 **示例 2：** 

```

输入：n = 100
输出：10
解释：具有至少 1 位重复数字的正数（<= 100）有 11，22，33，44，55，66，77，88，99 和 100 。

```
 **示例 3：** 

```

输入：n = 1000
输出：262

```
 

 **提示：** 
-  `1 <= n <= 10^9` 
 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 1013.将数组分成和相等的三个部分
[https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum](https://leetcode-cn.com/problems/partition-array-into-three-parts-with-equal-sum) 
## 原题
给你一个整数数组 `arr` ，只有可以将其划分为三个和相等的 **非空** 部分时才返回  `true` ，否则返回 `false` 。

形式上，如果可以找出索引  `i + 1 < j`  且满足  `(arr[0] + arr[1] + ... + arr[i] == arr[i + 1] + arr[i + 2] + ... + arr[j - 1] == arr[j] + arr[j + 1] + ... + arr[arr.length - 1])`  就可以将数组三等分。

 

 **示例 1：** 

```

输入：arr = [0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

```
 **示例 2：** 

```

输入：arr = [0,2,1,-6,6,7,9,-1,2,0,1]
输出：false

```
 **示例 3：** 

```

输入：arr = [3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

```
 

 **提示：** 
-  `3 <= arr.length <= 5 * 10^4` 
-  `-10^4 <= arr[i] <= 10^4` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1014.最佳观光组合
[https://leetcode-cn.com/problems/best-sightseeing-pair](https://leetcode-cn.com/problems/best-sightseeing-pair) 
## 原题
给你一个正整数数组 `values` ，其中 `values[i]`  表示第 `i` 个观光景点的评分，并且两个景点  `i` 和  `j`  之间的 **距离** 为  `j - i` 。

一对景点（ `i < j` ）组成的观光组合的得分为 `values[i] + values[j] + i - j` ，也就是景点的评分之和 **减去** 它们两者之间的距离。

返回一对观光景点能取得的最高分。

 

 **示例 1：** 

```

输入：values = [8,1,5,2,6]
输出：11
解释：i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

```
 **示例 2：** 

```

输入：values = [1,2]
输出：2

```
 

 **提示：** 
-  `2 <= values.length <= 5 * 10^4` 
-  `1 <= values[i] <= 1000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1015.可被 K 整除的最小整数
[https://leetcode-cn.com/problems/smallest-integer-divisible-by-k](https://leetcode-cn.com/problems/smallest-integer-divisible-by-k) 
## 原题
给定正整数 `k` ，你需要找出可以被 `k` 整除的、仅包含数字 `**1**` 的最 **小** 正整数 `n` 的长度。

返回 `n` 的长度。如果不存在这样的 `n` ，就返回-1。

 **注意：** `n` 不符合 64 位带符号整数。

 

 **示例 1：** 

```

输入：k = 1
输出：1
解释：最小的答案是 n = 1，其长度为 1。
```
 **示例 2：** 

```

输入：k = 2
输出：-1
解释：不存在可被 2 整除的正整数 n 。
```
 **示例 3：** 

```

输入：k = 3
输出：3
解释：最小的答案是 n = 111，其长度为 3。
```
 

 **提示：** 
-  `1 <= k <= 10^5` 
 
**标签**
`哈希表` `数学` 


## 
```python

```
>
# 1016.子串能表示从 1 到 N 数字的二进制串
[https://leetcode-cn.com/problems/binary-string-with-substrings-representing-1-to-n](https://leetcode-cn.com/problems/binary-string-with-substrings-representing-1-to-n) 
## 原题
给定一个二进制字符串 `s` 和一个正整数 `n` ，如果对于 `[1, n]` 范围内的每个整数， *其二进制表示都是 `s` 的 **子字符串** ，就返回 `true` ，否则返回 `false`* 。

 **子字符串** 是字符串中连续的字符序列。

 

 **示例 1：** 

```

输入：s = "0110", n = 3
输出：true

```
 **示例 2：** 

```

输入：s = "0110", n = 4
输出：false

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s[i]` 不是 `'0'` 就是 `'1'` 
-  `1 <= n <= 10^9` 
 
**标签**
`字符串` 


## 
```python

```
>
# 1017.负二进制转换
[https://leetcode-cn.com/problems/convert-to-base-2](https://leetcode-cn.com/problems/convert-to-base-2) 
## 原题
给出数字 `N` ，返回由若干 `"0"` 和 `"1"` 组成的字符串，该字符串为 `N` 的 **负二进制（ `base -2` ）** 表示。

除非字符串就是 `"0"` ，否则返回的字符串中不能含有前导零。

 

 **示例 1：** 

```
输入：2
输出："110"
解释：(-2) ^ 2 + (-2) ^ 1 = 2

```
 **示例 2：** 

```
输入：3
输出："111"
解释：(-2) ^ 2 + (-2) ^ 1 + (-2) ^ 0 = 3

```
 **示例 3：** 

```
输入：4
输出："100"
解释：(-2) ^ 2 = 4

```
 

 **提示：** 
-  `0 <= N <= 10^9` 
 
**标签**
`数学` 


## 
```python

```
>
# 1018.可被 5 整除的二进制前缀
[https://leetcode-cn.com/problems/binary-prefix-divisible-by-5](https://leetcode-cn.com/problems/binary-prefix-divisible-by-5) 
## 原题
给定由若干 `0` 和 `1` 组成的数组 `A` 。我们定义 `N_i` ：从 `A[0]` 到 `A[i]` 的第 `i` 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。

返回布尔值列表 `answer` ，只有当 `N_i` 可以被 `5` 整除时，答案 `answer[i]` 为 `true` ，否则为 `false` 。

 

 **示例 1：** 

```
输入：[0,1,1]
输出：[true,false,false]
解释：
输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。

```
 **示例 2：** 

```
输入：[1,1,1]
输出：[false,false,false]

```
 **示例 3：** 

```
输入：[0,1,1,1,1,1]
输出：[true,false,false,false,true,false]

```
 **示例 4：** 

```
输入：[1,1,1,0,1]
输出：[false,false,false,false,false]

```
 

 **提示：** 
-  `1 <= A.length <= 30000` 
-  `A[i]` 为 `0` 或 `1` 
 
**标签**
`数组` 


## 
```python

```
>
# 1019.链表中的下一个更大节点
[https://leetcode-cn.com/problems/next-greater-node-in-linked-list](https://leetcode-cn.com/problems/next-greater-node-in-linked-list) 
## 原题
给定一个长度为 `n` 的链表 `head` 

对于列表中的每个节点，查找下一个 **更大节点** 的值。也就是说，对于每个节点，找到它旁边的第一个节点的值，这个节点的值 **严格大于** 它的值。

返回一个整数数组 `answer` ，其中 `answer[i]` 是第 `i` 个节点( **从1开始** )的下一个更大的节点的值。如果第 `i` 个节点没有下一个更大的节点，设置 `answer[i] = 0` 。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext1.jpg" />

```

输入：head = [2,1,5]
输出：[5,5,0]

```
 **示例 2：** 

<img src="https://assets.leetcode.com/uploads/2021/08/05/linkedlistnext2.jpg" />

```

输入：head = [2,7,4,3,5]
输出：[7,0,5,5,0]

```
 

 **提示：** 
- 链表中节点数为 `n` 
-  `1 <= n <= 10^4` 
-  `1 <= Node.val <= 10^9` 
 
**标签**
`栈` `数组` `链表` `单调栈` 


## 
```python

```
>
# 1020.飞地的数量
[https://leetcode-cn.com/problems/number-of-enclaves](https://leetcode-cn.com/problems/number-of-enclaves) 
## 原题
给你一个大小为 `m x n` 的二进制矩阵 `grid` ，其中 `0` 表示一个海洋单元格、 `1` 表示一个陆地单元格。

一次 **移动** 是指从一个陆地单元格走到另一个相邻（ **上、下、左、右** ）的陆地单元格或跨过 `grid` 的边界。

返回网格中 **无法** 在任意次数的移动中离开网格边界的陆地单元格的数量。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/enclaves1.jpg" style="height: 200px; width: 200px;" />
```

输入：grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
输出：3
解释：有三个 1 被 0 包围。一个 1 没有被包围，因为它在边界上。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/enclaves2.jpg" style="height: 200px; width: 200px;" />
```

输入：grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
输出：0
解释：所有 1 都在边界上或可以到达边界。

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 500` 
-  `grid[i][j]` 的值为 `0` 或 `1` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` 


## 
```python

```
>
# 1021.删除最外层的括号
[https://leetcode-cn.com/problems/remove-outermost-parentheses](https://leetcode-cn.com/problems/remove-outermost-parentheses) 
## 原题
有效括号字符串为空 `""` 、 `"(" + A + ")"`  或  `A + B` ，其中  `A` 和  `B`  都是有效的括号字符串， `+`  代表字符串的连接。
- 例如， `""` ， `"()"` ， `"(())()"`  和  `"(()(()))"`  都是有效的括号字符串。
如果有效字符串 `s` 非空，且不存在将其拆分为 `s = A + B`  的方法，我们称其为 **原语（primitive）** ，其中  `A` 和  `B`  都是非空有效括号字符串。

给出一个非空有效字符串 `s` ，考虑将其进行原语化分解，使得： `s = P_1 + P_2 + ... + P_k` ，其中  `P_i`  是有效括号字符串原语。

对 `s` 进行原语化分解，删除分解中每个原语字符串的最外层括号，返回 `s` 。

 

 **示例 1：** 

```

输入：s = "(()())(())"
输出："()()()"
解释：
输入字符串为 "(()())(())"，原语化分解得到 "(()())" + "(())"，
删除每个部分中的最外层括号后得到 "()()" + "()" = "()()()"。
```
 **示例 2：** 

```

输入：s = "(()())(())(()(()))"
输出："()()()()(())"
解释：
输入字符串为 "(()())(())(()(()))"，原语化分解得到 "(()())" + "(())" + "(()(()))"，
删除每个部分中的最外层括号后得到 "()()" + "()" + "()(())" = "()()()()(())"。

```
 **示例 3：** 

```

输入：s = "()()"
输出：""
解释：
输入字符串为 "()()"，原语化分解得到 "()" + "()"，
删除每个部分中的最外层括号后得到 "" + "" = ""。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s[i]` 为 `'('` 或 `')'` 
-  `s` 是一个有效括号字符串
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 1022.从根到叶的二进制数之和
[https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers](https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers) 
## 原题
给出一棵二叉树，其上每个结点的值都是  `0`  或  `1`  。每一条从根到叶的路径都代表一个从最高有效位开始的二进制数。例如，如果路径为  `0 -> 1 -> 1 -> 0 -> 1` ，那么它表示二进制数  `01101` ，也就是  `13`  。

对树上的每一片叶子，我们都要找出从根到该叶子的路径所表示的数字。

返回这些数字之和。题目数据保证答案是一个 **32 位** 整数。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/04/sum-of-root-to-leaf-binary-numbers.png" style="width: 450px; height: 296px;" />
```

输入：root = [1,0,1,0,1,0,1]
输出：22
解释：(100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22

```
 **示例 2：** 

```

输入：root = [0]
输出：0

```
 **示例 3：** 

```

输入：root = [1]
输出：1

```
 **示例 4：** 

```

输入：root = [1,1]
输出：3

```
 

 **提示：** 
- 树中的结点数介于 `1` 和 `1000` 之间。
-  `Node.val` 为 `0` 或 `1` 。
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1023.驼峰式匹配
[https://leetcode-cn.com/problems/camelcase-matching](https://leetcode-cn.com/problems/camelcase-matching) 
## 原题
如果我们可以将 **小写字母** 插入模式串 `pattern` 得到待查询项 `query` ，那么待查询项与给定模式串匹配。（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定待查询列表 `queries` ，和模式串 `pattern` ，返回由布尔值组成的答案列表 `answer` 。只有在待查项 `queries[i]` 与模式串 `pattern` 匹配时， `answer[i]` 才为 `true` ，否则为 `false` 。

 

 **示例 1：** 

```
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".
```
 **示例 2：** 

```
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
输出：[true,false,true,false,false]
解释：
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".

```
 **示例 3：** 

```
输出：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
输入：[false,true,false,false,false]
解释： 
"FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".

```
 

 **提示：** 
-  `1 <= queries.length <= 100` 
-  `1 <= queries[i].length <= 100` 
-  `1 <= pattern.length <= 100` 
- 所有字符串都仅由大写和小写英文字母组成。
 
**标签**
`字典树` `双指针` `字符串` `字符串匹配` 


## 
```python

```
>
# 1024.视频拼接
[https://leetcode-cn.com/problems/video-stitching](https://leetcode-cn.com/problems/video-stitching) 
## 原题
你将会获得一系列视频片段，这些片段来自于一项持续时长为 `time` 秒的体育赛事。这些片段可能有所重叠，也可能长度不一。

使用数组 `clips` 描述所有的视频片段，其中 `clips[i] = [start<sub>i</sub>, end<sub>i</sub>]` 表示：某个视频片段开始于 `start<sub>i</sub>` 并于 `end<sub>i</sub>` 结束。

甚至可以对这些片段自由地再剪辑：
- 例如，片段 `[0, 7]` 可以剪切成 `[0, 1] + [1, 3] + [3, 7]` 三部分。
我们需要将这些片段进行再剪辑，并将剪辑后的内容拼接成覆盖整个运动过程的片段（ `[0, time]` ）。返回所需片段的最小数目，如果无法完成该任务，则返回 `-1` 。

 

 **示例 1：** 

```

输入：clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]], time = 10
输出：3
解释：
选中 [0,2], [8,10], [1,9] 这三个片段。
然后，按下面的方案重制比赛片段：
将 [1,9] 再剪辑为 [1,2] + [2,8] + [8,9] 。
现在手上的片段为 [0,2] + [2,8] + [8,10]，而这些覆盖了整场比赛 [0, 10]。

```
 **示例 2：** 

```

输入：clips = [[0,1],[1,2]], time = 5
输出：-1
解释：
无法只用 [0,1] 和 [1,2] 覆盖 [0,5] 的整个过程。

```
 **示例 3：** 

```

输入：clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]], time = 9
输出：3
解释： 
选取片段 [0,4], [4,7] 和 [6,9] 。

```
 **示例 4：** 

```

输入：clips = [[0,4],[2,8]], time = 5
输出：2
解释：
注意，你可能录制超过比赛结束时间的视频。

```
 

 **提示：** 
-  `1 <= clips.length <= 100` 
-  `0 <= start<sub>i</sub> <= end<sub>i</sub> <= 100` 
-  `1 <= time <= 100` 
 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 1025.除数博弈
[https://leetcode-cn.com/problems/divisor-game](https://leetcode-cn.com/problems/divisor-game) 
## 原题
爱丽丝和鲍勃一起玩游戏，他们轮流行动。爱丽丝先手开局。

最初，黑板上有一个数字 `n` 。在每个玩家的回合，玩家需要执行以下操作：
- 选出任一 `x` ，满足 `0 < x < n` 且 `n % x == 0` 。
- 用 `n - x` 替换黑板上的数字 `n` 。
如果玩家无法执行这些操作，就会输掉游戏。

 *只有在爱丽丝在游戏中取得胜利时才返回 `true` 。假设两个玩家都以最佳状态参与游戏。* 

 
 **示例 1：** 

```

输入：n = 2
输出：true
解释：爱丽丝选择 1，鲍勃无法进行操作。

```
 **示例 2：** 

```

输入：n = 3
输出：false
解释：爱丽丝选择 1，鲍勃也选择 1，然后爱丽丝无法进行操作。

```
 

 **提示：** 
-  `1 <= n <= 1000` 
 
**标签**
`脑筋急转弯` `数学` `动态规划` `博弈` 


## 
```python

```
>
# 1026.节点与其祖先之间的最大差值
[https://leetcode-cn.com/problems/maximum-difference-between-node-and-ancestor](https://leetcode-cn.com/problems/maximum-difference-between-node-and-ancestor) 
## 原题
给定二叉树的根节点  `root` ，找出存在于 **不同** 节点  `A` 和  `B`  之间的最大值 `V` ，其中  `V = |A.val - B.val|` ，且  `A`  是  `B`  的祖先。

（如果 A 的任何子节点之一为 B，或者 A 的任何子节点是 B 的祖先，那么我们认为 A 是 B 的祖先）

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg" style="width: 400px; height: 390px;" />

```

输入：root = [8,3,10,1,6,null,14,null,null,4,7,13]
输出：7
解释： 
我们有大量的节点与其祖先的差值，其中一些如下：
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
在所有可能的差值中，最大值 7 由 |8 - 1| = 7 得出。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg" style="width: 250px; height: 349px;" />
```

输入：root = [1,null,2,null,0,3]
输出：3

```
 

 **提示：** 
- 树中的节点数在  `2`  到  `5000`  之间。
-  `0 <= Node.val <= 10^5` 
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1027.最长等差数列
[https://leetcode-cn.com/problems/longest-arithmetic-subsequence](https://leetcode-cn.com/problems/longest-arithmetic-subsequence) 
## 原题
给你一个整数数组 `nums` ，返回 `nums` 中最长等差子序列的 **长度** 。

回想一下， `nums` 的子序列是一个列表 `nums[i<sub>1</sub>], nums[i<sub>2</sub>], ..., nums[i<sub>k</sub>]` ，且 `0 <= i<sub>1</sub> < i<sub>2</sub> < ... < i<sub>k</sub> <= nums.length - 1` 。并且如果 `seq[i+1] - seq[i]` ( `0 <= i < seq.length - 1` ) 的值都相同，那么序列 `seq` 是等差的。

 

 **示例 1：** 

```

输入：nums = [3,6,9,12]
输出：4
解释： 
整个数组是公差为 3 的等差数列。

```
 **示例 2：** 

```

输入：nums = [9,4,7,2,10]
输出：3
解释：
最长的等差子序列是 [4,7,10]。

```
 **示例 3：** 

```

输入：nums = [20,1,15,3,10,5,8]
输出：4
解释：
最长的等差子序列是 [20,15,10,5]。

```
 

 **提示：** 
-  `2 <= nums.length <= 1000` 
-  `0 <= nums[i] <= 500` 
 
**标签**
`数组` `哈希表` `二分查找` `动态规划` 


## 
```python

```
>
# 1028.从先序遍历还原二叉树
[https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal](https://leetcode-cn.com/problems/recover-a-tree-from-preorder-traversal) 
## 原题
我们从二叉树的根节点 `root` 开始进行深度优先搜索。

在遍历中的每个节点处，我们输出 `D` 条短划线（其中 `D` 是该节点的深度），然后输出该节点的值。（ *如果节点的深度为 `D` ，则其直接子节点的深度为 `D + 1` 。根节点的深度为 `0` ）。* 

如果节点只有一个子节点，那么保证该子节点为左子节点。

给出遍历输出 `S` ，还原树并返回其根节点 `root` 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/04/12/recover-a-tree-from-preorder-traversal.png" style="height: 200px; width: 320px;">** 

```
输入："1-2--3--4-5--6--7"
输出：[1,2,5,3,4,6,7]

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/04/12/screen-shot-2019-04-10-at-114101-pm.png" style="height: 250px; width: 256px;">** 

```
输入："1-2--3---4-5--6---7"
输出：[1,2,5,3,null,6,null,4,null,7]

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/04/12/screen-shot-2019-04-10-at-114955-pm.png" style="height: 250px; width: 276px;">

```
输入："1-401--349---90--88"
输出：[1,401,null,349,88,90]

```
 

 **提示：** 
- 原始树中的节点数介于 `1` 和 `1000` 之间。
- 每个节点的值介于 `1` 和 `10 ^ 9` 之间。
 
**标签**
`树` `深度优先搜索` `字符串` `二叉树` 


## 
```python

```
>
# 1029.两地调度
[https://leetcode-cn.com/problems/two-city-scheduling](https://leetcode-cn.com/problems/two-city-scheduling) 
## 原题
公司计划面试 `2n` 人。给你一个数组 `costs` ，其中 `costs[i] = [aCost<sub>i</sub>, bCost<sub>i</sub>]` 。第 `i` 人飞往 `a` 市的费用为 `aCost<sub>i</sub>` ，飞往 `b` 市的费用为 `bCost<sub>i</sub>` 。

返回将每个人都飞到 `a` 、 `b` 中某座城市的最低费用，要求每个城市都有 `n` 人抵达 **。** 

 

 **示例 1：** 

```

输入：costs = [[10,20],[30,200],[400,50],[30,20]]
输出：110
解释：
第一个人去 a 市，费用为 10。
第二个人去 a 市，费用为 30。
第三个人去 b 市，费用为 50。
第四个人去 b 市，费用为 20。

最低总费用为 10 + 30 + 50 + 20 = 110，每个城市都有一半的人在面试。

```
 **示例 2：** 

```

输入：costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
输出：1859

```
 **示例 3：** 

```

输入：costs = [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
输出：3086

```
 

 **提示：** 
-  `2 * n == costs.length` 
-  `2 <= costs.length <= 100` 
-  `costs.length` 为偶数
-  `1 <= aCost<sub>i</sub>, bCost<sub>i</sub> <= 1000` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1030.距离顺序排列矩阵单元格
[https://leetcode-cn.com/problems/matrix-cells-in-distance-order](https://leetcode-cn.com/problems/matrix-cells-in-distance-order) 
## 原题
给定四个整数 `row` , `cols` , `rCenter` 和 `cCenter` 。有一个 `rows x cols` 的矩阵，你在单元格上的坐标是 `(rCenter, cCenter)` 。

返回矩阵中的所有单元格的坐标，并按与 `(rCenter, cCenter)` 的 **距离** 从最小到最大的顺序排。你可以按 **任何** 满足此条件的顺序返回答案。

单元格 `(r1, c1)` 和 `(r2, c2)` 之间的距离为 `|r1 - r2| + |c1 - c2|` 。

 

 **示例 1：** 

```

输入：rows = 1, cols = 2, rCenter = 0, cCenter = 0
输出：[[0,0],[0,1]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1]

```
 **示例 2：** 

```

输入：rows = 2, cols = 2, rCenter = 0, cCenter = 1
输出：[[0,1],[0,0],[1,1],[1,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2]
[[0,1],[1,1],[0,0],[1,0]] 也会被视作正确答案。

```
 **示例 3：** 

```

输入：rows = 2, cols = 3, rCenter = 1, cCenter = 2
输出：[[1,2],[0,2],[1,1],[0,1],[1,0],[0,0]]
解释：从 (r0, c0) 到其他单元格的距离为：[0,1,1,2,2,3]
其他满足题目要求的答案也会被视为正确，例如 [[1,2],[1,1],[0,2],[1,0],[0,1],[0,0]]。

```
 

 **提示：** 
-  `1 <= rows, cols <= 100` 
-  `0 <= rCenter < rows` 
-  `0 <= cCenter < cols` 
 
**标签**
`几何` `数组` `数学` `矩阵` `排序` 


## 
```python

```
>
# 1031.两个非重叠子数组的最大和
[https://leetcode-cn.com/problems/maximum-sum-of-two-non-overlapping-subarrays](https://leetcode-cn.com/problems/maximum-sum-of-two-non-overlapping-subarrays) 
## 原题
给出非负整数数组 `A` ，返回两个非重叠（连续）子数组中元素的最大和，子数组的长度分别为 `L` 和 `M` 。（这里需要澄清的是，长为 L 的子数组可以出现在长为 M 的子数组之前或之后。）

从形式上看，返回最大的 `V` ，而 `V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1])` 并满足下列条件之一：

 
-  `0 <= i < i + L - 1 < j < j + M - 1 < A.length` , **或** 
-  `0 <= j < j + M - 1 < i < i + L - 1 < A.length` .
 

 **示例 1：** 

```
输入：A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
输出：20
解释：子数组的一种选择中，[9] 长度为 1，[6,5] 长度为 2。

```
 **示例 2：** 

```
输入：A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
输出：29
解释：子数组的一种选择中，[3,8,1] 长度为 3，[8,9] 长度为 2。

```
 **示例 3：** 

```
输入：A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
输出：31
解释：子数组的一种选择中，[5,6,0,9] 长度为 4，[0,3,8] 长度为 3。
```
 

 **提示：** 
-  `L >= 1` 
-  `M >= 1` 
-  `L + M <= A.length <= 1000` 
-  `0 <= A[i] <= 1000` 
 
**标签**
`数组` `动态规划` `滑动窗口` 


## 
```python

```
>
# 1032.字符流
[https://leetcode-cn.com/problems/stream-of-characters](https://leetcode-cn.com/problems/stream-of-characters) 
## 原题
设计一个算法：接收一个字符流，并检查这些字符的后缀是否是字符串数组 `words` 中的一个字符串。

例如， `words = ["abc", "xyz"]` 且字符流中逐个依次加入 4 个字符 `'a'` 、 `'x'` 、 `'y'` 和 `'z'` ，你所设计的算法应当可以检测到 `"axyz"` 的后缀 `"xyz"` 与 `words` 中的字符串 `"xyz"` 匹配。

按下述要求实现 `StreamChecker` 类：
-  `StreamChecker(String[] words)` ：构造函数，用字符串数组 `words` 初始化数据结构。
-  `boolean query(char letter)` ：从字符流中接收一个新字符，如果字符流中的任一非空后缀能匹配 `words` 中的某一字符串，返回 `true` ；否则，返回 `false` 。
 

 **示例：** 

```

输入：
["StreamChecker", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query", "query"]
[[["cd", "f", "kl"]], ["a"], ["b"], ["c"], ["d"], ["e"], ["f"], ["g"], ["h"], ["i"], ["j"], ["k"], ["l"]]
输出：
[null, false, false, false, true, false, true, false, false, false, false, false, true]

解释：
StreamChecker streamChecker = new StreamChecker(["cd", "f", "kl"]);
streamChecker.query("a"); // 返回 False
streamChecker.query("b"); // 返回 False
streamChecker.query("c"); // 返回n False
streamChecker.query("d"); // 返回 True ，因为 'cd' 在 words 中
streamChecker.query("e"); // 返回 False
streamChecker.query("f"); // 返回 True ，因为 'f' 在 words 中
streamChecker.query("g"); // 返回 False
streamChecker.query("h"); // 返回 False
streamChecker.query("i"); // 返回 False
streamChecker.query("j"); // 返回 False
streamChecker.query("k"); // 返回 False
streamChecker.query("l"); // 返回 True ，因为 'kl' 在 words 中

```
 

 **提示：** 
-  `1 <= words.length <= 2000` 
-  `1 <= words[i].length <= 2000` 
-  `words[i]` 由小写英文字母组成
-  `letter` 是一个小写英文字母
- 最多调用查询 `4 * 10^4` 次
 
**标签**
`设计` `字典树` `数组` `字符串` `数据流` 


## 
```python

```
>
# 1033.移动石子直到连续
[https://leetcode-cn.com/problems/moving-stones-until-consecutive](https://leetcode-cn.com/problems/moving-stones-until-consecutive) 
## 原题
三枚石子放置在数轴上，位置分别为 `a` ， `b` ， `c` 。

每一回合，你可以从两端之一拿起一枚石子（位置最大或最小），并将其放入两端之间的任一空闲位置。形式上，假设这三枚石子当前分别位于位置 `x, y, z` 且 `x < y < z` 。那么就可以从位置 `x` 或者是位置 `z` 拿起一枚石子，并将该石子移动到某一整数位置 `k` 处，其中 `x < k < z` 且 `k != y` 。

当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。

要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案： `answer = [minimum_moves, maximum_moves]` 

 

 **示例 1：** 

```

输入：a = 1, b = 2, c = 5
输出：[1, 2]
解释：将石子从 5 移动到 4 再移动到 3，或者我们可以直接将石子移动到 3。

```
 **示例 2：** 

```

输入：a = 4, b = 3, c = 2
输出：[0, 0]
解释：我们无法进行任何移动。

```
 

 **提示：** 
-  `1 <= a <= 100` 
-  `1 <= b <= 100` 
-  `1 <= c <= 100` 
-  `a != b, b != c, c != a` 
 
**标签**
`脑筋急转弯` `数学` 


## 
```python

```
>
# 1034.边界着色
[https://leetcode-cn.com/problems/coloring-a-border](https://leetcode-cn.com/problems/coloring-a-border) 
## 原题
给你一个大小为 `m x n` 的整数矩阵 `grid` ，表示一个网格。另给你三个整数 `row` 、 `col` 和 `color` 。网格中的每个值表示该位置处的网格块的颜色。

两个网格块属于同一 **连通分量** 需满足下述全部条件：
- 两个网格块颜色相同
- 在上、下、左、右任意一个方向上相邻
 **连通分量的边界** **** 是指连通分量中满足下述条件之一的所有网格块：
- 在上、下、左、右任意一个方向上与不属于同一连通分量的网格块相邻
- 在网格的边界上（第一行/列或最后一行/列）
请你使用指定颜色 `color` 为所有包含网格块 `grid[row][col]` 的 **连通分量的边界** 进行着色，并返回最终的网格 `grid` 。

 

 **示例 1：** 

```

输入：grid = [[1,1],[1,2]], row = 0, col = 0, color = 3
输出：[[3,3],[3,2]]
```
 **示例 2：** 

```

输入：grid = [[1,2,2],[2,3,2]], row = 0, col = 1, color = 3
输出：[[1,3,3],[2,3,3]]
```
 **示例 3：** 

```

输入：grid = [[1,1,1],[1,1,1],[1,1,1]], row = 1, col = 1, color = 2
输出：[[2,2,2],[2,1,2],[2,2,2]]
```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 50` 
-  `1 <= grid[i][j], color <= 1000` 
-  `0 <= row < m` 
-  `0 <= col < n` 
 

 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 1035.不相交的线
[https://leetcode-cn.com/problems/uncrossed-lines](https://leetcode-cn.com/problems/uncrossed-lines) 
## 原题
在两条独立的水平线上按给定的顺序写下 `nums1` 和 `nums2` 中的整数。

现在，可以绘制一些连接两个数字 `nums1[i]` 和 `nums2[j]` 的直线，这些直线需要同时满足满足：
-  `nums1[i] == nums2[j]` 
- 且绘制的直线不与任何其他连线（非水平线）相交。
请注意，连线即使在端点也不能相交：每个数字只能属于一条连线。

以这种方法绘制线条，并返回可以绘制的最大连线数。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/26/142.png" style="width: 400px; height: 286px;" />
```

输入：nums1 = <span id="example-input-1-1">[1,4,2]</span>, nums2 = <span id="example-input-1-2">[1,2,4]</span>
输出：<span id="example-output-1">2</span>
解释：可以画出两条不交叉的线，如上图所示。 
但无法画出第三条不相交的直线，因为从 nums1[1]=4 到 nums2[2]=4 的直线将与从 nums1[2]=2 到 nums2[1]=2 的直线相交。

```
 **示例 2：** 

```

输入：nums1 = <span id="example-input-2-1">[2,5,1,2,5]</span>, nums2 = <span id="example-input-2-2">[10,5,2,1,5,2]</span>
输出：<span id="example-output-2">3</span>

```
 **示例 3：** 

```

输入：nums1 = <span id="example-input-3-1">[1,3,7,1,7,5]</span>, nums2 = <span id="example-input-3-2">[1,9,2,5,1]</span>
输出：<span id="example-output-3">2</span>
```
 
 **提示：** 
-  `1 <= nums1.length, nums2.length <= 500` 
-  `1 <= nums1[i], nums2[j] <= 2000` 
 

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1036.逃离大迷宫
[https://leetcode-cn.com/problems/escape-a-large-maze](https://leetcode-cn.com/problems/escape-a-large-maze) 
## 原题
在一个 10^6 x 10^6 的网格中，每个网格上方格的坐标为  `(x, y)` 。

现在从源方格  `source = [s<sub>x</sub>, s<sub>y</sub>]`  开始出发，意图赶往目标方格  `target = [t<sub>x</sub>, t<sub>y</sub>]` 。数组 `blocked` 是封锁的方格列表，其中每个 `blocked[i] = [x<sub>i</sub>, y<sub>i</sub>]` 表示坐标为 `(x<sub>i</sub>, y<sub>i</sub>)` 的方格是禁止通行的。

每次移动，都可以走到网格中在四个方向上相邻的方格，只要该方格 **不** 在给出的封锁列表  `blocked`  上。同时，不允许走出网格。

只有在可以通过一系列的移动从源方格  `source` 到达目标方格  `target` 时才返回  `true` 。否则，返回 `false` 。

 

 **示例 1：** 

```

输入：blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
输出：false
解释：
从源方格无法到达目标方格，因为我们无法在网格中移动。
无法向北或者向东移动是因为方格禁止通行。
无法向南或者向西移动是因为不能走出网格。
```
 **示例 2：** 

```

输入：blocked = [], source = [0,0], target = [999999,999999]
输出：true
解释：
因为没有方格被封锁，所以一定可以到达目标方格。

```
 

 **提示：** 
-  `0 <= blocked.length <= 200` 
-  `blocked[i].length == 2` 
-  `0 <= x<sub>i</sub>, y<sub>i</sub> < 10^6` 
-  `source.length == target.length == 2` 
-  `0 <= s<sub>x</sub>, s<sub>y</sub>, t<sub>x</sub>, t<sub>y</sub> < 10^6` 
-  `source != target` 
- 题目数据保证 `source` 和 `target` 不在封锁列表内
 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `哈希表` 


## 
```python

```
>
# 1037.有效的回旋镖
[https://leetcode-cn.com/problems/valid-boomerang](https://leetcode-cn.com/problems/valid-boomerang) 
## 原题
给定一个数组<meta charset="UTF-8" /> `points` ，其中<meta charset="UTF-8" /> `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` 表示 **X-Y** 平面上的一个点， *如果这些点构成一个* **回旋镖** 则返回 `true` 。

 **回旋镖** 定义为一组三个点，这些点 **各不相同** 且 **不在一条直线上** 。

 

 **示例 1：** 

```

输入：points = [[1,1],[2,3],[3,2]]
输出：true

```
 **示例 2：** 

```

输入：points = [[1,1],[2,2],[3,3]]
输出：false
```
 

 **提示：** 
<meta charset="UTF-8" />
-  `points.length == 3` 
-  `points[i].length == 2` 
-  `0 <= x<sub>i</sub>, y<sub>i</sub> <= 100` 
 
**标签**
`几何` `数学` 


## 
```python

```
>
# 1038.把二叉搜索树转换为累加树
[https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree](https://leetcode-cn.com/problems/binary-search-tree-to-greater-sum-tree) 
## 原题
<span style="font-size:10.5pt"><span style="font-family:Calibri"><span style="font-size:10.5000pt"><span style="font-family:宋体"><font face="宋体">给定一个二叉搜索树</font></span></span></span></span> `root` (BST)<span style="font-size:10.5pt"><span style="font-family:Calibri"><span style="font-size:10.5000pt"><span style="font-family:宋体"><font face="宋体">，请将它的每个</font></span></span></span></span>节点<span style="font-size:10.5pt"><span style="font-family:Calibri"><span style="font-size:10.5000pt"><span style="font-family:宋体"><font face="宋体">的值替换成树中大于或者等于该</font></span></span></span></span>节点<span style="font-size:10.5pt"><span style="font-family:Calibri"><span style="font-size:10.5000pt"><span style="font-family:宋体"><font face="宋体">值的所有</font></span></span></span></span>节点<span style="font-size:10.5pt"><span style="font-family:Calibri"><span style="font-size:10.5000pt"><span style="font-family:宋体"><font face="宋体">值之和。</font></span></span></span></span>

提醒一下， *二叉搜索树* 满足下列约束条件：
- 节点的左子树仅包含键 **小于** 节点键的节点。
- 节点的右子树仅包含键 **大于** 节点键的节点。
- 左右子树也必须是二叉搜索树。
 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/05/03/tree.png" style="height:273px; width:400px" />** 

```

输入：[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
输出：[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

```
 **示例 2：** 

```

输入：root = [0,null,1]
输出：[1,null,1]

```
 

 **提示：** 
- 树中的节点数在 `[1, 100]` 范围内。
-  `0 <= Node.val <= 100` 
- 树中的所有值均 **不重复** 。
 

 **注意：** 该题目与 538: <a href="https://leetcode-cn.com/problems/convert-bst-to-greater-tree/">https://leetcode-cn.com/problems/convert-bst-to-greater-tree/  </a>相同

 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 1039.多边形三角剖分的最低得分
[https://leetcode-cn.com/problems/minimum-score-triangulation-of-polygon](https://leetcode-cn.com/problems/minimum-score-triangulation-of-polygon) 
## 原题
你有一个凸的<meta charset="UTF-8" /> `n` 边形，其每个顶点都有一个整数值。给定一个整数数组<meta charset="UTF-8" /> `values` ，其中<meta charset="UTF-8" /> `values[i]` 是第 `i` 个顶点的值（即 **顺时针顺序** ）。

假设将多边形 **剖分** 为 `n - 2` 个三角形。对于每个三角形，该三角形的值是顶点标记的 **乘积** ，三角剖分的分数是进行三角剖分后所有 `n - 2` 个三角形的值之和。

返回 *多边形进行三角剖分后可以得到的最低分* 。<br />
 
 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/shape1.jpg" />

```

输入：values = [1,2,3]
输出：6
解释：多边形已经三角化，唯一三角形的分数为 6。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/shape2.jpg" style="height: 163px; width: 446px;" />

```

输入：values = [3,7,4,5]
输出：144
解释：有两种三角剖分，可能得分分别为：3*7*5 + 4*5*7 = 245，或 3*4*5 + 3*4*7 = 144。最低分数为 144。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/02/25/shape3.jpg" />

```

输入：values = [1,3,1,4,1,5]
输出：13
解释：最低分数三角剖分的得分情况为 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13。

```
 

 **提示：** 
-  `n == values.length` 
-  `3 <= n <= 50` 
-  `1 <= values[i] <= 100` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1040.移动石子直到连续 II
[https://leetcode-cn.com/problems/moving-stones-until-consecutive-ii](https://leetcode-cn.com/problems/moving-stones-until-consecutive-ii) 
## 原题
在一个长度 **无限** 的数轴上，第 `i` 颗石子的位置为  `stones[i]` 。如果一颗石子的位置最小/最大，那么该石子被称作 **端点石子** 。

每个回合，你可以将一颗端点石子拿起并移动到一个未占用的位置，使得该石子不再是一颗端点石子。

值得注意的是，如果石子像  `stones = [1,2,5]`  这样，你将 **无法** 移动位于位置 5 的端点石子，因为无论将它移动到任何位置（例如 0 或 3），该石子都仍然会是端点石子。

当你无法进行任何移动时，即，这些石子的位置连续时，游戏结束。

要使游戏结束，你可以执行的最小和最大移动次数分别是多少？ 以长度为 2 的数组形式返回答案： `answer = [minimum_moves, maximum_moves]` 。

 

 **示例 1：** 

```

输入：[7,4,9]
输出：[1,2]
解释：
我们可以移动一次，4 -> 8，游戏结束。
或者，我们可以移动两次 9 -> 5，4 -> 6，游戏结束。

```
 **示例 2：** 

```

输入：[6,5,4,3,10]
输出：[2,3]
解释：
我们可以移动 3 -> 8，接着是 10 -> 7，游戏结束。
或者，我们可以移动 3 -> 7, 4 -> 8, 5 -> 9，游戏结束。
注意，我们无法进行 10 -> 2 这样的移动来结束游戏，因为这是不合要求的移动。

```
 **示例 3：** 

```

输入：[100,101,104,102,103]
输出：[0,0]
```
 

 **提示：** 
-  `3 <= stones.length <= 10^4` 
-  `1 <= stones[i] <= 10^9` 
-  `stones[i]`  的值各不相同。
 

 
**标签**
`数组` `数学` `双指针` `排序` 


## 
```python

```
>
# 1041.困于环中的机器人
[https://leetcode-cn.com/problems/robot-bounded-in-circle](https://leetcode-cn.com/problems/robot-bounded-in-circle) 
## 原题
在无限的平面上，机器人最初位于 `(0, 0)` 处，面朝北方。机器人可以接受下列三条指令之一：
-  `"G"` ：直走 1 个单位
-  `"L"` ：左转 90 度
-  `"R"` ：右转 90 度
机器人按顺序执行指令 `instructions` ，并一直重复它们。

只有在平面中存在环使得机器人永远无法离开时，返回 `true` 。否则，返回 `false` 。

 

 **示例 1：** 

```
输入："GGLLGG"
输出：true
解释：
机器人从 (0,0) 移动到 (0,2)，转 180 度，然后回到 (0,0)。
重复这些指令，机器人将保持在以原点为中心，2 为半径的环中进行移动。

```
 **示例 2：** 

```
输入："GG"
输出：false
解释：
机器人无限向北移动。

```
 **示例 3：** 

```
输入："GL"
输出：true
解释：
机器人按 (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ... 进行移动。
```
 

 **提示：** 
-  `1 <= instructions.length <= 100` 
-  `instructions[i]` 在 `{';G';, ';L';, ';R';}` 中
 
**标签**
`数学` `字符串` `模拟` 


## 
```python

```
>
# 1042.不邻接植花
[https://leetcode-cn.com/problems/flower-planting-with-no-adjacent](https://leetcode-cn.com/problems/flower-planting-with-no-adjacent) 
## 原题
有 `n` 个花园，按从 `1` 到 `n` 标记。另有数组 `paths` ，其中 `paths[i] = [x<sub>i</sub>, y<sub>i</sub>]` 描述了花园 `x<sub>i</sub>` 到花园 `y<sub>i</sub>` 的双向路径。在每个花园中，你打算种下四种花之一。

另外，所有花园 **最多** 有 **3** 条路径可以进入或离开.

你需要为每个花园选择一种花，使得通过路径相连的任何两个花园中的花的种类互不相同。

 *以数组形式返回 **任一** 可行的方案作为答案 `answer` ，其中 `answer[i]` 为在第 `(i+1)` 个花园中种植的花的种类。花的种类用  1、2、3、4 表示。保证存在答案。* 

 

 **示例 1：** 

```

输入：n = 3, paths = [[1,2],[2,3],[3,1]]
输出：[1,2,3]
解释：
花园 1 和 2 花的种类不同。
花园 2 和 3 花的种类不同。
花园 3 和 1 花的种类不同。
因此，[1,2,3] 是一个满足题意的答案。其他满足题意的答案有 [1,2,4]、[1,4,2] 和 [3,2,1]

```
 **示例 2：** 

```

输入：n = 4, paths = [[1,2],[3,4]]
输出：[1,2,1,2]

```
 **示例 3：** 

```

输入：n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
输出：[1,2,3,4]

```
 

 **提示：** 
-  `1 <= n <= 10^4` 
-  `0 <= paths.length <= 2 * 10^4` 
-  `paths[i].length == 2` 
-  `1 <= x<sub>i</sub>, y<sub>i</sub> <= n` 
-  `x<sub>i</sub> != y<sub>i</sub>` 
- 每个花园 **最多** 有 **3** 条路径可以进入或离开
 
**标签**
`深度优先搜索` `广度优先搜索` `图` 


## 
```python

```
>
# 1043.分隔数组以得到最大和
[https://leetcode-cn.com/problems/partition-array-for-maximum-sum](https://leetcode-cn.com/problems/partition-array-for-maximum-sum) 
## 原题
给你一个整数数组 `arr` ，请你将该数组分隔为长度最多为 k 的一些（连续）子数组。分隔完成后，每个子数组的中的所有值都会变为该子数组中的最大值。

返回将数组分隔变换后能够得到的元素最大和。

 

 **注意，** 原数组和分隔后的数组对应顺序应当一致，也就是说，你只能选择分隔数组的位置而不能调整数组中的顺序。

 

 **示例 1：** 

```

输入：arr = [1,15,7,9,2,5,10], k = 3
输出：84
解释：
因为 k=3 可以分隔成 [1,15,7] [9] [2,5,10]，结果为 [15,15,15,9,10,10,10]，和为 84，是该数组所有分隔变换后元素总和最大的。
若是分隔成 [1] [15,7,9] [2,5,10]，结果就是 [1, 15, 15, 15, 10, 10, 10] 但这种分隔方式的元素总和（76）小于上一种。 
```
 **示例 2：** 

```

输入：arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
输出：83

```
 **示例 3：** 

```

输入：arr = [1], k = 1
输出：1

```
 

 **提示：** 
-  `1 <= arr.length <= 500` 
-  `0 <= arr[i] <= 10^9` 
-  `1 <= k <= arr.length` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1044.最长重复子串
[https://leetcode-cn.com/problems/longest-duplicate-substring](https://leetcode-cn.com/problems/longest-duplicate-substring) 
## 原题
给你一个字符串 `s` ，考虑其所有 *重复子串* ：即 `s` 的（连续）子串，在 `s` 中出现 2 次或更多次。这些出现之间可能存在重叠。

返回 **任意一个** 可能具有最长长度的重复子串。如果 `s` 不含重复子串，那么答案为 `""` 。

 

 **示例 1：** 

```

输入：s = "banana"
输出："ana"

```
 **示例 2：** 

```

输入：s = "abcd"
输出：""

```
 

 **提示：** 
-  `2 <= s.length <= 3 * 10^4` 
-  `s` 由小写英文字母组成
 
**标签**
`字符串` `二分查找` `后缀数组` `滑动窗口` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 1045.买下所有产品的客户
[https://leetcode-cn.com/problems/customers-who-bought-all-products](https://leetcode-cn.com/problems/customers-who-bought-all-products) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1046.最后一块石头的重量
[https://leetcode-cn.com/problems/last-stone-weight](https://leetcode-cn.com/problems/last-stone-weight) 
## 原题
有一堆石头，每块石头的重量都是正整数。

每一回合，从中选出两块 **最重的** 石头，然后将它们一起粉碎。假设石头的重量分别为  `x` 和  `y` ，且  `x <= y` 。那么粉碎的可能结果如下：
- 如果  `x == y` ，那么两块石头都会被完全粉碎；
- 如果  `x != y` ，那么重量为  `x`  的石头将会完全粉碎，而重量为  `y`  的石头新重量为  `y-x` 。
最后，最多只会剩下一块石头。返回此石头的重量。如果没有石头剩下，就返回 `0` 。

 

 **示例：** 

```

输入：[2,7,4,1,8,1]
输出：1
解释：
先选出 7 和 8，得到 1，所以数组转换为 [2,4,1,1,1]，
再选出 2 和 4，得到 2，所以数组转换为 [2,1,1,1]，
接着是 2 和 1，得到 1，所以数组转换为 [1,1,1]，
最后选出 1 和 1，得到 0，最终数组转换为 [1]，这就是最后剩下那块石头的重量。
```
 

 **提示：** 
-  `1 <= stones.length <= 30` 
-  `1 <= stones[i] <= 1000` 
 
**标签**
`数组` `堆（优先队列）` 


## 
```python

```
>
# 1047.删除字符串中的所有相邻重复项
[https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string](https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string) 
## 原题
给出由小写字母组成的字符串 `S` ， **重复项删除操作** 会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一。

 

 **示例：** 

```
输入："abbaca"
输出："ca"
解释：
例如，在 "abbaca" 中，我们可以删除 "bb" 由于两字母相邻且相同，这是此时唯一可以执行删除操作的重复项。之后我们得到字符串 "aaca"，其中又只有 "aa" 可以执行重复项删除操作，所以最后的字符串为 "ca"。

```
 

 **提示：** 
-  `1 <= S.length <= 20000` 
-  `S` 仅由小写英文字母组成。
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 1048.最长字符串链
[https://leetcode-cn.com/problems/longest-string-chain](https://leetcode-cn.com/problems/longest-string-chain) 
## 原题
给出一个单词数组 `words` ，其中每个单词都由小写英文字母组成。

如果我们可以 **不改变其他字符的顺序** ，在 `word<sub>A</sub>` 的任何地方添加 **恰好一个** 字母使其变成 `word<sub>B</sub>` ，那么我们认为 `word<sub>A</sub>` 是 `word<sub>B</sub>` 的 **前身** 。
- 例如， `"abc"` 是 `"abac"` 的 **前身** ，而 `"cba"` 不是 `"bcad"` 的 **前身** 
 **词链** 是单词 `[word_1, word_2, ..., word_k]` 组成的序列， `k >= 1` ，其中 `word<sub>1</sub>` 是 `word<sub>2</sub>` 的前身， `word<sub>2</sub>` 是 `word<sub>3</sub>` 的前身，依此类推。一个单词通常是 `k == 1` 的 **单词链** 。

从给定单词列表 `words` 中选择单词组成词链，返回 词链的 **最长可能长度** 。<br />
 

 **示例 1：** 

```

输入：words = ["a","b","ba","bca","bda","bdca"]
输出：4
解释：最长单词链之一为 ["a","ba","bda","bdca"]

```
 **示例 2:** 

```

输入：words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]
输出：5
解释：所有的单词都可以放入单词链 ["xb", "xbc", "cxbc", "pcxbc", "pcxbcf"].

```
 **示例 3:** 

```

输入：words = ["abcd","dbqca"]
输出：1
解释：字链["abcd"]是最长的字链之一。
["abcd"，"dbqca"]不是一个有效的单词链，因为字母的顺序被改变了。

```
 

 **提示：** 
-  `1 <= words.length <= 1000` 
-  `1 <= words[i].length <= 16` 
-  `words[i]` 仅由小写英文字母组成。
 
**标签**
`数组` `哈希表` `双指针` `字符串` `动态规划` 


## 
```python

```
>
# 1049.最后一块石头的重量 II
[https://leetcode-cn.com/problems/last-stone-weight-ii](https://leetcode-cn.com/problems/last-stone-weight-ii) 
## 原题
有一堆石头，用整数数组  `stones` 表示。其中  `stones[i]` 表示第 `i` 块石头的重量。

每一回合，从中选出 **任意两块石头** ，然后将它们一起粉碎。假设石头的重量分别为  `x` 和  `y` ，且  `x <= y` 。那么粉碎的可能结果如下：
- 如果  `x == y` ，那么两块石头都会被完全粉碎；
- 如果  `x != y` ，那么重量为  `x`  的石头将会完全粉碎，而重量为  `y`  的石头新重量为  `y-x` 。
最后， **最多只会剩下一块** 石头。返回此石头 **最小的可能重量** 。如果没有石头剩下，就返回 `0` 。

 

 **示例 1：** 

```

输入：stones = [2,7,4,1,8,1]
输出：1
解释：
组合 2 和 4，得到 2，所以数组转化为 [2,7,1,8,1]，
组合 7 和 8，得到 1，所以数组转化为 [2,1,1,1]，
组合 2 和 1，得到 1，所以数组转化为 [1,1,1]，
组合 1 和 1，得到 0，所以数组转化为 [1]，这就是最优值。

```
 **示例 2：** 

```

输入：stones = [31,26,33,21,40]
输出：5

```
 **示例 3：** 

```

输入：stones = [1,2]
输出：1

```
 

 **提示：** 
-  `1 <= stones.length <= 30` 
-  `1 <= stones[i] <= 100` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1050.合作过至少三次的演员和导演
[https://leetcode-cn.com/problems/actors-and-directors-who-cooperated-at-least-three-times](https://leetcode-cn.com/problems/actors-and-directors-who-cooperated-at-least-three-times) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1051.高度检查器
[https://leetcode-cn.com/problems/height-checker](https://leetcode-cn.com/problems/height-checker) 
## 原题
学校打算为全体学生拍一张年度纪念照。根据要求，学生需要按照 **非递减** 的高度顺序排成一行。

排序后的高度情况用整数数组 `expected` 表示，其中 `expected[i]` 是预计排在这一行中第 `i` 位的学生的高度（ **下标从 0 开始** ）。

给你一个整数数组 `heights` ，表示 **当前学生站位** 的高度情况。 `heights[i]` 是这一行中第 `i` 位学生的高度（ **下标从 0 开始** ）。

返回满足 `heights[i] != expected[i]` 的 **下标数量** 。

 

 **示例：** 

```

输入：heights = [1,1,4,2,1,3]
输出：3 
解释：
高度：[1,1,4,2,1,3]
预期：[1,1,1,2,3,4]
下标 2 、4 、5 处的学生高度不匹配。
```
 **示例 2：** 

```

输入：heights = [5,1,2,3,4]
输出：5
解释：
高度：[5,1,2,3,4]
预期：[1,2,3,4,5]
所有下标的对应学生高度都不匹配。
```
 **示例 3：** 

```

输入：heights = [1,2,3,4,5]
输出：0
解释：
高度：[1,2,3,4,5]
预期：[1,2,3,4,5]
所有下标的对应学生高度都匹配。
```
 

 **提示：** 
-  `1 <= heights.length <= 100` 
-  `1 <= heights[i] <= 100` 
 
**标签**
`数组` `计数排序` `排序` 


## 
```python

```
>
# 1052.爱生气的书店老板
[https://leetcode-cn.com/problems/grumpy-bookstore-owner](https://leetcode-cn.com/problems/grumpy-bookstore-owner) 
## 原题
有一个书店老板，他的书店开了 `n` 分钟。每分钟都有一些顾客进入这家商店。给定一个长度为 `n` 的整数数组 `customers` ，其中 `customers[i]` 是在第 `i` 分钟开始时进入商店的顾客的编号，所有这些顾客在第 `i` 分钟结束后离开。

在某些时候，书店老板会生气。 如果书店老板在第 `i` 分钟生气，那么 `grumpy[i] = 1` ，否则 `grumpy[i] = 0` 。

当书店老板生气时，那一分钟的顾客就会不满意，若老板不生气则顾客是满意的。

书店老板知道一个秘密技巧，能抑制自己的情绪，可以让自己连续 `minutes` 分钟不生气，但却只能使用一次。

请你返回 *这一天营业下来，最多有多少客户能够感到满意* 。<br />
 

 **示例 1：** 

```

输入：customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3
输出：16
解释：书店老板在最后 3 分钟保持冷静。
感到满意的最大客户数量 = 1 + 1 + 1 + 1 + 7 + 5 = 16.

```
 **示例 2：** 

```

输入：customers = [1], grumpy = [0], minutes = 1
输出：1
```
 

 **提示：** 
-  `n == customers.length == grumpy.length` 
-  `1 <= minutes <= n <= 2 * 10^4` 
-  `0 <= customers[i] <= 1000` 
-  `grumpy[i] == 0 or 1` 
 
**标签**
`数组` `滑动窗口` 


## 
```python

```
>
# 1053.交换一次的先前排列
[https://leetcode-cn.com/problems/previous-permutation-with-one-swap](https://leetcode-cn.com/problems/previous-permutation-with-one-swap) 
## 原题
给你一个正整数的数组 `A` （其中的元素不一定完全不同），请你返回可在  **一次交换** （交换两数字 `A[i]` 和 `A[j]` 的位置）后得到的、按字典序排列小于 `A` 的最大可能排列。

如果无法这么操作，就请返回原数组。

 

 **示例 1：** 

```

输入：arr = [3,2,1]
输出：[3,1,2]
解释：交换 2 和 1

```
 **示例 2：** 

```

输入：arr = [1,1,5]
输出：[1,1,5]
解释：已经是最小排列

```
 **示例 3：** 

```

输入：arr = [1,9,4,6,7]
输出：[1,7,4,6,9]
解释：交换 9 和 7

```
 **示例 4：** 

```

输入：arr = [3,1,1,3]
输出：[1,3,1,3]
解释：交换 1 和 3

```
 

 **提示：** 
-  `1 <= arr.length <= 10^4` 
-  `1 <= arr[i] <= 10^4` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1054.距离相等的条形码
[https://leetcode-cn.com/problems/distant-barcodes](https://leetcode-cn.com/problems/distant-barcodes) 
## 原题
在一个仓库里，有一排条形码，其中第 `i` 个条形码为 `barcodes[i]` 。

请你重新排列这些条形码，使其中任意两个相邻的条形码不能相等。 你可以返回任何满足该要求的答案，此题保证存在答案。

 

 **示例 1：** 

```

输入：barcodes = [1,1,1,2,2,2]
输出：[2,1,2,1,2,1]

```
 **示例 2：** 

```

输入：barcodes = [1,1,1,1,2,2,3,3]
输出：[1,3,1,3,2,1,2,1]
```
 

 **提示：** 
-  `1 <= barcodes.length <= 10000` 
-  `1 <= barcodes[i] <= 10000` 
 
**标签**
`贪心` `数组` `哈希表` `计数` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1055.形成字符串的最短路径
[https://leetcode-cn.com/problems/shortest-way-to-form-string](https://leetcode-cn.com/problems/shortest-way-to-form-string) 
## 原题

 
**标签**
`贪心` `字符串` `动态规划` 


## 
```python

```
>
# 1056.易混淆数
[https://leetcode-cn.com/problems/confusing-number](https://leetcode-cn.com/problems/confusing-number) 
## 原题

 
**标签**
`数学` 


## 
```python

```
>
# 1057.校园自行车分配
[https://leetcode-cn.com/problems/campus-bikes](https://leetcode-cn.com/problems/campus-bikes) 
## 原题

 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1058.最小化舍入误差以满足目标
[https://leetcode-cn.com/problems/minimize-rounding-error-to-meet-target](https://leetcode-cn.com/problems/minimize-rounding-error-to-meet-target) 
## 原题

 
**标签**
`贪心` `数组` `数学` `字符串` 


## 
```python

```
>
# 1059.从始点到终点的所有路径
[https://leetcode-cn.com/problems/all-paths-from-source-lead-to-destination](https://leetcode-cn.com/problems/all-paths-from-source-lead-to-destination) 
## 原题

 
**标签**
`深度优先搜索` `图` 


## 
```python

```
>
# 1060.有序数组中的缺失元素
[https://leetcode-cn.com/problems/missing-element-in-sorted-array](https://leetcode-cn.com/problems/missing-element-in-sorted-array) 
## 原题

 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 1061.按字典序排列最小的等效字符串
[https://leetcode-cn.com/problems/lexicographically-smallest-equivalent-string](https://leetcode-cn.com/problems/lexicographically-smallest-equivalent-string) 
## 原题

 
**标签**
`并查集` `字符串` 


## 
```python

```
>
# 1062.最长重复子串
[https://leetcode-cn.com/problems/longest-repeating-substring](https://leetcode-cn.com/problems/longest-repeating-substring) 
## 原题

 
**标签**
`字符串` `二分查找` `动态规划` `后缀数组` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 1063.有效子数组的数目
[https://leetcode-cn.com/problems/number-of-valid-subarrays](https://leetcode-cn.com/problems/number-of-valid-subarrays) 
## 原题

 
**标签**
`栈` `数组` `单调栈` 


## 
```python

```
>
# 1064.不动点
[https://leetcode-cn.com/problems/fixed-point](https://leetcode-cn.com/problems/fixed-point) 
## 原题

 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 1065.字符串的索引对
[https://leetcode-cn.com/problems/index-pairs-of-a-string](https://leetcode-cn.com/problems/index-pairs-of-a-string) 
## 原题

 
**标签**
`字典树` `数组` `字符串` `排序` 


## 
```python

```
>
# 1066.校园自行车分配 II
[https://leetcode-cn.com/problems/campus-bikes-ii](https://leetcode-cn.com/problems/campus-bikes-ii) 
## 原题

 
**标签**
`位运算` `数组` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 1067.范围内的数字计数
[https://leetcode-cn.com/problems/digit-count-in-range](https://leetcode-cn.com/problems/digit-count-in-range) 
## 原题

 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 1068.产品销售分析 I
[https://leetcode-cn.com/problems/product-sales-analysis-i](https://leetcode-cn.com/problems/product-sales-analysis-i) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1069.产品销售分析 II
[https://leetcode-cn.com/problems/product-sales-analysis-ii](https://leetcode-cn.com/problems/product-sales-analysis-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1070.产品销售分析 III
[https://leetcode-cn.com/problems/product-sales-analysis-iii](https://leetcode-cn.com/problems/product-sales-analysis-iii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1071.字符串的最大公因子
[https://leetcode-cn.com/problems/greatest-common-divisor-of-strings](https://leetcode-cn.com/problems/greatest-common-divisor-of-strings) 
## 原题
对于字符串  `S` 和  `T` ，只有在 `S = T + ... + T` （ `T` 自身连接 1 次或多次）时，我们才认定 “ `T` 能除尽 `S` ”。

返回最长字符串  `X` ，要求满足  `X` 能除尽 `str1` 且  `X` 能除尽 `str2` 。

 

 **示例 1：** 

```

输入：str1 = "ABCABC", str2 = "ABC"
输出："ABC"

```
 **示例 2：** 

```

输入：str1 = "ABABAB", str2 = "ABAB"
输出："AB"

```
 **示例 3：** 

```

输入：str1 = "LEET", str2 = "CODE"
输出：""

```
 

 **提示：** 
-  `1 <= str1.length <= 1000` 
-  `1 <= str2.length <= 1000` 
-  `str1[i]` 和  `str2[i]` 为大写英文字母
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 1072.按列翻转得到最大值等行数
[https://leetcode-cn.com/problems/flip-columns-for-maximum-number-of-equal-rows](https://leetcode-cn.com/problems/flip-columns-for-maximum-number-of-equal-rows) 
## 原题
给定 `m x n` 矩阵 `matrix` 。

你可以从中选出任意数量的列并翻转其上的 **每个** 单元格。（即翻转后，单元格的值从 `0` 变成 `1` ，或者从 `1` 变为 `0` 。）

返回 *经过一些翻转后，行与行之间所有值都相等的最大行数* 。

 
 **示例 1：** 

```

输入：matrix = [[0,1],[1,1]]
输出：1
解释：不进行翻转，有 1 行所有值都相等。

```
 **示例 2：** 

```

输入：matrix = [[0,1],[1,0]]
输出：2
解释：翻转第一列的值之后，这两行都由相等的值组成。

```
 **示例 3：** 

```

输入：matrix = [[0,0,0],[0,0,1],[1,1,0]]
输出：2
解释：翻转前两列的值之后，后两行由相等的值组成。
```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m, n <= 300` 
-  `matrix[i][j] == 0` 或 `1` 
 
**标签**
`数组` `哈希表` `矩阵` 


## 
```python

```
>
# 1073.负二进制数相加
[https://leetcode-cn.com/problems/adding-two-negabinary-numbers](https://leetcode-cn.com/problems/adding-two-negabinary-numbers) 
## 原题
给出基数为 **-2** 的两个数 `arr1` 和 `arr2` ，返回两数相加的结果。

数字以 *数组形式* **** 给出：数组由若干 0 和 1 组成，按最高有效位到最低有效位的顺序排列。例如， `arr = [1,1,0,1]` 表示数字 `(-2)^3 + (-2)^2 + (-2)^0 = -3` 。 *数组形式* 中的数字 `arr` 也同样不含前导零：即 `arr == [0]` 或 `arr[0] == 1` 。

返回相同表示形式的 `arr1` 和 `arr2` 相加的结果。两数的表示形式为：不含前导零、由若干 0 和 1 组成的数组。

 

 **示例 1：** 

```

输入：arr1 = [1,1,1,1,1], arr2 = [1,0,1]
输出：[1,0,0,0,0]
解释：arr1 表示 11，arr2 表示 5，输出表示 16 。

```
<meta charset="UTF-8" />

 **示例 2：** 

```

输入：arr1 = [0], arr2 = [0]
输出：[0]

```
 **示例 3：** 

```

输入：arr1 = [0], arr2 = [1]
输出：[1]

```
 

 **提示：** 
<meta charset="UTF-8" />
-  `1 <= arr1.length, arr2.length <= 1000` 
-  `arr1[i]` 和 `arr2[i]` 都是 `0` 或 `1` 
-  `arr1` 和 `arr2` 都没有前导0
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 1074.元素和为目标值的子矩阵数量
[https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target](https://leetcode-cn.com/problems/number-of-submatrices-that-sum-to-target) 
## 原题
给出矩阵  `matrix`  和目标值  `target` ，返回元素总和等于目标值的非空子矩阵的数量。

子矩阵  `x1, y1, x2, y2`  是满足 `x1 <= x <= x2`  且  `y1 <= y <= y2`  的所有单元  `matrix[x][y]`  的集合。

如果  `(x1, y1, x2, y2)` 和  `(x1', y1', x2', y2')`  两个子矩阵中部分坐标不同（如： `x1 != x1'` ），那么这两个子矩阵也不同。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/02/mate1.jpg" style="width: 242px; height: 242px;" />

```

输入：matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
输出：4
解释：四个只含 0 的 1x1 子矩阵。

```
 **示例 2：** 

```

输入：matrix = [[1,-1],[-1,1]], target = 0
输出：5
解释：两个 1x2 子矩阵，加上两个 2x1 子矩阵，再加上一个 2x2 子矩阵。

```
 **示例 3：** 

```

输入：matrix = [[904]], target = 0
输出：0

```
 

 ** **提示：** ** 
-  `1 <= matrix.length <= 100` 
-  `1 <= matrix[0].length <= 100` 
-  `-1000 <= matrix[i] <= 1000` 
-  `-10^8 <= target <= 10^8` 
 
**标签**
`数组` `哈希表` `矩阵` `前缀和` 


## 
```python

```
>
# 1075.项目员工 I
[https://leetcode-cn.com/problems/project-employees-i](https://leetcode-cn.com/problems/project-employees-i) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1076.项目员工II
[https://leetcode-cn.com/problems/project-employees-ii](https://leetcode-cn.com/problems/project-employees-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1077.项目员工 III
[https://leetcode-cn.com/problems/project-employees-iii](https://leetcode-cn.com/problems/project-employees-iii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1078.Bigram 分词
[https://leetcode-cn.com/problems/occurrences-after-bigram](https://leetcode-cn.com/problems/occurrences-after-bigram) 
## 原题
给出第一个词 `first` 和第二个词 `second` ，考虑在某些文本 `text` 中可能以 `"first second third"` 形式出现的情况，其中 `second` 紧随 `first` 出现， `third` 紧随 `second` 出现。

对于每种这样的情况，将第三个词 " `third` " 添加到答案中，并返回答案。

 

 **示例 1：** 

```

输入：text = "alice is a good girl she is a good student", first = "a", second = "good"
输出：["girl","student"]

```
 **示例 2：** 

```

输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]

```
 

 **提示：** 
-  `1 <= text.length <= 1000` 
-  `text` 由小写英文字母和空格组成
-  `text` 中的所有单词之间都由 **单个空格字符** 分隔
-  `1 <= first.length, second.length <= 10` 
-  `first` 和 `second` 由小写英文字母组成
 
**标签**
`字符串` 


## 
```python

```
>
# 1079.活字印刷
[https://leetcode-cn.com/problems/letter-tile-possibilities](https://leetcode-cn.com/problems/letter-tile-possibilities) 
## 原题
你有一套活字字模 `tiles` ，其中每个字模上都刻有一个字母 `tiles[i]` 。返回你可以印出的非空字母序列的数目。

 **注意：** 本题中，每个活字字模只能使用一次。

 

 **示例 1：** 

```

输入："AAB"
输出：8
解释：可能的序列为 "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA"。

```
 **示例 2：** 

```

输入："AAABBC"
输出：188

```
 **示例 3：** 

```

输入："V"
输出：1
```
 

 **提示：** 
-  `1 <= tiles.length <= 7` 
-  `tiles` 由大写英文字母组成
 
**标签**
`字符串` `回溯` 


## 
```python

```
>
# 1080.根到叶路径上的不足节点
[https://leetcode-cn.com/problems/insufficient-nodes-in-root-to-leaf-paths](https://leetcode-cn.com/problems/insufficient-nodes-in-root-to-leaf-paths) 
## 原题
给定一棵二叉树的根 `root` ，请你考虑它所有 **从根到叶的路径** ：从根到任何叶的路径。（所谓一个叶子节点，就是一个没有子节点的节点）

假如通过节点 `node` 的每种可能的 “根-叶” 路径上值的总和全都小于给定的 `limit` ，则该节点被称之为「不足节点」，需要被删除。

请你删除所有不足节点，并返回生成的二叉树的根。

 

 **示例 1：** 

```
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/08/insufficient-1.png" style="height: 200px; width: 482px;">
输入：root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/08/insufficient-2.png" style="height: 200px; width: 258px;">
输出：[1,2,3,4,null,null,7,8,9,null,14]

```
 **示例 2：** 

```
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/08/insufficient-3.png" style="height: 200px; width: 292px;">
输入：root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/08/insufficient-4.png" style="height: 200px; width: 264px;">
输出：[5,4,8,11,null,17,4,7,null,null,null,5]
```
 **示例 3：** 

```
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/08/insufficient-5.png" style="height: 100px; width: 140px;">
输入：root = [5,-6,-6], limit = 0
输出：[]
```
 

 **提示：** 
- 给定的树有 `1` 到 `5000` 个节点
-  `-10^5 <= node.val <= 10^5` 
-  `-10^9 <= limit <= 10^9` 
 

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1081.不同字符的最小子序列
[https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters](https://leetcode-cn.com/problems/smallest-subsequence-of-distinct-characters) 
## 原题
返回 `s` 字典序最小的子序列，该子序列包含 `s` 的所有不同字符，且只包含一次。

 **注意：** 该题与 316 <a href="https://leetcode.com/problems/remove-duplicate-letters/">https://leetcode.com/problems/remove-duplicate-letters/</a> 相同

 

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
-  `1 <= s.length <= 1000` 
-  `s` 由小写英文字母组成
 
**标签**
`栈` `贪心` `字符串` `单调栈` 


## 
```python

```
>
# 1082.销售分析 I 
[https://leetcode-cn.com/problems/sales-analysis-i](https://leetcode-cn.com/problems/sales-analysis-i) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1083.销售分析 II
[https://leetcode-cn.com/problems/sales-analysis-ii](https://leetcode-cn.com/problems/sales-analysis-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1084.销售分析III
[https://leetcode-cn.com/problems/sales-analysis-iii](https://leetcode-cn.com/problems/sales-analysis-iii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1085.最小元素各数位之和
[https://leetcode-cn.com/problems/sum-of-digits-in-the-minimum-number](https://leetcode-cn.com/problems/sum-of-digits-in-the-minimum-number) 
## 原题

 
**标签**
`数组` `数学` 


## 
```python

```
>
# 1086.前五科的均分
[https://leetcode-cn.com/problems/high-five](https://leetcode-cn.com/problems/high-five) 
## 原题

 
**标签**
`数组` `哈希表` `排序` 


## 
```python

```
>
# 1087.花括号展开
[https://leetcode-cn.com/problems/brace-expansion](https://leetcode-cn.com/problems/brace-expansion) 
## 原题

 
**标签**
`广度优先搜索` `字符串` `回溯` 


## 
```python

```
>
# 1088.易混淆数 II
[https://leetcode-cn.com/problems/confusing-number-ii](https://leetcode-cn.com/problems/confusing-number-ii) 
## 原题

 
**标签**
`数学` `回溯` 


## 
```python

```
>
# 1089.复写零
[https://leetcode-cn.com/problems/duplicate-zeros](https://leetcode-cn.com/problems/duplicate-zeros) 
## 原题
给你一个长度固定的整数数组 `arr` ，请你将该数组中出现的每个零都复写一遍，并将其余的元素向右平移。

注意：请不要在超过该数组长度的位置写入元素。

要求：请对输入的数组 **就地** 进行上述修改，不要从函数返回任何东西。

 

 **示例 1：** 

```
输入：[1,0,2,3,0,4,5,0]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,0,0,2,3,0,0,4]

```
 **示例 2：** 

```
输入：[1,2,3]
输出：null
解释：调用函数后，输入的数组将被修改为：[1,2,3]

```
 

 **提示：** 
-  `1 <= arr.length <= 10000` 
-  `0 <= arr[i] <= 9` 
 
**标签**
`数组` `双指针` 


## 
```python

```
>
# 1090.受标签影响的最大值
[https://leetcode-cn.com/problems/largest-values-from-labels](https://leetcode-cn.com/problems/largest-values-from-labels) 
## 原题
我们有一个 `n` 项的集合。给出两个整数数组 `values` 和 `labels` ，第 `i` 个元素的值和标签分别是 `values[i]` 和 `labels[i]` 。还会给出两个整数 `numWanted` 和 `useLimit` 。

从 `n` 个元素中选择一个子集 `s` :
- 子集 `s` 的大小 **小于或等于** `numWanted` 。
-  `s` 中 **最多** 有相同标签的 `useLimit` 项。
一个子集的 **分数** 是该子集的值之和。

返回子集 `s` 的最大 **分数** 。

 

 **示例 1：** 

```

输入：values = [5,4,3,2,1], labels = [1,1,2,2,3], numWanted = 3, useLimit = 1
输出：9
解释：选出的子集是第一项，第三项和第五项。

```
 **示例 2：** 

```

输入：values = [5,4,3,2,1], labels = [1,3,3,3,2], numWanted = 3, useLimit = 2
输出：12
解释：选出的子集是第一项，第二项和第三项。

```
 **示例 3：** 

```

输入：values = [9,8,8,7,6], labels = [0,0,0,1,1], numWanted = 3, useLimit = 1
输出：16
解释：选出的子集是第一项和第四项。

```
 

 **提示：** 
-  `n == values.length == labels.length` 
-  `1 <= n <= 2 * 10^4` 
-  `0 <= values[i], labels[i] <= 2 * 10^4` 
-  `1 <= numWanted, useLimit <= n` 
 
**标签**
`贪心` `数组` `哈希表` `计数` `排序` 


## 
```python

```
>
# 1091.二进制矩阵中的最短路径
[https://leetcode-cn.com/problems/shortest-path-in-binary-matrix](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix) 
## 原题
给你一个 `n x n` 的二进制矩阵 `grid` 中，返回矩阵中最短 **畅通路径** 的长度。如果不存在这样的路径，返回 `-1` 。

二进制矩阵中的 畅通路径 是一条从 **左上角** 单元格（即， `(0, 0)` ）到 右下角 单元格（即， `(n - 1, n - 1)` ）的路径，该路径同时满足下述要求：
- 路径途经的所有单元格都的值都是 `0` 。
- 路径中所有相邻的单元格应当在 **8 个方向之一** 上连通（即，相邻两单元之间彼此不同且共享一条边或者一个角）。
 **畅通路径的长度** 是该路径途经的单元格总数。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/example1_1.png" style="width: 500px; height: 234px;" />
```

输入：grid = [[0,1],[1,0]]
输出：2

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/18/example2_1.png" style="height: 216px; width: 500px;" />
```

输入：grid = [[0,0,0],[1,1,0],[1,1,0]]
输出：4

```
 **示例 3：** 

```

输入：grid = [[1,0,0],[1,1,0],[1,1,0]]
输出：-1

```
 

 **提示：** 
-  `n == grid.length` 
-  `n == grid[i].length` 
-  `1 <= n <= 100` 
-  `grid[i][j]` 为 `0` 或 `1` 
 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 1092.最短公共超序列
[https://leetcode-cn.com/problems/shortest-common-supersequence](https://leetcode-cn.com/problems/shortest-common-supersequence) 
## 原题
给出两个字符串 `str1` 和 `str2` ，返回同时以 `str1` 和 `str2` 作为子序列的最短字符串。如果答案不止一个，则可以返回满足条件的任意一个答案。

（如果从字符串 T 中删除一些字符（也可能不删除，并且选出的这些字符可以位于 T 中的 **任意位置** ），可以得到字符串 S，那么 S 就是 T 的子序列）

 

 **示例：** 

```
输入：str1 = "abac", str2 = "cab"
输出："cabac"
解释：
str1 = "abac" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 的第一个 "c"得到 "abac"。 
str2 = "cab" 是 "cabac" 的一个子串，因为我们可以删去 "cabac" 末尾的 "ac" 得到 "cab"。
最终我们给出的答案是满足上述属性的最短字符串。

```
 

 **提示：** 
-  `1 <= str1.length, str2.length <= 1000` 
-  `str1` 和 `str2` 都由小写英文字母组成。
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1093.大样本统计
[https://leetcode-cn.com/problems/statistics-from-a-large-sample](https://leetcode-cn.com/problems/statistics-from-a-large-sample) 
## 原题
我们对 `0` 到 `255` 之间的整数进行采样，并将结果存储在数组 `count` 中： `count[k]` 就是整数 `k` 在样本中出现的次数。

计算以下统计数据:
-  `minimum` ：样本中的最小元素。
-  `maximum` ：样品中的最大元素。
-  `mean` ：样本的平均值，计算为所有元素的总和除以元素总数。
-  `median` ：
	
- 如果样本的元素个数是奇数，那么一旦样本排序后，中位数 `median` 就是中间的元素。
- 如果样本中有偶数个元素，那么中位数 `median` 就是样本排序后中间两个元素的平均值。
	
	
-  `mode` ：样本中出现次数最多的数字。保众数是 **唯一** 的。
以浮点数数组的形式返回样本的统计信息 `[minimum, maximum, mean, median, mode]` 。与真实答案误差在 `10^-5` 内的答案都可以通过。

 

 **示例 1：** 

```

输入：count = [0,1,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
输出：[1.00000,3.00000,2.37500,2.50000,3.00000]
解释：用count表示的样本为[1,2,2,2,3,3,3,3,3]。
最小值和最大值分别为1和3。
均值是(1+2+2+2+3+3+3+3) / 8 = 19 / 8 = 2.375。
因为样本的大小是偶数，所以中位数是中间两个元素2和3的平均值，也就是2.5。
众数为3，因为它在样本中出现的次数最多。
```
 **示例 2：** 

```

输入：count = [0,4,3,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
输出：[1.00000,4.00000,2.18182,2.00000,1.00000]
解释：用count表示的样本为[1,1,1,1,2,2,3,3,3,4,4]。
最小值为1，最大值为4。
平均数是(1+1+1+1+2+2+2+3+3+4+4)/ 11 = 24 / 11 = 2.18181818…(为了显示，输出显示了整数2.18182)。
因为样本的大小是奇数，所以中值是中间元素2。
众数为1，因为它在样本中出现的次数最多。

```
 

 **提示：** 
-  `count.length == 256` 
-  `0 <= count[i] <= 10^9` 
-  `1 <= sum(count) <= 10^9` 
-  `count` 的众数是 **唯一** 的
 
**标签**
`数学` `双指针` `概率与统计` 


## 
```python

```
>
# 1094.拼车
[https://leetcode-cn.com/problems/car-pooling](https://leetcode-cn.com/problems/car-pooling) 
## 原题
假设你是一位顺风车司机，车上最初有 `capacity` 个空座位可以用来载客。由于道路的限制，车 **只能** 向一个方向行驶（也就是说， **不允许掉头或改变方向** ，你可以将其想象为一个向量）。

这儿有一份乘客行程计划表 `trips[][]` ，其中 `trips[i] = [num_passengers, start_location, end_location]` 包含了第 `i` 组乘客的行程信息：
- 必须接送的乘客数量；
- 乘客的上车地点；
- 以及乘客的下车地点。
这些给出的地点位置是从你的 **初始** 出发位置向前行驶到这些地点所需的距离（它们一定在你的行驶方向上）。

请你根据给出的行程计划表和车子的座位数，来判断你的车是否可以顺利完成接送所有乘客的任务（当且仅当你可以在所有给定的行程中接送所有乘客时，返回 `true` ，否则请返回 `false` ）。

 

 **示例 1：** 

```
输入：trips = [[2,1,5],[3,3,7]], capacity = 4
输出：false

```
 **示例 2：** 

```
输入：trips = [[2,1,5],[3,3,7]], capacity = 5
输出：true

```
 **示例 3：** 

```
输入：trips = [[2,1,5],[3,5,7]], capacity = 3
输出：true

```
 **示例 4：** 

```
输入：trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
输出：true

```
 

 **提示：** 
- 你可以假设乘客会自觉遵守 “ **先下后上** ” 的良好素质
-  `trips.length <= 1000` 
-  `trips[i].length == 3` 
-  `1 <= trips[i][0] <= 100` 
-  `0 <= trips[i][1] < trips[i][2] <= 1000` 
-  `1 <= capacity <= 100000` 
 
**标签**
`数组` `前缀和` `排序` `模拟` `堆（优先队列）` 


## 
```python

```
>
# 1095.山脉数组中查找目标值
[https://leetcode-cn.com/problems/find-in-mountain-array](https://leetcode-cn.com/problems/find-in-mountain-array) 
## 原题
（这是一个 **交互式问题** ）

给你一个 **山脉数组** `mountainArr` ，请你返回能够使得 `mountainArr.get(index)` **等于** `target` **最小** 的下标 `index` 值。

如果不存在这样的下标 `index` ，就请返回 `-1` 。

 

何为山脉数组？如果数组 `A` 是一个山脉数组的话，那它满足如下条件：

 **首先** ， `A.length >= 3` 

 **其次** ，在 `0 < i < A.length - 1` 条件下，存在 `i` 使得：
-  `A[0] < A[1] < ... A[i-1] < A[i]` 
-  `A[i] > A[i+1] > ... > A[A.length - 1]` 
 

你将 **不能直接访问该山脉数组** ，必须通过 `MountainArray` 接口来获取数据：
-  `MountainArray.get(k)` - 会返回数组中索引为 `k` 的元素（下标从 0 开始）
-  `MountainArray.length()` - 会返回该数组的长度
 

 **注意：** 

对 `MountainArray.get` 发起超过 `100` 次调用的提交将被视为错误答案。此外，任何试图规避判题系统的解决方案都将会导致比赛资格被取消。

为了帮助大家更好地理解交互式问题，我们准备了一个样例 “ **答案** ”：<a href="https://leetcode-cn.com/playground/RKhe3ave" target="_blank">https://leetcode-cn.com/playground/RKhe3ave</a>，请注意这 **不是一个正确答案** 。
 

 **示例 1：** 

```
输入：array = [1,2,3,4,5,3,1], target = 3
输出：2
解释：3 在数组中出现了两次，下标分别为 2 和 5，我们返回最小的下标 2。
```
 **示例 2：** 

```
输入：array = [0,1,2,4,2,1], target = 3
输出：-1
解释：3 在数组中没有出现，返回 -1。

```
 

 **提示：** 
-  `3 <= mountain_arr.length() <= 10000` 
-  `0 <= target <= 10^9` 
-  `0 <= mountain_arr.get(index) <= 10^9` 
 
**标签**
`数组` `二分查找` `交互` 


## 
```python

```
>
# 1096.花括号展开 II
[https://leetcode-cn.com/problems/brace-expansion-ii](https://leetcode-cn.com/problems/brace-expansion-ii) 
## 原题
如果你熟悉 Shell 编程，那么一定了解过花括号展开，它可以用来生成任意字符串。

花括号展开的表达式可以看作一个由 **花括号** 、 **逗号** 和 **小写英文字母** 组成的字符串，定义下面几条语法规则：
- 如果只给出单一的元素 `x` ，那么表达式表示的字符串就只有 `"x"` 。 `R(x) = {x}` 

	
- 例如，表达式 `"a"` 表示字符串 `"a"` 。
- 而表达式 `"w"` 就表示字符串 `"w"` 。
	
	
- 当两个或多个表达式并列，以逗号分隔，我们取这些表达式中元素的并集。 `R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...` 
	
- 例如，表达式 `"{a,b,c}"` 表示字符串 `"a","b","c"` 。
- 而表达式 `"{{a,b},{b,c}}"` 也可以表示字符串 `"a","b","c"` 。
	
	
- 要是两个或多个表达式相接，中间没有隔开时，我们从这些表达式中各取一个元素依次连接形成字符串。 `R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)}` 
	
- 例如，表达式 `"{a,b}{c,d}"` 表示字符串 `"ac","ad","bc","bd"` 。
	
	
- 表达式之间允许嵌套，单一元素与表达式的连接也是允许的。
	
- 例如，表达式 `"a{b,c,d}"` 表示字符串 `"ab","ac","ad"​​​​​​` 。
- 例如，表达式 `"a{b,c}{d,e}f{g,h}"` 可以表示字符串 `"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"` 。
	
	
给出表示基于给定语法规则的表达式 `expression` ，返回它所表示的所有字符串组成的有序列表。

假如你希望以「集合」的概念了解此题，也可以通过点击 “ **显示英文描述** ” 获取详情。

 

 **示例 1：** 

```

输入：expression = "{a,b}{c,{d,e}}"
输出：["ac","ad","ae","bc","bd","be"]
```
 **示例 2：** 

```

输入：expression = "{{a,z},a{b,c},{ab,z}}"
输出：["a","ab","ac","z"]
解释：输出中 不应 出现重复的组合结果。

```
 

 **提示：** 
-  `1 <= expression.length <= 60` 
-  `expression[i]` 由 `'{'` ， `'}'` ， `','` 或小写英文字母组成
- 给出的表达式 `expression` 用以表示一组基于题目描述中语法构造的字符串
 
**标签**
`栈` `广度优先搜索` `字符串` `回溯` 


## 
```python

```
>
# 1097.游戏玩法分析 V
[https://leetcode-cn.com/problems/game-play-analysis-v](https://leetcode-cn.com/problems/game-play-analysis-v) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1098.小众书籍
[https://leetcode-cn.com/problems/unpopular-books](https://leetcode-cn.com/problems/unpopular-books) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1099.小于 K 的两数之和
[https://leetcode-cn.com/problems/two-sum-less-than-k](https://leetcode-cn.com/problems/two-sum-less-than-k) 
## 原题

 
**标签**
`数组` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 1100.长度为 K 的无重复字符子串
[https://leetcode-cn.com/problems/find-k-length-substrings-with-no-repeated-characters](https://leetcode-cn.com/problems/find-k-length-substrings-with-no-repeated-characters) 
## 原题

 
**标签**
`哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
