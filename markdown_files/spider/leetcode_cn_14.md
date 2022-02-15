# 1401.圆和矩形是否有重叠
[https://leetcode-cn.com/problems/circle-and-rectangle-overlapping](https://leetcode-cn.com/problems/circle-and-rectangle-overlapping) 
## 原题
给你一个以 ( `radius` , `x_center` , `y_center` ) 表示的圆和一个与坐标轴平行的矩形 ( `x1` , `y1` , `x2` , `y2` )，其中 ( `x1` , `y1` ) 是矩形左下角的坐标，( `x2` , `y2` ) 是右上角的坐标。

如果圆和矩形有重叠的部分，请你返回 True ，否则返回 False 。

换句话说，请你检测是否 **存在** 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_4_1728.png" style="height: 167px; width: 258px;">

```
输入：radius = 1, x_center = 0, y_center = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
输出：true
解释：圆和矩形有公共点 (1,0) 

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_2_1728.png" style="height: 135px; width: 150px;">** 

```
输入：radius = 1, x_center = 0, y_center = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
输出：true

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/04/sample_6_1728.png" style="height: 165px; width: 175px;">** 

```
输入：radius = 1, x_center = 1, y_center = 1, x1 = -3, y1 = -3, x2 = 3, y2 = 3
输出：true

```
 **示例 4：** 

```
输入：radius = 1, x_center = 1, y_center = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
输出：false

```
 

 **提示：** 
-  `1 <= radius <= 2000` 
-  `-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4` 
-  `x1 < x2` 
-  `y1 < y2` 
 
**标签**
`几何` `数学` 


## 
```python

```
>
# 1402.做菜顺序
[https://leetcode-cn.com/problems/reducing-dishes](https://leetcode-cn.com/problems/reducing-dishes) 
## 原题
一个厨师收集了他 `n` 道菜的满意程度 `satisfaction` ，这个厨师做出每道菜的时间都是 1 单位时间。

一道菜的 「喜爱时间」系数定义为烹饪这道菜以及之前每道菜所花费的时间乘以这道菜的满意程度，也就是 `time[i]` * `satisfaction[i]` 。

请你返回做完所有菜 「喜爱时间」总和的最大值为多少。

你可以按 **任意** 顺序安排做菜的顺序，你也可以选择放弃做某些菜来获得更大的总和。

 

 **示例 1：** 

```
输入：satisfaction = [-1,-8,0,5,-9]
输出：14
解释：去掉第二道和最后一道菜，最大的喜爱时间系数和为 (-1*1 + 0*2 + 5*3 = 14) 。每道菜都需要花费 1 单位时间完成。
```
 **示例 2：** 

```
输入：satisfaction = [4,3,2]
输出：20
解释：按照原来顺序相反的时间做菜 (2*1 + 3*2 + 4*3 = 20)

```
 **示例 3：** 

```
输入：satisfaction = [-1,-4,-5]
输出：0
解释：大家都不喜欢这些菜，所以不做任何菜可以获得最大的喜爱时间系数。

```
 **示例 4：** 

```
输入：satisfaction = [-2,5,-1,0,3,-3]
输出：35

```
 

 **提示：** 
-  `n == satisfaction.length` 
-  `1 <= n <= 500` 
-  `-10^3 <= satisfaction[i] <= 10^3` 
 
**标签**
`贪心` `数组` `动态规划` `排序` 


## 
```python

```
>
# 1403.非递增顺序的最小子序列
[https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order](https://leetcode-cn.com/problems/minimum-subsequence-in-non-increasing-order) 
## 原题
给你一个数组 `nums` ，请你从中抽取一个子序列，满足该子序列的元素之和 **严格** 大于未包含在该子序列中的各元素之和。

如果存在多个解决方案，只需返回 **长度最小** 的子序列。如果仍然有多个解决方案，则返回 **元素之和最大** 的子序列。

与子数组不同的地方在于，「数组的子序列」不强调元素在原数组中的连续性，也就是说，它可以通过从数组中分离一些（也可能不分离）元素得到。

 **注意** ，题目数据保证满足所有约束条件的解决方案是 **唯一** 的。同时，返回的答案应当按 **非递增顺序** 排列。

 

 **示例 1：** 

```
输入：nums = [4,3,10,9,8]
输出：[10,9] 
解释：子序列 [10,9] 和 [10,8] 是最小的、满足元素之和大于其他各元素之和的子序列。但是 [10,9] 的元素之和最大。 

```
 **示例 2：** 

```
输入：nums = [4,4,7,6,7]
输出：[7,7,6] 
解释：子序列 [7,7] 的和为 14 ，不严格大于剩下的其他元素之和（14 = 4 + 4 + 6）。因此，[7,6,7] 是满足题意的最小子序列。注意，元素按非递增顺序返回。  

```
 **示例 3：** 

```
输入：nums = [6]
输出：[6]

```
 

 **提示：** 
-  `1 <= nums.length <= 500` 
-  `1 <= nums[i] <= 100` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1404.将二进制表示减到 1 的步骤数
[https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one) 
## 原题
给你一个以二进制形式表示的数字 `s` 。请你返回按下述规则将其减少到 1 所需要的步骤数：
- 
	如果当前数字为偶数，则将其除以 2 。
	
- 
	如果当前数字为奇数，则将其加上 1 。
	
题目保证你总是可以按上述规则将测试用例变为 1 。

 

 **示例 1：** 

```
输入：s = "1101"
输出：6
解释："1101" 表示十进制数 13 。
Step 1) 13 是奇数，加 1 得到 14 
Step 2) 14 是偶数，除 2 得到 7
Step 3) 7  是奇数，加 1 得到 8
Step 4) 8  是偶数，除 2 得到 4  
Step 5) 4  是偶数，除 2 得到 2 
Step 6) 2  是偶数，除 2 得到 1  

```
 **示例 2：** 

```
输入：s = "10"
输出：1
解释："10" 表示十进制数 2 。
Step 1) 2 是偶数，除 2 得到 1 

```
 **示例 3：** 

```
输入：s = "1"
输出：0

```
 

 **提示：** 
-  `1 <= s.length <= 500` 
-  `s` 由字符 `';0';` 或 `';1';` 组成。
-  `s[0] == ';1';` 
 
**标签**
`位运算` `字符串` 


## 
```python

```
>
# 1405.最长快乐字符串
[https://leetcode-cn.com/problems/longest-happy-string](https://leetcode-cn.com/problems/longest-happy-string) 
## 原题
如果字符串中不含有任何 `';aaa';` ， `';bbb';` 或 `';ccc';` 这样的字符串作为子串，那么该字符串就是一个「快乐字符串」。

给你三个整数 `a` ， `b` ， `c` ，请你返回 **任意一个** 满足下列全部条件的字符串 `s` ：
-  `s` 是一个尽可能长的快乐字符串。
-  `s` 中 **最多** 有 `a` 个字母 `';a';` 、 `b` 个字母 `';b';` 、 `c` 个字母 `';c';` 。
-  `s` 中只含有 `';a';` 、 `';b';` 、 `';c';` 三种字母。
如果不存在这样的字符串 `s` ，请返回一个空字符串 `""` 。

 

 **示例 1：** 

```
输入：a = 1, b = 1, c = 7
输出："ccaccbcc"
解释："ccbccacc" 也是一种正确答案。

```
 **示例 2：** 

```
输入：a = 2, b = 2, c = 1
输出："aabbc"

```
 **示例 3：** 

```
输入：a = 7, b = 1, c = 0
输出："aabaa"
解释：这是该测试用例的唯一正确答案。
```
 

 **提示：** 
-  `0 <= a, b, c <= 100` 
-  `a + b + c > 0` 
 
**标签**
`贪心` `字符串` `堆（优先队列）` 


## 
```python

```
>
# 1406.石子游戏 III
[https://leetcode-cn.com/problems/stone-game-iii](https://leetcode-cn.com/problems/stone-game-iii) 
## 原题
Alice 和 Bob 用几堆石子在做游戏。几堆石子排成一行，每堆石子都对应一个得分，由数组 `stoneValue` 给出。

Alice 和 Bob 轮流取石子， **Alice** 总是先开始。在每个玩家的回合中，该玩家可以拿走剩下石子中的的前 **1、2 或 3 堆石子** 。比赛一直持续到所有石头都被拿走。

每个玩家的最终得分为他所拿到的每堆石子的对应得分之和。每个玩家的初始分数都是 **0** 。比赛的目标是决出最高分，得分最高的选手将会赢得比赛，比赛也可能会出现平局。

假设 Alice 和 Bob 都采取 **最优策略** 。如果 Alice 赢了就返回 *"Alice"* *，* Bob 赢了就返回 *"Bob"，* 平局（分数相同）返回 *"Tie"* 。

 

 **示例 1：** 

```
输入：values = [1,2,3,7]
输出："Bob"
解释：Alice 总是会输，她的最佳选择是拿走前三堆，得分变成 6 。但是 Bob 的得分为 7，Bob 获胜。

```
 **示例 2：** 

```
输入：values = [1,2,3,-9]
输出："Alice"
解释：Alice 要想获胜就必须在第一个回合拿走前三堆石子，给 Bob 留下负分。
如果 Alice 只拿走第一堆，那么她的得分为 1，接下来 Bob 拿走第二、三堆，得分为 5 。之后 Alice 只能拿到分数 -9 的石子堆，输掉比赛。
如果 Alice 拿走前两堆，那么她的得分为 3，接下来 Bob 拿走第三堆，得分为 3 。之后 Alice 只能拿到分数 -9 的石子堆，同样会输掉比赛。
注意，他们都应该采取 最优策略 ，所以在这里 Alice 将选择能够使她获胜的方案。
```
 **示例 3：** 

```
输入：values = [1,2,3,6]
输出："Tie"
解释：Alice 无法赢得比赛。如果她决定选择前三堆，她可以以平局结束比赛，否则她就会输。

```
 **示例 4：** 

```
输入：values = [1,2,3,-1,-2,-3,7]
输出："Alice"

```
 **示例 5：** 

```
输入：values = [-1,-2,-3]
输出："Tie"

```
 

 **提示：** 
-  `1 <= values.length <= 50000` 
-  `-1000 <= values[i] <= 1000` 
 
**标签**
`数组` `数学` `动态规划` `博弈` 


## 
```python

```
>
# 1407.排名靠前的旅行者
[https://leetcode-cn.com/problems/top-travellers](https://leetcode-cn.com/problems/top-travellers) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1408.数组中的字符串匹配
[https://leetcode-cn.com/problems/string-matching-in-an-array](https://leetcode-cn.com/problems/string-matching-in-an-array) 
## 原题
给你一个字符串数组 `words` ，数组中的每个字符串都可以看作是一个单词。请你按 **任意** 顺序返回 `words` 中是其他单词的子字符串的所有单词。

如果你可以删除 `words[j]` 最左侧和/或最右侧的若干字符得到 `word[i]` ，那么字符串 `words[i]` 就是 `words[j]` 的一个子字符串。

 

 **示例 1：** 

```
输入：words = ["mass","as","hero","superhero"]
输出：["as","hero"]
解释："as" 是 "mass" 的子字符串，"hero" 是 "superhero" 的子字符串。
["hero","as"] 也是有效的答案。

```
 **示例 2：** 

```
输入：words = ["leetcode","et","code"]
输出：["et","code"]
解释："et" 和 "code" 都是 "leetcode" 的子字符串。

```
 **示例 3：** 

```
输入：words = ["blue","green","bu"]
输出：[]

```
 

 **提示：** 
-  `1 <= words.length <= 100` 
-  `1 <= words[i].length <= 30` 
-  `words[i]` 仅包含小写英文字母。
- 题目数据 **保证** 每个 `words[i]` 都是独一无二的。
 
**标签**
`字符串` `字符串匹配` 


## 
```python

```
>
# 1409.查询带键的排列
[https://leetcode-cn.com/problems/queries-on-a-permutation-with-key](https://leetcode-cn.com/problems/queries-on-a-permutation-with-key) 
## 原题
给你一个待查数组 `queries` ，数组中的元素为 `1` 到 `m` 之间的正整数。 请你根据以下规则处理所有待查项 `queries[i]` （从 `i=0` 到 `i=queries.length-1` ）：
- 一开始，排列 `P=[1,2,3,...,m]` 。
- 对于当前的 `i` ，请你找出待查项 `queries[i]` 在排列 `P` 中的位置（ **下标从 0 开始** ），然后将其从原位置移动到排列 `P` 的起始位置（即下标为 0 处）。注意， `queries[i]` 在 `P` 中的位置就是 `queries[i]` 的查询结果。
请你以数组形式返回待查数组 `queries` 的查询结果。

 

 **示例 1：** 

```
输入：queries = [3,1,2,1], m = 5
输出：[2,1,2,1] 
解释：待查数组 queries 处理如下：
对于 i=0: queries[i]=3, P=[1,2,3,4,5], 3 在 P 中的位置是 2，接着我们把 3 移动到 P 的起始位置，得到 P=[3,1,2,4,5] 。
对于 i=1: queries[i]=1, P=[3,1,2,4,5], 1 在 P 中的位置是 1，接着我们把 1 移动到 P 的起始位置，得到 P=[1,3,2,4,5] 。 
对于 i=2: queries[i]=2, P=[1,3,2,4,5], 2 在 P 中的位置是 2，接着我们把 2 移动到 P 的起始位置，得到 P=[2,1,3,4,5] 。
对于 i=3: queries[i]=1, P=[2,1,3,4,5], 1 在 P 中的位置是 1，接着我们把 1 移动到 P 的起始位置，得到 P=[1,2,3,4,5] 。 
因此，返回的结果数组为 [2,1,2,1] 。  

```
 **示例 2：** 

```
输入：queries = [4,1,2,2], m = 4
输出：[3,1,2,0]

```
 **示例 3：** 

```
输入：queries = [7,5,5,8,3], m = 8
输出：[6,5,0,7,5]

```
 

 **提示：** 
-  `1 <= m <= 10^3` 
-  `1 <= queries.length <= m` 
-  `1 <= queries[i] <= m` 
 
**标签**
`树状数组` `数组` `模拟` 


## 
```python

```
>
# 1410.HTML 实体解析器
[https://leetcode-cn.com/problems/html-entity-parser](https://leetcode-cn.com/problems/html-entity-parser) 
## 原题
「HTML 实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。

HTML 里这些特殊字符和它们对应的字符实体包括：
-  **双引号：** 字符实体为 `&amp;quot;` ，对应的字符是 `"` 。
-  **单引号：** 字符实体为 `&amp;apos;` ，对应的字符是 `';` 。
-  **与符号：** 字符实体为 `&amp;amp;` ，对应对的字符是 `&amp;` 。
-  **大于号：** 字符实体为 `&amp;gt;` ，对应的字符是 `>` 。
-  **小于号：** 字符实体为 `&amp;lt;` ，对应的字符是 `<` 。
-  **斜线号：** 字符实体为 `&amp;frasl;` ，对应的字符是 `/` 。
给你输入字符串 `text` ，请你实现一个 HTML 实体解析器，返回解析器解析后的结果。

 

 **示例 1：** 

```

输入：text = "&amp;amp; is an HTML entity but &amp;ambassador; is not."
输出："&amp; is an HTML entity but &amp;ambassador; is not."
解释：解析器把字符实体 &amp;amp; 用 &amp; 替换

```
 **示例 2：** 

```

输入：text = "and I quote: &amp;quot;...&amp;quot;"
输出："and I quote: \"...\""

```
 **示例 3：** 

```

输入：text = "Stay home! Practice on Leetcode :)"
输出："Stay home! Practice on Leetcode :)"

```
 **示例 4：** 

```

输入：text = "x &amp;gt; y &amp;amp;&amp;amp; x &amp;lt; y is always false"
输出："x > y &amp;&amp; x < y is always false"

```
 **示例 5：** 

```

输入：text = "leetcode.com&amp;frasl;problemset&amp;frasl;all"
输出："leetcode.com/problemset/all"

```
 

 **提示：** 
-  `1 <= text.length <= 10^5` 
- 字符串可能包含 256 个ASCII 字符中的任意字符。
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1411.给 N x 3 网格图涂色的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-paint-n-3-grid](https://leetcode-cn.com/problems/number-of-ways-to-paint-n-3-grid) 
## 原题
你有一个 `n x 3` 的网格图 `grid` ，你需要用 **红，黄，绿** 三种颜色之一给每一个格子上色，且确保相邻格子颜色不同（也就是有相同水平边或者垂直边的格子颜色不同）。

给你网格图的行数 `n` 。

请你返回给 `grid` 涂色的方案数。由于答案可能会非常大，请你返回答案对 `10^9 + 7` 取余的结果。

 

 **示例 1：** 

```
输入：n = 1
输出：12
解释：总共有 12 种可行的方法：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/12/e1.png" style="height: 289px; width: 450px;">

```
 **示例 2：** 

```
输入：n = 2
输出：54

```
 **示例 3：** 

```
输入：n = 3
输出：246

```
 **示例 4：** 

```
输入：n = 7
输出：106494

```
 **示例 5：** 

```
输入：n = 5000
输出：30228214

```
 

 **提示：** 
-  `n == grid.length` 
-  `grid[i].length == 3` 
-  `1 <= n <= 5000` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 1412.查找成绩处于中游的学生
[https://leetcode-cn.com/problems/find-the-quiet-students-in-all-exams](https://leetcode-cn.com/problems/find-the-quiet-students-in-all-exams) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1413.逐步求和得到正数的最小值
[https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum](https://leetcode-cn.com/problems/minimum-value-to-get-positive-step-by-step-sum) 
## 原题
给你一个整数数组 `nums` 。你可以选定任意的 **正数** startValue 作为初始值。

你需要从左到右遍历 `nums` 数组，并将 startValue 依次累加上 `nums` 数组中的值。

请你在确保累加和始终大于等于 1 的前提下，选出一个最小的 **正数** 作为 startValue 。

 

 **示例 1：** 

```

输入：nums = [-3,2,-3,4,2]
输出：5
解释：如果你选择 startValue = 4，在第三次累加时，和小于 1 。
                累加求和
                startValue = 4 | startValue = 5 | nums
                  (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
                  (1 +2 ) = 3  | (2 +2 ) = 4    |   2
                  (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
                  (0 +4 ) = 4  | (1 +4 ) = 5    |   4
                  (4 +2 ) = 6  | (5 +2 ) = 7    |   2

```
 **示例 2：** 

```

输入：nums = [1,2]
输出：1
解释：最小的 startValue 需要是正数。

```
 **示例 3：** 

```

输入：nums = [1,-2,-3]
输出：5

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `-100 <= nums[i] <= 100` 
 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 1414.和为 K 的最少斐波那契数字数目
[https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k](https://leetcode-cn.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k) 
## 原题
给你数字 `k` ，请你返回和为 `k` 的斐波那契数字的最少数目，其中，每个斐波那契数字都可以被使用多次。

斐波那契数字定义为：
- F<sub>1</sub> = 1
- F<sub>2</sub> = 1
- F<sub>n</sub> = F<sub>n-1</sub> + F<sub>n-2</sub> ， 其中 n > 2 。
数据保证对于给定的 `k` ，一定能找到可行解。

 

 **示例 1：** 

```
输入：k = 7
输出：2 
解释：斐波那契数字为：1，1，2，3，5，8，13，&hellip;&hellip;
对于 k = 7 ，我们可以得到 2 + 5 = 7 。
```
 **示例 2：** 

```
输入：k = 10
输出：2 
解释：对于 k = 10 ，我们可以得到 2 + 8 = 10 。

```
 **示例 3：** 

```
输入：k = 19
输出：3 
解释：对于 k = 19 ，我们可以得到 1 + 5 + 13 = 19 。

```
 

 **提示：** 
-  `1 <= k <= 10^9` 
 
**标签**
`贪心` 


## 
```python

```
>
# 1415.长度为 n 的开心字符串中字典序第 k 小的字符串
[https://leetcode-cn.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n](https://leetcode-cn.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n) 
## 原题
一个 「开心字符串」定义为：
- 仅包含小写字母 `[';a';, ';b';, ';c';]` .
- 对所有在 `1` 到 `s.length - 1` 之间的 `i` ，满足 `s[i] != s[i + 1]` （字符串的下标从 1 开始）。
比方说，字符串 **"abc"** ， **"ac"，"b"** 和 **"abcbabcbcb"** 都是开心字符串，但是 **"aa"** ， **"baa"** 和 **"ababbc"** 都不是开心字符串。

给你两个整数 `n` 和 `k` ，你需要将长度为 `n` 的所有开心字符串按字典序排序。

请你返回排序后的第 k 个开心字符串，如果长度为 `n` 的开心字符串少于 `k` 个，那么请你返回 **空字符串** 。

 

 **示例 1：** 

```
输入：n = 1, k = 3
输出："c"
解释：列表 ["a", "b", "c"] 包含了所有长度为 1 的开心字符串。按照字典序排序后第三个字符串为 "c" 。

```
 **示例 2：** 

```
输入：n = 1, k = 4
输出：""
解释：长度为 1 的开心字符串只有 3 个。

```
 **示例 3：** 

```
输入：n = 3, k = 9
输出："cab"
解释：长度为 3 的开心字符串总共有 12 个 ["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"] 。第 9 个字符串为 "cab"

```
 **示例 4：** 

```
输入：n = 2, k = 7
输出：""

```
 **示例 5：** 

```
输入：n = 10, k = 100
输出："abacbabacb"

```
 

 **提示：** 
-  `1 <= n <= 10` 
-  `1 <= k <= 100` 
 

 
**标签**
`字符串` `回溯` 


## 
```python

```
>
# 1416.恢复数组
[https://leetcode-cn.com/problems/restore-the-array](https://leetcode-cn.com/problems/restore-the-array) 
## 原题
某个程序本来应该输出一个整数数组。但是这个程序忘记输出空格了以致输出了一个数字字符串，我们所知道的信息只有：数组中所有整数都在 `[1, k]` 之间，且数组中的数字都没有前导 0 。

给你字符串 `s` 和整数 `k` 。可能会有多种不同的数组恢复结果。

按照上述程序，请你返回所有可能输出字符串 `s` 的数组方案数。

由于数组方案数可能会很大，请你返回它对 `10^9 + 7` **取余** 后的结果。

 

 **示例 1：** 

```
输入：s = "1000", k = 10000
输出：1
解释：唯一一种可能的数组方案是 [1000]

```
 **示例 2：** 

```
输入：s = "1000", k = 10
输出：0
解释：不存在任何数组方案满足所有整数都 >= 1 且 <= 10 同时输出结果为 s 。

```
 **示例 3：** 

```
输入：s = "1317", k = 2000
输出：8
解释：可行的数组方案为 [1317]，[131,7]，[13,17]，[1,317]，[13,1,7]，[1,31,7]，[1,3,17]，[1,3,1,7]

```
 **示例 4：** 

```
输入：s = "2020", k = 30
输出：1
解释：唯一可能的数组方案是 [20,20] 。 [2020] 不是可行的数组方案，原因是 2020 > 30 。 [2,020] 也不是可行的数组方案，因为 020 含有前导 0 。

```
 **示例 5：** 

```
输入：s = "1234567890", k = 90
输出：34

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` .
-  `s` 只包含数字且不包含前导 0 。
-  `1 <= k <= 10^9` .
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1417.重新格式化字符串
[https://leetcode-cn.com/problems/reformat-the-string](https://leetcode-cn.com/problems/reformat-the-string) 
## 原题
给你一个混合了数字和字母的字符串 `s` ，其中的字母均为小写英文字母。

请你将该字符串重新格式化，使得任意两个相邻字符的类型都不同。也就是说，字母后面应该跟着数字，而数字后面应该跟着字母。

请你返回 **重新格式化后** 的字符串；如果无法按要求重新格式化，则返回一个 **空字符串** 。

 

 **示例 1：** 

```
输入：s = "a0b1c2"
输出："0a1b2c"
解释："0a1b2c" 中任意两个相邻字符的类型都不同。 "a0b1c2", "0a1b2c", "0c2a1b" 也是满足题目要求的答案。

```
 **示例 2：** 

```
输入：s = "leetcode"
输出：""
解释："leetcode" 中只有字母，所以无法满足重新格式化的条件。

```
 **示例 3：** 

```
输入：s = "1229857369"
输出：""
解释："1229857369" 中只有数字，所以无法满足重新格式化的条件。

```
 **示例 4：** 

```
输入：s = "covid2019"
输出："c2o0v1i9d"

```
 **示例 5：** 

```
输入：s = "ab123"
输出："1a2b3"

```
 

 **提示：** 
-  `1 <= s.length <= 500` 
-  `s` 仅由小写英文字母和/或数字组成。
 
**标签**
`字符串` 


## 
```python

```
>
# 1418.点菜展示表
[https://leetcode-cn.com/problems/display-table-of-food-orders-in-a-restaurant](https://leetcode-cn.com/problems/display-table-of-food-orders-in-a-restaurant) 
## 原题
给你一个数组 `orders` ，表示客户在餐厅中完成的订单，确切地说， `orders[i]=[customerName<sub>i</sub>,tableNumber<sub>i</sub>,foodItem<sub>i</sub>]` ，其中 `customerName<sub>i</sub>` 是客户的姓名， `tableNumber<sub>i</sub>` 是客户所在餐桌的桌号，而 `foodItem<sub>i</sub>` 是客户点的餐品名称。

请你返回该餐厅的 **点菜展示表** *。* 在这张表中，表中第一行为标题，其第一列为餐桌桌号 “Table” ，后面每一列都是按字母顺序排列的餐品名称。接下来每一行中的项则表示每张餐桌订购的相应餐品数量，第一列应当填对应的桌号，后面依次填写下单的餐品数量。

注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。

 

 **示例 1：** 

```
输入：orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
输出：[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
解释：
点菜展示表如下所示：
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
对于餐桌 3：David 点了 "Ceviche" 和 "Fried Chicken"，而 Rous 点了 "Ceviche"
而餐桌 5：Carla 点了 "Water" 和 "Ceviche"
餐桌 10：Corina 点了 "Beef Burrito" 

```
 **示例 2：** 

```
输入：orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
输出：[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]] 
解释：
对于餐桌 1：Adam 和 Brianna 都点了 "Canadian Waffles"
而餐桌 12：James, Ratesh 和 Amadeus 都点了 "Fried Chicken"

```
 **示例 3：** 

```
输入：orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
输出：[["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]

```
 

 **提示：** 
-  `1 <= orders.length <= 5 * 10^4` 
-  `orders[i].length == 3` 
-  `1 <= customerName<sub>i</sub>.length, foodItem<sub>i</sub>.length <= 20` 
-  `customerName<sub>i</sub>` 和 `foodItem<sub>i</sub>` 由大小写英文字母及空格字符 `'; ';` 组成。
-  `tableNumber<sub>i</sub>` 是 `1` 到 `500` 范围内的整数。
 
**标签**
`数组` `哈希表` `字符串` `有序集合` `排序` 


## 
```python

```
>
# 1419.数青蛙
[https://leetcode-cn.com/problems/minimum-number-of-frogs-croaking](https://leetcode-cn.com/problems/minimum-number-of-frogs-croaking) 
## 原题
给你一个字符串 `croakOfFrogs` ，它表示不同青蛙发出的蛙鸣声（字符串 `"croak"` ）的组合。由于同一时间可以有多只青蛙呱呱作响，所以 `croakOfFrogs` 中会混合多个 `“croak”` *。* 

请你返回模拟字符串中所有蛙鸣所需不同青蛙的最少数目。

要想发出蛙鸣 "croak"，青蛙必须 **依序** 输出 `‘c’, ’r’, ’o’, ’a’, ’k’` 这 5 个字母。如果没有输出全部五个字母，那么它就不会发出声音。如果字符串 `croakOfFrogs` 不是由若干有效的 "croak" 字符混合而成，请返回 `-1` 。

 

 **示例 1：** 

```

输入：croakOfFrogs = "croakcroak"
输出：1 
解释：一只青蛙 “呱呱” 两次

```
 **示例 2：** 

```

输入：croakOfFrogs = "crcoakroak"
输出：2 
解释：最少需要两只青蛙，“呱呱” 声用黑体标注
第一只青蛙 "crcoakroak"
第二只青蛙 "crcoakroak"

```
 **示例 3：** 

```

输入：croakOfFrogs = "croakcrook"
输出：-1
解释：给出的字符串不是 "croak" 的有效组合。

```
 

 **提示：** 
-  `1 <= croakOfFrogs.length <= 10^5` 
- 字符串中的字符只有 `'c'` , `'r'` , `'o'` , `'a'` 或者 `'k'` 
 
**标签**
`字符串` `计数` 


## 
```python

```
>
# 1420.生成数组
[https://leetcode-cn.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons](https://leetcode-cn.com/problems/build-array-where-you-can-find-the-maximum-exactly-k-comparisons) 
## 原题
给你三个整数 `n` 、 `m` 和 `k` 。下图描述的算法用于找出正整数数组中最大的元素。

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/19/e.png" style="height: 372px; width: 424px;">

请你生成一个具有下述属性的数组 `arr` ：
-  `arr` 中有 `n` 个整数。
-  `1 <= arr[i] <= m` 其中 `(0 <= i < n)` 。
- 将上面提到的算法应用于 `arr` ， `search_cost` 的值等于 `k` 。
返回上述条件下生成数组 `arr` 的 **方法数** ，由于答案可能会很大，所以 **必须** 对 `10^9 + 7` 取余。

 

 **示例 1：** 

```
输入：n = 2, m = 3, k = 1
输出：6
解释：可能的数组分别为 [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]

```
 **示例 2：** 

```
输入：n = 5, m = 2, k = 3
输出：0
解释：没有数组可以满足上述条件

```
 **示例 3：** 

```
输入：n = 9, m = 1, k = 1
输出：1
解释：可能的数组只有 [1, 1, 1, 1, 1, 1, 1, 1, 1]

```
 **示例 4：** 

```
输入：n = 50, m = 100, k = 25
输出：34549172
解释：不要忘了对 1000000007 取余

```
 **示例 5：** 

```
输入：n = 37, m = 17, k = 7
输出：418930126

```
 

 **提示：** 
-  `1 <= n <= 50` 
-  `1 <= m <= 100` 
-  `0 <= k <= n` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 1421.净现值查询
[https://leetcode-cn.com/problems/npv-queries](https://leetcode-cn.com/problems/npv-queries) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1422.分割字符串的最大得分
[https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string](https://leetcode-cn.com/problems/maximum-score-after-splitting-a-string) 
## 原题
给你一个由若干 0 和 1 组成的字符串 `s` ，请你计算并返回将该字符串分割成两个 **非空** 子字符串（即 **左** 子字符串和 **右** 子字符串）所能获得的最大得分。

「分割字符串的得分」为 **左** 子字符串中 **0** 的数量加上 **右** 子字符串中 **1** 的数量。

 

 **示例 1：** 

```
输入：s = "011101"
输出：5 
解释：
将字符串 s 划分为两个非空子字符串的可行方案有：
左子字符串 = "0" 且 右子字符串 = "11101"，得分 = 1 + 4 = 5 
左子字符串 = "01" 且 右子字符串 = "1101"，得分 = 1 + 3 = 4 
左子字符串 = "011" 且 右子字符串 = "101"，得分 = 1 + 2 = 3 
左子字符串 = "0111" 且 右子字符串 = "01"，得分 = 1 + 1 = 2 
左子字符串 = "01110" 且 右子字符串 = "1"，得分 = 2 + 1 = 3

```
 **示例 2：** 

```
输入：s = "00111"
输出：5
解释：当 左子字符串 = "00" 且 右子字符串 = "111" 时，我们得到最大得分 = 2 + 3 = 5

```
 **示例 3：** 

```
输入：s = "1111"
输出：3

```
 

 **提示：** 
-  `2 <= s.length <= 500` 
- 字符串 `s` 仅由字符 `';0';` 和 `';1';` 组成。
 
**标签**
`字符串` 


## 
```python

```
>
# 1423.可获得的最大点数
[https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards](https://leetcode-cn.com/problems/maximum-points-you-can-obtain-from-cards) 
## 原题
几张卡牌 **排成一行** ，每张卡牌都有一个对应的点数。点数由整数数组 `cardPoints` 给出。

每次行动，你可以从行的开头或者末尾拿一张卡牌，最终你必须正好拿 `k` 张卡牌。

你的点数就是你拿到手中的所有卡牌的点数之和。

给你一个整数数组 `cardPoints` 和整数 `k` ，请你返回可以获得的最大点数。

 

 **示例 1：** 

```
输入：cardPoints = [1,2,3,4,5,6,1], k = 3
输出：12
解释：第一次行动，不管拿哪张牌，你的点数总是 1 。但是，先拿最右边的卡牌将会最大化你的可获得点数。最优策略是拿右边的三张牌，最终点数为 1 + 6 + 5 = 12 。

```
 **示例 2：** 

```
输入：cardPoints = [2,2,2], k = 2
输出：4
解释：无论你拿起哪两张卡牌，可获得的点数总是 4 。

```
 **示例 3：** 

```
输入：cardPoints = [9,7,7,9,7,7,9], k = 7
输出：55
解释：你必须拿起所有卡牌，可以获得的点数为所有卡牌的点数之和。

```
 **示例 4：** 

```
输入：cardPoints = [1,1000,1], k = 1
输出：1
解释：你无法拿到中间那张卡牌，所以可以获得的最大点数为 1 。 

```
 **示例 5：** 

```
输入：cardPoints = [1,79,80,1,1,1,200,1], k = 3
输出：202

```
 

 **提示：** 
-  `1 <= cardPoints.length <= 10^5` 
-  `1 <= cardPoints[i] <= 10^4` 
-  `1 <= k <= cardPoints.length` 
 
**标签**
`数组` `前缀和` `滑动窗口` 


## 
```python

```
>
# 1424.对角线遍历 II
[https://leetcode-cn.com/problems/diagonal-traverse-ii](https://leetcode-cn.com/problems/diagonal-traverse-ii) 
## 原题
给你一个列表 `nums` ，里面每一个元素都是一个整数列表。请你依照下面各图的规则，按顺序返回 `nums` 中对角线上的整数。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/23/sample_1_1784.png" style="height: 143px; width: 158px;">** 

```
输入：nums = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,4,2,7,5,3,8,6,9]

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/23/sample_2_1784.png" style="height: 177px; width: 230px;">** 

```
输入：nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
输出：[1,6,2,8,7,3,9,4,12,10,5,13,11,14,15,16]

```
 **示例 3：** 

```
输入：nums = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
输出：[1,4,2,5,3,8,6,9,7,10,11]

```
 **示例 4：** 

```
输入：nums = [[1,2,3,4,5,6]]
输出：[1,2,3,4,5,6]

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i].length <= 10^5` 
-  `1 <= nums[i][j] <= 10^9` 
-  `nums` 中最多有 `10^5` 个数字。
 
**标签**
`数组` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1425.带限制的子序列和
[https://leetcode-cn.com/problems/constrained-subsequence-sum](https://leetcode-cn.com/problems/constrained-subsequence-sum) 
## 原题
给你一个整数数组 `nums` 和一个整数 `k` ，请你返回 **非空** 子序列元素和的最大值，子序列需要满足：子序列中每两个 **相邻** 的整数 `nums[i]` 和 `nums[j]` ，它们在原数组中的下标 `i` 和 `j` 满足 `i < j` 且 `j - i <= k` 。

数组的子序列定义为：将数组中的若干个数字删除（可以删除 0 个数字），剩下的数字按照原本的顺序排布。

 

 **示例 1：** 

```
输入：nums = [10,2,-10,5,20], k = 2
输出：37
解释：子序列为 [10, 2, 5, 20] 。

```
 **示例 2：** 

```
输入：nums = [-1,-2,-3], k = 1
输出：-1
解释：子序列必须是非空的，所以我们选择最大的数字。

```
 **示例 3：** 

```
输入：nums = [10,-2,-10,-5,20], k = 2
输出：23
解释：子序列为 [10, -2, -5, 20] 。

```
 

 **提示：** 
-  `1 <= k <= nums.length <= 10^5` 
-  `-10^4 <= nums[i] <= 10^4` 
 
**标签**
`队列` `数组` `动态规划` `滑动窗口` `单调队列` `堆（优先队列）` 


## 
```python

```
>
# 1426.数元素
[https://leetcode-cn.com/problems/counting-elements](https://leetcode-cn.com/problems/counting-elements) 
## 原题

 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1427.字符串的左右移
[https://leetcode-cn.com/problems/perform-string-shifts](https://leetcode-cn.com/problems/perform-string-shifts) 
## 原题

 
**标签**
`数组` `数学` `字符串` 


## 
```python

```
>
# 1428.至少有一个 1 的最左端列
[https://leetcode-cn.com/problems/leftmost-column-with-at-least-a-one](https://leetcode-cn.com/problems/leftmost-column-with-at-least-a-one) 
## 原题

 
**标签**
`数组` `二分查找` `交互` `矩阵` 


## 
```python

```
>
# 1429.第一个唯一数字
[https://leetcode-cn.com/problems/first-unique-number](https://leetcode-cn.com/problems/first-unique-number) 
## 原题

 
**标签**
`设计` `队列` `数组` `哈希表` `数据流` 


## 
```python

```
>
# 1430.判断给定的序列是否是二叉树从根到叶的路径
[https://leetcode-cn.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree](https://leetcode-cn.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 1431.拥有最多糖果的孩子
[https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies](https://leetcode-cn.com/problems/kids-with-the-greatest-number-of-candies) 
## 原题
给你一个数组 `candies` 和一个整数 `extraCandies` ，其中 `candies[i]` 代表第 `i` 个孩子拥有的糖果数目。

对每一个孩子，检查是否存在一种方案，将额外的 `extraCandies` 个糖果分配给孩子们之后，此孩子有 **最多** 的糖果。注意，允许有多个孩子同时拥有 **最多** 的糖果数目。

 

 **示例 1：** 

```
输入：candies = [2,3,5,1,3], extraCandies = 3
输出：[true,true,true,false,true] 
解释：
孩子 1 有 2 个糖果，如果他得到所有额外的糖果（3个），那么他总共有 5 个糖果，他将成为拥有最多糖果的孩子。
孩子 2 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。
孩子 3 有 5 个糖果，他已经是拥有最多糖果的孩子。
孩子 4 有 1 个糖果，即使他得到所有额外的糖果，他也只有 4 个糖果，无法成为拥有糖果最多的孩子。
孩子 5 有 3 个糖果，如果他得到至少 2 个额外糖果，那么他将成为拥有最多糖果的孩子。

```
 **示例 2：** 

```
输入：candies = [4,2,1,1,2], extraCandies = 1
输出：[true,false,false,false,false] 
解释：只有 1 个额外糖果，所以不管额外糖果给谁，只有孩子 1 可以成为拥有糖果最多的孩子。

```
 **示例 3：** 

```
输入：candies = [12,1,12], extraCandies = 10
输出：[true,false,true]

```
 

 **提示：** 
-  `2 <= candies.length <= 100` 
-  `1 <= candies[i] <= 100` 
-  `1 <= extraCandies <= 50` 
 
**标签**
`数组` 


## 
```python

```
>
# 1432.改变一个整数能得到的最大差值
[https://leetcode-cn.com/problems/max-difference-you-can-get-from-changing-an-integer](https://leetcode-cn.com/problems/max-difference-you-can-get-from-changing-an-integer) 
## 原题
给你一个整数 `num` 。你可以对它进行如下步骤恰好 **两次** ：
- 选择一个数字 `x (0 <= x <= 9)` .
- 选择另一个数字 `y (0 <= y <= 9)` 。数字 `y` 可以等于 `x` 。
- 将 `num` 中所有出现 `x` 的数位都用 `y` 替换。
- 得到的新的整数 **不能** 有前导 0 ，得到的新整数也 **不能** 是 0 。
令两次对 `num` 的操作得到的结果分别为 `a` 和 `b` 。

请你返回 `a` 和 `b` 的 **最大差值** 。

 

 **示例 1：** 

```
输入：num = 555
输出：888
解释：第一次选择 x = 5 且 y = 9 ，并把得到的新数字保存在 a 中。
第二次选择 x = 5 且 y = 1 ，并把得到的新数字保存在 b 中。
现在，我们有 a = 999 和 b = 111 ，最大差值为 888

```
 **示例 2：** 

```
输入：num = 9
输出：8
解释：第一次选择 x = 9 且 y = 9 ，并把得到的新数字保存在 a 中。
第二次选择 x = 9 且 y = 1 ，并把得到的新数字保存在 b 中。
现在，我们有 a = 9 和 b = 1 ，最大差值为 8

```
 **示例 3：** 

```
输入：num = 123456
输出：820000

```
 **示例 4：** 

```
输入：num = 10000
输出：80000

```
 **示例 5：** 

```
输入：num = 9288
输出：8700

```
 

 **提示：** 
-  `1 <= num <= 10^8` 
 
**标签**
`贪心` `数学` 


## 
```python

```
>
# 1433.检查一个字符串是否可以打破另一个字符串
[https://leetcode-cn.com/problems/check-if-a-string-can-break-another-string](https://leetcode-cn.com/problems/check-if-a-string-can-break-another-string) 
## 原题
给你两个字符串 `s1` 和 `s2` ，它们长度相等，请你检查是否存在一个 `s1` 的排列可以打破 `s2` 的一个排列，或者是否存在一个 `s2` 的排列可以打破 `s1` 的一个排列。

字符串 `x` 可以打破字符串 `y` （两者长度都为 `n` ）需满足对于所有 `i` （在 `0` 到 `n - 1` 之间）都有 `x[i] >= y[i]` （字典序意义下的顺序）。

 

 **示例 1：** 

```
输入：s1 = "abc", s2 = "xya"
输出：true
解释："ayx" 是 s2="xya" 的一个排列，"abc" 是字符串 s1="abc" 的一个排列，且 "ayx" 可以打破 "abc" 。

```
 **示例 2：** 

```
输入：s1 = "abe", s2 = "acd"
输出：false 
解释：s1="abe" 的所有排列包括："abe"，"aeb"，"bae"，"bea"，"eab" 和 "eba" ，s2="acd" 的所有排列包括："acd"，"adc"，"cad"，"cda"，"dac" 和 "dca"。然而没有任何 s1 的排列可以打破 s2 的排列。也没有 s2 的排列能打破 s1 的排列。

```
 **示例 3：** 

```
输入：s1 = "leetcodee", s2 = "interview"
输出：true

```
 

 **提示：** 
-  `s1.length == n` 
-  `s2.length == n` 
-  `1 <= n <= 10^5` 
- 所有字符串都只包含小写英文字母。
 
**标签**
`贪心` `字符串` `排序` 


## 
```python

```
>
# 1434.每个人戴不同帽子的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-wear-different-hats-to-each-other](https://leetcode-cn.com/problems/number-of-ways-to-wear-different-hats-to-each-other) 
## 原题
总共有 `n` 个人和 `40` 种不同的帽子，帽子编号从 `1` 到 `40` 。

给你一个整数列表的列表 `hats` ，其中 `hats[i]` 是第 `i` 个人所有喜欢帽子的列表。

请你给每个人安排一顶他喜欢的帽子，确保每个人戴的帽子跟别人都不一样，并返回方案数。

由于答案可能很大，请返回它对 `10^9 + 7` 取余后的结果。

 

 **示例 1：** 

```

输入：hats = [[3,4],[4,5],[5]]
输出：1
解释：给定条件下只有一种方法选择帽子。
第一个人选择帽子 3，第二个人选择帽子 4，最后一个人选择帽子 5。
```
 **示例 2：** 

```

输入：hats = [[3,5,1],[3,5]]
输出：4
解释：总共有 4 种安排帽子的方法：
(3,5)，(5,3)，(1,3) 和 (1,5)

```
 **示例 3：** 

```

输入：hats = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
输出：24
解释：每个人都可以从编号为 1 到 4 的帽子中选。
(1,2,3,4) 4 个帽子的排列方案数为 24 。

```
 **示例 4：** 

```

输入：hats = [[1,2,3],[2,3,5,6],[1,3,7,9],[1,8,9],[2,5,7]]
输出：111

```
 

 **提示：** 
-  `n == hats.length` 
-  `1 <= n <= 10` 
-  `1 <= hats[i].length <= 40` 
-  `1 <= hats[i][j] <= 40` 
-  `hats[i]` 包含一个数字互不相同的整数列表。
 
**标签**
`位运算` `数组` `动态规划` `状态压缩` 


## 
```python

```
>
# 1435.制作会话柱状图
[https://leetcode-cn.com/problems/create-a-session-bar-chart](https://leetcode-cn.com/problems/create-a-session-bar-chart) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1436.旅行终点站
[https://leetcode-cn.com/problems/destination-city](https://leetcode-cn.com/problems/destination-city) 
## 原题
给你一份旅游线路图，该线路图中的旅行线路用数组 `paths` 表示，其中 `paths[i] = [cityA<sub>i</sub>, cityB<sub>i</sub>]` 表示该线路将会从 `cityA<sub>i</sub>` 直接前往 `cityB<sub>i</sub>` 。请你找出这次旅行的终点站，即没有任何可以通往其他城市的线路的城市 *。* 

题目数据保证线路图会形成一条不存在循环的线路，因此恰有一个旅行终点站。

 

 **示例 1：** 

```

输入：paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
输出："Sao Paulo" 
解释：从 "London" 出发，最后抵达终点站 "Sao Paulo" 。本次旅行的路线是 "London" -> "New York" -> "Lima" -> "Sao Paulo" 。

```
 **示例 2：** 

```

输入：paths = [["B","C"],["D","B"],["C","A"]]
输出："A"
解释：所有可能的线路是：
"D" -> "B" -> "C" -> "A". 
"B" -> "C" -> "A". 
"C" -> "A". 
"A". 
显然，旅行终点站是 "A" 。

```
 **示例 3：** 

```

输入：paths = [["A","Z"]]
输出："Z"

```
 

 **提示：** 
-  `1 <= paths.length <= 100` 
-  `paths[i].length == 2` 
-  `1 <= cityA<sub>i</sub>.length, cityB<sub>i</sub>.length <= 10` 
-  `cityA<sub>i </sub>!= cityB<sub>i</sub>` 
- 所有字符串均由大小写英文字母和空格字符组成。
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1437.是否所有 1 都至少相隔 k 个元素
[https://leetcode-cn.com/problems/check-if-all-1s-are-at-least-length-k-places-away](https://leetcode-cn.com/problems/check-if-all-1s-are-at-least-length-k-places-away) 
## 原题
给你一个由若干 `0` 和 `1` 组成的数组 `nums` 以及整数 `k` 。如果所有 `1` 都至少相隔 `k` 个元素，则返回 `True` ；否则，返回 `False` 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_1_1791.png" style="width: 214px;">** 

```
输入：nums = [1,0,0,0,1,0,0,1], k = 2
输出：true
解释：每个 1 都至少相隔 2 个元素。
```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/03/sample_2_1791.png" style="height: 86px; width: 160px;">** 

```
输入：nums = [1,0,0,1,0,1], k = 2
输出：false
解释：第二个 1 和第三个 1 之间只隔了 1 个元素。
```
 **示例 3：** 

```
输入：nums = [1,1,1,1,1], k = 0
输出：true

```
 **示例 4：** 

```
输入：nums = [0,1,0,1], k = 1
输出：true

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= k <= nums.length` 
-  `nums[i]` 的值为 `0` 或 `1` 
 
**标签**
`数组` 


## 
```python

```
>
# 1438.绝对差不超过限制的最长连续子数组
[https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit](https://leetcode-cn.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit) 
## 原题
给你一个整数数组 `nums` ，和一个表示限制的整数 `limit` ，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 `limit` *。* 

如果不存在满足条件的子数组，则返回 `0` 。

 

 **示例 1：** 

```
输入：nums = [8,2,4,7], limit = 4
输出：2 
解释：所有子数组如下：
[8] 最大绝对差 |8-8| = 0 <= 4.
[8,2] 最大绝对差 |8-2| = 6 > 4. 
[8,2,4] 最大绝对差 |8-2| = 6 > 4.
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.
[2] 最大绝对差 |2-2| = 0 <= 4.
[2,4] 最大绝对差 |2-4| = 2 <= 4.
[2,4,7] 最大绝对差 |2-7| = 5 > 4.
[4] 最大绝对差 |4-4| = 0 <= 4.
[4,7] 最大绝对差 |4-7| = 3 <= 4.
[7] 最大绝对差 |7-7| = 0 <= 4. 
因此，满足题意的最长子数组的长度为 2 。

```
 **示例 2：** 

```
输入：nums = [10,1,2,4,7,2], limit = 5
输出：4 
解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。

```
 **示例 3：** 

```
输入：nums = [4,2,2,2,4,4,2,2], limit = 0
输出：3

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^9` 
-  `0 <= limit <= 10^9` 
 
**标签**
`队列` `数组` `有序集合` `滑动窗口` `单调队列` `堆（优先队列）` 


## 
```python

```
>
# 1439.有序矩阵中的第 k 个最小数组和
[https://leetcode-cn.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows](https://leetcode-cn.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows) 
## 原题
给你一个 `m * n` 的矩阵 `mat` ，以及一个整数 `k` ，矩阵中的每一行都以非递减的顺序排列。

你可以从每一行中选出 1 个元素形成一个数组。返回所有可能数组中的第 k 个 **最小** 数组和。

 

 **示例 1：** 

```
输入：mat = [[1,3,11],[2,4,6]], k = 5
输出：7
解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,2], [1,4], [3,2], [3,4], [1,6]。其中第 5 个的和是 7 。  
```
 **示例 2：** 

```
输入：mat = [[1,3,11],[2,4,6]], k = 9
输出：17

```
 **示例 3：** 

```
输入：mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
输出：9
解释：从每一行中选出一个元素，前 k 个和最小的数组分别是：
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]。其中第 7 个的和是 9 。 

```
 **示例 4：** 

```
输入：mat = [[1,1,10],[2,2,9]], k = 7
输出：12

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat.length[i]` 
-  `1 <= m, n <= 40` 
-  `1 <= k <= min(200, n ^ m)` 
-  `1 <= mat[i][j] <= 5000` 
-  `mat[i]` 是一个非递减数组
 
**标签**
`数组` `二分查找` `矩阵` `堆（优先队列）` 


## 
```python

```
>
# 1440.计算布尔表达式的值
[https://leetcode-cn.com/problems/evaluate-boolean-expression](https://leetcode-cn.com/problems/evaluate-boolean-expression) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1441.用栈操作构建数组
[https://leetcode-cn.com/problems/build-an-array-with-stack-operations](https://leetcode-cn.com/problems/build-an-array-with-stack-operations) 
## 原题
给你一个目标数组 `target` 和一个整数 `n` 。每次迭代，需要从  `list = {1,2,3..., n}` 中依序读取一个数字。

请使用下述操作来构建目标数组 `target` ：
-  **Push** ：从 `list` 中读取一个新元素， 并将其推入数组中。
-  **Pop** ：删除数组中的最后一个元素。
- 如果目标数组构建完成，就停止读取更多元素。
题目数据保证目标数组严格递增，并且只包含 `1` 到 `n` 之间的数字。

请返回构建目标数组所用的操作序列。

题目数据保证答案是唯一的。

 

 **示例 1：** 

```

输入：target = [1,3], n = 3
输出：["Push","Push","Pop","Push"]
解释： 
读取 1 并自动推入数组 -> [1]
读取 2 并自动推入数组，然后删除它 -> [1]
读取 3 并自动推入数组 -> [1,3]

```
 **示例 2：** 

```

输入：target = [1,2,3], n = 3
输出：["Push","Push","Push"]

```
 **示例 3：** 

```

输入：target = [1,2], n = 4
输出：["Push","Push"]
解释：只需要读取前 2 个数字就可以停止。

```
 **示例 4：** 

```

输入：target = [2,3,4], n = 4
输出：["Push","Pop","Push","Push","Push"]

```
 

 **提示：** 
-  `1 <= target.length <= 100` 
-  `1 <= target[i] <= 100` 
-  `1 <= n <= 100` 
-  `target` 是严格递增的
 
**标签**
`栈` `数组` `模拟` 


## 
```python

```
>
# 1442.形成两个异或相等数组的三元组数目
[https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor) 
## 原题
给你一个整数数组 `arr` 。

现需要从数组中取三个下标 `i` 、 `j` 和 `k` ，其中 `(0 <= i < j <= k < arr.length)` 。

 `a` 和 `b` 定义如下：
-  `a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]` 
-  `b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]` 
注意： **^** 表示 **按位异或** 操作。

请返回能够令 `a == b` 成立的三元组 ( `i` , `j` , `k` ) 的数目。

 

 **示例 1：** 

```
输入：arr = [2,3,1,6,7]
输出：4
解释：满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)

```
 **示例 2：** 

```
输入：arr = [1,1,1,1,1]
输出：10

```
 **示例 3：** 

```
输入：arr = [2,3]
输出：0

```
 **示例 4：** 

```
输入：arr = [1,3,5,7,9]
输出：3

```
 **示例 5：** 

```
输入：arr = [7,11,12,9,5,2,7,17,22]
输出：8

```
 

 **提示：** 
-  `1 <= arr.length <= 300` 
-  `1 <= arr[i] <= 10^8` 
 
**标签**
`位运算` `数组` `哈希表` `数学` `前缀和` 


## 
```python

```
>
# 1443.收集树上所有苹果的最少时间
[https://leetcode-cn.com/problems/minimum-time-to-collect-all-apples-in-a-tree](https://leetcode-cn.com/problems/minimum-time-to-collect-all-apples-in-a-tree) 
## 原题
给你一棵有 `n` 个节点的无向树，节点编号为 `0` 到 `n-1` ，它们中有一些节点有苹果。通过树上的一条边，需要花费 1 秒钟。你从 **节点 0** 出发，请你返回最少需要多少秒，可以收集到所有苹果，并回到节点 0 。

无向树的边由 `edges` 给出，其中 `edges[i] = [from<sub>i</sub>, to<sub>i</sub>]` ，表示有一条边连接 `from` 和 `to<sub>i</sub>` 。除此以外，还有一个布尔数组 `hasApple` ，其中 `hasApple[i] = true` 代表节点 `i` 有一个苹果，否则，节点 `i` 没有苹果。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/10/min_time_collect_apple_1.png" style="height: 212px; width: 300px;">** 

```
输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
输出：8 
解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/10/min_time_collect_apple_2.png" style="height: 212px; width: 300px;">** 

```
输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
输出：6
解释：上图展示了给定的树，其中红色节点表示有苹果。一个能收集到所有苹果的最优方案由绿色箭头表示。

```
 **示例 3：** 

```
输入：n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
输出：0

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `edges.length == n-1` 
-  `edges[i].length == 2` 
-  `0 <= from<sub>i</sub>, to<sub>i</sub> <= n-1` 
-  `from<sub>i</sub> < to<sub>i</sub>` 
-  `hasApple.length == n` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `哈希表` 


## 
```python

```
>
# 1444.切披萨的方案数
[https://leetcode-cn.com/problems/number-of-ways-of-cutting-a-pizza](https://leetcode-cn.com/problems/number-of-ways-of-cutting-a-pizza) 
## 原题
给你一个 `rows x cols` 大小的矩形披萨和一个整数 `k` ，矩形包含两种字符： `';A';` （表示苹果）和 `';.';` （表示空白格子）。你需要切披萨 `k-1` 次，得到 `k` 块披萨并送给别人。

切披萨的每一刀，先要选择是向垂直还是水平方向切，再在矩形的边界上选一个切的位置，将披萨一分为二。如果垂直地切披萨，那么需要把左边的部分送给一个人，如果水平地切，那么需要把上面的部分送给一个人。在切完最后一刀后，需要把剩下来的一块送给最后一个人。

请你返回确保每一块披萨包含 **至少** 一个苹果的切披萨方案数。由于答案可能是个很大的数字，请你返回它对 10^9 + 7 取余的结果。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/10/ways_to_cut_apple_1.png" style="height: 378px; width: 500px;">** 

```
输入：pizza = ["A..","AAA","..."], k = 3
输出：3 
解释：上图展示了三种切披萨的方案。注意每一块披萨都至少包含一个苹果。

```
 **示例 2：** 

```
输入：pizza = ["A..","AA.","..."], k = 3
输出：1

```
 **示例 3：** 

```
输入：pizza = ["A..","A..","..."], k = 1
输出：1

```
 

 **提示：** 
-  `1 <= rows, cols <= 50` 
-  `rows == pizza.length` 
-  `cols == pizza[i].length` 
-  `1 <= k <= 10` 
-  `pizza` 只包含字符 `';A';` 和 `';.';` 。
 
**标签**
`记忆化搜索` `数组` `动态规划` `矩阵` 


## 
```python

```
>
# 1445.苹果和桔子
[https://leetcode-cn.com/problems/apples-oranges](https://leetcode-cn.com/problems/apples-oranges) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1446.连续字符
[https://leetcode-cn.com/problems/consecutive-characters](https://leetcode-cn.com/problems/consecutive-characters) 
## 原题
给你一个字符串 `s` ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

请你返回字符串的能量。

 

 **示例 1：** 

```
输入：s = "leetcode"
输出：2
解释：子字符串 "ee" 长度为 2 ，只包含字符 ';e'; 。

```
 **示例 2：** 

```
输入：s = "abbcccddddeeeeedcba"
输出：5
解释：子字符串 "eeeee" 长度为 5 ，只包含字符 ';e'; 。

```
 **示例 3：** 

```
输入：s = "triplepillooooow"
输出：5

```
 **示例 4：** 

```
输入：s = "hooraaaaaaaaaaay"
输出：11

```
 **示例 5：** 

```
输入：s = "tourist"
输出：1

```
 

 **提示：** 
-  `1 <= s.length <= 500` 
-  `s` 只包含小写英文字母。
 
**标签**
`字符串` 


## 
```python

```
>
# 1447.最简分数
[https://leetcode-cn.com/problems/simplified-fractions](https://leetcode-cn.com/problems/simplified-fractions) 
## 原题
给你一个整数 `n` ，请你返回所有 0 到 1 之间（不包括 0 和 1）满足分母小于等于 `n` 的 **最简** 分数 。分数可以以 **任意** 顺序返回。

 

 **示例 1：** 

```
输入：n = 2
输出：["1/2"]
解释："1/2" 是唯一一个分母小于等于 2 的最简分数。
```
 **示例 2：** 

```
输入：n = 3
输出：["1/2","1/3","2/3"]

```
 **示例 3：** 

```
输入：n = 4
输出：["1/2","1/3","1/4","2/3","3/4"]
解释："2/4" 不是最简分数，因为它可以化简为 "1/2" 。
```
 **示例 4：** 

```
输入：n = 1
输出：[]

```
 

 **提示：** 
-  `1 <= n <= 100` 
 
**标签**
`数学` `字符串` `数论` 


## 
```python

```
>
# 1448.统计二叉树中好节点的数目
[https://leetcode-cn.com/problems/count-good-nodes-in-binary-tree](https://leetcode-cn.com/problems/count-good-nodes-in-binary-tree) 
## 原题
给你一棵根为 `root` 的二叉树，请你返回二叉树中好节点的数目。

「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/16/test_sample_1.png" style="height: 156px; width: 263px;">** 

```
输入：root = [3,1,4,3,null,1,5]
输出：4
解释：图中蓝色节点为好节点。
根节点 (3) 永远是个好节点。
节点 4 -> (3,4) 是路径中的最大值。
节点 5 -> (3,4,5) 是路径中的最大值。
节点 3 -> (3,1,3) 是路径中的最大值。
```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/16/test_sample_2.png" style="height: 161px; width: 157px;">** 

```
输入：root = [3,3,null,4,2]
输出：3
解释：节点 2 -> (3, 3, 2) 不是好节点，因为 "3" 比它大。
```
 **示例 3：** 

```
输入：root = [1]
输出：1
解释：根节点是好节点。
```
 

 **提示：** 
- 二叉树中节点数目范围是 `[1, 10^5]` 。
- 每个节点权值的范围是 `[-10^4, 10^4]` 。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 1449.数位成本和为目标值的最大数字
[https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target](https://leetcode-cn.com/problems/form-largest-integer-with-digits-that-add-up-to-target) 
## 原题
给你一个整数数组  `cost`  和一个整数  `target`  。请你返回满足如下规则可以得到的  **最大**  整数：
- 给当前结果添加一个数位（ `i + 1` ）的成本为  `cost[i]`  （ `cost`  数组下标从 0 开始）。
- 总成本必须恰好等于  `target`  。
- 添加的数位中没有数字 0 。
由于答案可能会很大，请你以字符串形式返回。

如果按照上述要求无法得到任何整数，请你返回 "0" 。

 

 **示例 1：** 

```

输入：cost = [4,3,2,5,6,7,2,5,5], target = 9
输出："7772"
解释：添加数位 '7' 的成本为 2 ，添加数位 '2' 的成本为 3 。所以 "7772" 的代价为 2*3+ 3*1 = 9 。 "977" 也是满足要求的数字，但 "7772" 是较大的数字。
 数字     成本
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5

```
 **示例 2：** 

```

输入：cost = [7,6,5,5,5,6,8,7,8], target = 12
输出："85"
解释：添加数位 '8' 的成本是 7 ，添加数位 '5' 的成本是 5 。"85" 的成本为 7 + 5 = 12 。

```
 **示例 3：** 

```

输入：cost = [2,4,6,2,4,6,4,4,4], target = 5
输出："0"
解释：总成本是 target 的条件下，无法生成任何整数。

```
 **示例 4：** 

```

输入：cost = [6,10,15,40,40,40,40,40,40], target = 47
输出："32211"

```
 

 **提示：** 
-  `cost.length == 9` 
-  `1 <= cost[i] <= 5000` 
-  `1 <= target <= 5000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1450.在既定时间做作业的学生人数
[https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time](https://leetcode-cn.com/problems/number-of-students-doing-homework-at-a-given-time) 
## 原题
给你两个整数数组 `startTime` （开始时间）和 `endTime` （结束时间），并指定一个整数 `queryTime` 作为查询时间。

已知，第 `i` 名学生在 `startTime[i]` 时开始写作业并于 `endTime[i]` 时完成作业。

请返回在查询时间 `queryTime` 时正在做作业的学生人数。形式上，返回能够使 `queryTime` 处于区间 `[startTime[i], endTime[i]]` （含）的学生人数。

 

 **示例 1：** 

```
输入：startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
输出：1
解释：一共有 3 名学生。
第一名学生在时间 1 开始写作业，并于时间 3 完成作业，在时间 4 没有处于做作业的状态。
第二名学生在时间 2 开始写作业，并于时间 2 完成作业，在时间 4 没有处于做作业的状态。
第三名学生在时间 3 开始写作业，预计于时间 7 完成作业，这是是唯一一名在时间 4 时正在做作业的学生。

```
 **示例 2：** 

```
输入：startTime = [4], endTime = [4], queryTime = 4
输出：1
解释：在查询时间只有一名学生在做作业。

```
 **示例 3：** 

```
输入：startTime = [4], endTime = [4], queryTime = 5
输出：0

```
 **示例 4：** 

```
输入：startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7
输出：0

```
 **示例 5：** 

```
输入：startTime = [9,8,7,6,5,4,3,2,1], endTime = [10,10,10,10,10,10,10,10,10], queryTime = 5
输出：5

```
 

 **提示：** 
-  `startTime.length == endTime.length` 
-  `1 <= startTime.length <= 100` 
-  `1 <= startTime[i] <= endTime[i] <= 1000` 
-  `1 <= queryTime <= 1000` 
 
**标签**
`数组` 


## 
```python

```
>
# 1451.重新排列句子中的单词
[https://leetcode-cn.com/problems/rearrange-words-in-a-sentence](https://leetcode-cn.com/problems/rearrange-words-in-a-sentence) 
## 原题
「句子」是一个用空格分隔单词的字符串。给你一个满足下述格式的句子 `text` :
- 句子的首字母大写
-  `text` 中的每个单词都用单个空格分隔。
请你重新排列 `text` 中的单词，使所有单词按其长度的升序排列。如果两个单词的长度相同，则保留其在原句子中的相对顺序。

请同样按上述格式返回新的句子。

 

 **示例 1：** 

```
输入：text = "Leetcode is cool"
输出："Is cool leetcode"
解释：句子中共有 3 个单词，长度为 8 的 "Leetcode" ，长度为 2 的 "is" 以及长度为 4 的 "cool" 。
输出需要按单词的长度升序排列，新句子中的第一个单词首字母需要大写。

```
 **示例 2：** 

```
输入：text = "Keep calm and code on"
输出："On and keep calm code"
解释：输出的排序情况如下：
"On" 2 个字母。
"and" 3 个字母。
"keep" 4 个字母，因为存在长度相同的其他单词，所以它们之间需要保留在原句子中的相对顺序。
"calm" 4 个字母。
"code" 4 个字母。

```
 **示例 3：** 

```
输入：text = "To be or not to be"
输出："To be or to be not"

```
 

 **提示：** 
-  `text` 以大写字母开头，然后包含若干小写字母以及单词间的单个空格。
-  `1 <= text.length <= 10^5` 
 
**标签**
`字符串` `排序` 


## 
```python

```
>
# 1452.收藏清单
[https://leetcode-cn.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list](https://leetcode-cn.com/problems/people-whose-list-of-favorite-companies-is-not-a-subset-of-another-list) 
## 原题
给你一个数组 `favoriteCompanies` ，其中 `favoriteCompanies[i]` 是第 `i` 名用户收藏的公司清单（ **下标从 0 开始** ）。

请找出不是其他任何人收藏的公司清单的子集的收藏清单，并返回该清单下标 *。* 下标需要按升序排列 *。* 

 

 **示例 1：** 

```
输入：favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
输出：[0,1,4] 
解释：
favoriteCompanies[2]=["google","facebook"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集。
favoriteCompanies[3]=["google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 和 favoriteCompanies[1]=["google","microsoft"] 的子集。
其余的收藏清单均不是其他任何人收藏的公司清单的子集，因此，答案为 [0,1,4] 。

```
 **示例 2：** 

```
输入：favoriteCompanies = [["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]
输出：[0,1] 
解释：favoriteCompanies[2]=["facebook","google"] 是 favoriteCompanies[0]=["leetcode","google","facebook"] 的子集，因此，答案为 [0,1] 。

```
 **示例 3：** 

```
输入：favoriteCompanies = [["leetcode"],["google"],["facebook"],["amazon"]]
输出：[0,1,2,3]

```
 

 **提示：** 
-  `1 <= favoriteCompanies.length <= 100` 
-  `1 <= favoriteCompanies[i].length <= 500` 
-  `1 <= favoriteCompanies[i][j].length <= 20` 
-  `favoriteCompanies[i]` 中的所有字符串 **各不相同** 。
- 用户收藏的公司清单也 **各不相同** ，也就是说，即便我们按字母顺序排序每个清单， `favoriteCompanies[i] != favoriteCompanies[j]` 仍然成立。
- 所有字符串仅包含小写英文字母。
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 1453.圆形靶内的最大飞镖数量
[https://leetcode-cn.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard](https://leetcode-cn.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard) 
## 原题
墙壁上挂着一个圆形的飞镖靶。现在请你蒙着眼睛向靶上投掷飞镖。

投掷到墙上的飞镖用二维平面上的点坐标数组表示。飞镖靶的半径为 `r` 。

请返回能够落在 **任意** 半径为 `r` 的圆形靶内或靶上的最大飞镖数。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/16/sample_1_1806.png" style="height: 159px; width: 186px;">

```
输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 2
输出：4
解释：如果圆形的飞镖靶的圆心为 (0,0) ，半径为 2 ，所有的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 4 。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/16/sample_2_1806.png" style="height: 183px; width: 224px;">** 

```
输入：points = [[-3,0],[3,0],[2,6],[5,4],[0,9],[7,8]], r = 5
输出：5
解释：如果圆形的飞镖靶的圆心为 (0,4) ，半径为 5 ，则除了 (7,8) 之外的飞镖都落在靶上，此时落在靶上的飞镖数最大，值为 5 。
```
 **示例 3：** 

```
输入：points = [[-2,0],[2,0],[0,2],[0,-2]], r = 1
输出：1

```
 **示例 4：** 

```
输入：points = [[1,2],[3,5],[1,-1],[2,3],[4,1],[1,3]], r = 2
输出：4

```
 

 **提示：** 
-  `1 <= points.length <= 100` 
-  `points[i].length == 2` 
-  `-10^4 <= points[i][0], points[i][1] <= 10^4` 
-  `1 <= r <= 5000` 
 
**标签**
`几何` `数组` `数学` 


## 
```python

```
>
# 1454.活跃用户
[https://leetcode-cn.com/problems/active-users](https://leetcode-cn.com/problems/active-users) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1455.检查单词是否为句中其他单词的前缀
[https://leetcode-cn.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence](https://leetcode-cn.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence) 
## 原题
给你一个字符串 `sentence` 作为句子并指定检索词为 `searchWord` ，其中句子由若干用 **单个空格** 分隔的单词组成。请你检查检索词 `searchWord` 是否为句子 `sentence` 中任意单词的前缀。

如果 `searchWord` 是某一个单词的前缀，则返回句子 `sentence` 中该单词所对应的下标（ **下标从 1 开始** ）。如果 `searchWord` 是多个单词的前缀，则返回匹配的第一个单词的下标（ **最小下标** ）。如果 `searchWord` 不是任何单词的前缀，则返回 `-1` **** 。

字符串 `s` 的 **前缀** 是 `s` 的任何前导连续子字符串。

 

 **示例 1：** 

```

输入：sentence = "i love eating burger", searchWord = "burg"
输出：4
解释："burg" 是 "burger" 的前缀，而 "burger" 是句子中第 4 个单词。
```
 **示例 2：** 

```

输入：sentence = "this problem is an easy problem", searchWord = "pro"
输出：2
解释："pro" 是 "problem" 的前缀，而 "problem" 是句子中第 2 个也是第 6 个单词，但是应该返回最小下标 2 。

```
 **示例 3：** 

```

输入：sentence = "i am tired", searchWord = "you"
输出：-1
解释："you" 不是句子中任何单词的前缀。
```
 

 **提示：** 
-  `1 <= sentence.length <= 100` 
-  `1 <= searchWord.length <= 10` 
-  `sentence` 由小写英文字母和空格组成。
-  `searchWord` 由小写英文字母组成。
 
**标签**
`字符串` `字符串匹配` 


## 
```python

```
>
# 1456.定长子串中元音的最大数目
[https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length](https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length) 
## 原题
给你字符串 `s` 和整数 `k` 。

请返回字符串 `s` 中长度为 `k` 的单个子字符串中可能包含的最大元音字母数。

英文中的 **元音字母** 为（ `a` , `e` , `i` , `o` , `u` ）。

 

 **示例 1：** 

```
输入：s = "abciiidef", k = 3
输出：3
解释：子字符串 "iii" 包含 3 个元音字母。

```
 **示例 2：** 

```
输入：s = "aeiou", k = 2
输出：2
解释：任意长度为 2 的子字符串都包含 2 个元音字母。

```
 **示例 3：** 

```
输入：s = "leetcode", k = 3
输出：2
解释："lee"、"eet" 和 "ode" 都包含 2 个元音字母。

```
 **示例 4：** 

```
输入：s = "rhythms", k = 4
输出：0
解释：字符串 s 中不含任何元音字母。

```
 **示例 5：** 

```
输入：s = "tryhard", k = 4
输出：1

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s` 由小写英文字母组成
-  `1 <= k <= s.length` 
 
**标签**
`字符串` `滑动窗口` 


## 
```python

```
>
# 1457.二叉树中的伪回文路径
[https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree](https://leetcode-cn.com/problems/pseudo-palindromic-paths-in-a-binary-tree) 
## 原题
给你一棵二叉树，每个节点的值为 1 到 9 。我们称二叉树中的一条路径是 「 **伪回文** 」的，当它满足：路径经过的所有节点值的排列中，存在一个回文序列。

请你返回从根到叶子节点的所有路径中 **伪回文** 路径的数目。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/23/palindromic_paths_1.png" style="height: 201px; width: 300px;" />

```

输入：root = [2,3,1,3,1,null,1]
输出：2 
解释：上图为给定的二叉树。总共有 3 条从根到叶子的路径：红色路径 [2,3,3] ，绿色路径 [2,1,1] 和路径 [2,3,1] 。
     在这些路径中，只有红色和绿色的路径是伪回文路径，因为红色路径 [2,3,3] 存在回文排列 [3,2,3] ，绿色路径 [2,1,1] 存在回文排列 [1,2,1] 。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/23/palindromic_paths_2.png" style="height: 314px; width: 300px;" />** 

```

输入：root = [2,1,1,1,3,null,null,null,null,null,1]
输出：1 
解释：上图为给定二叉树。总共有 3 条从根到叶子的路径：绿色路径 [2,1,1] ，路径 [2,1,3,1] 和路径 [2,1] 。
     这些路径中只有绿色路径是伪回文路径，因为 [2,1,1] 存在回文排列 [1,2,1] 。

```
 **示例 3：** 

```

输入：root = [9]
输出：1

```
 

 **提示：** 
- 给定二叉树的节点数目在范围 `[1, 10^5]` 内
-  `1 <= Node.val <= 9` 
 
**标签**
`位运算` `树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 1458.两个子序列的最大点积
[https://leetcode-cn.com/problems/max-dot-product-of-two-subsequences](https://leetcode-cn.com/problems/max-dot-product-of-two-subsequences) 
## 原题
给你两个数组 `nums1` 和 `nums2` 。

请你返回 `nums1` 和 `nums2` 中两个长度相同的 **非空** 子序列的最大点积。

数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说， `[2,3,5]` 是 `[1,2,3,4,5]` 的一个子序列而 `[1,5,3]` 不是。

 

 **示例 1：** 

```

输入：nums1 = [2,1,-2,5], nums2 = [3,0,-6]
输出：18
解释：从 nums1 中得到子序列 [2,-2] ，从 nums2 中得到子序列 [3,-6] 。
它们的点积为 (2*3 + (-2)*(-6)) = 18 。
```
 **示例 2：** 

```

输入：nums1 = [3,-2], nums2 = [2,-6,7]
输出：21
解释：从 nums1 中得到子序列 [3] ，从 nums2 中得到子序列 [7] 。
它们的点积为 (3*7) = 21 。
```
 **示例 3：** 

```

输入：nums1 = [-1,-1], nums2 = [1,1]
输出：-1
解释：从 nums1 中得到子序列 [-1] ，从 nums2 中得到子序列 [1] 。
它们的点积为 -1 。
```
 

 **提示：** 
-  `1 <= nums1.length, nums2.length <= 500` 
-  `-1000 <= nums1[i], nums2[i] <= 100` 
 

 **点积：** 

```

定义 a = [a1, a2,&hellip;, an] 和 b = [b1, b2,&hellip;, bn] 的点积为：

<img alt="\mathbf{a}\cdot \mathbf{b} = \sum_{i=1}^n a_ib_i = a_1b_1 + a_2b_2 + \cdots + a_nb_n " class="tex" src="http://upload.wikimedia.org/math/c/3/2/c329bf86e747d74f55ed2e17c36fd83f.png" />

这里的 &Sigma; 指示总和符号。

```
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1459.矩形面积
[https://leetcode-cn.com/problems/rectangles-area](https://leetcode-cn.com/problems/rectangles-area) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1460.通过翻转子数组使两个数组相等
[https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays](https://leetcode-cn.com/problems/make-two-arrays-equal-by-reversing-sub-arrays) 
## 原题
给你两个长度相同的整数数组 `target` 和 `arr` 。每一步中，你可以选择 `arr` 的任意 **非空子数组** 并将它翻转。你可以执行此过程任意次。

 *如果你能让 `arr` 变得与 `target` 相同，返回 True；否则，返回 False 。* 

 

 **示例 1：** 

```

输入：target = [1,2,3,4], arr = [2,4,1,3]
输出：true
解释：你可以按照如下步骤使 arr 变成 target：
1- 翻转子数组 [2,4,1] ，arr 变成 [1,4,2,3]
2- 翻转子数组 [4,2] ，arr 变成 [1,2,4,3]
3- 翻转子数组 [4,3] ，arr 变成 [1,2,3,4]
上述方法并不是唯一的，还存在多种将 arr 变成 target 的方法。

```
 **示例 2：** 

```

输入：target = [7], arr = [7]
输出：true
解释：arr 不需要做任何翻转已经与 target 相等。

```
 **示例 3：** 

```

输入：target = [3,7,9], arr = [3,7,11]
输出：false
解释：arr 没有数字 9 ，所以无论如何也无法变成 target 。

```
 

 **提示：** 
-  `target.length == arr.length` 
-  `1 <= target.length <= 1000` 
-  `1 <= target[i] <= 1000` 
-  `1 <= arr[i] <= 1000` 
 
**标签**
`数组` `哈希表` `排序` 


## 
```python

```
>
# 1461.检查一个字符串是否包含所有长度为 K 的二进制子串
[https://leetcode-cn.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k](https://leetcode-cn.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k) 
## 原题
给你一个二进制字符串 `s` 和一个整数 `k` 。如果所有长度为 `k` 的二进制字符串都是 `s` 的子串，请返回 `true` ，否则请返回 `false` 。

 

 **示例 1：** 

```

输入：s = "00110110", k = 2
输出：true
解释：长度为 2 的二进制串包括 "00"，"01"，"10" 和 "11"。它们分别是 s 中下标为 0，1，3，2 开始的长度为 2 的子串。

```
 **示例 2：** 

```

输入：s = "0110", k = 1
输出：true
解释：长度为 1 的二进制串包括 "0" 和 "1"，显然它们都是 s 的子串。

```
 **示例 3：** 

```

输入：s = "0110", k = 2
输出：false
解释：长度为 2 的二进制串 "00" 没有出现在 s 中。

```
 

 **提示：** 
-  `1 <= s.length <= 5 * 10^5` 
-  `s[i]` 不是 `'0'` 就是 `'1'` 
-  `1 <= k <= 20` 
 
**标签**
`位运算` `哈希表` `字符串` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 1462.课程表 IV
[https://leetcode-cn.com/problems/course-schedule-iv](https://leetcode-cn.com/problems/course-schedule-iv) 
## 原题
你总共需要上 `n` 门课，课程编号依次为 `0` 到 `n-1` 。

有的课会有直接的先修课程，比如如果想上课程 0 ，你必须先上课程 1 ，那么会以 `[1,0]` 数对的形式给出先修课程数对。

给你课程总数 `n` 和一个直接先修课程数对列表 `prerequisite` 和一个查询对列表 `queries` 。

对于每个查询对 `queries[i]` ，请判断 `queries[i][0]` 是否是 `queries[i][1]` 的先修课程。

请返回一个布尔值列表，列表中每个元素依次分别对应 `queries` 每个查询对的判断结果。

 **注意：** 如果课程 **a** 是课程 **b** 的先修课程且课程 **b** 是课程 **c** 的先修课程，那么课程 **a** 也是课程 **c** 的先修课程。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/graph.png" style="height: 300px; width: 300px;">

```
输入：n = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
输出：[false,true]
解释：课程 0 不是课程 1 的先修课程，但课程 1 是课程 0 的先修课程。

```
 **示例 2：** 

```
输入：n = 2, prerequisites = [], queries = [[1,0],[0,1]]
输出：[false,false]
解释：没有先修课程对，所以每门课程之间是独立的。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/graph-1.png" style="height: 300px; width: 300px;">

```
输入：n = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
输出：[true,true]

```
 **示例 4：** 

```
输入：n = 3, prerequisites = [[1,0],[2,0]], queries = [[0,1],[2,0]]
输出：[false,true]

```
 **示例 5：** 

```
输入：n = 5, prerequisites = [[0,1],[1,2],[2,3],[3,4]], queries = [[0,4],[4,0],[1,3],[3,0]]
输出：[true,false,true,false]

```
 

 **提示：** 
-  `2 <= n <= 100` 
-  `0 <= prerequisite.length <= (n * (n - 1) / 2)` 
-  `0 <= prerequisite[i][0], prerequisite[i][1] < n` 
-  `prerequisite[i][0] != prerequisite[i][1]` 
- 先修课程图中没有环。
- 先修课程图中没有重复的边。
-  `1 <= queries.length <= 10^4` 
-  `queries[i][0] != queries[i][1]` 
 
**标签**
`深度优先搜索` `广度优先搜索` `图` `拓扑排序` 


## 
```python

```
>
# 1463.摘樱桃 II
[https://leetcode-cn.com/problems/cherry-pickup-ii](https://leetcode-cn.com/problems/cherry-pickup-ii) 
## 原题
给你一个 `rows x cols` 的矩阵 `grid` 来表示一块樱桃地。 `grid` 中每个格子的数字表示你能获得的樱桃数目。

你有两个机器人帮你收集樱桃，机器人 1 从左上角格子 `(0,0)` 出发，机器人 2 从右上角格子 `(0, cols-1)` 出发。

请你按照如下规则，返回两个机器人能收集的最多樱桃数目：
- 从格子 `(i,j)` 出发，机器人可以移动到格子 `(i+1, j-1)` ， `(i+1, j)` 或者 `(i+1, j+1)` 。
- 当一个机器人经过某个格子时，它会把该格子内所有的樱桃都摘走，然后这个位置会变成空格子，即没有樱桃的格子。
- 当两个机器人同时到达同一个格子时，它们中只有一个可以摘到樱桃。
- 两个机器人在任意时刻都不能移动到 `grid` 外面。
- 两个机器人最后都要到达 `grid` 最底下一行。
 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/sample_1_1802.png" style="height: 182px; width: 139px;">** 

```
输入：grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
输出：24
解释：机器人 1 和机器人 2 的路径在上图中分别用绿色和蓝色表示。
机器人 1 摘的樱桃数目为 (3 + 2 + 5 + 2) = 12 。
机器人 2 摘的樱桃数目为 (1 + 5 + 5 + 1) = 12 。
樱桃总数为： 12 + 12 = 24 。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/sample_2_1802.png" style="height: 257px; width: 284px;">** 

```
输入：grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
输出：28
解释：机器人 1 和机器人 2 的路径在上图中分别用绿色和蓝色表示。
机器人 1 摘的樱桃数目为 (1 + 9 + 5 + 2) = 17 。
机器人 2 摘的樱桃数目为 (1 + 3 + 4 + 3) = 11 。
樱桃总数为： 17 + 11 = 28 。

```
 **示例 3：** 

```
输入：grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
输出：22

```
 **示例 4：** 

```
输入：grid = [[1,1],[1,1]]
输出：4

```
 

 **提示：** 
-  `rows == grid.length` 
-  `cols == grid[i].length` 
-  `2 <= rows, cols <= 70` 
-  `0 <= grid[i][j] <= 100` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 1464.数组中两元素的最大乘积
[https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array](https://leetcode-cn.com/problems/maximum-product-of-two-elements-in-an-array) 
## 原题
给你一个整数数组 `nums` ，请你选择数组的两个不同下标 `i` 和 `j` *，* 使 `(nums[i]-1)*(nums[j]-1)` 取得最大值。

请你计算并返回该式的最大值。

 

 **示例 1：** 

```
输入：nums = [3,4,5,2]
输出：12 
解释：如果选择下标 i=1 和 j=2（下标从 0 开始），则可以获得最大值，(nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12 。 

```
 **示例 2：** 

```
输入：nums = [1,5,4,5]
输出：16
解释：选择下标 i=1 和 j=3（下标从 0 开始），则可以获得最大值 (5-1)*(5-1) = 16 。

```
 **示例 3：** 

```
输入：nums = [3,7]
输出：12

```
 

 **提示：** 
-  `2 <= nums.length <= 500` 
-  `1 <= nums[i] <= 10^3` 
 
**标签**
`数组` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1465.切割后面积最大的蛋糕
[https://leetcode-cn.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts](https://leetcode-cn.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts) 
## 原题
矩形蛋糕的高度为 `h` 且宽度为 `w` ，给你两个整数数组 `horizontalCuts` 和 `verticalCuts` ，其中 `horizontalCuts[i]` 是从矩形蛋糕顶部到第 `i` 个水平切口的距离，类似地， `verticalCuts[j]` 是从矩形蛋糕的左侧到第 `j` 个竖直切口的距离。

请你按数组 *`horizontalCuts`* 和 *`verticalCuts`* 中提供的水平和竖直位置切割后，请你找出 **面积最大** 的那份蛋糕，并返回其 **面积** 。由于答案可能是一个很大的数字，因此需要将结果对 `10^9 + 7` 取余后返回。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_2.png" style="height: 320px; width: 300px;">

```
输入：h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
输出：4 
解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色的那份蛋糕面积最大。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/leetcode_max_area_3.png" style="height: 320px; width: 300px;">** 

```
输入：h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
输出：6
解释：上图所示的矩阵蛋糕中，红色线表示水平和竖直方向上的切口。切割蛋糕后，绿色和黄色的两份蛋糕面积最大。
```
 **示例 3：** 

```
输入：h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
输出：9

```
 

 **提示：** 
-  `2 <= h, w <= 10^9` 
-  `1 <= horizontalCuts.length < min(h, 10^5)` 
-  `1 <= verticalCuts.length < min(w, 10^5)` 
-  `1 <= horizontalCuts[i] < h` 
-  `1 <= verticalCuts[i] < w` 
- 题目数据保证 `horizontalCuts` 中的所有元素各不相同
- 题目数据保证 `verticalCuts` 中的所有元素各不相同
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1466.重新规划路线
[https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero](https://leetcode-cn.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero) 
## 原题
 `n` 座城市，从 `0` 到 `n-1` 编号，其间共有 `n-1` 条路线。因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。

路线用 `connections` 表示，其中 `connections[i] = [a, b]` 表示从城市 `a` 到 `b` 的一条有向路线。

今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。

请你帮助重新规划路线方向，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。

题目数据 **保证** 每个城市在重新规划路线方向后都能到达城市 0 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/sample_1_1819.png" style="height: 150px; width: 240px;">** 

```
输入：n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
输出：3
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/05/30/sample_2_1819.png" style="height: 60px; width: 380px;">** 

```
输入：n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
输出：2
解释：更改以红色显示的路线的方向，使每个城市都可以到达城市 0 。
```
 **示例 3：** 

```
输入：n = 3, connections = [[1,0],[2,0]]
输出：0

```
 

 **提示：** 
-  `2 <= n <= 5 * 10^4` 
-  `connections.length == n-1` 
-  `connections[i].length == 2` 
-  `0 <= connections[i][0], connections[i][1] <= n-1` 
-  `connections[i][0] != connections[i][1]` 
 
**标签**
`深度优先搜索` `广度优先搜索` `图` 


## 
```python

```
>
# 1467.两个盒子中球的颜色数相同的概率
[https://leetcode-cn.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls](https://leetcode-cn.com/problems/probability-of-a-two-boxes-having-the-same-number-of-distinct-balls) 
## 原题
桌面上有 `2n` 个颜色不完全相同的球，球上的颜色共有 `k` 种。给你一个大小为 `k` 的整数数组 `balls` ，其中 `balls[i]` 是颜色为 `i` 的球的数量。

所有的球都已经 **随机打乱顺序** ，前 `n` 个球放入第一个盒子，后 `n` 个球放入另一个盒子（请认真阅读示例 2 的解释部分）。

 **注意：** 这两个盒子是不同的。例如，两个球颜色分别为 `a` 和 `b` ，盒子分别为 `[]` 和 `()` ，那么 `[a] (b)` 和 `[b] (a)` 这两种分配方式是不同的（请认真阅读示例 1 的解释部分）。

请计算「两个盒子中球的颜色数相同」的情况的概率。

 

 **示例 1：** 

```
输入：balls = [1,1]
输出：1.00000
解释：球平均分配的方式只有两种：
- 颜色为 1 的球放入第一个盒子，颜色为 2 的球放入第二个盒子
- 颜色为 2 的球放入第一个盒子，颜色为 1 的球放入第二个盒子
这两种分配，两个盒子中球的颜色数都相同。所以概率为 2/2 = 1 。

```
 **示例 2：** 

```
输入：balls = [2,1,1]
输出：0.66667
解释：球的列表为 [1, 1, 2, 3]
随机打乱，得到 12 种等概率的不同打乱方案，每种方案概率为 1/12 ：
[1,1 / 2,3], [1,1 / 3,2], [1,2 / 1,3], [1,2 / 3,1], [1,3 / 1,2], [1,3 / 2,1], [2,1 / 1,3], [2,1 / 3,1], [2,3 / 1,1], [3,1 / 1,2], [3,1 / 2,1], [3,2 / 1,1]
然后，我们将前两个球放入第一个盒子，后两个球放入第二个盒子。
这 12 种可能的随机打乱方式中的 8 种满足「两个盒子中球的颜色数相同」。
概率 = 8/12 = 0.66667

```
 **示例 3：** 

```
输入：balls = [1,2,1,2]
输出：0.60000
解释：球的列表为 [1, 2, 2, 3, 4, 4]。要想显示所有 180 种随机打乱方案是很难的，但只检查「两个盒子中球的颜色数相同」的 108 种情况是比较容易的。
概率 = 108 / 180 = 0.6 。

```
 **示例 4：** 

```
输入：balls = [3,2,1]
输出：0.30000
解释：球的列表为 [1, 1, 1, 2, 2, 3]。要想显示所有 60 种随机打乱方案是很难的，但只检查「两个盒子中球的颜色数相同」的 18 种情况是比较容易的。
概率 = 18 / 60 = 0.3 。

```
 **示例 5：** 

```
输入：balls = [6,6,6,6,6,6]
输出：0.90327

```
 

 **提示：** 
-  `1 <= balls.length <= 8` 
-  `1 <= balls[i] <= 6` 
-  `sum(balls)` 是偶数
- 答案与真实值误差在 `10^-5` 以内，则被视为正确答案
 
**标签**
`数学` `动态规划` `回溯` `组合数学` `概率与统计` 


## 
```python

```
>
# 1468.计算税后工资
[https://leetcode-cn.com/problems/calculate-salaries](https://leetcode-cn.com/problems/calculate-salaries) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1469.寻找所有的独生节点
[https://leetcode-cn.com/problems/find-all-the-lonely-nodes](https://leetcode-cn.com/problems/find-all-the-lonely-nodes) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 1470.重新排列数组
[https://leetcode-cn.com/problems/shuffle-the-array](https://leetcode-cn.com/problems/shuffle-the-array) 
## 原题
给你一个数组 `nums` ，数组中有 `2n` 个元素，按 `[x<sub>1</sub>,x<sub>2</sub>,...,x<sub>n</sub>,y<sub>1</sub>,y<sub>2</sub>,...,y<sub>n</sub>]` 的格式排列。

请你将数组按 `[x<sub>1</sub>,y<sub>1</sub>,x<sub>2</sub>,y<sub>2</sub>,...,x<sub>n</sub>,y<sub>n</sub>]` 格式重新排列，返回重排后的数组。

 

 **示例 1：** 

```
输入：nums = [2,5,1,3,4,7], n = 3
输出：[2,3,5,4,1,7] 
解释：由于 x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 ，所以答案为 [2,3,5,4,1,7]

```
 **示例 2：** 

```
输入：nums = [1,2,3,4,4,3,2,1], n = 4
输出：[1,4,2,3,3,2,4,1]

```
 **示例 3：** 

```
输入：nums = [1,1,2,2], n = 2
输出：[1,2,1,2]

```
 

 **提示：** 
-  `1 <= n <= 500` 
-  `nums.length == 2n` 
-  `1 <= nums[i] <= 10^3` 
 
**标签**
`数组` 


## 
```python

```
>
# 1471.数组中的 k 个最强值
[https://leetcode-cn.com/problems/the-k-strongest-values-in-an-array](https://leetcode-cn.com/problems/the-k-strongest-values-in-an-array) 
## 原题
给你一个整数数组 `arr` 和一个整数 `k` 。

设 `m` 为数组的中位数，只要满足下述两个前提之一，就可以判定 `arr[i]` 的值比 `arr[j]` 的值更强：
-  `|arr[i] - m| > |arr[j] - m|` 
-  `|arr[i] - m| == |arr[j] - m|` ，且 `arr[i] > arr[j]` 
请返回由数组中最强的 `k` 个值组成的列表。答案可以以 **任意顺序** 返回。

 **中位数** 是一个有序整数列表中处于中间位置的值。形式上，如果列表的长度为 `n` ，那么中位数就是该有序列表（下标从 0 开始）中位于 `((n - 1) / 2)` 的元素。
- 例如 `arr = [6, -3, 7, 2, 11]` ， `n = 5` ：数组排序后得到 `arr = [-3, 2, 6, 7, 11]` ，数组的中间位置为 `m = ((5 - 1) / 2) = 2` ，中位数 `arr[m]` 的值为 `6` 。
- 例如 `arr = [-7, 22, 17,&thinsp;3]` ， `n = 4` ：数组排序后得到 `arr = [-7, 3, 17, 22]` ，数组的中间位置为 `m = ((4 - 1) / 2) = 1` ，中位数 `arr[m]` 的值为 `3` 。
 

 **示例 1：** 

```
输入：arr = [1,2,3,4,5], k = 2
输出：[5,1]
解释：中位数为 3，按从强到弱顺序排序后，数组变为 [5,1,4,2,3]。最强的两个元素是 [5, 1]。[1, 5] 也是正确答案。
注意，尽管 |5 - 3| == |1 - 3| ，但是 5 比 1 更强，因为 5 > 1 。

```
 **示例 2：** 

```
输入：arr = [1,1,3,5,5], k = 2
输出：[5,5]
解释：中位数为 3, 按从强到弱顺序排序后，数组变为 [5,5,1,1,3]。最强的两个元素是 [5, 5]。

```
 **示例 3：** 

```
输入：arr = [6,7,11,7,6,8], k = 5
输出：[11,8,6,6,7]
解释：中位数为 7, 按从强到弱顺序排序后，数组变为 [11,8,6,6,7,7]。
[11,8,6,6,7] 的任何排列都是正确答案。
```
 **示例 4：** 

```
输入：arr = [6,-3,7,2,11], k = 3
输出：[-3,11,2]

```
 **示例 5：** 

```
输入：arr = [-7,22,17,3], k = 2
输出：[22,17]

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `-10^5 <= arr[i] <= 10^5` 
-  `1 <= k <= arr.length` 
 
**标签**
`数组` `双指针` `排序` 


## 
```python

```
>
# 1472.设计浏览器历史记录
[https://leetcode-cn.com/problems/design-browser-history](https://leetcode-cn.com/problems/design-browser-history) 
## 原题
你有一个只支持单个标签页的 **浏览器** ，最开始你浏览的网页是 `homepage` ，你可以访问其他的网站 `url` ，也可以在浏览历史中后退 `steps` 步或前进 `steps` 步。

请你实现 `BrowserHistory` 类：
-  `BrowserHistory(string homepage)` ，用 `homepage` 初始化浏览器类。
-  `void visit(string url)` 从当前页跳转访问 `url` 对应的页面  。执行此操作会把浏览历史前进的记录全部删除。
-  `string back(int steps)` 在浏览历史中后退 `steps` 步。如果你只能在浏览历史中后退至多 `x` 步且 `steps > x` ，那么你只后退 `x` 步。请返回后退 **至多** `steps` 步以后的 `url` 。
-  `string forward(int steps)` 在浏览历史中前进 `steps` 步。如果你只能在浏览历史中前进至多 `x` 步且 `steps > x` ，那么你只前进 `x` 步。请返回前进 **至多** `steps` 步以后的 `url` 。
 

 **示例：** 

```
输入：
["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
[["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
输出：
[null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

解释：
BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
browserHistory.visit("google.com");       // 你原本在浏览 "leetcode.com" 。访问 "google.com"
browserHistory.visit("facebook.com");     // 你原本在浏览 "google.com" 。访问 "facebook.com"
browserHistory.visit("youtube.com");      // 你原本在浏览 "facebook.com" 。访问 "youtube.com"
browserHistory.back(1);                   // 你原本在浏览 "youtube.com" ，后退到 "facebook.com" 并返回 "facebook.com"
browserHistory.back(1);                   // 你原本在浏览 "facebook.com" ，后退到 "google.com" 并返回 "google.com"
browserHistory.forward(1);                // 你原本在浏览 "google.com" ，前进到 "facebook.com" 并返回 "facebook.com"
browserHistory.visit("linkedin.com");     // 你原本在浏览 "facebook.com" 。 访问 "linkedin.com"
browserHistory.forward(2);                // 你原本在浏览 "linkedin.com" ，你无法前进任何步数。
browserHistory.back(2);                   // 你原本在浏览 "linkedin.com" ，后退两步依次先到 "facebook.com" ，然后到 "google.com" ，并返回 "google.com"
browserHistory.back(7);                   // 你原本在浏览 "google.com"， 你只能后退一步到 "leetcode.com" ，并返回 "leetcode.com"

```
 

 **提示：** 
-  `1 <= homepage.length <= 20` 
-  `1 <= url.length <= 20` 
-  `1 <= steps <= 100` 
-  `homepage` 和 `url` 都只包含 ';.'; 或者小写英文字母。
- 最多调用 `5000` 次 `visit` ， `back` 和 `forward` 函数。
 
**标签**
`栈` `设计` `数组` `链表` `数据流` `双向链表` 


## 
```python

```
>
# 1473.粉刷房子 III
[https://leetcode-cn.com/problems/paint-house-iii](https://leetcode-cn.com/problems/paint-house-iii) 
## 原题
在一个小城市里，有  `m`  个房子排成一排，你需要给每个房子涂上 `n`  种颜色之一（颜色编号为 `1` 到 `n`  ）。有的房子去年夏天已经涂过颜色了，所以这些房子不可以被重新涂色。

我们将连续相同颜色尽可能多的房子称为一个街区。（比方说 `houses = [1,2,2,3,3,2,1,1]` ，它包含 5 个街区  `[{1}, {2,2}, {3,3}, {2}, {1,1}]` 。）

给你一个数组  `houses`  ，一个  `m * n`  的矩阵  `cost`  和一个整数  `target`  ，其中：
-  `houses[i]` ：是第  `i`  个房子的颜色， **0**  表示这个房子还没有被涂色。
-  `cost[i][j]` ：是将第  `i`  个房子涂成颜色  `j+1`  的花费。
请你返回房子涂色方案的最小总花费，使得每个房子都被涂色后，恰好组成  `target`  个街区。如果没有可用的涂色方案，请返回  **-1**  。

 

 **示例 1：** 

```

输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：9
解释：房子涂色方案为 [1,2,2,1,1]
此方案包含 target = 3 个街区，分别是 [{1}, {2,2}, {1,1}]。
涂色的总花费为 (1 + 1 + 1 + 1 + 5) = 9。

```
 **示例 2：** 

```

输入：houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
输出：11
解释：有的房子已经被涂色了，在此基础上涂色方案为 [2,2,1,2,2]
此方案包含 target = 3 个街区，分别是 [{2,2}, {1}, {2,2}]。
给第一个和最后一个房子涂色的花费为 (10 + 1) = 11。

```
 **示例 3：** 

```

输入：houses = [0,0,0,0,0], cost = [[1,10],[10,1],[1,10],[10,1],[1,10]], m = 5, n = 2, target = 5
输出：5

```
 **示例 4：** 

```

输入：houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
输出：-1
解释：房子已经被涂色并组成了 4 个街区，分别是 [{3},{1},{2},{3}] ，无法形成 target = 3 个街区。

```
 

 **提示：** 
-  `m == houses.length == cost.length` 
-  `n == cost[i].length` 
-  `1 <= m <= 100` 
-  `1 <= n <= 20` 
-  `1 <= target <= m` 
-  `0 <= houses[i] <= n` 
-  `1 <= cost[i][j] <= 10^4` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1474.删除链表 M 个节点之后的 N 个节点
[https://leetcode-cn.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list](https://leetcode-cn.com/problems/delete-n-nodes-after-m-nodes-of-a-linked-list) 
## 原题

 
**标签**
`链表` 


## 
```python

```
>
# 1475.商品折扣后的最终价格
[https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop](https://leetcode-cn.com/problems/final-prices-with-a-special-discount-in-a-shop) 
## 原题
给你一个数组 `prices` ，其中 `prices[i]` 是商店里第 `i` 件商品的价格。

商店里正在进行促销活动，如果你要买第 `i` 件商品，那么你可以得到与 `prices[j]` 相等的折扣，其中 `j` 是满足 `j > i` 且 `prices[j] <= prices[i]` 的 **最小下标** ，如果没有满足条件的 `j` ，你将没有任何折扣。

请你返回一个数组，数组中第 `i` 个元素是折扣后你购买商品 `i` 最终需要支付的价格。

 

 **示例 1：** 

```
输入：prices = [8,4,6,2,3]
输出：[4,2,4,2,3]
解释：
商品 0 的价格为 price[0]=8 ，你将得到 prices[1]=4 的折扣，所以最终价格为 8 - 4 = 4 。
商品 1 的价格为 price[1]=4 ，你将得到 prices[3]=2 的折扣，所以最终价格为 4 - 2 = 2 。
商品 2 的价格为 price[2]=6 ，你将得到 prices[3]=2 的折扣，所以最终价格为 6 - 2 = 4 。
商品 3 和 4 都没有折扣。

```
 **示例 2：** 

```
输入：prices = [1,2,3,4,5]
输出：[1,2,3,4,5]
解释：在这个例子中，所有商品都没有折扣。

```
 **示例 3：** 

```
输入：prices = [10,1,1,6]
输出：[9,0,1,6]

```
 

 **提示：** 
-  `1 <= prices.length <= 500` 
-  `1 <= prices[i] <= 10^3` 
 
**标签**
`栈` `数组` `单调栈` 


## 
```python

```
>
# 1476.子矩形查询
[https://leetcode-cn.com/problems/subrectangle-queries](https://leetcode-cn.com/problems/subrectangle-queries) 
## 原题
请你实现一个类 `SubrectangleQueries` ，它的构造函数的参数是一个 `rows x cols` 的矩形（这里用整数矩阵表示），并支持以下两种操作：

1. `updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)` 
- 用 `newValue` 更新以 `(row1,col1)` 为左上角且以 `(row2,col2)` 为右下角的子矩形。
2. `getValue(int row, int col)` 
- 返回矩形中坐标 `(row,col)` 的当前值。
 

 **示例 1：** 

```
输入：
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
输出：
[null,1,null,5,5,null,10,5]
解释：
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);  
// 初始的 (4x3) 矩形如下：
// 1 2 1
// 4 3 4
// 3 2 1
// 1 1 1
subrectangleQueries.getValue(0, 2); // 返回 1
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);
// 此次更新后矩形变为：
// 5 5 5
// 5 5 5
// 5 5 5
// 5 5 5 
subrectangleQueries.getValue(0, 2); // 返回 5
subrectangleQueries.getValue(3, 1); // 返回 5
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
// 此次更新后矩形变为：
// 5   5   5
// 5   5   5
// 5   5   5
// 10  10  10 
subrectangleQueries.getValue(3, 1); // 返回 10
subrectangleQueries.getValue(0, 2); // 返回 5

```
 **示例 2：** 

```
输入：
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue"]
[[[[1,1,1],[2,2,2],[3,3,3]]],[0,0],[0,0,2,2,100],[0,0],[2,2],[1,1,2,2,20],[2,2]]
输出：
[null,1,null,100,100,null,20]
解释：
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,1,1],[2,2,2],[3,3,3]]);
subrectangleQueries.getValue(0, 0); // 返回 1
subrectangleQueries.updateSubrectangle(0, 0, 2, 2, 100);
subrectangleQueries.getValue(0, 0); // 返回 100
subrectangleQueries.getValue(2, 2); // 返回 100
subrectangleQueries.updateSubrectangle(1, 1, 2, 2, 20);
subrectangleQueries.getValue(2, 2); // 返回 20

```
 

 **提示：** 
- 最多有 `500` 次 `updateSubrectangle` 和 `getValue` 操作。
-  `1 <= rows, cols <= 100` 
-  `rows == rectangle.length` 
-  `cols == rectangle[i].length` 
-  `0 <= row1 <= row2 < rows` 
-  `0 <= col1 <= col2 < cols` 
-  `1 <= newValue, rectangle[i][j] <= 10^9` 
-  `0 <= row < rows` 
-  `0 <= col < cols` 
 
**标签**
`设计` `数组` `矩阵` 


## 
```python

```
>
# 1477.找两个和为目标值且不重叠的子数组
[https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum](https://leetcode-cn.com/problems/find-two-non-overlapping-sub-arrays-each-with-target-sum) 
## 原题
给你一个整数数组 `arr` 和一个整数值 `target` 。

请你在 `arr` 中找 **两个互不重叠的子数组** 且它们的和都等于 `target` 。可能会有多种方案，请你返回满足要求的两个子数组长度和的 **最小值** 。

请返回满足要求的最小长度和，如果无法找到这样的两个子数组，请返回 **-1** 。

 

 **示例 1：** 

```
输入：arr = [3,2,2,4,3], target = 3
输出：2
解释：只有两个子数组和为 3 （[3] 和 [3]）。它们的长度和为 2 。

```
 **示例 2：** 

```
输入：arr = [7,3,4,7], target = 7
输出：2
解释：尽管我们有 3 个互不重叠的子数组和为 7 （[7], [3,4] 和 [7]），但我们会选择第一个和第三个子数组，因为它们的长度和 2 是最小值。

```
 **示例 3：** 

```
输入：arr = [4,3,2,6,2,3,4], target = 6
输出：-1
解释：我们只有一个和为 6 的子数组。

```
 **示例 4：** 

```
输入：arr = [5,5,4,4,5], target = 3
输出：-1
解释：我们无法找到和为 3 的子数组。

```
 **示例 5：** 

```
输入：arr = [3,1,1,1,5,1,2,1], target = 3
输出：3
解释：注意子数组 [1,2] 和 [2,1] 不能成为一个方案因为它们重叠了。

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `1 <= arr[i] <= 1000` 
-  `1 <= target <= 10^8` 
 
**标签**
`数组` `哈希表` `二分查找` `动态规划` `滑动窗口` 


## 
```python

```
>
# 1478.安排邮筒
[https://leetcode-cn.com/problems/allocate-mailboxes](https://leetcode-cn.com/problems/allocate-mailboxes) 
## 原题
给你一个房屋数组 `houses` 和一个整数 `k` ，其中 `houses[i]` 是第 `i` 栋房子在一条街上的位置，现需要在这条街上安排 `k` 个邮筒。

请你返回每栋房子与离它最近的邮筒之间的距离的 **最小** 总和。

答案保证在 32 位有符号整数范围以内。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/13/sample_11_1816.png" style="height: 154px; width: 454px;">

```
输入：houses = [1,4,8,10,20], k = 3
输出：5
解释：将邮筒分别安放在位置 3， 9 和 20 处。
每个房子到最近邮筒的距离和为 |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/13/sample_2_1816.png" style="height: 154px; width: 433px;">** 

```
输入：houses = [2,3,5,12,18], k = 2
输出：9
解释：将邮筒分别安放在位置 3 和 14 处。
每个房子到最近邮筒距离和为 |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9 。

```
 **示例 3：** 

```
输入：houses = [7,4,6,1], k = 1
输出：8

```
 **示例 4：** 

```
输入：houses = [3,6,14,10], k = 4
输出：0

```
 

 **提示：** 
-  `n == houses.length` 
-  `1 <= n <= 100` 
-  `1 <= houses[i] <= 10^4` 
-  `1 <= k <= n` 
- 数组 `houses` 中的整数互不相同。
 
**标签**
`数组` `数学` `动态规划` `排序` 


## 
```python

```
>
# 1479.周内每天的销售情况
[https://leetcode-cn.com/problems/sales-by-day-of-the-week](https://leetcode-cn.com/problems/sales-by-day-of-the-week) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1480.一维数组的动态和
[https://leetcode-cn.com/problems/running-sum-of-1d-array](https://leetcode-cn.com/problems/running-sum-of-1d-array) 
## 原题
给你一个数组 `nums` 。数组「动态和」的计算公式为： `runningSum[i] = sum(nums[0]&hellip;nums[i])` 。

请返回 `nums` 的动态和。

 

 **示例 1：** 

```
输入：nums = [1,2,3,4]
输出：[1,3,6,10]
解释：动态和计算过程为 [1, 1+2, 1+2+3, 1+2+3+4] 。
```
 **示例 2：** 

```
输入：nums = [1,1,1,1,1]
输出：[1,2,3,4,5]
解释：动态和计算过程为 [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1] 。
```
 **示例 3：** 

```
输入：nums = [3,1,2,10,1]
输出：[3,4,6,16,17]

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `-10^6 <= nums[i] <= 10^6` 
 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 1481.不同整数的最少数目
[https://leetcode-cn.com/problems/least-number-of-unique-integers-after-k-removals](https://leetcode-cn.com/problems/least-number-of-unique-integers-after-k-removals) 
## 原题
给你一个整数数组 `arr` 和一个整数 `k` 。现需要从数组中恰好移除 `k` 个元素，请找出移除后数组中不同整数的最少数目。
 

 **示例 1：** 

```
输入：arr = [5,5,4], k = 1
输出：1
解释：移除 1 个 4 ，数组中只剩下 5 一种整数。

```
 **示例 2：** 

```
输入：arr = [4,3,1,1,3,3,2], k = 3
输出：2
解释：先移除 4、2 ，然后再移除两个 1 中的任意 1 个或者三个 3 中的任意 1 个，最后剩下 1 和 3 两种整数。
```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `1 <= arr[i] <= 10^9` 
-  `0 <= k <= arr.length` 
 
**标签**
`贪心` `数组` `哈希表` `计数` `排序` 


## 
```python

```
>
# 1482.制作 m 束花所需的最少天数
[https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets](https://leetcode-cn.com/problems/minimum-number-of-days-to-make-m-bouquets) 
## 原题
给你一个整数数组 `bloomDay` ，以及两个整数 `m` 和 `k` 。

现需要制作 `m` 束花。制作花束时，需要使用花园中 **相邻的 `k` 朵花** 。

花园中有 `n` 朵花，第 `i` 朵花会在 `bloomDay[i]` 时盛开， **恰好** 可以用于 **一束** 花中。

请你返回从花园中摘 `m` 束花需要等待的最少的天数。如果不能摘到 `m` 束花则返回 **-1** 。

 

 **示例 1：** 

```
输入：bloomDay = [1,10,3,10,2], m = 3, k = 1
输出：3
解释：让我们一起观察这三天的花开过程，x 表示花开，而 _ 表示花还未开。
现在需要制作 3 束花，每束只需要 1 朵。
1 天后：[x, _, _, _, _]   // 只能制作 1 束花
2 天后：[x, _, _, _, x]   // 只能制作 2 束花
3 天后：[x, _, x, _, x]   // 可以制作 3 束花，答案为 3

```
 **示例 2：** 

```
输入：bloomDay = [1,10,3,10,2], m = 3, k = 2
输出：-1
解释：要制作 3 束花，每束需要 2 朵花，也就是一共需要 6 朵花。而花园中只有 5 朵花，无法满足制作要求，返回 -1 。

```
 **示例 3：** 

```
输入：bloomDay = [7,7,7,7,12,7,7], m = 2, k = 3
输出：12
解释：要制作 2 束花，每束需要 3 朵。
花园在 7 天后和 12 天后的情况如下：
7 天后：[x, x, x, x, _, x, x]
可以用前 3 朵盛开的花制作第一束花。但不能使用后 3 朵盛开的花，因为它们不相邻。
12 天后：[x, x, x, x, x, x, x]
显然，我们可以用不同的方式制作两束花。

```
 **示例 4：** 

```
输入：bloomDay = [1000000000,1000000000], m = 1, k = 1
输出：1000000000
解释：需要等 1000000000 天才能采到花来制作花束

```
 **示例 5：** 

```
输入：bloomDay = [1,10,2,9,3,8,4,7,5,6], m = 4, k = 2
输出：9

```
 

 **提示：** 
-  `bloomDay.length == n` 
-  `1 <= n <= 10^5` 
-  `1 <= bloomDay[i] <= 10^9` 
-  `1 <= m <= 10^6` 
-  `1 <= k <= n` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 1483.树节点的第 K 个祖先
[https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node](https://leetcode-cn.com/problems/kth-ancestor-of-a-tree-node) 
## 原题
给你一棵树，树上有 `n` 个节点，按从 `0` 到 `n-1` 编号。树以父节点数组的形式给出，其中 `parent[i]` 是节点 `i` 的父节点。树的根节点是编号为 `0` 的节点。

请你设计并实现 `getKthAncestor` `(int node, int k)` 函数，函数返回节点 `node` 的第 `k` 个祖先节点。如果不存在这样的祖先节点，返回 `-1` 。

树节点的第 *`k`* 个祖先节点是从该节点到根节点路径上的第 `k` 个节点。

 

 **示例：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/14/1528_ex1.png" style="height: 262px; width: 396px;">** 

```
输入：
["TreeAncestor","getKthAncestor","getKthAncestor","getKthAncestor"]
[[7,[-1,0,0,1,1,2,2]],[3,1],[5,2],[6,3]]

输出：
[null,1,0,-1]

解释：
TreeAncestor treeAncestor = new TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2]);

treeAncestor.getKthAncestor(3, 1);  // 返回 1 ，它是 3 的父节点
treeAncestor.getKthAncestor(5, 2);  // 返回 0 ，它是 5 的祖父节点
treeAncestor.getKthAncestor(6, 3);  // 返回 -1 因为不存在满足要求的祖先节点

```
 

 **提示：** 
-  `1 <= k <= n <= 5*10^4` 
-  `parent[0] == -1` 表示编号为 `0` 的节点是根节点。
- 对于所有的 `0 < i < n` ， `0 <= parent[i] < n` 总成立
-  `0 <= node < n` 
- 至多查询 `5*10^4` 次
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `设计` `二分查找` `动态规划` 


## 
```python

```
>
# 1484.按日期分组销售产品
[https://leetcode-cn.com/problems/group-sold-products-by-the-date](https://leetcode-cn.com/problems/group-sold-products-by-the-date) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1485.克隆含随机指针的二叉树
[https://leetcode-cn.com/problems/clone-binary-tree-with-random-pointer](https://leetcode-cn.com/problems/clone-binary-tree-with-random-pointer) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `哈希表` `二叉树` 


## 
```python

```
>
# 1486.数组异或操作
[https://leetcode-cn.com/problems/xor-operation-in-an-array](https://leetcode-cn.com/problems/xor-operation-in-an-array) 
## 原题
给你两个整数， `n` 和 `start` 。

数组 `nums` 定义为： `nums[i] = start + 2*i` （下标从 0 开始）且 `n == nums.length` 。

请返回 `nums` 中所有元素按位异或（ **XOR** ）后得到的结果。

 

 **示例 1：** 

```
输入：n = 5, start = 0
输出：8
解释：数组 nums 为 [0, 2, 4, 6, 8]，其中 (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8 。
     "^" 为按位异或 XOR 运算符。

```
 **示例 2：** 

```
输入：n = 4, start = 3
输出：8
解释：数组 nums 为 [3, 5, 7, 9]，其中 (3 ^ 5 ^ 7 ^ 9) = 8.
```
 **示例 3：** 

```
输入：n = 1, start = 7
输出：7

```
 **示例 4：** 

```
输入：n = 10, start = 5
输出：2

```
 

 **提示：** 
-  `1 <= n <= 1000` 
-  `0 <= start <= 1000` 
-  `n == nums.length` 
 
**标签**
`位运算` `数学` 


## 
```python

```
>
# 1487.保证文件名唯一
[https://leetcode-cn.com/problems/making-file-names-unique](https://leetcode-cn.com/problems/making-file-names-unique) 
## 原题
给你一个长度为 `n` 的字符串数组 `names` 。你将会在文件系统中创建 `n` 个文件夹：在第 `i` 分钟，新建名为 `names[i]` 的文件夹。

由于两个文件 **不能** 共享相同的文件名，因此如果新建文件夹使用的文件名已经被占用，系统会以 `(k)` 的形式为新文件夹的文件名添加后缀，其中 `k` 是能保证文件名唯一的 **最小正整数** 。

返回长度为 *`n`* 的字符串数组，其中 `ans[i]` 是创建第 `i` 个文件夹时系统分配给该文件夹的实际名称。

 

 **示例 1：** 

```
输入：names = ["pes","fifa","gta","pes(2019)"]
输出：["pes","fifa","gta","pes(2019)"]
解释：文件系统将会这样创建文件名：
"pes" --> 之前未分配，仍为 "pes"
"fifa" --> 之前未分配，仍为 "fifa"
"gta" --> 之前未分配，仍为 "gta"
"pes(2019)" --> 之前未分配，仍为 "pes(2019)"

```
 **示例 2：** 

```
输入：names = ["gta","gta(1)","gta","avalon"]
输出：["gta","gta(1)","gta(2)","avalon"]
解释：文件系统将会这样创建文件名：
"gta" --> 之前未分配，仍为 "gta"
"gta(1)" --> 之前未分配，仍为 "gta(1)"
"gta" --> 文件名被占用，系统为该名称添加后缀 (k)，由于 "gta(1)" 也被占用，所以 k = 2 。实际创建的文件名为 "gta(2)" 。
"avalon" --> 之前未分配，仍为 "avalon"

```
 **示例 3：** 

```
输入：names = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
输出：["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece(4)"]
解释：当创建最后一个文件夹时，最小的正有效 k 为 4 ，文件名变为 "onepiece(4)"。

```
 **示例 4：** 

```
输入：names = ["wano","wano","wano","wano"]
输出：["wano","wano(1)","wano(2)","wano(3)"]
解释：每次创建文件夹 "wano" 时，只需增加后缀中 k 的值即可。
```
 **示例 5：** 

```
输入：names = ["kaido","kaido(1)","kaido","kaido(1)"]
输出：["kaido","kaido(1)","kaido(2)","kaido(1)(1)"]
解释：注意，如果含后缀文件名被占用，那么系统也会按规则在名称后添加新的后缀 (k) 。

```
 

 **提示：** 
-  `1 <= names.length <= 5 * 10^4` 
-  `1 <= names[i].length <= 20` 
-  `names[i]` 由小写英文字母、数字和/或圆括号组成。
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 1488.避免洪水泛滥
[https://leetcode-cn.com/problems/avoid-flood-in-the-city](https://leetcode-cn.com/problems/avoid-flood-in-the-city) 
## 原题
你的国家有无数个湖泊，所有湖泊一开始都是空的。当第 `n` 个湖泊下雨的时候，如果第 `n` 个湖泊是空的，那么它就会装满水，否则这个湖泊会发生洪水。你的目标是避免任意一个湖泊发生洪水。

给你一个整数数组 `rains` ，其中：
-  `rains[i] > 0` 表示第 `i` 天时，第 `rains[i]` 个湖泊会下雨。
-  `rains[i] == 0` 表示第 `i` 天没有湖泊会下雨，你可以选择 **一个** 湖泊并 **抽干** 这个湖泊的水。
请返回一个数组 `ans` ，满足：
-  `ans.length == rains.length` 
- 如果 `rains[i] > 0` ，那么 `ans[i] == -1` 。
- 如果 `rains[i] == 0` ， `ans[i]` 是你第 `i` 天选择抽干的湖泊。
如果有多种可行解，请返回它们中的 **任意一个** 。如果没办法阻止洪水，请返回一个 **空的数组** 。

请注意，如果你选择抽干一个装满水的湖泊，它会变成一个空的湖泊。但如果你选择抽干一个空的湖泊，那么将无事发生（详情请看示例 4）。

 

 **示例 1：** 

```
输入：rains = [1,2,3,4]
输出：[-1,-1,-1,-1]
解释：第一天后，装满水的湖泊包括 [1]
第二天后，装满水的湖泊包括 [1,2]
第三天后，装满水的湖泊包括 [1,2,3]
第四天后，装满水的湖泊包括 [1,2,3,4]
没有哪一天你可以抽干任何湖泊的水，也没有湖泊会发生洪水。

```
 **示例 2：** 

```
输入：rains = [1,2,0,0,2,1]
输出：[-1,-1,2,1,-1,-1]
解释：第一天后，装满水的湖泊包括 [1]
第二天后，装满水的湖泊包括 [1,2]
第三天后，我们抽干湖泊 2 。所以剩下装满水的湖泊包括 [1]
第四天后，我们抽干湖泊 1 。所以暂时没有装满水的湖泊了。
第五天后，装满水的湖泊包括 [2]。
第六天后，装满水的湖泊包括 [1,2]。
可以看出，这个方案下不会有洪水发生。同时， [-1,-1,1,2,-1,-1] 也是另一个可行的没有洪水的方案。

```
 **示例 3：** 

```
输入：rains = [1,2,0,1,2]
输出：[]
解释：第二天后，装满水的湖泊包括 [1,2]。我们可以在第三天抽干一个湖泊的水。
但第三天后，湖泊 1 和 2 都会再次下雨，所以不管我们第三天抽干哪个湖泊的水，另一个湖泊都会发生洪水。

```
 **示例 4：** 

```
输入：rains = [69,0,0,0,69]
输出：[-1,69,1,1,-1]
解释：任何形如 [-1,69,x,y,-1], [-1,x,69,y,-1] 或者 [-1,x,y,69,-1] 都是可行的解，其中 1 <= x,y <= 10^9

```
 **示例 5：** 

```
输入：rains = [10,20,20]
输出：[]
解释：由于湖泊 20 会连续下 2 天的雨，所以没有没有办法阻止洪水。

```
 

 **提示：** 
-  `1 <= rains.length <= 10^5` 
-  `0 <= rains[i] <= 10^9` 
 
**标签**
`贪心` `数组` `哈希表` `二分查找` `堆（优先队列）` 


## 
```python

```
>
# 1489.找到最小生成树里的关键边和伪关键边
[https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree](https://leetcode-cn.com/problems/find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree) 
## 原题
给你一个 `n` 个点的带权无向连通图，节点编号为 `0` 到 `n-1` ，同时还有一个数组 `edges` ，其中 `edges[i] = [from` `<sub>i</sub>, to<sub>i</sub>, weight<sub>i</sub>]` 表示在 `from<sub>i</sub>` 和 `to<sub>i</sub>` 节点之间有一条带权无向边。最小生成树 (MST) 是给定图中边的一个子集，它连接了所有节点且没有环，而且这些边的权值和最小。

请你找到给定图中最小生成树的所有关键边和伪关键边。如果从图中删去某条边，会导致最小生成树的权值和增加，那么我们就说它是一条关键边。伪关键边则是可能会出现在某些最小生成树中但不会出现在所有最小生成树中的边。

请注意，你可以分别以任意顺序返回关键边的下标和伪关键边的下标。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/21/ex1.png" style="height: 262px; width: 259px;">

```
输入：n = 5, edges = [[0,1,1],[1,2,1],[2,3,2],[0,3,2],[0,4,3],[3,4,3],[1,4,6]]
输出：[[0,1],[2,3,4,5]]
解释：上图描述了给定图。
下图是所有的最小生成树。
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/21/msts.png" style="height: 553px; width: 540px;">
注意到第 0 条边和第 1 条边出现在了所有最小生成树中，所以它们是关键边，我们将这两个下标作为输出的第一个列表。
边 2，3，4 和 5 是所有 MST 的剩余边，所以它们是伪关键边。我们将它们作为输出的第二个列表。

```
 **示例 2 ：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/21/ex2.png" style="height: 253px; width: 247px;">

```
输入：n = 4, edges = [[0,1,1],[1,2,1],[2,3,1],[0,3,1]]
输出：[[],[0,1,2,3]]
解释：可以观察到 4 条边都有相同的权值，任选它们中的 3 条可以形成一棵 MST 。所以 4 条边都是伪关键边。

```
 

 **提示：** 
-  `2 <= n <= 100` 
-  `1 <= edges.length <= min(200, n * (n - 1) / 2)` 
-  `edges[i].length == 3` 
-  `0 <= from<sub>i</sub> < to<sub>i</sub> < n` 
-  `1 <= weight<sub>i</sub> <= 1000` 
- 所有 `(from<sub>i</sub>, to<sub>i</sub>)` 数对都是互不相同的。
 
**标签**
`并查集` `图` `最小生成树` `排序` `强连通分量` 


## 
```python

```
>
# 1490.克隆 N 叉树
[https://leetcode-cn.com/problems/clone-n-ary-tree](https://leetcode-cn.com/problems/clone-n-ary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `哈希表` 


## 
```python

```
>
# 1491.去掉最低工资和最高工资后的工资平均值
[https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary](https://leetcode-cn.com/problems/average-salary-excluding-the-minimum-and-maximum-salary) 
## 原题
给你一个整数数组 `salary` ，数组里每个数都是 **唯一** 的，其中 `salary[i]` 是第 `i` 个员工的工资。

请你返回去掉最低工资和最高工资以后，剩下员工工资的平均值。

 

 **示例 1：** 

```
输入：salary = [4000,3000,1000,2000]
输出：2500.00000
解释：最低工资和最高工资分别是 1000 和 4000 。
去掉最低工资和最高工资以后的平均工资是 (2000+3000)/2= 2500

```
 **示例 2：** 

```
输入：salary = [1000,2000,3000]
输出：2000.00000
解释：最低工资和最高工资分别是 1000 和 3000 。
去掉最低工资和最高工资以后的平均工资是 (2000)/1= 2000

```
 **示例 3：** 

```
输入：salary = [6000,5000,4000,3000,2000,1000]
输出：3500.00000

```
 **示例 4：** 

```
输入：salary = [8000,9000,2000,3000,6000,1000]
输出：4750.00000

```
 

 **提示：** 
-  `3 <= salary.length <= 100` 
-  `10^3 <= salary[i] <= 10^6` 
-  `salary[i]` 是唯一的。
- 与真实值误差在 `10^-5` 以内的结果都将视为正确答案。
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 1492.n 的第 k 个因子
[https://leetcode-cn.com/problems/the-kth-factor-of-n](https://leetcode-cn.com/problems/the-kth-factor-of-n) 
## 原题
给你两个正整数 `n` 和 `k` 。

如果正整数 `i` 满足 `n % i == 0` ，那么我们就说正整数 `i` 是整数 `n` 的因子。

考虑整数 `n` 的所有因子，将它们 **升序排列** 。请你返回第 `k` 个因子。如果 `n` 的因子数少于 `k` ，请你返回 **-1** 。

 

 **示例 1：** 

```
输入：n = 12, k = 3
输出：3
解释：因子列表包括 [1, 2, 3, 4, 6, 12]，第 3 个因子是 3 。

```
 **示例 2：** 

```
输入：n = 7, k = 2
输出：7
解释：因子列表包括 [1, 7] ，第 2 个因子是 7 。

```
 **示例 3：** 

```
输入：n = 4, k = 4
输出：-1
解释：因子列表包括 [1, 2, 4] ，只有 3 个因子，所以我们应该返回 -1 。

```
 **示例 4：** 

```
输入：n = 1, k = 1
输出：1
解释：因子列表包括 [1] ，第 1 个因子为 1 。

```
 **示例 5：** 

```
输入：n = 1000, k = 3
输出：4
解释：因子列表包括 [1, 2, 4, 5, 8, 10, 20, 25, 40, 50, 100, 125, 200, 250, 500, 1000] 。

```
 

 **提示：** 
-  `1 <= k <= n <= 1000` 
 
**标签**
`数学` 


## 
```python

```
>
# 1493.删掉一个元素以后全为 1 的最长子数组
[https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element](https://leetcode-cn.com/problems/longest-subarray-of-1s-after-deleting-one-element) 
## 原题
给你一个二进制数组 `nums` ，你需要从中删掉一个元素。

请你在删掉元素的结果数组中，返回最长的且只包含 1 的非空子数组的长度。

如果不存在这样的子数组，请返回 0 。

 

 **提示 1：** 

```
输入：nums = [1,1,0,1]
输出：3
解释：删掉位置 2 的数后，[1,1,1] 包含 3 个 1 。
```
 **示例 2：** 

```
输入：nums = [0,1,1,1,0,1,1,0,1]
输出：5
解释：删掉位置 4 的数字后，[0,1,1,1,1,1,0,1] 的最长全 1 子数组为 [1,1,1,1,1] 。
```
 **示例 3：** 

```
输入：nums = [1,1,1]
输出：2
解释：你必须要删除一个元素。
```
 **示例 4：** 

```
输入：nums = [1,1,0,0,1,1,1,0,1]
输出：4

```
 **示例 5：** 

```
输入：nums = [0,0,0]
输出：0

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `nums[i]` 要么是 `0` 要么是 `1` 。
 
**标签**
`数学` `动态规划` `滑动窗口` 


## 
```python

```
>
# 1494.并行课程 II
[https://leetcode-cn.com/problems/parallel-courses-ii](https://leetcode-cn.com/problems/parallel-courses-ii) 
## 原题
给你一个整数 `n` 表示某所大学里课程的数目，编号为 `1` 到 `n` ，数组 `dependencies` 中， `dependencies[i] = [x<sub>i</sub>, y<sub>i</sub>]` 表示一个先修课的关系，也就是课程 `x<sub>i</sub>` 必须在课程 `y<sub>i</sub>` <sub> </sub>之前上。同时你还有一个整数 `k` 。

在一个学期中，你 **最多** 可以同时上 `k` 门课，前提是这些课的先修课在之前的学期里已经上过了。

请你返回上完所有课最少需要多少个学期。题目保证一定存在一种上完所有课的方式。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/27/leetcode_parallel_courses_1.png" style="height: 164px; width: 300px;">** 

```
输入：n = 4, dependencies = [[2,1],[3,1],[1,4]], k = 2
输出：3 
解释：上图展示了题目输入的图。在第一个学期中，我们可以上课程 2 和课程 3 。然后第二个学期上课程 1 ，第三个学期上课程 4 。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/27/leetcode_parallel_courses_2.png" style="height: 234px; width: 300px;">** 

```
输入：n = 5, dependencies = [[2,1],[3,1],[4,1],[1,5]], k = 2
输出：4 
解释：上图展示了题目输入的图。一个最优方案是：第一学期上课程 2 和 3，第二学期上课程 4 ，第三学期上课程 1 ，第四学期上课程 5 。

```
 **示例 3：** 

```
输入：n = 11, dependencies = [], k = 2
输出：6

```
 

 **提示：** 
-  `1 <= n <= 15` 
-  `1 <= k <= n` 
-  `0 <= dependencies.length <= n * (n-1) / 2` 
-  `dependencies[i].length == 2` 
-  `1 <= x<sub>i</sub>, y<sub>i</sub> <= n` 
-  `x<sub>i</sub> != y<sub>i</sub>` 
- 所有先修关系都是不同的，也就是说 `dependencies[i] != dependencies[j]` 。
- 题目输入的图是个有向无环图。
 
**标签**
`位运算` `图` `动态规划` `状态压缩` 


## 
```python

```
>
# 1495.上月播放的儿童适宜电影
[https://leetcode-cn.com/problems/friendly-movies-streamed-last-month](https://leetcode-cn.com/problems/friendly-movies-streamed-last-month) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1496.判断路径是否相交
[https://leetcode-cn.com/problems/path-crossing](https://leetcode-cn.com/problems/path-crossing) 
## 原题
给你一个字符串 `path` ，其中 `path[i]` 的值可以是 `'N'` 、 `'S'` 、 `'E'` 或者 `'W'` ，分别表示向北、向南、向东、向西移动一个单位。

你从二维平面上的原点 `(0, 0)` 处开始出发，按 `path` 所指示的路径行走。

如果路径在任何位置上与自身相交，也就是走到之前已经走过的位置，请返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/28/screen-shot-2020-06-10-at-123929-pm.png" style="height: 224px; width: 250px;" />

```

输入：path = "NES"
输出：false 
解释：该路径没有在任何位置相交。
```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/06/28/screen-shot-2020-06-10-at-123843-pm.png" style="height: 212px; width: 250px;" />

```

输入：path = "NESWW"
输出：true
解释：该路径经过原点两次。
```
 

 **提示：** 
-  `1 <= path.length <= 10^4` 
-  `path[i]` 为 `'N'` 、 `'S'` 、 `'E'` 或 `'W'` 
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1497.检查数组对是否可以被 k 整除
[https://leetcode-cn.com/problems/check-if-array-pairs-are-divisible-by-k](https://leetcode-cn.com/problems/check-if-array-pairs-are-divisible-by-k) 
## 原题
给你一个整数数组 `arr` 和一个整数 `k` ，其中数组长度是偶数，值为 `n` 。

现在需要把数组恰好分成 `n / 2` 对，以使每对数字的和都能够被 `k` 整除。

如果存在这样的分法，请返回 *True* ；否则，返回 *False* 。

 

 **示例 1：** 

```
输入：arr = [1,2,3,4,5,10,6,7,8,9], k = 5
输出：true
解释：划分后的数字对为 (1,9),(2,8),(3,7),(4,6) 以及 (5,10) 。

```
 **示例 2：** 

```
输入：arr = [1,2,3,4,5,6], k = 7
输出：true
解释：划分后的数字对为 (1,6),(2,5) 以及 (3,4) 。

```
 **示例 3：** 

```
输入：arr = [1,2,3,4,5,6], k = 10
输出：false
解释：无法在将数组中的数字分为三对的同时满足每对数字和能够被 10 整除的条件。

```
 **示例 4：** 

```
输入：arr = [-10,10], k = 2
输出：true

```
 **示例 5：** 

```
输入：arr = [-1,1,-2,2,-3,3,-4,4], k = 3
输出：true

```
 

 **提示：** 
-  `arr.length == n` 
-  `1 <= n <= 10^5` 
-  `n` 为偶数
-  `-10^9 <= arr[i] <= 10^9` 
-  `1 <= k <= 10^5` 
 
**标签**
`数组` `哈希表` `计数` 


## 
```python

```
>
# 1498.满足条件的子序列数目
[https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition](https://leetcode-cn.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition) 
## 原题
给你一个整数数组 `nums` 和一个整数 `target` 。

请你统计并返回 `nums` 中能满足其最小元素与最大元素的 **和** 小于或等于 `target` 的 **非空** 子序列的数目。

由于答案可能很大，请将结果对 10^9 + 7 取余后返回。

 

 **示例 1：** 

```
输入：nums = [3,5,6,7], target = 9
输出：4
解释：有 4 个子序列满足该条件。
[3] -> 最小元素 + 最大元素 <= target (3 + 3 <= 9)
[3,5] -> (3 + 5 <= 9)
[3,5,6] -> (3 + 6 <= 9)
[3,6] -> (3 + 6 <= 9)

```
 **示例 2：** 

```
输入：nums = [3,3,6,8], target = 10
输出：6
解释：有 6 个子序列满足该条件。（nums 中可以有重复数字）
[3] , [3] , [3,3], [3,6] , [3,6] , [3,3,6]
```
 **示例 3：** 

```
输入：nums = [2,3,3,4,6,7], target = 12
输出：61
解释：共有 63 个非空子序列，其中 2 个不满足条件（[6,7], [7]）
有效序列总数为（63 - 2 = 61）

```
 **示例 4：** 

```
输入：nums = [5,2,4,1,7,6,8], target = 16
输出：127
解释：所有非空子序列都满足条件 (2^7 - 1) = 127
```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^6` 
-  `1 <= target <= 10^6` 
 
**标签**
`数组` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 1499.满足不等式的最大值
[https://leetcode-cn.com/problems/max-value-of-equation](https://leetcode-cn.com/problems/max-value-of-equation) 
## 原题
给你一个数组 `points` 和一个整数 `k` 。数组中每个元素都表示二维平面上的点的坐标，并按照横坐标 x 的值从小到大排序。也就是说 `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` ，并且在 `1 <= i < j <= points.length` 的前提下， `x<sub>i</sub> < x<sub>j</sub>` 总成立。

请你找出 `y<sub>i</sub> + y<sub>j</sub> + |x<sub>i</sub> - x<sub>j</sub>|` 的 **最大值** ，其中 `|x<sub>i</sub> - x<sub>j</sub>| <= k` 且 `1 <= i < j <= points.length` 。

题目测试数据保证至少存在一对能够满足 `|x<sub>i</sub> - x<sub>j</sub>| <= k` 的点。

 

 **示例 1：** 

```
输入：points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
输出：4
解释：前两个点满足 |xi - xj| <= 1 ，代入方程计算，则得到值 3 + 0 + |1 - 2| = 4 。第三个和第四个点也满足条件，得到值 10 + -10 + |5 - 6| = 1 。
没有其他满足条件的点，所以返回 4 和 1 中最大的那个。
```
 **示例 2：** 

```
输入：points = [[0,0],[3,0],[9,2]], k = 3
输出：3
解释：只有前两个点满足 |xi - xj| <= 3 ，代入方程后得到值 0 + 0 + |0 - 3| = 3 。

```
 

 **提示：** 
-  `2 <= points.length <= 10^5` 
-  `points[i].length == 2` 
-  `-10^8 <= points[i][0], points[i][1] <= 10^8` 
-  `0 <= k <= 2 * 10^8` 
- 对于所有的 `1 <= i < j <= points.length` ， `points[i][0] < points[j][0]` 都成立。也就是说， `x<sub>i</sub>` 是严格递增的。
 
**标签**
`队列` `数组` `滑动窗口` `单调队列` `堆（优先队列）` 


## 
```python

```
>
# 1500.设计文件分享系统
[https://leetcode-cn.com/problems/design-a-file-sharing-system](https://leetcode-cn.com/problems/design-a-file-sharing-system) 
## 原题

 
**标签**
`设计` `哈希表` `数据流` `堆（优先队列）` 


## 
```python

```
>
