# 1301.最大得分的路径数目
[https://leetcode-cn.com/problems/number-of-paths-with-max-score](https://leetcode-cn.com/problems/number-of-paths-with-max-score) 
## 原题
给你一个正方形字符数组 `board` ，你从数组最右下方的字符 `';S';` 出发。

你的目标是到达数组最左上角的字符 `';E';` ，数组剩余的部分为数字字符 `1, 2, ..., 9` 或者障碍 `';X';` 。在每一步移动中，你可以向上、向左或者左上方移动，可以移动的前提是到达的格子没有障碍。

一条路径的 「得分」 定义为：路径上所有数字的和。

请你返回一个列表，包含两个整数：第一个整数是 「得分」 的最大值，第二个整数是得到最大得分的方案数，请把结果对 ** `10^9 + 7` ** **取余** 。

如果没有任何路径可以到达终点，请返回 `[0, 0]` 。

 

 **示例 1：** 

```

输入：board = ["E23","2X2","12S"]
输出：[7,1]

```
 **示例 2：** 

```

输入：board = ["E12","1X1","21S"]
输出：[4,2]

```
 **示例 3：** 

```

输入：board = ["E11","XXX","11S"]
输出：[0,0]

```
 

 **提示：** 
-  `2 <= board.length == board[i].length <= 100` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 1302.层数最深叶子节点的和
[https://leetcode-cn.com/problems/deepest-leaves-sum](https://leetcode-cn.com/problems/deepest-leaves-sum) 
## 原题
给你一棵二叉树的根节点 `root` ，请你返回 **层数最深的叶子节点的和** 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/28/1483_ex1.png" style="height: 265px; width: 273px;" />** 

```

输入：root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
输出：15

```
 **示例 2：** 

```

输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：19

```
 

 **提示：** 
- 树中节点数目在范围 `[1, 10^4]`  之间。
-  `1 <= Node.val <= 100` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 1303.求团队人数
[https://leetcode-cn.com/problems/find-the-team-size](https://leetcode-cn.com/problems/find-the-team-size) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1304.和为零的N个唯一整数
[https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero](https://leetcode-cn.com/problems/find-n-unique-integers-sum-up-to-zero) 
## 原题
给你一个整数 `n` ，请你返回 **任意** 一个由 `n` 个 **各不相同** 的整数组成的数组，并且这 `n` 个数相加和为 `0` 。

 

 **示例 1：** 

```
输入：n = 5
输出：[-7,-1,1,3,4]
解释：这些数组也是正确的 [-5,-1,1,2,3]，[-3,-1,2,-2,4]。

```
 **示例 2：** 

```
输入：n = 3
输出：[-1,0,1]

```
 **示例 3：** 

```
输入：n = 1
输出：[0]

```
 

 **提示：** 
-  `1 <= n <= 1000` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 1305.两棵二叉搜索树中的所有元素
[https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees](https://leetcode-cn.com/problems/all-elements-in-two-binary-search-trees) 
## 原题
给你 `root1` 和 `root2` 这两棵二叉搜索树。请你返回一个列表，其中包含 **两棵树** 中的所有整数并按 **升序** 排序。.

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/29/q2-e1.png" />

```

输入：root1 = [2,1,4], root2 = [1,0,3]
输出：[0,1,1,2,3,4]

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/12/29/q2-e5-.png" />

```

输入：root1 = [1,null,8], root2 = [8,1]
输出：[1,1,8,8]

```
 

 **提示：** 
- 每棵树的节点数在 `[0, 5000]` 范围内
-  `-10^5 <= Node.val <= 10^5` 
 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` `排序` 


## 
```python

```
>
# 1306.跳跃游戏 III
[https://leetcode-cn.com/problems/jump-game-iii](https://leetcode-cn.com/problems/jump-game-iii) 
## 原题
这里有一个非负整数数组 `arr` ，你最开始位于该数组的起始下标 `start` 处。当你位于下标 `i` 处时，你可以跳到 `i + arr[i]` 或者 `i - arr[i]` 。

请你判断自己是否能够跳到对应元素值为 0 的 **任一** 下标处。

注意，不管是什么情况下，你都无法跳到数组之外。

 

 **示例 1：** 

```
输入：arr = [4,2,3,0,3,1,2], start = 5
输出：true
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 5 -> 下标 4 -> 下标 1 -> 下标 3 
下标 5 -> 下标 6 -> 下标 4 -> 下标 1 -> 下标 3 

```
 **示例 2：** 

```
输入：arr = [4,2,3,0,3,1,2], start = 0
输出：true 
解释：
到达值为 0 的下标 3 有以下可能方案： 
下标 0 -> 下标 4 -> 下标 1 -> 下标 3

```
 **示例 3：** 

```
输入：arr = [3,0,2,1,2], start = 2
输出：false
解释：无法到达值为 0 的下标 1 处。 

```
 

 **提示：** 
-  `1 <= arr.length <= 5 * 10^4` 
-  `0 <= arr[i] < arr.length` 
-  `0 <= start < arr.length` 
 
**标签**
`深度优先搜索` `广度优先搜索` `数组` 


## 
```python

```
>
# 1307.口算难题
[https://leetcode-cn.com/problems/verbal-arithmetic-puzzle](https://leetcode-cn.com/problems/verbal-arithmetic-puzzle) 
## 原题
给你一个方程，左边用 `words` 表示，右边用 `result` 表示。

你需要根据以下规则检查方程是否可解：
- 每个字符都会被解码成一位数字（0 - 9）。
- 每对不同的字符必须映射到不同的数字。
- 每个 `words[i]` 和 `result` 都会被解码成一个没有前导零的数字。
- 左侧数字之和（ `words` ）等于右侧数字（ `result` ）。 
如果方程可解，返回 `True` ，否则返回 `False` 。

 

 **示例 1：** 

```
输入：words = ["SEND","MORE"], result = "MONEY"
输出：true
解释：映射 ';S';-> 9, ';E';->5, ';N';->6, ';D';->7, ';M';->1, ';O';->0, ';R';->8, ';Y';->';2';
所以 "SEND" + "MORE" = "MONEY" ,  9567 + 1085 = 10652
```
 **示例 2：** 

```
输入：words = ["SIX","SEVEN","SEVEN"], result = "TWENTY"
输出：true
解释：映射 ';S';-> 6, ';I';->5, ';X';->0, ';E';->8, ';V';->7, ';N';->2, ';T';->1, ';W';->';3';, ';Y';->4
所以 "SIX" + "SEVEN" + "SEVEN" = "TWENTY" ,  650 + 68782 + 68782 = 138214
```
 **示例 3：** 

```
输入：words = ["THIS","IS","TOO"], result = "FUNNY"
输出：true

```
 **示例 4：** 

```
输入：words = ["LEET","CODE"], result = "POINT"
输出：false

```
 

 **提示：** 
-  `2 <= words.length <= 5` 
-  `1 <= words[i].length, results.length <= 7` 
-  `words[i], result` 只含有大写英文字母
- 表达式中使用的不同字符数最大为 10
 
**标签**
`数组` `数学` `字符串` `回溯` 


## 
```python

```
>
# 1308.不同性别每日分数总计
[https://leetcode-cn.com/problems/running-total-for-different-genders](https://leetcode-cn.com/problems/running-total-for-different-genders) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1309.解码字母到整数映射
[https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping](https://leetcode-cn.com/problems/decrypt-string-from-alphabet-to-integer-mapping) 
## 原题
给你一个字符串 `s` ，它由数字（ `';0';` - `';9';` ）和 `';#';` 组成。我们希望按下述规则将 `s` 映射为一些小写英文字符：
- 字符（ `';a';` - `';i';` ）分别用（ `';1';` - `';9';` ）表示。
- 字符（ `';j';` - `';z';` ）分别用（ `';10#';` - `';26#';` ）表示。 
返回映射之后形成的新字符串。

题目数据保证映射始终唯一。

 

 **示例 1：** 

```
输入：s = "10#11#12"
输出："jkab"
解释："j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".

```
 **示例 2：** 

```
输入：s = "1326#"
输出："acz"

```
 **示例 3：** 

```
输入：s = "25#"
输出："y"

```
 **示例 4：** 

```
输入：s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"
输出："abcdefghijklmnopqrstuvwxyz"

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s[i]` 只包含数字（ `';0';` - `';9';` ）和 `';#';` 字符。
-  `s` 是映射始终存在的有效字符串。
 
**标签**
`字符串` 


## 
```python

```
>
# 1310.子数组异或查询
[https://leetcode-cn.com/problems/xor-queries-of-a-subarray](https://leetcode-cn.com/problems/xor-queries-of-a-subarray) 
## 原题
有一个正整数数组  `arr` ，现给你一个对应的查询数组  `queries` ，其中  `queries[i] = [L<sub>i, </sub>R<sub>i</sub>]` 。

对于每个查询  `i` ，请你计算从  `L<sub>i</sub>`  到  `R<sub>i</sub>`  的  **XOR**  值（即  `arr[L<sub>i</sub>] **xor** arr[L<sub>i</sub>+1] **xor** ... **xor** arr[R<sub>i</sub>]` ）作为本次查询的结果。

并返回一个包含给定查询  `queries`  所有结果的数组。

 

 **示例 1：** 

```

输入：arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
输出：[2,7,14,8] 
解释：
数组中元素的二进制表示形式是：
1 = 0001 
3 = 0011 
4 = 0100 
8 = 1000 
查询的 XOR 值为：
[0,1] = 1 xor 3 = 2 
[1,2] = 3 xor 4 = 7 
[0,3] = 1 xor 3 xor 4 xor 8 = 14 
[3,3] = 8

```
 **示例 2：** 

```

输入：arr = [4,8,2,10], queries = [[2,3],[1,3],[0,0],[0,3]]
输出：[8,0,4,4]

```
 

 **提示：** 
-  `1 <= arr.length <= 3 * 10^4` 
-  `1 <= arr[i] <= 10^9` 
-  `1 <= queries.length <= 3 * 10^4` 
-  `queries[i].length == 2` 
-  `0 <= queries[i][0] <= queries[i][1] < arr.length` 
 
**标签**
`位运算` `数组` `前缀和` 


## 
```python

```
>
# 1311.获取你好友已观看的视频
[https://leetcode-cn.com/problems/get-watched-videos-by-your-friends](https://leetcode-cn.com/problems/get-watched-videos-by-your-friends) 
## 原题
有 `n` 个人，每个人都有一个 `0` 到 `n-1` 的唯一 *id* 。

给你数组 `watchedVideos` 和 `friends` ，其中 `watchedVideos[i]` 和 `friends[i]` 分别表示 `id = i` 的人观看过的视频列表和他的好友列表。

Level **1** 的视频包含所有你好友观看过的视频，level **2** 的视频包含所有你好友的好友观看过的视频，以此类推。一般的，Level 为 **k** 的视频包含所有从你出发，最短距离为 **k** 的好友观看过的视频。

给定你的 `id` 和一个 `level` 值，请你找出所有指定 `level` 的视频，并将它们按观看频率升序返回。如果有频率相同的视频，请将它们按字母顺序从小到大排列。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/03/leetcode_friends_1.png" style="height: 179px; width: 129px;">** 

```
输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 1
输出：["B","C"] 
解释：
你的 id 为 0（绿色），你的朋友包括（黄色）：
id 为 1 -> watchedVideos = ["C"] 
id 为 2 -> watchedVideos = ["B","C"] 
你朋友观看过视频的频率为：
B -> 1 
C -> 2

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/03/leetcode_friends_2.png" style="height: 179px; width: 129px;">** 

```
输入：watchedVideos = [["A","B"],["C"],["B","C"],["D"]], friends = [[1,2],[0,3],[0,3],[1,2]], id = 0, level = 2
输出：["D"]
解释：
你的 id 为 0（绿色），你朋友的朋友只有一个人，他的 id 为 3（黄色）。

```
 

 **提示：** 
-  `n == watchedVideos.length == friends.length` 
-  `2 <= n <= 100` 
-  `1 <= watchedVideos[i].length <= 100` 
-  `1 <= watchedVideos[i][j].length <= 8` 
-  `0 <= friends[i].length < n` 
-  `0 <= friends[i][j] < n` 
-  `0 <= id < n` 
-  `1 <= level < n` 
- 如果 `friends[i]` 包含 `j` ，那么 `friends[j]` 包含 `i` 
 
**标签**
`广度优先搜索` `数组` `哈希表` `排序` 


## 
```python

```
>
# 1312.让字符串成为回文串的最少插入次数
[https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome](https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome) 
## 原题
给你一个字符串 `s` ，每一次操作你都可以在字符串的任意位置插入任意字符。

请你返回让 `s` 成为回文串的 **最少操作次数** 。

「回文串」是正读和反读都相同的字符串。

 

 **示例 1：** 

```

输入：s = "zzazz"
输出：0
解释：字符串 "zzazz" 已经是回文串了，所以不需要做任何插入操作。

```
 **示例 2：** 

```

输入：s = "mbadm"
输出：2
解释：字符串可变为 "mbdadbm" 或者 "mdbabdm" 。

```
 **示例 3：** 

```

输入：s = "leetcode"
输出：5
解释：插入 5 个字符后字符串变为 "leetcodocteel" 。

```
 **示例 4：** 

```

输入：s = "g"
输出：0

```
 **示例 5：** 

```

输入：s = "no"
输出：1

```
 

 **提示：** 
-  `1 <= s.length <= 500` 
-  `s` 中所有字符都是小写字母。
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1313.解压缩编码列表
[https://leetcode-cn.com/problems/decompress-run-length-encoded-list](https://leetcode-cn.com/problems/decompress-run-length-encoded-list) 
## 原题
给你一个以行程长度编码压缩的整数列表  `nums`  。

考虑每对相邻的两个元素 `[freq, val] = [nums[2*i], nums[2*i+1]]`  （其中  `i >= 0`  ），每一对都表示解压后子列表中有 `freq`  个值为  `val`  的元素，你需要从左到右连接所有子列表以生成解压后的列表。

请你返回解压后的列表。

 

 **示例 1：** 

```

输入：nums = [1,2,3,4]
输出：[2,4,4,4]
解释：第一对 [1,2] 代表着 2 的出现频次为 1，所以生成数组 [2]。
第二对 [3,4] 代表着 4 的出现频次为 3，所以生成数组 [4,4,4]。
最后将它们串联到一起 [2] + [4,4,4] = [2,4,4,4]。
```
 **示例 2：** 

```

输入：nums = [1,1,2,3]
输出：[1,3,3]

```
 

 **提示：** 
-  `2 <= nums.length <= 100` 
-  `nums.length % 2 == 0` 
-  `1 <= nums[i] <= 100` 
 
**标签**
`数组` 


## 
```python

```
>
# 1314.矩阵区域和
[https://leetcode-cn.com/problems/matrix-block-sum](https://leetcode-cn.com/problems/matrix-block-sum) 
## 原题
给你一个  `m x n`  的矩阵  `mat`  和一个整数 `k` ，请你返回一个矩阵  `answer`  ，其中每个  `answer[i][j]`  是所有满足下述条件的元素  `mat[r][c]` 的和： 
-  `i - k <= r <= i + k,` 
-  `j - k <= c <= j + k` 且
-  `(r, c)`  在矩阵内。
 

 **示例 1：** 

```

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]

```
 **示例 2：** 

```

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat[i].length` 
-  `1 <= m, n, k <= 100` 
-  `1 <= mat[i][j] <= 100` 
 
**标签**
`数组` `矩阵` `前缀和` 


## 
```python

```
>
# 1315.祖父节点值为偶数的节点和
[https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent](https://leetcode-cn.com/problems/sum-of-nodes-with-even-valued-grandparent) 
## 原题
给你一棵二叉树，请你返回满足以下条件的所有节点的值之和：
- 该节点的祖父节点的值为偶数。（一个节点的祖父节点是指该节点的父节点的父节点。）
如果不存在祖父节点值为偶数的节点，那么返回 `0` 。

 

 **示例：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/10/1473_ex1.png" style="height: 214px; width: 350px;">** 

```
输入：root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
输出：18
解释：图中红色节点的祖父节点的值为偶数，蓝色节点为这些红色节点的祖父节点。

```
 

 **提示：** 
- 树中节点的数目在 `1` 到 `10^4` 之间。
- 每个节点的值在 `1` 到 `100` 之间。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 1316.不同的循环子字符串
[https://leetcode-cn.com/problems/distinct-echo-substrings](https://leetcode-cn.com/problems/distinct-echo-substrings) 
## 原题
给你一个字符串 `text` ，请你返回满足下述条件的 **不同** 非空子字符串的数目：
- 可以写成某个字符串与其自身相连接的形式（即，可以写为 `a + a` ，其中 `a` 是某个字符串）。
例如， `abcabc` 就是 `abc` 和它自身连接形成的。

 

 **示例 1：** 

```
输入：text = "abcabcabc"
输出：3
解释：3 个子字符串分别为 "abcabc"，"bcabca" 和 "cabcab" 。

```
 **示例 2：** 

```
输入：text = "leetcodeleetcode"
输出：2
解释：2 个子字符串为 "ee" 和 "leetcodeleetcode" 。

```
 

 **提示：** 
-  `1 <= text.length <= 2000` 
-  `text` 只包含小写英文字母。
 
**标签**
`字典树` `字符串` `动态规划` `滑动窗口` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 1317.将整数转换为两个无零整数的和
[https://leetcode-cn.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers](https://leetcode-cn.com/problems/convert-integer-to-the-sum-of-two-no-zero-integers) 
## 原题
「无零整数」是十进制表示中 **不含任何 0** 的正整数。

给你一个整数 `n` ，请你返回一个 **由两个整数组成的列表** `[A, B]` ，满足：
-  `A` 和 `B` 都是无零整数
-  `A + B = n` 
题目数据保证至少有一个有效的解决方案。

如果存在多个有效解决方案，你可以返回其中任意一个。

 

 **示例 1：** 

```
输入：n = 2
输出：[1,1]
解释：A = 1, B = 1. A + B = n 并且 A 和 B 的十进制表示形式都不包含任何 0 。

```
 **示例 2：** 

```
输入：n = 11
输出：[2,9]

```
 **示例 3：** 

```
输入：n = 10000
输出：[1,9999]

```
 **示例 4：** 

```
输入：n = 69
输出：[1,68]

```
 **示例 5：** 

```
输入：n = 1010
输出：[11,999]

```
 

 **提示：** 
-  `2 <= n <= 10^4` 
 
**标签**
`数学` 


## 
```python

```
>
# 1318.或运算的最小翻转次数
[https://leetcode-cn.com/problems/minimum-flips-to-make-a-or-b-equal-to-c](https://leetcode-cn.com/problems/minimum-flips-to-make-a-or-b-equal-to-c) 
## 原题
给你三个正整数 `a` 、 `b` 和 `c` 。

你可以对 `a` 和 `b` 的二进制表示进行位翻转操作，返回能够使按位或运算 `a` OR `b` == `c` 成立的最小翻转次数。

「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/11/sample_3_1676.png" style="height: 87px; width: 260px;">

```
输入：a = 2, b = 6, c = 5
输出：3
解释：翻转后 a = 1 , b = 4 , c = 5 使得 a OR b == c
```
 **示例 2：** 

```
输入：a = 4, b = 2, c = 7
输出：1

```
 **示例 3：** 

```
输入：a = 1, b = 2, c = 3
输出：0

```
 

 **提示：** 
-  `1 <= a <= 10^9` 
-  `1 <= b <= 10^9` 
-  `1 <= c <= 10^9` 
 
**标签**
`位运算` 


## 
```python

```
>
# 1319.连通网络的操作次数
[https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected](https://leetcode-cn.com/problems/number-of-operations-to-make-network-connected) 
## 原题
用以太网线缆将 `n` 台计算机连接成一个网络，计算机的编号从 `0` 到 `n-1` 。线缆用 `connections` 表示，其中 `connections[i] = [a, b]` 连接了计算机 `a` 和 `b` 。

网络中的任何一台计算机都可以通过网络直接或者间接访问同一个网络中其他任意一台计算机。

给你这个计算机网络的初始布线 `connections` ，你可以拔开任意两台直连计算机之间的线缆，并用它连接一对未直连的计算机。请你计算并返回使所有计算机都连通所需的最少操作次数。如果不可能，则返回 -1 。 

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/11/sample_1_1677.png" style="height: 167px; width: 570px;">** 

```
输入：n = 4, connections = [[0,1],[0,2],[1,2]]
输出：1
解释：拔下计算机 1 和 2 之间的线缆，并将它插到计算机 1 和 3 上。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/11/sample_2_1677.png" style="height: 175px; width: 660px;">** 

```
输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
输出：2

```
 **示例 3：** 

```
输入：n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
输出：-1
解释：线缆数量不足。

```
 **示例 4：** 

```
输入：n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
输出：0

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `1 <= connections.length <= min(n*(n-1)/2, 10^5)` 
-  `connections[i].length == 2` 
-  `0 <= connections[i][0], connections[i][1] < n` 
-  `connections[i][0] != connections[i][1]` 
- 没有重复的连接。
- 两台计算机不会通过多条线缆连接。
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `图` 


## 
```python

```
>
# 1320.二指输入的的最小距离
[https://leetcode-cn.com/problems/minimum-distance-to-type-a-word-using-two-fingers](https://leetcode-cn.com/problems/minimum-distance-to-type-a-word-using-two-fingers) 
## 原题
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/11/leetcode_keyboard.png" style="height: 250px; width: 417px;">

二指输入法定制键盘在 XY 平面上的布局如上图所示，其中每个大写英文字母都位于某个坐标处，例如字母 **A** 位于坐标 **(0,0)** ，字母 **B** 位于坐标 **(0,1)** ，字母 **P** 位于坐标 **(2,3)** 且字母 **Z** 位于坐标 **(4,1)** 。

给你一个待输入字符串 `word` ，请你计算并返回在仅使用两根手指的情况下，键入该字符串需要的最小移动总距离。坐标 **(x<sub>1</sub>,y<sub>1</sub>)** 和 **(x<sub>2</sub>,y<sub>2</sub>)** 之间的距离是 **|x<sub>1</sub> - x<sub>2</sub>| + |y<sub>1</sub> - y<sub>2</sub>|** 。 

注意，两根手指的起始位置是零代价的，不计入移动总距离。你的两根手指的起始位置也不必从首字母或者前两个字母开始。

 

 **示例 1：** 

```
输入：word = "CAKE"
输出：3
解释： 
使用两根手指输入 "CAKE" 的最佳方案之一是： 
手指 1 在字母 ';C'; 上 -> 移动距离 = 0 
手指 1 在字母 ';A'; 上 -> 移动距离 = 从字母 ';C'; 到字母 ';A'; 的距离 = 2 
手指 2 在字母 ';K'; 上 -> 移动距离 = 0 
手指 2 在字母 ';E'; 上 -> 移动距离 = 从字母 ';K'; 到字母 ';E'; 的距离  = 1 
总距离 = 3

```
 **示例 2：** 

```
输入：word = "HAPPY"
输出：6
解释： 
使用两根手指输入 "HAPPY" 的最佳方案之一是：
手指 1 在字母 ';H'; 上 -> 移动距离 = 0
手指 1 在字母 ';A'; 上 -> 移动距离 = 从字母 ';H'; 到字母 ';A'; 的距离 = 2
手指 2 在字母 ';P'; 上 -> 移动距离 = 0
手指 2 在字母 ';P'; 上 -> 移动距离 = 从字母 ';P'; 到字母 ';P'; 的距离 = 0
手指 1 在字母 ';Y'; 上 -> 移动距离 = 从字母 ';A'; 到字母 ';Y'; 的距离 = 4
总距离 = 6

```
 **示例 3：** 

```
输入：word = "NEW"
输出：3

```
 **示例 4：** 

```
输入：word = "YEAR"
输出：7

```
 

 **提示：** 
-  `2 <= word.length <= 300` 
- 每个 `word[i]` 都是一个大写英文字母。
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1321.餐馆营业额变化增长
[https://leetcode-cn.com/problems/restaurant-growth](https://leetcode-cn.com/problems/restaurant-growth) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1322.广告效果
[https://leetcode-cn.com/problems/ads-performance](https://leetcode-cn.com/problems/ads-performance) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1323.6 和 9 组成的最大数字
[https://leetcode-cn.com/problems/maximum-69-number](https://leetcode-cn.com/problems/maximum-69-number) 
## 原题
给你一个仅由数字 6 和 9 组成的正整数 `num` 。

你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。

请返回你可以得到的最大数字。

 

 **示例 1：** 

```
输入：num = 9669
输出：9969
解释：
改变第一位数字可以得到 6669 。
改变第二位数字可以得到 9969 。
改变第三位数字可以得到 9699 。
改变第四位数字可以得到 9666 。
其中最大的数字是 9969 。

```
 **示例 2：** 

```
输入：num = 9996
输出：9999
解释：将最后一位从 6 变到 9，其结果 9999 是最大的数。
```
 **示例 3：** 

```
输入：num = 9999
输出：9999
解释：无需改变就已经是最大的数字了。
```
 

 **提示：** 
-  `1 <= num <= 10^4` 
-  `num` 每一位上的数字都是 6 或者 9 。
 
**标签**
`贪心` `数学` 


## 
```python

```
>
# 1324.竖直打印单词
[https://leetcode-cn.com/problems/print-words-vertically](https://leetcode-cn.com/problems/print-words-vertically) 
## 原题
给你一个字符串 `s` 。请你按照单词在 `s` 中的出现顺序将它们全部竖直返回。<br>
单词应该以字符串列表的形式返回，必要时用空格补位，但输出尾部的空格需要删除（不允许尾随空格）。<br>
每个单词只能放在一列上，每一列中也只能有一个单词。

 

 **示例 1：** 

```
输入：s = "HOW ARE YOU"
输出：["HAY","ORO","WEU"]
解释：每个单词都应该竖直打印。 
 "HAY"
 "ORO"
 "WEU"

```
 **示例 2：** 

```
输入：s = "TO BE OR NOT TO BE"
输出：["TBONTB","OEROOE","   T"]
解释：题目允许使用空格补位，但不允许输出末尾出现空格。
"TBONTB"
"OEROOE"
"   T"

```
 **示例 3：** 

```
输入：s = "CONTEST IS COMING"
输出：["CIC","OSO","N M","T I","E N","S G","T"]

```
 

 **提示：** 
-  `1 <= s.length <= 200` 
-  `s` 仅含大写英文字母。
- 题目数据保证两个单词之间只有一个空格。
 
**标签**
`数组` `字符串` `模拟` 


## 
```python

```
>
# 1325.删除给定值的叶子节点
[https://leetcode-cn.com/problems/delete-leaves-with-a-given-value](https://leetcode-cn.com/problems/delete-leaves-with-a-given-value) 
## 原题
给你一棵以 `root` 为根的二叉树和一个整数 `target` ，请你删除所有值为 `target` 的 **叶子节点** 。

注意，一旦删除值为 `target` 的叶子节点，它的父节点就可能变成叶子节点；如果新叶子节点的值恰好也是 `target` ，那么这个节点也应该被删除。

也就是说，你需要重复此过程直到不能继续删除。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/16/sample_1_1684.png" style="height: 120px; width: 550px;">** 

```
输入：root = [1,2,3,2,null,2,4], target = 2
输出：[1,null,3,null,4]
解释：
上面左边的图中，绿色节点为叶子节点，且它们的值与 target 相同（同为 2 ），它们会被删除，得到中间的图。
有一个新的节点变成了叶子节点且它的值与 target 相同，所以将再次进行删除，从而得到最右边的图。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/16/sample_2_1684.png" style="height: 120px; width: 300px;">** 

```
输入：root = [1,3,3,3,2], target = 3
输出：[1,3,null,null,2]

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/16/sample_3_1684.png" style="width: 450px;">** 

```
输入：root = [1,2,null,2,null,2], target = 2
输出：[1]
解释：每一步都删除一个绿色的叶子节点（值为 2）。
```
 **示例 4：** 

```
输入：root = [1,1,1], target = 1
输出：[]

```
 **示例 5：** 

```
输入：root = [1,2,3], target = 1
输出：[1,2,3]

```
 

 **提示：** 
-  `1 <= target <= 1000` 
- 每一棵树最多有 `3000` 个节点。
- 每一个节点值的范围是 `[1, 1000]` 。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `哈希表` `二叉树` 


## 
```python

```
>
# 1326.灌溉花园的最少水龙头数目
[https://leetcode-cn.com/problems/minimum-number-of-taps-to-open-to-water-a-garden](https://leetcode-cn.com/problems/minimum-number-of-taps-to-open-to-water-a-garden) 
## 原题
在 x 轴上有一个一维的花园。花园长度为 `n` ，从点 `0` 开始，到点 `n` 结束。

花园里总共有 `n + 1` 个水龙头，分别位于 `[0, 1, ..., n]` 。

给你一个整数 `n` 和一个长度为 `n + 1` 的整数数组 `ranges` ，其中 `ranges[i]` （下标从 0 开始）表示：如果打开点 `i` 处的水龙头，可以灌溉的区域为 `[i -  ranges[i], i + ranges[i]]` 。

请你返回可以灌溉整个花园的 **最少水龙头数目** 。如果花园始终存在无法灌溉到的地方，请你返回 **-1** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/19/1685_example_1.png" style="width: 530px;">

```
输入：n = 5, ranges = [3,4,1,1,0,0]
输出：1
解释：
点 0 处的水龙头可以灌溉区间 [-3,3]
点 1 处的水龙头可以灌溉区间 [-3,5]
点 2 处的水龙头可以灌溉区间 [1,3]
点 3 处的水龙头可以灌溉区间 [2,4]
点 4 处的水龙头可以灌溉区间 [4,4]
点 5 处的水龙头可以灌溉区间 [5,5]
只需要打开点 1 处的水龙头即可灌溉整个花园 [0,5] 。

```
 **示例 2：** 

```
输入：n = 3, ranges = [0,0,0,0]
输出：-1
解释：即使打开所有水龙头，你也无法灌溉整个花园。

```
 **示例 3：** 

```
输入：n = 7, ranges = [1,2,1,0,2,1,0,1]
输出：3

```
 **示例 4：** 

```
输入：n = 8, ranges = [4,0,0,0,0,0,0,0,4]
输出：2

```
 **示例 5：** 

```
输入：n = 8, ranges = [4,0,0,0,4,0,0,0,4]
输出：1

```
 

 **提示：** 
-  `1 <= n <= 10^4` 
-  `ranges.length == n + 1` 
-  `0 <= ranges[i] <= 100` 
 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 1327.列出指定时间段内所有的下单产品
[https://leetcode-cn.com/problems/list-the-products-ordered-in-a-period](https://leetcode-cn.com/problems/list-the-products-ordered-in-a-period) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1328.破坏回文串
[https://leetcode-cn.com/problems/break-a-palindrome](https://leetcode-cn.com/problems/break-a-palindrome) 
## 原题
给你一个由小写英文字母组成的回文字符串  `palindrome` ，请你将其中  **一个** 字符用任意小写英文字母替换，使得结果字符串的 **字典序最小** ，且  **不是**  回文串。

请你返回结果字符串。如果无法做到，则返回一个 **空串** 。

如果两个字符串长度相同，那么字符串 `a` 字典序比字符串 `b` 小可以这样定义：在 `a` 和 `b` 出现不同的第一个位置上，字符串 `a` 中的字符严格小于 `b` 中的对应字符。例如， `"abcc”` 字典序比 `"abcd"` 小，因为不同的第一个位置是在第四个字符，显然 `'c'` 比 `'d'` 小。
 

 **示例 1：** 

```

输入：palindrome = "abccba"
输出："aaccba"
解释：存在多种方法可以使 "abccba" 不是回文，例如 "zbccba", "aaccba", 和 "abacba" 。
在所有方法中，"aaccba" 的字典序最小。
```
 **示例 2：** 

```

输入：palindrome = "a"
输出：""
解释：不存在替换一个字符使 "a" 变成非回文的方法，所以返回空字符串。
```
 **示例 3：** 

```

输入：palindrome = "aa"
输出："ab"
```
 **示例 4：** 

```

输入：palindrome = "aba"
输出："abb"

```
 

 **提示：** 
-  `1 <= palindrome.length <= 1000` 
-  `palindrome`  只包含小写英文字母。
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 1329.将矩阵按对角线排序
[https://leetcode-cn.com/problems/sort-the-matrix-diagonally](https://leetcode-cn.com/problems/sort-the-matrix-diagonally) 
## 原题
 **矩阵对角线** 是一条从矩阵最上面行或者最左侧列中的某个元素开始的对角线，沿右下方向一直到矩阵末尾的元素。例如，矩阵 `mat` 有 `6` 行 `3` 列，从 `mat[2][0]` 开始的 **矩阵对角线** 将会经过 `mat[2][0]` 、 `mat[3][1]` 和 `mat[4][2]` 。

给你一个  `m * n`  的整数矩阵  `mat`  ，请你将同一条 **矩阵对角线** 上的元素按升序排序后，返回排好序的矩阵。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/25/1482_example_1_2.png" style="height: 198px; width: 500px;" />

```

输入：mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
输出：[[1,1,1,1],[1,2,2,2],[1,2,3,3]]

```
 **示例 2：** 

```

输入：mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
输出：[[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat[i].length` 
-  `1 <= m, n <= 100` 
-  `1 <= mat[i][j] <= 100` 
 
**标签**
`数组` `矩阵` `排序` 


## 
```python

```
>
# 1330.翻转子数组得到最大的数组值
[https://leetcode-cn.com/problems/reverse-subarray-to-maximize-array-value](https://leetcode-cn.com/problems/reverse-subarray-to-maximize-array-value) 
## 原题
给你一个整数数组 `nums` 。「数组值」定义为所有满足 `0 <= i < nums.length-1` 的 `|nums[i]-nums[i+1]|` 的和。

你可以选择给定数组的任意子数组，并将该子数组翻转。但你只能执行这个操作 **一次** 。

请你找到可行的最大 **数组值** 。

 

 **示例 1：** 

```
输入：nums = [2,3,1,5,4]
输出：10
解释：通过翻转子数组 [3,1,5] ，数组变成 [2,5,1,3,4] ，数组值为 10 。

```
 **示例 2：** 

```
输入：nums = [2,4,9,24,2,1,10]
输出：68

```
 

 **提示：** 
-  `1 <= nums.length <= 3*10^4` 
-  `-10^5 <= nums[i] <= 10^5` 
 
**标签**
`贪心` `数组` `数学` 


## 
```python

```
>
# 1331.数组序号转换
[https://leetcode-cn.com/problems/rank-transform-of-an-array](https://leetcode-cn.com/problems/rank-transform-of-an-array) 
## 原题
给你一个整数数组 `arr` ，请你将数组中的每个元素替换为它们排序后的序号。

序号代表了一个元素有多大。序号编号的规则如下：
- 序号从 1 开始编号。
- 一个元素越大，那么序号越大。如果两个元素相等，那么它们的序号相同。
- 每个数字的序号都应该尽可能地小。
 

 **示例 1：** 

```
输入：arr = [40,10,20,30]
输出：[4,1,2,3]
解释：40 是最大的元素。 10 是最小的元素。 20 是第二小的数字。 30 是第三小的数字。
```
 **示例 2：** 

```
输入：arr = [100,100,100]
输出：[1,1,1]
解释：所有元素有相同的序号。

```
 **示例 3：** 

```
输入：arr = [37,12,28,9,100,56,80,5,12]
输出：[5,3,4,2,8,6,7,1,3]

```
 

 **提示：** 
-  `0 <= arr.length <= 10^5` 
-  `-10^9 <= arr[i] <= 10^9` 
 
**标签**
`数组` `哈希表` `排序` 


## 
```python

```
>
# 1332.删除回文子序列
[https://leetcode-cn.com/problems/remove-palindromic-subsequences](https://leetcode-cn.com/problems/remove-palindromic-subsequences) 
## 原题
给你一个字符串 `s` ，它仅由字母 `'a'` 和 `'b'` 组成。每一次删除操作都可以从 `s` 中删除一个回文 **子序列** 。

返回删除给定字符串中所有字符（字符串为空）的最小删除次数。

「子序列」定义：如果一个字符串可以通过删除原字符串某些字符而不改变原字符顺序得到，那么这个字符串就是原字符串的一个子序列。

「回文」定义：如果一个字符串向后和向前读是一致的，那么这个字符串就是一个回文。

 

 **示例 1：** 

```

输入：s = "ababa"
输出：1
解释：字符串本身就是回文序列，只需要删除一次。

```
 **示例 2：** 

```

输入：s = "abb"
输出：2
解释："abb" -> "bb" -> "". 
先删除回文子序列 "a"，然后再删除 "bb"。

```
 **示例 3：** 

```

输入：s = "baabb"
输出：2
解释："baabb" -> "b" -> "". 
先删除回文子序列 "baab"，然后再删除 "b"。

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s` 仅包含字母 `'a'` 和 `'b'` 
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 1333.餐厅过滤器
[https://leetcode-cn.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance](https://leetcode-cn.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance) 
## 原题
给你一个餐馆信息数组 `restaurants` ，其中 `restaurants[i] = [id<sub>i</sub>, rating<sub>i</sub>, veganFriendly<sub>i</sub>, price<sub>i</sub>, distance<sub>i</sub>]` 。你必须使用以下三个过滤器来过滤这些餐馆信息。

其中素食者友好过滤器 `veganFriendly` 的值可以为 `true` 或者 `false` ，如果为 *true* 就意味着你应该只包括 `veganFriendly<sub>i</sub>` 为 true 的餐馆，为 *false* 则意味着可以包括任何餐馆。此外，我们还有最大价格 `maxPrice` 和最大距离 `maxDistance` 两个过滤器，它们分别考虑餐厅的价格因素和距离因素的最大值。

过滤后返回餐馆的 ** *id* ** ，按照 ***rating*** 从高到低排序。如果 ***rating*** 相同，那么按 ***id*** 从高到低排序。简单起见， `veganFriendly<sub>i</sub>` 和 `veganFriendly` 为 *true* 时取值为 *1* ，为 *false* 时，取值为 *0 。* 

 

 **示例 1：** 

```
输入：restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
输出：[3,1,5] 
解释： 
这些餐馆为：
餐馆 1 [id=1, rating=4, veganFriendly=1, price=40, distance=10]
餐馆 2 [id=2, rating=8, veganFriendly=0, price=50, distance=5]
餐馆 3 [id=3, rating=8, veganFriendly=1, price=30, distance=4]
餐馆 4 [id=4, rating=10, veganFriendly=0, price=10, distance=3]
餐馆 5 [id=5, rating=1, veganFriendly=1, price=15, distance=1] 
在按照 veganFriendly = 1, maxPrice = 50 和 maxDistance = 10 进行过滤后，我们得到了餐馆 3, 餐馆 1 和 餐馆 5（按评分从高到低排序）。 

```
 **示例 2：** 

```
输入：restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 50, maxDistance = 10
输出：[4,3,2,1,5]
解释：餐馆与示例 1 相同，但在 veganFriendly = 0 的过滤条件下，应该考虑所有餐馆。

```
 **示例 3：** 

```
输入：restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 0, maxPrice = 30, maxDistance = 3
输出：[4,5]

```
 

 **提示：** 
-  `1 <= restaurants.length <= 10^4` 
-  `restaurants[i].length == 5` 
-  `1 <= id<sub>i</sub>, rating<sub>i</sub>, price<sub>i</sub>, distance<sub>i </sub><= 10^5` 
-  `1 <= maxPrice, maxDistance <= 10^5` 
-  `veganFriendly<sub>i</sub>` 和 `veganFriendly` 的值为 0 或 1 。
- 所有 `id<sub>i</sub>` 各不相同。
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 1334.阈值距离内邻居最少的城市
[https://leetcode-cn.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance](https://leetcode-cn.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance) 
## 原题
有 `n`  个城市，按从 `0` 到 `n-1`  编号。给你一个边数组  `edges` ，其中 `edges[i] = [from<sub>i</sub>, to<sub>i</sub>, weight<sub>i</sub>]`  代表  `from<sub>i</sub>`  和  `to<sub>i</sub>` <sub> </sub>两个城市之间的双向加权边，距离阈值是一个整数  `distanceThreshold` 。

返回能通过某些路径到达其他城市数目最少、且路径距离 **最大** 为  `distanceThreshold`  的城市。如果有多个这样的城市，则返回编号最大的城市。

注意，连接城市 ***i*** 和 ***j*** 的路径的距离等于沿该路径的所有边的权重之和。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/26/find_the_city_01.png" style="height: 225px; width: 300px;" />

```

输入：n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
输出：3
解释：城市分布图如上。
每个城市阈值距离 distanceThreshold = 4 内的邻居城市分别是：
城市 0 -> [城市 1, 城市 2] 
城市 1 -> [城市 0, 城市 2, 城市 3] 
城市 2 -> [城市 0, 城市 1, 城市 3] 
城市 3 -> [城市 1, 城市 2] 
城市 0 和 3 在阈值距离 4 以内都有 2 个邻居城市，但是我们必须返回城市 3，因为它的编号最大。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/26/find_the_city_02.png" style="height: 225px; width: 300px;" />** 

```

输入：n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
输出：0
解释：城市分布图如上。 
每个城市阈值距离 distanceThreshold = 2 内的邻居城市分别是：
城市 0 -> [城市 1] 
城市 1 -> [城市 0, 城市 4] 
城市 2 -> [城市 3, 城市 4] 
城市 3 -> [城市 2, 城市 4]
城市 4 -> [城市 1, 城市 2, 城市 3] 
城市 0 在阈值距离 2 以内只有 1 个邻居城市。

```
 

 **提示：** 
-  `2 <= n <= 100` 
-  `1 <= edges.length <= n * (n - 1) / 2` 
-  `edges[i].length == 3` 
-  `0 <= from<sub>i</sub> < to<sub>i</sub> < n` 
-  `1 <= weight<sub>i</sub>, distanceThreshold <= 10^4` 
- 所有 `(from<sub>i</sub>, to<sub>i</sub>)`  都是不同的。
 
**标签**
`图` `动态规划` `最短路` 


## 
```python

```
>
# 1335.工作计划的最低难度
[https://leetcode-cn.com/problems/minimum-difficulty-of-a-job-schedule](https://leetcode-cn.com/problems/minimum-difficulty-of-a-job-schedule) 
## 原题
你需要制定一份 `d` 天的工作计划表。工作之间存在依赖，要想执行第 `i` 项工作，你必须完成全部 `j` 项工作（ `0 <= j < i` ）。

你每天 **至少** 需要完成一项任务。工作计划的总难度是这 `d` 天每一天的难度之和，而一天的工作难度是当天应该完成工作的最大难度。

给你一个整数数组 `jobDifficulty` 和一个整数 `d` ，分别代表工作难度和需要计划的天数。第 `i` 项工作的难度是 `jobDifficulty[i]` 。

返回整个工作计划的 **最小难度** 。如果无法制定工作计划，则返回 **-1** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/26/untitled.png" style="height: 304px; width: 365px;">

```
输入：jobDifficulty = [6,5,4,3,2,1], d = 2
输出：7
解释：第一天，您可以完成前 5 项工作，总难度 = 6.
第二天，您可以完成最后一项工作，总难度 = 1.
计划表的难度 = 6 + 1 = 7 

```
 **示例 2：** 

```
输入：jobDifficulty = [9,9,9], d = 4
输出：-1
解释：就算你每天完成一项工作，仍然有一天是空闲的，你无法制定一份能够满足既定工作时间的计划表。

```
 **示例 3：** 

```
输入：jobDifficulty = [1,1,1], d = 3
输出：3
解释：工作计划为每天一项工作，总难度为 3 。

```
 **示例 4：** 

```
输入：jobDifficulty = [7,1,7,1,7,1], d = 3
输出：15

```
 **示例 5：** 

```
输入：jobDifficulty = [11,111,22,222,33,333,44,444], d = 6
输出：843

```
 

 **提示：** 
-  `1 <= jobDifficulty.length <= 300` 
-  `0 <= jobDifficulty[i] <= 1000` 
-  `1 <= d <= 10` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1336.每次访问的交易次数
[https://leetcode-cn.com/problems/number-of-transactions-per-visit](https://leetcode-cn.com/problems/number-of-transactions-per-visit) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1337.矩阵中战斗力最弱的 K 行
[https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix](https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix) 
## 原题
给你一个大小为  `m * n`  的矩阵  `mat` ，矩阵由若干军人和平民组成，分别用 1 和 0 表示。

请你返回矩阵中战斗力最弱的  `k`  行的索引，按从最弱到最强排序。

如果第  ***i***  行的军人数量少于第  ***j***  行，或者两行军人数量相同但 ***i*** 小于 ***j*** ，那么我们认为第 ***i*** 行的战斗力比第 ***j*** 行弱。

军人 **总是** 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

 

 **示例 1：** 

```

输入：mat = 
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]], 
k = 3
输出：[2,0,3]
解释：
每行中的军人数目：
行 0 -> 2 
行 1 -> 4 
行 2 -> 1 
行 3 -> 2 
行 4 -> 5 
从最弱到最强对这些行排序后得到 [2,0,3,1,4]

```
 **示例 2：** 

```

输入：mat = 
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]], 
k = 2
输出：[0,2]
解释： 
每行中的军人数目：
行 0 -> 1 
行 1 -> 4 
行 2 -> 1 
行 3 -> 1 
从最弱到最强对这些行排序后得到 [0,2,3,1]

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat[i].length` 
-  `2 <= n, m <= 100` 
-  `1 <= k <= m` 
-  `matrix[i][j]` 不是 0 就是 1
 
**标签**
`数组` `二分查找` `矩阵` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1338.数组大小减半
[https://leetcode-cn.com/problems/reduce-array-size-to-the-half](https://leetcode-cn.com/problems/reduce-array-size-to-the-half) 
## 原题
给你一个整数数组 `arr` 。你可以从中选出一个整数集合，并删除这些整数在数组中的每次出现。

返回 **至少** 能删除数组中的一半整数的整数集合的最小大小。

 

 **示例 1：** 

```
输入：arr = [3,3,3,3,5,5,5,2,2,7]
输出：2
解释：选择 {3,7} 使得结果数组为 [5,5,5,2,2]、长度为 5（原数组长度的一半）。
大小为 2 的可行集合有 {3,5},{3,2},{5,2}。
选择 {2,7} 是不可行的，它的结果数组为 [3,3,3,3,5,5,5]，新数组长度大于原数组的二分之一。

```
 **示例 2：** 

```
输入：arr = [7,7,7,7,7,7]
输出：1
解释：我们只能选择集合 {7}，结果数组为空。

```
 **示例 3：** 

```
输入：arr = [1,9]
输出：1

```
 **示例 4：** 

```
输入：arr = [1000,1000,3,7]
输出：1

```
 **示例 5：** 

```
输入：arr = [1,2,3,4,5,6,7,8,9,10]
输出：5

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `arr.length` 为偶数
-  `1 <= arr[i] <= 10^5` 
 
**标签**
`贪心` `数组` `哈希表` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1339.分裂二叉树的最大乘积
[https://leetcode-cn.com/problems/maximum-product-of-splitted-binary-tree](https://leetcode-cn.com/problems/maximum-product-of-splitted-binary-tree) 
## 原题
给你一棵二叉树，它的根为 `root` 。请你删除 1 条边，使二叉树分裂成两棵子树，且它们子树和的乘积尽可能大。

由于答案可能会很大，请你将结果对 10^9 + 7 取模后再返回。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/02/sample_1_1699.png" style="height: 200px; width: 495px;">** 

```
输入：root = [1,2,3,4,5,6]
输出：110
解释：删除红色的边，得到 2 棵子树，和分别为 11 和 10 。它们的乘积是 110 （11*10）

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/02/sample_2_1699.png" style="height: 200px; width: 495px;">

```
输入：root = [1,null,2,3,4,null,null,5,6]
输出：90
解释：移除红色的边，得到 2 棵子树，和分别是 15 和 6 。它们的乘积为 90 （15*6）

```
 **示例 3：** 

```
输入：root = [2,3,9,10,7,8,6,5,4,11,1]
输出：1025

```
 **示例 4：** 

```
输入：root = [1,1]
输出：1

```
 

 **提示：** 
- 每棵树最多有 `50000` 个节点，且至少有 `2` 个节点。
- 每个节点的值在 `[1, 10000]` 之间。
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1340.跳跃游戏 V
[https://leetcode-cn.com/problems/jump-game-v](https://leetcode-cn.com/problems/jump-game-v) 
## 原题
给你一个整数数组 `arr` 和一个整数 `d` 。每一步你可以从下标 `i` 跳到：
-  `i + x` ，其中 `i + x < arr.length` 且 `0 < x <= d` 。
-  `i - x` ，其中 `i - x >= 0` 且 `0 < x <= d` 。
除此以外，你从下标 `i` 跳到下标 `j` 需要满足： `arr[i] > arr[j]` 且 `arr[i] > arr[k]` ，其中下标 `k` 是所有 `i` 到 `j` 之间的数字（更正式的， `min(i, j) < k < max(i, j)` ）。

你可以选择数组的任意下标开始跳跃。请你返回你 **最多** 可以访问多少个下标。

请注意，任何时刻你都不能跳到数组的外面。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/02/meta-chart.jpeg" style="height: 419px; width: 633px;">

```
输入：arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
输出：4
解释：你可以从下标 10 出发，然后如上图依次经过 10 --> 8 --> 6 --> 7 。
注意，如果你从下标 6 开始，你只能跳到下标 7 处。你不能跳到下标 5 处因为 13 > 9 。你也不能跳到下标 4 处，因为下标 5 在下标 4 和 6 之间且 13 > 9 。
类似的，你不能从下标 3 处跳到下标 2 或者下标 1 处。

```
 **示例 2：** 

```
输入：arr = [3,3,3,3,3], d = 3
输出：1
解释：你可以从任意下标处开始且你永远无法跳到任何其他坐标。

```
 **示例 3：** 

```
输入：arr = [7,6,5,4,3,2,1], d = 1
输出：7
解释：从下标 0 处开始，你可以按照数值从大到小，访问所有的下标。

```
 **示例 4：** 

```
输入：arr = [7,1,7,1,7,1], d = 2
输出：2

```
 **示例 5：** 

```
输入：arr = [66], d = 1
输出：1

```
 

 **提示：** 
-  `1 <= arr.length <= 1000` 
-  `1 <= arr[i] <= 10^5` 
-  `1 <= d <= arr.length` 
 
**标签**
`数组` `动态规划` `排序` 


## 
```python

```
>
# 1341.电影评分
[https://leetcode-cn.com/problems/movie-rating](https://leetcode-cn.com/problems/movie-rating) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1342.将数字变成 0 的操作次数
[https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero](https://leetcode-cn.com/problems/number-of-steps-to-reduce-a-number-to-zero) 
## 原题
给你一个非负整数 `num` ，请你返回将它变成 0 所需要的步数。 如果当前数字是偶数，你需要把它除以 2 ；否则，减去 1 。

 

 **示例 1：** 

```
输入：num = 14
输出：6
解释：
步骤 1) 14 是偶数，除以 2 得到 7 。
步骤 2） 7 是奇数，减 1 得到 6 。
步骤 3） 6 是偶数，除以 2 得到 3 。
步骤 4） 3 是奇数，减 1 得到 2 。
步骤 5） 2 是偶数，除以 2 得到 1 。
步骤 6） 1 是奇数，减 1 得到 0 。

```
 **示例 2：** 

```
输入：num = 8
输出：4
解释：
步骤 1） 8 是偶数，除以 2 得到 4 。
步骤 2） 4 是偶数，除以 2 得到 2 。
步骤 3） 2 是偶数，除以 2 得到 1 。
步骤 4） 1 是奇数，减 1 得到 0 。

```
 **示例 3：** 

```
输入：num = 123
输出：12

```
 

 **提示：** 
-  `0 <= num <= 10^6` 
 
**标签**
`位运算` `数学` 


## 
```python

```
>
# 1343.大小为 K 且平均值大于等于阈值的子数组数目
[https://leetcode-cn.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold](https://leetcode-cn.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold) 
## 原题
给你一个整数数组 `arr` 和两个整数 `k` 和 `threshold` 。

请你返回长度为 `k` 且平均值大于等于 `threshold` 的子数组数目。

 

 **示例 1：** 

```
输入：arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
输出：3
解释：子数组 [2,5,5],[5,5,5] 和 [5,5,8] 的平均值分别为 4，5 和 6 。其他长度为 3 的子数组的平均值都小于 4 （threshold 的值)。

```
 **示例 2：** 

```
输入：arr = [1,1,1,1,1], k = 1, threshold = 0
输出：5

```
 **示例 3：** 

```
输入：arr = [11,13,17,23,29,31,7,5,2,3], k = 3, threshold = 5
输出：6
解释：前 6 个长度为 3 的子数组平均值都大于 5 。注意平均值不是整数。

```
 **示例 4：** 

```
输入：arr = [7,7,7,7,7,7,7], k = 7, threshold = 7
输出：1

```
 **示例 5：** 

```
输入：arr = [4,4,4,4], k = 4, threshold = 1
输出：1

```
 

 **提示：** 
-  `1 <= arr.length <= 10^5` 
-  `1 <= arr[i] <= 10^4` 
-  `1 <= k <= arr.length` 
-  `0 <= threshold <= 10^4` 
 
**标签**
`数组` `滑动窗口` 


## 
```python

```
>
# 1344.时钟指针的夹角
[https://leetcode-cn.com/problems/angle-between-hands-of-a-clock](https://leetcode-cn.com/problems/angle-between-hands-of-a-clock) 
## 原题
给你两个数 `hour` 和 `minutes` 。请你返回在时钟上，由给定时间的时针和分针组成的较小角的角度（60 单位制）。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/08/sample_1_1673.png" style="height: 225px; width: 230px;">

```
输入：hour = 12, minutes = 30
输出：165

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/08/sample_2_1673.png" style="height: 225px; width: 230px;">

```
输入：hour = 3, minutes = 30
输出；75

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/08/sample_3_1673.png" style="height: 231px; width: 230px;">** 

```
输入：hour = 3, minutes = 15
输出：7.5

```
 **示例 4：** 

```
输入：hour = 4, minutes = 50
输出：155

```
 **示例 5：** 

```
输入：hour = 12, minutes = 0
输出：0

```
 

 **提示：** 
-  `1 <= hour <= 12` 
-  `0 <= minutes <= 59` 
- 与标准答案误差在 `10^-5` 以内的结果都被视为正确结果。
 
**标签**
`数学` 


## 
```python

```
>
# 1345.跳跃游戏 IV
[https://leetcode-cn.com/problems/jump-game-iv](https://leetcode-cn.com/problems/jump-game-iv) 
## 原题
给你一个整数数组 `arr` ，你一开始在数组的第一个元素处（下标为 0）。

每一步，你可以从下标 `i` 跳到下标：
-  `i + 1` 满足： `i + 1 < arr.length` 
-  `i - 1` 满足： `i - 1 >= 0` 
-  `j` 满足： `arr[i] == arr[j]` 且 `i != j` 
请你返回到达数组最后一个元素的下标处所需的 **最少操作次数** 。

注意：任何时候你都不能跳到数组外面。

 

 **示例 1：** 

```
输入：arr = [100,-23,-23,404,100,23,23,23,3,404]
输出：3
解释：那你需要跳跃 3 次，下标依次为 0 --> 4 --> 3 --> 9 。下标 9 为数组的最后一个元素的下标。

```
 **示例 2：** 

```
输入：arr = [7]
输出：0
解释：一开始就在最后一个元素处，所以你不需要跳跃。

```
 **示例 3：** 

```
输入：arr = [7,6,9,6,9,6,9,7]
输出：1
解释：你可以直接从下标 0 处跳到下标 7 处，也就是数组的最后一个元素处。

```
 **示例 4：** 

```
输入：arr = [6,1,9]
输出：2

```
 **示例 5：** 

```
输入：arr = [11,22,7,7,7,7,7,7,7,22,13]
输出：3

```
 

 **提示：** 
-  `1 <= arr.length <= 5 * 10^4` 
-  `-10^8 <= arr[i] <= 10^8` 
 
**标签**
`广度优先搜索` `数组` `哈希表` 


## 
```python

```
>
# 1346.检查整数及其两倍数是否存在
[https://leetcode-cn.com/problems/check-if-n-and-its-double-exist](https://leetcode-cn.com/problems/check-if-n-and-its-double-exist) 
## 原题
给你一个整数数组 `arr` ，请你检查是否存在两个整数 `N` 和 `M` ，满足 `N` 是 `M` 的两倍（即， `N = 2 * M` ）。

更正式地，检查是否存在两个下标 `i` 和 `j` 满足：
-  `i != j` 
-  `0 <= i, j < arr.length` 
-  `arr[i] == 2 * arr[j]` 
 

 **示例 1：** 

```
输入：arr = [10,2,5,3]
输出：true
解释：N = 10 是 M = 5 的两倍，即 10 = 2 * 5 。

```
 **示例 2：** 

```
输入：arr = [7,1,14,11]
输出：true
解释：N = 14 是 M = 7 的两倍，即 14 = 2 * 7 。

```
 **示例 3：** 

```
输入：arr = [3,1,7,11]
输出：false
解释：在该情况下不存在 N 和 M 满足 N = 2 * M 。

```
 

 **提示：** 
-  `2 <= arr.length <= 500` 
-  `-10^3 <= arr[i] <= 10^3` 
 
**标签**
`数组` `哈希表` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 1347.制造字母异位词的最小步骤数
[https://leetcode-cn.com/problems/minimum-number-of-steps-to-make-two-strings-anagram](https://leetcode-cn.com/problems/minimum-number-of-steps-to-make-two-strings-anagram) 
## 原题
给你两个长度相等的字符串 `s` 和 `t` 。每一个步骤中，你可以选择将 `t` 中的 **任一字符** 替换为 **另一个字符** 。

返回使 `t` 成为 `s` 的字母异位词的最小步骤数。

 **字母异位词** 指字母相同，但排列不同（也可能相同）的字符串。

 

 **示例 1：** 

```
输出：s = "bab", t = "aba"
输出：1
提示：用 ';b'; 替换 t 中的第一个 ';a';，t = "bba" 是 s 的一个字母异位词。

```
 **示例 2：** 

```
输出：s = "leetcode", t = "practice"
输出：5
提示：用合适的字符替换 t 中的 ';p';, ';r';, ';a';, ';i'; 和 ';c';，使 t 变成 s 的字母异位词。

```
 **示例 3：** 

```
输出：s = "anagram", t = "mangaar"
输出：0
提示："anagram" 和 "mangaar" 本身就是一组字母异位词。 

```
 **示例 4：** 

```
输出：s = "xxyyzz", t = "xxyyzz"
输出：0

```
 **示例 5：** 

```
输出：s = "friend", t = "family"
输出：4

```
 

 **提示：** 
-  `1 <= s.length <= 50000` 
-  `s.length == t.length` 
-  `s` 和 `t` 只包含小写英文字母
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1348.推文计数
[https://leetcode-cn.com/problems/tweet-counts-per-frequency](https://leetcode-cn.com/problems/tweet-counts-per-frequency) 
## 原题
请你实现一个能够支持以下两种方法的推文计数类 `TweetCounts` ：

1. `recordTweet(string tweetName, int time)` 
- 记录推文发布情况：用户 `tweetName` 在 `time` （以 **秒** 为单位）时刻发布了一条推文。
2. `getTweetCountsPerFrequency(string freq, string tweetName, int startTime, int endTime)` 
- 返回从开始时间 `startTime` （以 **秒** 为单位）到结束时间 `endTime` （以 **秒** 为单位）内，每 **分** ***minute** ，* **时 *hour* ** 或者 **日 *day* ** （取决于 `freq` ）内指定用户 `tweetName` 发布的推文总数。
-  `freq` 的值始终为 **分** ***minute** ，* **时** ***hour*** 或者 **日** ***day*** 之一，表示获取指定用户 `tweetName` 发布推文次数的时间间隔。
- 第一个时间间隔始终从 `startTime` 开始，因此时间间隔为 `[startTime, startTime + delta*1>,  [startTime + delta*1, startTime + delta*2>, [startTime + delta*2, startTime + delta*3>, ... , [startTime + delta*i, **min** (startTime + delta*(i+1), endTime + 1)>` ，其中 `i` 和 `delta` （取决于 `freq` ）都是非负整数。
 

 **示例：** 

```
输入：
["TweetCounts","recordTweet","recordTweet","recordTweet","getTweetCountsPerFrequency","getTweetCountsPerFrequency","recordTweet","getTweetCountsPerFrequency"]
[[],["tweet3",0],["tweet3",60],["tweet3",10],["minute","tweet3",0,59],["minute","tweet3",0,60],["tweet3",120],["hour","tweet3",0,210]]

输出：
[null,null,null,null,[2],[2,1],null,[4]]

解释：
TweetCounts tweetCounts = new TweetCounts();
tweetCounts.recordTweet("tweet3", 0);
tweetCounts.recordTweet("tweet3", 60);
tweetCounts.recordTweet("tweet3", 10);                             // "tweet3" 发布推文的时间分别是 0, 10 和 60 。
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 59); // 返回 [2]。统计频率是每分钟（60 秒），因此只有一个有效时间间隔 [0,60> - > 2 条推文。
tweetCounts.getTweetCountsPerFrequency("minute", "tweet3", 0, 60); // 返回 [2,1]。统计频率是每分钟（60 秒），因此有两个有效时间间隔 1) [0,60> - > 2 条推文，和 2) [60,61> - > 1 条推文。 
tweetCounts.recordTweet("tweet3", 120);                            // "tweet3" 发布推文的时间分别是 0, 10, 60 和 120 。
tweetCounts.getTweetCountsPerFrequency("hour", "tweet3", 0, 210);  // 返回 [4]。统计频率是每小时（3600 秒），因此只有一个有效时间间隔 [0,211> - > 4 条推文。

```
 

 **提示：** 
- 同时考虑 `recordTweet` 和 `getTweetCountsPerFrequency` ，最多有 `10000` 次操作。
-  `0 <= time, startTime, endTime <= 10^9` 
-  `0 <= endTime - startTime <= 10^4` 
 
**标签**
`设计` `哈希表` `二分查找` `有序集合` `排序` 


## 
```python

```
>
# 1349.参加考试的最大学生数
[https://leetcode-cn.com/problems/maximum-students-taking-exam](https://leetcode-cn.com/problems/maximum-students-taking-exam) 
## 原题
给你一个 `m * n` 的矩阵 `seats` 表示教室中的座位分布。如果座位是坏的（不可用），就用 `';#';` 表示；否则，用 `';.';` 表示。

学生可以看到左侧、右侧、左上、右上这四个方向上紧邻他的学生的答卷，但是看不到直接坐在他前面或者后面的学生的答卷。请你计算并返回该考场可以容纳的一起参加考试且无法作弊的最大学生人数。

学生必须坐在状况良好的座位上。

 

 **示例 1：** 

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/09/image.png" style="height: 197px; width: 339px;">

```
输入：seats = [["#",".","#","#",".","#"],
              [".","#","#","#","#","."],
              ["#",".","#","#",".","#"]]
输出：4
解释：教师可以让 4 个学生坐在可用的座位上，这样他们就无法在考试中作弊。 

```
 **示例 2：** 

```
输入：seats = [[".","#"],
              ["#","#"],
              ["#","."],
              ["#","#"],
              [".","#"]]
输出：3
解释：让所有学生坐在可用的座位上。

```
 **示例 3：** 

```
输入：seats = [["#",".",".",".","#"],
              [".","#",".","#","."],
              [".",".","#",".","."],
              [".","#",".","#","."],
              ["#",".",".",".","#"]]
输出：10
解释：让学生坐在第 1、3 和 5 列的可用座位上。

```
 

 **提示：** 
-  `seats` 只包含字符 `';.'; 和` `';#';` 
-  `m == seats.length` 
-  `n == seats[i].length` 
-  `1 <= m <= 8` 
-  `1 <= n <= 8` 
 
**标签**
`位运算` `数组` `动态规划` `状态压缩` `矩阵` 


## 
```python

```
>
# 1350.院系无效的学生
[https://leetcode-cn.com/problems/students-with-invalid-departments](https://leetcode-cn.com/problems/students-with-invalid-departments) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1351.统计有序矩阵中的负数
[https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix](https://leetcode-cn.com/problems/count-negative-numbers-in-a-sorted-matrix) 
## 原题
给你一个  `m * n`  的矩阵  `grid` ，矩阵中的元素无论是按行还是按列，都以非递增顺序排列。 

请你统计并返回  `grid`  中 **负数** 的数目。

 

 **示例 1：** 

```

输入：grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
输出：8
解释：矩阵中共有 8 个负数。

```
 **示例 2：** 

```

输入：grid = [[3,2],[1,0]]
输出：0

```
 **示例 3：** 

```

输入：grid = [[1,-1],[-1,-1]]
输出：3

```
 **示例 4：** 

```

输入：grid = [[-1]]
输出：1

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 100` 
-  `-100 <= grid[i][j] <= 100` 
 

 **进阶：** 你可以设计一个时间复杂度为 `O(n + m)` 的解决方案吗？

 

 
**标签**
`数组` `二分查找` `矩阵` 


## 
```python

```
>
# 1352.最后 K 个数的乘积
[https://leetcode-cn.com/problems/product-of-the-last-k-numbers](https://leetcode-cn.com/problems/product-of-the-last-k-numbers) 
## 原题
请你实现一个「数字乘积类」 `ProductOfNumbers` ，要求支持下述两种方法：

1. `add(int num)` 
- 将数字 `num` 添加到当前数字列表的最后面。
2. `getProduct(int k)` 
- 返回当前数字列表中，最后 `k` 个数字的乘积。
- 你可以假设当前列表中始终 **至少** 包含 `k` 个数字。
题目数据保证：任何时候，任一连续数字序列的乘积都在 32-bit 整数范围内，不会溢出。

 

 **示例：** 

```
输入：
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

输出：
[null,null,null,null,null,null,20,40,0,null,32]

解释：
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // 返回 20 。最后 2 个数字的乘积是 5 * 4 = 20
productOfNumbers.getProduct(3); // 返回 40 。最后 3 个数字的乘积是 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // 返回  0 。最后 4 个数字的乘积是 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3,0,2,5,4,8]
productOfNumbers.getProduct(2); // 返回 32 。最后 2 个数字的乘积是 4 * 8 = 32 

```
 

 **提示：** 
-  `add` 和 `getProduct` 两种操作加起来总共不会超过 `40000` 次。
-  `0 <= num <= 100` 
-  `1 <= k <= 40000` 
 
**标签**
`设计` `队列` `数组` `数学` `数据流` 


## 
```python

```
>
# 1353.最多可以参加的会议数目
[https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended](https://leetcode-cn.com/problems/maximum-number-of-events-that-can-be-attended) 
## 原题
给你一个数组 `events` ，其中 `events[i] = [startDay<sub>i</sub>, endDay<sub>i</sub>]` ，表示会议 `i` 开始于 `startDay<sub>i</sub>` ，结束于 `endDay<sub>i</sub>` 。

你可以在满足 `startDay<sub>i</sub> <= d <= endDay<sub>i</sub>` <sub> </sub>中的任意一天 `d` 参加会议 `i` 。注意，一天只能参加一个会议。

请你返回你可以参加的 **最大** 会议数目。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/16/e1.png" style="height: 267px; width: 400px;" />

```

输入：events = [[1,2],[2,3],[3,4]]
输出：3
解释：你可以参加所有的三个会议。
安排会议的一种方案如上图。
第 1 天参加第一个会议。
第 2 天参加第二个会议。
第 3 天参加第三个会议。

```
 **示例 2：** 

```

输入：events= [[1,2],[2,3],[3,4],[1,2]]
输出：4

```
 

 **提示：** ​​​​​​
-  `1 <= events.length <= 10^5` 
-  `events[i].length == 2` 
-  `1 <= startDay<sub>i</sub> <= endDay<sub>i</sub> <= 10^5` 
 
**标签**
`贪心` `数组` `堆（优先队列）` 


## 
```python

```
>
# 1354.多次求和构造目标数组
[https://leetcode-cn.com/problems/construct-target-array-with-multiple-sums](https://leetcode-cn.com/problems/construct-target-array-with-multiple-sums) 
## 原题
给你一个整数数组 `target` 。一开始，你有一个数组 `A` ，它的所有元素均为 1 ，你可以执行以下操作：
- 令 `x` 为你数组里所有元素的和
- 选择满足 `0 <= i < target.size` 的任意下标 `i` ，并让 `A` 数组里下标为 `i` 处的值为 `x` 。
- 你可以重复该过程任意次
如果能从 `A` 开始构造出目标数组 `target` ，请你返回 True ，否则返回 False 。

 

 **示例 1：** 

```
输入：target = [9,3,5]
输出：true
解释：从 [1, 1, 1] 开始
[1, 1, 1], 和为 3 ，选择下标 1
[1, 3, 1], 和为 5， 选择下标 2
[1, 3, 5], 和为 9， 选择下标 0
[9, 3, 5] 完成

```
 **示例 2：** 

```
输入：target = [1,1,1,2]
输出：false
解释：不可能从 [1,1,1,1] 出发构造目标数组。

```
 **示例 3：** 

```
输入：target = [8,5]
输出：true

```
 

 **提示：** 
-  `N == target.length` 
-  `1 <= target.length <= 5 * 10^4` 
-  `1 <= target[i] <= 10^9` 
 
**标签**
`数组` `堆（优先队列）` 


## 
```python

```
>
# 1355.活动参与者
[https://leetcode-cn.com/problems/activity-participants](https://leetcode-cn.com/problems/activity-participants) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1356.根据数字二进制下 1 的数目排序
[https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits](https://leetcode-cn.com/problems/sort-integers-by-the-number-of-1-bits) 
## 原题
给你一个整数数组 `arr` 。请你将数组中的元素按照其二进制表示中数字 **1** 的数目升序排序。

如果存在多个数字二进制中 **1** 的数目相同，则必须将它们按照数值大小升序排列。

请你返回排序后的数组。

 

 **示例 1：** 

```
输入：arr = [0,1,2,3,4,5,6,7,8]
输出：[0,1,2,4,8,3,5,6,7]
解释：[0] 是唯一一个有 0 个 1 的数。
[1,2,4,8] 都有 1 个 1 。
[3,5,6] 有 2 个 1 。
[7] 有 3 个 1 。
按照 1 的个数排序得到的结果数组为 [0,1,2,4,8,3,5,6,7]

```
 **示例 2：** 

```
输入：arr = [1024,512,256,128,64,32,16,8,4,2,1]
输出：[1,2,4,8,16,32,64,128,256,512,1024]
解释：数组中所有整数二进制下都只有 1 个 1 ，所以你需要按照数值大小将它们排序。

```
 **示例 3：** 

```
输入：arr = [10000,10000]
输出：[10000,10000]

```
 **示例 4：** 

```
输入：arr = [2,3,5,7,11,13,17,19]
输出：[2,3,5,17,7,11,13,19]

```
 **示例 5：** 

```
输入：arr = [10,100,1000,10000]
输出：[10,100,10000,1000]

```
 

 **提示：** 
-  `1 <= arr.length <= 500` 
-  `0 <= arr[i] <= 10^4` 
 
**标签**
`位运算` `数组` `计数` `排序` 


## 
```python

```
>
# 1357.每隔 n 个顾客打折
[https://leetcode-cn.com/problems/apply-discount-every-n-orders](https://leetcode-cn.com/problems/apply-discount-every-n-orders) 
## 原题
超市里正在举行打折活动，每隔 `n` 个顾客会得到 `discount` 的折扣。

超市里有一些商品，第 `i` 种商品为 `products[i]` 且每件单品的价格为 `prices[i]` 。

结账系统会统计顾客的数目，每隔 `n` 个顾客结账时，该顾客的账单都会打折，折扣为 `discount` （也就是如果原本账单为 `x` ，那么实际金额会变成 `x - (discount * x) / 100` ），然后系统会重新开始计数。

顾客会购买一些商品， `product[i]` 是顾客购买的第 `i` 种商品， `amount[i]` 是对应的购买该种商品的数目。

请你实现 `Cashier` 类：
-  `Cashier(int n, int discount, int[] products, int[] prices)` 初始化实例对象，参数分别为打折频率 `n` ，折扣大小 `discount` ，超市里的商品列表 `products` 和它们的价格 `prices` 。
-  `double getBill(int[] product, int[] amount)` 返回账单的实际金额（如果有打折，请返回打折后的结果）。返回结果与标准答案误差在 `10^-5` 以内都视为正确结果。
 

 **示例 1：** 

```
输入
["Cashier","getBill","getBill","getBill","getBill","getBill","getBill","getBill"]
[[3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]],[[1,2],[1,2]],[[3,7],[10,10]],[[1,2,3,4,5,6,7],[1,1,1,1,1,1,1]],[[4],[10]],[[7,3],[10,10]],[[7,5,3,1,6,4,2],[10,10,10,9,9,9,7]],[[2,3,5],[5,3,2]]]
输出
[null,500.0,4000.0,800.0,4000.0,4000.0,7350.0,2500.0]
解释
Cashier cashier = new Cashier(3,50,[1,2,3,4,5,6,7],[100,200,300,400,300,200,100]);
cashier.getBill([1,2],[1,2]);                        // 返回 500.0, 账单金额为 = 1 * 100 + 2 * 200 = 500.
cashier.getBill([3,7],[10,10]);                      // 返回 4000.0
cashier.getBill([1,2,3,4,5,6,7],[1,1,1,1,1,1,1]);    // 返回 800.0 ，账单原本为 1600.0 ，但由于该顾客是第三位顾客，他将得到 50% 的折扣，所以实际金额为 1600 - 1600 * (50 / 100) = 800 。
cashier.getBill([4],[10]);                           // 返回 4000.0
cashier.getBill([7,3],[10,10]);                      // 返回 4000.0
cashier.getBill([7,5,3,1,6,4,2],[10,10,10,9,9,9,7]); // 返回 7350.0 ，账单原本为 14700.0 ，但由于系统计数再次达到三，该顾客将得到 50% 的折扣，实际金额为 7350.0 。
cashier.getBill([2,3,5],[5,3,2]);                    // 返回 2500.0

```
 

 **提示：** 
-  `1 <= n <= 10^4` 
-  `0 <= discount <= 100` 
-  `1 <= products.length <= 200` 
-  `1 <= products[i] <= 200` 
-  `products` 列表中 **不会** 有重复的元素。
-  `prices.length == products.length` 
-  `1 <= prices[i] <= 1000` 
-  `1 <= product.length <= products.length` 
-  `product[i]` 在 `products` 出现过。
-  `amount.length == product.length` 
-  `1 <= amount[i] <= 1000` 
- 最多有 `1000` 次对 `getBill` 函数的调用。
- 返回结果与标准答案误差在 `10^-5` 以内都视为正确结果。
 
**标签**
`设计` `数组` `哈希表` 


## 
```python

```
>
# 1358.包含所有三种字符的子字符串数目
[https://leetcode-cn.com/problems/number-of-substrings-containing-all-three-characters](https://leetcode-cn.com/problems/number-of-substrings-containing-all-three-characters) 
## 原题
给你一个字符串 `s` ，它只包含三种字符 a, b 和 c 。

请你返回 a，b 和 c 都 **至少** 出现过一次的子字符串数目。

 

 **示例 1：** 

```
输入：s = "abcabc"
输出：10
解释：包含 a，b 和 c 各至少一次的子字符串为 "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" 和 "abc" (相同字符串算多次)。

```
 **示例 2：** 

```
输入：s = "aaacb"
输出：3
解释：包含 a，b 和 c 各至少一次的子字符串为 "aaacb", "aacb" 和 "acb" 。

```
 **示例 3：** 

```
输入：s = "abc"
输出：1

```
 

 **提示：** 
-  `3 <= s.length <= 5 x 10^4` 
-  `s` 只包含字符 a，b 和 c 。
 
**标签**
`哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
# 1359.有效的快递序列数目
[https://leetcode-cn.com/problems/count-all-valid-pickup-and-delivery-options](https://leetcode-cn.com/problems/count-all-valid-pickup-and-delivery-options) 
## 原题
给你 `n` 笔订单，每笔订单都需要快递服务。

请你统计所有有效的 收件/配送 序列的数目，确保第 `i` 个物品的配送服务 `delivery(i)` 总是在其收件服务 `pickup(i)` 之后。

由于答案可能很大，请返回答案对 `10^9 + 7` 取余的结果。

 

 **示例 1：** 

```
输入：n = 1
输出：1
解释：只有一种序列 (P1, D1)，物品 1 的配送服务（D1）在物品 1 的收件服务（P1）后。

```
 **示例 2：** 

```
输入：n = 2
输出：6
解释：所有可能的序列包括：
(P1,P2,D1,D2)，(P1,P2,D2,D1)，(P1,D1,P2,D2)，(P2,P1,D1,D2)，(P2,P1,D2,D1) 和 (P2,D2,P1,D1)。
(P1,D2,P2,D1) 是一个无效的序列，因为物品 2 的收件服务（P2）不应在物品 2 的配送服务（D2）之后。

```
 **示例 3：** 

```
输入：n = 3
输出：90

```
 

 **提示：** 
-  `1 <= n <= 500` 
 
**标签**
`数学` `动态规划` `组合数学` 


## 
```python

```
>
# 1360.日期之间隔几天
[https://leetcode-cn.com/problems/number-of-days-between-two-dates](https://leetcode-cn.com/problems/number-of-days-between-two-dates) 
## 原题
请你编写一个程序来计算两个日期之间隔了多少天。

日期以字符串形式给出，格式为 `YYYY-MM-DD` ，如示例所示。

 

 **示例 1：** 

```
输入：date1 = "2019-06-29", date2 = "2019-06-30"
输出：1

```
 **示例 2：** 

```
输入：date1 = "2020-01-15", date2 = "2019-12-31"
输出：15

```
 

 **提示：** 
- 给定的日期是 `1971` 年到 `2100` 年之间的有效日期。
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 1361.验证二叉树
[https://leetcode-cn.com/problems/validate-binary-tree-nodes](https://leetcode-cn.com/problems/validate-binary-tree-nodes) 
## 原题
二叉树上有 `n` 个节点，按从 `0` 到 `n - 1` 编号，其中节点 `i` 的两个子节点分别是 `leftChild[i]` 和 `rightChild[i]` 。

只有 **所有** 节点能够形成且 **只** 形成 **一颗** 有效的二叉树时，返回 `true` ；否则返回 `false` 。

如果节点 `i` 没有左子节点，那么 `leftChild[i]` 就等于 `-1` 。右子节点也符合该规则。

注意：节点没有值，本问题中仅仅使用节点编号。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/23/1503_ex1.png" style="height: 287px; width: 195px;">** 

```
输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
输出：true

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/23/1503_ex2.png" style="height: 272px; width: 183px;">** 

```
输入：n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
输出：false

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/23/1503_ex3.png" style="height: 174px; width: 82px;">** 

```
输入：n = 2, leftChild = [1,0], rightChild = [-1,-1]
输出：false

```
 **示例 4：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/23/1503_ex4.png" style="height: 191px; width: 470px;">** 

```
输入：n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1]
输出：false

```
 

 **提示：** 
-  `1 <= n <= 10^4` 
-  `leftChild.length == rightChild.length == n` 
-  `-1 <= leftChild[i], rightChild[i] <= n - 1` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `并查集` `图` `二叉树` 


## 
```python

```
>
# 1362.最接近的因数
[https://leetcode-cn.com/problems/closest-divisors](https://leetcode-cn.com/problems/closest-divisors) 
## 原题
给你一个整数 `num` ，请你找出同时满足下面全部要求的两个整数：
- 两数乘积等于 `num + 1` 或 `num + 2` 
- 以绝对差进行度量，两数大小最接近
你可以按任意顺序返回这两个整数。

 

 **示例 1：** 

```
输入：num = 8
输出：[3,3]
解释：对于 num + 1 = 9，最接近的两个因数是 3 &amp; 3；对于 num + 2 = 10, 最接近的两个因数是 2 &amp; 5，因此返回 3 &amp; 3 。

```
 **示例 2：** 

```
输入：num = 123
输出：[5,25]

```
 **示例 3：** 

```
输入：num = 999
输出：[40,25]

```
 

 **提示：** 
-  `1 <= num <= 10^9` 
 
**标签**
`数学` 


## 
```python

```
>
# 1363.形成三的最大倍数
[https://leetcode-cn.com/problems/largest-multiple-of-three](https://leetcode-cn.com/problems/largest-multiple-of-three) 
## 原题
给你一个整数数组 `digits` ，你可以通过按任意顺序连接其中某些数字来形成 **3** 的倍数，请你返回所能得到的最大的 3 的倍数。

由于答案可能不在整数数据类型范围内，请以字符串形式返回答案。

如果无法得到答案，请返回一个空字符串。

 

 **示例 1：** 

```
输入：digits = [8,1,9]
输出："981"

```
 **示例 2：** 

```
输入：digits = [8,6,7,1,0]
输出："8760"

```
 **示例 3：** 

```
输入：digits = [1]
输出：""

```
 **示例 4：** 

```
输入：digits = [0,0,0,0,0,0]
输出："0"

```
 

 **提示：** 
-  `1 <= digits.length <= 10^4` 
-  `0 <= digits[i] <= 9` 
- 返回的结果不应包含不必要的前导零。
 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 1364.顾客的可信联系人数量
[https://leetcode-cn.com/problems/number-of-trusted-contacts-of-a-customer](https://leetcode-cn.com/problems/number-of-trusted-contacts-of-a-customer) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1365.有多少小于当前数字的数字
[https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number](https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number) 
## 原题
给你一个数组 `nums` ，对于其中每个元素 `nums[i]` ，请你统计数组中比它小的所有数字的数目。

换而言之，对于每个 `nums[i]` 你必须计算出有效的 `j` 的数量，其中 `j` 满足 `j != i` **且** `nums[j] < nums[i]` 。

以数组形式返回答案。

 

 **示例 1：** 

```
输入：nums = [8,1,2,2,3]
输出：[4,0,1,1,3]
解释： 
对于 nums[0]=8 存在四个比它小的数字：（1，2，2 和 3）。 
对于 nums[1]=1 不存在比它小的数字。
对于 nums[2]=2 存在一个比它小的数字：（1）。 
对于 nums[3]=2 存在一个比它小的数字：（1）。 
对于 nums[4]=3 存在三个比它小的数字：（1，2 和 2）。

```
 **示例 2：** 

```
输入：nums = [6,5,4,8]
输出：[2,1,0,3]

```
 **示例 3：** 

```
输入：nums = [7,7,7,7]
输出：[0,0,0,0]

```
 

 **提示：** 
-  `2 <= nums.length <= 500` 
-  `0 <= nums[i] <= 100` 
 
**标签**
`数组` `哈希表` `计数` `排序` 


## 
```python

```
>
# 1366.通过投票对团队排名
[https://leetcode-cn.com/problems/rank-teams-by-votes](https://leetcode-cn.com/problems/rank-teams-by-votes) 
## 原题
现在有一个特殊的排名系统，依据参赛团队在投票人心中的次序进行排名，每个投票者都需要按从高到低的顺序对参与排名的所有团队进行排位。

排名规则如下：
- 参赛团队的排名次序依照其所获「排位第一」的票的多少决定。如果存在多个团队并列的情况，将继续考虑其「排位第二」的票的数量。以此类推，直到不再存在并列的情况。
- 如果在考虑完所有投票情况后仍然出现并列现象，则根据团队字母的字母顺序进行排名。
给你一个字符串数组 `votes` 代表全体投票者给出的排位情况，请你根据上述排名规则对所有参赛团队进行排名。

请你返回能表示按排名系统 **排序后** 的所有团队排名的字符串。

 

 **示例 1：** 

```
输入：votes = ["ABC","ACB","ABC","ACB","ACB"]
输出："ACB"
解释：A 队获得五票「排位第一」，没有其他队获得「排位第一」，所以 A 队排名第一。
B 队获得两票「排位第二」，三票「排位第三」。
C 队获得三票「排位第二」，两票「排位第三」。
由于 C 队「排位第二」的票数较多，所以 C 队排第二，B 队排第三。

```
 **示例 2：** 

```
输入：votes = ["WXYZ","XYZW"]
输出："XWYZ"
解释：X 队在并列僵局打破后成为排名第一的团队。X 队和 W 队的「排位第一」票数一样，但是 X 队有一票「排位第二」，而 W 没有获得「排位第二」。 

```
 **示例 3：** 

```
输入：votes = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
输出："ZMNAGUEDSJYLBOPHRQICWFXTVK"
解释：只有一个投票者，所以排名完全按照他的意愿。

```
 **示例 4：** 

```
输入：votes = ["BCA","CAB","CBA","ABC","ACB","BAC"]
输出："ABC"
解释： 
A 队获得两票「排位第一」，两票「排位第二」，两票「排位第三」。
B 队获得两票「排位第一」，两票「排位第二」，两票「排位第三」。
C 队获得两票「排位第一」，两票「排位第二」，两票「排位第三」。
完全并列，所以我们需要按照字母升序排名。

```
 **示例 5：** 

```
输入：votes = ["M","M","M","M"]
输出："M"
解释：只有 M 队参赛，所以它排名第一。

```
 

 **提示：** 
-  `1 <= votes.length <= 1000` 
-  `1 <= votes[i].length <= 26` 
-  `votes[i].length == votes[j].length` for `0 <= i, j < votes.length` 
-  `votes[i][j]` 是英文 **大写** 字母
-  `votes[i]` 中的所有字母都是唯一的
-  `votes[0]` 中出现的所有字母 **同样也** 出现在 `votes[j]` 中，其中 `1 <= j < votes.length` 
 
**标签**
`数组` `哈希表` `字符串` `计数` `排序` 


## 
```python

```
>
# 1367.二叉树中的列表
[https://leetcode-cn.com/problems/linked-list-in-binary-tree](https://leetcode-cn.com/problems/linked-list-in-binary-tree) 
## 原题
给你一棵以 `root` 为根的二叉树和一个 `head` 为第一个节点的链表。

如果在二叉树中，存在一条一直向下的路径，且每个点的数值恰好一一对应以 `head` 为首的链表中每个节点的值，那么请你返回 `True` ，否则返回 `False` 。

一直向下的路径的意思是：从树中某个节点开始，一直连续向下的路径。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/29/sample_1_1720.png" style="height: 280px; width: 220px;">** 

```
输入：head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true
解释：树中蓝色的节点构成了与链表对应的子路径。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/29/sample_2_1720.png" style="height: 280px; width: 220px;">** 

```
输入：head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：true

```
 **示例 3：** 

```
输入：head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
输出：false
解释：二叉树中不存在一一对应链表的路径。

```
 

 **提示：** 
- 二叉树和链表中的每个节点的值都满足 `1 <= node.val <= 100` 。
- 链表包含的节点数目在 `1` 到 `100` 之间。
- 二叉树包含的节点数目在 `1` 到 `2500` 之间。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `链表` `二叉树` 


## 
```python

```
>
# 1368.使网格图至少有一条有效路径的最小代价
[https://leetcode-cn.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid](https://leetcode-cn.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid) 
## 原题
给你一个 m x n 的网格图 `grid` 。 `grid` 中每个格子都有一个数字，对应着从该格子出发下一步走的方向。 `grid[i][j]` 中的数字可能为以下几种情况：
-  **1** ，下一步往右走，也就是你会从 `grid[i][j]` 走到 `grid[i][j + 1]` 
-  **2** ，下一步往左走，也就是你会从 `grid[i][j]` 走到 `grid[i][j - 1]` 
-  **3** ，下一步往下走，也就是你会从 `grid[i][j]` 走到 `grid[i + 1][j]` 
-  **4** ，下一步往上走，也就是你会从 `grid[i][j]` 走到 `grid[i - 1][j]` 
注意网格图中可能会有 **无效数字** ，因为它们可能指向 `grid` 以外的区域。

一开始，你会从最左上角的格子 `(0,0)` 出发。我们定义一条 **有效路径** 为从格子 `(0,0)` 出发，每一步都顺着数字对应方向走，最终在最右下角的格子 `(m - 1, n - 1)` 结束的路径。有效路径 **不需要是最短路径** 。

你可以花费 `cost = 1` 的代价修改一个格子中的数字，但每个格子中的数字 **只能修改一次** 。

请你返回让网格图至少有一条有效路径的最小代价。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/29/grid1.png" style="height: 528px; width: 542px;">

```
输入：grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
输出：3
解释：你将从点 (0, 0) 出发。
到达 (3, 3) 的路径为： (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) 花费代价 cost = 1 使方向向下 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0) 花费代价 cost = 1 使方向向下 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3) 花费代价 cost = 1 使方向向下 --> (3, 3)
总花费为 cost = 3.

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/29/grid2.png" style="height: 408px; width: 419px;">

```
输入：grid = [[1,1,3],[3,2,2],[1,1,4]]
输出：0
解释：不修改任何数字你就可以从 (0, 0) 到达 (2, 2) 。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/02/29/grid3.png" style="height: 302px; width: 314px;">

```
输入：grid = [[1,2],[4,3]]
输出：1

```
 **示例 4：** 

```
输入：grid = [[2,2,2],[2,2,2]]
输出：3

```
 **示例 5：** 

```
输入：grid = [[4]]
输出：0

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 100` 
 
**标签**
`广度优先搜索` `图` `数组` `矩阵` `最短路` `堆（优先队列）` 


## 
```python

```
>
# 1369.获取最近第二次的活动
[https://leetcode-cn.com/problems/get-the-second-most-recent-activity](https://leetcode-cn.com/problems/get-the-second-most-recent-activity) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1370.上升下降字符串
[https://leetcode-cn.com/problems/increasing-decreasing-string](https://leetcode-cn.com/problems/increasing-decreasing-string) 
## 原题
给你一个字符串 `s` ，请你根据下面的算法重新构造字符串：
- 从 `s` 中选出 **最小** 的字符，将它 **接在** 结果字符串的后面。
- 从 `s` 剩余字符中选出 **最小** 的字符，且该字符比上一个添加的字符大，将它 **接在** 结果字符串后面。
- 重复步骤 2 ，直到你没法从 `s` 中选择字符。
- 从 `s` 中选出 **最大** 的字符，将它 **接在** 结果字符串的后面。
- 从 `s` 剩余字符中选出 **最大** 的字符，且该字符比上一个添加的字符小，将它 **接在** 结果字符串后面。
- 重复步骤 5 ，直到你没法从 `s` 中选择字符。
- 重复步骤 1 到 6 ，直到 `s` 中所有字符都已经被选过。
在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 `s` 中字符重新排序后的 **结果字符串** 。

 

 **示例 1：** 

```
输入：s = "aaaabbbbcccc"
输出："abccbaabccba"
解释：第一轮的步骤 1，2，3 后，结果字符串为 result = "abc"
第一轮的步骤 4，5，6 后，结果字符串为 result = "abccba"
第一轮结束，现在 s = "aabbcc" ，我们再次回到步骤 1
第二轮的步骤 1，2，3 后，结果字符串为 result = "abccbaabc"
第二轮的步骤 4，5，6 后，结果字符串为 result = "abccbaabccba"

```
 **示例 2：** 

```
输入：s = "rat"
输出："art"
解释：单词 "rat" 在上述算法重排序以后变成 "art"

```
 **示例 3：** 

```
输入：s = "leetcode"
输出："cdelotee"

```
 **示例 4：** 

```
输入：s = "ggggggg"
输出："ggggggg"

```
 **示例 5：** 

```
输入：s = "spo"
输出："ops"

```
 

 **提示：** 
-  `1 <= s.length <= 500` 
-  `s` 只包含小写英文字母。
 
**标签**
`哈希表` `字符串` `计数` 


## 
```python

```
>
# 1371.每个元音包含偶数次的最长子字符串
[https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts](https://leetcode-cn.com/problems/find-the-longest-substring-containing-vowels-in-even-counts) 
## 原题
给你一个字符串 `s` ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 ';a';，';e';，';i';，';o';，';u'; ，在子字符串中都恰好出现了偶数次。

 

 **示例 1：** 

```

输入：s = "eleetminicoworoep"
输出：13
解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。

```
 **示例 2：** 

```

输入：s = "leetcodeisgreat"
输出：5
解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。

```
 **示例 3：** 

```

输入：s = "bcbcbc"
输出：6
解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。

```
 

 **提示：** 
-  `1 <= s.length <= 5 x 10^5` 
-  `s` 只包含小写英文字母。
 
**标签**
`位运算` `哈希表` `字符串` `前缀和` 


## 
```python

```
>
# 1372.二叉树中的最长交错路径
[https://leetcode-cn.com/problems/longest-zigzag-path-in-a-binary-tree](https://leetcode-cn.com/problems/longest-zigzag-path-in-a-binary-tree) 
## 原题
给你一棵以 `root` 为根的二叉树，二叉树中的交错路径定义如下：
- 选择二叉树中 **任意** 节点和一个方向（左或者右）。
- 如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
- 改变前进方向：左变右或者右变左。
- 重复第二步和第三步，直到你在树中无法继续移动。
交错路径的长度定义为： **访问过的节点数目 - 1** （单个节点的路径长度为 0 ）。

请你返回给定树中最长 **交错路径** 的长度。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/07/sample_1_1702.png" style="height: 283px; width: 151px;">** 

```
输入：root = [1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]
输出：3
解释：蓝色节点为树中最长交错路径（右 -> 左 -> 右）。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/07/sample_2_1702.png" style="height: 253px; width: 120px;">** 

```
输入：root = [1,1,1,null,1,null,null,1,1,null,1]
输出：4
解释：蓝色节点为树中最长交错路径（左 -> 右 -> 左 -> 右）。

```
 **示例 3：** 

```
输入：root = [1]
输出：0

```
 

 **提示：** 
- 每棵树最多有 `50000` 个节点。
- 每个节点的值在 `[1, 100]` 之间。
 
**标签**
`树` `深度优先搜索` `动态规划` `二叉树` 


## 
```python

```
>
# 1373.二叉搜索子树的最大键值和
[https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree](https://leetcode-cn.com/problems/maximum-sum-bst-in-binary-tree) 
## 原题
给你一棵以  `root`  为根的  **二叉树**  ，请你返回 **任意**  二叉搜索子树的最大键值和。

二叉搜索树的定义如下：
- 任意节点的左子树中的键值都  **小于**  此节点的键值。
- 任意节点的右子树中的键值都 **大于**  此节点的键值。
- 任意节点的左子树和右子树都是二叉搜索树。
 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/07/sample_1_1709.png" style="height: 250px; width: 320px;" />

```

输入：root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
输出：20
解释：键值为 3 的子树是和最大的二叉搜索树。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/07/sample_2_1709.png" style="height: 180px; width: 134px;" />

```

输入：root = [4,3,null,1,2]
输出：2
解释：键值为 2 的单节点子树是和最大的二叉搜索树。

```
 **示例 3：** 

```

输入：root = [-4,-2,-5]
输出：0
解释：所有节点键值都为负数，和最大的二叉搜索树为空。

```
 **示例 4：** 

```

输入：root = [2,1,3]
输出：6

```
 **示例 5：** 

```

输入：root = [5,4,8,3,null,6,3]
输出：7

```
 

 **提示：** 
- 每棵树有 `1` 到 `40000`  个节点。
- 每个节点的键值在  `[-4 * 10^4 , 4 * 10^4]` 之间。
 
**标签**
`树` `深度优先搜索` `二叉搜索树` `动态规划` `二叉树` 


## 
```python

```
>
# 1374.生成每种字符都是奇数个的字符串
[https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts](https://leetcode-cn.com/problems/generate-a-string-with-characters-that-have-odd-counts) 
## 原题
给你一个整数 `n` ，请你返回一个含 *`n`* 个字符的字符串，其中每种字符在该字符串中都恰好出现 **奇数次** ***。*** 

返回的字符串必须只含小写英文字母。如果存在多个满足题目要求的字符串，则返回其中任意一个即可。

 

 **示例 1：** 

```
输入：n = 4
输出："pppz"
解释："pppz" 是一个满足题目要求的字符串，因为 ';p'; 出现 3 次，且 ';z'; 出现 1 次。当然，还有很多其他字符串也满足题目要求，比如："ohhh" 和 "love"。

```
 **示例 2：** 

```
输入：n = 2
输出："xy"
解释："xy" 是一个满足题目要求的字符串，因为 ';x'; 和 ';y'; 各出现 1 次。当然，还有很多其他字符串也满足题目要求，比如："ag" 和 "ur"。

```
 **示例 3：** 

```
输入：n = 7
输出："holasss"

```
 

 **提示：** 
-  `1 <= n <= 500` 
 
**标签**
`字符串` 


## 
```python

```
>
# 1375.二进制字符串前缀一致的次数
[https://leetcode-cn.com/problems/number-of-times-binary-string-is-prefix-aligned](https://leetcode-cn.com/problems/number-of-times-binary-string-is-prefix-aligned) 
## 原题
给你一个长度为 `n` 、下标从 **1** 开始的二进制字符串，所有位最开始都是 `0` 。我们会按步翻转该二进制字符串的所有位（即，将 `0` 变为 `1` ）。

给你一个下标从 **1** 开始的整数数组 `flips` ，其中 `flips[i]` 表示对应下标 `i` 的位将会在第 `i` 步翻转。

二进制字符串 **前缀一致** 需满足：在第 `i` 步之后，在 **闭** 区间 `[1, i]` 内的所有位都是 1 ，而其他位都是 0 。

返回二进制字符串在翻转过程中 **前缀一致** 的次数。

 

 **示例 1：** 

```

输入：flips = [3,2,4,1,5]
输出：2
解释：二进制字符串最开始是 "00000" 。
执行第 1 步：字符串变为 "00100" ，不属于前缀一致的情况。
执行第 2 步：字符串变为 "01100" ，不属于前缀一致的情况。
执行第 3 步：字符串变为 "01110" ，不属于前缀一致的情况。
执行第 4 步：字符串变为 "11110" ，属于前缀一致的情况。
执行第 5 步：字符串变为 "11111" ，属于前缀一致的情况。
在翻转过程中，前缀一致的次数为 2 ，所以返回 2 。

```
 **示例 2：** 

```

输入：flips = [4,1,2,3]
输出：1
解释：二进制字符串最开始是 "0000" 。
执行第 1 步：字符串变为 "0001" ，不属于前缀一致的情况。
执行第 2 步：字符串变为 "1001" ，不属于前缀一致的情况。
执行第 3 步：字符串变为 "1101" ，不属于前缀一致的情况。
执行第 4 步：字符串变为 "1111" ，属于前缀一致的情况。
在翻转过程中，前缀一致的次数为 1 ，所以返回 1 。
```
 

 **提示：** 
-  `n == flips.length` 
-  `1 <= n <= 5 * 10^4` 
-  `flips` 是范围 `[1, n]` 中所有整数构成的一个排列
 
**标签**
`数组` 


## 
```python

```
>
# 1376.通知所有员工所需的时间
[https://leetcode-cn.com/problems/time-needed-to-inform-all-employees](https://leetcode-cn.com/problems/time-needed-to-inform-all-employees) 
## 原题
公司里有 `n` 名员工，每个员工的 ID 都是独一无二的，编号从 `0` 到 `n - 1` 。公司的总负责人通过 `headID` 进行标识。

在 `manager` 数组中，每个员工都有一个直属负责人，其中 `manager[i]` 是第 `i` 名员工的直属负责人。对于总负责人， `manager[headID] = -1` 。题目保证从属关系可以用树结构显示。

公司总负责人想要向公司所有员工通告一条紧急消息。他将会首先通知他的直属下属们，然后由这些下属通知他们的下属，直到所有的员工都得知这条紧急消息。

第 `i` 名员工需要 `informTime[i]` 分钟来通知它的所有直属下属（也就是说在 `informTime[i]` 分钟后，他的所有直属下属都可以开始传播这一消息）。

返回通知所有员工这一紧急消息所需要的 **分钟数** 。

 

 **示例 1：** 

```
输入：n = 1, headID = 0, manager = [-1], informTime = [0]
输出：0
解释：公司总负责人是该公司的唯一一名员工。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/08/graph.png" style="height: 174px; width: 404px;">

```
输入：n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
输出：1
解释：id = 2 的员工是公司的总负责人，也是其他所有员工的直属负责人，他需要 1 分钟来通知所有员工。
上图显示了公司员工的树结构。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/08/1730_example_3_5.PNG" style="height: 432px; width: 568px;">

```
输入：n = 7, headID = 6, manager = [1,2,3,4,5,6,-1], informTime = [0,6,5,4,3,2,1]
输出：21
解释：总负责人 id = 6。他将在 1 分钟内通知 id = 5 的员工。
id = 5 的员工将在 2 分钟内通知 id = 4 的员工。
id = 4 的员工将在 3 分钟内通知 id = 3 的员工。
id = 3 的员工将在 4 分钟内通知 id = 2 的员工。
id = 2 的员工将在 5 分钟内通知 id = 1 的员工。
id = 1 的员工将在 6 分钟内通知 id = 0 的员工。
所需时间 = 1 + 2 + 3 + 4 + 5 + 6 = 21 。

```
 **示例 4：** 

```
输入：n = 15, headID = 0, manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6], informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
输出：3
解释：第一分钟总负责人通知员工 1 和 2 。
第二分钟他们将会通知员工 3, 4, 5 和 6 。
第三分钟他们将会通知剩下的员工。

```
 **示例 5：** 

```
输入：n = 4, headID = 2, manager = [3,3,-1,2], informTime = [0,0,162,914]
输出：1076

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `0 <= headID < n` 
-  `manager.length == n` 
-  `0 <= manager[i] < n` 
-  `manager[headID] == -1` 
-  `informTime.length == n` 
-  `0 <= informTime[i] <= 1000` 
- 如果员工 `i` 没有下属， `informTime[i] == 0` 。
- 题目 **保证** 所有员工都可以收到通知。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` 


## 
```python

```
>
# 1377.T 秒后青蛙的位置
[https://leetcode-cn.com/problems/frog-position-after-t-seconds](https://leetcode-cn.com/problems/frog-position-after-t-seconds) 
## 原题
给你一棵由 n 个顶点组成的无向树，顶点编号从 1 到 `n` 。青蛙从 **顶点 1** 开始起跳。规则如下：
- 在一秒内，青蛙从它所在的当前顶点跳到另一个 **未访问** 过的顶点（如果它们直接相连）。
- 青蛙无法跳回已经访问过的顶点。
- 如果青蛙可以跳到多个不同顶点，那么它跳到其中任意一个顶点上的机率都相同。
- 如果青蛙不能跳到任何未访问过的顶点上，那么它每次跳跃都会停留在原地。
无向树的边用数组 `edges` 描述，其中 `edges[i] = [from<sub>i</sub>, to<sub>i</sub>]` 意味着存在一条直接连通 `from<sub>i</sub>` 和 `to<sub>i</sub>` 两个顶点的边。

返回青蛙在 *`t`* 秒后位于目标顶点 *`target`* 上的概率。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/08/frog_2.png" style="height: 236px; width: 350px;">

```
输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
输出：0.16666666666666666 
解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，第 1 秒 有 1/3 的概率跳到顶点 2 ，然后第 2 秒 有 1/2 的概率跳到顶点 4，因此青蛙在 2 秒后位于顶点 4 的概率是 1/3 * 1/2 = 1/6 = 0.16666666666666666 。 

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/08/frog_3.png" style="height: 236px; width: 350px;">** 

```
输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
输出：0.3333333333333333
解释：上图显示了青蛙的跳跃路径。青蛙从顶点 1 起跳，有 1/3 = 0.3333333333333333 的概率能够 1 秒 后跳到顶点 7 。 

```
 **示例 3：** 

```
输入：n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
输出：0.16666666666666666

```
 

 **提示：** 
-  `1 <= n <= 100` 
-  `edges.length == n-1` 
-  `edges[i].length == 2` 
-  `1 <= edges[i][0], edges[i][1] <= n` 
-  `1 <= t <= 50` 
-  `1 <= target <= n` 
- 与准确值误差在 `10^-5` 之内的结果将被判定为正确。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `图` 


## 
```python

```
>
# 1378.使用唯一标识码替换员工ID
[https://leetcode-cn.com/problems/replace-employee-id-with-the-unique-identifier](https://leetcode-cn.com/problems/replace-employee-id-with-the-unique-identifier) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1379.找出克隆二叉树中的相同节点
[https://leetcode-cn.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree](https://leetcode-cn.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree) 
## 原题
给你两棵二叉树，原始树 `original` 和克隆树 `cloned` ，以及一个位于原始树 `original` 中的目标节点 `target` 。

其中，克隆树 `cloned` 是原始树 `original` 的一个 **副本** 。

请找出在树 `cloned` 中，与 `target` **相同** 的节点，并返回对该节点的引用（在 C/C++ 等有指针的语言中返回 节点指针，其他语言返回节点本身）。

 

 **注意：** 
- 你 **不能** 对两棵二叉树，以及 `target` 节点进行更改。
-  **只能** 返回对克隆树 `cloned` 中已有的节点的引用。
 **进阶：** 如果树中允许出现值相同的节点，你将如何解答？

 
 **示例 1:** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e1.png" style="height: 426px; width: 544px;">

```
输入: tree = [7,4,3,null,null,6,19], target = 3
输出: 3
解释: 上图画出了树 original 和 cloned。target 节点在树 original 中，用绿色标记。答案是树 cloned 中的黄颜色的节点（其他示例类似）。
```
 **示例 2:** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e2.png" style="height: 159px; width: 221px;">

```
输入: tree = [7], target =  7
输出: 7

```
 **示例 3:** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e3.png" style="height: 486px; width: 459px;">

```
输入: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
输出: 4

```
 **示例 4:** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e4.png" style="height: 239px; width: 555px;">

```
输入: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
输出: 5

```
 **示例 5:** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/02/21/e5.png" style="height: 345px; width: 427px;">

```
输入: tree = [1,2,null,3], target = 2
输出: 2
```
 

 **提示：** 
- 树中节点的数量范围为 `[1, 10^4]` 。
- 同一棵树中，没有值相同的节点。
-  `target` 节点是树 `original` 中的一个节点，并且不会是 `null` 。
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 1380.矩阵中的幸运数
[https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix](https://leetcode-cn.com/problems/lucky-numbers-in-a-matrix) 
## 原题
给你一个 `m * n` 的矩阵，矩阵中的数字 **各不相同** 。请你按 **任意** 顺序返回矩阵中的所有幸运数。

幸运数是指矩阵中满足同时下列两个条件的元素：
- 在同一行的所有元素中最小
- 在同一列的所有元素中最大
 

 **示例 1：** 

```
输入：matrix = [[3,7,8],[9,11,13],[15,16,17]]
输出：[15]
解释：15 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

```
 **示例 2：** 

```
输入：matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
输出：[12]
解释：12 是唯一的幸运数，因为它是其所在行中的最小值，也是所在列中的最大值。

```
 **示例 3：** 

```
输入：matrix = [[7,8],[1,2]]
输出：[7]

```
 

 **提示：** 
-  `m == mat.length` 
-  `n == mat[i].length` 
-  `1 <= n, m <= 50` 
-  `1 <= matrix[i][j] <= 10^5` 
- 矩阵中的所有元素都是不同的
 
**标签**
`数组` `矩阵` 


## 
```python

```
>
# 1381.设计一个支持增量操作的栈
[https://leetcode-cn.com/problems/design-a-stack-with-increment-operation](https://leetcode-cn.com/problems/design-a-stack-with-increment-operation) 
## 原题
请你设计一个支持下述操作的栈。

实现自定义栈类 `CustomStack` ：
-  `CustomStack(int maxSize)` ：用 `maxSize` 初始化对象， `maxSize` 是栈中最多能容纳的元素数量，栈在增长到 `maxSize` 之后则不支持 `push` 操作。
-  `void push(int x)` ：如果栈还未增长到 `maxSize` ，就将 `x` 添加到栈顶。
-  `int pop()` ：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 **-1** 。
-  `void inc(int k, int val)` ：栈底的 `k` 个元素的值都增加 `val` 。如果栈中元素总数小于 `k` ，则栈中的所有元素都增加 `val` 。
 

 **示例：** 

```
输入：
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
输出：
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
解释：
CustomStack customStack = new CustomStack(3); // 栈是空的 []
customStack.push(1);                          // 栈变为 [1]
customStack.push(2);                          // 栈变为 [1, 2]
customStack.pop();                            // 返回 2 --> 返回栈顶值 2，栈变为 [1]
customStack.push(2);                          // 栈变为 [1, 2]
customStack.push(3);                          // 栈变为 [1, 2, 3]
customStack.push(4);                          // 栈仍然是 [1, 2, 3]，不能添加其他元素使栈大小变为 4
customStack.increment(5, 100);                // 栈变为 [101, 102, 103]
customStack.increment(2, 100);                // 栈变为 [201, 202, 103]
customStack.pop();                            // 返回 103 --> 返回栈顶值 103，栈变为 [201, 202]
customStack.pop();                            // 返回 202 --> 返回栈顶值 202，栈变为 [201]
customStack.pop();                            // 返回 201 --> 返回栈顶值 201，栈变为 []
customStack.pop();                            // 返回 -1 --> 栈为空，返回 -1

```
 

 **提示：** 
-  `1 <= maxSize <= 1000` 
-  `1 <= x <= 1000` 
-  `1 <= k <= 1000` 
-  `0 <= val <= 100` 
- 每种方法 `increment` ， `push` 以及 `pop` 分别最多调用 `1000` 次
 
**标签**
`栈` `设计` `数组` 


## 
```python

```
>
# 1382.将二叉搜索树变平衡
[https://leetcode-cn.com/problems/balance-a-binary-search-tree](https://leetcode-cn.com/problems/balance-a-binary-search-tree) 
## 原题
给你一棵二叉搜索树，请你返回一棵 **平衡后** 的二叉搜索树，新生成的树应该与原来的树有着相同的节点值。

如果一棵二叉搜索树中，每个节点的两棵子树高度差不超过 1 ，我们就称这棵二叉搜索树是 **平衡的** 。

如果有多种构造方法，请你返回任意一种。

 

 **示例：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/15/1515_ex1.png" style="height: 248px; width: 250px;"><img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/15/1515_ex1_out.png" style="height: 200px; width: 200px;">** 

```
输入：root = [1,null,2,null,3,null,4,null,null]
输出：[2,1,3,null,null,null,4]
解释：这不是唯一的正确答案，[3,1,4,null,2,null,null] 也是一个可行的构造方案。

```
 

 **提示：** 
- 树节点的数目在 `1` 到 `10^4` 之间。
- 树节点的值互不相同，且在 `1` 到 `10^5` 之间。
 
**标签**
`贪心` `树` `深度优先搜索` `二叉搜索树` `分治` `二叉树` 


## 
```python

```
>
# 1383.最大的团队表现值
[https://leetcode-cn.com/problems/maximum-performance-of-a-team](https://leetcode-cn.com/problems/maximum-performance-of-a-team) 
## 原题
公司有编号为 `1` 到 `n` 的 `n` 个工程师，给你两个数组 `speed` 和 `efficiency` ，其中 `speed[i]` 和 `efficiency[i]` 分别代表第 `i` 位工程师的速度和效率。请你返回由最多 `k` 个工程师组成的 **​​​​​​最大团队表现值** ，由于答案可能很大，请你返回结果对 `10^9 + 7` 取余后的结果。

 **团队表现值** 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。

 

 **示例 1：** 

```
输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
输出：60
解释：
我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为 performance = (10 + 5) * min(4, 7) = 60 。

```
 **示例 2：** 

```
输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
输出：68
解释：
此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance = (2 + 10 + 5) * min(5, 4, 7) = 68 。

```
 **示例 3：** 

```
输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
输出：72

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `speed.length == n` 
-  `efficiency.length == n` 
-  `1 <= speed[i] <= 10^5` 
-  `1 <= efficiency[i] <= 10^8` 
-  `1 <= k <= n` 
 
**标签**
`贪心` `数组` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1384.按年度列出销售总额
[https://leetcode-cn.com/problems/total-sales-amount-by-year](https://leetcode-cn.com/problems/total-sales-amount-by-year) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1385.两个数组间的距离值
[https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays](https://leetcode-cn.com/problems/find-the-distance-value-between-two-arrays) 
## 原题
给你两个整数数组 `arr1` ， `arr2` 和一个整数 `d` ，请你返回两个数组之间的 **距离值** 。

「 **距离值** 」 **** 定义为符合此距离要求的元素数目：对于元素 `arr1[i]` ，不存在任何元素 `arr2[j]` 满足 `|arr1[i]-arr2[j]| <= d` 。

 

 **示例 1：** 

```
输入：arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
输出：2
解释：
对于 arr1[0]=4 我们有：
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
所以 arr1[0]=4 符合距离要求

对于 arr1[1]=5 我们有：
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
所以 arr1[1]=5 也符合距离要求

对于 arr1[2]=8 我们有：
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2
存在距离小于等于 2 的情况，不符合距离要求 

故而只有 arr1[0]=4 和 arr1[1]=5 两个符合距离要求，距离值为 2
```
 **示例 2：** 

```
输入：arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3
输出：2

```
 **示例 3：** 

```
输入：arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6
输出：1

```
 

 **提示：** 
-  `1 <= arr1.length, arr2.length <= 500` 
-  `-10^3 <= arr1[i], arr2[j] <= 10^3` 
-  `0 <= d <= 100` 
 
**标签**
`数组` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 1386.安排电影院座位
[https://leetcode-cn.com/problems/cinema-seat-allocation](https://leetcode-cn.com/problems/cinema-seat-allocation) 
## 原题
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/cinema_seats_1.png" style="height: 149px; width: 400px;">

如上图所示，电影院的观影厅中有 `n` 行座位，行编号从 1 到 `n` ，且每一行内总共有 10 个座位，列编号从 1 到 10 。

给你数组 `reservedSeats` ，包含所有已经被预约了的座位。比如说， `researvedSeats[i]=[3,8]` ，它表示第 **3** 行第 **8** 个座位被预约了。

请你返回 **最多能安排多少个 4 人家庭** 。4 人家庭要占据 **同一行内连续** 的 4 个座位。隔着过道的座位（比方说 [3,3] 和 [3,4]）不是连续的座位，但是如果你可以将 4 人家庭拆成过道两边各坐 2 人，这样子是允许的。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/cinema_seats_3.png" style="height: 96px; width: 400px;">

```
输入：n = 3, reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
输出：4
解释：上图所示是最优的安排方案，总共可以安排 4 个家庭。蓝色的叉表示被预约的座位，橙色的连续座位表示一个 4 人家庭。

```
 **示例 2：** 

```
输入：n = 2, reservedSeats = [[2,1],[1,8],[2,6]]
输出：2

```
 **示例 3：** 

```
输入：n = 4, reservedSeats = [[4,3],[1,4],[4,6],[1,7]]
输出：4

```
 

 **提示：** 
-  `1 <= n <= 10^9` 
-  `1 <= reservedSeats.length <= min(10*n, 10^4)` 
-  `reservedSeats[i].length == 2` 
-  `1 <= reservedSeats[i][0] <= n` 
-  `1 <= reservedSeats[i][1] <= 10` 
- 所有 `reservedSeats[i]` 都是互不相同的。
 
**标签**
`贪心` `位运算` `数组` `哈希表` 


## 
```python

```
>
# 1387.将整数按权重排序
[https://leetcode-cn.com/problems/sort-integers-by-the-power-value](https://leetcode-cn.com/problems/sort-integers-by-the-power-value) 
## 原题
我们将整数 `x` 的 **权重** 定义为按照下述规则将 `x` 变成 `1` 所需要的步数：
- 如果 `x` 是偶数，那么 `x = x / 2` 
- 如果 `x` 是奇数，那么 `x = 3 * x + 1` 
比方说，x=3 的权重为 7 。因为 3 需要 7 步变成 1 （3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）。

给你三个整数 `lo` ， `hi` 和 `k` 。你的任务是将区间 `[lo, hi]` 之间的整数按照它们的权重 **升序排序** ，如果大于等于 2 个整数有 **相同** 的权重，那么按照数字自身的数值 **升序排序** 。

请你返回区间 `[lo, hi]` 之间的整数按权重排序后的第 `k` 个数。

注意，题目保证对于任意整数 `x` `（lo <= x <= hi）` ，它变成 `1` 所需要的步数是一个 32 位有符号整数。

 

 **示例 1：** 

```
输入：lo = 12, hi = 15, k = 2
输出：13
解释：12 的权重为 9（12 --> 6 --> 3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1）
13 的权重为 9
14 的权重为 17
15 的权重为 17
区间内的数按权重排序以后的结果为 [12,13,14,15] 。对于 k = 2 ，答案是第二个整数也就是 13 。
注意，12 和 13 有相同的权重，所以我们按照它们本身升序排序。14 和 15 同理。

```
 **示例 2：** 

```
输入：lo = 1, hi = 1, k = 1
输出：1

```
 **示例 3：** 

```
输入：lo = 7, hi = 11, k = 4
输出：7
解释：区间内整数 [7, 8, 9, 10, 11] 对应的权重为 [16, 3, 19, 6, 14] 。
按权重排序后得到的结果为 [8, 10, 11, 7, 9] 。
排序后数组中第 4 个数字为 7 。

```
 **示例 4：** 

```
输入：lo = 10, hi = 20, k = 5
输出：13

```
 **示例 5：** 

```
输入：lo = 1, hi = 1000, k = 777
输出：570

```
 

 **提示：** 
-  `1 <= lo <= hi <= 1000` 
-  `1 <= k <= hi - lo + 1` 
 
**标签**
`记忆化搜索` `动态规划` `排序` 


## 
```python

```
>
# 1388.3n 块披萨
[https://leetcode-cn.com/problems/pizza-with-3n-slices](https://leetcode-cn.com/problems/pizza-with-3n-slices) 
## 原题
给你一个披萨，它由 3n 块不同大小的部分组成，现在你和你的朋友们需要按照如下规则来分披萨：
- 你挑选 **任意** 一块披萨。
- Alice 将会挑选你所选择的披萨逆时针方向的下一块披萨。
- Bob 将会挑选你所选择的披萨顺时针方向的下一块披萨。
- 重复上述过程直到没有披萨剩下。
每一块披萨的大小按顺时针方向由循环数组 `slices` 表示。

请你返回你可以获得的披萨大小总和的最大值。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/sample_3_1723.png" style="height: 240px; width: 475px;">

```
输入：slices = [1,2,3,4,5,6]
输出：10
解释：选择大小为 4 的披萨，Alice 和 Bob 分别挑选大小为 3 和 5 的披萨。然后你选择大小为 6 的披萨，Alice 和 Bob 分别挑选大小为 2 和 1 的披萨。你获得的披萨总大小为 4 + 6 = 10 。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/sample_4_1723.png" style="height: 250px; width: 475px;">** 

```
输入：slices = [8,9,8,6,1,1]
输出：16
解释：两轮都选大小为 8 的披萨。如果你选择大小为 9 的披萨，你的朋友们就会选择大小为 8 的披萨，这种情况下你的总和不是最大的。

```
 **示例 3：** 

```
输入：slices = [4,1,2,5,8,3,1,9,7]
输出：21

```
 **示例 4：** 

```
输入：slices = [3,1,2]
输出：3

```
 

 **提示：** 
-  `1 <= slices.length <= 500` 
-  `slices.length % 3 == 0` 
-  `1 <= slices[i] <= 1000` 
 
**标签**
`贪心` `数组` `动态规划` `堆（优先队列）` 


## 
```python

```
>
# 1389.按既定顺序创建目标数组
[https://leetcode-cn.com/problems/create-target-array-in-the-given-order](https://leetcode-cn.com/problems/create-target-array-in-the-given-order) 
## 原题
给你两个整数数组 `nums` 和 `index` 。你需要按照以下规则创建目标数组：
- 目标数组 `target` 最初为空。
- 按从左到右的顺序依次读取 `nums[i]` 和 `index[i]` ，在 `target` 数组中的下标 `index[i]` 处插入值 `nums[i]` 。
- 重复上一步，直到在 `nums` 和 `index` 中都没有要读取的元素。
请你返回目标数组。

题目保证数字插入位置总是存在。

 

 **示例 1：** 

```
输入：nums = [0,1,2,3,4], index = [0,1,2,2,1]
输出：[0,4,1,3,2]
解释：
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

```
 **示例 2：** 

```
输入：nums = [1,2,3,4,0], index = [0,1,2,3,0]
输出：[0,1,2,3,4]
解释：
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]

```
 **示例 3：** 

```
输入：nums = [1], index = [0]
输出：[1]

```
 

 **提示：** 
-  `1 <= nums.length, index.length <= 100` 
-  `nums.length == index.length` 
-  `0 <= nums[i] <= 100` 
-  `0 <= index[i] <= i` 
 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 1390.四因数
[https://leetcode-cn.com/problems/four-divisors](https://leetcode-cn.com/problems/four-divisors) 
## 原题
给你一个整数数组 `nums` ，请你返回该数组中恰有四个因数的这些整数的各因数之和。

如果数组中不存在满足题意的整数，则返回 `0` 。

 

 **示例：** 

```
输入：nums = [21,4,7]
输出：32
解释：
21 有 4 个因数：1, 3, 7, 21
4 有 3 个因数：1, 2, 4
7 有 2 个因数：1, 7
答案仅为 21 的所有因数的和。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `1 <= nums[i] <= 10^5` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 1391.检查网格中是否存在有效路径
[https://leetcode-cn.com/problems/check-if-there-is-a-valid-path-in-a-grid](https://leetcode-cn.com/problems/check-if-there-is-a-valid-path-in-a-grid) 
## 原题
给你一个 *m* x *n* 的网格 `grid` 。网格里的每个单元都代表一条街道。 `grid[i][j]` 的街道可以是：
-  **1** 表示连接左单元格和右单元格的街道。
-  **2** 表示连接上单元格和下单元格的街道。
-  **3** 表示连接左单元格和下单元格的街道。
-  **4** 表示连接右单元格和下单元格的街道。
-  **5** 表示连接左单元格和上单元格的街道。
-  **6** 表示连接右单元格和上单元格的街道。
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/main.png" style="height: 708px; width: 450px;">

你最开始从左上角的单元格 `(0,0)` 开始出发，网格中的「有效路径」是指从左上方的单元格 `(0,0)` 开始、一直到右下方的 `(m-1,n-1)` 结束的路径。 **该路径必须只沿着街道走** 。

 **注意：** 你 **不能** 变更街道。

如果网格中存在有效的路径，则返回 `true` ，否则返回 `false` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/e1.png" style="height: 311px; width: 455px;">

```
输入：grid = [[2,4,3],[6,5,2]]
输出：true
解释：如图所示，你可以从 (0, 0) 开始，访问网格中的所有单元格并到达 (m - 1, n - 1) 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/03/21/e2.png" style="height: 293px; width: 455px;">

```
输入：grid = [[1,2,1],[1,2,1]]
输出：false
解释：如图所示，单元格 (0, 0) 上的街道没有与任何其他单元格上的街道相连，你只会停在 (0, 0) 处。

```
 **示例 3：** 

```
输入：grid = [[1,1,2]]
输出：false
解释：你会停在 (0, 1)，而且无法到达 (0, 2) 。

```
 **示例 4：** 

```
输入：grid = [[1,1,1,1,1,1,3]]
输出：true

```
 **示例 5：** 

```
输入：grid = [[2],[2],[2],[2],[2],[2],[6]]
输出：true

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 300` 
-  `1 <= grid[i][j] <= 6` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` 


## 
```python

```
>
# 1392.最长快乐前缀
[https://leetcode-cn.com/problems/longest-happy-prefix](https://leetcode-cn.com/problems/longest-happy-prefix) 
## 原题
「快乐前缀」是在原字符串中既是 **非空** 前缀也是后缀（不包括原字符串自身）的字符串。

给你一个字符串 `s` ，请你返回它的 **最长快乐前缀** 。

如果不存在满足题意的前缀，则返回一个空字符串。

 

 **示例 1：** 

```
输入：s = "level"
输出："l"
解释：不包括 s 自己，一共有 4 个前缀（"l", "le", "lev", "leve"）和 4 个后缀（"l", "el", "vel", "evel"）。最长的既是前缀也是后缀的字符串是 "l" 。

```
 **示例 2：** 

```
输入：s = "ababab"
输出："abab"
解释："abab" 是最长的既是前缀也是后缀的字符串。题目允许前后缀在原字符串中重叠。

```
 **示例 3：** 

```
输入：s = "leetcodeleet"
输出："leet"

```
 **示例 4：** 

```
输入：s = "a"
输出：""

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s` 只含有小写英文字母
 
**标签**
`字符串` `字符串匹配` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 1393.股票的资本损益
[https://leetcode-cn.com/problems/capital-gainloss](https://leetcode-cn.com/problems/capital-gainloss) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1394.找出数组中的幸运数
[https://leetcode-cn.com/problems/find-lucky-integer-in-an-array](https://leetcode-cn.com/problems/find-lucky-integer-in-an-array) 
## 原题
在整数数组中，如果一个整数的出现频次和它的数值大小相等，我们就称这个整数为「幸运数」。

给你一个整数数组 `arr` ，请你从中找出并返回一个幸运数。
- 如果数组中存在多个幸运数，只需返回 **最大** 的那个。
- 如果数组中不含幸运数，则返回 **-1** 。
 

 **示例 1：** 

```
输入：arr = [2,2,3,4]
输出：2
解释：数组中唯一的幸运数是 2 ，因为数值 2 的出现频次也是 2 。

```
 **示例 2：** 

```
输入：arr = [1,2,2,3,3,3]
输出：3
解释：1、2 以及 3 都是幸运数，只需要返回其中最大的 3 。

```
 **示例 3：** 

```
输入：arr = [2,2,2,3,3]
输出：-1
解释：数组中不存在幸运数。

```
 **示例 4：** 

```
输入：arr = [5]
输出：-1

```
 **示例 5：** 

```
输入：arr = [7,7,7,7,7,7,7]
输出：7

```
 

 **提示：** 
-  `1 <= arr.length <= 500` 
-  `1 <= arr[i] <= 500` 
 
**标签**
`数组` `哈希表` `计数` 


## 
```python

```
>
# 1395.统计作战单位数
[https://leetcode-cn.com/problems/count-number-of-teams](https://leetcode-cn.com/problems/count-number-of-teams) 
## 原题
  `n` 名士兵站成一排。每个士兵都有一个 **独一无二** 的评分 `rating` 。

每 **3** 个士兵可以组成一个作战单位，分组规则如下：
- 从队伍中选出下标分别为 `i` 、 `j` 、 `k` 的 3 名士兵，他们的评分分别为 `rating[i]` 、 `rating[j]` 、 `rating[k]` 
- 作战单位需满足： `rating[i] < rating[j] < rating[k]` 或者 `rating[i] > rating[j] > rating[k]` ，其中  `0 <= i < j < k < n` 
请你返回按上述条件可以组建的作战单位数量。每个士兵都可以是多个作战单位的一部分。

 

 **示例 1：** 

```

输入：rating = [2,5,3,4,1]
输出：3
解释：我们可以组建三个作战单位 (2,3,4)、(5,4,1)、(5,3,1) 。

```
 **示例 2：** 

```

输入：rating = [2,1,3]
输出：0
解释：根据题目条件，我们无法组建作战单位。

```
 **示例 3：** 

```

输入：rating = [1,2,3,4]
输出：4

```
 

 **提示：** 
-  `n == rating.length` 
-  `3 <= n <= 1000` 
-  `1 <= rating[i] <= 10^5` 
-  `rating`  中的元素都是唯一的
 
**标签**
`树状数组` `数组` `动态规划` 


## 
```python

```
>
# 1396.设计地铁系统
[https://leetcode-cn.com/problems/design-underground-system](https://leetcode-cn.com/problems/design-underground-system) 
## 原题
地铁系统跟踪不同车站之间的乘客出行时间，并使用这一数据来计算从一站到另一站的平均时间。

实现 `UndergroundSystem` 类：
-  `void checkIn(int id, string stationName, int t)` 

	
- 通行卡 ID 等于 `id` 的乘客，在时间 `t` ，从 `stationName` 站进入
- 乘客一次只能从一个站进入
	
	
-  `void checkOut(int id, string stationName, int t)` 
	
- 通行卡 ID 等于 `id` 的乘客，在时间 `t` ，从 `stationName` 站离开
	
	
-  `double getAverageTime(string startStation, string endStation)` 
	
- 返回从 `startStation` 站到 `endStation` 站的平均时间
- 平均时间会根据截至目前所有从 `startStation` 站 **直接** 到达 `endStation` 站的行程进行计算，也就是从 `startStation` 站进入并从 `endStation` 离开的行程
- 从 `startStation` 到 `endStation` 的行程时间与从 `endStation` 到 `startStation` 的行程时间可能不同
- 在调用 `getAverageTime` 之前，至少有一名乘客从 `startStation` 站到达 `endStation` 站
	
	
你可以假设对 `checkIn` 和 `checkOut` 方法的所有调用都是符合逻辑的。如果一名乘客在时间 `t<sub>1</sub>` 进站、时间 `t<sub>2</sub>` 出站，那么 `t<sub>1</sub> < t<sub>2</sub>` 。所有时间都按时间顺序发生。
 

 **示例 1：** 

```

输入
["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
[[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]

输出
[null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]

解释
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(45, "Leyton", 3);
undergroundSystem.checkIn(32, "Paradise", 8);
undergroundSystem.checkIn(27, "Leyton", 10);
undergroundSystem.checkOut(45, "Waterloo", 15);  // 乘客 45 "Leyton" -> "Waterloo" ，用时 15-3 = 12
undergroundSystem.checkOut(27, "Waterloo", 20);  // 乘客 27 "Leyton" -> "Waterloo" ，用时 20-10 = 10
undergroundSystem.checkOut(32, "Cambridge", 22); // 乘客 32 "Paradise" -> "Cambridge" ，用时 22-8 = 14
undergroundSystem.getAverageTime("Paradise", "Cambridge"); // 返回 14.00000 。只有一个 "Paradise" -> "Cambridge" 的行程，(14) / 1 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // 返回 11.00000 。有两个 "Leyton" -> "Waterloo" 的行程，(10 + 12) / 2 = 11
undergroundSystem.checkIn(10, "Leyton", 24);
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // 返回 11.00000
undergroundSystem.checkOut(10, "Waterloo", 38);  // 乘客 10 "Leyton" -> "Waterloo" ，用时 38-24 = 14
undergroundSystem.getAverageTime("Leyton", "Waterloo");    // 返回 12.00000 。有三个 "Leyton" -> "Waterloo" 的行程，(10 + 12 + 14) / 3 = 12

```
 **示例 2：** 

```

输入
["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
[[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]

输出
[null,null,null,5.00000,null,null,5.50000,null,null,6.66667]

解释
UndergroundSystem undergroundSystem = new UndergroundSystem();
undergroundSystem.checkIn(10, "Leyton", 3);
undergroundSystem.checkOut(10, "Paradise", 8); // 乘客 10 "Leyton" -> "Paradise" ，用时 8-3 = 5
undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 5.00000 ，(5) / 1 = 5
undergroundSystem.checkIn(5, "Leyton", 10);
undergroundSystem.checkOut(5, "Paradise", 16); // 乘客 5 "Leyton" -> "Paradise" ，用时 16-10 = 6
undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 5.50000 ，(5 + 6) / 2 = 5.5
undergroundSystem.checkIn(2, "Leyton", 21);
undergroundSystem.checkOut(2, "Paradise", 30); // 乘客 2 "Leyton" -> "Paradise" ，用时 30-21 = 9
undergroundSystem.getAverageTime("Leyton", "Paradise"); // 返回 6.66667 ，(5 + 6 + 9) / 3 = 6.66667

```
 

 **提示：** 
-  `1 <= id, t <= 10^6` 
-  `1 <= stationName.length, startStation.length, endStation.length <= 10` 次
- 所有字符串由大小写英文字母与数字组成
- 总共最多调用 `checkIn` 、 `checkOut` 和 `getAverageTime` 方法 `2 * 10^4` 
- 与标准答案误差在 `10^-5` 以内的结果都被视为正确结果
 
**标签**
`设计` `哈希表` `字符串` 


## 
```python

```
>
# 1397.找到所有好字符串
[https://leetcode-cn.com/problems/find-all-good-strings](https://leetcode-cn.com/problems/find-all-good-strings) 
## 原题
给你两个长度为 `n` 的字符串 `s1` 和 `s2` ，以及一个字符串 `evil` 。请你返回 **好字符串** 的数目。

 **好字符串** 的定义为：它的长度为 `n` ，字典序大于等于 `s1` ，字典序小于等于 `s2` ，且不包含 `evil` 为子字符串。

由于答案可能很大，请你返回答案对 10^9 + 7 取余的结果。

 

 **示例 1：** 

```
输入：n = 2, s1 = "aa", s2 = "da", evil = "b"
输出：51 
解释：总共有 25 个以 ';a'; 开头的好字符串："aa"，"ac"，"ad"，...，"az"。还有 25 个以 ';c'; 开头的好字符串："ca"，"cc"，"cd"，...，"cz"。最后，还有一个以 ';d'; 开头的好字符串："da"。

```
 **示例 2：** 

```
输入：n = 8, s1 = "leetcode", s2 = "leetgoes", evil = "leet"
输出：0 
解释：所有字典序大于等于 s1 且小于等于 s2 的字符串都以 evil 字符串 "leet" 开头。所以没有好字符串。

```
 **示例 3：** 

```
输入：n = 2, s1 = "gx", s2 = "gz", evil = "x"
输出：2

```
 

 **提示：** 
-  `s1.length == n` 
-  `s2.length == n` 
-  `s1 <= s2` 
-  `1 <= n <= 500` 
-  `1 <= evil.length <= 50` 
- 所有字符串都只包含小写英文字母。
 
**标签**
`字符串` `动态规划` `字符串匹配` 


## 
```python

```
>
# 1398.购买了产品 A 和产品 B 却没有购买产品 C 的顾客
[https://leetcode-cn.com/problems/customers-who-bought-products-a-and-b-but-not-c](https://leetcode-cn.com/problems/customers-who-bought-products-a-and-b-but-not-c) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1399.统计最大组的数目
[https://leetcode-cn.com/problems/count-largest-group](https://leetcode-cn.com/problems/count-largest-group) 
## 原题
给你一个整数 `n` 。请你先求出从 `1` 到 `n` 的每个整数 10 进制表示下的数位和（每一位上的数字相加），然后把数位和相等的数字放到同一个组中。

请你统计每个组中的数字数目，并返回数字数目并列最多的组有多少个。

 

 **示例 1：** 

```
输入：n = 13
输出：4
解释：总共有 9 个组，将 1 到 13 按数位求和后这些组分别是：
[1,10]，[2,11]，[3,12]，[4,13]，[5]，[6]，[7]，[8]，[9]。总共有 4 个组拥有的数字并列最多。

```
 **示例 2：** 

```
输入：n = 2
输出：2
解释：总共有 2 个大小为 1 的组 [1]，[2]。

```
 **示例 3：** 

```
输入：n = 15
输出：6

```
 **示例 4：** 

```
输入：n = 24
输出：5

```
 

 **提示：** 
-  `1 <= n <= 10^4` 
 
**标签**
`哈希表` `数学` 


## 
```python

```
>
# 1400.构造 K 个回文字符串
[https://leetcode-cn.com/problems/construct-k-palindrome-strings](https://leetcode-cn.com/problems/construct-k-palindrome-strings) 
## 原题
给你一个字符串 `s` 和一个整数 `k` 。请你用 `s` 字符串中 **所有字符** 构造 `k` 个非空 **回文串** 。

如果你可以用 `s` 中所有字符构造 `k` 个回文字符串，那么请你返回 **True** ，否则返回 **False** 。

 

 **示例 1：** 

```

输入：s = "annabelle", k = 2
输出：true
解释：可以用 s 中所有字符构造 2 个回文字符串。
一些可行的构造方案包括："anna" + "elble"，"anbna" + "elle"，"anellena" + "b"

```
 **示例 2：** 

```

输入：s = "leetcode", k = 3
输出：false
解释：无法用 s 中所有字符构造 3 个回文串。

```
 **示例 3：** 

```

输入：s = "true", k = 4
输出：true
解释：唯一可行的方案是让 s 中每个字符单独构成一个字符串。

```
 **示例 4：** 

```

输入：s = "yzyzyzyzyzyzyzy", k = 2
输出：true
解释：你只需要将所有的 z 放在一个字符串中，所有的 y 放在另一个字符串中。那么两个字符串都是回文串。

```
 **示例 5：** 

```

输入：s = "cr", k = 7
输出：false
解释：我们没有足够的字符去构造 7 个回文串。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s` 中所有字符都是小写英文字母。
-  `1 <= k <= 10^5` 
 
**标签**
`贪心` `哈希表` `字符串` `计数` 


## 
```python

```
>
