# 201.数字范围按位与
[https://leetcode-cn.com/problems/bitwise-and-of-numbers-range](https://leetcode-cn.com/problems/bitwise-and-of-numbers-range) 
## 原题
给你两个整数 `left` 和 `right` ，表示区间 `[left, right]` ，返回此区间内所有数字 **按位与** 的结果（包含 `left` 、 `right` 端点）。

 

 **示例 1：** 

```

输入：left = 5, right = 7
输出：4

```
 **示例 2：** 

```

输入：left = 0, right = 0
输出：0

```
 **示例 3：** 

```

输入：left = 1, right = 2147483647
输出：0

```
 

 **提示：** 
-  `0 <= left <= right <= 2^31 - 1` 
 
**标签**
`位运算` 


## 
```python

```
>
# 202.快乐数
[https://leetcode-cn.com/problems/happy-number](https://leetcode-cn.com/problems/happy-number) 
## 原题
编写一个算法来判断一个数 `n` 是不是快乐数。

 **「快乐数」** 定义为：
- 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
- 然后重复这个过程直到这个数变为 1，也可能是 **无限循环** 但始终变不到 1。
- 如果这个过程 **结果为** 1，那么这个数就是快乐数。
如果 `n` 是 *快乐数* 就返回 `true` ；不是，则返回 `false` 。

 

 **示例 1：** 

```

输入：n = 19
输出：true
解释：
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

```
 **示例 2：** 

```

输入：n = 2
输出：false

```
 

 **提示：** 
-  `1 <= n <= 2^31 - 1` 
 
**标签**
`哈希表` `数学` `双指针` 


## 
```python

```
>
# 203.移除链表元素
[https://leetcode-cn.com/problems/remove-linked-list-elements](https://leetcode-cn.com/problems/remove-linked-list-elements) 
## 原题
给你一个链表的头节点 `head` 和一个整数 `val` ，请你删除链表中所有满足 `Node.val == val` 的节点，并返回 **新的头节点** 。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/06/removelinked-list.jpg" style="width: 500px; height: 142px;" />
```

输入：head = [1,2,6,3,4,5,6], val = 6
输出：[1,2,3,4,5]

```
 **示例 2：** 

```

输入：head = [], val = 1
输出：[]

```
 **示例 3：** 

```

输入：head = [7,7,7,7], val = 7
输出：[]

```
 

 **提示：** 
- 列表中的节点数目在范围 `[0, 10^4]` 内
-  `1 <= Node.val <= 50` 
-  `0 <= val <= 50` 
 
**标签**
`递归` `链表` 


## 
```python

```
>
# 204.计数质数
[https://leetcode-cn.com/problems/count-primes](https://leetcode-cn.com/problems/count-primes) 
## 原题
给定整数 `n` ，返回 *所有小于非负整数 `n` 的质数的数量* 。

 

 **示例 1：** 

```

输入：n = 10
输出：4
解释：小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

```
 **示例 2：** 

```

输入：n = 0
输出：0

```
 **示例 3：** 

```

输入：n = 1
输出：0

```
 

 **提示：** 
-  `0 <= n <= 5 * 10^6` 
 
**标签**
`数组` `数学` `枚举` `数论` 


## 
```python

```
>
# 205.同构字符串
[https://leetcode-cn.com/problems/isomorphic-strings](https://leetcode-cn.com/problems/isomorphic-strings) 
## 原题
给定两个字符串 `s` 和 `t` ，判断它们是否是同构的。

如果 `s` 中的字符可以按某种映射关系替换得到 `t` ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。

 

 **示例 1:** 

```

输入：s = "egg", t = "add"
输出：true

```
 **示例 2：** 

```

输入：s = "foo", t = "bar"
输出：false
```
 **示例 3：** 

```

输入：s = "paper", t = "title"
输出：true
```
 

 **提示：** 

<meta charset="UTF-8" />
-  `1 <= s.length <= 5 * 10^4` 
-  `t.length == s.length` 
-  `s` 和 `t` 由任意有效的 ASCII 字符组成
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 206.反转链表
[https://leetcode-cn.com/problems/reverse-linked-list](https://leetcode-cn.com/problems/reverse-linked-list) 
## 原题
给你单链表的头节点 `head` ，请你反转链表，并返回反转后的链表。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" style="width: 542px; height: 222px;" />
```

输入：head = [1,2,3,4,5]
输出：[5,4,3,2,1]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" style="width: 182px; height: 222px;" />
```

输入：head = [1,2]
输出：[2,1]

```
 **示例 3：** 

```

输入：head = []
输出：[]

```
 

 **提示：** 
- 链表中节点的数目范围是 `[0, 5000]` 
-  `-5000 <= Node.val <= 5000` 
 

 **进阶：** 链表可以选用迭代或递归方式完成反转。你能否用两种方法解决这道题？
 
**标签**
`递归` `链表` 


## 
```python

```
>
# 207.课程表
[https://leetcode-cn.com/problems/course-schedule](https://leetcode-cn.com/problems/course-schedule) 
## 原题
你这个学期必须选修 `numCourses` 门课程，记为  `0`  到  `numCourses - 1` 。

在选修某些课程之前需要一些先修课程。 先修课程按数组  `prerequisites` 给出，其中  `prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]` ，表示如果要学习课程  `a<sub>i</sub>` 则 **必须** 先学习课程  `b<sub>i</sub>` <sub> </sub>。
- 例如，先修课程对  `[0, 1]` 表示：想要学习课程 `0` ，你需要先完成课程 `1` 。
请你判断是否可能完成所有课程的学习？如果可以，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
```
 **示例 2：** 

```

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
```
 

 **提示：** 
-  `1 <= numCourses <= 10^5` 
-  `0 <= prerequisites.length <= 5000` 
-  `prerequisites[i].length == 2` 
-  `0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses` 
-  `prerequisites[i]` 中的所有课程对 **互不相同** 
 
**标签**
`深度优先搜索` `广度优先搜索` `图` `拓扑排序` 


## 
```python

```
>
# 208.实现 Trie (前缀树)
[https://leetcode-cn.com/problems/implement-trie-prefix-tree](https://leetcode-cn.com/problems/implement-trie-prefix-tree) 
## 原题
 **<a href="https://baike.baidu.com/item/字典树/9825209?fr=aladdin" target="_blank">Trie</a>** （发音类似 "try"）或者说 **前缀树** 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。这一数据结构有相当多的应用情景，例如自动补完和拼写检查。

请你实现 Trie 类：
-  `Trie()` 初始化前缀树对象。
-  `void insert(String word)` 向前缀树中插入字符串 `word` 。
-  `boolean search(String word)` 如果字符串 `word` 在前缀树中，返回 `true` （即，在检索之前已经插入）；否则，返回 `false` 。
-  `boolean startsWith(String prefix)` 如果之前已经插入的字符串  `word` 的前缀之一为 `prefix` ，返回 `true` ；否则，返回 `false` 。
 

 **示例：** 

```

输入
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
输出
[null, null, true, false, true, null, true]

解释
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // 返回 True
trie.search("app");     // 返回 False
trie.startsWith("app"); // 返回 True
trie.insert("app");
trie.search("app");     // 返回 True

```
 

 **提示：** 
-  `1 <= word.length, prefix.length <= 2000` 
-  `word` 和 `prefix` 仅由小写英文字母组成
-  `insert` 、 `search` 和 `startsWith` 调用次数 **总计** 不超过 `3 * 10^4` 次
 
**标签**
`设计` `字典树` `哈希表` `字符串` 


## 
```python

```
>
# 209.长度最小的子数组
[https://leetcode-cn.com/problems/minimum-size-subarray-sum](https://leetcode-cn.com/problems/minimum-size-subarray-sum) 
## 原题
给定一个含有  `n` ** ** 个正整数的数组和一个正整数 `target` **。** 

找出该数组中满足其和 **** `≥ target` **** 的长度最小的 **连续子数组**   `[nums<sub>l</sub>, nums<sub>l+1</sub>, ..., nums<sub>r-1</sub>, nums<sub>r</sub>]` ，并返回其长度 **。** 如果不存在符合条件的子数组，返回 `0` 。

 

 **示例 1：** 

```

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。

```
 **示例 2：** 

```

输入：target = 4, nums = [1,4,4]
输出：1

```
 **示例 3：** 

```

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0

```
 

 **提示：** 
-  `1 <= target <= 10^9` 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^5` 
 

 **进阶：** 
- 如果你已经实现 `O(n)` 时间复杂度的解法, 请尝试设计一个 `O(n log(n))` 时间复杂度的解法。
 
**标签**
`数组` `二分查找` `前缀和` `滑动窗口` 


## 
```python

```
>
# 210.课程表 II
[https://leetcode-cn.com/problems/course-schedule-ii](https://leetcode-cn.com/problems/course-schedule-ii) 
## 原题
现在你总共有 `numCourses` 门课需要选，记为 `0` 到 `numCourses - 1` 。给你一个数组 `prerequisites` ，其中 `prerequisites[i] = [a<sub>i</sub>, b<sub>i</sub>]` ，表示在选修课程 `a<sub>i</sub>` 前 **必须** 先选修 `b<sub>i</sub>` 。
- 例如，想要学习课程 `0` ，你需要先完成课程 `1` ，我们用一个匹配来表示： `[0,1]` 。
返回你为了学完所有课程所安排的学习顺序。可能会有多个正确的顺序，你只要返回 **任意一种** 就可以了。如果不可能完成所有课程，返回 **一个空数组** 。

 

 **示例 1：** 

```

输入：numCourses = 2, prerequisites = [[1,0]]
输出：[0,1]
解释：总共有 2 门课程。要学习课程 1，你需要先完成课程 0。因此，正确的课程顺序为 [0,1] 。

```
 **示例 2：** 

```

输入：numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
输出：[0,2,1,3]
解释：总共有 4 门课程。要学习课程 3，你应该先完成课程 1 和课程 2。并且课程 1 和课程 2 都应该排在课程 0 之后。
因此，一个正确的课程顺序是 [0,1,2,3] 。另一个正确的排序是 [0,2,1,3] 。
```
 **示例 3：** 

```

输入：numCourses = 1, prerequisites = []
输出：[0]

```
 
 **提示：** 
-  `1 <= numCourses <= 2000` 
-  `0 <= prerequisites.length <= numCourses * (numCourses - 1)` 
-  `prerequisites[i].length == 2` 
-  `0 <= a<sub>i</sub>, b<sub>i</sub> < numCourses` 
-  `a<sub>i</sub> != b<sub>i</sub>` 
- 所有 `[a<sub>i</sub>, b<sub>i</sub>]` **互不相同** 
 
**标签**
`深度优先搜索` `广度优先搜索` `图` `拓扑排序` 


## 
```python

```
>
# 211.添加与搜索单词 - 数据结构设计
[https://leetcode-cn.com/problems/design-add-and-search-words-data-structure](https://leetcode-cn.com/problems/design-add-and-search-words-data-structure) 
## 原题
请你设计一个数据结构，支持 添加新单词 和 查找字符串是否与任何先前添加的字符串匹配 。

实现词典类 `WordDictionary` ：
-  `WordDictionary()` 初始化词典对象
-  `void addWord(word)` 将 `word` 添加到数据结构中，之后可以对它进行匹配
-  `bool search(word)` 如果数据结构中存在字符串与  `word` 匹配，则返回 `true` ；否则，返回  `false` 。 `word` 中可能包含一些 `'.'` ，每个  `.` 都可以表示任何一个字母。
 

 **示例：** 

```

输入：
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
输出：
[null,null,null,null,false,true,true,true]

解释：
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

```
 

 **提示：** 
-  `1 <= word.length <= 500` 
-  `addWord` 中的 `word` 由小写英文字母组成
-  `search` 中的 `word` 由 '.' 或小写英文字母组成
- 最多调用 `50000` 次 `addWord` 和 `search` 
 
**标签**
`深度优先搜索` `设计` `字典树` `字符串` 


## 
```python

```
>
# 212.单词搜索 II
[https://leetcode-cn.com/problems/word-search-ii](https://leetcode-cn.com/problems/word-search-ii) 
## 原题
给定一个 `m x n` 二维字符网格 `board` **** 和一个单词（字符串）列表 `words` ， *返回所有二维网格上的单词* 。

单词必须按照字母顺序，通过 **相邻的单元格** 内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search1.jpg" />
```

输入：board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
输出：["eat","oath"]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/07/search2.jpg" />
```

输入：board = [["a","b"],["c","d"]], words = ["abcb"]
输出：[]

```
 

 **提示：** 
-  `m == board.length` 
-  `n == board[i].length` 
-  `1 <= m, n <= 12` 
-  `board[i][j]` 是一个小写英文字母
-  `1 <= words.length <= 3 * 10^4` 
-  `1 <= words[i].length <= 10` 
-  `words[i]` 由小写英文字母组成
-  `words` 中的所有字符串互不相同
 
**标签**
`字典树` `数组` `字符串` `回溯` `矩阵` 


## 
```python

```
>
# 213.打家劫舍 II
[https://leetcode-cn.com/problems/house-robber-ii](https://leetcode-cn.com/problems/house-robber-ii) 
## 原题
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 **围成一圈** ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统， **如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警** 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 **在不触动警报装置的情况下** ，今晚能够偷窃到的最高金额。

 

 **示例 1：** 

```

输入：nums = [2,3,2]
输出：3
解释：你不能先偷窃 1 号房屋（金额 = 2），然后偷窃 3 号房屋（金额 = 2）, 因为他们是相邻的。

```
 **示例 2：** 

```

输入：nums = [1,2,3,1]
输出：4
解释：你可以先偷窃 1 号房屋（金额 = 1），然后偷窃 3 号房屋（金额 = 3）。
     偷窃到的最高金额 = 1 + 3 = 4 。
```
 **示例 3：** 

```

输入：nums = [1,2,3]
输出：3

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `0 <= nums[i] <= 1000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 214.最短回文串
[https://leetcode-cn.com/problems/shortest-palindrome](https://leetcode-cn.com/problems/shortest-palindrome) 
## 原题
给定一个字符串 ***s*** ，你可以通过在字符串前面添加字符将其转换为回文串。找到并返回可以用这种方式转换的最短回文串。

 

 **示例 1：** 

```

输入：s = "aacecaaa"
输出："aaacecaaa"

```
 **示例 2：** 

```

输入：s = "abcd"
输出："dcbabcd"

```
 

 **提示：** 
-  `0 <= s.length <= 5 * 10^4` 
-  `s` 仅由小写英文字母组成
 
**标签**
`字符串` `字符串匹配` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 215.数组中的第K个最大元素
[https://leetcode-cn.com/problems/kth-largest-element-in-an-array](https://leetcode-cn.com/problems/kth-largest-element-in-an-array) 
## 原题
给定整数数组 `nums` 和整数 `k` ，请返回数组中第 `**k**` 个最大的元素。

请注意，你需要找的是数组排序后的第 `k` 个最大的元素，而不是第 `k` 个不同的元素。

 

 **示例 1:** 

```

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

```
 **示例 2:** 

```

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
```
 

 **提示：** 
-  `1 <= k <= nums.length <= 10^4` 
-  `-10^4 <= nums[i] <= 10^4` 
 
**标签**
`数组` `分治` `快速选择` `排序` `堆（优先队列）` 


## 
```python

```
>
# 216.组合总和 III
[https://leetcode-cn.com/problems/combination-sum-iii](https://leetcode-cn.com/problems/combination-sum-iii) 
## 原题
找出所有相加之和为 ***n*** 的 ** *k* ** 个数的组合 ** *。* ** 组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

 **说明：** 
- 所有数字都是正整数。
- 解集不能包含重复的组合。 
 **示例 1:** 

```
输入: k = 3, n = 7
输出: [[1,2,4]]

```
 **示例 2:** 

```
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]

```
 
**标签**
`数组` `回溯` 


## 
```python

```
>
# 217.存在重复元素
[https://leetcode-cn.com/problems/contains-duplicate](https://leetcode-cn.com/problems/contains-duplicate) 
## 原题
给你一个整数数组 `nums` 。如果任一值在数组中出现 **至少两次** ，返回 `true` ；如果数组中每个元素互不相同，返回 `false` 。
 

 **示例 1：** 

```

输入：nums = [1,2,3,1]
输出：true
```
 **示例 2：** 

```

输入：nums = [1,2,3,4]
输出：false
```
 **示例 3：** 

```

输入：nums = [1,1,1,3,3,4,3,2,4,2]
输出：true
```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-10^9 <= nums[i] <= 10^9` 
 
**标签**
`数组` `哈希表` `排序` 


## 
```python

```
>
# 218.天际线问题
[https://leetcode-cn.com/problems/the-skyline-problem](https://leetcode-cn.com/problems/the-skyline-problem) 
## 原题
城市的 **天际线** 是从远处观看该城市中所有建筑物形成的轮廓的外部轮廓。给你所有建筑物的位置和高度，请返回 *由这些建筑物形成的 **天际线*** 。

每个建筑物的几何信息由数组 `buildings` 表示，其中三元组 `buildings[i] = [lefti, righti, heighti]` 表示：
-  `left<sub>i</sub>` 是第 `i` 座建筑物左边缘的 `x` 坐标。
-  `right<sub>i</sub>` 是第 `i` 座建筑物右边缘的 `x` 坐标。
-  `height<sub>i</sub>` 是第 `i` 座建筑物的高度。
你可以假设所有的建筑都是完美的长方形，在高度为 `0` 的绝对平坦的表面上。

 **天际线** 应该表示为由 “关键点” 组成的列表，格式 `[[x<sub>1</sub>,y<sub>1</sub>],[x<sub>2</sub>,y<sub>2</sub>],...]` ，并按 **x 坐标** 进行 **排序** 。 **关键点是水平线段的左端点** 。列表中最后一个点是最右侧建筑物的终点， `y` 坐标始终为 `0` ，仅用于标记天际线的终点。此外，任何两个相邻建筑物之间的地面都应被视为天际线轮廓的一部分。

 **注意：** 输出天际线中不得有连续的相同高度的水平线。例如 `[...[2 3], [4 5], [7 5], [11 5], [12 7]...]` 是不正确的答案；三条高度为 5 的线应该在最终输出中合并为一个： `[...[2 3], [4 5], [12 7], ...]` 

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/merged.jpg" style="height: 331px; width: 800px;" />
```

输入：buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
输出：[[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
解释：
图 A 显示输入的所有建筑物的位置和高度，
图 B 显示由这些建筑物形成的天际线。图 B 中的红点表示输出列表中的关键点。
```
 **示例 2：** 

```

输入：buildings = [[0,2,3],[2,5,3]]
输出：[[0,3],[5,0]]

```
 

 **提示：** 
-  `1 <= buildings.length <= 10^4` 
-  `0 <= left<sub>i</sub> < right<sub>i</sub> <= 2^31 - 1` 
-  `1 <= height<sub>i</sub> <= 2^31 - 1` 
-  `buildings` 按 `left<sub>i</sub>` 非递减排序
 
**标签**
`树状数组` `线段树` `数组` `分治` `有序集合` `扫描线` `堆（优先队列）` 


## 
```python

```
>
# 219.存在重复元素 II
[https://leetcode-cn.com/problems/contains-duplicate-ii](https://leetcode-cn.com/problems/contains-duplicate-ii) 
## 原题
给你一个整数数组 `nums` 和一个整数 `k` ，判断数组中是否存在两个 **不同的索引**  `i` 和 `j` ，满足 `nums[i] == nums[j]` 且 `abs(i - j) <= k` 。如果存在，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：nums = [1,2,3,1], k = 3
输出：true
```
 **示例 2：** 

```

输入：nums = [1,0,1,1], k = 1
输出：true
```
 **示例 3：** 

```

输入：nums = [1,2,3,1,2,3], k = 2
输出：false
```
 

 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-10^9 <= nums[i] <= 10^9` 
-  `0 <= k <= 10^5` 
 
**标签**
`数组` `哈希表` `滑动窗口` 


## 
```python

```
>
# 220.存在重复元素 III
[https://leetcode-cn.com/problems/contains-duplicate-iii](https://leetcode-cn.com/problems/contains-duplicate-iii) 
## 原题
给你一个整数数组 `nums` 和两个整数  `k` 和 `t` 。请你判断是否存在 <b>两个不同下标</b> `i` 和 `j` ，使得  `abs(nums[i] - nums[j]) <= t` ，同时又满足 `abs(i - j) <= k` 。

如果存在则返回 `true` ，不存在返回 `false` 。

 

 **示例 1：** 

```

输入：nums = [1,2,3,1], k = 3, t = 0
输出：true
```
 **示例 2：** 

```

输入：nums = [1,0,1,1], k = 1, t = 2
输出：true
```
 **示例 3：** 

```

输入：nums = [1,5,9,1,5,9], k = 2, t = 3
输出：false
```
 

 **提示：** 
-  `0 <= nums.length <= 2 * 10^4` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
-  `0 <= k <= 10^4` 
-  `0 <= t <= 2^31 - 1` 
 
**标签**
`数组` `桶排序` `有序集合` `排序` `滑动窗口` 


## 
```python

```
>
# 221.最大正方形
[https://leetcode-cn.com/problems/maximal-square](https://leetcode-cn.com/problems/maximal-square) 
## 原题
在一个由 `'0'` 和 `'1'` 组成的二维矩阵内，找到只包含 `'1'` 的最大正方形，并返回其面积。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max1grid.jpg" style="width: 400px; height: 319px;" />
```

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/max2grid.jpg" style="width: 165px; height: 165px;" />
```

输入：matrix = [["0","1"],["1","0"]]
输出：1

```
 **示例 3：** 

```

输入：matrix = [["0"]]
输出：0

```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m, n <= 300` 
-  `matrix[i][j]` 为 `'0'` 或 `'1'` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 222.完全二叉树的节点个数
[https://leetcode-cn.com/problems/count-complete-tree-nodes](https://leetcode-cn.com/problems/count-complete-tree-nodes) 
## 原题
给你一棵 **完全二叉树** 的根节点 `root` ，求出该树的节点个数。

<a href="https://baike.baidu.com/item/%E5%AE%8C%E5%85%A8%E4%BA%8C%E5%8F%89%E6%A0%91/7773232?fr=aladdin">完全二叉树</a> 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 `h` 层，则该层包含 `1~ 2^h`  个节点。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/14/complete.jpg" style="width: 372px; height: 302px;" />
```

输入：root = [1,2,3,4,5,6]
输出：6

```
 **示例 2：** 

```

输入：root = []
输出：0

```
 **示例 3：** 

```

输入：root = [1]
输出：1

```
 

 **提示：** 
- 树中节点的数目范围是 `[0, 5 * 10^4]` 
-  `0 <= Node.val <= 5 * 10^4` 
- 题目数据保证输入的树是 **完全二叉树** 
 

 **进阶：** 遍历树来统计节点是一种时间复杂度为 `O(n)` 的简单解决方案。你可以设计一个更快的算法吗？

 
**标签**
`树` `深度优先搜索` `二分查找` `二叉树` 


## 
```python

```
>
# 223.矩形面积
[https://leetcode-cn.com/problems/rectangle-area](https://leetcode-cn.com/problems/rectangle-area) 
## 原题
给你 **二维** 平面上两个 **由直线构成且边与坐标轴平行/垂直** 的矩形，请你计算并返回两个矩形覆盖的总面积。

每个矩形由其 **左下** 顶点和 **右上** 顶点坐标表示：
	<li class="MachineTrans-lang-zh-CN">第一个矩形由其左下顶点 `(ax1, ay1)` 和右上顶点 `(ax2, ay2)` 定义。
	<li class="MachineTrans-lang-zh-CN">第二个矩形由其左下顶点 `(bx1, by1)` 和右上顶点 `(bx2, by2)` 定义。
 

 **示例 1：** 
<img alt="Rectangle Area" src="https://assets.leetcode.com/uploads/2021/05/08/rectangle-plane.png" style="width: 700px; height: 365px;" />
```

输入：ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
输出：45

```
 **示例 2：** 

```

输入：ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
输出：16

```
 

 **提示：** 
-  `-10^4 <= ax1, ay1, ax2, ay2, bx1, by1, bx2, by2 <= 10^4` 
 
**标签**
`几何` `数学` 


## 
```python

```
>
# 224.基本计算器
[https://leetcode-cn.com/problems/basic-calculator](https://leetcode-cn.com/problems/basic-calculator) 
## 原题
给你一个字符串表达式 `s` ，请你实现一个基本计算器来计算并返回它的值。

注意:不允许使用任何将字符串作为数学表达式计算的内置函数，比如 `eval()` 。

 

 **示例 1：** 

```

输入：s = "1 + 1"
输出：2

```
 **示例 2：** 

```

输入：s = " 2-1 + 2 "
输出：3

```
 **示例 3：** 

```

输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

```
 

 **提示：** 
-  `1 <= s.length <= 3 * 10^5` 
-  `s` 由数字、 `'+'` 、 `'-'` 、 `'('` 、 `')'` 、和 `' '` 组成
-  `s` 表示一个有效的表达式
- <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'+'</span></span></font></font> 不能用作一元运算(例如， <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">"+1"</span></span></font></font> 和 `"+(2 + 3)"` 无效)
- <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'-'</span></span></font></font> 可以用作一元运算(即 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">"-1"</span></span></font></font> 和 `"-(2 + 3)"` 是有效的)
- 输入中不存在两个连续的操作符
- 每个数字和运行的计算将适合于一个有符号的 32位 整数
 
**标签**
`栈` `递归` `数学` `字符串` 


## 
```python

```
>
# 225.用队列实现栈
[https://leetcode-cn.com/problems/implement-stack-using-queues](https://leetcode-cn.com/problems/implement-stack-using-queues) 
## 原题
请你仅使用两个队列实现一个后入先出（LIFO）的栈，并支持普通栈的全部四种操作（ `push` 、 `top` 、 `pop` 和 `empty` ）。

实现 `MyStack` 类：
-  `void push(int x)` 将元素 x 压入栈顶。
-  `int pop()` 移除并返回栈顶元素。
-  `int top()` 返回栈顶元素。
-  `boolean empty()` 如果栈是空的，返回 `true` ；否则，返回 `false` 。
 

 **注意：** 
- 你只能使用队列的基本操作 —— 也就是 `push to back` 、 `peek/pop from front` 、 `size` 和 `is empty` 这些操作。
- 你所使用的语言也许不支持队列。 你可以使用 list （列表）或者 deque（双端队列）来模拟一个队列 , 只要是标准的队列操作即可。
 

 **示例：** 

```

输入：
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 2, 2, false]

解释：
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // 返回 2
myStack.pop(); // 返回 2
myStack.empty(); // 返回 False

```
 

 **提示：** 
-  `1 <= x <= 9` 
- 最多调用 `100` 次 `push` 、 `pop` 、 `top` 和 `empty` 
- 每次调用 `pop` 和 `top` 都保证栈不为空
 

 **进阶：** 你能否仅用一个队列来实现栈。

 
**标签**
`栈` `设计` `队列` 


## 
```python

```
>
# 226.翻转二叉树
[https://leetcode-cn.com/problems/invert-binary-tree](https://leetcode-cn.com/problems/invert-binary-tree) 
## 原题
给你一棵二叉树的根节点 `root` ，翻转这棵二叉树，并返回其根节点。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg" style="height: 165px; width: 500px;" />

```

输入：root = [4,2,7,1,3,6,9]
输出：[4,7,2,9,6,3,1]

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg" style="width: 500px; height: 120px;" />

```

输入：root = [2,1,3]
输出：[2,3,1]

```
 **示例 3：** 

```

输入：root = []
输出：[]

```
 

 **提示：** 
- 树中节点数目范围在 `[0, 100]` 内
-  `-100 <= Node.val <= 100` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 227.基本计算器 II
[https://leetcode-cn.com/problems/basic-calculator-ii](https://leetcode-cn.com/problems/basic-calculator-ii) 
## 原题
给你一个字符串表达式 `s` ，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分。
 

 **示例 1：** 

```

输入：s = "3+2*2"
输出：7

```
 **示例 2：** 

```

输入：s = " 3/2 "
输出：1

```
 **示例 3：** 

```

输入：s = " 3+5 / 2 "
输出：5

```
 

 **提示：** 
-  `1 <= s.length <= 3 * 10^5` 
-  `s` 由整数和算符 `('+', '-', '*', '/')` 组成，中间由一些空格隔开
-  `s` 表示一个 **有效表达式** 
- 表达式中的所有整数都是非负整数，且在范围 `[0, 2^31 - 1]` 内
- 题目数据保证答案是一个 **32-bit 整数** 
 
**标签**
`栈` `数学` `字符串` 


## 
```python

```
>
# 228.汇总区间
[https://leetcode-cn.com/problems/summary-ranges](https://leetcode-cn.com/problems/summary-ranges) 
## 原题
给定一个 **无重复元素** 的 **有序** 整数数组 `nums` 。

返回 ***恰好覆盖数组中所有数字** 的 **最小有序** 区间范围列表* 。也就是说， `nums` 的每个元素都恰好被某个区间范围所覆盖，并且不存在属于某个范围但不属于 `nums` 的数字 `x` 。

列表中的每个区间范围 `[a,b]` 应该按如下格式输出：
-  `"a->b"` ，如果 `a != b` 
-  `"a"` ，如果 `a == b` 
 

 **示例 1：** 

```

输入：nums = [0,1,2,4,5,7]
输出：["0->2","4->5","7"]
解释：区间范围是：
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"

```
 **示例 2：** 

```

输入：nums = [0,2,3,4,6,8,9]
输出：["0","2->4","6","8->9"]
解释：区间范围是：
[0,0] --> "0"
[2,4] --> "2->4"
[6,6] --> "6"
[8,9] --> "8->9"

```
 

 **提示：** 
-  `0 <= nums.length <= 20` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
-  `nums` 中的所有值都 **互不相同** 
-  `nums` 按升序排列
 
**标签**
`数组` 


## 
```python

```
>
# 229.求众数 II
[https://leetcode-cn.com/problems/majority-element-ii](https://leetcode-cn.com/problems/majority-element-ii) 
## 原题
给定一个大小为 *n* 的整数数组，找出其中所有出现超过 `⌊ n/3 ⌋` 次的元素。

 

 

 **示例 1：** 

```

输入：[3,2,3]
输出：[3]
```
 **示例 2：** 

```

输入：nums = [1]
输出：[1]

```
 **示例 3：** 

```

输入：[1,1,1,3,3,2,2,2]
输出：[1,2]
```
 

 **提示：** 
-  `1 <= nums.length <= 5 * 10^4` 
-  `-10^9 <= nums[i] <= 10^9` 
 

 **进阶：** 尝试设计时间复杂度为 O(n)、空间复杂度为 O(1)的算法解决此问题。

 
**标签**
`数组` `哈希表` `计数` `排序` 


## 
```python

```
>
# 230.二叉搜索树中第K小的元素
[https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst](https://leetcode-cn.com/problems/kth-smallest-element-in-a-bst) 
## 原题
给定一个二叉搜索树的根节点 `root` ，和一个整数 `k` ，请你设计一个算法查找其中第  `k` ** ** 个最小元素（从 1 开始计数）。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree1.jpg" style="width: 212px; height: 301px;" />
```

输入：root = [3,1,4,null,2], k = 1
输出：1

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/28/kthtree2.jpg" style="width: 382px; height: 302px;" />
```

输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3

```
 

 

 **提示：** 
- 树中的节点数为 `n` 。
-  `1 <= k <= n <= 10^4` 
-  `0 <= Node.val <= 10^4` 
 

 **进阶：** 如果二叉搜索树经常被修改（插入/删除操作）并且你需要频繁地查找第 `k` 小的值，你将如何优化算法？

 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 231.2 的幂
[https://leetcode-cn.com/problems/power-of-two](https://leetcode-cn.com/problems/power-of-two) 
## 原题
给你一个整数 `n` ，请你判断该整数是否是 2 的幂次方。如果是，返回 `true` ；否则，返回 `false` 。

如果存在一个整数 `x` 使得  `n == 2^x` ，则认为 `n` 是 2 的幂次方。

 

 **示例 1：** 

```

输入：n = 1
输出：true
解释：2^0 = 1

```
 **示例 2：** 

```

输入：n = 16
输出：true
解释：2^4 = 16

```
 **示例 3：** 

```

输入：n = 3
输出：false

```
 **示例 4：** 

```

输入：n = 4
输出：true

```
 **示例 5：** 

```

输入：n = 5
输出：false

```
 

 **提示：** 
-  `-2^31 <= n <= 2^31 - 1` 
 

 **进阶：** 你能够不使用循环/递归解决此问题吗？

 
**标签**
`位运算` `递归` `数学` 


## 
```python

```
>
# 232.用栈实现队列
[https://leetcode-cn.com/problems/implement-queue-using-stacks](https://leetcode-cn.com/problems/implement-queue-using-stacks) 
## 原题
请你仅使用两个栈实现先入先出队列。队列应当支持一般队列支持的所有操作（ `push` 、 `pop` 、 `peek` 、 `empty` ）：

实现 `MyQueue` 类：
-  `void push(int x)` 将元素 x 推到队列的末尾
-  `int pop()` 从队列的开头移除并返回元素
-  `int peek()` 返回队列开头的元素
-  `boolean empty()` 如果队列为空，返回 `true` ；否则，返回 `false` 
 **说明：** 
- 你 **只能** 使用标准的栈操作 —— 也就是只有 `push to top` , `peek/pop from top` , `size` , 和 `is empty` 操作是合法的。
- 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准的栈操作即可。
 

 **示例 1：** 

```

输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false

```
 

 **提示：** 
-  `1 <= x <= 9` 
- 最多调用 `100` 次 `push` 、 `pop` 、 `peek` 和 `empty` 
- 假设所有操作都是有效的 （例如，一个空的队列不会调用 `pop` 或者 `peek` 操作）
 

 **进阶：** 
- 你能否实现每个操作均摊时间复杂度为 `O(1)` 的队列？换句话说，执行 `n` 个操作的总时间复杂度为 `O(n)` ，即使其中一个操作可能花费较长时间。
 
**标签**
`栈` `设计` `队列` 


## 
```python

```
>
# 233.数字 1 的个数
[https://leetcode-cn.com/problems/number-of-digit-one](https://leetcode-cn.com/problems/number-of-digit-one) 
## 原题
给定一个整数 `n` ，计算所有小于等于 `n` 的非负整数中数字 `1` 出现的个数。

 

 **示例 1：** 

```

输入：n = 13
输出：6

```
 **示例 2：** 

```

输入：n = 0
输出：0

```
 

 **提示：** 
-  `0 <= n <= 10^9` 
 
**标签**
`递归` `数学` `动态规划` 


## 
```python

```
>
# 234.回文链表
[https://leetcode-cn.com/problems/palindrome-linked-list](https://leetcode-cn.com/problems/palindrome-linked-list) 
## 原题
给你一个单链表的头节点 `head` ，请你判断该链表是否为回文链表。如果是，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal1linked-list.jpg" style="width: 422px; height: 62px;" />
```

输入：head = [1,2,2,1]
输出：true

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/03/pal2linked-list.jpg" style="width: 182px; height: 62px;" />
```

输入：head = [1,2]
输出：false

```
 

 **提示：** 
- 链表中节点数目在范围 `[1, 10^5]` 内
-  `0 <= Node.val <= 9` 
 

 **进阶：** 你能否用 `O(n)` 时间复杂度和 `O(1)` 空间复杂度解决此题？

 
**标签**
`栈` `递归` `链表` `双指针` 


## 
```python

```
>
# 235.二叉搜索树的最近公共祖先
[https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree) 
## 原题
给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。

<a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank">百度百科</a>中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（ **一个节点也可以是它自己的祖先** ）。”

例如，给定如下二叉搜索树:  root = [6,2,8,0,4,7,9,null,null,3,5]

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/binarysearchtree_improved.png" style="height: 190px; width: 200px;">

 

 **示例 1:** 

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
输出: 6 
解释: 节点 2 和节点 8 的最近公共祖先是 6。

```
 **示例 2:** 

```
输入: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
输出: 2
解释: 节点 2 和节点 4 的最近公共祖先是 2, 因为根据定义最近公共祖先节点可以为节点本身。
```
 

 **说明:** 
- 所有节点的值都是唯一的。
- p、q 为不同节点且均存在于给定的二叉搜索树中。
 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 236.二叉树的最近公共祖先
[https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree) 
## 原题
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

<a href="https://baike.baidu.com/item/%E6%9C%80%E8%BF%91%E5%85%AC%E5%85%B1%E7%A5%96%E5%85%88/8918834?fr=aladdin" target="_blank">百度百科</a>中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（ **一个节点也可以是它自己的祖先** ）。”

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
```

输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出：3
解释：节点 5 和节点 1 的最近公共祖先是节点 3 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2018/12/14/binarytree.png" style="width: 200px; height: 190px;" />
```

输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出：5
解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。

```
 **示例 3：** 

```

输入：root = [1,2], p = 1, q = 2
输出：1

```
 

 **提示：** 
- 树中节点数目在范围 `[2, 10^5]` 内。
-  `-10^9 <= Node.val <= 10^9` 
- 所有 `Node.val` `互不相同` 。
-  `p != q` 
-  `p` 和 `q` 均存在于给定的二叉树中。
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 237.删除链表中的节点
[https://leetcode-cn.com/problems/delete-node-in-a-linked-list](https://leetcode-cn.com/problems/delete-node-in-a-linked-list) 
## 原题
请编写一个函数，用于 **删除单链表中某个特定节点** 。在设计函数时需要注意，你无法访问链表的头节点 `head` ，只能直接访问 **要被删除的节点** 。

题目数据保证需要删除的节点 **不是末尾节点** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/node1.jpg" style="width: 450px; height: 322px;" />
```

输入：head = [4,5,1,9], node = 5
输出：[4,1,9]
解释：指定链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/01/node2.jpg" style="width: 450px; height: 354px;" />
```

输入：head = [4,5,1,9], node = 1
输出：[4,5,9]
解释：指定链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9
```
 **示例 3：** 

```

输入：head = [1,2,3,4], node = 3
输出：[1,2,4]

```
 **示例 4：** 

```

输入：head = [0,1], node = 0
输出：[1]

```
 **示例 5：** 

```

输入：head = [-3,5,-99], node = -3
输出：[5,-99]

```
 

 **提示：** 
- 链表中节点的数目范围是 `[2, 1000]` 
-  `-1000 <= Node.val <= 1000` 
- 链表中每个节点的值都是唯一的
- 需要删除的节点 `node` 是 **链表中的一个有效节点** ，且 **不是末尾节点** 
 
**标签**
`链表` 


## 
```python

```
>
# 238.除自身以外数组的乘积
[https://leetcode-cn.com/problems/product-of-array-except-self](https://leetcode-cn.com/problems/product-of-array-except-self) 
## 原题
给你一个整数数组 `nums` ，返回 *数组 `answer` ，其中 `answer[i]` 等于 `nums` 中除 `nums[i]` 之外其余各元素的乘积* 。

题目数据 **保证** 数组 `nums` 之中任意元素的全部前缀元素和后缀的乘积都在 **32 位** 整数范围内。

请 **不要使用除法，** 且在 `O( *n* )` 时间复杂度内完成此题。

 

 **示例 1:** 

```

输入: nums = [1,2,3,4]
输出: [24,12,8,6]

```
 **示例 2:** 

```

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]

```
 

 **提示：** 
-  `2 <= nums.length <= 10^5` 
-  `-30 <= nums[i] <= 30` 
-  **保证** 数组 `nums` 之中任意元素的全部前缀元素和后缀的乘积都在 **32 位** 整数范围内
 

 **进阶：** 你可以在 `O(1)` 的额外空间复杂度内完成这个题目吗？（ 出于对空间复杂度分析的目的，输出数组 **不被视为** 额外空间。）

 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 239.滑动窗口最大值
[https://leetcode-cn.com/problems/sliding-window-maximum](https://leetcode-cn.com/problems/sliding-window-maximum) 
## 原题
给你一个整数数组 `nums` ，有一个大小为 `k` 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 `k` 个数字。滑动窗口每次只向右移动一位。

返回 *滑动窗口中的最大值* 。

 

 **示例 1：** 

```

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

```
 **示例 2：** 

```

输入：nums = [1], k = 1
输出：[1]

```
 

<b>提示：</b>
-  `1 <= nums.length <= 10^5` 
-  `-10^4 <= nums[i] <= 10^4` 
-  `1 <= k <= nums.length` 
 
**标签**
`队列` `数组` `滑动窗口` `单调队列` `堆（优先队列）` 


## 
```python

```
>
# 240.搜索二维矩阵 II
[https://leetcode-cn.com/problems/search-a-2d-matrix-ii](https://leetcode-cn.com/problems/search-a-2d-matrix-ii) 
## 原题
编写一个高效的算法来搜索 ` *m* x *n* ` 矩阵 `matrix` 中的一个目标值 `target` 。该矩阵具有以下特性：
- 每行的元素从左到右升序排列。
- 每列的元素从上到下升序排列。
 

<b>示例 1：</b>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/searchgrid2.jpg" />
```

输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
输出：true

```
<b>示例 2：</b>
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/searchgrid.jpg" />
```

输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
输出：false

```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= n, m <= 300` 
-  `-10^9 <= matrix[i][j] <= 10^9` 
- 每行的所有元素从左到右升序排列
- 每列的所有元素从上到下升序排列
-  `-10^9 <= target <= 10^9` 
 
**标签**
`数组` `二分查找` `分治` `矩阵` 


## 
```python

```
>
# 241.为运算表达式设计优先级
[https://leetcode-cn.com/problems/different-ways-to-add-parentheses](https://leetcode-cn.com/problems/different-ways-to-add-parentheses) 
## 原题
给你一个由数字和运算符组成的字符串 `expression` ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 **按任意顺序** 返回答案。

 

 **示例 1：** 

```

输入：expression = "2-1-1"
输出：[0,2]
解释：
((2-1)-1) = 0 
(2-(1-1)) = 2

```
 **示例 2：** 

```

输入：expression = "2*3-4*5"
输出：[-34,-14,-10,-10,10]
解释：
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10

```
 

 **提示：** 
-  `1 <= expression.length <= 20` 
-  `expression` 由数字和算符 `'+'` 、 `'-'` 和 `'*'` 组成。
- 输入表达式中的所有整数值在范围 `[0, 99]` 
 
**标签**
`递归` `记忆化搜索` `数学` `字符串` `动态规划` 


## 
```python

```
>
# 242.有效的字母异位词
[https://leetcode-cn.com/problems/valid-anagram](https://leetcode-cn.com/problems/valid-anagram) 
## 原题
给定两个字符串 ` *s* ` 和 ` *t* ` ，编写一个函数来判断 ` *t* ` 是否是 ` *s* ` 的字母异位词。

 **注意：** 若  ` *s* ` 和 ` *t* ` * * 中每个字符出现的次数都相同，则称  ` *s* ` 和 ` *t* ` * * 互为字母异位词。

 

 **示例 1:** 

```

输入: s = "anagram", t = "nagaram"
输出: true

```
 **示例 2:** 

```

输入: s = "rat", t = "car"
输出: false
```
 

 **提示:** 
-  `1 <= s.length, t.length <= 5 * 10^4` 
-  `s` 和 `t`  仅包含小写字母
 

 **进阶: ** 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

 
**标签**
`哈希表` `字符串` `排序` 


## 
```python

```
>
# 243.最短单词距离
[https://leetcode-cn.com/problems/shortest-word-distance](https://leetcode-cn.com/problems/shortest-word-distance) 
## 原题

 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 244.最短单词距离 II
[https://leetcode-cn.com/problems/shortest-word-distance-ii](https://leetcode-cn.com/problems/shortest-word-distance-ii) 
## 原题

 
**标签**
`设计` `数组` `哈希表` `双指针` `字符串` 


## 
```python

```
>
# 245.最短单词距离 III
[https://leetcode-cn.com/problems/shortest-word-distance-iii](https://leetcode-cn.com/problems/shortest-word-distance-iii) 
## 原题

 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 246.中心对称数
[https://leetcode-cn.com/problems/strobogrammatic-number](https://leetcode-cn.com/problems/strobogrammatic-number) 
## 原题

 
**标签**
`哈希表` `双指针` `字符串` 


## 
```python

```
>
# 247.中心对称数 II
[https://leetcode-cn.com/problems/strobogrammatic-number-ii](https://leetcode-cn.com/problems/strobogrammatic-number-ii) 
## 原题

 
**标签**
`递归` `数组` `字符串` 


## 
```python

```
>
# 248.中心对称数 III
[https://leetcode-cn.com/problems/strobogrammatic-number-iii](https://leetcode-cn.com/problems/strobogrammatic-number-iii) 
## 原题

 
**标签**
`递归` `数组` `字符串` 


## 
```python

```
>
# 249.移位字符串分组
[https://leetcode-cn.com/problems/group-shifted-strings](https://leetcode-cn.com/problems/group-shifted-strings) 
## 原题

 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 250.统计同值子树
[https://leetcode-cn.com/problems/count-univalue-subtrees](https://leetcode-cn.com/problems/count-univalue-subtrees) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 251.展开二维向量
[https://leetcode-cn.com/problems/flatten-2d-vector](https://leetcode-cn.com/problems/flatten-2d-vector) 
## 原题

 
**标签**
`设计` `数组` `双指针` `迭代器` 


## 
```python

```
>
# 252.会议室
[https://leetcode-cn.com/problems/meeting-rooms](https://leetcode-cn.com/problems/meeting-rooms) 
## 原题

 
**标签**
`数组` `排序` 


## 
```python

```
>
# 253.会议室 II
[https://leetcode-cn.com/problems/meeting-rooms-ii](https://leetcode-cn.com/problems/meeting-rooms-ii) 
## 原题

 
**标签**
`贪心` `数组` `双指针` `排序` `堆（优先队列）` 


## 
```python

```
>
# 254.因子的组合
[https://leetcode-cn.com/problems/factor-combinations](https://leetcode-cn.com/problems/factor-combinations) 
## 原题

 
**标签**
`数组` `回溯` 


## 
```python

```
>
# 255.验证前序遍历序列二叉搜索树
[https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree](https://leetcode-cn.com/problems/verify-preorder-sequence-in-binary-search-tree) 
## 原题

 
**标签**
`栈` `树` `二叉搜索树` `递归` `二叉树` `单调栈` 


## 
```python

```
>
# 256.粉刷房子
[https://leetcode-cn.com/problems/paint-house](https://leetcode-cn.com/problems/paint-house) 
## 原题

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 257.二叉树的所有路径
[https://leetcode-cn.com/problems/binary-tree-paths](https://leetcode-cn.com/problems/binary-tree-paths) 
## 原题
给你一个二叉树的根节点 `root` ，按 **任意顺序** ，返回所有从根节点到叶子节点的路径。

 **叶子节点** 是指没有子节点的节点。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/12/paths-tree.jpg" style="width: 207px; height: 293px;" />
```

输入：root = [1,2,3,null,5]
输出：["1->2->5","1->3"]

```
 **示例 2：** 

```

输入：root = [1]
输出：["1"]

```
 

 **提示：** 
- 树中节点的数目在范围 `[1, 100]` 内
-  `-100 <= Node.val <= 100` 
 
**标签**
`树` `深度优先搜索` `字符串` `回溯` `二叉树` 


## 
```python

```
>
# 258.各位相加
[https://leetcode-cn.com/problems/add-digits](https://leetcode-cn.com/problems/add-digits) 
## 原题
给定一个非负整数 `num` ，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

 

 **示例 1:** 

```

输入: num = 38
输出: 2 
解释: 各位相加的过程为：
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2
由于 2 是一位数，所以返回 2。

```
 **示例 1:** 

```

输入: num = 0
输出: 0
```
 

 **提示：** 
-  `0 <= num <= 2^31 - 1` 
 

 **进阶：** 你可以不使用循环或者递归，在 `O(1)` 时间复杂度内解决这个问题吗？

 
**标签**
`数学` `数论` `模拟` 


## 
```python

```
>
# 259.较小的三数之和
[https://leetcode-cn.com/problems/3sum-smaller](https://leetcode-cn.com/problems/3sum-smaller) 
## 原题

 
**标签**
`数组` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 260.只出现一次的数字 III
[https://leetcode-cn.com/problems/single-number-iii](https://leetcode-cn.com/problems/single-number-iii) 
## 原题
给定一个整数数组  `nums` ，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 **任意顺序** 返回答案。

 

 **进阶：** 你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

 

 **示例 1：** 

```

输入：nums = [1,2,1,3,2,5]
输出：[3,5]
解释：[5, 3] 也是有效的答案。

```
 **示例 2：** 

```

输入：nums = [-1,0]
输出：[-1,0]

```
 **示例 3：** 

```

输入：nums = [0,1]
输出：[1,0]

```
 **提示：** 
-  `2 <= nums.length <= 3 * 10^4` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
- 除两个只出现一次的整数外， `nums` 中的其他数字都出现两次
 
**标签**
`位运算` `数组` 


## 
```python

```
>
# 261.以图判树
[https://leetcode-cn.com/problems/graph-valid-tree](https://leetcode-cn.com/problems/graph-valid-tree) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `图` 


## 
```python

```
>
# 262.行程和用户
[https://leetcode-cn.com/problems/trips-and-users](https://leetcode-cn.com/problems/trips-and-users) 
## 原题
表： `Trips` 
```

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| client_id   | int      |
| driver_id   | int      |
| city_id     | int      |
| status      | enum     |
| request_at  | date     |     
+-------------+----------+
id 是这张表的主键。
这张表中存所有出租车的行程信息。每段行程有唯一 id ，其中 client_id 和 driver_id 是 Users 表中 users_id 的外键。
status 是一个表示行程状态的枚举类型，枚举成员为(‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’) 。

```
 
表： `Users` 
```

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| users_id    | int      |
| banned      | enum     |
| role        | enum     |
+-------------+----------+
users_id 是这张表的主键。
这张表中存所有用户，每个用户都有一个唯一的 users_id ，role 是一个表示用户身份的枚举类型，枚举成员为 (‘client’, ‘driver’, ‘partner’) 。
banned 是一个表示用户是否被禁止的枚举类型，枚举成员为 (‘Yes’, ‘No’) 。

```
 

 **取消率** 的计算方式如下：(被司机或乘客取消的非禁止用户生成的订单数量) / (非禁止用户生成的订单总数)。

写一段 SQL 语句查出 `"2013-10-01"` **** 至 `"2013-10-03"` **** 期间非禁止用户（ **乘客和司机都必须未被禁止** ）的取消率。非禁止用户即 banned 为 No 的用户，禁止用户即 banned 为 Yes 的用户。

返回结果表中的数据可以按任意顺序组织。其中取消率 `Cancellation Rate` 需要四舍五入保留 **两位小数** 。

查询结果格式如下例所示。

 

 **示例：** 

```

输入： 
Trips 表：
+----+-----------+-----------+---------+---------------------+------------+
| id | client_id | driver_id | city_id | status              | request_at |
+----+-----------+-----------+---------+---------------------+------------+
| 1  | 1         | 10        | 1       | completed           | 2013-10-01 |
| 2  | 2         | 11        | 1       | cancelled_by_driver | 2013-10-01 |
| 3  | 3         | 12        | 6       | completed           | 2013-10-01 |
| 4  | 4         | 13        | 6       | cancelled_by_client | 2013-10-01 |
| 5  | 1         | 10        | 1       | completed           | 2013-10-02 |
| 6  | 2         | 11        | 6       | completed           | 2013-10-02 |
| 7  | 3         | 12        | 6       | completed           | 2013-10-02 |
| 8  | 2         | 12        | 12      | completed           | 2013-10-03 |
| 9  | 3         | 10        | 12      | completed           | 2013-10-03 |
| 10 | 4         | 13        | 12      | cancelled_by_driver | 2013-10-03 |
+----+-----------+-----------+---------+---------------------+------------+

Users 表：
+----------+--------+--------+
| users_id | banned | role   |
+----------+--------+--------+
| 1        | No     | client |
| 2        | Yes    | client |
| 3        | No     | client |
| 4        | No     | client |
| 10       | No     | driver |
| 11       | No     | driver |
| 12       | No     | driver |
| 13       | No     | driver |
+----------+--------+--------+
输出：
+------------+-------------------+
| Day        | Cancellation Rate |
+------------+-------------------+
| 2013-10-01 | 0.33              |
| 2013-10-02 | 0.00              |
| 2013-10-03 | 0.50              |
+------------+-------------------+
解释：
2013-10-01：
  - 共有 4 条请求，其中 2 条取消。
  - 然而，id=2 的请求是由禁止用户（user_id=2）发出的，所以计算时应当忽略它。
  - 因此，总共有 3 条非禁止请求参与计算，其中 1 条取消。
  - 取消率为 (1 / 3) = 0.33
2013-10-02：
  - 共有 3 条请求，其中 0 条取消。
  - 然而，id=6 的请求是由禁止用户发出的，所以计算时应当忽略它。
  - 因此，总共有 2 条非禁止请求参与计算，其中 0 条取消。
  - 取消率为 (0 / 2) = 0.00
2013-10-03：
  - 共有 3 条请求，其中 1 条取消。
  - 然而，id=8 的请求是由禁止用户发出的，所以计算时应当忽略它。
  - 因此，总共有 2 条非禁止请求参与计算，其中 1 条取消。
  - 取消率为 (1 / 2) = 0.50

```
 
**标签**
`数据库` 


## 
```python

```
>
# 263.丑数
[https://leetcode-cn.com/problems/ugly-number](https://leetcode-cn.com/problems/ugly-number) 
## 原题
给你一个整数 `n` ，请你判断 `n` 是否为 **丑数** 。如果是，返回 `true` ；否则，返回 `false` 。

 **丑数** 就是只包含质因数  `2` 、 `3` 和/或  `5`  的正整数。

 

 **示例 1：** 

```

输入：n = 6
输出：true
解释：6 = 2 × 3
```
 **示例 2：** 

```

输入：n = 8
输出：true
解释：8 = 2 × 2 × 2

```
 **示例 3：** 

```

输入：n = 14
输出：false
解释：14 不是丑数，因为它包含了另外一个质因数 7 。

```
 **示例 4：** 

```

输入：n = 1
输出：true
解释：1 通常被视为丑数。

```
 

 **提示：** 
-  `-2^31 <= n <= 2^31 - 1` 
 
**标签**
`数学` 


## 
```python

```
>
# 264.丑数 II
[https://leetcode-cn.com/problems/ugly-number-ii](https://leetcode-cn.com/problems/ugly-number-ii) 
## 原题
给你一个整数 `n` ，请你找出并返回第 `n` 个 **丑数** 。

 **丑数** 就是只包含质因数  `2` 、 `3` 和/或  `5`  的正整数。

 

 **示例 1：** 

```

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

```
 **示例 2：** 

```

输入：n = 1
输出：1
解释：1 通常被视为丑数。

```
 

 **提示：** 
-  `1 <= n <= 1690` 
 
**标签**
`哈希表` `数学` `动态规划` `堆（优先队列）` 


## 
```python

```
>
# 265.粉刷房子 II
[https://leetcode-cn.com/problems/paint-house-ii](https://leetcode-cn.com/problems/paint-house-ii) 
## 原题

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 266.回文排列
[https://leetcode-cn.com/problems/palindrome-permutation](https://leetcode-cn.com/problems/palindrome-permutation) 
## 原题

 
**标签**
`位运算` `哈希表` `字符串` 


## 
```python

```
>
# 267.回文排列 II
[https://leetcode-cn.com/problems/palindrome-permutation-ii](https://leetcode-cn.com/problems/palindrome-permutation-ii) 
## 原题

 
**标签**
`哈希表` `字符串` `回溯` 


## 
```python

```
>
# 268.丢失的数字
[https://leetcode-cn.com/problems/missing-number](https://leetcode-cn.com/problems/missing-number) 
## 原题
给定一个包含 `[0, n]` 中 `n` 个数的数组 `nums` ，找出 `[0, n]` 这个范围内没有出现在数组中的那个数。
 

 **示例 1：** 

```

输入：nums = [3,0,1]
输出：2
解释：n = 3，因为有 3 个数字，所以所有的数字都在范围 [0,3] 内。2 是丢失的数字，因为它没有出现在 nums 中。
```
 **示例 2：** 

```

输入：nums = [0,1]
输出：2
解释：n = 2，因为有 2 个数字，所以所有的数字都在范围 [0,2] 内。2 是丢失的数字，因为它没有出现在 nums 中。
```
 **示例 3：** 

```

输入：nums = [9,6,4,2,3,5,7,0,1]
输出：8
解释：n = 9，因为有 9 个数字，所以所有的数字都在范围 [0,9] 内。8 是丢失的数字，因为它没有出现在 nums 中。
```
 **示例 4：** 

```

输入：nums = [0]
输出：1
解释：n = 1，因为有 1 个数字，所以所有的数字都在范围 [0,1] 内。1 是丢失的数字，因为它没有出现在 nums 中。
```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 10^4` 
-  `0 <= nums[i] <= n` 
-  `nums` 中的所有数字都 **独一无二** 
 

 **进阶：** 你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

 
**标签**
`位运算` `数组` `哈希表` `数学` `排序` 


## 
```python

```
>
# 269.火星词典
[https://leetcode-cn.com/problems/alien-dictionary](https://leetcode-cn.com/problems/alien-dictionary) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `图` `拓扑排序` `数组` `字符串` 


## 
```python

```
>
# 270.最接近的二叉搜索树值
[https://leetcode-cn.com/problems/closest-binary-search-tree-value](https://leetcode-cn.com/problems/closest-binary-search-tree-value) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二分查找` `二叉树` 


## 
```python

```
>
# 271.字符串的编码与解码
[https://leetcode-cn.com/problems/encode-and-decode-strings](https://leetcode-cn.com/problems/encode-and-decode-strings) 
## 原题

 
**标签**
`设计` `数组` `字符串` 


## 
```python

```
>
# 272.最接近的二叉搜索树值 II
[https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii](https://leetcode-cn.com/problems/closest-binary-search-tree-value-ii) 
## 原题

 
**标签**
`栈` `树` `深度优先搜索` `二叉搜索树` `双指针` `二叉树` `堆（优先队列）` 


## 
```python

```
>
# 273.整数转换英文表示
[https://leetcode-cn.com/problems/integer-to-english-words](https://leetcode-cn.com/problems/integer-to-english-words) 
## 原题
将非负整数 `num` 转换为其对应的英文表示。

 

 **示例 1：** 

```

输入：num = 123
输出："One Hundred Twenty Three"

```
 **示例 2：** 

```

输入：num = 12345
输出："Twelve Thousand Three Hundred Forty Five"

```
 **示例 3：** 

```

输入：num = 1234567
输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

```
 

 **提示：** 
-  `0 <= num <= 2^31 - 1` 
 
**标签**
`递归` `数学` `字符串` 


## 
```python

```
>
# 274.H 指数
[https://leetcode-cn.com/problems/h-index](https://leetcode-cn.com/problems/h-index) 
## 原题
给你一个整数数组 `citations` ，其中 `citations[i]` 表示研究者的第 `i` 篇论文被引用的次数。计算并返回该研究者的 ** `h` 指数** 。

根据维基百科上 <a href="https://baike.baidu.com/item/h-index/3991452?fr=aladdin" target="_blank">h 指数的定义</a>：h 代表“高引用次数”，一名科研人员的 `h` **指数** 是指他（她）的 （ `n` 篇论文中） **总共** 有 `h` 篇论文分别被引用了 **至少** `h` 次。且其余的 *`n - h`* 篇论文每篇被引用次数 **不超过** *`h`* 次。

如果 `h` 有多种可能的值， ** `h` 指数** 是其中最大的那个。

 

 **示例 1：** 

```

输入：citations = [3,0,6,1,5]
输出：3 
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 3, 0, 6, 1, 5 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3。
```
 **示例 2：** 

```

输入：citations = [1,3,1]
输出：1

```
 

 **提示：** 
-  `n == citations.length` 
-  `1 <= n <= 5000` 
-  `0 <= citations[i] <= 1000` 
 
**标签**
`数组` `计数排序` `排序` 


## 
```python

```
>
# 275.H 指数 II
[https://leetcode-cn.com/problems/h-index-ii](https://leetcode-cn.com/problems/h-index-ii) 
## 原题
给你一个整数数组 `citations` ，其中 `citations[i]` 表示研究者的第 `i` 篇论文被引用的次数， `citations` 已经按照  **升序排列 ** 。计算并返回该研究者的 ** `h` * * 指数** 。

<a href="https://baike.baidu.com/item/h-index/3991452?fr=aladdin" target="_blank">h 指数的定义</a>：h 代表“高引用次数”（high citations），一名科研人员的 h 指数是指他（她）的 （ `n` 篇论文中） **总共** 有 `h` 篇论文分别被引用了 **至少** `h` 次。且其余的 *`n - h`  * 篇论文每篇被引用次数  **不超过** *`h`* 次。

 **提示：** 如果 `h` 有多种可能的值， ** `h` 指数** 是其中最大的那个。

请你设计并实现对数时间复杂度的算法解决此问题。

 

 **示例 1：** 

```

输入：citations = [0,1,3,5,6]
输出：3 
解释：给定数组表示研究者总共有 5 篇论文，每篇论文相应的被引用了 0, 1, 3, 5, 6 次。
     由于研究者有 3 篇论文每篇 至少 被引用了 3 次，其余两篇论文每篇被引用 不多于 3 次，所以她的 h 指数是 3 。
```
 **示例 2：** 

```

输入：citations = [1,2,100]
输出：2

```
 

 **提示：** 
-  `n == citations.length` 
-  `1 <= n <= 10^5` 
-  `0 <= citations[i] <= 1000` 
-  `citations` 按 **升序排列** 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 276.栅栏涂色
[https://leetcode-cn.com/problems/paint-fence](https://leetcode-cn.com/problems/paint-fence) 
## 原题

 
**标签**
`动态规划` 


## 
```python

```
>
# 277.搜寻名人
[https://leetcode-cn.com/problems/find-the-celebrity](https://leetcode-cn.com/problems/find-the-celebrity) 
## 原题

 
**标签**
`贪心` `图` `双指针` `交互` 


## 
```python

```
>
# 278.第一个错误的版本
[https://leetcode-cn.com/problems/first-bad-version](https://leetcode-cn.com/problems/first-bad-version) 
## 原题
你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有版本都是错的。

假设你有 `n` 个版本 `[1, 2, ..., n]` ，你想找出导致之后所有版本出错的第一个错误的版本。

你可以通过调用  `bool isBadVersion(version)`  接口来判断版本号 `version` 是否在单元测试中出错。实现一个函数来查找第一个错误的版本。你应该尽量减少对调用 API 的次数。
 

 **示例 1：** 

```

输入：n = 5, bad = 4
输出：4
解释：
调用 isBadVersion(3) -> false 
调用 isBadVersion(5) -> true 
调用 isBadVersion(4) -> true
所以，4 是第一个错误的版本。

```
 **示例 2：** 

```

输入：n = 1, bad = 1
输出：1

```
 

 **提示：** 
-  `1 <= bad <= n <= 2^31 - 1` 
 
**标签**
`二分查找` `交互` 


## 
```python

```
>
# 279.完全平方数
[https://leetcode-cn.com/problems/perfect-squares](https://leetcode-cn.com/problems/perfect-squares) 
## 原题
给你一个整数 `n` ，返回 *和为 `n` 的完全平方数的最少数量* 。

 **完全平方数** 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。例如， `1` 、 `4` 、 `9` 和 `16` 都是完全平方数，而 `3` 和 `11` 不是。

 

 **示例 1：** 

```

输入：n = 12
输出：3 
解释：12 = 4 + 4 + 4
```
 **示例 2：** 

```

输入：n = 13
输出：2
解释：13 = 4 + 9
```

 

 **提示：** 
-  `1 <= n <= 10^4` 
 
**标签**
`广度优先搜索` `数学` `动态规划` 


## 
```python

```
>
# 280.摆动排序
[https://leetcode-cn.com/problems/wiggle-sort](https://leetcode-cn.com/problems/wiggle-sort) 
## 原题

 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 281.锯齿迭代器
[https://leetcode-cn.com/problems/zigzag-iterator](https://leetcode-cn.com/problems/zigzag-iterator) 
## 原题

 
**标签**
`设计` `队列` `数组` `迭代器` 


## 
```python

```
>
# 282.给表达式添加运算符
[https://leetcode-cn.com/problems/expression-add-operators](https://leetcode-cn.com/problems/expression-add-operators) 
## 原题
给定一个仅包含数字 `0-9` 的字符串 `num` 和一个目标值整数 `target` ，在 `num` 的数字之间添加 **二元** 运算符（不是一元） `+` 、 `-` 或 `*` ，返回所有能够得到目标值的表达式。

 

 **示例 1:** 

```

输入: num = "123", target = 6
输出: ["1+2+3", "1*2*3"] 

```
 **示例 2:** 

```

输入: num = "232", target = 8
输出: ["2*3+2", "2+3*2"]
```
 **示例 3:** 

```

输入: num = "105", target = 5
输出: ["1*0+5","10-5"]
```
 **示例 4:** 

```

输入: num = "00", target = 0
输出: ["0+0", "0-0", "0*0"]

```
 **示例 5:** 

```

输入: num = "3456237490", target = 9191
输出: []
```
 

 **提示：** 
-  `1 <= num.length <= 10` 
-  `num` 仅含数字
-  `-2^31 <= target <= 2^31 - 1` 
 
**标签**
`数学` `字符串` `回溯` 


## 
```python

```
>
# 283.移动零
[https://leetcode-cn.com/problems/move-zeroes](https://leetcode-cn.com/problems/move-zeroes) 
## 原题
给定一个数组 `nums` ，编写一个函数将所有 `0` 移动到数组的末尾，同时保持非零元素的相对顺序。

 **请注意** ，必须在不复制数组的情况下原地对数组进行操作。

 

 **示例 1:** 

```

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

```
 **示例 2:** 

```

输入: nums = [0]
输出: [0]
```
 

 **提示** :
<meta charset="UTF-8" />
-  `1 <= nums.length <= 10^4` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
 

<b>进阶：</b>你能尽量减少完成的操作次数吗？

 
**标签**
`数组` `双指针` 


## 
```python

```
>
# 284.顶端迭代器
[https://leetcode-cn.com/problems/peeking-iterator](https://leetcode-cn.com/problems/peeking-iterator) 
## 原题
请你在设计一个迭代器，在集成现有迭代器拥有的 `hasNext` 和 `next` 操作的基础上，还额外支持 `peek` 操作。

实现 `PeekingIterator` 类：
-  `PeekingIterator(Iterator<int> nums)` 使用指定整数迭代器 `nums` 初始化迭代器。
-  `int next()` 返回数组中的下一个元素，并将指针移动到下个元素处。
-  `bool hasNext()` 如果数组中存在下一个元素，返回 `true` ；否则，返回 `false` 。
-  `int peek()` 返回数组中的下一个元素，但 **不** 移动指针。
 **注意：** 每种语言可能有不同的构造函数和迭代器 `Iterator` ，但均支持 `int next()` 和 `boolean hasNext()` 函数。

 

 **示例 1：** 

```

输入：
["PeekingIterator", "next", "peek", "next", "next", "hasNext"]
[[[1, 2, 3]], [], [], [], [], []]
输出：
[null, 1, 2, 2, 3, false]

解释：
PeekingIterator peekingIterator = new PeekingIterator([1, 2, 3]); // [1,2,3]
peekingIterator.next();    // 返回 1 ，指针移动到下一个元素 [1,2,3]
peekingIterator.peek();    // 返回 2 ，指针未发生移动 [1,2,3]
peekingIterator.next();    // 返回 2 ，指针移动到下一个元素 [1,2,3]
peekingIterator.next();    // 返回 3 ，指针移动到下一个元素 [1,2,3]
peekingIterator.hasNext(); // 返回 False

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `1 <= nums[i] <= 1000` 
- 对 `next` 和 `peek` 的调用均有效
-  `next` 、 `hasNext` 和 `peek` 最多调用 `1000` 次
 

 **进阶：** 你将如何拓展你的设计？使之变得通用化，从而适应所有的类型，而不只是整数型？

 
**标签**
`设计` `数组` `迭代器` 


## 
```python

```
>
# 285.二叉搜索树中的中序后继
[https://leetcode-cn.com/problems/inorder-successor-in-bst](https://leetcode-cn.com/problems/inorder-successor-in-bst) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 286.墙与门
[https://leetcode-cn.com/problems/walls-and-gates](https://leetcode-cn.com/problems/walls-and-gates) 
## 原题

 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 287.寻找重复数
[https://leetcode-cn.com/problems/find-the-duplicate-number](https://leetcode-cn.com/problems/find-the-duplicate-number) 
## 原题
给定一个包含 `n + 1` 个整数的数组 `nums` ，其数字都在 `[1, n]` 范围内（包括 `1` 和 `n` ），可知至少存在一个重复的整数。

假设 `nums` 只有 **一个重复的整数** ，返回 **这个重复的数** 。

你设计的解决方案必须 **不修改** 数组 `nums` 且只用常量级 `O(1)` 的额外空间。

 

 **示例 1：** 

```

输入：nums = [1,3,4,2,2]
输出：2

```
 **示例 2：** 

```

输入：nums = [3,1,3,4,2]
输出：3

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `nums.length == n + 1` 
-  `1 <= nums[i] <= n` 
-  `nums` 中 **只有一个整数** 出现 **两次或多次** ，其余整数均只出现 **一次** 
 

<b>进阶：</b>
- 如何证明 `nums` 中至少存在一个重复的数字?
- 你可以设计一个线性级时间复杂度 `O(n)` 的解决方案吗？
 
**标签**
`位运算` `数组` `双指针` `二分查找` 


## 
```python

```
>
# 288.单词的唯一缩写
[https://leetcode-cn.com/problems/unique-word-abbreviation](https://leetcode-cn.com/problems/unique-word-abbreviation) 
## 原题

 
**标签**
`设计` `数组` `哈希表` `字符串` 


## 
```python

```
>
# 289.生命游戏
[https://leetcode-cn.com/problems/game-of-life](https://leetcode-cn.com/problems/game-of-life) 
## 原题
根据 <a href="https://baike.baidu.com/item/%E7%94%9F%E5%91%BD%E6%B8%B8%E6%88%8F/2926434?fr=aladdin" target="_blank">百度百科</a> ， **生命游戏** ，简称为 **生命** ，是英国数学家约翰·何顿·康威在 1970 年发明的细胞自动机。

给定一个包含 `m × n` 个格子的面板，每一个格子都可以看成是一个细胞。每个细胞都具有一个初始状态： `1` 即为 **活细胞** （live），或 `0` 即为 **死细胞** （dead）。每个细胞与其八个相邻位置（水平，垂直，对角线）的细胞都遵循以下四条生存定律：
- 如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
- 如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
- 如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
- 如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
下一个状态是通过将上述规则同时应用于当前状态下的每个细胞所形成的，其中细胞的出生和死亡是同时发生的。给你 `m x n` 网格面板 `board` 的当前状态，返回下一个状态。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid1.jpg" />
```

输入：board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
输出：[[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/26/grid2.jpg" />
```

输入：board = [[1,1],[1,0]]
输出：[[1,1],[1,1]]

```
 

 **提示：** 
-  `m == board.length` 
-  `n == board[i].length` 
-  `1 <= m, n <= 25` 
-  `board[i][j]` 为 `0` 或 `1` 
 

 **进阶：** 
- 你可以使用原地算法解决本题吗？请注意，面板上所有格子需要同时被更新：你不能先更新某些格子，然后使用它们的更新后的值再更新其他格子。
- 本题中，我们使用二维数组来表示面板。原则上，面板是无限的，但当活细胞侵占了面板边界时会造成问题。你将如何解决这些问题？
 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 290.单词规律
[https://leetcode-cn.com/problems/word-pattern](https://leetcode-cn.com/problems/word-pattern) 
## 原题
给定一种规律 `pattern` 和一个字符串 `str` ，判断 `str` 是否遵循相同的规律。

这里的 **遵循** 指完全匹配，例如， `pattern` 里的每个字母和字符串 `str` **** 中的每个非空单词之间存在着双向连接的对应规律。

 **示例1:** 

```
输入: pattern = "abba", str = "dog cat cat dog"
输出: true
```
 **示例 2:** 

```
输入:pattern = "abba", str = "dog cat cat fish"
输出: false
```
 **示例 3:** 

```
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
```
 **示例 4:** 

```
输入: pattern = "abba", str = "dog dog dog dog"
输出: false
```
 **说明:** <br>
你可以假设 `pattern` 只包含小写字母， `str` 包含了由单个空格分隔的小写字母。    

 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 291.单词规律 II
[https://leetcode-cn.com/problems/word-pattern-ii](https://leetcode-cn.com/problems/word-pattern-ii) 
## 原题

 
**标签**
`哈希表` `字符串` `回溯` 


## 
```python

```
>
# 292.Nim 游戏
[https://leetcode-cn.com/problems/nim-game](https://leetcode-cn.com/problems/nim-game) 
## 原题
你和你的朋友，两个人一起玩 <a href="https://baike.baidu.com/item/Nim游戏/6737105" target="_blank">Nim 游戏</a>：
- 桌子上有一堆石头。
- 你们轮流进行自己的回合， **你作为先手** 。
- 每一回合，轮到的人拿掉 1 - 3 块石头。
- 拿掉最后一块石头的人就是获胜者。
假设你们每一步都是最优解。请编写一个函数，来判断你是否可以在给定石头数量为 `n` 的情况下赢得游戏。如果可以赢，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：n = 4
输出：false 
解释：以下是可能的结果:
1. 移除1颗石头。你的朋友移走了3块石头，包括最后一块。你的朋友赢了。
2. 移除2个石子。你的朋友移走2块石头，包括最后一块。你的朋友赢了。
3.你移走3颗石子。你的朋友移走了最后一块石头。你的朋友赢了。
在所有结果中，你的朋友是赢家。

```
 **示例 2：** 

```

输入：n = 1
输出：true

```
 **示例 3：** 

```

输入：n = 2
输出：true

```
 

 **提示：** 
-  `1 <= n <= 2^31 - 1` 
 
**标签**
`脑筋急转弯` `数学` `博弈` 


## 
```python

```
>
# 293.翻转游戏
[https://leetcode-cn.com/problems/flip-game](https://leetcode-cn.com/problems/flip-game) 
## 原题

 
**标签**
`字符串` 


## 
```python

```
>
# 294.翻转游戏 II
[https://leetcode-cn.com/problems/flip-game-ii](https://leetcode-cn.com/problems/flip-game-ii) 
## 原题

 
**标签**
`记忆化搜索` `数学` `动态规划` `回溯` `博弈` 


## 
```python

```
>
# 295.数据流的中位数
[https://leetcode-cn.com/problems/find-median-from-data-stream](https://leetcode-cn.com/problems/find-median-from-data-stream) 
## 原题
中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。

例如，

[2,3,4] 的中位数是 3

[2,3] 的中位数是 (2 + 3) / 2 = 2.5

设计一个支持以下两种操作的数据结构：
- void addNum(int num) - 从数据流中添加一个整数到数据结构中。
- double findMedian() - 返回目前所有元素的中位数。
 **示例：** 

```
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
```
 **进阶:** 
- 如果数据流中所有整数都在 0 到 100 范围内，你将如何优化你的算法？
- 如果数据流中 99% 的整数都在 0 到 100 范围内，你将如何优化你的算法？
 
**标签**
`设计` `双指针` `数据流` `排序` `堆（优先队列）` 


## 
```python

```
>
# 296.最佳的碰头地点
[https://leetcode-cn.com/problems/best-meeting-point](https://leetcode-cn.com/problems/best-meeting-point) 
## 原题

 
**标签**
`数组` `数学` `矩阵` `排序` 


## 
```python

```
>
# 297.二叉树的序列化与反序列化
[https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree) 
## 原题
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

 **提示:** 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 <a href="/faq/#binary-tree">LeetCode 序列化二叉树的格式</a>。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/serdeser.jpg" style="width: 442px; height: 324px;" />
```

输入：root = [1,2,3,null,null,4,5]
输出：[1,2,3,null,null,4,5]

```
 **示例 2：** 

```

输入：root = []
输出：[]

```
 **示例 3：** 

```

输入：root = [1]
输出：[1]

```
 **示例 4：** 

```

输入：root = [1,2]
输出：[1,2]

```
 

 **提示：** 
- 树中结点数在范围 `[0, 10^4]` 内
-  `-1000 <= Node.val <= 1000` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `设计` `字符串` `二叉树` 


## 
```python

```
>
# 298.二叉树最长连续序列
[https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence](https://leetcode-cn.com/problems/binary-tree-longest-consecutive-sequence) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 299.猜数字游戏
[https://leetcode-cn.com/problems/bulls-and-cows](https://leetcode-cn.com/problems/bulls-and-cows) 
## 原题
你在和朋友一起玩 <a href="https://baike.baidu.com/item/%E7%8C%9C%E6%95%B0%E5%AD%97/83200?fromtitle=Bulls+and+Cows&amp;fromid=12003488&amp;fr=aladdin" target="_blank">猜数字（Bulls and Cows）</a>游戏，该游戏规则如下：

写出一个秘密数字，并请朋友猜这个数字是多少。朋友每猜测一次，你就会给他一个包含下述信息的提示：
- 猜测数字中有多少位属于数字和确切位置都猜对了（称为 "Bulls"，公牛），
- 有多少位属于数字猜对了但是位置不对（称为 "Cows"，奶牛）。也就是说，这次猜测中有多少位非公牛数字可以通过重新排列转换成公牛数字。
给你一个秘密数字 `secret` 和朋友猜测的数字 `guess` ，请你返回对朋友这次猜测的提示。

提示的格式为 `"xAyB"` ， `x` 是公牛个数， `y` 是奶牛个数， `A` 表示公牛， `B` 表示奶牛。

请注意秘密数字和朋友猜测的数字都可能含有重复数字。

 

 **示例 1：** 

```

输入：secret = "1807", guess = "7810"
输出："1A3B"
解释：数字和位置都对（公牛）用 '|' 连接，数字猜对位置不对（奶牛）的采用斜体加粗标识。
"1807"
  |
"7810"
```
 **示例 2：** 

```

输入：secret = "1123", guess = "0111"
输出："1A1B"
解释：数字和位置都对（公牛）用 '|' 连接，数字猜对位置不对（奶牛）的采用斜体加粗标识。
"1123"        "1123"
  |      or     |
"0111"        "0111"
注意，两个不匹配的 1 中，只有一个会算作奶牛（数字猜对位置不对）。通过重新排列非公牛数字，其中仅有一个 1 可以成为公牛数字。
```
 

 **提示：** 
-  `1 <= secret.length, guess.length <= 1000` 
-  `secret.length == guess.length` 
-  `secret` 和 `guess` 仅由数字组成
 
**标签**
`哈希表` `字符串` `计数` 


## 
```python

```
>
# 300.最长递增子序列
[https://leetcode-cn.com/problems/longest-increasing-subsequence](https://leetcode-cn.com/problems/longest-increasing-subsequence) 
## 原题
给你一个整数数组 `nums` ，找到其中最长严格递增子序列的长度。

 **子序列** 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如， `[3,6,2,7]` 是数组 `[0,3,1,6,2,2,7]` 的子序列。
 

 **示例 1：** 

```

输入：nums = [10,9,2,5,3,7,101,18]
输出：4
解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。

```
 **示例 2：** 

```

输入：nums = [0,1,0,3,2,3]
输出：4

```
 **示例 3：** 

```

输入：nums = [7,7,7,7,7,7,7]
输出：1

```
 

 **提示：** 
-  `1 <= nums.length <= 2500` 
-  `-10^4 <= nums[i] <= 10^4` 
 

<b>进阶：</b>
- 你能将算法的时间复杂度降低到 `O(n log(n))` 吗?
 
**标签**
`数组` `二分查找` `动态规划` 


## 
```python

```
>
