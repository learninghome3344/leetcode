# 1801.积压订单中的订单总数
[https://leetcode-cn.com/problems/number-of-orders-in-the-backlog](https://leetcode-cn.com/problems/number-of-orders-in-the-backlog) 
## 原题
给你一个二维整数数组 `orders` ，其中每个 `orders[i] = [price<sub>i</sub>, amount<sub>i</sub>, orderType<sub>i</sub>]` 表示有 `amount<sub>i</sub>` <sub> </sub>笔类型为  `orderType<sub>i</sub>` 、价格为  `price<sub>i</sub>` 的订单。

订单类型 `orderType<sub>i</sub>` 可以分为两种：
-  `0` 表示这是一批采购订单 `buy` 
-  `1` 表示这是一批销售订单 `sell` 
注意， `orders[i]` 表示一批共计 `amount<sub>i</sub>` 笔的独立订单，这些订单的价格和类型相同。对于所有有效的 `i` ，由 `orders[i]` 表示的所有订单提交时间均早于 `orders[i+1]` 表示的所有订单。

存在由未执行订单组成的 **积压订单** 。积压订单最初是空的。提交订单时，会发生以下情况：
- 如果该订单是一笔采购订单 `buy` ，则可以查看积压订单中价格 **最低** 的销售订单 `sell` 。如果该销售订单 `sell` 的价格 **低于或等于** 当前采购订单 `buy` 的价格，则匹配并执行这两笔订单，并将销售订单 `sell` 从积压订单中删除。否则，采购订单 `buy` 将会添加到积压订单中。
- 反之亦然，如果该订单是一笔销售订单 `sell` ，则可以查看积压订单中价格 **最高** 的采购订单 `buy` 。如果该采购订单 `buy` 的价格 **高于或等于** 当前销售订单 `sell` 的价格，则匹配并执行这两笔订单，并将采购订单 `buy` 从积压订单中删除。否则，销售订单 `sell` 将会添加到积压订单中。
输入所有订单后，返回积压订单中的 **订单总数** 。由于数字可能很大，所以需要返回对 `10^9 + 7` 取余的结果。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/03/21/ex1.png" style="width: 450px; height: 479px;" />
```

输入：orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]
输出：6
解释：输入订单后会发生下述情况：
- 提交 5 笔采购订单，价格为 10 。没有销售订单，所以这 5 笔订单添加到积压订单中。
- 提交 2 笔销售订单，价格为 15 。没有采购订单的价格大于或等于 15 ，所以这 2 笔订单添加到积压订单中。
- 提交 1 笔销售订单，价格为 25 。没有采购订单的价格大于或等于 25 ，所以这 1 笔订单添加到积压订单中。
- 提交 4 笔采购订单，价格为 30 。前 2 笔采购订单与价格最低（价格为 15）的 2 笔销售订单匹配，从积压订单中删除这 2 笔销售订单。第 3 笔采购订单与价格最低的 1 笔销售订单匹配，销售订单价格为 25 ，从积压订单中删除这 1 笔销售订单。积压订单中不存在更多销售订单，所以第 4 笔采购订单需要添加到积压订单中。
最终，积压订单中有 5 笔价格为 10 的采购订单，和 1 笔价格为 30 的采购订单。所以积压订单中的订单总数为 6 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/03/21/ex2.png" style="width: 450px; height: 584px;" />
```

输入：orders = [[7,1000000000,1],[15,3,0],[5,999999995,0],[5,1,1]]
输出：999999984
解释：输入订单后会发生下述情况：
- 提交 10^9 笔销售订单，价格为 7 。没有采购订单，所以这 10^9 笔订单添加到积压订单中。
- 提交 3 笔采购订单，价格为 15 。这些采购订单与价格最低（价格为 7 ）的 3 笔销售订单匹配，从积压订单中删除这 3 笔销售订单。
- 提交 999999995 笔采购订单，价格为 5 。销售订单的最低价为 7 ，所以这 999999995 笔订单添加到积压订单中。
- 提交 1 笔销售订单，价格为 5 。这笔销售订单与价格最高（价格为 5 ）的 1 笔采购订单匹配，从积压订单中删除这 1 笔采购订单。
最终，积压订单中有 (1000000000-3) 笔价格为 7 的销售订单，和 (999999995-1) 笔价格为 5 的采购订单。所以积压订单中的订单总数为 1999999991 ，等于 999999984 % (10^9 + 7) 。
```
 

 **提示：** 
-  `1 <= orders.length <= 10^5` 
-  `orders[i].length == 3` 
-  `1 <= price<sub>i</sub>, amount<sub>i</sub> <= 10^9` 
-  `orderType<sub>i</sub>` 为 `0` 或 `1` 
 
**标签**
`数组` `模拟` `堆（优先队列）` 


## 
```python

```
>
# 1802.有界数组中指定下标处的最大值
[https://leetcode-cn.com/problems/maximum-value-at-a-given-index-in-a-bounded-array](https://leetcode-cn.com/problems/maximum-value-at-a-given-index-in-a-bounded-array) 
## 原题
给你三个正整数 `n` 、 `index` 和 `maxSum` 。你需要构造一个同时满足下述所有条件的数组 `nums` （下标 **从 0 开始** 计数）：
-  `nums.length == n` 
-  `nums[i]` 是 **正整数** ，其中 `0 <= i < n` 
-  `abs(nums[i] - nums[i+1]) <= 1` ，其中 `0 <= i < n-1` 
-  `nums` 中所有元素之和不超过 `maxSum` 
-  `nums[index]` 的值被 **最大化** 
返回你所构造的数组中的 `nums[index]` 。

注意： `abs(x)` 等于 `x` 的前提是 `x >= 0` ；否则， `abs(x)` 等于 `-x` 。

 

 **示例 1：** 

```
输入：n = 4, index = 2,  maxSum = 6
输出：2
解释：数组 [1,1,2,1] 和 [1,2,2,1] 满足所有条件。不存在其他在指定下标处具有更大值的有效数组。

```
 **示例 2：** 

```
输入：n = 6, index = 1,  maxSum = 10
输出：3

```
 

 **提示：** 
-  `1 <= n <= maxSum <= 10^9` 
-  `0 <= index < n` 
 
**标签**
`贪心` `二分查找` 


## 
```python

```
>
# 1803.统计异或值在范围内的数对有多少
[https://leetcode-cn.com/problems/count-pairs-with-xor-in-a-range](https://leetcode-cn.com/problems/count-pairs-with-xor-in-a-range) 
## 原题
给你一个整数数组 `nums` （下标 **从 0 开始** 计数）以及两个整数： `low` 和 `high` ，请返回 **漂亮数对** 的数目。

 **漂亮数对** 是一个形如 `(i, j)` 的数对，其中 `0 <= i < j < nums.length` 且 `low <= (nums[i] XOR nums[j]) <= high` 。

 

 **示例 1：** 

```
输入：nums = [1,4,2,7], low = 2, high = 6
输出：6
解释：所有漂亮数对 (i, j) 列出如下：
    - (0, 1): nums[0] XOR nums[1] = 5 
    - (0, 2): nums[0] XOR nums[2] = 3
    - (0, 3): nums[0] XOR nums[3] = 6
    - (1, 2): nums[1] XOR nums[2] = 6
    - (1, 3): nums[1] XOR nums[3] = 3
    - (2, 3): nums[2] XOR nums[3] = 5

```
 **示例 2：** 

```
输入：nums = [9,8,4,2,1], low = 5, high = 14
输出：8
解释：所有漂亮数对 (i, j) 列出如下：
​​​​​    - (0, 2): nums[0] XOR nums[2] = 13
    - (0, 3): nums[0] XOR nums[3] = 11
    - (0, 4): nums[0] XOR nums[4] = 8
    - (1, 2): nums[1] XOR nums[2] = 12
    - (1, 3): nums[1] XOR nums[3] = 10
    - (1, 4): nums[1] XOR nums[4] = 9
    - (2, 3): nums[2] XOR nums[3] = 6
    - (2, 4): nums[2] XOR nums[4] = 5
```
 

 **提示：** 
-  `1 <= nums.length <= 2 * 10^4` 
-  `1 <= nums[i] <= 2 * 10^4` 
-  `1 <= low <= high <= 2 * 10^4` 
 
**标签**
`位运算` `字典树` `数组` 


## 
```python

```
>
# 1804.实现 Trie （前缀树） II
[https://leetcode-cn.com/problems/implement-trie-ii-prefix-tree](https://leetcode-cn.com/problems/implement-trie-ii-prefix-tree) 
## 原题

 
**标签**
`设计` `字典树` `哈希表` `字符串` 


## 
```python

```
>
# 1805.字符串中不同整数的数目
[https://leetcode-cn.com/problems/number-of-different-integers-in-a-string](https://leetcode-cn.com/problems/number-of-different-integers-in-a-string) 
## 原题
给你一个字符串 `word` ，该字符串由数字和小写英文字母组成。

请你用空格替换每个不是数字的字符。例如， `"a123bc34d8ef34"` 将会变成 `" 123  34 8  34"` 。注意，剩下的这些整数为（相邻彼此至少有一个空格隔开）： `"123"` 、 `"34"` 、 `"8"` 和 `"34"` 。

返回对 `word` 完成替换后形成的 **不同** 整数的数目。

只有当两个整数的 **不含前导零** 的十进制表示不同， 才认为这两个整数也不同。

 

 **示例 1：** 

```

输入：word = "a123bc34d8ef34"
输出：3
解释：不同的整数有 "123"、"34" 和 "8" 。注意，"34" 只计数一次。

```
 **示例 2：** 

```

输入：word = "leet1234code234"
输出：2

```
 **示例 3：** 

```

输入：word = "a1b01c001"
输出：1
解释："1"、"01" 和 "001" 视为同一个整数的十进制表示，因为在比较十进制值时会忽略前导零的存在。

```
 

 **提示：** 
-  `1 <= word.length <= 1000` 
-  `word` 由数字和小写英文字母组成
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1806.还原排列的最少操作步数
[https://leetcode-cn.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation](https://leetcode-cn.com/problems/minimum-number-of-operations-to-reinitialize-a-permutation) 
## 原题
给你一个偶数 `n` ​​​​​​ ，已知存在一个长度为 `n` 的排列 `perm` ，其中 `perm[i] == i` ​（下标 **从 0 开始** 计数）。

一步操作中，你将创建一个新数组 `arr` ，对于每个 `i` ：
- 如果 `i % 2 == 0` ，那么 `arr[i] = perm[i / 2]` 
- 如果 `i % 2 == 1` ，那么 `arr[i] = perm[n / 2 + (i - 1) / 2]` 
然后将 `arr` ​​ 赋值​​给 `perm` 。

要想使 `perm` 回到排列初始值，至少需要执行多少步操作？返回最小的 **非零** 操作步数。

 

 **示例 1：** 

```

输入：n = 2
输出：1
解释：最初，perm = [0,1]
第 1 步操作后，perm = [0,1]
所以，仅需执行 1 步操作
```
 **示例 2：** 

```

输入：n = 4
输出：2
解释：最初，perm = [0,1,2,3]
第 1 步操作后，perm = [0,2,1,3]
第 2 步操作后，perm = [0,1,2,3]
所以，仅需执行 2 步操作
```
 **示例 3：** 

```

输入：n = 6
输出：4

```
 

 **提示：** 
-  `2 <= n <= 1000` 
-  `n` ​​​​​​ 是一个偶数
 
**标签**
`数组` `数学` `模拟` 


## 
```python

```
>
# 1807.替换字符串中的括号内容
[https://leetcode-cn.com/problems/evaluate-the-bracket-pairs-of-a-string](https://leetcode-cn.com/problems/evaluate-the-bracket-pairs-of-a-string) 
## 原题
给你一个字符串  `s`  ，它包含一些括号对，每个括号中包含一个 **非空**  的键。
- 比方说，字符串  `"(name)is(age)yearsold"`  中，有  **两个**  括号对，分别包含键  `"name"` 和  `"age"`  。
你知道许多键对应的值，这些关系由二维字符串数组  `knowledge`  表示，其中  `knowledge[i] = [key<sub>i</sub>, value<sub>i</sub>]`  ，表示键  `key<sub>i</sub>`  对应的值为  `value<sub>i</sub>` <sub> </sub>。

你需要替换 **所有**  的括号对。当你替换一个括号对，且它包含的键为  `key<sub>i</sub>`  时，你需要：
- 将  `key<sub>i</sub>`  和括号用对应的值  `value<sub>i</sub>`  替换。
- 如果从 `knowledge`  中无法得知某个键对应的值，你需要将  `key<sub>i</sub>`  和括号用问号  `"?"`  替换（不需要引号）。
 `knowledge`  中每个键最多只会出现一次。 `s`  中不会有嵌套的括号。

请你返回替换 **所有**  括号对后的结果字符串。

 

 **示例 1：** 

```
输入：s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
输出："bobistwoyearsold"
解释：
键 "name" 对应的值为 "bob" ，所以将 "(name)" 替换为 "bob" 。
键 "age" 对应的值为 "two" ，所以将 "(age)" 替换为 "two" 。

```
 **示例 2：** 

```
输入：s = "hi(name)", knowledge = [["a","b"]]
输出："hi?"
解释：由于不知道键 "name" 对应的值，所以用 "?" 替换 "(name)" 。

```
 **示例 3：** 

```
输入：s = "(a)(a)(a)aaa", knowledge = [["a","yes"]]
输出："yesyesyesaaa"
解释：相同的键在 s 中可能会出现多次。
键 "a" 对应的值为 "yes" ，所以将所有的 "(a)" 替换为 "yes" 。
注意，不在括号里的 "a" 不需要被替换。

```
 **示例 4：** 

```
输入：s = "(a)(b)", knowledge = [["a","b"],["b","a"]]
输出："ba"
```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `0 <= knowledge.length <= 10^5` 
-  `knowledge[i].length == 2` 
-  `1 <= key<sub>i</sub>.length, value<sub>i</sub>.length <= 10` 
-  `s`  只包含小写英文字母和圆括号  `'('`  和  `')'`  。
-  `s`  中每一个左圆括号  `'('`  都有对应的右圆括号  `')'`  。
-  `s`  中每对括号内的键都不会为空。
-  `s`  中不会有嵌套括号对。
-  `key<sub>i</sub>`  和  `value<sub>i</sub>`  只包含小写英文字母。
-  `knowledge`  中的  `key<sub>i</sub>`  不会重复。
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 1808.好因子的最大数目
[https://leetcode-cn.com/problems/maximize-number-of-nice-divisors](https://leetcode-cn.com/problems/maximize-number-of-nice-divisors) 
## 原题
给你一个正整数  `primeFactors`  。你需要构造一个正整数  `n`  ，它满足以下条件：
-  `n`  质因数（质因数需要考虑重复的情况）的数目 **不超过 ** `primeFactors`  个。
-  `n`  好因子的数目最大化。如果 `n`  的一个因子可以被 `n`  的每一个质因数整除，我们称这个因子是 **好因子** 。比方说，如果  `n = 12`  ，那么它的质因数为  `[2,2,3]`  ，那么  `6`  和  `12`  是好因子，但  `3` 和  `4`  不是。
请你返回  `n`  的好因子的数目。由于答案可能会很大，请返回答案对  `10^9 + 7`  <b>取余</b> 的结果。

请注意，一个质数的定义是大于 `1`  ，且不能被分解为两个小于该数的自然数相乘。一个数 `n`  的质因子是将 `n`  分解为若干个质因子，且它们的乘积为 `n`  。

 

 **示例 1：** 

```

输入：primeFactors = 5
输出：6
解释：200 是一个可行的 n 。
它有 5 个质因子：[2,2,2,5,5] ，且有 6 个好因子：[10,20,40,50,100,200] 。
不存在别的 n 有至多 5 个质因子，且同时有更多的好因子。

```
 **示例 2：** 

```

输入：primeFactors = 8
输出：18

```
 

 **提示：** 
-  `1 <= primeFactors <= 10^9` 
 
**标签**
`递归` `数学` 


## 
```python

```
>
# 1809.没有广告的剧集
[https://leetcode-cn.com/problems/ad-free-sessions](https://leetcode-cn.com/problems/ad-free-sessions) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1810.隐藏网格下的最小消耗路径
[https://leetcode-cn.com/problems/minimum-path-cost-in-a-hidden-grid](https://leetcode-cn.com/problems/minimum-path-cost-in-a-hidden-grid) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `图` `交互` `堆（优先队列）` 


## 
```python

```
>
# 1811.寻找面试候选人
[https://leetcode-cn.com/problems/find-interview-candidates](https://leetcode-cn.com/problems/find-interview-candidates) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1812.判断国际象棋棋盘中一个格子的颜色
[https://leetcode-cn.com/problems/determine-color-of-a-chessboard-square](https://leetcode-cn.com/problems/determine-color-of-a-chessboard-square) 
## 原题
给你一个坐标  `coordinates`  ，它是一个字符串，表示国际象棋棋盘中一个格子的坐标。下图是国际象棋棋盘示意图。

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/03/chessboard.png" style="width: 400px; height: 396px;" />

如果所给格子的颜色是白色，请你返回  `true` ，如果是黑色，请返回  `false`  。

给定坐标一定代表国际象棋棋盘上一个存在的格子。坐标第一个字符是字母，第二个字符是数字。

 

 **示例 1：** 

```

输入：coordinates = "a1"
输出：false
解释：如上图棋盘所示，"a1" 坐标的格子是黑色的，所以返回 false 。

```
 **示例 2：** 

```

输入：coordinates = "h3"
输出：true
解释：如上图棋盘所示，"h3" 坐标的格子是白色的，所以返回 true 。

```
 **示例 3：** 

```

输入：coordinates = "c7"
输出：false

```
 

 **提示：** 
-  `coordinates.length == 2` 
-  `'a' <= coordinates[0] <= 'h'` 
-  `'1' <= coordinates[1] <= '8'` 
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 1813.句子相似性 III
[https://leetcode-cn.com/problems/sentence-similarity-iii](https://leetcode-cn.com/problems/sentence-similarity-iii) 
## 原题
一个句子是由一些单词与它们之间的单个空格组成，且句子的开头和结尾没有多余空格。比方说， `"Hello World"`  ， `"HELLO"`  ， `"hello world hello world"`  都是句子。每个单词都 **只**  包含大写和小写英文字母。

如果两个句子  `sentence1` 和  `sentence2`  ，可以通过往其中一个句子插入一个任意的句子（ **可以是空句子** ）而得到另一个句子，那么我们称这两个句子是 **相似的**  。比方说， `sentence1 = "Hello my name is Jane"` 且  `sentence2 = "Hello Jane"`  ，我们可以往 `sentence2`  中  `"Hello"` 和  `"Jane"`  之间插入  `"my name is"`  得到 `sentence1`  。

给你两个句子  `sentence1` 和  `sentence2`  ，如果 * * `sentence1` 和 * * `sentence2` 是相似的，请你返回  `true`  ，否则返回  `false`  。

 

 **示例 1：** 

```
输入：sentence1 = "My name is Haley", sentence2 = "My Haley"
输出：true
解释：可以往 sentence2 中 "My" 和 "Haley" 之间插入 "name is" ，得到 sentence1 。

```
 **示例 2：** 

```
输入：sentence1 = "of", sentence2 = "A lot of words"
输出：false
解释：没法往这两个句子中的一个句子只插入一个句子就得到另一个句子。

```
 **示例 3：** 

```
输入：sentence1 = "Eating right now", sentence2 = "Eating"
输出：true
解释：可以往 sentence2 的结尾插入 "right now" 得到 sentence1 。

```
 **示例 4：** 

```
输入：sentence1 = "Luky", sentence2 = "Lucccky"
输出：false

```
 

 **提示：** 
-  `1 <= sentence1.length, sentence2.length <= 100` 
-  `sentence1`  和  `sentence2`  都只包含大小写英文字母和空格。
-  `sentence1`  和  `sentence2`  中的单词都只由单个空格隔开。
 
**标签**
`数组` `双指针` `字符串` 


## 
```python

```
>
# 1814.统计一个数组中好对子的数目
[https://leetcode-cn.com/problems/count-nice-pairs-in-an-array](https://leetcode-cn.com/problems/count-nice-pairs-in-an-array) 
## 原题
给你一个数组  `nums`  ，数组中只包含非负整数。定义  `rev(x)`  的值为将整数  `x`  各个数字位反转得到的结果。比方说  `rev(123) = 321`  ，  `rev(120) = 21`  。我们称满足下面条件的下标对  `(i, j)` 是  **好的**  ：
-  `0 <= i < j < nums.length` 
-  `nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])` 
请你返回好下标对的数目。由于结果可能会很大，请将结果对  `10^9 + 7`  <b>取余</b> 后返回。

 

 **示例 1：** 

```
输入：nums = [42,11,1,97]
输出：2
解释：两个坐标对为：
 - (0,3)：42 + rev(97) = 42 + 79 = 121, 97 + rev(42) = 97 + 24 = 121 。
 - (1,2)：11 + rev(1) = 11 + 1 = 12, 1 + rev(11) = 1 + 11 = 12 。

