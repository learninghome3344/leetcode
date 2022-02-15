# 1.两数之和
[https://leetcode-cn.com/problems/two-sum](https://leetcode-cn.com/problems/two-sum) 
## 原题
给定一个整数数组 `nums`  和一个整数目标值 `target` ，请你在该数组中找出 **和为目标值** *`target`*   的那  **两个**  整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

 **示例 1：** 

```

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

```
 **示例 2：** 

```

输入：nums = [3,2,4], target = 6
输出：[1,2]

```
 **示例 3：** 

```

输入：nums = [3,3], target = 6
输出：[0,1]

```
 

 **提示：** 
-  `2 <= nums.length <= 10^4` 
-  `-10^9 <= nums[i] <= 10^9` 
-  `-10^9 <= target <= 10^9` 
-  **只会存在一个有效答案** 
 **进阶：** 你可以想出一个时间复杂度小于 `O(n^2)` 的算法吗？

 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 2.两数相加
[https://leetcode-cn.com/problems/add-two-numbers](https://leetcode-cn.com/problems/add-two-numbers) 
## 原题
给你两个  **非空** 的链表，表示两个非负的整数。它们每位数字都是按照  **逆序**  的方式存储的，并且每个节点只能存储  **一位**  数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/01/02/addtwonumber1.jpg" style="width: 483px; height: 342px;" />
```

输入：l1 = [2,4,3], l2 = [5,6,4]
输出：[7,0,8]
解释：342 + 465 = 807.

```
 **示例 2：** 

```

输入：l1 = [0], l2 = [0]
输出：[0]

```
 **示例 3：** 

```

输入：l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
输出：[8,9,9,9,0,0,0,1]

```
 

 **提示：** 
- 每个链表中的节点数在范围 `[1, 100]` 内
-  `0 <= Node.val <= 9` 
- 题目数据保证列表表示的数字不含前导零
 
**标签**
`递归` `链表` `数学` 


## 
```python

```
>
# 3.无重复字符的最长子串
[https://leetcode-cn.com/problems/longest-substring-without-repeating-characters](https://leetcode-cn.com/problems/longest-substring-without-repeating-characters) 
## 原题
给定一个字符串 `s` ，请你找出其中不含有重复字符的 **最长子串** 的长度。

 

 **示例 1:** 

```

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

```
 **示例 2:** 

```

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

```
 **示例 3:** 

```

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

```
 

 **提示：** 
-  `0 <= s.length <= 5 * 10^4` 
-  `s` 由英文字母、数字、符号和空格组成
 
**标签**
`哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
# 4.寻找两个正序数组的中位数
[https://leetcode-cn.com/problems/median-of-two-sorted-arrays](https://leetcode-cn.com/problems/median-of-two-sorted-arrays) 
## 原题
给定两个大小分别为 `m` 和 `n` 的正序（从小到大）数组 `nums1` 和 `nums2` 。请你找出并返回这两个正序数组的 **中位数** 。

算法的时间复杂度应该为 `O(log (m+n))` 。

 

 **示例 1：** 

```

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2

```
 **示例 2：** 

```

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

```
 

 

 **提示：** 
-  `nums1.length == m` 
-  `nums2.length == n` 
-  `0 <= m <= 1000` 
-  `0 <= n <= 1000` 
-  `1 <= m + n <= 2000` 
-  `-10^6 <= nums1[i], nums2[i] <= 10^6` 
 
**标签**
`数组` `二分查找` `分治` 


## 
```python

```
>
# 5.最长回文子串
[https://leetcode-cn.com/problems/longest-palindromic-substring](https://leetcode-cn.com/problems/longest-palindromic-substring) 
## 原题
给你一个字符串 `s` ，找到 `s` 中最长的回文子串。

 

 **示例 1：** 

```

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。

```
 **示例 2：** 

```

输入：s = "cbbd"
输出："bb"

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s` 仅由数字和英文字母组成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 6.Z 字形变换
[https://leetcode-cn.com/problems/zigzag-conversion](https://leetcode-cn.com/problems/zigzag-conversion) 
## 原题
将一个给定字符串 `s` 根据给定的行数 `numRows` ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 `"PAYPALISHIRING"`  行数为 `3` 时，排列如下：

```

P   A   H   N
A P L S I I G
Y   I   R
```
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如： `"PAHNAPLSIIGYIR"` 。

请你实现这个将字符串进行指定行数变换的函数：

```

string convert(string s, int numRows);
```
 

 **示例 1：** 

```

输入：s = "PAYPALISHIRING", numRows = 3
输出："PAHNAPLSIIGYIR"

```

 **示例 2：** 

```

输入：s = "PAYPALISHIRING", numRows = 4
输出："PINALSIGYAHRPI"
解释：
P     I    N
A   L S  I G
Y A   H R
P     I

```
 **示例 3：** 

```

输入：s = "A", numRows = 1
输出："A"

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s` 由英文字母（小写和大写）、 `','` 和 `'.'` 组成
-  `1 <= numRows <= 1000` 
 
**标签**
`字符串` 


## 
```python

```
>
# 7.整数反转
[https://leetcode-cn.com/problems/reverse-integer](https://leetcode-cn.com/problems/reverse-integer) 
## 原题
给你一个 32 位的有符号整数 `x` ，返回将 `x` 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围  `[−2^31,  2^31 − 1]` ，就返回 0。
 **假设环境不允许存储 64 位整数（有符号或无符号）。** 

 

 **示例 1：** 

```

输入：x = 123
输出：321

```
 **示例 2：** 

```

输入：x = -123
输出：-321

```
 **示例 3：** 

```

输入：x = 120
输出：21

```
 **示例 4：** 

```

输入：x = 0
输出：0

```
 

 **提示：** 
-  `-2^31 <= x <= 2^31 - 1` 
 
**标签**
`数学` 


## 
```python

```
>
# 8.字符串转换整数 (atoi)
[https://leetcode-cn.com/problems/string-to-integer-atoi](https://leetcode-cn.com/problems/string-to-integer-atoi) 
## 原题
请你来实现一个 `myAtoi(string s)` 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 `atoi` 函数）。

函数 `myAtoi(string s)` 的算法如下：
- 读入字符串并丢弃无用的前导空格
- 检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
- 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
- 将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 `0` 。必要时更改符号（从步骤 2 开始）。
- 如果整数数超过 32 位有符号整数范围 `[−2^31,  2^31 − 1]` ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 `−2^31` 的整数应该被固定为 `−2^31` ，大于 `2^31 − 1` 的整数应该被固定为 `2^31 − 1` 。
- 返回整数作为最终结果。
 **注意：** 
- 本题中的空白字符只包括空格字符 `' '` 。
- 除前导空格或数字后的其余字符串外， **请勿忽略** 任何其他字符。
 

 **示例 1：** 

```

输入：s = "42"
输出：42
解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
第 1 步："42"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："42"（读入 "42"）
           ^
解析得到整数 42 。
由于 "42" 在范围 [-2^31, 2^31 - 1] 内，最终结果为 42 。
```
 **示例 2：** 

```

输入：s = "   -42"
输出：-42
解释：
第 1 步："   -42"（读入前导空格，但忽视掉）
            ^
第 2 步："   -42"（读入 '-' 字符，所以结果应该是负数）
             ^
第 3 步："   -42"（读入 "42"）
               ^
解析得到整数 -42 。
由于 "-42" 在范围 [-2^31, 2^31 - 1] 内，最终结果为 -42 。

```
 **示例 3：** 

```

输入：s = "4193 with words"
输出：4193
解释：
第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："4193 with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止）
             ^
解析得到整数 4193 。
由于 "4193" 在范围 [-2^31, 2^31 - 1] 内，最终结果为 4193 。

```
 

 **提示：** 
-  `0 <= s.length <= 200` 
-  `s` 由英文字母（大写和小写）、数字（ `0-9` ）、 `' '` 、 `'+'` 、 `'-'` 和 `'.'` 组成
 
**标签**
`字符串` 


## 
```python

```
>
# 9.回文数
[https://leetcode-cn.com/problems/palindrome-number](https://leetcode-cn.com/problems/palindrome-number) 
## 原题
给你一个整数 `x` ，如果 `x` 是一个回文整数，返回 `true` ；否则，返回 `false` 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
- 例如， `121` 是回文，而 `123` 不是。
 

 **示例 1：** 

```

输入：x = 121
输出：true

```
 **示例 2：** 

```

输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

```
 **示例 3：** 

```

输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。

```
 

 **提示：** 
-  `-2^31 <= x <= 2^31 - 1` 
 

 **进阶：** 你能不将整数转为字符串来解决这个问题吗？

 
**标签**
`数学` 


## 
```python

```
>
# 10.正则表达式匹配
[https://leetcode-cn.com/problems/regular-expression-matching](https://leetcode-cn.com/problems/regular-expression-matching) 
## 原题
给你一个字符串 `s` 和一个字符规律 `p` ，请你来实现一个支持 `'.'` 和 `'*'` 的正则表达式匹配。
-  `'.'` 匹配任意单个字符
-  `'*'` 匹配零个或多个前面的那一个元素
所谓匹配，是要涵盖 **整个** 字符串 `s` 的，而不是部分字符串。
 

 **示例 1：** 

```

输入：s = "aa", p = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。

```
 **示例 2:** 

```

输入：s = "aa", p = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。

```
 **示例 3：** 

```

输入：s = "ab", p = ".*"
输出：true
解释：".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。

```
 

 **提示：** 
-  `1 <= s.length <= 20` 
-  `1 <= p.length <= 30` 
-  `s` 只包含从 `a-z` 的小写字母。
-  `p` 只包含从 `a-z` 的小写字母，以及字符 `.` 和 `*` 。
- 保证每次出现字符 `*` 时，前面都匹配到有效的字符
 
**标签**
`递归` `字符串` `动态规划` 


## 
```python

```
>
# 11.盛最多水的容器
[https://leetcode-cn.com/problems/container-with-most-water](https://leetcode-cn.com/problems/container-with-most-water) 
## 原题
给定一个长度为 `n` 的整数数组 `height` 。有 `n` 条垂线，第 `i` 条线的两个端点是 `(i, 0)` 和 `(i, height[i])` 。

找出其中的两条线，使得它们与 `x` 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

 **说明：** 你不能倾斜容器。

 

 **示例 1：** 

<img alt="" src="https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg" />

```

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
```
 **示例 2：** 

```

输入：height = [1,1]
输出：1

```
 

 **提示：** 
-  `n == height.length` 
-  `2 <= n <= 10^5` 
-  `0 <= height[i] <= 10^4` 
 
**标签**
`贪心` `数组` `双指针` 


## 
```python

```
>
# 12.整数转罗马数字
[https://leetcode-cn.com/problems/integer-to-roman](https://leetcode-cn.com/problems/integer-to-roman) 
## 原题
罗马数字包含以下七种字符：  `I` ，  `V` ，  `X` ，  `L` ， `C` ， `D`  和  `M` 。

```

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
例如， 罗马数字 2 写做  `II`  ，即为两个并列的 1。12 写做  `XII`  ，即为  `X`  +  `II`  。 27 写做   `XXVII` , 即为  `XX`  +  `V`  +  `II`  。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做  `IIII` ，而是  `IV` 。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为  `IX` 。这个特殊的规则只适用于以下六种情况：
-  `I`  可以放在  `V`  (5) 和  `X`  (10) 的左边，来表示 4 和 9。
-  `X`  可以放在  `L`  (50) 和  `C`  (100) 的左边，来表示 40 和 90。 
-  `C`  可以放在  `D`  (500) 和  `M`  (1000) 的左边，来表示 400 和 900。
给你一个整数，将其转为罗马数字。

 

 **示例 1:** 

```

输入: num = 3
输出: "III"
```
 **示例 2:** 

```

输入: num = 4
输出: "IV"
```
 **示例 3:** 

```

输入: num = 9
输出: "IX"
```
 **示例 4:** 

```

输入: num = 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

```
 **示例 5:** 

```

输入: num = 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```
 

 **提示：** 
-  `1 <= num <= 3999` 
 
**标签**
`哈希表` `数学` `字符串` 


## 
```python

```
>
# 13.罗马数字转整数
[https://leetcode-cn.com/problems/roman-to-integer](https://leetcode-cn.com/problems/roman-to-integer) 
## 原题
罗马数字包含以下七种字符: `I` ， `V` ， `X` ， `L` ， `C` ， `D` 和 `M` 。

```

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```
例如， 罗马数字 `2` 写做 `II` ，即为两个并列的 1 。 `12` 写做 `XII` ，即为 `X` + `II` 。 `27` 写做 `XXVII` , 即为 `XX` + `V` + `II` 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 `IIII` ，而是 `IV` 。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 `IX` 。这个特殊的规则只适用于以下六种情况：
-  `I` 可以放在 `V` (5) 和 `X` (10) 的左边，来表示 4 和 9。
-  `X` 可以放在 `L` (50) 和 `C` (100) 的左边，来表示 40 和 90。 
-  `C` 可以放在 `D` (500) 和 `M` (1000) 的左边，来表示 400 和 900。
给定一个罗马数字，将其转换成整数。

 

 **示例 1:** 

```

输入: s = "III"
输出: 3
```
 **示例 2:** 

```

输入: s = "IV"
输出: 4
```
 **示例 3:** 

```

输入: s = "IX"
输出: 9
```
 **示例 4:** 

```

输入: s = "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

```
 **示例 5:** 

```

输入: s = "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```
 

 **提示：** 
-  `1 <= s.length <= 15` 
-  `s` 仅含字符 `('I', 'V', 'X', 'L', 'C', 'D', 'M')` 
- 题目数据保证 `s` 是一个有效的罗马数字，且表示整数在范围 `[1, 3999]` 内
- 题目所给测试用例皆符合罗马数字书写规则，不会出现跨位等情况。
- IL 和 IM 这样的例子并不符合题目要求，49 应该写作 XLIX，999 应该写作 CMXCIX 。
- 关于罗马数字的详尽书写规则，可以参考 <a href="https://b2b.partcommunity.com/community/knowledge/zh_CN/detail/10753/%E7%BD%97%E9%A9%AC%E6%95%B0%E5%AD%97#knowledge_article">罗马数字 - Mathematics </a>。
 
**标签**
`哈希表` `数学` `字符串` 


## 
```python

```
>
# 14.最长公共前缀
[https://leetcode-cn.com/problems/longest-common-prefix](https://leetcode-cn.com/problems/longest-common-prefix) 
## 原题
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 `""` 。

 

 **示例 1：** 

```

输入：strs = ["flower","flow","flight"]
输出："fl"

```
 **示例 2：** 

```

输入：strs = ["dog","racecar","car"]
输出：""
解释：输入不存在公共前缀。
```
 

 **提示：** 
-  `1 <= strs.length <= 200` 
-  `0 <= strs[i].length <= 200` 
-  `strs[i]` 仅由小写英文字母组成
 
**标签**
`字符串` 


## 
```python

```
>
# 15.三数之和
[https://leetcode-cn.com/problems/3sum](https://leetcode-cn.com/problems/3sum) 
## 原题
给你一个包含 `n` 个整数的数组  `nums` ，判断  `nums`  中是否存在三个元素 *a，b，c ，* 使得  *a + b + c =* 0 ？请你找出所有和为 `0` 且不重复的三元组。

 **注意：** 答案中不可以包含重复的三元组。

 

 **示例 1：** 

```

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

```
 **示例 2：** 

```

输入：nums = []
输出：[]

```
 **示例 3：** 

```

输入：nums = [0]
输出：[]

```
 

 **提示：** 
-  `0 <= nums.length <= 3000` 
-  `-10^5 <= nums[i] <= 10^5` 
 
**标签**
`数组` `双指针` `排序` 


## 
```python

```
>
# 16.最接近的三数之和
[https://leetcode-cn.com/problems/3sum-closest](https://leetcode-cn.com/problems/3sum-closest) 
## 原题
给你一个长度为 `n` 的整数数组 `nums` 和 一个目标值 `target` 。请你从 `nums` 中选出三个整数，使它们的和与 `target` 最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。

 

 **示例 1：** 

```

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

```
 **示例 2：** 

```

输入：nums = [0,0,0], target = 1
输出：0

```
 

 **提示：** 
-  `3 <= nums.length <= 1000` 
-  `-1000 <= nums[i] <= 1000` 
-  `-10^4 <= target <= 10^4` 
 
**标签**
`数组` `双指针` `排序` 


## 
```python

```
>
# 17.电话号码的字母组合
[https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number) 
## 原题
给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。答案可以按 **任意顺序** 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/11/09/200px-telephone-keypad2svg.png" style="width: 200px;" />

 

 **示例 1：** 

```

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]

```
 **示例 2：** 

```

输入：digits = ""
输出：[]

```
 **示例 3：** 

```

输入：digits = "2"
输出：["a","b","c"]

```
 

 **提示：** 
-  `0 <= digits.length <= 4` 
-  `digits[i]` 是范围 `['2', '9']` 的一个数字。
 
**标签**
`哈希表` `字符串` `回溯` 


## 
```python

```
>
# 18.四数之和
[https://leetcode-cn.com/problems/4sum](https://leetcode-cn.com/problems/4sum) 
## 原题
给你一个由 `n` 个整数组成的数组 `nums` ，和一个目标值 `target` 。请你找出并返回满足下述全部条件且 **不重复** 的四元组 `[nums[a], nums[b], nums[c], nums[d]]` （若两个四元组元素一一对应，则认为两个四元组重复）：
-  `0 <= a, b, c, d < n` 
-  `a` 、 `b` 、 `c` 和 `d` **互不相同** 
-  `nums[a] + nums[b] + nums[c] + nums[d] == target` 
你可以按 **任意顺序** 返回答案 。

 

 **示例 1：** 

```

输入：nums = [1,0,-1,0,-2,2], target = 0
输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

```
 **示例 2：** 

```

输入：nums = [2,2,2,2,2], target = 8
输出：[[2,2,2,2]]

```
 

 **提示：** 
-  `1 <= nums.length <= 200` 
-  `-10^9 <= nums[i] <= 10^9` 
-  `-10^9 <= target <= 10^9` 
 
**标签**
`数组` `双指针` `排序` 


## 
```python

```
>
# 19.删除链表的倒数第 N 个结点
[https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list) 
## 原题
给你一个链表，删除链表的倒数第 `n` 个结点，并且返回链表的头结点。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/remove_ex1.jpg" style="width: 542px; height: 222px;" />
```

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]

```
 **示例 2：** 

```

输入：head = [1], n = 1
输出：[]

```
 **示例 3：** 

```

输入：head = [1,2], n = 1
输出：[1]

```
 

 **提示：** 
- 链表中结点的数目为 `sz` 
-  `1 <= sz <= 30` 
-  `0 <= Node.val <= 100` 
-  `1 <= n <= sz` 
 

 **进阶：** 你能尝试使用一趟扫描实现吗？

 
**标签**
`链表` `双指针` 


## 
```python

```
>
# 20.有效的括号
[https://leetcode-cn.com/problems/valid-parentheses](https://leetcode-cn.com/problems/valid-parentheses) 
## 原题
给定一个只包括 `'('` ， `')'` ， `'{'` ， `'}'` ， `'['` ， `']'`  的字符串 `s` ，判断字符串是否有效。

有效字符串需满足：
- 左括号必须用相同类型的右括号闭合。
- 左括号必须以正确的顺序闭合。
 

 **示例 1：** 

```

输入：s = "()"
输出：true

```
 **示例 2：** 

```

输入：s = "()[]{}"
输出：true

```
 **示例 3：** 

```

输入：s = "(]"
输出：false

```
 **示例 4：** 

```

输入：s = "([)]"
输出：false

```
 **示例 5：** 

```

输入：s = "{[]}"
输出：true
```
 

 **提示：** 
-  `1 <= s.length <= 10^4` 
-  `s` 仅由括号 `'()[]{}'` 组成
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 21.合并两个有序链表
[https://leetcode-cn.com/problems/merge-two-sorted-lists](https://leetcode-cn.com/problems/merge-two-sorted-lists) 
## 原题
将两个升序链表合并为一个新的 **升序** 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg" style="width: 662px; height: 302px;" />
```

输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]

```
 **示例 2：** 

```

输入：l1 = [], l2 = []
输出：[]

```
 **示例 3：** 

```

输入：l1 = [], l2 = [0]
输出：[0]

```
 

 **提示：** 
- 两个链表的节点数目范围是 `[0, 50]` 
-  `-100 <= Node.val <= 100` 
-  `l1` 和 `l2` 均按 **非递减顺序** 排列
 
**标签**
`递归` `链表` 


## 
```python

```
>
# 22.括号生成
[https://leetcode-cn.com/problems/generate-parentheses](https://leetcode-cn.com/problems/generate-parentheses) 
## 原题
数字 `n` 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 **有效的** 括号组合。

 

 **示例 1：** 

```

输入：n = 3
输出：["((()))","(()())","(())()","()(())","()()()"]

```
 **示例 2：** 

```

输入：n = 1
输出：["()"]

```
 

 **提示：** 
-  `1 <= n <= 8` 
 
**标签**
`字符串` `动态规划` `回溯` 


## 
```python

```
>
# 23.合并K个升序链表
[https://leetcode-cn.com/problems/merge-k-sorted-lists](https://leetcode-cn.com/problems/merge-k-sorted-lists) 
## 原题
给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 

 **示例 1：** 

```
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6

```
 **示例 2：** 

```
输入：lists = []
输出：[]

```
 **示例 3：** 

```
输入：lists = [[]]
输出：[]

```
 

 **提示：** 
-  `k == lists.length` 
-  `0 <= k <= 10^4` 
-  `0 <= lists[i].length <= 500` 
-  `-10^4 <= lists[i][j] <= 10^4` 
-  `lists[i]` 按 **升序** 排列
-  `lists[i].length` 的总和不超过 `10^4` 
 
**标签**
`链表` `分治` `堆（优先队列）` `归并排序` 


## 
```python

```
>
# 24.两两交换链表中的节点
[https://leetcode-cn.com/problems/swap-nodes-in-pairs](https://leetcode-cn.com/problems/swap-nodes-in-pairs) 
## 原题
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/swap_ex1.jpg" style="width: 422px; height: 222px;" />
```

输入：head = [1,2,3,4]
输出：[2,1,4,3]

```
 **示例 2：** 

```

输入：head = []
输出：[]

```
 **示例 3：** 

```

输入：head = [1]
输出：[1]

```
 

 **提示：** 
- 链表中节点的数目在范围 `[0, 100]` 内
-  `0 <= Node.val <= 100` 
 
**标签**
`递归` `链表` 


## 
```python

```
>
# 25.K 个一组翻转链表
[https://leetcode-cn.com/problems/reverse-nodes-in-k-group](https://leetcode-cn.com/problems/reverse-nodes-in-k-group) 
## 原题
给你一个链表，每  *k * 个节点一组进行翻转，请你返回翻转后的链表。

 *k * 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是  *k * 的整数倍，那么请将最后剩余的节点保持原有顺序。

 **进阶：** 
- 你可以设计一个只使用常数额外空间的算法来解决此问题吗？
-  **你不能只是单纯的改变节点内部的值** ，而是需要实际进行节点交换。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex1.jpg" style="width: 542px; height: 222px;" />
```

输入：head = [1,2,3,4,5], k = 2
输出：[2,1,4,3,5]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/03/reverse_ex2.jpg" style="width: 542px; height: 222px;" />
```

输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]

```
 **示例 3：** 

```

输入：head = [1,2,3,4,5], k = 1
输出：[1,2,3,4,5]

```
 **示例 4：** 

```

输入：head = [1], k = 1
输出：[1]

```
 **提示：** 
- 列表中节点的数量在范围 `sz` 内
-  `1 <= sz <= 5000` 
-  `0 <= Node.val <= 1000` 
-  `1 <= k <= sz` 
 
**标签**
`递归` `链表` 


## 
```python

```
>
# 26.删除有序数组中的重复项
[https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array) 
## 原题
给你一个 **升序排列** 的数组 `nums` ，请你 **<a href="http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地</a>** 删除重复出现的元素，使每个元素 **只出现一次** ，返回删除后数组的新长度。元素的 **相对顺序** 应该保持 **一致** 。

由于在某些语言中不能改变数组的长度，所以必须将结果放在数组nums的第一部分。更规范地说，如果在删除重复项之后有 `k` 个元素，那么 `nums` 的前 `k` 个元素应该保存最终结果。

将最终结果插入 `nums` 的前 `k` 个位置后返回 `k` 。

不要使用额外的空间，你必须在 **<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地 </a>修改输入数组** 并在使用 O(1) 额外空间的条件下完成。

 **判题标准:** 

系统会用下面的代码来测试你的题解:

```

int[] nums = [...]; // 输入数组
int[] expectedNums = [...]; // 长度正确的期望答案

int k = removeDuplicates(nums); // 调用

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```
如果所有断言都通过，那么您的题解将被 **通过** 。

 

 **示例 1：** 

```

输入：nums = [1,1,2]
输出：2, nums = [1,2,_]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

```
 **示例 2：** 

```

输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。

```
 

 **提示：** 
-  `0 <= nums.length <= 3 * 10^4` 
-  `-10^4 <= nums[i] <= 10^4` 
-  `nums` 已按 **升序** 排列
 
**标签**
`数组` `双指针` 


## 
```python

```
>
# 27.移除元素
[https://leetcode-cn.com/problems/remove-element](https://leetcode-cn.com/problems/remove-element) 
## 原题
给你一个数组 `nums` * * 和一个值 `val` ，你需要 **<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a>** 移除所有数值等于  `val` * * 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 `O(1)` 额外空间并 **<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地 </a>修改输入数组** 。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

 

 **说明:** 

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以 **「引用」** 方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```

// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

```
 

 **示例 1：** 

```

输入：nums = [3,2,2,3], val = 3
输出：2, nums = [2,2]
解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

```
 **示例 2：** 

```

输入：nums = [0,1,2,2,3,0,4,2], val = 2
输出：5, nums = [0,1,4,0,3]
解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。

```
 

 **提示：** 
-  `0 <= nums.length <= 100` 
-  `0 <= nums[i] <= 50` 
-  `0 <= val <= 100` 
 
**标签**
`数组` `双指针` 


## 
```python

```
>
# 28.实现 strStr()
[https://leetcode-cn.com/problems/implement-strstr](https://leetcode-cn.com/problems/implement-strstr) 
## 原题
实现 <a href="https://baike.baidu.com/item/strstr/811469" target="_blank">strStr()</a> 函数。

给你两个字符串  `haystack` 和 `needle` ，请你在 `haystack` 字符串中找出 `needle` 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  `-1` **** 。

 

 **说明：** 

当  `needle`  是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当  `needle`  是空字符串时我们应当返回 0 。这与 C 语言的 <a href="https://baike.baidu.com/item/strstr/811469" target="_blank">strstr()</a> 以及 Java 的 <a href="https://docs.oracle.com/javase/7/docs/api/java/lang/String.html#indexOf(java.lang.String)" target="_blank">indexOf()</a> 定义相符。

 

 **示例 1：** 

```

输入：haystack = "hello", needle = "ll"
输出：2

```
 **示例 2：** 

```

输入：haystack = "aaaaa", needle = "bba"
输出：-1

```
 **示例 3：** 

```

输入：haystack = "", needle = ""
输出：0

```
 

 **提示：** 
-  `0 <= haystack.length, needle.length <= 5 * 10^4` 
-  `haystack` 和 `needle` 仅由小写英文字符组成
 
**标签**
`双指针` `字符串` `字符串匹配` 


## 
```python

```
>
# 29.两数相除
[https://leetcode-cn.com/problems/divide-two-integers](https://leetcode-cn.com/problems/divide-two-integers) 
## 原题
给定两个整数，被除数 `dividend` 和除数 `divisor` 。将两数相除，要求不使用乘法、除法和 mod 运算符。

返回被除数 `dividend` 除以除数 `divisor` 得到的商。

整数除法的结果应当截去（ `truncate` ）其小数部分，例如： `truncate(8.345) = 8` 以及 `truncate(-2.7335) = -2` 

 

 **示例 1:** 

```
输入: dividend = 10, divisor = 3
输出: 3
解释: 10/3 = truncate(3.33333..) = truncate(3) = 3
```
 **示例 2:** 

```
输入: dividend = 7, divisor = -3
输出: -2
解释: 7/-3 = truncate(-2.33333..) = -2
```
 

 **提示：** 
- 被除数和除数均为 32 位有符号整数。
- 除数不为 0。
- 假设我们的环境只能存储 32 位有符号整数，其数值范围是 [&minus;2^31,  2^31 &minus; 1]。本题中，如果除法结果溢出，则返回 2^31 &minus; 1。
 
**标签**
`位运算` `数学` 


## 
```python

```
>
# 30.串联所有单词的子串
[https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words](https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words) 
## 原题
给定一个字符串  `s` ** ** 和一些 **长度相同** 的单词  `words` **。** 找出 `s` **** 中恰好可以由  `words` **** 中所有单词串联形成的子串的起始位置。

注意子串要与  `words` **** 中的单词完全匹配， **中间不能有其他字符** ，但不需要考虑  `words` ** ** 中单词串联的顺序。

 

 **示例 1：** 

```

输入：s = "barfoothefoobarman", words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。

```
 **示例 2：** 

```

输入：s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]
输出：[]

```
 **示例 3：** 

```

输入：s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]
输出：[6,9,12]

```
 

 **提示：** 
-  `1 <= s.length <= 10^4` 
-  `s` 由小写英文字母组成
-  `1 <= words.length <= 5000` 
-  `1 <= words[i].length <= 30` 
-  `words[i]`  由小写英文字母组成
 
**标签**
`哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
# 31.下一个排列
[https://leetcode-cn.com/problems/next-permutation](https://leetcode-cn.com/problems/next-permutation) 
## 原题
整数数组的一个 **排列** 就是将其所有成员以序列或线性顺序排列。
- 例如， `arr = [1,2,3]` ，以下这些都可以视作 `arr` 的排列： `[1,2,3]` 、 `[1,3,2]` 、 `[3,1,2]` 、 `[2,3,1]` 。
整数数组的 **下一个排列** 是指其整数的下一个字典序更大的排列。更正式地，如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的 **下一个排列** 就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
- 例如， `arr = [1,2,3]` 的下一个排列是 `[1,3,2]` 。
- 类似地， `arr = [2,3,1]` 的下一个排列是 `[3,1,2]` 。
- 而 `arr = [3,2,1]` 的下一个排列是 `[1,2,3]` ，因为 `[3,2,1]` 不存在一个字典序更大的排列。
给你一个整数数组 `nums` ，找出 `nums` 的下一个排列。

必须 **<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地 </a>** 修改，只允许使用额外常数空间。

 

 **示例 1：** 

```

输入：nums = [1,2,3]
输出：[1,3,2]

```
 **示例 2：** 

```

输入：nums = [3,2,1]
输出：[1,2,3]

```
 **示例 3：** 

```

输入：nums = [1,1,5]
输出：[1,5,1]

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `0 <= nums[i] <= 100` 
 
**标签**
`数组` `双指针` 


## 
```python

```
>
# 32.最长有效括号
[https://leetcode-cn.com/problems/longest-valid-parentheses](https://leetcode-cn.com/problems/longest-valid-parentheses) 
## 原题
给你一个只包含 `'('`  和 `')'`  的字符串，找出最长有效（格式正确且连续）括号子串的长度。

 
 **示例 1：** 

```

输入：s = "(()"
输出：2
解释：最长有效括号子串是 "()"

```
 **示例 2：** 

```

输入：s = ")()())"
输出：4
解释：最长有效括号子串是 "()()"

```
 **示例 3：** 

```

输入：s = ""
输出：0

```
 

 **提示：** 
-  `0 <= s.length <= 3 * 10^4` 
-  `s[i]` 为 `'('` 或 `')'` 
 
**标签**
`栈` `字符串` `动态规划` 


## 
```python

```
>
# 33.搜索旋转排序数组
[https://leetcode-cn.com/problems/search-in-rotated-sorted-array](https://leetcode-cn.com/problems/search-in-rotated-sorted-array) 
## 原题
整数数组 `nums` 按升序排列，数组中的值 **互不相同** 。

在传递给函数之前， `nums` 在预先未知的某个下标 `k` （ `0 <= k < nums.length` ）上进行了 **旋转** ，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` （下标 **从 0 开始** 计数）。例如， `[0,1,2,4,5,6,7]` 在下标 `3` 处经旋转后可能变为  `[4,5,6,7,0,1,2]` 。

给你 **旋转后** 的数组 `nums` 和一个整数 `target` ，如果 `nums` 中存在这个目标值 `target` ，则返回它的下标，否则返回  `-1`  。

 

 **示例 1：** 

```

输入：nums = [4,5,6,7,0,1,2], target = 0
输出：4

```
 **示例 2：** 

```

输入：nums = [4,5,6,7,0,1,2], target = 3
输出：-1
```
 **示例 3：** 

```

输入：nums = [1], target = 0
输出：-1

```
 

 **提示：** 
-  `1 <= nums.length <= 5000` 
-  `-10^4 <= nums[i] <= 10^4` 
-  `nums` 中的每个值都 **独一无二** 
- 题目数据保证 `nums` 在预先未知的某个下标上进行了旋转
-  `-10^4 <= target <= 10^4` 
 

 **进阶：** 你可以设计一个时间复杂度为 `O(log n)` 的解决方案吗？

 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 34.在排序数组中查找元素的第一个和最后一个位置
[https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array](https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array) 
## 原题
给定一个按照升序排列的整数数组 `nums` ，和一个目标值 `target` 。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 `target` ，返回  `[-1, -1]` 。

 **进阶：** 
- 你可以设计并实现时间复杂度为  `O(log n)`  的算法解决此问题吗？
 

 **示例 1：** 

```

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
```
 **示例 2：** 

```

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
```
 **示例 3：** 

```

输入：nums = [], target = 0
输出：[-1,-1]
```
 

 **提示：** 
-  `0 <= nums.length <= 10^5` 
-  `-10^9 <= nums[i] <= 10^9` 
-  `nums`  是一个非递减数组
-  `-10^9 <= target <= 10^9` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 35.搜索插入位置
[https://leetcode-cn.com/problems/search-insert-position](https://leetcode-cn.com/problems/search-insert-position) 
## 原题
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 `O(log n)` 的算法。

 

 **示例 1:** 

```

输入: nums = [1,3,5,6], target = 5
输出: 2

```
 **示例 2:** 

```

输入: nums = [1,3,5,6], target = 2
输出: 1

```
 **示例 3:** 

```

输入: nums = [1,3,5,6], target = 7
输出: 4

```
 **示例 4:** 

```

输入: nums = [1,3,5,6], target = 0
输出: 0

```
 **示例 5:** 

```

输入: nums = [1], target = 0
输出: 0

```
 

 **提示:** 
-  `1 <= nums.length <= 10^4` 
-  `-10^4 <= nums[i] <= 10^4` 
-  `nums` 为 **无重复元素** 的 **升序** 排列数组
-  `-10^4 <= target <= 10^4` 
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 36.有效的数独
[https://leetcode-cn.com/problems/valid-sudoku](https://leetcode-cn.com/problems/valid-sudoku) 
## 原题
请你判断一个 `9 x 9` 的数独是否有效。只需要 **根据以下规则** ，验证已经填入的数字是否有效即可。
- 数字 `1-9` 在每一行只能出现一次。
- 数字 `1-9` 在每一列只能出现一次。
- 数字 `1-9` 在每一个以粗实线分隔的 `3x3` 宫内只能出现一次。（请参考示例图）
 

 **注意：** 
- 一个有效的数独（部分已被填充）不一定是可解的。
- 只需要根据以上规则，验证已经填入的数字是否有效即可。
- 空白格用 `'.'` 表示。
 

 **示例 1：** 
<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png" style="height:250px; width:250px" />
```

输入：board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true

```
 **示例 2：** 

```

输入：board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：false
解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
```
 

 **提示：** 
-  `board.length == 9` 
-  `board[i].length == 9` 
-  `board[i][j]` 是一位数字（ `1-9` ）或者 `'.'` 
 
**标签**
`数组` `哈希表` `矩阵` 


## 
```python

```
>
# 37.解数独
[https://leetcode-cn.com/problems/sudoku-solver](https://leetcode-cn.com/problems/sudoku-solver) 
## 原题
编写一个程序，通过填充空格来解决数独问题。

数独的解法需 **遵循如下规则** ：
- 数字  `1-9`  在每一行只能出现一次。
- 数字  `1-9`  在每一列只能出现一次。
- 数字  `1-9`  在每一个以粗实线分隔的  `3x3`  宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用  `'.'`  表示。

 
 **示例：** 
<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714svg.png" style="height:250px; width:250px" />
```

输入：board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
输出：[["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
解释：输入的数独如上图所示，唯一有效的解决方案如下所示：

<img src=" https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2021/04/12/250px-sudoku-by-l2g-20050714_solutionsvg.png" style="height:250px; width:250px" />

```
 

 **提示：** 
-  `board.length == 9` 
-  `board[i].length == 9` 
-  `board[i][j]` 是一位数字或者 `'.'` 
- 题目数据 **保证** 输入数独仅有一个解
 
**标签**
`数组` `回溯` `矩阵` 


## 
```python

```
>
# 38.外观数列
[https://leetcode-cn.com/problems/count-and-say](https://leetcode-cn.com/problems/count-and-say) 
## 原题
给定一个正整数 `n` ，输出外观数列的第 `n` 项。

「外观数列」是一个整数序列，从数字 1 开始，序列中的每一项都是对前一项的描述。

你可以将其视作是由递归公式定义的数字字符串序列：
-  `countAndSay(1) = "1"` 
-  `countAndSay(n)` 是对 `countAndSay(n-1)` 的描述，然后转换成另一个数字字符串。
前五项如下：

```

1.     1
2.     11
3.     21
4.     1211
5.     111221
第一项是数字 1 
描述前一项，这个数是 1 即 “ 一 个 1 ”，记作 "11"
描述前一项，这个数是 11 即 “ 二 个 1 ” ，记作 "21"
描述前一项，这个数是 21 即 “ 一 个 2 + 一 个 1 ” ，记作 "1211"
描述前一项，这个数是 1211 即 “ 一 个 1 + 一 个 2 + 二 个 1 ” ，记作 "111221"

```
要 **描述** 一个数字字符串，首先要将字符串分割为 **最小** 数量的组，每个组都由连续的最多 **相同字符** 组成。然后对于每个组，先描述字符的数量，然后描述字符，形成一个描述组。要将描述转换为数字字符串，先将每组中的字符数量用数字替换，再将所有描述组连接起来。

例如，数字字符串 `"3322251"` 的描述如下图：
<img alt="" src="https://pic.leetcode-cn.com/1629874763-TGmKUh-image.png" style="width: 581px; height: 172px;" />
 

 **示例 1：** 

```

输入：n = 1
输出："1"
解释：这是一个基本样例。

```
 **示例 2：** 

```

输入：n = 4
输出："1211"
解释：
countAndSay(1) = "1"
countAndSay(2) = 读 "1" = 一 个 1 = "11"
countAndSay(3) = 读 "11" = 二 个 1 = "21"
countAndSay(4) = 读 "21" = 一 个 2 + 一 个 1 = "12" + "11" = "1211"

```
 

 **提示：** 
-  `1 <= n <= 30` 
 
**标签**
`字符串` 


## 
```python

```
>
# 39.组合总和
[https://leetcode-cn.com/problems/combination-sum](https://leetcode-cn.com/problems/combination-sum) 
## 原题
给你一个 **无重复元素** 的整数数组 `candidates` 和一个目标整数 `target` ，找出 `candidates` 中可以使数字和为目标数 `target` 的 *所有* **不同组合** ，并以列表形式返回。你可以按 **任意顺序** 返回这些组合。

 `candidates` 中的 **同一个** 数字可以 **无限制重复被选取** 。如果至少一个数字的被选数量不同，则两种组合是不同的。 

对于给定的输入，保证和为 `target` 的不同组合数少于 `150` 个。

 

 **示例 1：** 

```

输入：candidates = [2,3,6,7], target = 7
输出：[[2,2,3],[7]]
解释：
2 和 3 可以形成一组候选，2 + 2 + 3 = 7 。注意 2 可以使用多次。
7 也是一个候选， 7 = 7 。
仅有这两种组合。
```
 **示例 2：** 

```

输入: candidates = [2,3,5], target = 8
输出: [[2,2,2,2],[2,3,3],[3,5]]
```
 **示例 3：** 

```

输入: candidates = [2], target = 1
输出: []

```
 

 **提示：** 
-  `1 <= candidates.length <= 30` 
-  `1 <= candidates[i] <= 200` 
-  `candidate` 中的每个元素都 **互不相同** 
-  `1 <= target <= 500` 
 
**标签**
`数组` `回溯` 


## 
```python

```
>
# 40.组合总和 II
[https://leetcode-cn.com/problems/combination-sum-ii](https://leetcode-cn.com/problems/combination-sum-ii) 
## 原题
给定一个候选人编号的集合 `candidates` 和一个目标数 `target` ，找出 `candidates` 中所有可以使数字和为 `target` 的组合。

 `candidates` 中的每个数字在每个组合中只能使用 **一次** 。

 **注意：** 解集不能包含重复的组合。 

 

 **示例 1:** 

```

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
```
 **示例 2:** 

```

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
```
 

 **提示:** 
-  `1 <= candidates.length <= 100` 
-  `1 <= candidates[i] <= 50` 
-  `1 <= target <= 30` 
 
**标签**
`数组` `回溯` 


## 
```python

```
>
# 41.缺失的第一个正数
[https://leetcode-cn.com/problems/first-missing-positive](https://leetcode-cn.com/problems/first-missing-positive) 
## 原题
给你一个未排序的整数数组 `nums` ，请你找出其中没有出现的最小的正整数。
请你实现时间复杂度为 `O(n)` 并且只使用常数级别额外空间的解决方案。

 

 **示例 1：** 

```

输入：nums = [1,2,0]
输出：3

```
 **示例 2：** 

```

输入：nums = [3,4,-1,1]
输出：2

```
 **示例 3：** 

```

输入：nums = [7,8,9,11,12]
输出：1

```
 

 **提示：** 
-  `1 <= nums.length <= 5 * 10^5` 
-  `-2^31 <= nums[i] <= 2^31 - 1` 
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 42.接雨水
[https://leetcode-cn.com/problems/trapping-rain-water](https://leetcode-cn.com/problems/trapping-rain-water) 
## 原题
给定 `n` 个非负整数表示每个宽度为 `1` 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

 **示例 1：** 

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png" style="height: 161px; width: 412px;" />

```

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 

```
 **示例 2：** 

```

输入：height = [4,2,0,3,2,5]
输出：9

```
 

 **提示：** 
-  `n == height.length` 
-  `1 <= n <= 2 * 10^4` 
-  `0 <= height[i] <= 10^5` 
 
**标签**
`栈` `数组` `双指针` `动态规划` `单调栈` 


## 
```python

```
>
# 43.字符串相乘
[https://leetcode-cn.com/problems/multiply-strings](https://leetcode-cn.com/problems/multiply-strings) 
## 原题
给定两个以字符串形式表示的非负整数 `num1` 和 `num2` ，返回 `num1` 和 `num2` 的乘积，它们的乘积也表示为字符串形式。

 **注意：** 不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

 

 **示例 1:** 

```

输入: num1 = "2", num2 = "3"
输出: "6"
```
 **示例 2:** 

```

输入: num1 = "123", num2 = "456"
输出: "56088"
```
 

 **提示：** 
-  `1 <= num1.length, num2.length <= 200` 
-  `num1` 和 `num2` 只能由数字组成。
-  `num1` 和 `num2` 都不包含任何前导零，除了数字0本身。
 
**标签**
`数学` `字符串` `模拟` 


## 
```python

```
>
# 44.通配符匹配
[https://leetcode-cn.com/problems/wildcard-matching](https://leetcode-cn.com/problems/wildcard-matching) 
## 原题
给定一个字符串 ( `s` ) 和一个字符模式 ( `p` ) ，实现一个支持 `';?';` 和 `';*';` 的通配符匹配。

```
';?'; 可以匹配任何单个字符。
';*'; 可以匹配任意字符串（包括空字符串）。

```
两个字符串 **完全匹配** 才算匹配成功。

 **说明:** 
-  `s` 可能为空，且只包含从 `a-z` 的小写字母。
-  `p` 可能为空，且只包含从 `a-z` 的小写字母，以及字符 `?` 和 `*` 。
 **示例 1:** 

```
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
```
 **示例 2:** 

```
输入:
s = "aa"
p = "*"
输出: true
解释: ';*'; 可以匹配任意字符串。

```
 **示例 3:** 

```
输入:
s = "cb"
p = "?a"
输出: false
解释: ';?'; 可以匹配 ';c';, 但第二个 ';a'; 无法匹配 ';b';。

```
 **示例 4:** 

```
输入:
s = "adceb"
p = "*a*b"
输出: true
解释: 第一个 ';*'; 可以匹配空字符串, 第二个 ';*'; 可以匹配字符串 "dce".

```
 **示例 5:** 

```
输入:
s = "acdcb"
p = "a*c?b"
输出: false
```
 
**标签**
`贪心` `递归` `字符串` `动态规划` 


## 
```python

```
>
# 45.跳跃游戏 II
[https://leetcode-cn.com/problems/jump-game-ii](https://leetcode-cn.com/problems/jump-game-ii) 
## 原题
给你一个非负整数数组  `nums` ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

 

 **示例 1:** 

```

输入: nums = [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。

```
 **示例 2:** 

```

输入: nums = [2,3,0,1,4]
输出: 2

```
 

 **提示:** 
-  `1 <= nums.length <= 10^4` 
-  `0 <= nums[i] <= 1000` 
 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 46.全排列
[https://leetcode-cn.com/problems/permutations](https://leetcode-cn.com/problems/permutations) 
## 原题
给定一个不含重复数字的数组 `nums` ，返回其 *所有可能的全排列* 。你可以 **按任意顺序** 返回答案。

 

 **示例 1：** 

```

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```
 **示例 2：** 

```

输入：nums = [0,1]
输出：[[0,1],[1,0]]

```
 **示例 3：** 

```

输入：nums = [1]
输出：[[1]]

```
 

 **提示：** 
-  `1 <= nums.length <= 6` 
-  `-10 <= nums[i] <= 10` 
-  `nums` 中的所有整数 **互不相同** 
 
**标签**
`数组` `回溯` 


## 
```python

```
>
# 47.全排列 II
[https://leetcode-cn.com/problems/permutations-ii](https://leetcode-cn.com/problems/permutations-ii) 
## 原题
给定一个可包含重复数字的序列 `nums` ， ***按任意顺序*** 返回所有不重复的全排列。

 

 **示例 1：** 

```

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]

```
 **示例 2：** 

```

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

```
 

 **提示：** 
-  `1 <= nums.length <= 8` 
-  `-10 <= nums[i] <= 10` 
 
**标签**
`数组` `回溯` 


## 
```python

```
>
# 48.旋转图像
[https://leetcode-cn.com/problems/rotate-image](https://leetcode-cn.com/problems/rotate-image) 
## 原题
给定一个 *n* × *n* 的二维矩阵 `matrix` 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 **<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地</a>** 旋转图像，这意味着你需要直接修改输入的二维矩阵。 **请不要** 使用另一个矩阵来旋转图像。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat1.jpg" style="height: 188px; width: 500px;" />
```

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/28/mat2.jpg" style="height: 201px; width: 500px;" />
```

输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

```
 

 **提示：** 
-  `n == matrix.length == matrix[i].length` 
-  `1 <= n <= 20` 
-  `-1000 <= matrix[i][j] <= 1000` 
 

 
**标签**
`数组` `数学` `矩阵` 


## 
```python

```
>
# 49.字母异位词分组
[https://leetcode-cn.com/problems/group-anagrams](https://leetcode-cn.com/problems/group-anagrams) 
## 原题
给你一个字符串数组，请你将 **字母异位词** 组合在一起。可以按任意顺序返回结果列表。

 **字母异位词** 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

 

 **示例 1:** 

```

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
```
 **示例 2:** 

```

输入: strs = [""]
输出: [[""]]

```
 **示例 3:** 

```

输入: strs = ["a"]
输出: [["a"]]
```
 

 **提示：** 
-  `1 <= strs.length <= 10^4` 
-  `0 <= strs[i].length <= 100` 
-  `strs[i]` 仅包含小写字母
 
**标签**
`哈希表` `字符串` `排序` 


## 
```python

```
>
# 50.Pow(x, n)
[https://leetcode-cn.com/problems/powx-n](https://leetcode-cn.com/problems/powx-n) 
## 原题
实现 <a href="https://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow( *x* , *n* )</a> ，即计算 `x` 的 `n` 次幂函数（即， `x^n` ^<span style="font-size:10.8333px"> </span>）。

 

 **示例 1：** 

```

输入：x = 2.00000, n = 10
输出：1024.00000

```
 **示例 2：** 

```

输入：x = 2.10000, n = 3
输出：9.26100

```
 **示例 3：** 

```

输入：x = 2.00000, n = -2
输出：0.25000
解释：2^-2 = 1/2^2 = 1/4 = 0.25

```
 

 **提示：** 
-  `-100.0 < x < 100.0` 
-  `-2^31 <= n <= 2^31-1` 
-  `-10^4 <= x^n <= 10^4` 
 
**标签**
`递归` `数学` 


## 
```python

```
>
# 51.N 皇后
[https://leetcode-cn.com/problems/n-queens](https://leetcode-cn.com/problems/n-queens) 
## 原题
 **n 皇后问题** 研究的是如何将 `n` 个皇后放置在 `n×n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回所有不同的 **n皇后问题** 的解决方案。
每一种解法包含一个不同的 **n 皇后问题** 的棋子放置方案，该方案中 `'Q'` 和 `'.'` 分别代表了皇后和空位。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" />
```

输入：n = 4
输出：[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
解释：如上图所示，4 皇后问题存在两个不同的解法。

```
 **示例 2：** 

```

输入：n = 1
输出：[["Q"]]

```
 

 **提示：** 
-  `1 <= n <= 9` 
 
**标签**
`数组` `回溯` 


## 
```python

```
>
# 52.N皇后 II
[https://leetcode-cn.com/problems/n-queens-ii](https://leetcode-cn.com/problems/n-queens-ii) 
## 原题
 **n 皇后问题** 研究的是如何将 `n` 个皇后放置在 `n × n` 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 `n` ，返回 **n 皇后问题** 不同的解决方案的数量。

 
 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/queens.jpg" style="width: 600px; height: 268px;" />
```

输入：n = 4
输出：2
解释：如上图所示，4 皇后问题存在两个不同的解法。

```
 **示例 2：** 

```

输入：n = 1
输出：1

```
 

 **提示：** 
-  `1 <= n <= 9` 
 
**标签**
`回溯` 


## 
```python

```
>
# 53.最大子数组和
[https://leetcode-cn.com/problems/maximum-subarray](https://leetcode-cn.com/problems/maximum-subarray) 
## 原题
给你一个整数数组 `nums` ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 **子数组** 是数组中的一个连续部分。

 

 **示例 1：** 

```

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

```
 **示例 2：** 

```

输入：nums = [1]
输出：1

```
 **示例 3：** 

```

输入：nums = [5,4,-1,7,8]
输出：23

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `-10^4 <= nums[i] <= 10^4` 
 

 **进阶：** 如果你已经实现复杂度为 `O(n)` 的解法，尝试使用更为精妙的 **分治法** 求解。

 
**标签**
`数组` `分治` `动态规划` 


## 
```python

```
>
# 54.螺旋矩阵
[https://leetcode-cn.com/problems/spiral-matrix](https://leetcode-cn.com/problems/spiral-matrix) 
## 原题
给你一个 `m` 行 `n` 列的矩阵  `matrix` ，请按照 **顺时针螺旋顺序** ，返回矩阵中的所有元素。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg" style="width: 242px; height: 242px;" />
```

输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg" style="width: 322px; height: 242px;" />
```

输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]

```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m, n <= 10` 
-  `-100 <= matrix[i][j] <= 100` 
 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 55.跳跃游戏
[https://leetcode-cn.com/problems/jump-game](https://leetcode-cn.com/problems/jump-game) 
## 原题
给定一个非负整数数组  `nums` ，你最初位于数组的 **第一个下标** 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

 

 **示例 1：** 

```

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

```
 **示例 2：** 

```

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。

```
 

 **提示：** 
-  `1 <= nums.length <= 3 * 10^4` 
-  `0 <= nums[i] <= 10^5` 
 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 56.合并区间
[https://leetcode-cn.com/problems/merge-intervals](https://leetcode-cn.com/problems/merge-intervals) 
## 原题
以数组 `intervals` 表示若干个区间的集合，其中单个区间为 `intervals[i] = [start<sub>i</sub>, end<sub>i</sub>]` 。请你合并所有重叠的区间，并返回 *一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间* 。

 

 **示例 1：** 

```

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

```
 **示例 2：** 

```

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
```
 

 **提示：** 
-  `1 <= intervals.length <= 10^4` 
-  `intervals[i].length == 2` 
-  `0 <= start<sub>i</sub> <= end<sub>i</sub> <= 10^4` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 57.插入区间
[https://leetcode-cn.com/problems/insert-interval](https://leetcode-cn.com/problems/insert-interval) 
## 原题
给你一个 **无重叠的** *，* 按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

 **示例 1：** 

```

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]

```
 **示例 2：** 

```

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
```
 **示例 3：** 

```

输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]

```
 **示例 4：** 

```

输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]

```
 **示例 5：** 

```

输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]

```
 

 **提示：** 
-  `0 <= intervals.length <= 10^4` 
-  `intervals[i].length == 2` 
-  `0 <= intervals[i][0] <= intervals[i][1] <= 10^5` 
-  `intervals` 根据 `intervals[i][0]` 按 **升序** 排列
-  `newInterval.length == 2` 
-  `0 <= newInterval[0] <= newInterval[1] <= 10^5` 
 
**标签**
`数组` 


## 
```python

```
>
# 58.最后一个单词的长度
[https://leetcode-cn.com/problems/length-of-last-word](https://leetcode-cn.com/problems/length-of-last-word) 
## 原题
给你一个字符串 `s` ，由若干单词组成，单词前后用一些空格字符隔开。返回字符串中最后一个单词的长度。

 **单词** 是指仅由字母组成、不包含任何空格字符的最大子字符串。

 

 **示例 1：** 

```

输入：s = "Hello World"
输出：5

```
 **示例 2：** 

```

输入：s = "   fly me   to   the moon  "
输出：4

```
 **示例 3：** 

```

输入：s = "luffy is still joyboy"
输出：6

```
 

 **提示：** 
-  `1 <= s.length <= 10^4` 
-  `s` 仅有英文字母和空格 `' '` 组成
-  `s` 中至少存在一个单词
 
**标签**
`字符串` 


## 
```python

```
>
# 59.螺旋矩阵 II
[https://leetcode-cn.com/problems/spiral-matrix-ii](https://leetcode-cn.com/problems/spiral-matrix-ii) 
## 原题
给你一个正整数  `n` ，生成一个包含 `1` 到  `n^2`  所有元素，且元素按顺时针顺序螺旋排列的  `n x n` 正方形矩阵 `matrix` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/spiraln.jpg" style="width: 242px; height: 242px;" />
```

输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]

```
 **示例 2：** 

```

输入：n = 1
输出：[[1]]

```
 

 **提示：** 
-  `1 <= n <= 20` 
 
**标签**
`数组` `矩阵` `模拟` 


## 
```python

```
>
# 60.排列序列
[https://leetcode-cn.com/problems/permutation-sequence](https://leetcode-cn.com/problems/permutation-sequence) 
## 原题
给出集合  `[1,2,3,...,n]` ，其所有元素共有  `n!` 种排列。

按大小顺序列出所有排列情况，并一一标记，当  `n = 3` 时, 所有排列如下：
-  `"123"` 
-  `"132"` 
-  `"213"` 
-  `"231"` 
-  `"312"` 
-  `"321"` 
给定  `n` 和  `k` ，返回第  `k`  个排列。

 

 **示例 1：** 

```

输入：n = 3, k = 3
输出："213"

```
 **示例 2：** 

```

输入：n = 4, k = 9
输出："2314"

```
 **示例 3：** 

```

输入：n = 3, k = 1
输出："123"

```
 

 **提示：** 
-  `1 <= n <= 9` 
-  `1 <= k <= n!` 
 
**标签**
`递归` `数学` 


## 
```python

```
>
# 61.旋转链表
[https://leetcode-cn.com/problems/rotate-list](https://leetcode-cn.com/problems/rotate-list) 
## 原题
给你一个链表的头节点 `head` ，旋转链表，将链表每个节点向右移动  `k` * * 个位置。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/rotate1.jpg" style="width: 600px; height: 254px;" />
```

输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/13/roate2.jpg" style="width: 472px; height: 542px;" />
```

输入：head = [0,1,2], k = 4
输出：[2,0,1]

```
 

 **提示：** 
- 链表中节点的数目在范围 `[0, 500]` 内
-  `-100 <= Node.val <= 100` 
-  `0 <= k <= 2 * 10^9` 
 
**标签**
`链表` `双指针` 


## 
```python

```
>
# 62.不同路径
[https://leetcode-cn.com/problems/unique-paths](https://leetcode-cn.com/problems/unique-paths) 
## 原题
一个机器人位于一个 `m x n` * * 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

 **示例 1：** 
<img src="https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png" />
```

输入：m = 3, n = 7
输出：28
```
 **示例 2：** 

```

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下

```
 **示例 3：** 

```

输入：m = 7, n = 3
输出：28

```
 **示例 4：** 

```

输入：m = 3, n = 3
输出：6
```
 

 **提示：** 
-  `1 <= m, n <= 100` 
- 题目数据保证答案小于等于 `2 * 10^9` 
 
**标签**
`数学` `动态规划` `组合数学` 


## 
```python

```
>
# 63.不同路径 II
[https://leetcode-cn.com/problems/unique-paths-ii](https://leetcode-cn.com/problems/unique-paths-ii) 
## 原题
一个机器人位于一个<meta charset="UTF-8" /> `m x n` 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？

网格中的障碍物和空位置分别用 `1` 和 `0` 来表示。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot1.jpg" />
```

输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/robot2.jpg" />
```

输入：obstacleGrid = [[0,1],[0,0]]
输出：1

```
 

 **提示：** 
-  `m == obstacleGrid.length` 
-  `n == obstacleGrid[i].length` 
-  `1 <= m, n <= 100` 
-  `obstacleGrid[i][j]` 为 `0` 或 `1` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 64.最小路径和
[https://leetcode-cn.com/problems/minimum-path-sum](https://leetcode-cn.com/problems/minimum-path-sum) 
## 原题
给定一个包含非负整数的 ` *m*  x  *n* `  网格  `grid` ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

 **说明：** 每次只能向下或者向右移动一步。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/05/minpath.jpg" style="width: 242px; height: 242px;" />
```

输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。

```
 **示例 2：** 

```

输入：grid = [[1,2,3],[4,5,6]]
输出：12

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 200` 
-  `0 <= grid[i][j] <= 100` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 65.有效数字
[https://leetcode-cn.com/problems/valid-number](https://leetcode-cn.com/problems/valid-number) 
## 原题
 **有效数字** （按顺序）可以分成以下几个部分：
- 一个 **小数** 或者 **整数** 
- （可选）一个 `'e'` 或 `'E'` ，后面跟着一个 **整数** 
 **小数** （按顺序）可以分成以下几个部分：
- （可选）一个符号字符（ `'+'` 或 `'-'` ）
- 下述格式之一：
	
- 至少一位数字，后面跟着一个点 `'.'` 
- 至少一位数字，后面跟着一个点 `'.'` ，后面再跟着至少一位数字
- 一个点 `'.'` ，后面跟着至少一位数字
	
	
 **整数** （按顺序）可以分成以下几个部分：
- （可选）一个符号字符（ `'+'` 或 `'-'` ）
- 至少一位数字
部分有效数字列举如下： `["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]` 

部分无效数字列举如下： `["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]` 

给你一个字符串 `s` ，如果 `s` 是一个 **有效数字** ，请返回 `true` 。

 

 **示例 1：** 

```

输入：s = "0"
输出：true

```
 **示例 2：** 

```

输入：s = "e"
输出：false

```
 **示例 3：** 

```

输入：s = "."
输出：false

```
 

 **提示：** 
-  `1 <= s.length <= 20` 
-  `s` 仅含英文字母（大写和小写），数字（ `0-9` ），加号 `'+'` ，减号 `'-'` ，或者点 `'.'` 。
 
**标签**
`字符串` 


## 
```python

```
>
# 66.加一
[https://leetcode-cn.com/problems/plus-one](https://leetcode-cn.com/problems/plus-one) 
## 原题
给定一个由 **整数** 组成的 **非空** 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储 **单个** 数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

 **示例 1：** 

```

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。

```
 **示例 2：** 

```

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。

```
 **示例 3：** 

```

输入：digits = [0]
输出：[1]

```
 

 **提示：** 
-  `1 <= digits.length <= 100` 
-  `0 <= digits[i] <= 9` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 67.二进制求和
[https://leetcode-cn.com/problems/add-binary](https://leetcode-cn.com/problems/add-binary) 
## 原题
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 **非空** 字符串且只包含数字 `1` 和 `0` 。

 

 **示例 1:** 

```
输入: a = "11", b = "1"
输出: "100"
```
 **示例 2:** 

```
输入: a = "1010", b = "1011"
输出: "10101"
```
 

 **提示：** 
- 每个字符串仅由字符 `';0';` 或 `';1';` 组成。
-  `1 <= a.length, b.length <= 10^4` 
- 字符串如果不是 `"0"` ，就都不含前导零。
 
**标签**
`位运算` `数学` `字符串` `模拟` 


## 
```python

```
>
# 68.文本左右对齐
[https://leetcode-cn.com/problems/text-justification](https://leetcode-cn.com/problems/text-justification) 
## 原题
给定一个单词数组 `words` 和一个长度 `maxWidth` ，重新排版单词，使其成为每行恰好有 `maxWidth` 个字符，且左右两端对齐的文本。

你应该使用 “ **贪心算法** ” 来放置给定的单词；也就是说，尽可能多地往每行中放置单词。必要时可用空格 `' '` 填充，使得每行恰好有 *maxWidth* 个字符。

要求尽可能均匀分配单词间的空格数量。如果某一行单词间的空格不能均匀分配，则左侧放置的空格数要多于右侧的空格数。

文本的最后一行应为左对齐，且单词之间不插入 **额外的** 空格。

 **注意:** 
- 单词是指由非空格字符组成的字符序列。
- 每个单词的长度大于 0，小于等于 *maxWidth* 。
- 输入单词数组 `words` 至少包含一个单词。
 

 **示例 1:** 

```

输入: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16
输出:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

```
 **示例 2:** 

```

输入:words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
输出:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
解释: 注意最后一行的格式应为 "shall be    " 而不是 "shall     be",
     因为最后一行应为左对齐，而不是左右两端对齐。       
     第二行同样为左对齐，这是因为这行只包含一个单词。

```
 **示例 3:** 

```

输入:words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]，maxWidth = 20
输出:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

```
 

 **提示:** 
-  `1 <= words.length <= 300` 
-  `1 <= words[i].length <= 20` 
-  `words[i]` 由小写英文字母和符号组成
-  `1 <= maxWidth <= 100` 
-  `words[i].length <= maxWidth` 
 
**标签**
`字符串` `模拟` 


## 
```python

```
>
# 69.x 的平方根 
[https://leetcode-cn.com/problems/sqrtx](https://leetcode-cn.com/problems/sqrtx) 
## 原题
给你一个非负整数 `x` ，计算并返回 `x` 的 **算术平方根** 。

由于返回类型是整数，结果只保留 **整数部分** ，小数部分将被 **舍去 。** 

 **注意：** 不允许使用任何内置指数函数和算符，例如 `pow(x, 0.5)` 或者 `x ** 0.5` 。

 

 **示例 1：** 

```

输入：x = 4
输出：2

```
 **示例 2：** 

```

输入：x = 8
输出：2
解释：8 的算术平方根是 2.82842..., 由于返回类型是整数，小数部分将被舍去。

```
 

 **提示：** 
-  `0 <= x <= 2^31 - 1` 
 
**标签**
`数学` `二分查找` 


## 
```python

```
>
# 70.爬楼梯
[https://leetcode-cn.com/problems/climbing-stairs](https://leetcode-cn.com/problems/climbing-stairs) 
## 原题
假设你正在爬楼梯。需要 `n` 阶你才能到达楼顶。

每次你可以爬 `1` 或 `2` 个台阶。你有多少种不同的方法可以爬到楼顶呢？

 

 **示例 1：** 

```

输入：n = 2
输出：2
解释：有两种方法可以爬到楼顶。
1. 1 阶 + 1 阶
2. 2 阶
```
 **示例 2：** 

```

输入：n = 3
输出：3
解释：有三种方法可以爬到楼顶。
1. 1 阶 + 1 阶 + 1 阶
2. 1 阶 + 2 阶
3. 2 阶 + 1 阶

```
 

 **提示：** 
-  `1 <= n <= 45` 
 
**标签**
`记忆化搜索` `数学` `动态规划` 


## 
```python

```
>
# 71.简化路径
[https://leetcode-cn.com/problems/simplify-path](https://leetcode-cn.com/problems/simplify-path) 
## 原题
给你一个字符串 `path` ，表示指向某一文件或目录的 Unix 风格 **绝对路径** （以 `'/'` 开头），请你将其转化为更加简洁的规范路径。

<p class="MachineTrans-lang-zh-CN">在 Unix 风格的文件系统中，一个点（ `.` ）表示当前目录本身；此外，两个点 （ `..` ） 表示将目录切换到上一级（指向父目录）；两者都可以是复杂相对路径的组成部分。任意多个连续的斜杠（即， `'//'` ）都被视为单个斜杠 `'/'` 。 对于此问题，任何其他格式的点（例如， `'...'` ）均被视为文件/目录名称。

请注意，返回的 **规范路径** 必须遵循下述格式：
- 始终以斜杠 `'/'` 开头。
- 两个目录名之间必须只有一个斜杠 `'/'` 。
- 最后一个目录名（如果存在） **不能** 以 `'/'` 结尾。
- 此外，路径仅包含从根目录到目标文件或目录的路径上的目录（即，不含 `'.'` 或 `'..'` ）。
返回简化后得到的 **规范路径** 。

 

 **示例 1：** 

```

输入：path = "/home/"
输出："/home"
解释：注意，最后一个目录名后面没有斜杠。 
```
 **示例 2：** 

```

输入：path = "/../"
输出："/"
解释：从根目录向上一级是不可行的，因为根目录是你可以到达的最高级。

```
 **示例 3：** 

```

输入：path = "/home//foo/"
输出："/home/foo"
解释：在规范路径中，多个连续斜杠需要用一个斜杠替换。

```
 **示例 4：** 

```

输入：path = "/a/./b/../../c/"
输出："/c"

```
 

 **提示：** 
-  `1 <= path.length <= 3000` 
-  `path` 由英文字母，数字， `'.'` ， `'/'` 或 `'_'` 组成。
-  `path` 是一个有效的 Unix 风格绝对路径。
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 72.编辑距离
[https://leetcode-cn.com/problems/edit-distance](https://leetcode-cn.com/problems/edit-distance) 
## 原题
给你两个单词 `word1` 和 `word2` ， *请返回将 `word1` 转换成 `word2` 所使用的最少操作数* 。

你可以对一个单词进行如下三种操作：
- 插入一个字符
- 删除一个字符
- 替换一个字符
 

 **示例 1：** 

```

输入：word1 = "horse", word2 = "ros"
输出：3
解释：
horse -> rorse (将 'h' 替换为 'r')
rorse -> rose (删除 'r')
rose -> ros (删除 'e')

```
 **示例 2：** 

```

输入：word1 = "intention", word2 = "execution"
输出：5
解释：
intention -> inention (删除 't')
inention -> enention (将 'i' 替换为 'e')
enention -> exention (将 'n' 替换为 'x')
exention -> exection (将 'n' 替换为 'c')
exection -> execution (插入 'u')

```
 

 **提示：** 
-  `0 <= word1.length, word2.length <= 500` 
-  `word1` 和 `word2` 由小写英文字母组成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 73.矩阵置零
[https://leetcode-cn.com/problems/set-matrix-zeroes](https://leetcode-cn.com/problems/set-matrix-zeroes) 
## 原题
给定一个 ` *m* x *n* ` 的矩阵，如果一个元素为 **0** ，则将其所在行和列的所有元素都设为 **0** 。请使用 **<a href="http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a>** 算法 **。** 
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg" style="width: 450px; height: 169px;" />
```

输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg" style="width: 450px; height: 137px;" />
```

输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]

```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[0].length` 
-  `1 <= m, n <= 200` 
-  `-2^31 <= matrix[i][j] <= 2^31 - 1` 
 

 **进阶：** 
- 一个直观的解决方案是使用 `O( *m* *n* )` 的额外空间，但这并不是一个好的解决方案。
- 一个简单的改进方案是使用 `O( *m* + *n* )` 的额外空间，但这仍然不是最好的解决方案。
- 你能想出一个仅使用常量空间的解决方案吗？
 
**标签**
`数组` `哈希表` `矩阵` 


## 
```python

```
>
# 74.搜索二维矩阵
[https://leetcode-cn.com/problems/search-a-2d-matrix](https://leetcode-cn.com/problems/search-a-2d-matrix) 
## 原题
编写一个高效的算法来判断  `m x n`  矩阵中，是否存在一个目标值。该矩阵具有如下特性：
- 每行中的整数从左到右按升序排列。
- 每行的第一个整数大于前一行的最后一个整数。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/mat.jpg" style="width: 322px; height: 242px;" />
```

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/25/mat2.jpg" style="width: 322px; height: 242px;" />
```

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false

```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m, n <= 100` 
-  `-10^4 <= matrix[i][j], target <= 10^4` 
 
**标签**
`数组` `二分查找` `矩阵` 


## 
```python

```
>
# 75.颜色分类
[https://leetcode-cn.com/problems/sort-colors](https://leetcode-cn.com/problems/sort-colors) 
## 原题
给定一个包含红色、白色和蓝色、共 `n` 个元素的数组<meta charset="UTF-8" /> `nums` ， **<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地</a>** 对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

我们使用整数 `0` 、 `1` 和 `2` 分别表示红色、白色和蓝色。
必须在不使用库的sort函数的情况下解决这个问题。

 

 **示例 1：** 

```

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

```
 **示例 2：** 

```

输入：nums = [2,0,1]
输出：[0,1,2]

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 300` 
-  `nums[i]` 为 `0` 、 `1` 或 `2` 
 

 **进阶：** 
- 你可以不使用代码库中的排序函数来解决这道题吗？
- 你能想出一个仅使用常数空间的一趟扫描算法吗？
 
**标签**
`数组` `双指针` `排序` 


## 
```python

```
>
# 76.最小覆盖子串
[https://leetcode-cn.com/problems/minimum-window-substring](https://leetcode-cn.com/problems/minimum-window-substring) 
## 原题
给你一个字符串 `s` 、一个字符串 `t` 。返回 `s` 中涵盖 `t` 所有字符的最小子串。如果 `s` 中不存在涵盖 `t` 所有字符的子串，则返回空字符串 `""` 。

 

 **注意：** 
- 对于 `t` 中重复字符，我们寻找的子字符串中该字符数量必须不少于 `t` 中该字符数量。
- 如果 `s` 中存在这样的子串，我们保证它是唯一的答案。
 

 **示例 1：** 

```

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"

```
 **示例 2：** 

```

输入：s = "a", t = "a"
输出："a"

```
 **示例 3:** 

```

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
```
 

 **提示：** 
-  `1 <= s.length, t.length <= 10^5` 
-  `s` 和 `t` 由英文字母组成
 
 **进阶：** 你能设计一个在 `o(n)` 时间内解决此问题的算法吗？
 
**标签**
`哈希表` `字符串` `滑动窗口` 


## 
```python

```
>
# 77.组合
[https://leetcode-cn.com/problems/combinations](https://leetcode-cn.com/problems/combinations) 
## 原题
给定两个整数 `n` 和 `k` ，返回范围 `[1, n]` 中所有可能的 `k` 个数的组合。

你可以按 **任何顺序** 返回答案。

 

 **示例 1：** 

```

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```
 **示例 2：** 

```

输入：n = 1, k = 1
输出：[[1]]
```
 

 **提示：** 
-  `1 <= n <= 20` 
-  `1 <= k <= n` 
 
**标签**
`数组` `回溯` 


## 
```python

```
>
# 78.子集
[https://leetcode-cn.com/problems/subsets](https://leetcode-cn.com/problems/subsets) 
## 原题
给你一个整数数组  `nums` ，数组中的元素 **互不相同** 。返回该数组所有可能的子集（幂集）。

解集 **不能** 包含重复的子集。你可以按 **任意顺序** 返回解集。

 

 **示例 1：** 

```

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

```
 **示例 2：** 

```

输入：nums = [0]
输出：[[],[0]]

```
 

 **提示：** 
-  `1 <= nums.length <= 10` 
-  `-10 <= nums[i] <= 10` 
-  `nums` 中的所有元素 **互不相同** 
 
**标签**
`位运算` `数组` `回溯` 


## 
```python

```
>
# 79.单词搜索
[https://leetcode-cn.com/problems/word-search](https://leetcode-cn.com/problems/word-search) 
## 原题
给定一个  `m x n` 二维字符网格  `board` 和一个字符串单词  `word` 。如果  `word` 存在于网格中，返回 `true` ；否则，返回 `false` 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word2.jpg" style="width: 322px; height: 242px;" />
```

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg" style="width: 322px; height: 242px;" />
```

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/word3.jpg" style="width: 322px; height: 242px;" />
```

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false

```
 

 **提示：** 
-  `m == board.length` 
-  `n = board[i].length` 
-  `1 <= m, n <= 6` 
-  `1 <= word.length <= 15` 
-  `board` 和 `word` 仅由大小写英文字母组成
 

 **进阶：** 你可以使用搜索剪枝的技术来优化解决方案，使其在 `board` 更大的情况下可以更快解决问题？

 
**标签**
`数组` `回溯` `矩阵` 


## 
```python

```
>
# 80.删除有序数组中的重复项 II
[https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii) 
## 原题
给你一个有序数组 `nums` ，请你 **<a href="http://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank"> 原地</a>** 删除重复出现的元素，使每个元素 **最多出现两次** ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 **<a href="https://baike.baidu.com/item/%E5%8E%9F%E5%9C%B0%E7%AE%97%E6%B3%95" target="_blank">原地 </a>修改输入数组** 并在使用 O(1) 额外空间的条件下完成。

 

 **说明：** 

为什么返回数值是整数，但输出的答案是数组呢？

请注意，输入数组是以 **「引用」** 方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

```
 

 **示例 1：** 

```

输入：nums = [1,1,1,2,2,3]
输出：5, nums = [1,1,2,2,3]
解释：函数应返回新长度 length = 5, 并且原数组的前五个元素被修改为 1, 1, 2, 2, 3 。 不需要考虑数组中超出新长度后面的元素。

```
 **示例 2：** 

```

输入：nums = [0,0,1,1,1,1,2,3,3]
输出：7, nums = [0,0,1,1,2,3,3]
解释：函数应返回新长度 length = 7, 并且原数组的前五个元素被修改为 0, 0, 1, 1, 2, 3, 3 。 不需要考虑数组中超出新长度后面的元素。

```
 

 **提示：** 
-  `1 <= nums.length <= 3 * 10^4` 
-  `-10^4 <= nums[i] <= 10^4` 
-  `nums` 已按升序排列
 
**标签**
`数组` `双指针` 


## 
```python

```
>
# 81.搜索旋转排序数组 II
[https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii) 
## 原题
已知存在一个按非降序排列的整数数组 `nums` ，数组中的值不必互不相同。

在传递给函数之前， `nums` 在预先未知的某个下标 `k` （ `0 <= k < nums.length` ）上进行了 **旋转** ，使数组变为 `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` （下标 **从 0 开始** 计数）。例如， `[0,1,2,4,4,4,5,6,6,7]` 在下标 `5` 处经旋转后可能变为 `[4,5,6,6,7,0,1,2,4,4]` 。

给你 **旋转后** 的数组 `nums` 和一个整数 `target` ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 `nums` 中存在这个目标值 `target` ，则返回 `true` ，否则返回 `false` 。

你必须尽可能减少整个操作步骤。

 

 **示例 1：** 

```

输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true

```
 **示例 2：** 

```

输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
```
 

 **提示：** 
-  `1 <= nums.length <= 5000` 
-  `-10^4 <= nums[i] <= 10^4` 
- 题目数据保证 `nums` 在预先未知的某个下标上进行了旋转
-  `-10^4 <= target <= 10^4` 
 

 **进阶：** 
- 这是 <a href="https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/">搜索旋转排序数组</a> 的延伸题目，本题中的 `nums` 可能包含重复元素。
- 这会影响到程序的时间复杂度吗？会有怎样的影响，为什么？
 

 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 82.删除排序链表中的重复元素 II
[https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii) 
## 原题
给定一个已排序的链表的头 `head` ， *删除原始链表中所有重复数字的节点，只留下不同的数字* 。返回 *已排序的链表* 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist1.jpg" style="height: 142px; width: 500px;" />
```

输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/linkedlist2.jpg" style="height: 164px; width: 400px;" />
```

输入：head = [1,1,1,2,3]
输出：[2,3]

```
 

 **提示：** 
- 链表中节点数目在范围 `[0, 300]` 内
-  `-100 <= Node.val <= 100` 
- 题目数据保证链表已经按升序 **排列** 
 
**标签**
`链表` `双指针` 


## 
```python

```
>
# 83.删除排序链表中的重复元素
[https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list) 
## 原题
给定一个已排序的链表的头<meta charset="UTF-8" /> `head` ， *删除所有重复的元素，使每个元素只出现一次* 。返回 *已排序的链表* 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/list1.jpg" style="height: 160px; width: 200px;" />
```

输入：head = [1,1,2]
输出：[1,2]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/list2.jpg" style="height: 123px; width: 300px;" />
```

输入：head = [1,1,2,3,3]
输出：[1,2,3]

```
 

 **提示：** 
- 链表中节点数目在范围 `[0, 300]` 内
-  `-100 <= Node.val <= 100` 
- 题目数据保证链表已经按升序 **排列** 
 
**标签**
`链表` 


## 
```python

```
>
# 84.柱状图中最大的矩形
[https://leetcode-cn.com/problems/largest-rectangle-in-histogram](https://leetcode-cn.com/problems/largest-rectangle-in-histogram) 
## 原题
给定 *n* 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

 **示例 1:** 

<img src="https://assets.leetcode.com/uploads/2021/01/04/histogram.jpg" />

```

输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10

```
 **示例 2：** 

<img src="https://assets.leetcode.com/uploads/2021/01/04/histogram-1.jpg" />

```

输入： heights = [2,4]
输出： 4
```
 

 **提示：** 
-  `1 <= heights.length <=10^5` 
-  `0 <= heights[i] <= 10^4` 
 
**标签**
`栈` `数组` `单调栈` 


## 
```python

```
>
# 85.最大矩形
[https://leetcode-cn.com/problems/maximal-rectangle](https://leetcode-cn.com/problems/maximal-rectangle) 
## 原题
给定一个仅包含 `0` 和 `1` 、大小为 `rows x cols` 的二维二进制矩阵，找出只包含 `1` 的最大矩形，并返回其面积。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;" />
```

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。

```
 **示例 2：** 

```

输入：matrix = []
输出：0

```
 **示例 3：** 

```

输入：matrix = [["0"]]
输出：0

```
 **示例 4：** 

```

输入：matrix = [["1"]]
输出：1

```
 **示例 5：** 

```

输入：matrix = [["0","0"]]
输出：0

```
 

 **提示：** 
-  `rows == matrix.length` 
-  `cols == matrix[0].length` 
-  `1 <= row, cols <= 200` 
-  `matrix[i][j]` 为 `'0'` 或 `'1'` 
 
**标签**
`栈` `数组` `动态规划` `矩阵` `单调栈` 


## 
```python

```
>
# 86.分隔链表
[https://leetcode-cn.com/problems/partition-list](https://leetcode-cn.com/problems/partition-list) 
## 原题
给你一个链表的头节点 `head` 和一个特定值 `x` ，请你对链表进行分隔，使得所有 **小于** `x` 的节点都出现在 **大于或等于** `x` 的节点之前。

你应当 **保留** 两个分区中每个节点的初始相对位置。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/04/partition.jpg" style="width: 662px; height: 222px;" />
```

输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]

```
 **示例 2：** 

```

输入：head = [2,1], x = 2
输出：[1,2]

```
 

 **提示：** 
- 链表中节点的数目在范围 `[0, 200]` 内
-  `-100 <= Node.val <= 100` 
-  `-200 <= x <= 200` 
 
**标签**
`链表` `双指针` 


## 
```python

```
>
# 87.扰乱字符串
[https://leetcode-cn.com/problems/scramble-string](https://leetcode-cn.com/problems/scramble-string) 
## 原题
使用下面描述的算法可以扰乱字符串 `s` 得到字符串 `t` ：

- 如果字符串的长度为 1 ，算法停止
- 如果字符串的长度 > 1 ，执行下述步骤：
	
- 在一个随机下标处将字符串分割成两个非空的子字符串。即，如果已知字符串 `s` ，则可以将其分成两个子字符串 `x` 和 `y` ，且满足 `s = x + y` 。
-  **随机** 决定是要「交换两个子字符串」还是要「保持这两个子字符串的顺序不变」。即，在执行这一步骤之后， `s` 可能是 `s = x + y` 或者 `s = y + x` 。
- 在 `x` 和 `y` 这两个子字符串上继续从步骤 1 开始递归执行此算法。
	
	
给你两个 **长度相等** 的字符串 `s1` 和  `s2` ，判断  `s2` * * 是否是  `s1` * * 的扰乱字符串。如果是，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：s1 = "great", s2 = "rgeat"
输出：true
解释：s1 上可能发生的一种情形是：
"great" --> "gr/eat" // 在一个随机下标处分割得到两个子字符串
"gr/eat" --> "gr/eat" // 随机决定：「保持这两个子字符串的顺序不变」
"gr/eat" --> "g/r / e/at" // 在子字符串上递归执行此算法。两个子字符串分别在随机下标处进行一轮分割
"g/r / e/at" --> "r/g / e/at" // 随机决定：第一组「交换两个子字符串」，第二组「保持这两个子字符串的顺序不变」
"r/g / e/at" --> "r/g / e/ a/t" // 继续递归执行此算法，将 "at" 分割得到 "a/t"
"r/g / e/ a/t" --> "r/g / e/ a/t" // 随机决定：「保持这两个子字符串的顺序不变」
算法终止，结果字符串和 s2 相同，都是 "rgeat"
这是一种能够扰乱 s1 得到 s2 的情形，可以认为 s2 是 s1 的扰乱字符串，返回 true

```
 **示例 2：** 

```

输入：s1 = "abcde", s2 = "caebd"
输出：false

```
 **示例 3：** 

```

输入：s1 = "a", s2 = "a"
输出：true

```
 

 **提示：** 
-  `s1.length == s2.length` 
-  `1 <= s1.length <= 30` 
-  `s1` 和 `s2` 由小写英文字母组成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 88.合并两个有序数组
[https://leetcode-cn.com/problems/merge-sorted-array](https://leetcode-cn.com/problems/merge-sorted-array) 
## 原题
给你两个按 **非递减顺序** 排列的整数数组 `nums1` 和 `nums2` ，另有两个整数 `m` 和 `n` ，分别表示 `nums1` 和 `nums2` 中的元素数目。

请你 **合并** `nums2` 到 `nums1` 中，使合并后的数组同样按 **非递减顺序** 排列。

 **注意：** 最终，合并后数组不应由函数返回，而是存储在数组 `nums1` 中。为了应对这种情况， `nums1` 的初始长度为 `m + n` ，其中前 `m` 个元素表示应合并的元素，后 `n` 个元素为 `0` ，应忽略。 `nums2` 的长度为 `n` 。

 

 **示例 1：** 

```

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

```
 **示例 2：** 

```

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
解释：需要合并 [1] 和 [] 。
合并结果是 [1] 。

```
 **示例 3：** 

```

输入：nums1 = [0], m = 0, nums2 = [1], n = 1
输出：[1]
解释：需要合并的数组是 [] 和 [1] 。
合并结果是 [1] 。
注意，因为 m = 0 ，所以 nums1 中没有元素。nums1 中仅存的 0 仅仅是为了确保合并结果可以顺利存放到 nums1 中。

```
 

 **提示：** 
-  `nums1.length == m + n` 
-  `nums2.length == n` 
-  `0 <= m, n <= 200` 
-  `1 <= m + n <= 200` 
-  `-10^9 <= nums1[i], nums2[j] <= 10^9` 
 

 **进阶：** 你可以设计实现一个时间复杂度为 `O(m + n)` 的算法解决此问题吗？

 
**标签**
`数组` `双指针` `排序` 


## 
```python

```
>
# 89.格雷编码
[https://leetcode-cn.com/problems/gray-code](https://leetcode-cn.com/problems/gray-code) 
## 原题
 **n 位格雷码序列** 是一个由 `2^n` 个整数组成的序列，其中：

- 每个整数都在范围 `[0, 2^n - 1]` 内（含 `0` 和 `2^n - 1` ）
- 第一个整数是 `0` 
- 一个整数在序列中出现 **不超过一次** 
- 每对 **相邻** 整数的二进制表示 **恰好一位不同** ，且
-  **第一个** 和 **最后一个** 整数的二进制表示 **恰好一位不同** 
给你一个整数 `n` ，返回任一有效的 **n 位格雷码序列** 。

 

 **示例 1：** 

```

输入：n = 2
输出：[0,1,3,2]
解释：
[0,1,3,2] 的二进制表示是 [00,01,11,10] 。
- 00 和 01 有一位不同
- 01 和 11 有一位不同
- 11 和 10 有一位不同
- 10 和 00 有一位不同
[0,2,3,1] 也是一个有效的格雷码序列，其二进制表示是 [00,10,11,01] 。
- 00 和 10 有一位不同
- 10 和 11 有一位不同
- 11 和 01 有一位不同
- 01 和 00 有一位不同

```
 **示例 2：** 

```

输入：n = 1
输出：[0,1]

```
 

 **提示：** 
-  `1 <= n <= 16` 
 
**标签**
`位运算` `数学` `回溯` 


## 
```python

```
>
# 90.子集 II
[https://leetcode-cn.com/problems/subsets-ii](https://leetcode-cn.com/problems/subsets-ii) 
## 原题
给你一个整数数组 `nums` ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 **不能** 包含重复的子集。返回的解集中，子集可以按 **任意顺序** 排列。
 

 **示例 1：** 

```

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]

```
 **示例 2：** 

```

输入：nums = [0]
输出：[[],[0]]

```
 

 **提示：** 
-  `1 <= nums.length <= 10` 
-  `-10 <= nums[i] <= 10` 
 
**标签**
`位运算` `数组` `回溯` 


## 
```python

```
>
# 91.解码方法
[https://leetcode-cn.com/problems/decode-ways](https://leetcode-cn.com/problems/decode-ways) 
## 原题
一条包含字母 `A-Z` 的消息通过以下映射进行了 **编码** ：

```

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```
要 **解码** 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如， `"11106"` 可以映射为：
-  `"AAJF"` ，将消息分组为 `(1 1 10 6)` 
-  `"KJF"` ，将消息分组为 `(11 10 6)` 
注意，消息不能分组为 `(1 11 06)` ，因为 `"06"` 不能映射为 `"F"` ，这是由于 `"6"` 和 `"06"` 在映射中并不等价。

给你一个只含数字的 **非空** 字符串 `s` ，请计算并返回 **解码** 方法的 **总数** 。

题目数据保证答案肯定是一个 **32 位** 的整数。

 

 **示例 1：** 

```

输入：s = "12"
输出：2
解释：它可以解码为 "AB"（1 2）或者 "L"（12）。

```
 **示例 2：** 

```

输入：s = "226"
输出：3
解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。

```
 **示例 3：** 

```

输入：s = "0"
输出：0
解释：没有字符映射到以 0 开头的数字。
含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。

```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `s` 只包含数字，并且可能包含前导零。
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 92.反转链表 II
[https://leetcode-cn.com/problems/reverse-linked-list-ii](https://leetcode-cn.com/problems/reverse-linked-list-ii) 
## 原题
给你单链表的头指针 `head` 和两个整数  `left` 和 `right` ，其中  `left <= right` 。请你反转从位置 `left` 到位置 `right` 的链表节点，返回 **反转后的链表** 。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg" style="width: 542px; height: 222px;" />
```

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]

```
 **示例 2：** 

```

输入：head = [5], left = 1, right = 1
输出：[5]

```
 

 **提示：** 
- 链表中节点数目为 `n` 
-  `1 <= n <= 500` 
-  `-500 <= Node.val <= 500` 
-  `1 <= left <= right <= n` 
 

 **进阶：** 你可以使用一趟扫描完成反转吗？

 
**标签**
`链表` 


## 
```python

```
>
# 93.复原 IP 地址
[https://leetcode-cn.com/problems/restore-ip-addresses](https://leetcode-cn.com/problems/restore-ip-addresses) 
## 原题
 **有效 IP 地址** 正好由四个整数（每个整数位于 `0` 到 `255` 之间组成，且不能含有前导 `0` ），整数之间用 `'.'` 分隔。
- 例如： `"0.1.2.201"` 和 `"192.168.1.1"` 是 **有效** IP 地址，但是 `"0.011.255.245"` 、 `"192.168.1.312"` 和 `"192.168@1.1"` 是 **无效** IP 地址。
给定一个只包含数字的字符串 `s` ，用以表示一个 IP 地址，返回所有可能的 **有效 IP 地址** ，这些地址可以通过在 `s` 中插入 `'.'` 来形成。你 **不能** 重新排序或删除 `s` 中的任何数字。你可以按 **任何** 顺序返回答案。

 

 **示例 1：** 

```

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]

```
 **示例 2：** 

```

输入：s = "0000"
输出：["0.0.0.0"]

```
 **示例 3：** 

```

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]

```
 

 **提示：** 
-  `0 <= s.length <= 20` 
-  `s` 仅由数字组成
 
**标签**
`字符串` `回溯` 


## 
```python

```
>
# 94.二叉树的中序遍历
[https://leetcode-cn.com/problems/binary-tree-inorder-traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) 
## 原题
给定一个二叉树的根节点 `root` ，返回它的 **中序**  遍历。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 202px; height: 324px;" />
```

输入：root = [1,null,2,3]
输出：[1,3,2]

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
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg" style="width: 202px; height: 202px;" />
```

输入：root = [1,2]
输出：[2,1]

```
 **示例 5：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg" style="width: 202px; height: 202px;" />
```

输入：root = [1,null,2]
输出：[1,2]

```
 

 **提示：** 
- 树中节点数目在范围 `[0, 100]` 内
-  `-100 <= Node.val <= 100` 
 

 **进阶:**  递归算法很简单，你可以通过迭代算法完成吗？

 
**标签**
`栈` `树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 95.不同的二叉搜索树 II
[https://leetcode-cn.com/problems/unique-binary-search-trees-ii](https://leetcode-cn.com/problems/unique-binary-search-trees-ii) 
## 原题
给你一个整数 `n` ，请你生成并返回所有由 `n` 个节点组成且节点值从 `1` 到 `n` 互不相同的不同 **二叉搜索树** 。可以按 **任意顺序** 返回答案。

 
 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;" />
```

输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]

```
 **示例 2：** 

```

输入：n = 1
输出：[[1]]

```
 

 **提示：** 
-  `1 <= n <= 8` 
 
**标签**
`树` `二叉搜索树` `动态规划` `回溯` `二叉树` 


## 
```python

```
>
# 96.不同的二叉搜索树
[https://leetcode-cn.com/problems/unique-binary-search-trees](https://leetcode-cn.com/problems/unique-binary-search-trees) 
## 原题
给你一个整数 `n` ，求恰由 `n` 个节点组成且节点值从 `1` 到 `n` 互不相同的 **二叉搜索树** 有多少种？返回满足题意的二叉搜索树的种数。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/uniquebstn3.jpg" style="width: 600px; height: 148px;" />
```

输入：n = 3
输出：5

```
 **示例 2：** 

```

输入：n = 1
输出：1

```
 

 **提示：** 
-  `1 <= n <= 19` 
 
**标签**
`树` `二叉搜索树` `数学` `动态规划` `二叉树` 


## 
```python

```
>
# 97.交错字符串
[https://leetcode-cn.com/problems/interleaving-string](https://leetcode-cn.com/problems/interleaving-string) 
## 原题
给定三个字符串 `s1` 、 `s2` 、 `s3` ，请你帮忙验证 `s3` 是否是由 `s1` 和 `s2`  **交错** 组成的。

两个字符串 `s` 和 `t` **交错** 的定义与过程如下，其中每个字符串都会被分割成若干 **非空** 子字符串：
-  `s = s<sub>1</sub> + s<sub>2</sub> + ... + s<sub>n</sub>` 
-  `t = t<sub>1</sub> + t<sub>2</sub> + ... + t<sub>m</sub>` 
-  `|n - m| <= 1` 
-  **交错** 是 `s<sub>1</sub> + t<sub>1</sub> + s<sub>2</sub> + t<sub>2</sub> + s<sub>3</sub> + t<sub>3</sub> + ...` 或者 `t<sub>1</sub> + s<sub>1</sub> + t<sub>2</sub> + s<sub>2</sub> + t<sub>3</sub> + s<sub>3</sub> + ...` 
 **注意：** `a + b` 意味着字符串 `a` 和 `b` 连接。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/02/interleave.jpg" />
```

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true

```
 **示例 2：** 

```

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false

```
 **示例 3：** 

```

输入：s1 = "", s2 = "", s3 = ""
输出：true

```
 

 **提示：** 
-  `0 <= s1.length, s2.length <= 100` 
-  `0 <= s3.length <= 200` 
-  `s1` 、 `s2` 、和 `s3` 都由小写英文字母组成
 

 **进阶：** 您能否仅使用 `O(s2.length)` 额外的内存空间来解决它?

 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 98.验证二叉搜索树
[https://leetcode-cn.com/problems/validate-binary-search-tree](https://leetcode-cn.com/problems/validate-binary-search-tree) 
## 原题
给你一个二叉树的根节点 `root` ，判断其是否是一个有效的二叉搜索树。

 **有效** 二叉搜索树定义如下：
- 节点的左子树只包含 **小于** 当前节点的数。
- 节点的右子树只包含 **大于** 当前节点的数。
- 所有左子树和右子树自身必须也是二叉搜索树。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree1.jpg" style="width: 302px; height: 182px;" />
```

输入：root = [2,1,3]
输出：true

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/01/tree2.jpg" style="width: 422px; height: 292px;" />
```

输入：root = [5,1,4,null,null,3,6]
输出：false
解释：根节点的值是 5 ，但是右子节点的值是 4 。

```
 

 **提示：** 
- 树中节点数目范围在 `[1, 10^4]` 内
-  `-2^31 <= Node.val <= 2^31 - 1` 
 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 99.恢复二叉搜索树
[https://leetcode-cn.com/problems/recover-binary-search-tree](https://leetcode-cn.com/problems/recover-binary-search-tree) 
## 原题
给你二叉搜索树的根节点 `root` ，该树中的 **恰好** 两个节点的值被错误地交换。 *请在不改变其结构的情况下，恢复这棵树* 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover1.jpg" style="width: 300px;" />
```

输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/28/recover2.jpg" style="height: 208px; width: 400px;" />
```

输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
```
 

 **提示：** 
- 树上节点的数目在范围 `[2, 1000]` 内
-  `-2^31 <= Node.val <= 2^31 - 1` 
 

 **进阶：** 使用 `O(n)` 空间复杂度的解法很容易实现。你能想出一个只使用 `O(1)` 空间的解决方案吗？

 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 100.相同的树
[https://leetcode-cn.com/problems/same-tree](https://leetcode-cn.com/problems/same-tree) 
## 原题
给你两棵二叉树的根节点 `p` 和 `q` ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex1.jpg" style="width: 622px; height: 182px;" />
```

输入：p = [1,2,3], q = [1,2,3]
输出：true

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex2.jpg" style="width: 382px; height: 182px;" />
```

输入：p = [1,2], q = [1,null,2]
输出：false

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/ex3.jpg" style="width: 622px; height: 182px;" />
```

输入：p = [1,2,1], q = [1,1,2]
输出：false

```
 

 **提示：** 
- 两棵树上的节点数目都在范围 `[0, 100]` 内
-  `-10^4 <= Node.val <= 10^4` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