```
 **示例 2：** 

```
输入：nums = [13,10,35,24,76]
输出：4

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^9` 
 
**标签**
`数组` `哈希表` `数学` `计数` 


## 
```python

```
>
# 1815.得到新鲜甜甜圈的最多组数
[https://leetcode-cn.com/problems/maximum-number-of-groups-getting-fresh-donuts](https://leetcode-cn.com/problems/maximum-number-of-groups-getting-fresh-donuts) 
## 原题
有一个甜甜圈商店，每批次都烤  `batchSize`  个甜甜圈。这个店铺有个规则，就是在烤一批新的甜甜圈时，之前 **所有**  甜甜圈都必须已经全部销售完毕。给你一个整数 `batchSize`  和一个整数数组 `groups`  ，数组中的每个整数都代表一批前来购买甜甜圈的顾客，其中 `groups[i]`  表示这一批顾客的人数。每一位顾客都恰好只要一个甜甜圈。

当有一批顾客来到商店时，他们所有人都必须在下一批顾客来之前购买完甜甜圈。如果一批顾客中第一位顾客得到的甜甜圈不是上一组剩下的，那么这一组人都会很开心。

你可以随意安排每批顾客到来的顺序。请你返回在此前提下， **最多**  有多少组人会感到开心。

 

 **示例 1：** 

```

输入：batchSize = 3, groups = [1,2,3,4,5,6]
输出：4
解释：你可以将这些批次的顾客顺序安排为 [6,2,4,5,1,3] 。那么第 1，2，4，6 组都会感到开心。

```
 **示例 2：** 

```

输入：batchSize = 4, groups = [1,3,2,5,2,2,1,6]
输出：4

```
 

 **提示：** 
-  `1 <= batchSize <= 9` 
-  `1 <= groups.length <= 30` 
-  `1 <= groups[i] <= 10^9` 
 
**标签**
`位运算` `记忆化搜索` `数组` `动态规划` `状态压缩` 


## 
```python

```
>
# 1816.截断句子
[https://leetcode-cn.com/problems/truncate-sentence](https://leetcode-cn.com/problems/truncate-sentence) 
## 原题
 **句子** 是一个单词列表，列表中的单词之间用单个空格隔开，且不存在前导或尾随空格。每个单词仅由大小写英文字母组成（不含标点符号）。
- 例如， `"Hello World"` 、 `"HELLO"` 和 `"hello world hello world"` 都是句子。
给你一个句子 `s` ​​​​​​ 和一个整数 `k` ​​​​​​ ，请你将 `s` ​​ **截断** ​，​​​使截断后的句子仅含 **前** `k` ​​​​​​ 个单词。返回 **截断** `s` ​​​​ *​​* 后得到的句子 *。* 

 

 **示例 1：** 

```
输入：s = "Hello how are you Contestant", k = 4
输出："Hello how are you"
解释：
s 中的单词为 ["Hello", "how" "are", "you", "Contestant"]
前 4 个单词为 ["Hello", "how", "are", "you"]
因此，应当返回 "Hello how are you"

```
 **示例 2：** 

```
输入：s = "What is the solution to this problem", k = 4
输出："What is the solution"
解释：
s 中的单词为 ["What", "is" "the", "solution", "to", "this", "problem"]
前 4 个单词为 ["What", "is", "the", "solution"]
因此，应当返回 "What is the solution"
```
 **示例 3：** 

```
输入：s = "chopper is not a tanuki", k = 5
输出："chopper is not a tanuki"

```
 

 **提示：** 
-  `1 <= s.length <= 500` 
-  `k` 的取值范围是 `[1,  s 中单词的数目]` 
-  `s` 仅由大小写英文字母和空格组成
-  `s` 中的单词之间由单个空格隔开
- 不存在前导或尾随空格
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 1817.查找用户活跃分钟数
[https://leetcode-cn.com/problems/finding-the-users-active-minutes](https://leetcode-cn.com/problems/finding-the-users-active-minutes) 
## 原题
给你用户在 LeetCode 的操作日志，和一个整数 `k` 。日志用一个二维整数数组 `logs` 表示，其中每个 `logs[i] = [ID<sub>i</sub>, time<sub>i</sub>]` 表示 ID 为 `ID<sub>i</sub>` 的用户在 `time<sub>i</sub>` 分钟时执行了某个操作。

 **多个用户** 可以同时执行操作，单个用户可以在同一分钟内执行 **多个操作** 。

指定用户的 **用户活跃分钟数（user active minutes，UAM）** 定义为用户对 LeetCode 执行操作的 **唯一分钟数** 。 即使一分钟内执行多个操作，也只能按一分钟计数。

请你统计用户活跃分钟数的分布情况，统计结果是一个长度为 `k` 且 **下标从 1 开始计数** 的数组 `answer` ，对于每个 `j` （ `1 <= j <= k` ）， `answer[j]` 表示 **用户活跃分钟数** 等于 `j` 的用户数。

返回上面描述的答案数组<i> </i> `answer` <i> </i>。

 

 **示例 1：** 

```

输入：logs = [[0,5],[1,2],[0,2],[0,5],[1,3]], k = 5
输出：[0,2,0,0,0]
解释：
ID=0 的用户执行操作的分钟分别是：5 、2 和 5 。因此，该用户的用户活跃分钟数为 2（分钟 5 只计数一次）
ID=1 的用户执行操作的分钟分别是：2 和 3 。因此，该用户的用户活跃分钟数为 2
2 个用户的用户活跃分钟数都是 2 ，answer[2] 为 2 ，其余 answer[j] 的值都是 0

```
 **示例 2：** 

```

输入：logs = [[1,1],[2,2],[2,3]], k = 4
输出：[1,1,0,0]
解释：
ID=1 的用户仅在分钟 1 执行单个操作。因此，该用户的用户活跃分钟数为 1
ID=2 的用户执行操作的分钟分别是：2 和 3 。因此，该用户的用户活跃分钟数为 2
1 个用户的用户活跃分钟数是 1 ，1 个用户的用户活跃分钟数是 2 
因此，answer[1] = 1 ，answer[2] = 1 ，其余的值都是 0

```
 

 **提示：** 
-  `1 <= logs.length <= 10^4` 
-  `0 <= ID<sub>i</sub> <= 10^9` 
-  `1 <= time<sub>i</sub> <= 10^5` 
-  `k` 的取值范围是 `[用户的最大用户活跃分钟数, 10^5]` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1818.绝对差值和
[https://leetcode-cn.com/problems/minimum-absolute-sum-difference](https://leetcode-cn.com/problems/minimum-absolute-sum-difference) 
## 原题
给你两个正整数数组 `nums1` 和 `nums2` ，数组的长度都是 `n` 。

数组 `nums1` 和 `nums2` 的 **绝对差值和** 定义为所有 `|nums1[i] - nums2[i]|` （ `0 <= i < n` ）的 **总和** （ **下标从 0 开始** ）。

你可以选用 `nums1` 中的 **任意一个** 元素来替换 `nums1` 中的 **至多** 一个元素，以 **最小化** 绝对差值和。

在替换数组 `nums1` 中最多一个元素 **之后** ，返回最小绝对差值和。因为答案可能很大，所以需要对 `10^9 + 7` **取余** 后返回。

 `|x|` 定义为：
- 如果 `x >= 0` ，值为 `x` ，或者
- 如果 `x <= 0` ，值为 `-x` 
 

 **示例 1：** 

```

输入：nums1 = [1,7,5], nums2 = [2,3,5]
输出：3
解释：有两种可能的最优方案：
- 将第二个元素替换为第一个元素：[1,7,5] => [1,1,5] ，或者
- 将第二个元素替换为第三个元素：[1,7,5] => [1,5,5]
两种方案的绝对差值和都是 |1-2| + (|1-3| 或者 |5-3|) + |5-5| = 3

```
 **示例 2：** 

```

输入：nums1 = [2,4,6,8,10], nums2 = [2,4,6,8,10]
输出：0
解释：nums1 和 nums2 相等，所以不用替换元素。绝对差值和为 0

```
 **示例 3** **：** 

```

输入：nums1 = [1,10,4,4,2,7], nums2 = [9,3,5,1,7,4]
输出：20
解释：将第一个元素替换为第二个元素：[1,10,4,4,2,7] => [10,10,4,4,2,7]
绝对差值和为 |10-9| + |10-3| + |4-5| + |4-1| + |2-7| + |7-4| = 20

```
 

 **提示：** 
-  `n == nums1.length` 
-  `n == nums2.length` 
-  `1 <= n <= 10^5` 
-  `1 <= nums1[i], nums2[i] <= 10^5` 
 
**标签**
`数组` `二分查找` `有序集合` `排序` 


## 
```python

```
>
# 1819.序列中不同最大公约数的数目
[https://leetcode-cn.com/problems/number-of-different-subsequences-gcds](https://leetcode-cn.com/problems/number-of-different-subsequences-gcds) 
## 原题
给你一个由正整数组成的数组 `nums` 。

数字序列的 **最大公约数** 定义为序列中所有整数的共有约数中的最大整数。
- 例如，序列 `[4,6,16]` 的最大公约数是 `2` 。
数组的一个 **子序列** 本质是一个序列，可以通过删除数组中的某些元素（或者不删除）得到。
- 例如， `[2,5,10]` 是 `[1,2,1, **2** ,4,1, **5** , **10** ]` 的一个子序列。
计算并返回 `nums` 的所有 **非空** 子序列中 **不同** 最大公约数的 **数目** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/03/image-1.png" />
```

输入：nums = [6,10,3]
输出：5
解释：上图显示了所有的非空子序列与各自的最大公约数。
不同的最大公约数为 6 、10 、3 、2 和 1 。

```
 **示例 2：** 

```

输入：nums = [5,15,40,5,6]
输出：7

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 2 * 10^5` 
 
**标签**
`数组` `数学` `计数` `数论` 


## 
```python

```
>
# 1820.最多邀请的个数
[https://leetcode-cn.com/problems/maximum-number-of-accepted-invitations](https://leetcode-cn.com/problems/maximum-number-of-accepted-invitations) 
## 原题

 
**标签**
`数组` `回溯` `矩阵` 


## 
```python

```
>
# 1821.寻找今年具有正收入的客户
[https://leetcode-cn.com/problems/find-customers-with-positive-revenue-this-year](https://leetcode-cn.com/problems/find-customers-with-positive-revenue-this-year) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1822.数组元素积的符号
[https://leetcode-cn.com/problems/sign-of-the-product-of-an-array](https://leetcode-cn.com/problems/sign-of-the-product-of-an-array) 
## 原题
已知函数  `signFunc(x)` 将会根据 `x` 的正负返回特定值：
- 如果 `x` 是正数，返回 `1` 。
- 如果 `x` 是负数，返回 `-1` 。
- 如果 `x` 是等于 `0` ，返回 `0` 。
给你一个整数数组 `nums` 。令 `product` 为数组 `nums` 中所有元素值的乘积。

返回 `signFunc(product)` 。

 

 **示例 1：** 

```

输入：nums = [-1,-2,-3,-4,3,2,1]
输出：1
解释：数组中所有值的乘积是 144 ，且 signFunc(144) = 1

```
 **示例 2：** 

```

输入：nums = [1,5,0,2,-3]
输出：0
解释：数组中所有值的乘积是 0 ，且 signFunc(0) = 0

```
 **示例 3：** 

```

输入：nums = [-1,1,-1,1,-1]
输出：-1
解释：数组中所有值的乘积是 -1 ，且 signFunc(-1) = -1

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `-100 <= nums[i] <= 100` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 1823.找出游戏的获胜者
[https://leetcode-cn.com/problems/find-the-winner-of-the-circular-game](https://leetcode-cn.com/problems/find-the-winner-of-the-circular-game) 
## 原题
共有 `n` 名小伙伴一起做游戏。小伙伴们围成一圈，按 **顺时针顺序** 从 `1` 到 `n` 编号。确切地说，从第 `i` 名小伙伴顺时针移动一位会到达第 `(i+1)` 名小伙伴的位置，其中 `1 <= i < n` ，从第 `n` 名小伙伴顺时针移动一位会回到第 `1` 名小伙伴的位置。

游戏遵循如下规则：
- 从第 `1` 名小伙伴所在位置 **开始** 。
- 沿着顺时针方向数 `k` 名小伙伴，计数时需要 **包含** 起始时的那位小伙伴。逐个绕圈进行计数，一些小伙伴可能会被数过不止一次。
- 你数到的最后一名小伙伴需要离开圈子，并视作输掉游戏。
- 如果圈子中仍然有不止一名小伙伴，从刚刚输掉的小伙伴的 **顺时针下一位** 小伙伴 **开始** ，回到步骤 `2` 继续执行。
- 否则，圈子中最后一名小伙伴赢得游戏。
给你参与游戏的小伙伴总数 `n` ，和一个整数 `k` ，返回游戏的获胜者。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q2-ex11.png" style="width: 500px; height: 345px;" />
```

输入：n = 5, k = 2
输出：3
解释：游戏运行步骤如下：
1) 从小伙伴 1 开始。
2) 顺时针数 2 名小伙伴，也就是小伙伴 1 和 2 。
3) 小伙伴 2 离开圈子。下一次从小伙伴 3 开始。
4) 顺时针数 2 名小伙伴，也就是小伙伴 3 和 4 。
5) 小伙伴 4 离开圈子。下一次从小伙伴 5 开始。
6) 顺时针数 2 名小伙伴，也就是小伙伴 5 和 1 。
7) 小伙伴 1 离开圈子。下一次从小伙伴 3 开始。
8) 顺时针数 2 名小伙伴，也就是小伙伴 3 和 5 。
9) 小伙伴 5 离开圈子。只剩下小伙伴 3 。所以小伙伴 3 是游戏的获胜者。
```
 **示例 2：** 

```

输入：n = 6, k = 5
输出：1
解释：小伙伴离开圈子的顺序：5、4、6、2、3 。小伙伴 1 是游戏的获胜者。

```
 

 **提示：** 
-  `1 <= k <= n <= 500` 
 
**标签**
`递归` `队列` `数组` `数学` `模拟` 


## 
```python

```
>
# 1824.最少侧跳次数
[https://leetcode-cn.com/problems/minimum-sideway-jumps](https://leetcode-cn.com/problems/minimum-sideway-jumps) 
## 原题
给你一个长度为  `n`  的  **3 跑道道路**  ，它总共包含  `n + 1`  个  **点**  ，编号为  `0`  到  `n`  。一只青蛙从  `0`  号点第二条跑道  **出发**  ，它想要跳到点  `n`  处。然而道路上可能有一些障碍。

给你一个长度为 `n + 1`  的数组  `obstacles`  ，其中  `obstacles[i]`  （<b>取值范围从 0 到 3</b>）表示在点 `i`  处的  `obstacles[i]`  跑道上有一个障碍。如果  `obstacles[i] == 0`  ，那么点  `i`  处没有障碍。任何一个点的三条跑道中  **最多有一个**  障碍。
- 比方说，如果  `obstacles[2] == 1`  ，那么说明在点 2 处跑道 1 有障碍。
这只青蛙从点 `i`  跳到点 `i + 1`  且跑道不变的前提是点 `i + 1`  的同一跑道上没有障碍。为了躲避障碍，这只青蛙也可以在  **同一个**  点处  **侧跳**  到 **另外一条**  跑道（这两条跑道可以不相邻），但前提是跳过去的跑道该点处没有障碍。
- 比方说，这只青蛙可以从点 3 处的跑道 3 跳到点 3 处的跑道 1 。
这只青蛙从点 0 处跑道 `2`  出发，并想到达点 `n`  处的 **任一跑道** ，请你返回 **最少侧跳次数**  。

 **注意** ：点 `0`  处和点 `n`  处的任一跑道都不会有障碍。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q3-ex1.png" style="width: 500px; height: 244px;" />
```

输入：obstacles = [0,1,2,3,0]
输出：2 
解释：最优方案如上图箭头所示。总共有 2 次侧跳（红色箭头）。
注意，这只青蛙只有当侧跳时才可以跳过障碍（如上图点 2 处所示）。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q3-ex2.png" style="width: 500px; height: 196px;" />
```

输入：obstacles = [0,1,1,3,3,0]
输出：0
解释：跑道 2 没有任何障碍，所以不需要任何侧跳。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/ic234-q3-ex3.png" style="width: 500px; height: 196px;" />
```

输入：obstacles = [0,2,1,0,3,0]
输出：2
解释：最优方案如上图所示。总共有 2 次侧跳。

```
 

 **提示：** 
-  `obstacles.length == n + 1` 
-  `1 <= n <= 5 * 10^5` 
-  `0 <= obstacles[i] <= 3` 
-  `obstacles[0] == obstacles[n] == 0` 
 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 1825.求出 MK 平均值
[https://leetcode-cn.com/problems/finding-mk-average](https://leetcode-cn.com/problems/finding-mk-average) 
## 原题
给你两个整数  `m`  和  `k`  ，以及数据流形式的若干整数。你需要实现一个数据结构，计算这个数据流的 <b>MK 平均值</b> 。

 **MK 平均值**  按照如下步骤计算：
- 如果数据流中的整数少于 `m`  个， **MK 平均值**  为 `-1`  ，否则将数据流中最后 `m`  个元素拷贝到一个独立的容器中。
- 从这个容器中删除最小的 `k`  个数和最大的 `k`  个数。
- 计算剩余元素的平均值，并 **向下取整到最近的整数**  。
请你实现  `MKAverage`  类：
-  `MKAverage(int m, int k)`  用一个空的数据流和两个整数 `m`  和 `k`  初始化  **MKAverage**  对象。
-  `void addElement(int num)`  往数据流中插入一个新的元素  `num`  。
-  `int calculateMKAverage()`  对当前的数据流计算并返回 **MK 平均数**  ，结果需 **向下取整到最近的整数** 。
 

 **示例 1：** 

```

输入：
["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement", "calculateMKAverage", "addElement", "addElement", "addElement", "calculateMKAverage"]
[[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
输出：
[null, null, null, -1, null, 3, null, null, null, 5]

解释：
MKAverage obj = new MKAverage(3, 1); 
obj.addElement(3);        // 当前元素为 [3]
obj.addElement(1);        // 当前元素为 [3,1]
obj.calculateMKAverage(); // 返回 -1 ，因为 m = 3 ，但数据流中只有 2 个元素
obj.addElement(10);       // 当前元素为 [3,1,10]
obj.calculateMKAverage(); // 最后 3 个元素为 [3,1,10]
                          // 删除最小以及最大的 1 个元素后，容器为 [3]
                          // [3] 的平均值等于 3/1 = 3 ，故返回 3
obj.addElement(5);        // 当前元素为 [3,1,10,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5]
obj.addElement(5);        // 当前元素为 [3,1,10,5,5,5]
obj.calculateMKAverage(); // 最后 3 个元素为 [5,5,5]
                          // 删除最小以及最大的 1 个元素后，容器为 [5]
                          // [5] 的平均值等于 5/1 = 5 ，故返回 5

```
 

 **提示：** 
-  `3 <= m <= 10^5` 
-  `1 <= k*2 < m` 
-  `1 <= num <= 10^5` 
-  `addElement` 与  `calculateMKAverage`  总操作次数不超过 `10^5` 次。
 
**标签**
`设计` `队列` `有序集合` `堆（优先队列）` 


## 
```python

```
>
# 1826.有缺陷的传感器
[https://leetcode-cn.com/problems/faulty-sensor](https://leetcode-cn.com/problems/faulty-sensor) 
## 原题

 
**标签**
`数组` `双指针` 


## 
```python

```
>
# 1827.最少操作使数组递增
[https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-increasing](https://leetcode-cn.com/problems/minimum-operations-to-make-the-array-increasing) 
## 原题
给你一个整数数组  `nums`  （ **下标从 0 开始** ）。每一次操作中，你可以选择数组中一个元素，并将它增加  `1`  。
- 比方说，如果  `nums = [1,2,3]`  ，你可以选择增加  `nums[1]`  得到  `nums = [1,<b>3</b>,3]`  。
请你返回使 `nums`   **严格递增**  的 **最少**  操作次数。

我们称数组  `nums`  是 **严格递增的**  ，当它满足对于所有的  `0 <= i < nums.length - 1`  都有  `nums[i] < nums[i+1]`  。一个长度为 `1`  的数组是严格递增的一种特殊情况。

 

 **示例 1：** 

```
输入：nums = [1,1,1]
输出：3
解释：你可以进行如下操作：
1) 增加 nums[2] ，数组变为 [1,1,2] 。
2) 增加 nums[1] ，数组变为 [1,2,2] 。
3) 增加 nums[2] ，数组变为 [1,2,3] 。

```
 **示例 2：** 

```
输入：nums = [1,5,2,4,1]
输出：14

```
 **示例 3：** 

```
输入：nums = [8]
输出：0

```
 

 **提示：** 
-  `1 <= nums.length <= 5000` 
-  `1 <= nums[i] <= 10^4` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1828.统计一个圆中点的数目
[https://leetcode-cn.com/problems/queries-on-number-of-points-inside-a-circle](https://leetcode-cn.com/problems/queries-on-number-of-points-inside-a-circle) 
## 原题
给你一个数组  `points`  ，其中  `points[i] = [x<sub>i</sub>, y<sub>i</sub>]`  ，表示第  `i`  个点在二维平面上的坐标。多个点可能会有 **相同**  的坐标。

同时给你一个数组  `queries`  ，其中  `queries[j] = [x<sub>j</sub>, y<sub>j</sub>, r<sub>j</sub>]`  ，表示一个圆心在  `(x<sub>j</sub>, y<sub>j</sub>)`  且半径为  `r<sub>j</sub>` <sub> </sub>的圆。

对于每一个查询  `queries[j]`  ，计算在第 `j`  个圆 **内**  点的数目。如果一个点在圆的 **边界上**  ，我们同样认为它在圆  **内**  。

请你返回一个数组 * * `answer`  ，其中 * * `answer[j]` 是第  `j`  个查询的答案。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/chrome_2021-03-25_22-34-16.png" style="width: 500px; height: 418px;">
```
输入：points = [[1,3],[3,3],[5,3],[2,2]], queries = [[2,3,1],[4,3,1],[1,1,2]]
输出：[3,2,2]
解释：所有的点和圆如上图所示。
queries[0] 是绿色的圆，queries[1] 是红色的圆，queries[2] 是蓝色的圆。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/25/chrome_2021-03-25_22-42-07.png" style="width: 500px; height: 390px;">
```
输入：points = [[1,1],[2,2],[3,3],[4,4],[5,5]], queries = [[1,2,2],[2,2,2],[4,3,2],[4,3,3]]
输出：[2,3,2,4]
解释：所有的点和圆如上图所示。
queries[0] 是绿色的圆，queries[1] 是红色的圆，queries[2] 是蓝色的圆，queries[3] 是紫色的圆。

```
 

 **提示：** 
-  `1 <= points.length <= 500` 
-  `points[i].length == 2` 
-  `0 <= x<sub>​​​​​​i</sub>, y<sub>​​​​​​i</sub> <= 500` 
-  `1 <= queries.length <= 500` 
-  `queries[j].length == 3` 
-  `0 <= x<sub>j</sub>, y<sub>j</sub> <= 500` 
-  `1 <= r<sub>j</sub> <= 500` 
- 所有的坐标都是整数。
 
**标签**
`几何` `数组` `数学` 


## 
```python

```
>
# 1829.每个查询的最大异或值
[https://leetcode-cn.com/problems/maximum-xor-for-each-query](https://leetcode-cn.com/problems/maximum-xor-for-each-query) 
## 原题
给你一个 **有序**  数组  `nums`  ，它由  `n`  个非负整数组成，同时给你一个整数  `maximumBit`  。你需要执行以下查询 `n`  次：
- 找到一个非负整数  `k < 2^maximumBit`  ，使得  `nums[0] XOR nums[1] XOR ... XOR nums[nums.length-1] XOR k`  的结果 **最大化**  。 `k`  是第 `i`  个查询的答案。
- 从当前数组  `nums`  删除  **最后**  一个元素。
请你返回一个数组  `answer`  ，其中 * * `answer[i]` 是第  `i`  个查询的结果。

 

 **示例 1：** 

```

输入：nums = [0,1,1,3], maximumBit = 2
输出：[0,3,2,3]
解释：查询的答案如下：
第一个查询：nums = [0,1,1,3]，k = 0，因为 0 XOR 1 XOR 1 XOR 3 XOR 0 = 3 。
第二个查询：nums = [0,1,1]，k = 3，因为 0 XOR 1 XOR 1 XOR 3 = 3 。
第三个查询：nums = [0,1]，k = 2，因为 0 XOR 1 XOR 2 = 3 。
第四个查询：nums = [0]，k = 3，因为 0 XOR 3 = 3 。

```
 **示例 2：** 

```

输入：nums = [2,3,4,7], maximumBit = 3
输出：[5,2,6,5]
解释：查询的答案如下：
第一个查询：nums = [2,3,4,7]，k = 5，因为 2 XOR 3 XOR 4 XOR 7 XOR 5 = 7。
第二个查询：nums = [2,3,4]，k = 2，因为 2 XOR 3 XOR 4 XOR 2 = 7 。
第三个查询：nums = [2,3]，k = 6，因为 2 XOR 3 XOR 6 = 7 。
第四个查询：nums = [2]，k = 5，因为 2 XOR 5 = 7 。

```
 **示例 3：** 

```

输入：nums = [0,1,2,2,5,7], maximumBit = 3
输出：[4,3,6,4,6,7]

```
 

 **提示：** 
-  `nums.length == n` 
-  `1 <= n <= 10^5` 
-  `1 <= maximumBit <= 20` 
-  `0 <= nums[i] < 2^maximumBit` 
-  `nums` ​​​ 中的数字已经按  **升序**  排好序。
 
**标签**
`位运算` `数组` `前缀和` 


## 
```python

```
>
# 1830.使字符串有序的最少操作次数
[https://leetcode-cn.com/problems/minimum-number-of-operations-to-make-string-sorted](https://leetcode-cn.com/problems/minimum-number-of-operations-to-make-string-sorted) 
## 原题
给你一个字符串  `s`  （ **下标从 0 开始** ）。你需要对 `s`  执行以下操作直到它变为一个有序字符串：
- 找到 **最大下标**   `i`  ，使得  `1 <= i < s.length` 且  `s[i] < s[i - 1]`  。
- 找到 **最大下标**   `j`  ，使得  `i <= j < s.length` 且对于所有在闭区间  `[i, j]`  之间的  `k`  都有  `s[k] < s[i - 1]`  。
- 交换下标为  `i - 1` ​​​​ 和  `j` ​​​​ 处的两个字符。
- 将下标 `i`  开始的字符串后缀反转。
请你返回将字符串变成有序的最少操作次数。由于答案可能会很大，请返回它对  `10^9 + 7`   **取余**  的结果。

 

 **示例 1：** 

```
输入：s = "cba"
输出：5
解释：模拟过程如下所示：
操作 1：i=2，j=2。交换 s[1] 和 s[2] 得到 s="cab" ，然后反转下标从 2 开始的后缀字符串，得到 s="cab" 。
操作 2：i=1，j=2。交换 s[0] 和 s[2] 得到 s="bac" ，然后反转下标从 1 开始的后缀字符串，得到 s="bca" 。
操作 3：i=2，j=2。交换 s[1] 和 s[2] 得到 s="bac" ，然后反转下标从 2 开始的后缀字符串，得到 s="bac" 。
操作 4：i=1，j=1。交换 s[0] 和 s[1] 得到 s="abc" ，然后反转下标从 1 开始的后缀字符串，得到 s="acb" 。
操作 5：i=2，j=2。交换 s[1] 和 s[2] 得到 s="abc" ，然后反转下标从 2 开始的后缀字符串，得到 s="abc" 。

```
 **示例 2：** 

```
输入：s = "aabaa"
输出：2
解释：模拟过程如下所示：
操作 1：i=3，j=4。交换 s[2] 和 s[4] 得到 s="aaaab" ，然后反转下标从 3 开始的后缀字符串，得到 s="aaaba" 。
操作 2：i=4，j=4。交换 s[3] 和 s[4] 得到 s="aaaab" ，然后反转下标从 4 开始的后缀字符串，得到 s="aaaab" 。

```
 **示例 3：** 

```
输入：s = "cdbea"
输出：63
```
 **示例 4：** 

```
输入：s = "leetcodeleetcodeleetcode"
输出：982157772

```
 

 **提示：** 
-  `1 <= s.length <= 3000` 
-  `s` ​ 只包含小写英文字母。
 
**标签**
`数学` `字符串` `组合数学` 


## 
```python

```
>
# 1831.每天的最大交易
[https://leetcode-cn.com/problems/maximum-transaction-each-day](https://leetcode-cn.com/problems/maximum-transaction-each-day) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1832.判断句子是否为全字母句
[https://leetcode-cn.com/problems/check-if-the-sentence-is-pangram](https://leetcode-cn.com/problems/check-if-the-sentence-is-pangram) 
## 原题
 **全字母句** 指包含英语字母表中每个字母至少一次的句子。

给你一个仅由小写英文字母组成的字符串 `sentence` ，请你判断  `sentence` 是否为 **全字母句** 。

如果是，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：sentence = "thequickbrownfoxjumpsoverthelazydog"
输出：true
解释：sentence 包含英语字母表中每个字母至少一次。

```
 **示例 2：** 

```

输入：sentence = "leetcode"
输出：false

```
 

 **提示：** 
-  `1 <= sentence.length <= 1000` 
-  `sentence` 由小写英语字母组成
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1833.雪糕的最大数量
[https://leetcode-cn.com/problems/maximum-ice-cream-bars](https://leetcode-cn.com/problems/maximum-ice-cream-bars) 
## 原题
夏日炎炎，小男孩 Tony 想买一些雪糕消消暑。

商店中新到 `n` 支雪糕，用长度为 `n` 的数组 `costs` 表示雪糕的定价，其中 `costs[i]` 表示第 `i` 支雪糕的现金价格。Tony 一共有 `coins` 现金可以用于消费，他想要买尽可能多的雪糕。

给你价格数组 `costs` 和现金量 `coins` ，请你计算并返回 Tony 用 `coins` 现金能够买到的雪糕的 **最大数量** 。

 **注意：** Tony 可以按任意顺序购买雪糕。

 

 **示例 1：** 

```
输入：costs = [1,3,2,4,1], coins = 7
输出：4
解释：Tony 可以买下标为 0、1、2、4 的雪糕，总价为 1 + 3 + 2 + 1 = 7

```
 **示例 2：** 

```
输入：costs = [10,6,8,7,7,8], coins = 5
输出：0
解释：Tony 没有足够的钱买任何一支雪糕。

```
 **示例 3：** 

```
输入：costs = [1,6,3,1,2,5], coins = 20
输出：6
解释：Tony 可以买下所有的雪糕，总价为 1 + 6 + 3 + 1 + 2 + 5 = 18 。

```
 

 **提示：** 
-  `costs.length == n` 
-  `1 <= n <= 10^5` 
-  `1 <= costs[i] <= 10^5` 
-  `1 <= coins <= 10^8` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1834.单线程 CPU
[https://leetcode-cn.com/problems/single-threaded-cpu](https://leetcode-cn.com/problems/single-threaded-cpu) 
## 原题
给你一个二维数组 `tasks` ，用于表示 `n` ​​​​​​ 项从 `0` 到 `n - 1` 编号的任务。其中 `tasks[i] = [enqueueTime<sub>i</sub>, processingTime<sub>i</sub>]` 意味着第 `i^​​​​​​` ​​​​ 项任务将会于 `enqueueTime<sub>i</sub>` 时进入任务队列，需要 `processingTime<sub>i</sub>` <sub> </sub>的时长完成执行。

现有一个单线程 CPU ，同一时间只能执行 **最多一项** 任务，该 CPU 将会按照下述方式运行：
- 如果 CPU 空闲，且任务队列中没有需要执行的任务，则 CPU 保持空闲状态。
- 如果 CPU 空闲，但任务队列中有需要执行的任务，则 CPU 将会选择 **执行时间最短** 的任务开始执行。如果多个任务具有同样的最短执行时间，则选择下标最小的任务开始执行。
- 一旦某项任务开始执行，CPU 在 **执行完整个任务** 前都不会停止。
- CPU 可以在完成一项任务后，立即开始执行一项新任务。
返回CPU处理任务的顺序。

 

 **示例 1：** 

```
输入：tasks = [[1,2],[2,4],[3,2],[4,1]]
输出：[0,2,3,1]
解释：事件按下述流程运行： 
- time = 1 ，任务 0 进入任务队列，可执行任务项 = {0}
- 同样在 time = 1 ，空闲状态的 CPU 开始执行任务 0 ，可执行任务项 = {}
- time = 2 ，任务 1 进入任务队列，可执行任务项 = {1}
- time = 3 ，任务 2 进入任务队列，可执行任务项 = {1, 2}
- 同样在 time = 3 ，CPU 完成任务 0 并开始执行队列中用时最短的任务 2 ，可执行任务项 = {1}
- time = 4 ，任务 3 进入任务队列，可执行任务项 = {1, 3}
- time = 5 ，CPU 完成任务 2 并开始执行队列中用时最短的任务 3 ，可执行任务项 = {1}
- time = 6 ，CPU 完成任务 3 并开始执行任务 1 ，可执行任务项 = {}
- time = 10 ，CPU 完成任务 1 并进入空闲状态

```
 **示例 2：** 

```
输入：tasks = [[7,10],[7,12],[7,5],[7,4],[7,2]]
输出：[4,3,2,0,1]
解释：事件按下述流程运行： 
- time = 7 ，所有任务同时进入任务队列，可执行任务项  = {0,1,2,3,4}
- 同样在 time = 7 ，空闲状态的 CPU 开始执行任务 4 ，可执行任务项 = {0,1,2,3}
- time = 9 ，CPU 完成任务 4 并开始执行任务 3 ，可执行任务项 = {0,1,2}
- time = 13 ，CPU 完成任务 3 并开始执行任务 2 ，可执行任务项 = {0,1}
- time = 18 ，CPU 完成任务 2 并开始执行任务 0 ，可执行任务项 = {1}
- time = 28 ，CPU 完成任务 0 并开始执行任务 1 ，可执行任务项 = {}
- time = 40 ，CPU 完成任务 1 并进入空闲状态
```
 

 **提示：** 
-  `tasks.length == n` 
-  `1 <= n <= 10^5` 
-  `1 <= enqueueTime<sub>i</sub>, processingTime<sub>i</sub> <= 10^9` 
 
**标签**
`数组` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1835.所有数对按位与结果的异或和
[https://leetcode-cn.com/problems/find-xor-sum-of-all-pairs-bitwise-and](https://leetcode-cn.com/problems/find-xor-sum-of-all-pairs-bitwise-and) 
## 原题
列表的 **异或和** （ **XOR sum** ）指对所有元素进行按位 `XOR` 运算的结果。如果列表中仅有一个元素，那么其 **异或和** 就等于该元素。
- 例如， `[1,2,3,4]` 的 **异或和** 等于 `1 XOR 2 XOR 3 XOR 4 = 4` ，而 `[3]` 的 **异或和** 等于 `3` 。
给你两个下标 **从 0 开始** 计数的数组 `arr1` 和 `arr2` ，两数组均由非负整数组成。

根据每个  `(i, j)` 数对，构造一个由 `arr1[i] AND arr2[j]` （按位 `AND` 运算）结果组成的列表。其中 `0 <= i < arr1.length` 且 `0 <= j < arr2.length` 。

返回上述列表的 **异或和** 。

 

 **示例 1：** 

```
输入：arr1 = [1,2,3], arr2 = [6,5]
输出：0
解释：列表 = [1 AND 6, 1 AND 5, 2 AND 6, 2 AND 5, 3 AND 6, 3 AND 5] = [0,1,2,0,2,1] ，
异或和 = 0 XOR 1 XOR 2 XOR 0 XOR 2 XOR 1 = 0 。
```
 **示例 2：** 

```
输入：arr1 = [12], arr2 = [4]
输出：4
解释：列表 = [12 AND 4] = [4] ，异或和 = 4 。

```
 

 **提示：** 
-  `1 <= arr1.length, arr2.length <= 10^5` 
-  `0 <= arr1[i], arr2[j] <= 10^9` 
 
**标签**
`位运算` `数组` `数学` 


## 
```python

```
>
# 1836.从未排序的链表中移除重复元素
[https://leetcode-cn.com/problems/remove-duplicates-from-an-unsorted-linked-list](https://leetcode-cn.com/problems/remove-duplicates-from-an-unsorted-linked-list) 
## 原题

 
**标签**
`哈希表` `链表` 


## 
```python

```
>
# 1837.K 进制表示下的各位数字总和
[https://leetcode-cn.com/problems/sum-of-digits-in-base-k](https://leetcode-cn.com/problems/sum-of-digits-in-base-k) 
## 原题
给你一个整数 `n` （ `10` 进制）和一个基数 `k` ，请你将 `n` 从 `10` 进制表示转换为 `k` 进制表示，计算并返回转换后各位数字的 **总和** 。

转换后，各位数字应当视作是 `10` 进制数字，且它们的总和也应当按 `10` 进制表示返回。

 

 **示例 1：** 

```

输入：n = 34, k = 6
输出：9
解释：34 (10 进制) 在 6 进制下表示为 54 。5 + 4 = 9 。

```
 **示例 2：** 

```

输入：n = 10, k = 10
输出：1
解释：n 本身就是 10 进制。 1 + 0 = 1 。

```
 

 **提示：** 
-  `1 <= n <= 100` 
-  `2 <= k <= 10` 
 
**标签**
`数学` 


## 
```python

```
>
# 1838.最高频元素的频数
[https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element](https://leetcode-cn.com/problems/frequency-of-the-most-frequent-element) 
## 原题
元素的 **频数** 是该元素在一个数组中出现的次数。

给你一个整数数组 `nums` 和一个整数 `k` 。在一步操作中，你可以选择 `nums` 的一个下标，并将该下标对应元素的值增加 `1` 。

执行最多 `k` 次操作后，返回数组中最高频元素的 **最大可能频数** *。* 

 

 **示例 1：** 

```

输入：nums = [1,2,4], k = 5
输出：3
解释：对第一个元素执行 3 次递增操作，对第二个元素执 2 次递增操作，此时 nums = [4,4,4] 。
4 是数组中最高频元素，频数是 3 。
```
 **示例 2：** 

```

输入：nums = [1,4,8,13], k = 5
输出：2
解释：存在多种最优解决方案：
- 对第一个元素执行 3 次递增操作，此时 nums = [4,4,8,13] 。4 是数组中最高频元素，频数是 2 。
- 对第二个元素执行 4 次递增操作，此时 nums = [1,8,8,13] 。8 是数组中最高频元素，频数是 2 。
- 对第三个元素执行 5 次递增操作，此时 nums = [1,4,13,13] 。13 是数组中最高频元素，频数是 2 。

```
 **示例 3：** 

```

输入：nums = [3,9,6], k = 2
输出：1

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^5` 
-  `1 <= k <= 10^5` 
 
**标签**
`数组` `二分查找` `前缀和` `滑动窗口` 


## 
```python

```
>
# 1839.所有元音按顺序排布的最长子字符串
[https://leetcode-cn.com/problems/longest-substring-of-all-vowels-in-order](https://leetcode-cn.com/problems/longest-substring-of-all-vowels-in-order) 
## 原题
当一个字符串满足如下条件时，我们称它是 <b>美丽的</b> ：
- 所有 5 个英文元音字母（ `'a'`  ， `'e'`  ， `'i'`  ， `'o'`  ， `'u'` ）都必须  **至少**  出现一次。
- 这些元音字母的顺序都必须按照 **字典序**  升序排布（也就是说所有的 `'a'`  都在 `'e'`  前面，所有的 `'e'`  都在 `'i'`  前面，以此类推）
比方说，字符串  `"aeiou"` 和  `"aaaaaaeiiiioou"`  都是 **美丽的**  ，但是  `"uaeio"`  ， `"aeoiu"`  和  `"aaaeeeooo"`   **不是美丽的**  。

给你一个只包含英文元音字母的字符串  `word`  ，请你返回  `word` 中 **最长美丽子字符串的长度**  。如果不存在这样的子字符串，请返回 `0`  。

 **子字符串** 是字符串中一个连续的字符序列。

 

 **示例 1：** 

```

输入：word = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
输出：13
解释：最长子字符串是 "aaaaeiiiiouuu" ，长度为 13 。
```
 **示例 2：** 

```

输入：word = "aeeeiiiioooauuuaeiou"
输出：5
解释：最长子字符串是 "aeiou" ，长度为 5 。

```
 **示例 3：** 

```

输入：word = "a"
输出：0
解释：没有美丽子字符串，所以返回 0 。

```
 

 **提示：** 
-  `1 <= word.length <= 5 * 10^5` 
-  `word`  只包含字符  `'a'` ， `'e'` ， `'i'` ， `'o'`  和  `'u'`  。
 
**标签**
`字符串` `滑动窗口` 


## 
```python

```
>
# 1840.最高建筑高度
[https://leetcode-cn.com/problems/maximum-building-height](https://leetcode-cn.com/problems/maximum-building-height) 
## 原题
在一座城市里，你需要建  `n`  栋新的建筑。这些新的建筑会从 `1`  到 `n`  编号排成一列。

这座城市对这些新建筑有一些规定：
- 每栋建筑的高度必须是一个非负整数。
- 第一栋建筑的高度 **必须**  是  `0`  。
- 任意两栋相邻建筑的高度差 **不能超过**    `1`  。
除此以外，某些建筑还有额外的最高高度限制。这些限制会以二维整数数组  `restrictions`  的形式给出，其中  `restrictions[i] = [id<sub>i</sub>, maxHeight<sub>i</sub>]`  ，表示建筑  `id<sub>i</sub>`  的高度 **不能超过**   `maxHeight<sub>i</sub>`  。

题目保证每栋建筑在 `restrictions`  中 ** 至多出现一次**  ，同时建筑 `1`   **不会**  出现在  `restrictions`  中。

请你返回 **最高**  建筑能达到的 **最高高度**  。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/25/ic236-q4-ex1-1.png" style="width: 400px; height: 253px;" />
```

输入：n = 5, restrictions = [[2,1],[4,1]]
输出：2
解释：上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,1,2] ，最高建筑的高度为 2 。
```
 **示例 2：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/25/ic236-q4-ex2.png" style="width: 500px; height: 269px;" />
```

输入：n = 6, restrictions = []
输出：5
解释：上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,3,4,5] ，最高建筑的高度为 5 。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/25/ic236-q4-ex3.png" style="width: 500px; height: 187px;" />
```

输入：n = 10, restrictions = [[5,3],[2,5],[7,4],[10,3]]
输出：5
解释：上图中的绿色区域为每栋建筑被允许的最高高度。
我们可以使建筑高度分别为 [0,1,2,3,3,4,4,5,4,3] ，最高建筑的高度为 5 。

```
 

 **提示：** 
-  `2 <= n <= 10^9` 
-  `0 <= restrictions.length <= min(n - 1, 10^5)` 
-  `2 <= id<sub>i</sub> <= n` 
-  `id<sub>i</sub>`  是 **唯一的**  。
-  `0 <= maxHeight<sub>i</sub> <= 10^9` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 1841.联赛信息统计
[https://leetcode-cn.com/problems/league-statistics](https://leetcode-cn.com/problems/league-statistics) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1842.下个由相同数字构成的回文串
[https://leetcode-cn.com/problems/next-palindrome-using-same-digits](https://leetcode-cn.com/problems/next-palindrome-using-same-digits) 
## 原题

 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 1843.可疑银行账户
[https://leetcode-cn.com/problems/suspicious-bank-accounts](https://leetcode-cn.com/problems/suspicious-bank-accounts) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1844.将所有数字用字符替换
[https://leetcode-cn.com/problems/replace-all-digits-with-characters](https://leetcode-cn.com/problems/replace-all-digits-with-characters) 
## 原题
给你一个下标从 **0**  开始的字符串 `s`  ，它的 **偶数** 下标处为小写英文字母， **奇数**  下标处为数字。

定义一个函数  `shift(c, x)`  ，其中  `c`  是一个字符且  `x`  是一个数字，函数返回字母表中  `c`  后面第 `x`  个字符。
- 比方说， `shift('a', 5) = 'f'`  和  `shift('x', 0) = 'x'`  。
对于每个 **奇数**  下标  `i`  ，你需要将数字  `s[i]` 用  `shift(s[i-1], s[i])`  替换。

请你替换所有数字以后，将字符串 `s`  返回。题目 **保证** * * `shift(s[i-1], s[i])`  不会超过 `'z'`  。

 

 **示例 1：** 

```
输入：s = "a1c1e1"
输出："abcdef"
解释：数字被替换结果如下：
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('c',1) = 'd'
- s[5] -> shift('e',1) = 'f'
```
 **示例 2：** 

```
输入：s = "a1b2c3d4e"
输出："abbdcfdhe"
解释：数字被替换结果如下：
- s[1] -> shift('a',1) = 'b'
- s[3] -> shift('b',2) = 'd'
- s[5] -> shift('c',3) = 'f'
- s[7] -> shift('d',4) = 'h'
```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `s`  只包含小写英文字母和数字。
- 对所有 **奇数** 下标处的  `i`  ，满足  `shift(s[i-1], s[i]) <= 'z'`  。
 
**标签**
`字符串` 


## 
```python

```
>
# 1845.座位预约管理系统
[https://leetcode-cn.com/problems/seat-reservation-manager](https://leetcode-cn.com/problems/seat-reservation-manager) 
## 原题
请你设计一个管理 `n`  个座位预约的系统，座位编号从  `1`  到  `n`  。

请你实现  `SeatManager`  类：
-  `SeatManager(int n)`  初始化一个  `SeatManager`  对象，它管理从 `1`  到 `n`  编号的  `n`  个座位。所有座位初始都是可预约的。
-  `int reserve()`  返回可以预约座位的  **最小编号**  ，此座位变为不可预约。
-  `void unreserve(int seatNumber)`  将给定编号  `seatNumber`  对应的座位变成可以预约。
 

 **示例 1：** 

```
输入：
["SeatManager", "reserve", "reserve", "unreserve", "reserve", "reserve", "reserve", "reserve", "unreserve"]
[[5], [], [], [2], [], [], [], [], [5]]
输出：
[null, 1, 2, null, 2, 3, 4, 5, null]

解释：
SeatManager seatManager = new SeatManager(5); // 初始化 SeatManager ，有 5 个座位。
seatManager.reserve();    // 所有座位都可以预约，所以返回最小编号的座位，也就是 1 。
seatManager.reserve();    // 可以预约的座位为 [2,3,4,5] ，返回最小编号的座位，也就是 2 。
seatManager.unreserve(2); // 将座位 2 变为可以预约，现在可预约的座位为 [2,3,4,5] 。
seatManager.reserve();    // 可以预约的座位为 [2,3,4,5] ，返回最小编号的座位，也就是 2 。
seatManager.reserve();    // 可以预约的座位为 [3,4,5] ，返回最小编号的座位，也就是 3 。
seatManager.reserve();    // 可以预约的座位为 [4,5] ，返回最小编号的座位，也就是 4 。
seatManager.reserve();    // 唯一可以预约的是座位 5 ，所以返回 5 。
seatManager.unreserve(5); // 将座位 5 变为可以预约，现在可预约的座位为 [5] 。

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `1 <= seatNumber <= n` 
- 每一次对  `reserve`  的调用，题目保证至少存在一个可以预约的座位。
- 每一次对  `unreserve`  的调用，题目保证  `seatNumber`  在调用函数前都是被预约状态。
- 对  `reserve` 和  `unreserve`  的调用  **总共**  不超过  `10^5`  次。
 
**标签**
`设计` `堆（优先队列）` 


## 
```python

```
>
# 1846.减小和重新排列数组后的最大元素
[https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging](https://leetcode-cn.com/problems/maximum-element-after-decreasing-and-rearranging) 
## 原题
给你一个正整数数组  `arr`  。请你对 `arr`  执行一些操作（也可以不进行任何操作），使得数组满足以下条件：
-  `arr`  中 **第一个**  元素必须为  `1`  。
- 任意相邻两个元素的差的绝对值 **小于等于**   `1`  ，也就是说，对于任意的 `1 <= i < arr.length`  （ **数组下标从 0 开始** ），都满足  `abs(arr[i] - arr[i - 1]) <= 1`  。 `abs(x)`  为  `x`  的绝对值。
你可以执行以下 2 种操作任意次：
-  **减小** `arr`  中任意元素的值，使其变为一个 **更小的正整数**  。
-  **重新排列**   `arr`  中的元素，你可以以任意顺序重新排列。
请你返回执行以上操作后，在满足前文所述的条件下， `arr`  中可能的 **最大值**  。

 

 **示例 1：** 

```

输入：arr = [2,2,1,2,1]
输出：2
解释：
我们可以重新排列 arr 得到 [1,2,2,2,1] ，该数组满足所有条件。
arr 中最大元素为 2 。

```
 **示例 2：** 

```

输入：arr = [100,1,1000]
输出：3
解释：
一个可行的方案如下：
1. 重新排列 arr 得到 [1,100,1000] 。
2. 将第二个元素减小为 2 。
3. 将第三个元素减小为 3 。
现在 arr = [1,2,3] ，满足所有条件。
arr 中最大元素为 3 。

```
 **示例 3：** 

```

输入：arr = [1,2,3,4,5]
输出：5
解释：数组已经满足所有条件，最大元素为 5 。

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `1 <= arr[i] <= 10^9` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1847.最近的房间
[https://leetcode-cn.com/problems/closest-room](https://leetcode-cn.com/problems/closest-room) 
## 原题
一个酒店里有  `n`  个房间，这些房间用二维整数数组  `rooms`  表示，其中  `rooms[i] = [roomId<sub>i</sub>, size<sub>i</sub>]`  表示有一个房间号为  `roomId<sub>i</sub>`  的房间且它的面积为  `size<sub>i</sub>`  。每一个房间号  `roomId<sub>i</sub>`  保证是 **独一无二**  的。

同时给你 `k`  个查询，用二维数组  `queries`  表示，其中  `queries[j] = [preferred<sub>j</sub>, minSize<sub>j</sub>]`  。第  `j`  个查询的答案是满足如下条件的房间  `id`  ：
- 房间的面积 <b>至少</b> 为  `minSize<sub>j</sub>`  ，且
-  `abs(id - preferred<sub>j</sub>)`  的值 **最小**  ，其中  `abs(x)`  是  `x`  的绝对值。
如果差的绝对值有 **相等**  的，选择 **最小**  的  `id`  。如果 **没有满足条件的房间**  ，答案为 `-1`  。

请你返回长度为 `k`  的数组  `answer`  ，其中 * * `answer[j]`  为第 `j`  个查询的结果。

 

 **示例 1：** 

```

输入：rooms = [[2,2],[1,2],[3,2]], queries = [[3,1],[3,3],[5,2]]
输出：[3,-1,3]
解释：查询的答案如下：
查询 [3,1] ：房间 3 的面积为 2 ，大于等于 1 ，且号码是最接近 3 的，为 abs(3 - 3) = 0 ，所以答案为 3 。
查询 [3,3] ：没有房间的面积至少为 3 ，所以答案为 -1 。
查询 [5,2] ：房间 3 的面积为 2 ，大于等于 2 ，且号码是最接近 5 的，为 abs(3 - 5) = 2 ，所以答案为 3 。
```
 **示例 2：** 

```

输入：rooms = [[1,4],[2,3],[3,5],[4,1],[5,2]], queries = [[2,3],[2,4],[2,5]]
输出：[2,1,3]
解释：查询的答案如下：
查询 [2,3] ：房间 2 的面积为 3 ，大于等于 3 ，且号码是最接近的，为 abs(2 - 2) = 0 ，所以答案为 2 。
查询 [2,4] ：房间 1 和 3 的面积都至少为 4 ，答案为 1 因为它房间编号更小。
查询 [2,5] ：房间 3 是唯一面积大于等于 5 的，所以答案为 3 。
```
 

 **提示：** 
-  `n == rooms.length` 
-  `1 <= n <= 10^5` 
-  `k == queries.length` 
-  `1 <= k <= 10^4` 
-  `1 <= roomId<sub>i</sub>, preferred<sub>j</sub> <= 10^7` 
-  `1 <= size<sub>i</sub>, minSize<sub>j</sub> <= 10^7` 
 
**标签**
`数组` `二分查找` `排序` 


## 
```python

```
>
# 1848.到目标元素的最小距离
[https://leetcode-cn.com/problems/minimum-distance-to-the-target-element](https://leetcode-cn.com/problems/minimum-distance-to-the-target-element) 
## 原题
给你一个整数数组 `nums` （下标 **从 0 开始** 计数）以及两个整数 `target` 和 `start` ，请你找出一个下标 `i` ，满足 `nums[i] == target` 且 `abs(i - start)` **最小化** 。注意： `abs(x)` 表示 `x` 的绝对值。

返回 `abs(i - start)` 。

题目数据保证 `target` 存在于 `nums` 中。

 

 **示例 1：** 

```

输入：nums = [1,2,3,4,5], target = 5, start = 3
输出：1
解释：nums[4] = 5 是唯一一个等于 target 的值，所以答案是 abs(4 - 3) = 1 。

```
 **示例 2：** 

```

输入：nums = [1], target = 1, start = 0
输出：0
解释：nums[0] = 1 是唯一一个等于 target 的值，所以答案是 abs(0 - 0) = 0 。

```
 **示例 3：** 

```

输入：nums = [1,1,1,1,1,1,1,1,1,1], target = 1, start = 0
输出：0
解释：nums 中的每个值都是 1 ，但 nums[0] 使 abs(i - start) 的结果得以最小化，所以答案是 abs(0 - 0) = 0 。

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `1 <= nums[i] <= 10^4` 
-  `0 <= start < nums.length` 
-  `target` 存在于 `nums` 中
 
**标签**
`数组` 


## 
```python

```
>
# 1849.将字符串拆分为递减的连续值
[https://leetcode-cn.com/problems/splitting-a-string-into-descending-consecutive-values](https://leetcode-cn.com/problems/splitting-a-string-into-descending-consecutive-values) 
## 原题
给你一个仅由数字组成的字符串 `s` 。

请你判断能否将 `s` 拆分成两个或者多个 **非空子字符串** ，使子字符串的 **数值** 按 **降序** 排列，且每两个 **相邻子字符串** 的数值之 **差** 等于 `1` 。
- 例如，字符串 `s = "0090089"` 可以拆分成 `["0090", "089"]` ，数值为 `[90,89]` 。这些数值满足按降序排列，且相邻值相差 `1` ，这种拆分方法可行。
- 另一个例子中，字符串 `s = "001"` 可以拆分成 `["0", "01"]` 、 `["00", "1"]` 或 `["0", "0", "1"]` 。然而，所有这些拆分方法都不可行，因为对应数值分别是 `[0,1]` 、 `[0,1]` 和 `[0,0,1]` ，都不满足按降序排列的要求。
如果可以按要求拆分 `s` ，返回 `true` ；否则，返回 `false` 。

 **子字符串** 是字符串中的一个连续字符序列。

 

 **示例 1：** 

```

输入：s = "1234"
输出：false
解释：不存在拆分 s 的可行方法。

```
 **示例 2：** 

```

输入：s = "050043"
输出：true
解释：s 可以拆分为 ["05", "004", "3"] ，对应数值为 [5,4,3] 。
满足按降序排列，且相邻值相差 1 。

```
 **示例 3：** 

```

输入：s = "9080701"
输出：false
解释：不存在拆分 s 的可行方法。

```
 **示例 4：** 

```

输入：s = "10009998"
输出：true
解释：s 可以拆分为 ["100", "099", "98"] ，对应数值为 [100,99,98] 。
满足按降序排列，且相邻值相差 1 。
```
 

 **提示：** 
-  `1 <= s.length <= 20` 
-  `s` 仅由数字组成
 
**标签**
`字符串` `回溯` 


## 
```python

```
>
# 1850.邻位交换的最小次数
[https://leetcode-cn.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number](https://leetcode-cn.com/problems/minimum-adjacent-swaps-to-reach-the-kth-smallest-number) 
## 原题
给你一个表示大整数的字符串 `num` ，和一个整数 `k` 。

如果某个整数是 `num` 中各位数字的一个 **排列** 且它的 **值大于** `num` ，则称这个整数为 **妙数** 。可能存在很多妙数，但是只需要关注 **值最小** 的那些。
- 例如， `num = "5489355142"` ：

	
- 第 1 个最小妙数是 `"5489355214"` 
- 第 2 个最小妙数是 `"5489355241"` 
- 第 3 个最小妙数是 `"5489355412"` 
- 第 4 个最小妙数是 `"5489355421"` 
	
	
返回要得到第 `k` 个 **最小妙数** 需要对 `num` 执行的 **相邻位数字交换的最小次数** 。

测试用例是按存在第 `k` 个最小妙数而生成的。

 

 **示例 1：** 

```
输入：num = "5489355142", k = 4
输出：2
解释：第 4 个最小妙数是 "5489355421" ，要想得到这个数字：
- 交换下标 7 和下标 8 对应的位："5489355142" -> "5489355412"
- 交换下标 8 和下标 9 对应的位："5489355412" -> "5489355421"

```
 **示例 2：** 

```
输入：num = "11112", k = 4
输出：4
解释：第 4 个最小妙数是 "21111" ，要想得到这个数字：
- 交换下标 3 和下标 4 对应的位："11112" -> "11121"
- 交换下标 2 和下标 3 对应的位："11121" -> "11211"
- 交换下标 1 和下标 2 对应的位："11211" -> "12111"
- 交换下标 0 和下标 1 对应的位："12111" -> "21111"

```
 **示例 3：** 

```
输入：num = "00123", k = 1
输出：1
解释：第 1 个最小妙数是 "00132" ，要想得到这个数字：
- 交换下标 3 和下标 4 对应的位："00123" -> "00132"

```
 

 **提示：** 
-  `2 <= num.length <= 1000` 
-  `1 <= k <= 1000` 
-  `num` 仅由数字组成
 
**标签**
`贪心` `双指针` `字符串` 


## 
```python

```
>
# 1851.包含每个查询的最小区间
[https://leetcode-cn.com/problems/minimum-interval-to-include-each-query](https://leetcode-cn.com/problems/minimum-interval-to-include-each-query) 
## 原题
给你一个二维整数数组 `intervals` ，其中 `intervals[i] = [left<sub>i</sub>, right<sub>i</sub>]` 表示第 `i` 个区间开始于 `left<sub>i</sub>` 、结束于 `right<sub>i</sub>` （包含两侧取值， **闭区间** ）。区间的 **长度** 定义为区间中包含的整数数目，更正式地表达是 `right<sub>i</sub> - left<sub>i</sub> + 1` 。

再给你一个整数数组 `queries` 。第 `j` 个查询的答案是满足  `left<sub>i</sub> <= queries[j] <= right<sub>i</sub>` 的 **长度最小区间 `i` 的长度** 。如果不存在这样的区间，那么答案是 `-1` 。

以数组形式返回对应查询的所有答案。

 

 **示例 1：** 

```

输入：intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
输出：[3,3,1,4]
解释：查询处理如下：
- Query = 2 ：区间 [2,4] 是包含 2 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 3 ：区间 [2,4] 是包含 3 的最小区间，答案为 4 - 2 + 1 = 3 。
- Query = 4 ：区间 [4,4] 是包含 4 的最小区间，答案为 4 - 4 + 1 = 1 。
- Query = 5 ：区间 [3,6] 是包含 5 的最小区间，答案为 6 - 3 + 1 = 4 。

```
 **示例 2：** 

```

输入：intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
输出：[2,-1,4,6]
解释：查询处理如下：
- Query = 2 ：区间 [2,3] 是包含 2 的最小区间，答案为 3 - 2 + 1 = 2 。
- Query = 19：不存在包含 19 的区间，答案为 -1 。
- Query = 5 ：区间 [2,5] 是包含 5 的最小区间，答案为 5 - 2 + 1 = 4 。
- Query = 22：区间 [20,25] 是包含 22 的最小区间，答案为 25 - 20 + 1 = 6 。

```
 

 **提示：** 
-  `1 <= intervals.length <= 10^5` 
-  `1 <= queries.length <= 10^5` 
-  `queries[i].length == 2` 
-  `1 <= left<sub>i</sub> <= right<sub>i</sub> <= 10^7` 
-  `1 <= queries[j] <= 10^7` 
 
**标签**
`数组` `二分查找` `排序` `扫描线` `堆（优先队列）` 


## 
```python

```
>
# 1852.每个子数组的数字种类数
[https://leetcode-cn.com/problems/distinct-numbers-in-each-subarray](https://leetcode-cn.com/problems/distinct-numbers-in-each-subarray) 
## 原题

 
**标签**
`数组` `哈希表` `滑动窗口` 


## 
```python

```
>
# 1853.转换日期格式
[https://leetcode-cn.com/problems/convert-date-format](https://leetcode-cn.com/problems/convert-date-format) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1854.人口最多的年份
[https://leetcode-cn.com/problems/maximum-population-year](https://leetcode-cn.com/problems/maximum-population-year) 
## 原题
给你一个二维整数数组 `logs` ，其中每个 `logs[i] = [birth<sub>i</sub>, death<sub>i</sub>]` 表示第 `i` 个人的出生和死亡年份。

年份 `x` 的 **人口** 定义为这一年期间活着的人的数目。第 `i` 个人被计入年份 `x` 的人口需要满足： `x` 在闭区间 `[birth<sub>i</sub>, death<sub>i</sub> - 1]` 内。注意，人不应当计入他们死亡当年的人口中。

返回 **人口最多** 且 **最早** 的年份。

 

 **示例 1：** 

```
输入：logs = [[1993,1999],[2000,2010]]
输出：1993
解释：人口最多为 1 ，而 1993 是人口为 1 的最早年份。

```
 **示例 2：** 

```
输入：logs = [[1950,1961],[1960,1971],[1970,1981]]
输出：1960
解释： 
人口最多为 2 ，分别出现在 1960 和 1970 。
其中最早年份是 1960 。
```
 

 **提示：** 
-  `1 <= logs.length <= 100` 
-  `1950 <= birth<sub>i</sub> < death<sub>i</sub> <= 2050` 
 
**标签**
`数组` `计数` 


## 
```python

```
>
# 1855.下标对中的最大距离
[https://leetcode-cn.com/problems/maximum-distance-between-a-pair-of-values](https://leetcode-cn.com/problems/maximum-distance-between-a-pair-of-values) 
## 原题
给你两个 **非递增** 的整数数组 `nums1` ​​​​​​ 和 `nums2` ​​​​​​ ，数组下标均 **从 0 开始** 计数。

下标对 `(i, j)` 中 `0 <= i < nums1.length` 且 `0 <= j < nums2.length` 。如果该下标对同时满足 `i <= j` 且 `nums1[i] <= nums2[j]` ，则称之为 **有效** 下标对，该下标对的 **距离** 为 `j - i` ​​ 。​​

返回所有 **有效** 下标对 `(i, j)` 中的 **最大距离** 。如果不存在有效下标对，返回 `0` 。

一个数组 `arr` ，如果每个 `1 <= i < arr.length` 均有 `arr[i-1] >= arr[i]` 成立，那么该数组是一个 **非递增** 数组。

 

 **示例 1：** 

```

输入：nums1 = [55,30,5,4,2], nums2 = [100,20,10,10,5]
输出：2
解释：有效下标对是 (0,0), (2,2), (2,3), (2,4), (3,3), (3,4) 和 (4,4) 。
最大距离是 2 ，对应下标对 (2,4) 。

```
 **示例 2：** 

```

输入：nums1 = [2,2,2], nums2 = [10,10,1]
输出：1
解释：有效下标对是 (0,0), (0,1) 和 (1,1) 。
最大距离是 1 ，对应下标对 (0,1) 。
```
 **示例 3：** 

```

输入：nums1 = [30,29,19,5], nums2 = [25,25,25,25,25]
输出：2
解释：有效下标对是 (2,2), (2,3), (2,4), (3,3) 和 (3,4) 。
最大距离是 2 ，对应下标对 (2,4) 。

```
 **示例 4：** 

```

输入：nums1 = [5,4], nums2 = [3,2]
输出：0
解释：不存在有效下标对，所以返回 0 。

```
 

 **提示：** 
-  `1 <= nums1.length <= 10^5` 
-  `1 <= nums2.length <= 10^5` 
-  `1 <= nums1[i], nums2[j] <= 10^5` 
-  `nums1` 和 `nums2` 都是 **非递增** 数组
 
**标签**
`贪心` `数组` `双指针` `二分查找` 


## 
```python

```
>
# 1856.子数组最小乘积的最大值
[https://leetcode-cn.com/problems/maximum-subarray-min-product](https://leetcode-cn.com/problems/maximum-subarray-min-product) 
## 原题
一个数组的 **最小乘积**  定义为这个数组中 **最小值**   **乘以 ** 数组的 **和**  。
- 比方说，数组  `[3,2,5]`  （最小值是  `2` ）的最小乘积为  `2 * (3+2+5) = 2 * 10 = 20`  。
给你一个正整数数组  `nums`  ，请你返回  `nums`  任意  **非空子数组**  的 **最小乘积**  的  **最大值**  。由于答案可能很大，请你返回答案对   `10^9 + 7`   **取余 ** 的结果。

请注意，最小乘积的最大值考虑的是取余操作 **之前**  的结果。题目保证最小乘积的最大值在 **不取余** 的情况下可以用 **64 位有符号整数**  保存。

 **子数组**  定义为一个数组的 **连续**  部分。

 

 **示例 1：** 

```

输入：nums = [1,2,3,2]
输出：14
解释：最小乘积的最大值由子数组 [2,3,2] （最小值是 2）得到。
2 * (2+3+2) = 2 * 7 = 14 。

```
 **示例 2：** 

```

输入：nums = [2,3,3,1,2]
输出：18
解释：最小乘积的最大值由子数组 [3,3] （最小值是 3）得到。
3 * (3+3) = 3 * 6 = 18 。

```
 **示例 3：** 

```

输入：nums = [3,1,5,6,4,2]
输出：60
解释：最小乘积的最大值由子数组 [5,6,4] （最小值是 4）得到。
4 * (5+6+4) = 4 * 15 = 60 。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^7` 
 
**标签**
`栈` `数组` `前缀和` `单调栈` 


## 
```python

```
>
# 1857.有向图中最大颜色值
[https://leetcode-cn.com/problems/largest-color-value-in-a-directed-graph](https://leetcode-cn.com/problems/largest-color-value-in-a-directed-graph) 
## 原题
给你一个  **有向图**  ，它含有  `n`  个节点和 `m`  条边。节点编号从  `0` 到  `n - 1`  。

给你一个字符串  `colors` ，其中  `colors[i]`  是小写英文字母，表示图中第 `i`  个节点的 <b>颜色</b> （下标从 **0**  开始）。同时给你一个二维数组  `edges`  ，其中  `edges[j] = [a<sub>j</sub>, b<sub>j</sub>]`  表示从节点  `a<sub>j</sub>`  到节点  `b<sub>j</sub>` <sub> </sub>有一条  **有向边**  。

图中一条有效 **路径**  是一个点序列  `x<sub>1</sub> -> x<sub>2</sub> -> x<sub>3</sub> -> ... -> x<sub>k</sub>`  ，对于所有  `1 <= i < k`  ，从  `x<sub>i</sub>` 到  `x<sub>i+1</sub>`  在图中有一条有向边。路径的 **颜色值**  是路径中 **出现次数最多** 颜色的节点数目。

请你返回给定图中有效路径里面的  **最大颜色值** ** 。** 如果图中含有环，请返回 `-1`  。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/leet1.png" style="width: 400px; height: 182px;">

```
输入：colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
输出：3
解释：路径 0 -> 2 -> 3 -> 4 含有 3 个颜色为 "a" 的节点（上图中的红色节点）。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/21/leet2.png" style="width: 85px; height: 85px;">

```
输入：colors = "a", edges = [[0,0]]
输出：-1
解释：从 0 到 0 有一个环。

```
 

 **提示：** 
-  `n == colors.length` 
-  `m == edges.length` 
-  `1 <= n <= 10^5` 
-  `0 <= m <= 10^5` 
-  `colors`  只含有小写英文字母。
-  `0 <= a<sub>j</sub>, b<sub>j</sub> < n` 
 
**标签**
`图` `拓扑排序` `记忆化搜索` `哈希表` `动态规划` `计数` 


## 
```python

```
>
# 1858.包含所有前缀的最长单词
[https://leetcode-cn.com/problems/longest-word-with-all-prefixes](https://leetcode-cn.com/problems/longest-word-with-all-prefixes) 
## 原题

 
**标签**
`深度优先搜索` `字典树` 


## 
```python

```
>
# 1859.将句子排序
[https://leetcode-cn.com/problems/sorting-the-sentence](https://leetcode-cn.com/problems/sorting-the-sentence) 
## 原题
一个 **句子**  指的是一个序列的单词用单个空格连接起来，且开头和结尾没有任何空格。每个单词都只包含小写或大写英文字母。

我们可以给一个句子添加 **从 1 开始的单词位置索引** ，并且将句子中所有单词  **打乱顺序**  。
- 比方说，句子  `"This is a sentence"`  可以被打乱顺序得到  `"sentence4 a3 is2 This1"`  或者  `"is2 sentence4 This1 a3"`  。
给你一个 **打乱顺序**  的句子  `s`  ，它包含的单词不超过  `9`  个，请你重新构造并得到原本顺序的句子。

 

 **示例 1：** 

```

输入：s = "is2 sentence4 This1 a3"
输出："This is a sentence"
解释：将 s 中的单词按照初始位置排序，得到 "This1 is2 a3 sentence4" ，然后删除数字。

```
 **示例 2：** 

```

输入：s = "Myself2 Me1 I4 and3"
输出："Me Myself and I"
解释：将 s 中的单词按照初始位置排序，得到 "Me1 Myself2 and3 I4" ，然后删除数字。
```
 

 **提示：** 
-  `2 <= s.length <= 200` 
-  `s`  只包含小写和大写英文字母、空格以及从  `1`  到  `9`  的数字。
-  `s`  中单词数目为  `1`  到  `9`  个。
-  `s`  中的单词由单个空格分隔。
-  `s`  不包含任何前导或者后缀空格。
 
**标签**
`字符串` `排序` 


## 
```python

```
>
# 1860.增长的内存泄露
[https://leetcode-cn.com/problems/incremental-memory-leak](https://leetcode-cn.com/problems/incremental-memory-leak) 
## 原题
给你两个整数  `memory1` 和  `memory2`  分别表示两个内存条剩余可用内存的位数。现在有一个程序每秒递增的速度消耗着内存。

在第  `i`  秒（秒数从 1 开始），有 `i`  位内存被分配到  **剩余内存较多**  的内存条（如果两者一样多，则分配到第一个内存条）。如果两者剩余内存都不足 `i`  位，那么程序将 <b>意外退出</b> 。

请你返回一个数组，包含 `[crashTime, memory1<sub>crash</sub>, memory2<sub>crash</sub>]`  ，其中  `crashTime` 是程序意外退出的时间（单位为秒）， * * `memory1<sub>crash</sub>` 和 * * `memory2<sub>crash</sub>` * * 分别是两个内存条最后剩余内存的位数。

 

 **示例 1：** 

```
输入：memory1 = 2, memory2 = 2
输出：[3,1,0]
解释：内存分配如下：
- 第 1 秒，内存条 1 被占用 1 位内存。内存条 1 现在有 1 位剩余可用内存。
- 第 2 秒，内存条 2 被占用 2 位内存。内存条 2 现在有 0 位剩余可用内存。
- 第 3 秒，程序意外退出，两个内存条分别有 1 位和 0 位剩余可用内存。

```
 **示例 2：** 

```
输入：memory1 = 8, memory2 = 11
输出：[6,0,4]
解释：内存分配如下：
- 第 1 秒，内存条 2 被占用 1 位内存，内存条 2 现在有 10 位剩余可用内存。
- 第 2 秒，内存条 2 被占用 2 位内存，内存条 2 现在有 8 位剩余可用内存。
- 第 3 秒，内存条 1 被占用 3 位内存，内存条 1 现在有 5 位剩余可用内存。
- 第 4 秒，内存条 2 被占用 4 位内存，内存条 2 现在有 4 位剩余可用内存。
- 第 5 秒，内存条 1 被占用 5 位内存，内存条 1 现在有 0 位剩余可用内存。
- 第 6 秒，程序意外退出，两个内存条分别有 0 位和 4 位剩余可用内存。

```
 

 **提示：** 
-  `0 <= memory1, memory2 <= 2^31 - 1` 
 
**标签**
`模拟` 


## 
```python

```
>
# 1861.旋转盒子
[https://leetcode-cn.com/problems/rotating-the-box](https://leetcode-cn.com/problems/rotating-the-box) 
## 原题
给你一个  `m x n`  的字符矩阵  `box`  ，它表示一个箱子的侧视图。箱子的每一个格子可能为：
-  `'#'`  表示石头
-  `'*'`  表示固定的障碍物
-  `'.'`  表示空位置
这个箱子被 **顺时针旋转 90 度**  ，由于重力原因，部分石头的位置会发生改变。每个石头会垂直掉落，直到它遇到障碍物，另一个石头或者箱子的底部。重力 **不会**  影响障碍物的位置，同时箱子旋转不会产生 **惯性**  ，也就是说石头的水平位置不会发生改变。

题目保证初始时  `box`  中的石头要么在一个障碍物上，要么在另一个石头上，要么在箱子的底部。

请你返回一个 * * `n x m` 的矩阵，表示按照上述旋转后，箱子内的结果。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcodewithstones.png" style="width: 300px; height: 150px;">

```
输入：box = [["#",".","#"]]
输出：[["."],
      ["#"],
      ["#"]]

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode2withstones.png" style="width: 375px; height: 195px;">

```
输入：box = [["#",".","*","."],
            ["#","#","*","."]]
输出：[["#","."],
      ["#","#"],
      ["*","*"],
      [".","."]]

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/04/08/rotatingtheboxleetcode3withstone.png" style="width: 400px; height: 218px;">

```
输入：box = [["#","#","*",".","*","."],
            ["#","#","#","*",".","."],
            ["#","#","#",".","#","."]]
输出：[[".","#","#"],
      [".","#","#"],
      ["#","#","*"],
      ["#","*","."],
      ["#",".","*"],
      ["#",".","."]]

```
 

 **提示：** 
-  `m == box.length` 
-  `n == box[i].length` 
-  `1 <= m, n <= 500` 
-  `box[i][j]`  只可能是  `'#'`  ， `'*'`  或者  `'.'`  。
 
**标签**
`数组` `双指针` `矩阵` 


## 
```python

```
>
# 1862.向下取整数对和
[https://leetcode-cn.com/problems/sum-of-floored-pairs](https://leetcode-cn.com/problems/sum-of-floored-pairs) 
## 原题
给你一个整数数组  `nums`  ，请你返回所有下标对  `0 <= i, j < nums.length`  的  `floor(nums[i] / nums[j])`  结果之和。由于答案可能会很大，请你返回答案对 `10^9 + 7`   **取余**  的结果。

函数  `floor()`  返回输入数字的整数部分。

 

 **示例 1：** 

```
输入：nums = [2,5,9]
输出：10
解释：
floor(2 / 5) = floor(2 / 9) = floor(5 / 9) = 0
floor(2 / 2) = floor(5 / 5) = floor(9 / 9) = 1
floor(5 / 2) = 2
floor(9 / 2) = 4
floor(9 / 5) = 1
我们计算每一个数对商向下取整的结果并求和得到 10 。

```
 **示例 2：** 

```
输入：nums = [7,7,7,7,7,7,7]
输出：49

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^5` 
 
**标签**
`数组` `数学` `二分查找` `前缀和` 


## 
```python

```
>
# 1863.找出所有子集的异或总和再求和
[https://leetcode-cn.com/problems/sum-of-all-subset-xor-totals](https://leetcode-cn.com/problems/sum-of-all-subset-xor-totals) 
## 原题
一个数组的 **异或总和** 定义为数组中所有元素按位 `XOR` 的结果；如果数组为 **空** ，则异或总和为 `0` 。
- 例如，数组  `[2,5,6]` 的 **异或总和** 为 `2 XOR 5 XOR 6 = 1` 。
给你一个数组 `nums` ，请你求出 `nums` 中每个 **子集** 的 **异或总和** ，计算并返回这些值相加之 **和** 。

 **注意：** 在本题中，元素 **相同** 的不同子集应 **多次** 计数。

数组 `a` 是数组 `b` 的一个 **子集** 的前提条件是：从 `b` 删除几个（也可能不删除）元素能够得到 `a` 。

 

 **示例 1：** 

```
输入：nums = [1,3]
输出：6
解释：[1,3] 共有 4 个子集：
- 空子集的异或总和是 0 。
- [1] 的异或总和为 1 。
- [3] 的异或总和为 3 。
- [1,3] 的异或总和为 1 XOR 3 = 2 。
0 + 1 + 3 + 2 = 6

```
 **示例 2：** 

```
输入：nums = [5,1,6]
输出：28
解释：[5,1,6] 共有 8 个子集：
- 空子集的异或总和是 0 。
- [5] 的异或总和为 5 。
- [1] 的异或总和为 1 。
- [6] 的异或总和为 6 。
- [5,1] 的异或总和为 5 XOR 1 = 4 。
- [5,6] 的异或总和为 5 XOR 6 = 3 。
- [1,6] 的异或总和为 1 XOR 6 = 7 。
- [5,1,6] 的异或总和为 5 XOR 1 XOR 6 = 2 。
0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

```
 **示例 3：** 

```
输入：nums = [3,4,5,6,7,8]
输出：480
解释：每个子集的全部异或总和值之和为 480 。

```
 

 **提示：** 
-  `1 <= nums.length <= 12` 
-  `1 <= nums[i] <= 20` 
 
**标签**
`位运算` `数组` `数学` `回溯` `组合数学` 


## 
```python

```
>
# 1864.构成交替字符串需要的最小交换次数
[https://leetcode-cn.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating](https://leetcode-cn.com/problems/minimum-number-of-swaps-to-make-the-binary-string-alternating) 
## 原题
给你一个二进制字符串 `s` ，现需要将其转化为一个 **交替字符串** 。请你计算并返回转化所需的 **最小** 字符交换次数，如果无法完成转化，返回 `-1` 。

 **交替字符串** 是指：相邻字符之间不存在相等情况的字符串。例如，字符串 `"010"` 和 `"1010"` 属于交替字符串，但 `"0100"` 不是。

任意两个字符都可以进行交换， **不必相邻** 。

 

 **示例 1：** 

```

输入：s = "111000"
输出：1
解释：交换位置 1 和 4："111000" -> "101010" ，字符串变为交替字符串。

```
 **示例 2：** 

```

输入：s = "010"
输出：0
解释：字符串已经是交替字符串了，不需要交换。

```
 **示例 3：** 

```

输入：s = "1110"
输出：-1

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s[i]` 的值为 `'0'` 或 `'1'` 
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 1865.找出和为指定值的下标对
[https://leetcode-cn.com/problems/finding-pairs-with-a-certain-sum](https://leetcode-cn.com/problems/finding-pairs-with-a-certain-sum) 
## 原题
给你两个整数数组 `nums1` 和 `nums2` ，请你实现一个支持下述两类查询的数据结构：
-  **累加** ，将一个正整数加到 `nums2` 中指定下标对应元素上。
-  **计数** ，统计满足 `nums1[i] + nums2[j]` 等于指定值的下标对 `(i, j)` 数目（ `0 <= i < nums1.length` 且 `0 <= j < nums2.length` ）。
实现 `FindSumPairs` 类：
-  `FindSumPairs(int[] nums1, int[] nums2)` 使用整数数组  `nums1` 和 `nums2` 初始化 `FindSumPairs` 对象。
-  `void add(int index, int val)` 将 `val` 加到 `nums2[index]` 上，即，执行 `nums2[index] += val` 。
-  `int count(int tot)` 返回满足  `nums1[i] + nums2[j] == tot` 的下标对 `(i, j)` 数目。
 

 **示例：** 

```

输入：
["FindSumPairs", "count", "add", "count", "count", "add", "add", "count"]
[[[1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]], [7], [3, 2], [8], [4], [0, 1], [1, 1], [7]]
输出：
[null, 8, null, 2, 1, null, null, 11]

解释：
FindSumPairs findSumPairs = new FindSumPairs([1, 1, 2, 2, 2, 3], [1, 4, 5, 2, 5, 4]);
findSumPairs.count(7);  // 返回 8 ; 下标对 (2,2), (3,2), (4,2), (2,4), (3,4), (4,4) 满足 2 + 5 = 7 ，下标对 (5,1), (5,5) 满足 3 + 4 = 7
findSumPairs.add(3, 2); // 此时 nums2 = [1,4,5,4,5,4]
findSumPairs.count(8);  // 返回 2 ；下标对 (5,2), (5,4) 满足 3 + 5 = 8
findSumPairs.count(4);  // 返回 1 ；下标对 (5,0) 满足 3 + 1 = 4
findSumPairs.add(0, 1); // 此时 nums2 = [2,4,5,4,5,4]
findSumPairs.add(1, 1); // 此时 nums2 = [2,5,5,4,5,4]
findSumPairs.count(7);  // 返回 11 ；下标对 (2,1), (2,2), (2,4), (3,1), (3,2), (3,4), (4,1), (4,2), (4,4) 满足 2 + 5 = 7 ，下标对 (5,3), (5,5) 满足 3 + 4 = 7

```
 

 **提示：** 
-  `1 <= nums1.length <= 1000` 
-  `1 <= nums2.length <= 10^5` 
-  `1 <= nums1[i] <= 10^9` 
-  `1 <= nums2[i] <= 10^5` 
-  `0 <= index < nums2.length` 
-  `1 <= val <= 10^5` 
-  `1 <= tot <= 10^9` 
- 最多调用  `add` 和 `count` 函数各 `1000` 次
 
**标签**
`设计` `数组` `哈希表` 


## 
```python

```
>
# 1866.恰有 K 根木棍可以看到的排列数目
[https://leetcode-cn.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible](https://leetcode-cn.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible) 
## 原题
有 `n` 根长度互不相同的木棍，长度为从 `1` 到 `n` 的整数。请你将这些木棍排成一排，并满足从左侧 **可以看到**   **恰好** `k` 根木棍。从左侧 **可以看到** 木棍的前提是这个木棍的 **左侧** 不存在比它 **更长的** 木棍。
- 例如，如果木棍排列为 `[ ***1*** , ***3*** ,2, ***5*** ,4]` ，那么从左侧可以看到的就是长度分别为 `1` 、 `3` 、 `5` 的木棍。
给你 `n` 和 `k` ，返回符合题目要求的排列 **数目** 。由于答案可能很大，请返回对 `10^9 + 7` **取余** 的结果。

 

 **示例 1：** 

```
输入：n = 3, k = 2
输出：3
解释：[1,3,2], [2,3,1] 和 [2,1,3] 是仅有的能满足恰好 2 根木棍可以看到的排列。
可以看到的木棍已经用粗体+斜体标识。

```
 **示例 2：** 

```
输入：n = 5, k = 5
输出：1
解释：[1,2,3,4,5] 是唯一一种能满足全部 5 根木棍可以看到的排列。
可以看到的木棍已经用粗体+斜体标识。

```
 **示例 3：** 

```
输入：n = 20, k = 11
输出：647427950
解释：总共有 647427950 (mod 10^9 + 7) 种能满足恰好有 11 根木棍可以看到的排列。

```
 

 **提示：** 
-  `1 <= n <= 1000` 
-  `1 <= k <= n` 
 
**标签**
`数学` `动态规划` `组合数学` 


## 
```python

```
>
# 1867.最大数量高于平均水平的订单
[https://leetcode-cn.com/problems/orders-with-maximum-quantity-above-average](https://leetcode-cn.com/problems/orders-with-maximum-quantity-above-average) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1868.两个行程编码数组的积
[https://leetcode-cn.com/problems/product-of-two-run-length-encoded-arrays](https://leetcode-cn.com/problems/product-of-two-run-length-encoded-arrays) 
## 原题

 
**标签**
`数组` `双指针` 


## 
```python

```
>
# 1869.哪种连续子字符串更长
[https://leetcode-cn.com/problems/longer-contiguous-segments-of-ones-than-zeros](https://leetcode-cn.com/problems/longer-contiguous-segments-of-ones-than-zeros) 
## 原题
给你一个二进制字符串 `s` 。如果字符串中由 `1` 组成的 **最长** 连续子字符串 **严格长于** 由 `0` 组成的 **最长** 连续子字符串，返回 `true` ；否则，返回 `false` 。
- 例如， `s = " **11** 01 **000** 10"` 中，由 `1` 组成的最长连续子字符串的长度是 `2` ，由 `0` 组成的最长连续子字符串的长度是 `3` 。
注意，如果字符串中不存在 `0` ，此时认为由 `0` 组成的最长连续子字符串的长度是 `0` 。字符串中不存在 `1` 的情况也适用此规则。

 

 **示例 1：** 

```

输入：s = "1101"
输出：true
解释：
由 1 组成的最长连续子字符串的长度是 2："1101"
由 0 组成的最长连续子字符串的长度是 1："1101"
由 1 组成的子字符串更长，故返回 true 。

```
 **示例 2：** 

```

输入：s = "111000"
输出：false
解释：
由 1 组成的最长连续子字符串的长度是 3："111000"
由 0 组成的最长连续子字符串的长度是 3："111000"
由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。

```
 **示例 3：** 

```

输入：s = "110100010"
输出：false
解释：
由 1 组成的最长连续子字符串的长度是 2："110100010"
由 0 组成的最长连续子字符串的长度是 3："110100010"
由 1 组成的子字符串不比由 0 组成的子字符串长，故返回 false 。

```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `s[i]` 不是 `'0'` 就是 `'1'` 
 
**标签**
`字符串` 


## 
```python

```
>
# 1870.准时到达的列车最小时速
[https://leetcode-cn.com/problems/minimum-speed-to-arrive-on-time](https://leetcode-cn.com/problems/minimum-speed-to-arrive-on-time) 
## 原题
给你一个浮点数 `hour` ，表示你到达办公室可用的总通勤时间。要到达办公室，你必须按给定次序乘坐 `n` 趟列车。另给你一个长度为 `n` 的整数数组 `dist` ，其中 `dist[i]` 表示第 `i` 趟列车的行驶距离（单位是千米）。

每趟列车均只能在整点发车，所以你可能需要在两趟列车之间等待一段时间。
- 例如，第 `1` 趟列车需要 `1.5` 小时，那你必须再等待 `0.5` 小时，搭乘在第 2 小时发车的第 `2` 趟列车。
返回能满足你准时到达办公室所要求全部列车的 **最小正整数** 时速（单位：千米每小时），如果无法准时到达，则返回 `-1` 。

生成的测试用例保证答案不超过 `10^7` ，且 `hour` 的 **小数点后最多存在两位数字** 。

 

 **示例 1：** 

```

输入：dist = [1,3,2], hour = 6
输出：1
解释：速度为 1 时：
- 第 1 趟列车运行需要 1/1 = 1 小时。
- 由于是在整数时间到达，可以立即换乘在第 1 小时发车的列车。第 2 趟列车运行需要 3/1 = 3 小时。
- 由于是在整数时间到达，可以立即换乘在第 4 小时发车的列车。第 3 趟列车运行需要 2/1 = 2 小时。
- 你将会恰好在第 6 小时到达。

```
 **示例 2：** 

```

输入：dist = [1,3,2], hour = 2.7
输出：3
解释：速度为 3 时：
- 第 1 趟列车运行需要 1/3 = 0.33333 小时。
- 由于不是在整数时间到达，故需要等待至第 1 小时才能搭乘列车。第 2 趟列车运行需要 3/3 = 1 小时。
- 由于是在整数时间到达，可以立即换乘在第 2 小时发车的列车。第 3 趟列车运行需要 2/3 = 0.66667 小时。
- 你将会在第 2.66667 小时到达。
```
 **示例 3：** 

```

输入：dist = [1,3,2], hour = 1.9
输出：-1
解释：不可能准时到达，因为第 3 趟列车最早是在第 2 小时发车。
```
 

 **提示：** 
-  `n == dist.length` 
-  `1 <= n <= 10^5` 
-  `1 <= dist[i] <= 10^5` 
-  `1 <= hour <= 10^9` 
-  `hours` 中，小数点后最多存在两位数字
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 1871.跳跃游戏 VII
[https://leetcode-cn.com/problems/jump-game-vii](https://leetcode-cn.com/problems/jump-game-vii) 
## 原题
给你一个下标从 **0** 开始的二进制字符串  `s`  和两个整数  `minJump` 和  `maxJump`  。一开始，你在下标  `0`  处，且该位置的值一定为  `'0'`  。当同时满足如下条件时，你可以从下标  `i`  移动到下标  `j`  处：
-  `i + minJump <= j <= min(i + maxJump, s.length - 1)`  且
-  `s[j] == '0'` .
如果你可以到达 `s`  的下标<i> </i> `s.length - 1`  处，请你返回  `true`  ，否则返回  `false`  。

 

 **示例 1：** 

```

输入：s = "011010", minJump = 2, maxJump = 3
输出：true
解释：
第一步，从下标 0 移动到下标 3 。
第二步，从下标 3 移动到下标 5 。

```
 **示例 2：** 

```

输入：s = "01101110", minJump = 2, maxJump = 3
输出：false

```
 

 **提示：** 
-  `2 <= s.length <= 10^5` 
-  `s[i]`  要么是  `'0'`  ，要么是  `'1'` 
-  `s[0] == '0'` 
-  `1 <= minJump <= maxJump < s.length` 
 
**标签**
`双指针` `字符串` `前缀和` 


## 
```python

```
>
# 1872.石子游戏 VIII
[https://leetcode-cn.com/problems/stone-game-viii](https://leetcode-cn.com/problems/stone-game-viii) 
## 原题
Alice 和 Bob 玩一个游戏，两人轮流操作， **Alice 先手**  。

总共有  `n`  个石子排成一行。轮到某个玩家的回合时，如果石子的数目 **大于 1**  ，他将执行以下操作：
- 选择一个整数  `x > 1`  ，并且 **移除**  最左边的  `x`  个石子。
- 将 ** 移除**  的石子价值之 **和**  累加到该玩家的分数中。
- 将一个 **新的石子**  放在最左边，且新石子的值为被移除石子值之和。
当只剩下 **一个**  石子时，游戏结束。

Alice 和 Bob 的 **分数之差**  为  `(Alice 的分数 - Bob 的分数)`  。 Alice 的目标是 ** 最大化**  分数差，Bob 的目标是 **最小化**  分数差。

给你一个长度为 `n`  的整数数组  `stones`  ，其中  `stones[i]`  是 **从左边起**  第  `i`  个石子的价值。请你返回在双方都采用 **最优** 策略的情况下，Alice 和 Bob 的 **分数之差** 。

 

 **示例 1：** 

```
输入：stones = [-1,2,-3,4,-5]
输出：5
解释：
- Alice 移除最左边的 4 个石子，得分增加 (-1) + 2 + (-3) + 4 = 2 ，并且将一个价值为 2 的石子放在最左边。stones = [2,-5] 。
- Bob 移除最左边的 2 个石子，得分增加 2 + (-5) = -3 ，并且将一个价值为 -3 的石子放在最左边。stones = [-3] 。
两者分数之差为 2 - (-3) = 5 。

```
 **示例 2：** 

```
输入：stones = [7,-6,5,10,5,-2,-6]
输出：13
解释：
- Alice 移除所有石子，得分增加 7 + (-6) + 5 + 10 + 5 + (-2) + (-6) = 13 ，并且将一个价值为 13 的石子放在最左边。stones = [13] 。
两者分数之差为 13 - 0 = 13 。

```
 **示例 3：** 

```
输入：stones = [-10,-12]
输出：-22
解释：
- Alice 只有一种操作，就是移除所有石子。得分增加 (-10) + (-12) = -22 ，并且将一个价值为 -22 的石子放在最左边。stones = [-22] 。
两者分数之差为 (-22) - 0 = -22 。

```
 

 **提示：** 
-  `n == stones.length` 
-  `2 <= n <= 10^5` 
-  `-10^4 <= stones[i] <= 10^4` 
 
**标签**
`数组` `数学` `动态规划` `博弈` `前缀和` 


## 
```python

```
>
# 1873.计算特殊奖金
[https://leetcode-cn.com/problems/calculate-special-bonus](https://leetcode-cn.com/problems/calculate-special-bonus) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1874.两个数组的最小乘积和
[https://leetcode-cn.com/problems/minimize-product-sum-of-two-arrays](https://leetcode-cn.com/problems/minimize-product-sum-of-two-arrays) 
## 原题

 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1875.将工资相同的雇员分组
[https://leetcode-cn.com/problems/group-employees-of-the-same-salary](https://leetcode-cn.com/problems/group-employees-of-the-same-salary) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1876.长度为三且各字符不同的子字符串
[https://leetcode-cn.com/problems/substrings-of-size-three-with-distinct-characters](https://leetcode-cn.com/problems/substrings-of-size-three-with-distinct-characters) 
## 原题
如果一个字符串不含有任何重复字符，我们称这个字符串为 **好**  字符串。

给你一个字符串 `s`  ，请你返回 `s`  中长度为 **3**  的 **好子字符串** 的数量。

注意，如果相同的好子字符串出现多次，每一次都应该被记入答案之中。

 **子字符串** 是一个字符串中连续的字符序列。

 

 **示例 1：** 

```

输入：s = "xyzzaz"
输出：1
解释：总共有 4 个长度为 3 的子字符串："xyz"，"yzz"，"zza" 和 "zaz" 。
唯一的长度为 3 的好子字符串是 "xyz" 。

```
 **示例 2：** 

```

输入：s = "aababcabc"
输出：4
解释：总共有 7 个长度为 3 的子字符串："aab"，"aba"，"bab"，"abc"，"bca"，"cab" 和 "abc" 。
好子字符串包括 "abc"，"bca"，"cab" 和 "abc" 。

```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `s` ​​​​​​ 只包含小写英文字母。
 
**标签**
`哈希表` `字符串` `计数` `滑动窗口` 


## 
```python

```
>
# 1877.数组中最大数对和的最小值
[https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array](https://leetcode-cn.com/problems/minimize-maximum-pair-sum-in-array) 
## 原题
一个数对  `(a,b)`  的 **数对和**  等于  `a + b`  。 **最大数对和**  是一个数对数组中最大的  **数对和**  。
- 比方说，如果我们有数对  `(1,5)`  ， `(2,3)`  和  `(4,4)` ， **最大数对和**  为  `max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8`  。
给你一个长度为 **偶数**   `n`  的数组  `nums`  ，请你将 `nums`  中的元素分成 `n / 2`  个数对，使得：
-  `nums`  中每个元素  **恰好**  在 **一个**  数对中，且
-  **最大数对和**  的值 **最小**  。
请你在最优数对划分的方案下，返回最小的 **最大数对和**  。

 

 **示例 1：** 

```
输入：nums = [3,5,2,3]
输出：7
解释：数组中的元素可以分为数对 (3,3) 和 (5,2) 。
最大数对和为 max(3+3, 5+2) = max(6, 7) = 7 。

```
 **示例 2：** 

```
输入：nums = [3,5,4,2,4,6]
输出：8
解释：数组中的元素可以分为数对 (3,5)，(4,4) 和 (6,2) 。
最大数对和为 max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8 。

```
 

 **提示：** 
-  `n == nums.length` 
-  `2 <= n <= 10^5` 
-  `n`  是 **偶数**  。
-  `1 <= nums[i] <= 10^5` 
 
**标签**
`贪心` `数组` `双指针` `排序` 


## 
```python

```
>
# 1878.矩阵中最大的三个菱形和
[https://leetcode-cn.com/problems/get-biggest-three-rhombus-sums-in-a-grid](https://leetcode-cn.com/problems/get-biggest-three-rhombus-sums-in-a-grid) 
## 原题
给你一个  `m x n`  的整数矩阵  `grid`  。

 **菱形和** 指的是 `grid`  中一个正菱形 **边界**  上的元素之和。本题中的菱形必须为正方形旋转45度，且四个角都在一个格子当中。下图是四个可行的菱形，每个菱形和应该包含的格子都用了相应颜色标注在图中。
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-desc-2.png" style="width: 385px; height: 385px;" />
 

注意，菱形可以是一个面积为 0 的区域，如上图中右下角的紫色菱形所示。

请你按照 **降序**  返回 `grid`  中三个最大的  **互不相同的菱形和**  。如果不同的和少于三个，则将它们全部返回。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex1.png" style="width: 360px; height: 361px;" />
```

输入：grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
输出：[228,216,211]
解释：最大的三个菱形和如上图所示。
- 蓝色：20 + 3 + 200 + 5 = 228
- 红色：200 + 2 + 10 + 4 = 216
- 绿色：5 + 200 + 4 + 2 = 211

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/04/23/pc73-q4-ex2.png" style="width: 217px; height: 217px;" />
```

输入：grid = [[1,2,3],[4,5,6],[7,8,9]]
输出：[20,9,8]
解释：最大的三个菱形和如上图所示。
- 蓝色：4 + 2 + 6 + 8 = 20
- 红色：9 （右下角红色的面积为 0 的菱形）
- 绿色：8 （下方中央面积为 0 的菱形）

```
 **示例 3：** 

```

输入：grid = [[7,7,7]]
输出：[7]
解释：所有三个可能的菱形和都相同，所以返回 [7] 。

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 100` 
-  `1 <= grid[i][j] <= 10^5` 
 
**标签**
`数组` `数学` `矩阵` `前缀和` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1879.两个数组最小的异或值之和
[https://leetcode-cn.com/problems/minimum-xor-sum-of-two-arrays](https://leetcode-cn.com/problems/minimum-xor-sum-of-two-arrays) 
## 原题
给你两个整数数组  `nums1` 和  `nums2`  ，它们长度都为  `n`  。

两个数组的 **异或值之和**  为  `(nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1])`  （ **下标从 0 开始** ）。
- 比方说， `[1,2,3]` 和  `[3,2,1]`  的 **异或值之和**  等于  `(1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4`  。
请你将  `nums2`  中的元素重新排列，使得 **异或值之和**   **最小**  。

请你返回重新排列之后的 **异或值之和**  。

 

 **示例 1：** 

```
输入：nums1 = [1,2], nums2 = [2,3]
输出：2
解释：将 nums2 重新排列得到 [3,2] 。
异或值之和为 (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2 。
```
 **示例 2：** 

```
输入：nums1 = [1,0,3], nums2 = [5,3,4]
输出：8
解释：将 nums2 重新排列得到 [5,4,3] 。
异或值之和为 (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8 。

```
 

 **提示：** 
-  `n == nums1.length` 
-  `n == nums2.length` 
-  `1 <= n <= 14` 
-  `0 <= nums1[i], nums2[i] <= 10^7` 
 
**标签**
`位运算` `数组` `动态规划` `状态压缩` 


## 
```python

```
>
# 1880.检查某单词是否等于两单词之和
[https://leetcode-cn.com/problems/check-if-word-equals-summation-of-two-words](https://leetcode-cn.com/problems/check-if-word-equals-summation-of-two-words) 
## 原题
字母的 **字母值** 取决于字母在字母表中的位置， **从 0 开始** 计数。即， `'a' -> 0` 、 `'b' -> 1` 、 `'c' -> 2` ，以此类推。

对某个由小写字母组成的字符串  `s` 而言，其 **数值** 就等于将 `s` 中每个字母的 **字母值** 按顺序 **连接** 并 **转换** 成对应整数。
- 例如， `s = "acb"` ，依次连接每个字母的字母值可以得到 `"021"` ，转换为整数得到 `21` 。
给你三个字符串 `firstWord` 、 `secondWord` 和 `targetWord` ，每个字符串都由从 `'a'` 到 `'j'` （ **含 ** `'a'` 和 `'j'` **** ）的小写英文字母组成。

如果  `firstWord` 和 `secondWord` 的 **数值之和** 等于 `targetWord` 的数值，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```
输入：firstWord = "acb", secondWord = "cba", targetWord = "cdb"
输出：true
解释：
firstWord 的数值为 "acb" -> "021" -> 21
secondWord 的数值为 "cba" -> "210" -> 210
targetWord 的数值为 "cdb" -> "231" -> 231
由于 21 + 210 == 231 ，返回 true

```
 **示例 2：** 

```
输入：firstWord = "aaa", secondWord = "a", targetWord = "aab"
输出：false
解释：
firstWord 的数值为 "aaa" -> "000" -> 0
secondWord 的数值为 "a" -> "0" -> 0
targetWord 的数值为 "aab" -> "001" -> 1
由于 0 + 0 != 1 ，返回 false
```
 **示例 3：** 

```
输入：firstWord = "aaa", secondWord = "a", targetWord = "aaaa"
输出：true
解释：
firstWord 的数值为 "aaa" -> "000" -> 0
secondWord 的数值为 "a" -> "0" -> 0
targetWord 的数值为 "aaaa" -> "0000" -> 0
由于 0 + 0 == 0 ，返回 true

```
 

 **提示：** 
-  `1 <= firstWord.length,` `secondWord.length,` `targetWord.length <= 8` 
-  `firstWord` 、 `secondWord` 和 `targetWord` 仅由从 `'a'` 到 `'j'` （ **含 ** `'a'` 和 `'j'` **** ）的小写英文字母组成 **。** 
 
**标签**
`字符串` 


## 
```python

```
>
# 1881.插入后的最大值
[https://leetcode-cn.com/problems/maximum-value-after-insertion](https://leetcode-cn.com/problems/maximum-value-after-insertion) 
## 原题
给你一个非常大的整数 `n` 和一个整数数字 `x` ，大整数 `n`  用一个字符串表示。 `n` 中每一位数字和数字 `x` 都处于闭区间 `[1, 9]` 中，且 `n` 可能表示一个 **负数** 。

你打算通过在 `n` 的十进制表示的任意位置插入 `x` 来 **最大化** `n` 的 **数值** ​​​​​​。但 **不能** 在负号的左边插入 `x` 。
- 例如，如果 `n = 73` 且 `x = 6` ，那么最佳方案是将 `6` 插入 `7` 和 `3` 之间，使 `n = 763` 。
- 如果 `n = -55` 且 `x = 2` ，那么最佳方案是将 `2` 插在第一个 `5` 之前，使 `n = -255` 。
返回插入操作后，用字符串表示的  `n` 的最大值。

 

 **示例 1：** 

```

输入：n = "99", x = 9
输出："999"
解释：不管在哪里插入 9 ，结果都是相同的。

```
 **示例 2：** 

```

输入：n = "-13", x = 2
输出："-123"
解释：向 n 中插入 x 可以得到 -213、-123 或者 -132 ，三者中最大的是 -123 。

```
 

 **提示：** 
-  `1 <= n.length <= 10^5` 
-  `1 <= x <= 9` 
-  `n` ​​​ 中每一位的数字都在闭区间 `[1, 9]` 中。
-  `n`  代表一个有效的整数。
- 当 `n` 表示负数时，将会以字符 `'-'` 开始。
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 1882.使用服务器处理任务
[https://leetcode-cn.com/problems/process-tasks-using-servers](https://leetcode-cn.com/problems/process-tasks-using-servers) 
## 原题
给你两个 **下标从 0 开始** 的整数数组 `servers` 和 `tasks` ，长度分别为 `n` ​​​​​​ 和 `m` ​​​​​​ 。 `servers[i]` 是第 `i^​​​​​​` ​​​​ 台服务器的 **权重** ，而 `tasks[j]` 是处理第 `j^​​​​​​` 项任务 **所需要的时间** （单位：秒）。

你正在运行一个仿真系统，在处理完所有任务后，该系统将会关闭。每台服务器只能同时处理一项任务。第 `0` 项任务在第 `0` 秒可以开始处理，相应地，第 `j` 项任务在第 `j`  秒可以开始处理。处理第 `j` 项任务时，你需要为它分配一台 **权重最小** 的空闲服务器。如果存在多台相同权重的空闲服务器，请选择 **下标最小** 的服务器。如果一台空闲服务器在第 `t` 秒分配到第 `j` 项任务，那么在 `t + tasks[j]` 时它将恢复空闲状态。

如果没有空闲服务器，则必须等待，直到出现一台空闲服务器，并 **尽可能早**  地处理剩余任务。 如果有多项任务等待分配，则按照 **下标递增** 的顺序完成分配。

如果同一时刻存在多台空闲服务器，可以同时将多项任务分别分配给它们。

构建长度为  `m` 的答案数组 `ans` ，其中 `ans[j]` 是第 `j` 项任务分配的服务器的下标。

返回答案数组 `ans` ​​​​ 。

 

 **示例 1：** 

```

输入：servers = [3,3,2], tasks = [1,2,3,2,1,2]
输出：[2,2,0,2,1,2]
解释：事件按时间顺序如下：
- 0 秒时，第 0 项任务加入到任务队列，使用第 2 台服务器处理到 1 秒。
- 1 秒时，第 2 台服务器空闲，第 1 项任务加入到任务队列，使用第 2 台服务器处理到 3 秒。
- 2 秒时，第 2 项任务加入到任务队列，使用第 0 台服务器处理到 5 秒。
- 3 秒时，第 2 台服务器空闲，第 3 项任务加入到任务队列，使用第 2 台服务器处理到 5 秒。
- 4 秒时，第 4 项任务加入到任务队列，使用第 1 台服务器处理到 5 秒。
- 5 秒时，所有服务器都空闲，第 5 项任务加入到任务队列，使用第 2 台服务器处理到 7 秒。
```
 **示例 2：** 

```

输入：servers = [5,1,4,3,2], tasks = [2,1,2,4,5,2,1]
输出：[1,4,1,4,1,3,2]
解释：事件按时间顺序如下：
- 0 秒时，第 0 项任务加入到任务队列，使用第 1 台服务器处理到 2 秒。
- 1 秒时，第 1 项任务加入到任务队列，使用第 4 台服务器处理到 2 秒。
- 2 秒时，第 1 台和第 4 台服务器空闲，第 2 项任务加入到任务队列，使用第 1 台服务器处理到 4 秒。
- 3 秒时，第 3 项任务加入到任务队列，使用第 4 台服务器处理到 7 秒。
- 4 秒时，第 1 台服务器空闲，第 4 项任务加入到任务队列，使用第 1 台服务器处理到 9 秒。
- 5 秒时，第 5 项任务加入到任务队列，使用第 3 台服务器处理到 7 秒。
- 6 秒时，第 6 项任务加入到任务队列，使用第 2 台服务器处理到 7 秒。
```
 

 **提示：** 
-  `servers.length == n` 
-  `tasks.length == m` 
-  `1 <= n, m <= 2 * 10^5` 
-  `1 <= servers[i], tasks[j] <= 2 * 10^5` 
 
**标签**
`数组` `堆（优先队列）` 


## 
```python

```
>
# 1883.准时抵达会议现场的最小跳过休息次数
[https://leetcode-cn.com/problems/minimum-skips-to-arrive-at-meeting-on-time](https://leetcode-cn.com/problems/minimum-skips-to-arrive-at-meeting-on-time) 
## 原题
给你一个整数 `hoursBefore` ，表示你要前往会议所剩下的可用小时数。要想成功抵达会议现场，你必须途经 `n` 条道路。道路的长度用一个长度为 `n` 的整数数组 `dist` 表示，其中 `dist[i]` 表示第 `i` 条道路的长度（单位： **千米** ）。另给你一个整数 `speed` ，表示你在道路上前进的速度（单位： **千米每小时** ）。

当你通过第 `i` 条路之后，就必须休息并等待，直到 **下一个整数小时** 才能开始继续通过下一条道路。注意：你不需要在通过最后一条道路后休息，因为那时你已经抵达会议现场。
- 例如，如果你通过一条道路用去 `1.4` 小时，那你必须停下来等待，到  `2` 小时才可以继续通过下一条道路。如果通过一条道路恰好用去 `2` 小时，就无需等待，可以直接继续。
然而，为了能准时到达，你可以选择 **跳过** 一些路的休息时间，这意味着你不必等待下一个整数小时。注意，这意味着与不跳过任何休息时间相比，你可能在不同时刻到达接下来的道路。
- 例如，假设通过第 `1` 条道路用去 `1.4` 小时，且通过第 `2` 条道路用去 `0.6` 小时。跳过第 `1` 条道路的休息时间意味着你将会在恰好  `2` 小时完成通过第 `2` 条道路，且你能够立即开始通过第 `3` 条道路。
返回准时抵达会议现场所需要的 **最小跳过次数** ，如果 **无法准时参会** ，返回 `-1` 。

 

 **示例 1：** 

```

输入：dist = [1,3,2], speed = 4, hoursBefore = 2
输出：1
解释：
不跳过任何休息时间，你将用 (1/4 + 3/4) + (3/4 + 1/4) + (2/4) = 2.5 小时才能抵达会议现场。
可以跳过第 1 次休息时间，共用 ((1/4 + 0) + (3/4 + 0)) + (2/4) = 1.5 小时抵达会议现场。
注意，第 2 次休息时间缩短为 0 ，由于跳过第 1 次休息时间，你是在整数小时处完成通过第 2 条道路。

```
 **示例 2：** 

```

输入：dist = [7,3,5,5], speed = 2, hoursBefore = 10
输出：2
解释：
不跳过任何休息时间，你将用 (7/2 + 1/2) + (3/2 + 1/2) + (5/2 + 1/2) + (5/2) = 11.5 小时才能抵达会议现场。
可以跳过第 1 次和第 3 次休息时间，共用 ((7/2 + 0) + (3/2 + 0)) + ((5/2 + 0) + (5/2)) = 10 小时抵达会议现场。

```
 **示例 3：** 

```

输入：dist = [7,3,5,5], speed = 1, hoursBefore = 10
输出：-1
解释：即使跳过所有的休息时间，也无法准时参加会议。

```
 

 **提示：** 
-  `n == dist.length` 
-  `1 <= n <= 1000` 
-  `1 <= dist[i] <= 10^5` 
-  `1 <= speed <= 10^6` 
-  `1 <= hoursBefore <= 10^7` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1884.鸡蛋掉落-两枚鸡蛋
[https://leetcode-cn.com/problems/egg-drop-with-2-eggs-and-n-floors](https://leetcode-cn.com/problems/egg-drop-with-2-eggs-and-n-floors) 
## 原题
给你 **2 枚相同** 的鸡蛋，和一栋从第 `1` 层到第 `n` 层共有 `n` 层楼的建筑。

已知存在楼层 `f` ，满足 `0 <= f <= n` ，任何从 **高于** `f` 的楼层落下的鸡蛋都 **会碎** ，从 ** `f` 楼层或比它低** 的楼层落下的鸡蛋都 **不会碎** 。

每次操作，你可以取一枚 **没有碎** 的鸡蛋并把它从任一楼层 `x` 扔下（满足 `1 <= x <= n` ）。如果鸡蛋碎了，你就不能再次使用它。如果某枚鸡蛋扔下后没有摔碎，则可以在之后的操作中 **重复使用** 这枚鸡蛋。

请你计算并返回要确定 `f` **确切的值** 的 **最小操作次数** 是多少？

 

 **示例 1：** 

```

输入：n = 2
输出：2
解释：我们可以将第一枚鸡蛋从 1 楼扔下，然后将第二枚从 2 楼扔下。
如果第一枚鸡蛋碎了，可知 f = 0；
如果第二枚鸡蛋碎了，但第一枚没碎，可知 f = 1；
否则，当两个鸡蛋都没碎时，可知 f = 2。

```
 **示例 2：** 

```

输入：n = 100
输出：14
解释：
一种最优的策略是：
- 将第一枚鸡蛋从 9 楼扔下。如果碎了，那么 f 在 0 和 8 之间。将第二枚从 1 楼扔下，然后每扔一次上一层楼，在 8 次内找到 f 。总操作次数 = 1 + 8 = 9 。
- 如果第一枚鸡蛋没有碎，那么再把第一枚鸡蛋从 22 层扔下。如果碎了，那么 f 在 9 和 21 之间。将第二枚鸡蛋从 10 楼扔下，然后每扔一次上一层楼，在 12 次内找到 f 。总操作次数 = 2 + 12 = 14 。
- 如果第一枚鸡蛋没有再次碎掉，则按照类似的方法从 34, 45, 55, 64, 72, 79, 85, 90, 94, 97, 99 和 100 楼分别扔下第一枚鸡蛋。
不管结果如何，最多需要扔 14 次来确定 f 。

```
 

 **提示：** 
-  `1 <= n <= 1000` 
 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 1885.统计数对
[https://leetcode-cn.com/problems/count-pairs-in-two-arrays](https://leetcode-cn.com/problems/count-pairs-in-two-arrays) 
## 原题

 
**标签**
`数组` `二分查找` `排序` 


## 
```python

```
>
# 1886.判断矩阵经轮转后是否一致
[https://leetcode-cn.com/problems/determine-whether-matrix-can-be-obtained-by-rotation](https://leetcode-cn.com/problems/determine-whether-matrix-can-be-obtained-by-rotation) 
## 原题
给你两个大小为 `n x n` 的二进制矩阵 `mat` 和 `target` 。现 **以 90 度顺时针轮转** 矩阵 `mat` 中的元素 **若干次** ，如果能够使 `mat` 与  `target` 一致，返回 `true` ；否则，返回 `false` *。* 

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid3.png" style="width: 301px; height: 121px;" />
```

输入：mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
输出：true
解释：顺时针轮转 90 度一次可以使 mat 和 target 一致。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid4.png" style="width: 301px; height: 121px;" />
```

输入：mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
输出：false
解释：无法通过轮转矩阵中的元素使 equal 与 target 一致。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/26/grid4.png" style="width: 661px; height: 184px;" />
```

输入：mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
输出：true
解释：顺时针轮转 90 度两次可以使 mat 和 target 一致。

```
 

 **提示：** 
-  `n == mat.length == target.length` 
-  `n == mat[i].length == target[i].length` 
-  `1 <= n <= 10` 
-  `mat[i][j]` 和 `target[i][j]` 不是 `0` 就是 `1` 
 
**标签**
`数组` `矩阵` 


## 
```python

```
>
# 1887.使数组元素相等的减少操作次数
[https://leetcode-cn.com/problems/reduction-operations-to-make-the-array-elements-equal](https://leetcode-cn.com/problems/reduction-operations-to-make-the-array-elements-equal) 
## 原题
给你一个整数数组 `nums` ，你的目标是令 `nums` 中的所有元素相等。完成一次减少操作需要遵照下面的几个步骤：
- 找出 `nums` 中的 **最大** 值。记这个值为 `largest` 并取其下标 `i` （ **下标从 0 开始计数** ）。如果有多个元素都是最大值，则取最小的 `i` 。
- 找出 `nums` 中的 **下一个最大** 值，这个值 **严格小于** `largest` ，记为 `nextLargest` 。
- 将 `nums[i]` 减少到 `nextLargest` 。
返回使 `nums` 中的所有元素相等的操作次数。

 

 **示例 1：** 

```

输入：nums = [5,1,3]
输出：3
解释：需要 3 次操作使 nums 中的所有元素相等：
1. largest = 5 下标为 0 。nextLargest = 3 。将 nums[0] 减少到 3 。nums = [3,1,3] 。
2. largest = 3 下标为 0 。nextLargest = 1 。将 nums[0] 减少到 1 。nums = [1,1,3] 。
3. largest = 3 下标为 2 。nextLargest = 1 。将 nums[2] 减少到 1 。nums = [1,1,1] 。

```
 **示例 2：** 

```

输入：nums = [1,1,1]
输出：0
解释：nums 中的所有元素已经是相等的。

```
 **示例 3：** 

```

输入：nums = [1,1,2,2,3]
输出：4
解释：需要 4 次操作使 nums 中的所有元素相等：
1. largest = 3 下标为 4 。nextLargest = 2 。将 nums[4] 减少到 2 。nums = [1,1,2,2,2] 。
2. largest = 2 下标为 2 。nextLargest = 1 。将 nums[2] 减少到 1 。nums = [1,1,1,2,2] 。 
3. largest = 2 下标为 3 。nextLargest = 1 。将 nums[3] 减少到 1 。nums = [1,1,1,1,2] 。 
4. largest = 2 下标为 4 。nextLargest = 1 。将 nums[4] 减少到 1 。nums = [1,1,1,1,1] 。

```
 

 **提示：** 
-  `1 <= nums.length <= 5 * 10^4` 
-  `1 <= nums[i] <= 5 * 10^4` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 1888.使二进制字符串字符交替的最少反转次数
[https://leetcode-cn.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating](https://leetcode-cn.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating) 
## 原题
给你一个二进制字符串  `s`  。你可以按任意顺序执行以下两种操作任意次：
-  **类型 1 ：删除** 字符串  `s`  的第一个字符并将它 **添加**  到字符串结尾。
-  **类型 2 ：选择** 字符串  `s`  中任意一个字符并将该字符  **反转 ** ，也就是如果值为  `'0'`  ，则反转得到  `'1'`  ，反之亦然。
请你返回使 `s`  变成 **交替** 字符串的前提下，  **类型 2 ** 的 **最少**  操作次数 。

我们称一个字符串是 **交替**  的，需要满足任意相邻字符都不同。
- 比方说，字符串  `"010"` 和  `"1010"`  都是交替的，但是字符串  `"0100"`  不是。
 

 **示例 1：** 

```
输入：s = "111000"
输出：2
解释：执行第一种操作两次，得到 s = "100011" 。
然后对第三个和第六个字符执行第二种操作，得到 s = "101010" 。

```
 **示例 2：** 

```
输入：s = "010"
输出：0
解释：字符串已经是交替的。

```
 **示例 3：** 

```
输入：s = "1110"
输出：1
解释：对第二个字符执行第二种操作，得到 s = "1010" 。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s[i]`  要么是  `'0'`  ，要么是  `'1'`  。
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 1889.装包裹的最小浪费空间
[https://leetcode-cn.com/problems/minimum-space-wasted-from-packaging](https://leetcode-cn.com/problems/minimum-space-wasted-from-packaging) 
## 原题
给你  `n`  个包裹，你需要把它们装在箱子里， **每个箱子装一个包裹** 。总共有  `m`  个供应商提供 **不同尺寸**  的箱子（每个规格都有无数个箱子）。如果一个包裹的尺寸 **小于等于**  一个箱子的尺寸，那么这个包裹就可以放入这个箱子之中。

包裹的尺寸用一个整数数组  `packages`  表示，其中  `packages[i]`  是第  `i`  个包裹的尺寸。供应商用二维数组  `boxes`  表示，其中  `boxes[j]`  是第 `j`  个供应商提供的所有箱子尺寸的数组。

你想要选择 **一个供应商**  并只使用该供应商提供的箱子，使得 **总浪费空间最小**  。对于每个装了包裹的箱子，我们定义 **浪费的**  空间等于 `箱子的尺寸 - 包裹的尺寸`  。 **总浪费空间**  为  **所有**  箱子中浪费空间的总和。
- 比方说，如果你想要用尺寸数组为  `[4,8]`  的箱子装下尺寸为  `[2,3,5]`  的包裹，你可以将尺寸为 `2`  和 `3`  的两个包裹装入两个尺寸为 `4`  的箱子中，同时把尺寸为 `5`  的包裹装入尺寸为 `8`  的箱子中。总浪费空间为  `(4-2) + (4-3) + (8-5) = 6`  。
请你选择 **最优**  箱子供应商，使得 **总浪费空间最小**  。如果 **无法** 将所有包裹放入箱子中，请你返回 `-1`  。由于答案可能会 **很大**  ，请返回它对 ** ** `10^9 + 7`  <b>取余</b> 的结果。

 

 **示例 1：** 

```

输入：packages = [2,3,5], boxes = [[4,8],[2,8]]
输出：6
解释：选择第一个供应商最优，用两个尺寸为 4 的箱子和一个尺寸为 8 的箱子。
总浪费空间为 (4-2) + (4-3) + (8-5) = 6 。

```
 **示例 2：** 

```

输入：packages = [2,3,5], boxes = [[1,4],[2,3],[3,4]]
输出：-1
解释：没有箱子能装下尺寸为 5 的包裹。

```
 **示例 3：** 

```

输入：packages = [3,5,8,10,11,12], boxes = [[12],[11,9],[10,5,14]]
输出：9
解释：选择第三个供应商最优，用两个尺寸为 5 的箱子，两个尺寸为 10 的箱子和两个尺寸为 14 的箱子。
总浪费空间为 (5-3) + (5-5) + (10-8) + (10-10) + (14-11) + (14-12) = 9 。

```
 

 **提示：** 
-  `n == packages.length` 
-  `m == boxes.length` 
-  `1 <= n <= 10^5` 
-  `1 <= m <= 10^5` 
-  `1 <= packages[i] <= 10^5` 
-  `1 <= boxes[j].length <= 10^5` 
-  `1 <= boxes[j][k] <= 10^5` 
-  `sum(boxes[j].length) <= 10^5` 
-  `boxes[j]`  中的元素 **互不相同**  。
 
**标签**
`数组` `二分查找` `前缀和` `排序` 


## 
```python

```
>
# 1890.2020年最后一次登录
[https://leetcode-cn.com/problems/the-latest-login-in-2020](https://leetcode-cn.com/problems/the-latest-login-in-2020) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1891.割绳子
[https://leetcode-cn.com/problems/cutting-ribbons](https://leetcode-cn.com/problems/cutting-ribbons) 
## 原题

 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 1892.页面推荐Ⅱ
[https://leetcode-cn.com/problems/page-recommendations-ii](https://leetcode-cn.com/problems/page-recommendations-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1893.检查是否区域内所有整数都被覆盖
[https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered](https://leetcode-cn.com/problems/check-if-all-the-integers-in-a-range-are-covered) 
## 原题
给你一个二维整数数组  `ranges`  和两个整数  `left`  和  `right`  。每个  `ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]`  表示一个从  `start<sub>i</sub>`  到  `end<sub>i</sub>`  的  **闭区间**  。

如果闭区间  `[left, right]`  内每个整数都被  `ranges`  中  **至少一个**  区间覆盖，那么请你返回  `true`  ，否则返回  `false`  。

已知区间 `ranges[i] = [start<sub>i</sub>, end<sub>i</sub>]` ，如果整数 `x` 满足 `start<sub>i</sub> <= x <= end<sub>i</sub>`  ，那么我们称整数 `x`  被覆盖了。

 

 **示例 1：** 

```

输入：ranges = [[1,2],[3,4],[5,6]], left = 2, right = 5
输出：true
解释：2 到 5 的每个整数都被覆盖了：
- 2 被第一个区间覆盖。
- 3 和 4 被第二个区间覆盖。
- 5 被第三个区间覆盖。

```
 **示例 2：** 

```

输入：ranges = [[1,10],[10,20]], left = 21, right = 21
输出：false
解释：21 没有被任何一个区间覆盖。

```
 

 **提示：** 
-  `1 <= ranges.length <= 50` 
-  `1 <= start<sub>i</sub> <= end<sub>i</sub> <= 50` 
-  `1 <= left <= right <= 50` 
 
**标签**
`数组` `哈希表` `前缀和` 


## 
```python

```
>
# 1894.找到需要补充粉笔的学生编号
[https://leetcode-cn.com/problems/find-the-student-that-will-replace-the-chalk](https://leetcode-cn.com/problems/find-the-student-that-will-replace-the-chalk) 
## 原题
一个班级里有  `n`  个学生，编号为 `0`  到 `n - 1`  。每个学生会依次回答问题，编号为 `0`  的学生先回答，然后是编号为 `1`  的学生，以此类推，直到编号为 `n - 1`  的学生，然后老师会重复这个过程，重新从编号为 `0`  的学生开始回答问题。

给你一个长度为 `n`  且下标从 `0`  开始的整数数组  `chalk`  和一个整数  `k`  。一开始粉笔盒里总共有  `k`  支粉笔。当编号为  `i`  的学生回答问题时，他会消耗 `chalk[i]`  支粉笔。如果剩余粉笔数量 **严格小于**   `chalk[i]`  ，那么学生 `i`  需要 **补充**  粉笔。

请你返回需要 **补充**  粉笔的学生 **编号**  。

 

 **示例 1：** 

```
输入：chalk = [5,1,5], k = 22
输出：0
解释：学生消耗粉笔情况如下：
- 编号为 0 的学生使用 5 支粉笔，然后 k = 17 。
- 编号为 1 的学生使用 1 支粉笔，然后 k = 16 。
- 编号为 2 的学生使用 5 支粉笔，然后 k = 11 。
- 编号为 0 的学生使用 5 支粉笔，然后 k = 6 。
- 编号为 1 的学生使用 1 支粉笔，然后 k = 5 。
- 编号为 2 的学生使用 5 支粉笔，然后 k = 0 。
编号为 0 的学生没有足够的粉笔，所以他需要补充粉笔。
```
 **示例 2：** 

```
输入：chalk = [3,4,1,2], k = 25
输出：1
解释：学生消耗粉笔情况如下：
- 编号为 0 的学生使用 3 支粉笔，然后 k = 22 。
- 编号为 1 的学生使用 4 支粉笔，然后 k = 18 。
- 编号为 2 的学生使用 1 支粉笔，然后 k = 17 。
- 编号为 3 的学生使用 2 支粉笔，然后 k = 15 。
- 编号为 0 的学生使用 3 支粉笔，然后 k = 12 。
- 编号为 1 的学生使用 4 支粉笔，然后 k = 8 。
- 编号为 2 的学生使用 1 支粉笔，然后 k = 7 。
- 编号为 3 的学生使用 2 支粉笔，然后 k = 5 。
- 编号为 0 的学生使用 3 支粉笔，然后 k = 2 。
编号为 1 的学生没有足够的粉笔，所以他需要补充粉笔。

```
 

 **提示：** 
-  `chalk.length == n` 
-  `1 <= n <= 10^5` 
-  `1 <= chalk[i] <= 10^5` 
-  `1 <= k <= 10^9` 
 
**标签**
`数组` `二分查找` `前缀和` `模拟` 


## 
```python

```
>
# 1895.最大的幻方
[https://leetcode-cn.com/problems/largest-magic-square](https://leetcode-cn.com/problems/largest-magic-square) 
## 原题
一个  `k x k`  的 ** 幻方**  指的是一个  `k x k`  填满整数的方格阵，且每一行、每一列以及两条对角线的和 **全部** **相等**  。幻方中的整数 **不需要互不相同**  。显然，每个  `1 x 1`  的方格都是一个幻方。

给你一个  `m x n`  的整数矩阵  `grid`  ，请你返回矩阵中  **最大幻方**  的  **尺寸**  （即边长 `k` ）。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/29/magicsquare-grid.jpg" style="width: 413px; height: 335px;">
```
输入：grid = [[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]
输出：3
解释：最大幻方尺寸为 3 。
每一行，每一列以及两条对角线的和都等于 12 。
- 每一行的和：5+1+6 = 5+4+3 = 2+7+3 = 12
- 每一列的和：5+5+2 = 1+4+7 = 6+3+3 = 12
- 对角线的和：5+4+3 = 6+4+2 = 12

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/29/magicsquare2-grid.jpg" style="width: 333px; height: 255px;">
```
输入：grid = [[5,1,3,1],[9,3,3,1],[1,3,3,8]]
输出：2

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 50` 
-  `1 <= grid[i][j] <= 10^6` 
 
**标签**
`数组` `矩阵` `前缀和` 


## 
```python

```
>
# 1896.反转表达式值的最少操作次数
[https://leetcode-cn.com/problems/minimum-cost-to-change-the-final-value-of-expression](https://leetcode-cn.com/problems/minimum-cost-to-change-the-final-value-of-expression) 
## 原题
给你一个 **有效的**  布尔表达式，用字符串  `expression`  表示。这个字符串包含字符  `'1'` ， `'0'` ， `'&amp;'` （按位 **与**  运算）， `'|'` （按位 **或**  运算）， `'('`  和  `')'`  。
- 比方说， `"()1|1"` 和  `"(1)&amp;()"`   **不是有效**  布尔表达式。而  `"1"` ，  `"(((1))|(0))"`  和  `"1|(0&amp;(1))"`  是 **有效**  布尔表达式。
你的目标是将布尔表达式的 **值**   **反转** （也就是将 `0`  变为 `1`  ，或者将 `1`  变为 `0` ），请你返回达成目标需要的 **最少操作**  次数。
- 比方说，如果表达式  `expression = "1|1|(0&amp;0)&amp;1"`  ，它的  **值**  为  `1|1|(0&amp;0)&amp;1 = 1|1|0&amp;1 = 1|0&amp;1 = 1&amp;1 = 1`  。我们想要执行操作将  **新的**  表达式的值变成  `0`  。
可执行的 **操作**  如下：
- 将一个  `'1'`  变成一个  `'0'`  。
- 将一个  `'0'`  变成一个  `'1'`  。
- 将一个  `'&amp;'` 变成一个  `'|'`  。
- 将一个  `'|'`  变成一个  `'&amp;'`  。
 **注意：** `'&amp;'`  的 **运算优先级**  与  `'|'` **相同**  。计算表达式时，括号优先级 **最高**  ，然后按照 **从左到右** 的顺序运算。

 

 **示例 1：** 

```
输入：expression = "1&amp;(0|1)"
输出：1
解释：我们可以将 "1&amp;(0|1)" 变成 "1&amp;(0&amp;1)" ，执行的操作为将一个 '|' 变成一个 '&amp;' ，执行了 1 次操作。
新表达式的值为 0 。

```
 **示例 2：** 

```
输入：expression = "(0&amp;0)&amp;(0&amp;0&amp;0)"
输出：3
解释：我们可以将 "(0&amp;0)&amp;(0&amp;0&amp;0)" 变成 "(0|1)|(0&amp;0&amp;0)" ，执行了 3 次操作。
新表达式的值为 1 。

```
 **示例 3：** 

```
输入：expression = "(0|(1|0&amp;1))"
输出：1
解释：我们可以将 "(0|(1|0&amp;1))" 变成 "(0|(0|0&amp;1))" ，执行了 1 次操作。
新表达式的值为 0 。
```
 

 **提示：** 
-  `1 <= expression.length <= 10^5` 
-  `expression`  只包含  `'1'` ， `'0'` ， `'&amp;'` ， `'|'` ， `'('`  和  `')'` 
- 所有括号都有与之匹配的对应括号。
- 不会有空的括号（也就是说  `"()"`  不是  `expression` 的子字符串）。
 
**标签**
`栈` `数学` `字符串` `动态规划` 


## 
```python

```
>
# 1897.重新分配字符使所有字符串都相等
[https://leetcode-cn.com/problems/redistribute-characters-to-make-all-strings-equal](https://leetcode-cn.com/problems/redistribute-characters-to-make-all-strings-equal) 
## 原题
给你一个字符串数组 `words` （下标 **从 0 开始** 计数）。

在一步操作中，需先选出两个 **不同** 下标 `i` 和 `j` ，其中 `words[i]` 是一个非空字符串，接着将 `words[i]` 中的 **任一** 字符移动到 `words[j]` 中的 **任一** 位置上。

如果执行任意步操作可以使 `words` 中的每个字符串都相等，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```
输入：words = ["abc","aabc","bc"]
输出：true
解释：将 words[1] 中的第一个 'a' 移动到 words[2] 的最前面。
使 words[1] = "abc" 且 words[2] = "abc" 。
所有字符串都等于 "abc" ，所以返回 true 。

```
 **示例 2：** 

```
输入：words = ["ab","a"]
输出：false
解释：执行操作无法使所有字符串都相等。

```
 

 **提示：** 
-  `1 <= words.length <= 100` 
-  `1 <= words[i].length <= 100` 
-  `words[i]` 由小写英文字母组成
 
**标签**
`哈希表` `字符串` `计数` 


## 
```python

```
>
# 1898.可移除字符的最大数目
[https://leetcode-cn.com/problems/maximum-number-of-removable-characters](https://leetcode-cn.com/problems/maximum-number-of-removable-characters) 
## 原题
给你两个字符串 `s` 和 `p` ，其中 `p` 是 `s` 的一个 **子序列** 。同时，给你一个元素 **互不相同** 且下标 **从 0 开始** 计数的整数数组  `removable` ，该数组是 `s` 中下标的一个子集（ `s` 的下标也 **从 0 开始** 计数）。

请你找出一个整数 `k` （ `0 <= k <= removable.length` ），选出  `removable` 中的 **前** `k` 个下标，然后从 `s` 中移除这些下标对应的 `k` 个字符。整数 `k` 需满足：在执行完上述步骤后， `p` 仍然是 `s` 的一个 **子序列** 。更正式的解释是，对于每个 `0 <= i < k` ，先标记出位于 `s[removable[i]]` 的字符，接着移除所有标记过的字符，然后检查 `p` 是否仍然是 `s` 的一个子序列。

返回你可以找出的 **最大**  `k` ，满足在移除字符后 `p` 仍然是 `s` 的一个子序列。

字符串的一个 **子序列** 是一个由原字符串生成的新字符串，生成过程中可能会移除原字符串中的一些字符（也可能不移除）但不改变剩余字符之间的相对顺序。

 

 **示例 1：** 

```

输入：s = "abcacb", p = "ab", removable = [3,1,0]
输出：2
解释：在移除下标 3 和 1 对应的字符后，"abcacb" 变成 "accb" 。
"ab" 是 "accb" 的一个子序列。
如果移除下标 3、1 和 0 对应的字符后，"abcacb" 变成 "ccb" ，那么 "ab" 就不再是 s 的一个子序列。
因此，最大的 k 是 2 。

```
 **示例 2：** 

```

输入：s = "abcbddddd", p = "abcd", removable = [3,2,1,4,5,6]
输出：1
解释：在移除下标 3 对应的字符后，"abcbddddd" 变成 "abcddddd" 。
"abcd" 是 "abcddddd" 的一个子序列。

```
 **示例 3：** 

```

输入：s = "abcab", p = "abc", removable = [0,1,2,3,4]
输出：0
解释：如果移除数组 removable 的第一个下标，"abc" 就不再是 s 的一个子序列。

```
 

 **提示：** 
-  `1 <= p.length <= s.length <= 10^5` 
-  `0 <= removable.length < s.length` 
-  `0 <= removable[i] < s.length` 
-  `p` 是 `s` 的一个 **子字符串** 
-  `s` 和 `p` 都由小写英文字母组成
-  `removable` 中的元素 **互不相同** 
 
**标签**
`数组` `字符串` `二分查找` 


## 
```python

```
>
# 1899.合并若干三元组以形成目标三元组
[https://leetcode-cn.com/problems/merge-triplets-to-form-target-triplet](https://leetcode-cn.com/problems/merge-triplets-to-form-target-triplet) 
## 原题
 **三元组** 是一个由三个整数组成的数组。给你一个二维整数数组 `triplets` ，其中 `triplets[i] = [a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>]` 表示第 `i` 个 **三元组** 。同时，给你一个整数数组 `target = [x, y, z]` ，表示你想要得到的 **三元组** 。

为了得到 `target` ，你需要对 `triplets` 执行下面的操作 **任意次** （可能 **零** 次）：
- 选出两个下标（下标 **从 0 开始** 计数） `i` 和 `j` （ `i != j` ），并 **更新** `triplets[j]` 为 `[max(a<sub>i</sub>, a<sub>j</sub>), max(b<sub>i</sub>, b<sub>j</sub>), max(c<sub>i</sub>, c<sub>j</sub>)]` 。

	
- 例如， `triplets[i] = [2, 5, 3]` 且 `triplets[j] = [1, 7, 5]` ， `triplets[j]` 将会更新为 `[max(2, 1), max(5, 7), max(3, 5)] = [2, 7, 5]` 。
	
	
如果通过以上操作我们可以使得目标 **三元组**   `target`  成为  `triplets` 的一个 **元素**  ，则返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：triplets = [[2,5,3],[1,8,4],[1,7,5]], target = [2,7,5]
输出：true
解释：执行下述操作：
- 选择第一个和最后一个三元组 [[2,5,3],[1,8,4],[1,7,5]] 。更新最后一个三元组为 [max(2,1), max(5,7), max(3,5)] = [2,7,5] 。triplets = [[2,5,3],[1,8,4],[2,7,5]]
目标三元组 [2,7,5] 现在是 triplets 的一个元素。

```
 **示例 2：** 

```

输入：triplets = [[1,3,4],[2,5,8]], target = [2,5,8]
输出：true
解释：目标三元组 [2,5,8] 已经是 triplets 的一个元素。

```
 **示例 3：** 

```

输入：triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]], target = [5,5,5]
输出：true
解释：执行下述操作：
- 选择第一个和第三个三元组 [[2,5,3],[2,3,4],[1,2,5],[5,2,3]] 。更新第三个三元组为 [max(2,1), max(5,2), max(3,5)] = [2,5,5] 。triplets = [[2,5,3],[2,3,4],[2,5,5],[5,2,3]] 。
- 选择第三个和第四个三元组 [[2,5,3],[2,3,4],[2,5,5],[5,2,3]] 。更新第四个三元组为 [max(2,5), max(5,2), max(5,3)] = [5,5,5] 。triplets = [[2,5,3],[2,3,4],[2,5,5],[5,5,5]] 。
目标三元组 [5,5,5] 现在是 triplets 的一个元素。

```
 **示例 4：** 

```

输入：triplets = [[3,4,5],[4,5,6]], target = [3,2,5]
输出：false
解释：无法得到 [3,2,5] ，因为 triplets 不含 2 。

```
 

 **提示：** 
-  `1 <= triplets.length <= 10^5` 
-  `triplets[i].length == target.length == 3` 
-  `1 <= a<sub>i</sub>, b<sub>i</sub>, c<sub>i</sub>, x, y, z <= 1000` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1900.最佳运动员的比拼回合
[https://leetcode-cn.com/problems/the-earliest-and-latest-rounds-where-players-compete](https://leetcode-cn.com/problems/the-earliest-and-latest-rounds-where-players-compete) 
## 原题
 `n` 名运动员参与一场锦标赛，所有运动员站成一排，并根据 **最开始的** 站位从 `1` 到 `n` 编号（运动员 `1` 是这一排中的第一个运动员，运动员 `2` 是第二个运动员，依此类推）。

锦标赛由多个回合组成（从回合 `1` 开始）。每一回合中，这一排从前往后数的第 `i` 名运动员需要与从后往前数的第 `i` 名运动员比拼，获胜者将会进入下一回合。如果当前回合中运动员数目为奇数，那么中间那位运动员将轮空晋级下一回合。
- 例如，当前回合中，运动员 `1, 2, 4, 6, 7` 站成一排

	
- 运动员 `1` 需要和运动员 `7` 比拼
- 运动员 `2` 需要和运动员 `6` 比拼
- 运动员 `4` 轮空晋级下一回合
	
	
每回合结束后，获胜者将会基于最开始分配给他们的原始顺序（升序）重新排成一排。

编号为 `firstPlayer` 和 `secondPlayer` 的运动员是本场锦标赛中的最佳运动员。在他们开始比拼之前，完全可以战胜任何其他运动员。而任意两个其他运动员进行比拼时，其中任意一个都有获胜的可能，因此你可以 **裁定** 谁是这一回合的获胜者。

给你三个整数 `n` 、 `firstPlayer` 和 `secondPlayer` 。返回一个由两个值组成的整数数组，分别表示两位最佳运动员在本场锦标赛中比拼的 **最早** 回合数和 **最晚** 回合数。

 

 **示例 1：** 

```
输入：n = 11, firstPlayer = 2, secondPlayer = 4
输出：[3,4]
解释：
一种能够产生最早回合数的情景是：
回合 1：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
回合 2：2, 3, 4, 5, 6, 11
回合 3：2, 3, 4
一种能够产生最晚回合数的情景是：
回合 1：1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
回合 2：1, 2, 3, 4, 5, 6
回合 3：1, 2, 4
回合 4：2, 4

```
 **示例 2：** 

```
输入：n = 5, firstPlayer = 1, secondPlayer = 5
输出：[1,1]
解释：两名最佳运动员 1 和 5 将会在回合 1 进行比拼。
不存在使他们在其他回合进行比拼的可能。

```
 

 **提示：** 
-  `2 <= n <= 28` 
-  `1 <= firstPlayer < secondPlayer <= n` 
 
**标签**
`记忆化搜索` `动态规划` 


## 
```python

```
>
