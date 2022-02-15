# 701.二叉搜索树中的插入操作
[https://leetcode-cn.com/problems/insert-into-a-binary-search-tree](https://leetcode-cn.com/problems/insert-into-a-binary-search-tree) 
## 原题
给定二叉搜索树（BST）的根节点<meta charset="UTF-8" /> `root` 和要插入树中的值<meta charset="UTF-8" /> `value` ，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据 **保证** ，新值和原始二叉搜索树中的任意节点值都不同。

 **注意** ，可能存在多种有效的插入方式，只要树在插入后仍保持为二叉搜索树即可。 你可以返回 **任意有效的结果** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/insertbst.jpg" />
```

输入：root = [4,2,7,1,3], val = 5
输出：[4,2,7,1,3,5]
解释：另一个满足题目要求可以通过的树是：
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/05/bst.jpg" />

```
 **示例 2：** 

```

输入：root = [40,20,60,10,30,50,70], val = 25
输出：[40,20,60,10,30,50,70,null,null,25]

```
 **示例 3：** 

```

输入：root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
输出：[4,2,7,1,3,5]

```
 

 **提示：** 
- 树中的节点数将在<meta charset="UTF-8" /> `[0, 10^4]` 的范围内。<meta charset="UTF-8" />
-  `-10^8 <= Node.val <= 10^8` 
- 所有值 <meta charset="UTF-8" /> `Node.val` 是 **独一无二** 的。
-  `-10^8 <= val <= 10^8` 
-  **保证** `val` 在原始BST中不存在。
 
**标签**
`树` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 702.搜索长度未知的有序数组
[https://leetcode-cn.com/problems/search-in-a-sorted-array-of-unknown-size](https://leetcode-cn.com/problems/search-in-a-sorted-array-of-unknown-size) 
## 原题

 
**标签**
`数组` `二分查找` `交互` 


## 
```python

```
>
# 703.数据流中的第 K 大元素
[https://leetcode-cn.com/problems/kth-largest-element-in-a-stream](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream) 
## 原题
设计一个找到数据流中第 `k` 大元素的类（class）。注意是排序后的第 `k` 大元素，不是第 `k` 个不同的元素。

请实现 `KthLargest`  类：
-  `KthLargest(int k, int[] nums)` 使用整数 `k` 和整数流 `nums` 初始化对象。
-  `int add(int val)` 将 `val` 插入数据流 `nums` 后，返回当前数据流中第 `k` 大的元素。
 

 **示例：** 

```

输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8

```
 
 **提示：** 
-  `1 <= k <= 10^4` 
-  `0 <= nums.length <= 10^4` 
-  `-10^4 <= nums[i] <= 10^4` 
-  `-10^4 <= val <= 10^4` 
- 最多调用 `add` 方法 `10^4` 次
- 题目数据保证，在查找第 `k` 大元素时，数组中至少有 `k` 个元素
 
**标签**
`树` `设计` `二叉搜索树` `二叉树` `数据流` `堆（优先队列）` 


## 
```python

```
>
# 704.二分查找
[https://leetcode-cn.com/problems/binary-search](https://leetcode-cn.com/problems/binary-search) 
## 原题
给定一个 `n` 个元素有序的（升序）整型数组 `nums` 和一个目标值 `target` ，写一个函数搜索 `nums` 中的 `target` ，如果目标值存在返回下标，否则返回 `-1` 。

<br>
 **示例 1:** 

```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4

```
 **示例 2:** 

```
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1

```
 

 **提示：** 
- 你可以假设 `nums` 中的所有元素是不重复的。
-  `n` 将在 `[1, 10000]` 之间。
-  `nums` 的每个元素都将在 `[-9999, 9999]` 之间。
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 705.设计哈希集合
[https://leetcode-cn.com/problems/design-hashset](https://leetcode-cn.com/problems/design-hashset) 
## 原题
不使用任何内建的哈希表库设计一个哈希集合（HashSet）。

实现 `MyHashSet` 类：
-  `void add(key)` 向哈希集合中插入值 `key` 。
-  `bool contains(key)` 返回哈希集合中是否存在这个值 `key` 。
-  `void remove(key)` 将给定值 `key` 从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

 

 **示例：** 

```

输入：
["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
[[], [1], [2], [1], [3], [2], [2], [2], [2]]
输出：
[null, null, null, true, false, null, true, null, false]

解释：
MyHashSet myHashSet = new MyHashSet();
myHashSet.add(1);      // set = [1]
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(1); // 返回 True
myHashSet.contains(3); // 返回 False ，（未找到）
myHashSet.add(2);      // set = [1, 2]
myHashSet.contains(2); // 返回 True
myHashSet.remove(2);   // set = [1]
myHashSet.contains(2); // 返回 False ，（已移除）
```
 

 **提示：** 
-  `0 <= key <= 10^6` 
- 最多调用 `10^4` 次 `add` 、 `remove` 和 `contains` 
 
**标签**
`设计` `数组` `哈希表` `链表` `哈希函数` 


## 
```python

```
>
# 706.设计哈希映射
[https://leetcode-cn.com/problems/design-hashmap](https://leetcode-cn.com/problems/design-hashmap) 
## 原题
不使用任何内建的哈希表库设计一个哈希映射（HashMap）。

实现 `MyHashMap` 类：
-  `MyHashMap()` 用空映射初始化对象
-  `void put(int key, int value)` 向 HashMap 插入一个键值对 `(key, value)` 。如果 `key` 已经存在于映射中，则更新其对应的值 `value` 。
-  `int get(int key)` 返回特定的 `key` 所映射的 `value` ；如果映射中不包含 `key` 的映射，返回 `-1` 。
-  `void remove(key)` 如果映射中存在 `key` 的映射，则移除 `key` 和它所对应的 `value` 。
 

 **示例：** 

```

输入：
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
输出：
[null, null, null, 1, -1, null, 1, null, -1]

解释：
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // myHashMap 现在为 [[1,1]]
myHashMap.put(2, 2); // myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(1);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,2]]
myHashMap.get(3);    // 返回 -1（未找到），myHashMap 现在为 [[1,1], [2,2]]
myHashMap.put(2, 1); // myHashMap 现在为 [[1,1], [2,1]]（更新已有的值）
myHashMap.get(2);    // 返回 1 ，myHashMap 现在为 [[1,1], [2,1]]
myHashMap.remove(2); // 删除键为 2 的数据，myHashMap 现在为 [[1,1]]
myHashMap.get(2);    // 返回 -1（未找到），myHashMap 现在为 [[1,1]]

```
 

 **提示：** 
-  `0 <= key, value <= 10^6` 
- 最多调用 `10^4` 次 `put` 、 `get` 和 `remove` 方法
 
**标签**
`设计` `数组` `哈希表` `链表` `哈希函数` 


## 
```python

```
>
# 707.设计链表
[https://leetcode-cn.com/problems/design-linked-list](https://leetcode-cn.com/problems/design-linked-list) 
## 原题
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性： `val` 和 `next` 。 `val` 是当前节点的值， `next` 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 `prev` 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：
- get(index)：获取链表中第 `index` 个节点的值。如果索引无效，则返回 `-1` 。
- addAtHead(val)：在链表的第一个元素之前添加一个值为 `val` 的节点。插入后，新节点将成为链表的第一个节点。
- addAtTail(val)：将值为 `val` 的节点追加到链表的最后一个元素。
- addAtIndex(index,val)：在链表中的第 `index` 个节点之前添加值为 `val` 的节点。如果 `index` 等于链表的长度，则该节点将附加到链表的末尾。如果 `index` 大于链表长度，则不会插入节点。如果 `index` 小于0，则在头部插入节点。
- deleteAtIndex(index)：如果索引 `index` 有效，则删除链表中的第 `index` 个节点。
 

 **示例：** 

```
MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3

```
 

 **提示：** 
- 所有 `val` 值都在 `[1, 1000]` 之内。
- 操作次数将在 `[1, 1000]` 之内。
- 请不要使用内置的 LinkedList 库。
 
**标签**
`设计` `链表` 


## 
```python

```
>
# 708.循环有序列表的插入
[https://leetcode-cn.com/problems/insert-into-a-sorted-circular-linked-list](https://leetcode-cn.com/problems/insert-into-a-sorted-circular-linked-list) 
## 原题

 
**标签**
`链表` 


## 
```python

```
>
# 709.转换成小写字母
[https://leetcode-cn.com/problems/to-lower-case](https://leetcode-cn.com/problems/to-lower-case) 
## 原题
给你一个字符串 `s` ，将该字符串中的大写字母转换成相同的小写字母，返回新的字符串。

 

 **示例 1：** 

```

输入：s = "Hello"
输出："hello"

```
 **示例 2：** 

```

输入：s = "here"
输出："here"

```
 **示例 3：** 

```

输入：s = "LOVELY"
输出："lovely"

```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `s` 由 ASCII 字符集中的可打印字符组成
 
**标签**
`字符串` 


## 
```python

```
>
# 710.黑名单中的随机数
[https://leetcode-cn.com/problems/random-pick-with-blacklist](https://leetcode-cn.com/problems/random-pick-with-blacklist) 
## 原题
给定一个整数 `n` 和一个 **无重复** 黑名单整数数组 `blacklist` 。设计一种算法，从 `[0, n - 1]` 范围内的任意整数中选取一个 **未加入** 黑名单 `blacklist` 的整数。任何在上述范围内且不在黑名单 `blacklist` 中的整数都应该有 **同等的可能性** 被返回。

优化你的算法，使它最小化调用语言 **内置** 随机函数的次数。

实现 `Solution` 类:
-  `Solution(int n, int[] blacklist)` 初始化整数 `n` 和被加入黑名单 `blacklist` 的整数
-  `int pick()` 返回一个范围为 `[0, n - 1]` 且不在黑名单 `blacklist` 中的随机整数
 

 **示例 1：** 

```

输入
["Solution", "pick", "pick", "pick", "pick", "pick", "pick", "pick"]
[[7, [2, 3, 5]], [], [], [], [], [], [], []]
输出
[null, 0, 4, 1, 6, 1, 0, 4]

解释
Solution solution = new Solution(7, [2, 3, 5]);
solution.pick(); // 返回0，任何[0,1,4,6]的整数都可以。注意，对于每一个pick的调用，
                 // 0、1、4和6的返回概率必须相等(即概率为1/4)。
solution.pick(); // 返回 4
solution.pick(); // 返回 1
solution.pick(); // 返回 6
solution.pick(); // 返回 1
solution.pick(); // 返回 0
solution.pick(); // 返回 4

```
 

 **提示:** 
-  `1 <= n <= 10^9` 
-  `0 <= blacklist.length <- min(10^5, n - 1)` 
-  `0 <= blacklist[i] < n` 
-  `blacklist` 中所有值都 **不同** 
-  `pick` 最多被调用 `2 * 10^4` 次
 
**标签**
`哈希表` `数学` `二分查找` `排序` `随机化` 


## 
```python

```
>
# 711.不同岛屿的数量 II
[https://leetcode-cn.com/problems/number-of-distinct-islands-ii](https://leetcode-cn.com/problems/number-of-distinct-islands-ii) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `哈希表` `哈希函数` 


## 
```python

```
>
# 712.两个字符串的最小ASCII删除和
[https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings](https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings) 
## 原题
给定两个字符串 `s1` 和 `s2` ，返回 *使两个字符串相等所需删除字符的 **ASCII** 值的最小和* 。

 

 **示例 1:** 

```

输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。

```
 **示例 2:** 

```

输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。

```
 

 **提示:** 
-  `0 <= s1.length, s2.length <= 1000` 
-  `s1` 和 `s2` 由小写英文字母组成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 713.乘积小于K的子数组
[https://leetcode-cn.com/problems/subarray-product-less-than-k](https://leetcode-cn.com/problems/subarray-product-less-than-k) 
## 原题
给定一个正整数数组  `nums` 和整数 `k` 。

请找出该数组内乘积小于  `k`  的连续的子数组的个数。

 

 **示例 1:** 

```

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。

```
 **示例 2:** 

```

输入: nums = [1,2,3], k = 0
输出: 0
```
 

 **提示: ** 
-  `1 <= nums.length <= 3 * 10^4` 
-  `1 <= nums[i] <= 1000` 
-  `0 <= k <= 10^6` 
 
**标签**
`数组` `滑动窗口` 


## 
```python

```
>
# 714.买卖股票的最佳时机含手续费
[https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee) 
## 原题
给定一个整数数组 `prices` ，其中 `prices[i]` 表示第 `i` 天的股票价格 ；整数 `fee` 代表了交易股票的手续费用。

你可以无限次地完成交易，但是你每笔交易都需要付手续费。如果你已经购买了一个股票，在卖出它之前你就不能再继续购买股票了。

返回获得利润的最大值。

 **注意：** 这里的一笔交易指买入持有并卖出股票的整个过程，每笔交易你只需要为支付一次手续费。

 

 **示例 1：** 

```

输入：prices = [1, 3, 2, 8, 4, 9], fee = 2
输出：8
解释：能够达到的最大利润:  
在此处买入 prices[0] = 1
在此处卖出 prices[3] = 8
在此处买入 prices[4] = 4
在此处卖出 prices[5] = 9
总利润: ((8 - 1) - 2) + ((9 - 4) - 2) = 8
```
 **示例 2：** 

```

输入：prices = [1,3,7,5,10,3], fee = 3
输出：6

```
 

 **提示：** 
-  `1 <= prices.length <= 5 * 10^4` 
-  `1 <= prices[i] < 5 * 10^4` 
-  `0 <= fee < 5 * 10^4` 
 
**标签**
`贪心` `数组` `动态规划` 


## 
```python

```
>
# 715.Range 模块
[https://leetcode-cn.com/problems/range-module](https://leetcode-cn.com/problems/range-module) 
## 原题
Range模块是跟踪数字范围的模块。设计一个数据结构来跟踪表示为 **半开区间** 的范围并查询它们。

 **半开区间** `[left, right)` 表示所有 `left <= x < right` 的实数 `x` 。

实现 `RangeModule` 类:
-  `RangeModule()` 初始化数据结构的对象。
-  `void addRange(int left, int right)` 添加 **半开区间** `[left, right)` ，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠的区间时，应当添加在区间 `[left, right)` 中尚未跟踪的任何数字到该区间中。
-  `boolean queryRange(int left, int right)` 只有在当前正在跟踪区间 `[left, right)` 中的每一个实数时，才返回 `true` ，否则返回 `false` 。
-  `void removeRange(int left, int right)` 停止跟踪 **半开区间** `[left, right)` 中当前正在跟踪的每个实数。
 

 **示例 1：** 

```

输入
["RangeModule", "addRange", "removeRange", "queryRange", "queryRange", "queryRange"]
[[], [10, 20], [14, 16], [10, 14], [13, 15], [16, 17]]
输出
[null, null, null, true, false, true]

解释
RangeModule rangeModule = new RangeModule();
rangeModule.addRange(10, 20);
rangeModule.removeRange(14, 16);
rangeModule.queryRange(10, 14); 返回 true （区间 [10, 14) 中的每个数都正在被跟踪）
rangeModule.queryRange(13, 15); 返回 false（未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
rangeModule.queryRange(16, 17); 返回 true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）

```
 

 **提示：** 
-  `1 <= left < right <= 10^9` 
- 在单个测试用例中，对 `addRange` 、 `queryRange` 和 `removeRange` 的调用总数不超过 `10^4` 次
 
**标签**
`设计` `线段树` `有序集合` 


## 
```python

```
>
# 716.最大栈
[https://leetcode-cn.com/problems/max-stack](https://leetcode-cn.com/problems/max-stack) 
## 原题

 
**标签**
`栈` `设计` `链表` `双向链表` `有序集合` 


## 
```python

```
>
# 717.1比特与2比特字符
[https://leetcode-cn.com/problems/1-bit-and-2-bit-characters](https://leetcode-cn.com/problems/1-bit-and-2-bit-characters) 
## 原题
有两种特殊字符：
- 第一种字符可以用一个比特 `0` 来表示
- 第二种字符可以用两个比特( `10` 或 `11` )来表示、
给定一个以 `0` 结尾的二进制数组 `bits` ，如果最后一个字符必须是一位字符，则返回 `true` 。

 

 **示例 1:** 

```

输入: bits = [1, 0, 0]
输出: true
解释: 唯一的编码方式是一个两比特字符和一个一比特字符。
所以最后一个字符是一比特字符。

```
 **示例 2:** 

```

输入: bits = [1, 1, 1, 0]
输出: false
解释: 唯一的编码方式是两比特字符和两比特字符。
所以最后一个字符不是一比特字符。

```
 

 **提示:** 
-  `1 <= bits.length <= 1000` 
-  `bits[i] == 0 or 1` 
 
**标签**
`数组` 


## 
```python

```
>
# 718.最长重复子数组
[https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray](https://leetcode-cn.com/problems/maximum-length-of-repeated-subarray) 
## 原题
给两个整数数组 `nums1` 和 `nums2` ，返回 *两个数组中 **公共的** 、长度最长的子数组的长度* 。

 

 **示例 1：** 

```

输入：nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
输出：3
解释：长度最长的公共子数组是 [3,2,1] 。

```
 **示例 2：** 

```

输入：nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
输出：5

```
 

 **提示：** 
-  `1 <= nums1.length, nums2.length <= 1000` 
-  `0 <= nums1[i], nums2[i] <= 100` 
 
**标签**
`数组` `二分查找` `动态规划` `滑动窗口` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 719.找出第 k 小的距离对
[https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance](https://leetcode-cn.com/problems/find-k-th-smallest-pair-distance) 
## 原题
给定一个整数数组，返回所有数对之间的第 k 个最小 **距离** 。一对 (A, B) 的距离被定义为 A 和 B 之间的绝对差值。

 **示例 1:** 

```

输入：
nums = [1,3,1]
k = 1
输出：0 
解释：
所有数对如下：
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
因此第 1 个最小距离的数对是 (1,1)，它们之间的距离为 0。

```
 **提示:** 
-  `2 <= len(nums) <= 10000` .
-  `0 <= nums[i] < 1000000` .
-  `1 <= k <= len(nums) * (len(nums) - 1) / 2` .
 
**标签**
`数组` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 720.词典中最长的单词
[https://leetcode-cn.com/problems/longest-word-in-dictionary](https://leetcode-cn.com/problems/longest-word-in-dictionary) 
## 原题
给出一个字符串数组 `words` 组成的一本英语词典。返回 `words` 中最长的一个单词，该单词是由 `words` 词典中其他单词逐步添加一个字母组成。

若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。

 

 **示例 1：** 

```

输入：words = ["w","wo","wor","worl", "world"]
输出："world"
解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。

```
 **示例 2：** 

```

输入：words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释："apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply" 

```
 

 **提示：** 
-  `1 <= words.length <= 1000` 
-  `1 <= words[i].length <= 30` 
- 所有输入的字符串 `words[i]` 都只包含小写字母。
 
**标签**
`字典树` `数组` `哈希表` `字符串` `排序` 


## 
```python

```
>
# 721.账户合并
[https://leetcode-cn.com/problems/accounts-merge](https://leetcode-cn.com/problems/accounts-merge) 
## 原题
给定一个列表 `accounts` ，每个元素 `accounts[i]` 是一个字符串列表，其中第一个元素 `accounts[i][0]` 是 *名称 (name)* ，其余元素是 ***emails*** 表示该账户的邮箱地址。

现在，我们想合并这些账户。如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。

合并账户后，按以下格式返回账户：每个账户的第一个元素是名称，其余元素是 **按字符 ASCII 顺序排列** 的邮箱地址。账户本身可以以 **任意顺序** 返回。

 

 **示例 1：** 

```

输入：accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
输出：[["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
解释：
第一个和第三个 John 是同一个人，因为他们有共同的邮箱地址 "johnsmith@mail.com"。 
第二个 John 和 Mary 是不同的人，因为他们的邮箱地址没有被其他帐户使用。
可以以任何顺序返回这些列表，例如答案 [['Mary'，'mary@mail.com']，['John'，'johnnybravo@mail.com']，
['John'，'john00@mail.com'，'john_newyork@mail.com'，'johnsmith@mail.com']] 也是正确的。

```
 **示例 2：** 

```

输入：accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
输出：[["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]

```
 

 **提示：** 
-  `1 <= accounts.length <= 1000` 
-  `2 <= accounts[i].length <= 10` 
-  `1 <= accounts[i][j].length <= 30` 
-  `accounts[i][0]` 由英文字母组成
-  `accounts[i][j] (for j > 0)` 是有效的邮箱地址
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `字符串` 


## 
```python

```
>
# 722.删除注释
[https://leetcode-cn.com/problems/remove-comments](https://leetcode-cn.com/problems/remove-comments) 
## 原题
给一个 C++ 程序，删除程序中的注释。这个程序 `source` 是一个数组，其中 `source[i]` 表示第 `i` 行源码。 这表示每行源码由<font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4"> `'\n'` </span></span></font></font>分隔。

在 C++ 中有两种注释风格，行内注释和块注释。
- 字符串 `//` 表示行注释，表示 `//` 和其右侧的其余字符应该被忽略。
- 字符串 `/*` 表示一个块注释，它表示直到下一个（非重叠）出现的 `*/` 之间的所有字符都应该被忽略。（阅读顺序为从左到右）非重叠是指，字符串 `/*/` 并没有结束块注释，因为注释的结尾与开头相重叠。
第一个有效注释优先于其他注释。
- 如果字符串 `//` 出现在块注释中会被忽略。
- 同样，如果字符串 `/*` 出现在行或块注释中也会被忽略。
如果一行在删除注释之后变为空字符串，那么 **不要** 输出该行。即，答案列表中的每个字符串都是非空的。

样例中 **没有** 控制字符，单引号或双引号字符。
- 比如， `source = "string s = "/* Not a comment. */";"` 不会出现在测试样例里。
此外，没有其他内容（如定义或宏）会干扰注释。

我们保证每一个块注释最终都会被闭合， 所以在行或块注释之外的 `/*` 总是开始新的注释。

最后，隐式换行符 **可以** 通过块注释删除。 有关详细信息，请参阅下面的示例。

从源代码中删除注释后，需要以相同的格式返回源代码。

 

 **示例 1:** 

```

输入: source = ["/*Test program */", "int main()", "{ ", "  // variable declaration ", "int a, b, c;", "/* This is a test", "   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]
输出: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]
解释: 示例代码可以编排成这样:
/*Test program */
int main()
{ 
  // variable declaration 
int a, b, c;
/* This is a test
   multiline  
   comment for 
   testing */
a = b + c;
}
第 1 行和第 6-9 行的字符串 /* 表示块注释。第 4 行的字符串 // 表示行注释。
编排后: 
int main()
{ 
  
int a, b, c;
a = b + c;
}
```
 **示例 2:** 

```

输入: source = ["a/*comment", "line", "more_comment*/b"]
输出: ["ab"]
解释: 原始的 source 字符串是 "a/*comment\nline\nmore_comment*/b", 其中我们用粗体显示了换行符。删除注释后，隐含的换行符被删除，留下字符串 "ab" 用换行符分隔成数组时就是 ["ab"].

```
 

 **提示:** 
-  `1 <= source.length <= 100` 
-  `0 <= source[i].length <= 80` 
-  `source[i]` 由可打印的 **ASCII** 字符组成。
- 每个块注释都会被闭合。
- 给定的源码中不会有单引号、双引号或其他控制字符。

<span style="display:block"><span style="height:0px"><span style="position:absolute"><span style="top:0px"><span style="left:-9999px"><span style="opacity:0"><span style="overflow:hidden"> </span></span></span></span></span></span>​​​​​​</span>
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 723.粉碎糖果
[https://leetcode-cn.com/problems/candy-crush](https://leetcode-cn.com/problems/candy-crush) 
## 原题

 
**标签**
`数组` `双指针` `矩阵` `模拟` 


## 
```python

```
>
# 724.寻找数组的中心下标
[https://leetcode-cn.com/problems/find-pivot-index](https://leetcode-cn.com/problems/find-pivot-index) 
## 原题
给你一个整数数组 `nums` ，请计算数组的 **中心下标** 。

数组 **中心下标** **** 是数组的一个下标，其左侧所有元素相加的和等于右侧所有元素相加的和。

如果中心下标位于数组最左端，那么左侧数之和视为 `0` ，因为在下标的左侧不存在元素。这一点对于中心下标位于数组最右端同样适用。

如果数组有多个中心下标，应该返回 **最靠近左边** 的那一个。如果数组不存在中心下标，返回 `-1` 。

 

 **示例 1：** 

```

输入：nums = [1, 7, 3, 6, 5, 6]
输出：3
解释：
中心下标是 3 。
左侧数之和 sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11 ，
右侧数之和 sum = nums[4] + nums[5] = 5 + 6 = 11 ，二者相等。

```
 **示例 2：** 

```

输入：nums = [1, 2, 3]
输出：-1
解释：
数组中不存在满足此条件的中心下标。
```
 **示例 3：** 

```

输入：nums = [2, 1, -1]
输出：0
解释：
中心下标是 0 。
左侧数之和 sum = 0 ，（下标 0 左侧不存在元素），
右侧数之和 sum = nums[1] + nums[2] = 1 + -1 = 0 。
```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `-1000 <= nums[i] <= 1000` 
 

 **注意：** 本题与主站 1991 题相同：<a href="https://leetcode-cn.com/problems/find-the-middle-index-in-array/" target="_blank">https://leetcode-cn.com/problems/find-the-middle-index-in-array/</a>

 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 725.分隔链表
[https://leetcode-cn.com/problems/split-linked-list-in-parts](https://leetcode-cn.com/problems/split-linked-list-in-parts) 
## 原题
给你一个头结点为 `head` 的单链表和一个整数 `k` ，请你设计一个算法将链表分隔为 `k` 个连续的部分。

每部分的长度应该尽可能的相等：任意两部分的长度差距不能超过 1 。这可能会导致有些部分为 null 。

这 `k` 个部分应该按照在链表中出现的顺序排列，并且排在前面的部分的长度应该大于或等于排在后面的长度。

返回一个由上述 `k` 部分组成的数组。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/13/split1-lc.jpg" style="width: 400px; height: 134px;" />
```

输入：head = [1,2,3], k = 5
输出：[[1],[2],[3],[],[]]
解释：
第一个元素 output[0] 为 output[0].val = 1 ，output[0].next = null 。
最后一个元素 output[4] 为 null ，但它作为 ListNode 的字符串表示是 [] 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/06/13/split2-lc.jpg" style="width: 600px; height: 60px;" />
```

输入：head = [1,2,3,4,5,6,7,8,9,10], k = 3
输出：[[1,2,3,4],[5,6,7],[8,9,10]]
解释：
输入被分成了几个连续的部分，并且每部分的长度相差不超过 1 。前面部分的长度大于等于后面部分的长度。

```
 

 **提示：** 
- 链表中节点的数目在范围 `[0, 1000]` 
-  `0 <= Node.val <= 1000` 
-  `1 <= k <= 50` 
 
**标签**
`链表` 


## 
```python

```
>
# 726.原子的数量
[https://leetcode-cn.com/problems/number-of-atoms](https://leetcode-cn.com/problems/number-of-atoms) 
## 原题
给你一个字符串化学式 `formula` ，返回 **每种原子的数量** 。

原子总是以一个大写字母开始，接着跟随 0 个或任意个小写字母，表示原子的名字。

如果数量大于 1，原子后会跟着数字表示原子的数量。如果数量等于 1 则不会跟数字。
- 例如， `"H2O"` 和 `"H2O2"` 是可行的，但 `"H1O2"` 这个表达是不可行的。
两个化学式连在一起可以构成新的化学式。
- 例如 `"H2O2He3Mg4"` 也是化学式。
由括号括起的化学式并佐以数字（可选择性添加）也是化学式。
- 例如 `"(H2O2)"` 和 `"(H2O2)3"` 是化学式。
返回所有原子的数量，格式为：第一个（按字典序）原子的名字，跟着它的数量（如果数量大于 1），然后是第二个原子的名字（按字典序），跟着它的数量（如果数量大于 1），以此类推。

 

 **示例 1：** 

```

输入：formula = "H2O"
输出："H2O"
解释：原子的数量是 {'H': 2, 'O': 1}。

```
 **示例 2：** 

```

输入：formula = "Mg(OH)2"
输出："H2MgO2"
解释：原子的数量是 {'H': 2, 'Mg': 1, 'O': 2}。

```
 **示例 3：** 

```

输入：formula = "K4(ON(SO3)2)2"
输出："K4N2O14S4"
解释：原子的数量是 {'K': 4, 'N': 2, 'O': 14, 'S': 4}。

```
 **示例 4：** 

```

输入：formula = "Be32"
输出："Be32"

```
 

 **提示：** 
-  `1 <= formula.length <= 1000` 
-  `formula` 由英文字母、数字、 `'('` 和 `')'` 组成
-  `formula` 总是有效的化学式
- 输出的所有值总是在 32-bit 整数范围内
 
**标签**
`栈` `哈希表` `字符串` `排序` 


## 
```python

```
>
# 727.最小窗口子序列
[https://leetcode-cn.com/problems/minimum-window-subsequence](https://leetcode-cn.com/problems/minimum-window-subsequence) 
## 原题

 
**标签**
`字符串` `动态规划` `滑动窗口` 


## 
```python

```
>
# 728.自除数
[https://leetcode-cn.com/problems/self-dividing-numbers](https://leetcode-cn.com/problems/self-dividing-numbers) 
## 原题
 **自除数** 是指可以被它包含的每一位数整除的数。
- 例如， `128` 是一个 **自除数** ，因为 `128 % 1 == 0` ， `128 % 2 == 0` ， `128 % 8 == 0` 。
 **自除数** 不允许包含 0 。

给定两个整数 `left` 和 `right` ，返回一个列表， *列表的元素是范围 `[left, right]` 内所有的 **自除数*** 。

 

 **示例 1：** 

```

输入：left = 1, right = 22
输出：[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

```
 **示例 2:** 

```

输入：left = 47, right = 85
输出：[48,55,66,77]

```
 

 **提示：** 
-  `1 <= left <= right <= 10^4` 
 
**标签**
`数学` 


## 
```python

```
>
# 729.我的日程安排表 I
[https://leetcode-cn.com/problems/my-calendar-i](https://leetcode-cn.com/problems/my-calendar-i) 
## 原题
实现一个 `MyCalendar` 类来存放你的日程安排。如果要添加的日程安排不会造成 **重复预订** ，则可以存储这个新的日程安排。

当两个日程安排有一些时间上的交叉时（例如两个日程安排都在同一时间内），就会产生 **重复预订** 。

日程可以用一对整数 `start` 和 `end` 表示，这里的时间是半开区间，即 `[start, end)` , 实数 `x` 的范围为， `start <= x < end` 。

实现 `MyCalendar` 类：
-  `MyCalendar()` 初始化日历对象。
-  `boolean book(int start, int end)` 如果可以将日程安排成功添加到日历中而不会导致重复预订，返回 `true` 。否则，返回 `false` 并且不要将该日程安排添加到日历中。
 

 **示例：** 

```

输入：
["MyCalendar", "book", "book", "book"]
[[], [10, 20], [15, 25], [20, 30]]
输出：
[null, true, false, true]

解释：
MyCalendar myCalendar = new MyCalendar();
myCalendar.book(10, 20); // return True
myCalendar.book(15, 25); // return False ，这个日程安排不能添加到日历中，因为时间 15 已经被另一个日程安排预订了。
myCalendar.book(20, 30); // return True ，这个日程安排可以添加到日历中，因为第一个日程安排预订的每个时间都小于 20 ，且不包含时间 20 。
```
 

 **提示：** 
-  `0 <= start < end <= 10^9` 
- 每个测试用例，调用 `book` 方法的次数最多不超过 `1000` 次。
 
**标签**
`设计` `线段树` `有序集合` 


## 
```python

```
>
# 730.统计不同回文子序列
[https://leetcode-cn.com/problems/count-different-palindromic-subsequences](https://leetcode-cn.com/problems/count-different-palindromic-subsequences) 
## 原题
给定一个字符串 s，返回 *`s` 中不同的非空「回文子序列」个数 。* 

通过从 s 中删除 0 个或多个字符来获得子序列。

如果一个字符序列与它反转后的字符序列一致，那么它是「回文字符序列」。

如果有某个 `i` , 满足 `a<sub>i</sub> != b<sub>i</sub>` <sub> </sub>，则两个序列 `a<sub>1</sub>, a<sub>2</sub>, ...` 和 `b<sub>1</sub>, b<sub>2</sub>, ...` 不同。

 **注意：** 
- 结果可能很大，你需要对 `10^9 + 7` 取模 。
 

 **示例 1：** 

```

输入：s = 'bccb'
输出：6
解释：6 个不同的非空回文子字符序列分别为：'b', 'c', 'bb', 'cc', 'bcb', 'bccb'。
注意：'bcb' 虽然出现两次但仅计数一次。

```
 **示例 2：** 

```

输入：s = 'abcdabcdabcdabcdabcdabcdabcdabcddcbadcbadcbadcbadcbadcbadcbadcba'
输出：104860361
解释：共有 3104860382 个不同的非空回文子序列，104860361 对 10^9 + 7 取模后的值。

```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s[i]` 仅包含 `'a'` , `'b'` , `'c'` 或 `'d'` 
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 731.我的日程安排表 II
[https://leetcode-cn.com/problems/my-calendar-ii](https://leetcode-cn.com/problems/my-calendar-ii) 
## 原题
实现一个 `MyCalendar` 类来存放你的日程安排。如果要添加的时间内不会导致三重预订时，则可以存储这个新的日程安排。

 `MyCalendar` 有一个 `book(int start, int end)` 方法。它意味着在 `start` 到 `end` 时间内增加一个日程安排，注意，这里的时间是半开区间，即 `[start, end)` , 实数 `x` 的范围为， `start <= x < end` 。

当三个日程安排有一些时间上的交叉时（例如三个日程安排都在同一时间内），就会产生三重预订。

每次调用 `MyCalendar.book` 方法时，如果可以将日程安排成功添加到日历中而不会导致三重预订，返回 `true` 。否则，返回 `false` 并且不要将该日程安排添加到日历中。

请按照以下步骤调用 `MyCalendar` 类: `MyCalendar cal = new MyCalendar();` `MyCalendar.book(start, end)` 

 

 **示例：** 

```
MyCalendar();
MyCalendar.book(10, 20); // returns true
MyCalendar.book(50, 60); // returns true
MyCalendar.book(10, 40); // returns true
MyCalendar.book(5, 15); // returns false
MyCalendar.book(5, 10); // returns true
MyCalendar.book(25, 55); // returns true
解释： 
前两个日程安排可以添加至日历中。 第三个日程安排会导致双重预订，但可以添加至日历中。
第四个日程安排活动（5,15）不能添加至日历中，因为它会导致三重预订。
第五个日程安排（5,10）可以添加至日历中，因为它未使用已经双重预订的时间10。
第六个日程安排（25,55）可以添加至日历中，因为时间 [25,40] 将和第三个日程安排双重预订；
时间 [40,50] 将单独预订，时间 [50,55）将和第二个日程安排双重预订。

```
 

 **提示：** 
- 每个测试用例，调用 `MyCalendar.book` 函数最多不超过 `1000` 次。
- 调用函数 `MyCalendar.book(start, end)` 时， `start` 和 `end` 的取值范围为 `[0, 10^9]` 。
 
**标签**
`设计` `线段树` `有序集合` 


## 
```python

```
>
# 732.我的日程安排表 III
[https://leetcode-cn.com/problems/my-calendar-iii](https://leetcode-cn.com/problems/my-calendar-iii) 
## 原题
当 `k` 个日程安排有一些时间上的交叉时（例如 `k` 个日程安排都在同一时间内），就会产生 `k` 次预订。

给你一些日程安排 `[start, end)` ，请你在每个日程安排添加后，返回一个整数 `k` ，表示所有先前日程安排会产生的最大 `k` 次预订。

实现一个 `MyCalendarThree` 类来存放你的日程安排，你可以一直添加新的日程安排。
-  `MyCalendarThree()` 初始化对象。
-  `int book(int start, int end)` 返回一个整数 `k` ，表示日历中存在的 `k` 次预订的最大值。
 

 **示例：** 

```

输入：
["MyCalendarThree", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
输出：
[null, 1, 1, 2, 3, 3, 3]

解释：
MyCalendarThree myCalendarThree = new MyCalendarThree();
myCalendarThree.book(10, 20); // 返回 1 ，第一个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(50, 60); // 返回 1 ，第二个日程安排可以预订并且不存在相交，所以最大 k 次预订是 1 次预订。
myCalendarThree.book(10, 40); // 返回 2 ，第三个日程安排 [10, 40) 与第一个日程安排相交，所以最大 k 次预订是 2 次预订。
myCalendarThree.book(5, 15); // 返回 3 ，剩下的日程安排的最大 k 次预订是 3 次预订。
myCalendarThree.book(5, 10); // 返回 3
myCalendarThree.book(25, 55); // 返回 3

```
 

 **提示：** 
-  `0 <= start < end <= 10^9` 
- 每个测试用例，调用 `book`  函数最多不超过  `400` 次
 
**标签**
`设计` `线段树` `有序集合` 


## 
```python

```
>
# 733.图像渲染
[https://leetcode-cn.com/problems/flood-fill](https://leetcode-cn.com/problems/flood-fill) 
## 原题
有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标 `(sr, sc)` 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 `newColor` ，让你重新上色这幅图像。

为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，&hellip;&hellip;，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。

 **示例 1:** 

```

输入: 
image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1, sc = 1, newColor = 2
输出: [[2,2,2],[2,2,0],[2,0,1]]
解析: 
在图像的正中间，(坐标(sr,sc)=(1,1)),
在路径上所有符合条件的像素点的颜色都被更改成2。
注意，右下角的像素没有更改为2，
因为它不是在上下左右四个方向上与初始点相连的像素点。

```
 **注意:** 
-  `image` 和 `image[0]` 的长度在范围 `[1, 50]` 内。
- 给出的初始点将满足 `0 <= sr < image.length` 和 `0 <= sc < image[0].length` 。
-  `image[i][j]` 和 `newColor` 表示的颜色值在范围 `[0, 65535]` 内。
 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 734.句子相似性
[https://leetcode-cn.com/problems/sentence-similarity](https://leetcode-cn.com/problems/sentence-similarity) 
## 原题

 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 735.行星碰撞
[https://leetcode-cn.com/problems/asteroid-collision](https://leetcode-cn.com/problems/asteroid-collision) 
## 原题
给定一个整数数组 `asteroids` ，表示在同一行的行星。

对于数组中的每一个元素，其绝对值表示行星的大小，正负表示行星的移动方向（正表示向右移动，负表示向左移动）。每一颗行星以相同的速度移动。

找出碰撞后剩下的所有行星。碰撞规则：两个行星相互碰撞，较小的行星会爆炸。如果两颗行星大小相同，则两颗行星都会爆炸。两颗移动方向相同的行星，永远不会发生碰撞。

 

 **示例 1：** 

```

输入：asteroids = [5,10,-5]
输出：[5,10]
解释：10 和 -5 碰撞后只剩下 10 。 5 和 10 永远不会发生碰撞。
```
 **示例 2：** 

```

输入：asteroids = [8,-8]
输出：[]
解释：8 和 -8 碰撞后，两者都发生爆炸。
```
 **示例 3：** 

```

输入：asteroids = [10,2,-5]
输出：[10]
解释：2 和 -5 发生碰撞后剩下 -5 。10 和 -5 发生碰撞后剩下 10 。
```
 **示例 4：** 

```

输入：asteroids = [-2,-1,1,2]
输出：[-2,-1,1,2]
解释：-2 和 -1 向左移动，而 1 和 2 向右移动。 由于移动方向相同的行星不会发生碰撞，所以最终没有行星发生碰撞。 
```
 

 **提示：** 
-  `2 <= asteroids.length <= 10^4` 
-  `-1000 <= asteroids[i] <= 1000` 
-  `asteroids[i] != 0` 
 
**标签**
`栈` `数组` 


## 
```python

```
>
# 736.Lisp 语法解析
[https://leetcode-cn.com/problems/parse-lisp-expression](https://leetcode-cn.com/problems/parse-lisp-expression) 
## 原题
给你一个类似 Lisp 语句的字符串表达式 `expression` ，求出其计算结果。

表达式语法如下所示:
- 表达式可以为整数， **let** 表达式， **add** 表达式， **mult** 表达式，或赋值的变量。表达式的结果总是一个整数。
- (整数可以是正整数、负整数、0)
-  **let** 表达式采用 `"(let v<sub>1</sub> e<sub>1</sub> v<sub>2</sub> e<sub>2</sub> ... v<sub>n</sub> e<sub>n</sub> expr)"` 的形式，其中 `let` 总是以字符串 `"let"` 来表示，接下来会跟随一对或多对交替的变量和表达式，也就是说，第一个变量 `v<sub>1</sub>` 被分配为表达式 `e<sub>1</sub>` 的值，第二个变量 `v<sub>2</sub>` 被分配为表达式 `e<sub>2</sub>` 的值， **依次类推** ；最终 `let` 表达式的值为 `expr` 表达式的值。
-  **add** 表达式表示为 `"(add e<sub>1</sub> e<sub>2</sub>)"` ，其中 `add` 总是以字符串 `"add"` 来表示，该表达式总是包含两个表达式 `e<sub>1</sub>` 、 `e<sub>2</sub>` ，最终结果是 `e<sub>1</sub>` 表达式的值与 `e<sub>2</sub>` 表达式的值之 **和** 。
-  **mult** 表达式表示为 `"(mult e<sub>1</sub> e<sub>2</sub>)"` ，其中 `mult` 总是以字符串 `"mult"` 表示，该表达式总是包含两个表达式 `e<sub>1</sub>` 、 `e<sub>2</sub>` ，最终结果是 `e<sub>1</sub>` 表达式的值与 `e<sub>2</sub>` 表达式的值之 **积** 。
- 在该题目中，变量名以小写字符开始，之后跟随 0 个或多个小写字符或数字。为了方便， `"add"` ， `"let"` ， `"mult"` 会被定义为 "关键字" ，不会用作变量名。
- 最后，要说一下作用域的概念。计算变量名所对应的表达式时，在计算上下文中，首先检查最内层作用域（按括号计），然后按顺序依次检查外部作用域。测试用例中每一个表达式都是合法的。有关作用域的更多详细信息，请参阅示例。

 

 **示例 1：** 

```

输入：expression = "(let x 2 (mult x (let x 3 y 4 (add x y))))"
输出：14
解释：
计算表达式 (add x y), 在检查变量 x 值时，
在变量的上下文中由最内层作用域依次向外检查。
首先找到 x = 3, 所以此处的 x 值是 3 。

```
 **示例 2：** 

```

输入：expression = "(let x 3 x 2 x)"
输出：2
解释：let 语句中的赋值运算按顺序处理即可。

```
 **示例 3：** 

```

输入：expression = "(let x 1 y 2 x (add x y) (add x y))"
输出：5
解释：
第一个 (add x y) 计算结果是 3，并且将此值赋给了 x 。 
第二个 (add x y) 计算结果是 3 + 2 = 5 。

```

 

 **提示：** 
-  `1 <= expression.length <= 2000` 
-  `exprssion` 中不含前导和尾随空格
-  `expressoin` 中的不同部分（token）之间用单个空格进行分隔
- 答案和所有中间计算结果都符合 **32-bit** 整数范围
- 测试用例中的表达式均为合法的且最终结果为整数
 
**标签**
`栈` `递归` `哈希表` `字符串` 


## 
```python

```
>
# 737.句子相似性 II
[https://leetcode-cn.com/problems/sentence-similarity-ii](https://leetcode-cn.com/problems/sentence-similarity-ii) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `哈希表` `字符串` 


## 
```python

```
>
# 738.单调递增的数字
[https://leetcode-cn.com/problems/monotone-increasing-digits](https://leetcode-cn.com/problems/monotone-increasing-digits) 
## 原题
当且仅当每个相邻位数上的数字 `x` 和 `y` 满足 `x <= y` 时，我们称这个整数是 **单调递增** 的。

给定一个整数 `n` ，返回 *小于或等于 `n` 的最大数字，且数字呈 **单调递增*** 。

 

 **示例 1:** 

```

输入: n = 10
输出: 9

```
 **示例 2:** 

```

输入: n = 1234
输出: 1234

```
 **示例 3:** 

```

输入: n = 332
输出: 299

```
 

 **提示:** 
-  `0 <= n <= 10^9` 
 
**标签**
`贪心` `数学` 


## 
```python

```
>
# 739.每日温度
[https://leetcode-cn.com/problems/daily-temperatures](https://leetcode-cn.com/problems/daily-temperatures) 
## 原题
给定一个整数数组 `temperatures` ，表示每天的温度，返回一个数组 `answer` ，其中 `answer[i]` 是指在第 `i` 天之后，<span style="font-size:10.5pt"><span style="font-family:Calibri"><span style="font-size:10.5000pt"><span style="font-family:宋体"><font face="宋体">才会有更高的温度</font></span></span></span></span>。如果气温在这之后都不会升高，请在该位置用 `0` 来代替。

 

 **示例 1:** 

```

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]

```
 **示例 2:** 

```

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]

```
 **示例 3:** 

```

输入: temperatures = [30,60,90]
输出: [1,1,0]
```
 

 **提示：** 
-  `1 <= temperatures.length <= 10^5` 
-  `30 <= temperatures[i] <= 100` 
 
**标签**
`栈` `数组` `单调栈` 


## 
```python

```
>
# 740.删除并获得点数
[https://leetcode-cn.com/problems/delete-and-earn](https://leetcode-cn.com/problems/delete-and-earn) 
## 原题
给你一个整数数组  `nums`  ，你可以对它进行一些操作。

每次操作中，选择任意一个  `nums[i]`  ，删除它并获得  `nums[i]`  的点数。之后，你必须删除 **所有** 等于  `nums[i] - 1` 和 `nums[i] + 1`  的元素。

开始你拥有 `0` 个点数。返回你能通过这些操作获得的最大点数。

 

 **示例 1：** 

```

输入：nums = [3,4,2]
输出：6
解释：
删除 4 获得 4 个点数，因此 3 也被删除。
之后，删除 2 获得 2 个点数。总共获得 6 个点数。

```
 **示例 2：** 

```

输入：nums = [2,2,3,3,3,4]
输出：9
解释：
删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
总共获得 9 个点数。

```
 

 **提示：** 
-  `1 <= nums.length <= 2 * 10^4` 
-  `1 <= nums[i] <= 10^4` 
 
**标签**
`数组` `哈希表` `动态规划` 


## 
```python

```
>
# 741.摘樱桃
[https://leetcode-cn.com/problems/cherry-pickup](https://leetcode-cn.com/problems/cherry-pickup) 
## 原题
一个N x N的网格 `(grid)` 代表了一块樱桃地，每个格子由以下三种数字的一种来表示：
- 0 表示这个格子是空的，所以你可以穿过它。
- 1 表示这个格子里装着一个樱桃，你可以摘到樱桃然后穿过它。
- -1 表示这个格子里有荆棘，挡着你的路。
你的任务是在遵守下列规则的情况下，尽可能的摘到最多樱桃：
- 从位置 (0, 0) 出发，最后到达 (N-1, N-1) ，只能向下或向右走，并且只能穿越有效的格子（即只可以穿过值为0或者1的格子）；
- 当到达 (N-1, N-1) 后，你要继续走，直到返回到 (0, 0) ，只能向上或向左走，并且只能穿越有效的格子；
- 当你经过一个格子且这个格子包含一个樱桃时，你将摘到樱桃并且这个格子会变成空的（值变为0）；
- 如果在 (0, 0) 和 (N-1, N-1) 之间不存在一条可经过的路径，则没有任何一个樱桃能被摘到。
 **示例 1:** 

```

输入: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
输出: 5
解释： 
玩家从（0,0）点出发，经过了向下走，向下走，向右走，向右走，到达了点(2, 2)。
在这趟单程中，总共摘到了4颗樱桃，矩阵变成了[[0,1,-1],[0,0,-1],[0,0,0]]。
接着，这名玩家向左走，向上走，向上走，向左走，返回了起始点，又摘到了1颗樱桃。
在旅程中，总共摘到了5颗樱桃，这是可以摘到的最大值了。

```
 **说明:** 
-  `grid` 是一个 `N` * `N` 的二维数组，N的取值范围是 `1 <= N <= 50` 。
- 每一个 `grid[i][j]` 都是集合 `{-1, 0, 1}` 其中的一个数。
- 可以保证起点 `grid[0][0]` 和终点 `grid[N-1][N-1]` 的值都不会是 -1。
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 742.二叉树最近的叶节点
[https://leetcode-cn.com/problems/closest-leaf-in-a-binary-tree](https://leetcode-cn.com/problems/closest-leaf-in-a-binary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 743.网络延迟时间
[https://leetcode-cn.com/problems/network-delay-time](https://leetcode-cn.com/problems/network-delay-time) 
## 原题
有 `n` 个网络节点，标记为 `1` 到 `n` 。

给你一个列表 `times` ，表示信号经过 **有向** 边的传递时间。 `times[i] = (u<sub>i</sub>, v<sub>i</sub>, w<sub>i</sub>)` ，其中 `u<sub>i</sub>` 是源节点， `v<sub>i</sub>` 是目标节点， `w<sub>i</sub>` 是一个信号从源节点传递到目标节点的时间。

现在，从某个节点 `K` 发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回 `-1` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2019/05/23/931_example_1.png" style="height: 220px; width: 200px;" />

```

输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2

```
 **示例 2：** 

```

输入：times = [[1,2,1]], n = 2, k = 1
输出：1

```
 **示例 3：** 

```

输入：times = [[1,2,1]], n = 2, k = 2
输出：-1

```
 

 **提示：** 
-  `1 <= k <= n <= 100` 
-  `1 <= times.length <= 6000` 
-  `times[i].length == 3` 
-  `1 <= u<sub>i</sub>, v<sub>i</sub> <= n` 
-  `u<sub>i</sub> != v<sub>i</sub>` 
-  `0 <= w<sub>i</sub> <= 100` 
- 所有 `(u<sub>i</sub>, v<sub>i</sub>)` 对都 **互不相同** （即，不含重复边）
 
**标签**
`深度优先搜索` `广度优先搜索` `图` `最短路` `堆（优先队列）` 


## 
```python

```
>
# 744.寻找比目标字母大的最小字母
[https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target](https://leetcode-cn.com/problems/find-smallest-letter-greater-than-target) 
## 原题
给你一个排序后的字符列表 `letters` ，列表中只包含小写英文字母。另给出一个目标字母 `target` ，请你寻找在这一有序列表里比目标字母大的最小字母。

在比较时，字母是依序循环出现的。举个例子：
- 如果目标字母 `target = 'z'` 并且字符列表为 `letters = ['a', 'b']` ，则答案返回 `'a'` 
 

 **示例 1：** 

```

输入: letters = ["c", "f", "j"]，target = "a"
输出: "c"

```
 **示例 2:** 

```

输入: letters = ["c","f","j"], target = "c"
输出: "f"

```
 **示例 3:** 

```

输入: letters = ["c","f","j"], target = "d"
输出: "f"

```
 

 **提示：** 
-  `2 <= letters.length <= 10^4` 
-  `letters[i]` 是一个小写字母
-  `letters` 按非递减顺序排序
-  `letters` 最少包含两个不同的字母
-  `target` 是一个小写字母
 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 745.前缀和后缀搜索
[https://leetcode-cn.com/problems/prefix-and-suffix-search](https://leetcode-cn.com/problems/prefix-and-suffix-search) 
## 原题
设计一个包含一些单词的特殊词典，并能够通过前缀和后缀来检索单词。

实现 `WordFilter` 类：
-  `WordFilter(string[] words)` 使用词典中的单词 `words` 初始化对象。
-  `f(string prefix, string suffix)` 返回词典中具有前缀  `prefix`  和后缀 `suffix`  的单词的下标。如果存在不止一个满足要求的下标，返回其中 **最大的下标** 。如果不存在这样的单词，返回 `-1` 。
 

 **示例** 

```

输入：
["WordFilter", "f"]
[[["apple"]], ["a", "e"]]
输出：
[null, 0]

解释：
WordFilter wordFilter = new WordFilter(["apple"]);
wordFilter.f("a", "e"); // 返回 0 ，因为下标为 0 的单词的 prefix = "a" 且 suffix = 'e" 。

```

 

 **提示：** 
-  `1 <= words.length <= 15000` 
-  `1 <= words[i].length <= 10` 
-  `1 <= prefix.length, suffix.length <= 10` 
-  `words[i]` 、 `prefix` 和 `suffix` 仅由小写英文字母组成
- 最多对函数  `f` 进行 `15000` 次调用
 
**标签**
`设计` `字典树` `字符串` 


## 
```python

```
>
# 746.使用最小花费爬楼梯
[https://leetcode-cn.com/problems/min-cost-climbing-stairs](https://leetcode-cn.com/problems/min-cost-climbing-stairs) 
## 原题
给你一个整数数组 `cost` ，其中 `cost[i]` 是从楼梯第 `i` 个台阶向上爬需要支付的费用。一旦你支付此费用，即可选择向上爬一个或者两个台阶。

你可以选择从下标为 `0` 或下标为 `1` 的台阶开始爬楼梯。

请你计算并返回达到楼梯顶部的最低花费。

 

 **示例 1：** 

```

输入：cost = [10,15,20]
输出：15
解释：你将从下标为 1 的台阶开始。
- 支付 15 ，向上爬两个台阶，到达楼梯顶部。
总花费为 15 。

```
 **示例 2：** 

```

输入：cost = [1,100,1,1,1,100,1,1,100,1]
输出：6
解释：你将从下标为 0 的台阶开始。
- 支付 1 ，向上爬两个台阶，到达下标为 2 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 4 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 6 的台阶。
- 支付 1 ，向上爬一个台阶，到达下标为 7 的台阶。
- 支付 1 ，向上爬两个台阶，到达下标为 9 的台阶。
- 支付 1 ，向上爬一个台阶，到达楼梯顶部。
总花费为 6 。

```
 

 **提示：** 
-  `2 <= cost.length <= 1000` 
-  `0 <= cost[i] <= 999` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 747.至少是其他数字两倍的最大数
[https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others](https://leetcode-cn.com/problems/largest-number-at-least-twice-of-others) 
## 原题
给你一个整数数组 `nums` ，其中总是存在 **唯一的** 一个最大整数 。

请你找出数组中的最大元素并检查它是否 **至少是数组中每个其他数字的两倍** 。如果是，则返回 **最大元素的下标** ，否则返回 `-1` 。

 

 **示例 1：** 

```

输入：nums = [3,6,1,0]
输出：1
解释：6 是最大的整数，对于数组中的其他整数，6 至少是数组中其他元素的两倍。6 的下标是 1 ，所以返回 1 。

```
 **示例 2：** 

```

输入：nums = [1,2,3,4]
输出：-1
解释：4 没有超过 3 的两倍大，所以返回 -1 。
```
 **示例 3：** 

```

输入：nums = [1]
输出：0
解释：因为不存在其他数字，所以认为现有数字 1 至少是其他数字的两倍。

```
 

 **提示：** 
-  `1 <= nums.length <= 50` 
-  `0 <= nums[i] <= 100` 
-  `nums` 中的最大元素是唯一的
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 748.最短补全词
[https://leetcode-cn.com/problems/shortest-completing-word](https://leetcode-cn.com/problems/shortest-completing-word) 
## 原题
给你一个字符串 `licensePlate` 和一个字符串数组 `words` ，请你找出 `words` 中的 **最短补全词** 。

 **补全词** 是一个包含 `licensePlate` 中所有字母的单词。 **忽略** `licensePlate` 中的 **数字和空格** 。 **不区分大小写** 。如果某个字母在 `licensePlate` 中出现不止一次，那么该字母在补全词中的出现次数应当一致或者更多。

例如： `licensePlate` `= "aBc 12c"` ，那么它的补全词应当包含字母 `'a'` 、 `'b'` （忽略大写）和两个 `'c'` 。可能的 **补全词** 有 `"abccdef"` 、 `"caaacab"` 以及 `"cbca"` 。

请返回 `words` 中的 **最短补全词** 。题目数据保证一定存在一个最短补全词。当有多个单词都符合最短补全词的匹配条件时取 `words` 中 **第一个** 出现的那个。

 

 **示例 1：** 

```

输入：licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
输出："steps"
解释：最短补全词应该包括 "s"、"p"、"s"（忽略大小写） 以及 "t"。
"step" 包含 "t"、"p"，但只包含一个 "s"，所以它不符合条件。
"steps" 包含 "t"、"p" 和两个 "s"。
"stripe" 缺一个 "s"。
"stepple" 缺一个 "s"。
因此，"steps" 是唯一一个包含所有字母的单词，也是本例的答案。
```
 **示例 2：** 

```

输入：licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
输出："pest"
解释：licensePlate 只包含字母 "s" 。所有的单词都包含字母 "s" ，其中 "pest"、"stew"、和 "show" 三者最短。答案是 "pest" ，因为它是三个单词中在 words 里最靠前的那个。

```
 

 **提示：** 
-  `1 <= licensePlate.length <= 7` 
-  `licensePlate` 由数字、大小写字母或空格 `' '` 组成
-  `1 <= words.length <= 1000` 
-  `1 <= words[i].length <= 15` 
-  `words[i]` 由小写英文字母组成
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 749.隔离病毒
[https://leetcode-cn.com/problems/contain-virus](https://leetcode-cn.com/problems/contain-virus) 
## 原题
病毒扩散得很快，现在你的任务是尽可能地通过安装防火墙来隔离病毒。

假设世界由 `m x n` 的二维矩阵 `isInfected` 组成， `isInfected[i][j] == 0` 表示该区域未感染病毒，而 `isInfected[i][j] == 1` 表示该区域已感染病毒。可以在任意 2 个相邻单元之间的共享边界上安装一个防火墙（并且只有一个防火墙）。

每天晚上，病毒会从被感染区域向相邻未感染区域扩散，除非被防火墙隔离。现由于资源有限，每天你只能安装一系列防火墙来隔离其中一个被病毒感染的区域（一个区域或连续的一片区域），且该感染区域对未感染区域的威胁最大且 **保证唯一** 。

你需要努力使得最后有部分区域不被病毒感染，如果可以成功，那么返回需要使用的防火墙个数; 如果无法实现，则返回在世界被病毒全部感染时已安装的防火墙个数。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/06/01/virus11-grid.jpg" style="height: 255px; width: 500px;" />

```

输入: isInfected = [[0,1,0,0,0,0,0,1],[0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0]]
输出: 10
解释:一共有两块被病毒感染的区域。
在第一天，添加 5 墙隔离病毒区域的左侧。病毒传播后的状态是:

第二天，在右侧添加 5 个墙来隔离病毒区域。此时病毒已经被完全控制住了。
<img src="https://assets.leetcode.com/uploads/2021/06/01/virus13edited-grid.jpg" style="height: 261px; width: 500px;" />

```
 **示例 2：** 

<img src="https://assets.leetcode.com/uploads/2021/06/01/virus2-grid.jpg" style="height: 253px; width: 653px;" />

```

输入: isInfected = [[1,1,1],[1,0,1],[1,1,1]]
输出: 4
解释: 虽然只保存了一个小区域，但却有四面墙。
注意，防火墙只建立在两个不同区域的共享边界上。

```
 **示例 3:** 

```

输入: isInfected = [[1,1,1,0,0,0,0,0,0],[1,0,1,0,1,1,1,1,1],[1,1,1,0,0,0,0,0,0]]
输出: 13
解释: 在隔离右边感染区域后，隔离左边病毒区域只需要 2 个防火墙。

```
 

 **提示:** 
-  `m == isInfected.length` 
-  `n == isInfected[i].length` 
-  `1 <= m, n <= 50` 
-  `isInfected[i][j]` is either `0` or `1` 
- 在整个描述的过程中，总有一个相邻的病毒区域，它将在下一轮 **严格地感染更多未受污染的方块** 
 

 
**标签**
`深度优先搜索` `广度优先搜索` `数组` `矩阵` `模拟` 


## 
```python

```
>
# 750.角矩形的数量
[https://leetcode-cn.com/problems/number-of-corner-rectangles](https://leetcode-cn.com/problems/number-of-corner-rectangles) 
## 原题

 
**标签**
`数组` `数学` `动态规划` `矩阵` 


## 
```python

```
>
# 751.IP 到 CIDR
[https://leetcode-cn.com/problems/ip-to-cidr](https://leetcode-cn.com/problems/ip-to-cidr) 
## 原题

 
**标签**
`位运算` `字符串` 


## 
```python

```
>
# 752.打开转盘锁
[https://leetcode-cn.com/problems/open-the-lock](https://leetcode-cn.com/problems/open-the-lock) 
## 原题
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'` 。每个拨轮可以自由旋转：例如把 `'9'` 变为  `'0'` ， `'0'` 变为 `'9'` 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 `'0000'` ，一个代表四个拨轮的数字的字符串。

列表 `deadends` 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 `target` 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 `-1` 。

 

 **示例 1:** 

```

输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
输出：6
解释：
可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
因为当拨动到 "0102" 时这个锁就会被锁定。

```
 **示例 2:** 

```

输入: deadends = ["8888"], target = "0009"
输出：1
解释：
把最后一位反向旋转一次即可 "0000" -> "0009"。

```
 **示例 3:** 

```

输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
输出：-1
解释：
无法旋转到目标数字且不被锁定。

```
 **示例 4:** 

```

输入: deadends = ["0000"], target = "8888"
输出：-1

```
 

 **提示：** 
-  `1 <= deadends.length <= 500` 
-  `<font face="monospace">deadends[i].length == 4</font>` 
-  `<font face="monospace">target.length == 4</font>` 
-  `target` **不在** `deadends` 之中
-  `target` 和 `deadends[i]` 仅由若干位数字组成
 
**标签**
`广度优先搜索` `数组` `哈希表` `字符串` 


## 
```python

```
>
# 753.破解保险箱
[https://leetcode-cn.com/problems/cracking-the-safe](https://leetcode-cn.com/problems/cracking-the-safe) 
## 原题
有一个需要密码才能打开的保险箱。密码是 `n` 位数, 密码的每一位是 `k` 位序列 `0, 1, ..., k-1` 中的一个 。

你可以随意输入密码，保险箱会自动记住最后 `n` 位输入，如果匹配，则能够打开保险箱。

举个例子，假设密码是 `"345"` ，你可以输入 `"012345"` 来打开它，只是你输入了 6 个字符.

请返回一个能打开保险箱的最短字符串。

 

 **示例1:** 

```
输入: n = 1, k = 2
输出: "01"
说明: "10"也可以打开保险箱。

```
 

 **示例2:** 

```
输入: n = 2, k = 2
输出: "00110"
说明: "01100", "10011", "11001" 也能打开保险箱。

```
 

 **提示：** 
-  `n` 的范围是 `[1, 4]` 。
-  `k` 的范围是 `[1, 10]` 。
-  `k^n` 最大可能为 `4096` 。
 

 
**标签**
`深度优先搜索` `图` `欧拉回路` 


## 
```python

```
>
# 754.到达终点数字
[https://leetcode-cn.com/problems/reach-a-number](https://leetcode-cn.com/problems/reach-a-number) 
## 原题
在一根无限长的数轴上，你站在 `0` 的位置。终点在 `target` 的位置。

你可以做一些数量的移动 `numMoves` :
- 每次你可以选择向左或向右移动。
- 第 `i` 次移动（从 `i == 1` 开始，到 `i == numMoves` ），在选择的方向上走 `i` 步。
给定整数 `target` ，返回 *到达目标所需的 **最小** 移动次数(即最小 `numMoves` )* 。

 

 **示例 1:** 

```

输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。

```
 **示例 2:** 

```

输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。

```
 

 **提示:** 
-  `-10^9 <= target <= 10^9` 
-  `target != 0` 
 
**标签**
`数学` `二分查找` 


## 
```python

```
>
# 755.倒水
[https://leetcode-cn.com/problems/pour-water](https://leetcode-cn.com/problems/pour-water) 
## 原题

 
**标签**
`数组` `模拟` 


## 
```python

```
>
# 756.金字塔转换矩阵
[https://leetcode-cn.com/problems/pyramid-transition-matrix](https://leetcode-cn.com/problems/pyramid-transition-matrix) 
## 原题
现在，我们用一些方块来堆砌一个金字塔。 每个方块用仅包含一个字母的字符串表示。

使用三元组表示金字塔的堆砌规则如下：

对于三元组 `ABC` ， `C` 为顶层方块，方块 `A` 、 `B` 分别作为方块 `C` 下一层的的左、右子块。当且仅当 `ABC` 是被允许的三元组，我们才可以将其堆砌上。

初始时，给定金字塔的基层  `bottom` ，用一个字符串表示。一个允许的三元组列表  `allowed` ，每个三元组用一个长度为 3 的字符串表示。

如果可以由基层一直堆到塔尖就返回 `true` ，否则返回 `false` 。

 

 **示例 1：** 

```

输入：bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
输出：true
解释：
可以堆砌成这样的金字塔:
    A
   / \
  G   E
 / \ / \
B   C   D

因为符合 BCG、CDE 和 GEA 三种规则。

```
 **示例 2：** 

```

输入：bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
输出：false
解释：
无法一直堆到塔尖。
注意, 允许存在像 ABC 和 ABD 这样的三元组，其中 C != D。

```
 

 **提示：** 
-  `bottom` 的长度范围在  `[2, 8]` 。
-  `allowed` 的长度范围在 `[0, 200]` 。
- 方块的标记字母范围为 `{'A', 'B', 'C', 'D', 'E', 'F', 'G'}` 。
 
**标签**
`位运算` `深度优先搜索` `广度优先搜索` 


## 
```python

```
>
# 757.设置交集大小至少为2
[https://leetcode-cn.com/problems/set-intersection-size-at-least-two](https://leetcode-cn.com/problems/set-intersection-size-at-least-two) 
## 原题
一个整数区间 `[a, b]` ( `a < b` ) 代表着从 `a` 到 `b` 的所有连续整数，包括 `a` 和 `b` 。

给你一组整数区间 `intervals` ，请找到一个最小的集合 S，使得 S 里的元素与区间 `intervals` 中的每一个整数区间都至少有2个元素相交。

输出这个最小集合S的大小。

 **示例 1:** 

```
输入: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
输出: 3
解释:
考虑集合 S = {2, 3, 4}. S与intervals中的四个区间都有至少2个相交的元素。
且这是S最小的情况，故我们输出3。

```
 **示例 2:** 

```
输入: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
输出: 5
解释:
最小的集合S = {1, 2, 3, 4, 5}.

```
 **注意:** 
-  `intervals` 的长度范围为 `[1, 3000]` 。
-  `intervals[i]` 长度为 `2` ，分别代表左、右边界。
-  `intervals[i][j]` 的值是 `[0, 10^8]` 范围内的整数。
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 758.字符串中的加粗单词
[https://leetcode-cn.com/problems/bold-words-in-string](https://leetcode-cn.com/problems/bold-words-in-string) 
## 原题

 
**标签**
`字典树` `数组` `哈希表` `字符串` `字符串匹配` 


## 
```python

```
>
# 759.员工空闲时间
[https://leetcode-cn.com/problems/employee-free-time](https://leetcode-cn.com/problems/employee-free-time) 
## 原题

 
**标签**
`数组` `排序` `堆（优先队列）` 


## 
```python

```
>
# 760.找出变位映射
[https://leetcode-cn.com/problems/find-anagram-mappings](https://leetcode-cn.com/problems/find-anagram-mappings) 
## 原题

 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 761.特殊的二进制序列
[https://leetcode-cn.com/problems/special-binary-string](https://leetcode-cn.com/problems/special-binary-string) 
## 原题
特殊的二进制序列是具有以下两个性质的二进制序列：
- 0 的数量与 1 的数量相等。
- 二进制序列的每一个前缀码中 1 的数量要大于等于 0 的数量。
给定一个特殊的二进制序列 `S` ，以字符串形式表示。定义一个 *操作* 为首先选择 `S` 的两个连续且非空的特殊的子串，然后将它们交换。（两个子串为连续的当且仅当第一个子串的最后一个字符恰好为第二个子串的第一个字符的前一个字符。)

在任意次数的操作之后，交换后的字符串按照字典序排列的最大的结果是什么？

 **示例 1:** 

```

输入: S = "11011000"
输出: "11100100"
解释:
将子串 "10" （在S[1]出现） 和 "1100" （在S[3]出现）进行交换。
这是在进行若干次操作后按字典序排列最大的结果。

```
 **说明:** 
-  `S` 的长度不超过 `50` 。
-  `S` 保证为一个满足上述定义的 *特殊* 的二进制序列。
 
**标签**
`递归` `字符串` 


## 
```python

```
>
# 762.二进制表示中质数个计算置位
[https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation](https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation) 
## 原题
给定两个整数 `L` 和 `R` ，找到闭区间 `[L, R]` 范围内，计算置位位数为质数的整数个数。

（注意，计算置位代表二进制表示中1的个数。例如 `21` 的二进制表示 `10101` 有 3 个计算置位。还有，1 不是质数。）

 **示例 1:** 

```

输入: L = 6, R = 10
输出: 4
解释:
6 -> 110 (2 个计算置位，2 是质数)
7 -> 111 (3 个计算置位，3 是质数)
9 -> 1001 (2 个计算置位，2 是质数)
10-> 1010 (2 个计算置位，2 是质数)

```
 **示例 2:** 

```

输入: L = 10, R = 15
输出: 5
解释:
10 -> 1010 (2 个计算置位, 2 是质数)
11 -> 1011 (3 个计算置位, 3 是质数)
12 -> 1100 (2 个计算置位, 2 是质数)
13 -> 1101 (3 个计算置位, 3 是质数)
14 -> 1110 (3 个计算置位, 3 是质数)
15 -> 1111 (4 个计算置位, 4 不是质数)

```
 **注意:** 
-  `L, R` 是 `L <= R` 且在 `[1, 10^6]` 中的整数。
-  `R - L` 的最大值为 10000。
 
**标签**
`位运算` `数学` 


## 
```python

```
>
# 763.划分字母区间
[https://leetcode-cn.com/problems/partition-labels](https://leetcode-cn.com/problems/partition-labels) 
## 原题
字符串 `S` 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

 

 **示例：** 

```

输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

```
 

 **提示：** 
-  `S` 的长度在 `[1, 500]` 之间。
-  `S` 只包含小写字母 `'a'` 到 `'z'` 。
 
**标签**
`贪心` `哈希表` `双指针` `字符串` 


## 
```python

```
>
# 764.最大加号标志
[https://leetcode-cn.com/problems/largest-plus-sign](https://leetcode-cn.com/problems/largest-plus-sign) 
## 原题
在一个 `n x n` 的矩阵 `grid` 中，除了在数组 `mines` 中给出的元素为 `0` ，其他每个元素都为 `1` 。 `mines[i] = [x<sub>i</sub>, y<sub>i</sub>]` 表示 `grid[x<sub>i</sub>][y<sub>i</sub>] == 0` 

返回  `grid` *中包含 `1` 的最大的 **轴对齐** 加号标志的阶数* 。如果未找到加号标志，则返回 `0` 。

一个 `k` 阶由 *`1`* 组成的 **“轴对称”加号标志** 具有中心网格 `grid[r][c] == 1` ，以及4个从中心向上、向下、向左、向右延伸，长度为 `k-1` ，由 `1` 组成的臂。注意，只有加号标志的所有网格要求为 `1` ，别的网格可能为 `0` 也可能为 `1` 。

 

 **示例 1：** 

<img src="https://assets.leetcode.com/uploads/2021/06/13/plus1-grid.jpg" />

```

输入: n = 5, mines = [[4, 2]]
输出: 2
解释: 在上面的网格中，最大加号标志的阶只能是2。一个标志已在图中标出。

```
 **示例 2：** 

<img src="https://assets.leetcode.com/uploads/2021/06/13/plus2-grid.jpg" />

```

输入: n = 1, mines = [[0, 0]]
输出: 0
解释: 没有加号标志，返回 0 。

```
 

 **提示：** 
-  `1 <= n <= 500` 
-  `1 <= mines.length <= 5000` 
-  `0 <= x<sub>i</sub>, y<sub>i</sub> < n` 
- 每一对 `(x<sub>i</sub>, y<sub>i</sub>)` 都 **不重复** ​​​​​​​
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 765.情侣牵手
[https://leetcode-cn.com/problems/couples-holding-hands](https://leetcode-cn.com/problems/couples-holding-hands) 
## 原题
 `n` 对情侣坐在连续排列的 `2n` 个座位上，想要牵到对方的手。

人和座位由一个整数数组 `row` 表示，其中 `row[i]` 是坐在第 `i` 个座位上的人的 **ID** 。情侣们按顺序编号，第一对是 `(0, 1)` ，第二对是 `(2, 3)` ，以此类推，最后一对是 `(2n-2, 2n-1)` 。

返回 *最少交换座位的次数，以便每对情侣可以并肩坐在一起* 。 <i>每次</i>交换可选择任意两人，让他们站起来交换座位。

 

 **示例 1:** 

```

输入: row = [0,2,1,3]
输出: 1
解释: 只需要交换row[1]和row[2]的位置即可。

```
 **示例 2:** 

```

输入: row = [3,2,0,1]
输出: 0
解释: 无需交换座位，所有的情侣都已经可以手牵手了。

```
 

 **提示:** 
-  `2n == row.length` 
-  `2 <= n <= 30` 
-  `n` 是偶数
-  `0 <= row[i] < 2n` 
-  `row` 中所有元素均 **无重复** 
 
**标签**
`贪心` `深度优先搜索` `广度优先搜索` `并查集` `图` 


## 
```python

```
>
# 766.托普利茨矩阵
[https://leetcode-cn.com/problems/toeplitz-matrix](https://leetcode-cn.com/problems/toeplitz-matrix) 
## 原题
给你一个 `m x n` 的矩阵 `matrix` 。如果这个矩阵是托普利茨矩阵，返回 `true` ；否则，返回 `false` *。* 

如果矩阵上每一条由左上到右下的对角线上的元素都相同，那么这个矩阵是 **托普利茨矩阵** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/ex1.jpg" style="width: 322px; height: 242px;" />
```

输入：matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
输出：true
解释：
在上述矩阵中, 其对角线为: 
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]"。 
各条对角线上的所有元素均相同, 因此答案是 True 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/04/ex2.jpg" style="width: 162px; height: 162px;" />
```

输入：matrix = [[1,2],[2,2]]
输出：false
解释：
对角线 "[1, 2]" 上的元素不同。
```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m, n <= 20` 
-  `0 <= matrix[i][j] <= 99` 
 

 **进阶：** 
- 如果矩阵存储在磁盘上，并且内存有限，以至于一次最多只能将矩阵的一行加载到内存中，该怎么办？
- 如果矩阵太大，以至于一次只能将不完整的一行加载到内存中，该怎么办？
 
**标签**
`数组` `矩阵` 


## 
```python

```
>
# 767.重构字符串
[https://leetcode-cn.com/problems/reorganize-string](https://leetcode-cn.com/problems/reorganize-string) 
## 原题
给定一个字符串 `S` ，检查是否能重新排布其中的字母，使得两相邻的字符不同。

若可行，输出任意可行的结果。若不可行，返回空字符串。

 **示例 1:** 

```

输入: S = "aab"
输出: "aba"

```
 **示例 2:** 

```

输入: S = "aaab"
输出: ""

```
 **注意:** 
-  `S` 只包含小写字母并且长度在 `[1, 500]` 区间内。
 
**标签**
`贪心` `哈希表` `字符串` `计数` `排序` `堆（优先队列）` 


## 
```python

```
>
# 768.最多能完成排序的块 II
[https://leetcode-cn.com/problems/max-chunks-to-make-sorted-ii](https://leetcode-cn.com/problems/max-chunks-to-make-sorted-ii) 
## 原题
 *这个问题和“最多能完成排序的块”相似，但给定数组中的元素可以重复，输入数组最大长度为 `2000` ，其中的元素最大为 `10**8` 。* 

 `arr` 是一个可能包含 **重复元素** 的整数数组，我们将这个数组分割成几个“块”，并将这些块分别进行排序。之后再连接起来，使得连接的结果和按升序排序后的原数组相同。

我们最多能将数组分成多少块？

 **示例 1:** 

```

输入: arr = [5,4,3,2,1]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [5, 4], [3, 2, 1] 的结果是 [4, 5, 1, 2, 3]，这不是有序的数组。 

```
 **示例 2:** 

```

输入: arr = [2,1,3,4,4]
输出: 4
解释:
我们可以把它分成两块，例如 [2, 1], [3, 4, 4]。
然而，分成 [2, 1], [3], [4], [4] 可以得到最多的块数。 

```
 **注意:** 
-  `arr` 的长度在 `[1, 2000]` 之间。
-  `arr[i]` 的大小在 `[0, 10**8]` 之间。
 
**标签**
`栈` `贪心` `数组` `排序` `单调栈` 


## 
```python

```
>
# 769.最多能完成排序的块
[https://leetcode-cn.com/problems/max-chunks-to-make-sorted](https://leetcode-cn.com/problems/max-chunks-to-make-sorted) 
## 原题
给定一个长度为 `n` 的整数数组 `arr` ，它表示在 `[0, n - 1]` 范围内的整数的排列。

我们将 `arr` 分割成若干 **块** (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。

返回数组能分成的最多块数量。

 

 **示例 1:** 

```

输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。

```
 **示例 2:** 

```

输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。

```
 

 **提示:** 
-  `n == arr.length` 
-  `1 <= n <= 10` 
-  `0 <= arr[i] < n` 
-  `arr` 中每个元素都 **不同** 
 
**标签**
`栈` `贪心` `数组` `排序` `单调栈` 


## 
```python

```
>
# 770.基本计算器 IV
[https://leetcode-cn.com/problems/basic-calculator-iv](https://leetcode-cn.com/problems/basic-calculator-iv) 
## 原题
给定一个表达式如 `expression = "e + 8 - a + 5"` 和一个求值映射，如 `{"e": 1}` （给定的形式为 `evalvars = ["e"]` 和 `evalints = [1]` ），返回表示简化表达式的标记列表，例如 `["-1*a","14"]` 
- 表达式交替使用块和符号，每个块和符号之间有一个空格。
- 块要么是括号中的表达式，要么是变量，要么是非负整数。
- 变量是一个由小写字母组成的字符串（不包括数字）。请注意，变量可以是多个字母，并注意变量从不具有像 `"2x"` 或 `"-x"` 这样的前导系数或一元运算符 。
表达式按通常顺序进行求值：先是括号，然后求乘法，再计算加法和减法。
- 例如， `expression = "1 + 2 * 3"` 的答案是 `["7"]` 。
输出格式如下：
- 对于系数非零的每个自变量项，我们按字典排序的顺序将自变量写在一个项中。
	
- 例如，我们永远不会写像 `“b*a*c”` 这样的项，只写 `“a*b*c”` 。
	
	
- 项的次数等于被乘的自变量的数目，并计算重复项。我们先写出答案的最大次数项，用字典顺序打破关系，此时忽略词的前导系数。
	
- 例如， `"a*a*b*c"` 的次数为 4。
	
	
- 项的前导系数直接放在左边，用星号将它与变量分隔开(如果存在的话)。前导系数 1 仍然要打印出来。
- 格式良好的一个示例答案是 `["-2*a*a*a", "3*a*a*b", "3*b*b", "4*a", "5*c", "-6"]` 。
- 系数为 `0` 的项（包括常数项）不包括在内。
	
- 例如， `“0”` 的表达式输出为 `[]` 。
	
	
 

 **示例 1：** 

```

输入：expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
输出：["-1*a","14"]

```
 **示例 2：** 

```

输入：expression = "e - 8 + temperature - pressure",
evalvars = ["e", "temperature"], evalints = [1, 12]
输出：["-1*pressure","5"]

```
 **示例 3：** 

```

输入：expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
输出：["1*e*e","-64"]

```
 

 **提示：** 
-  `1 <= expression.length <= 250` 
-  `expression` 由小写英文字母，数字 `'+'` , `'-'` , `'*'` , `'('` , `')'` , `' '` 组成
-  `expression` 不包含任何前空格或后空格
-  `expression` 中的所有符号都用一个空格隔开
-  `0 <= evalvars.length <= 100` 
-  `1 <= evalvars[i].length <= 20` 
-  `evalvars[i]` 由小写英文字母组成
-  `evalints.length == evalvars.length` 
-  `-100 <= evalints[i] <= 100` 
 
**标签**
`栈` `递归` `哈希表` `数学` `字符串` 


## 
```python

```
>
# 771.宝石与石头
[https://leetcode-cn.com/problems/jewels-and-stones](https://leetcode-cn.com/problems/jewels-and-stones) 
## 原题
 给你一个字符串 `jewels` 代表石头中宝石的类型，另有一个字符串 `stones` 代表你拥有的石头。 `stones` 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

字母区分大小写，因此 `"a"` 和 `"A"` 是不同类型的石头。

 

 **示例 1：** 

```

输入：jewels = "aA", stones = "aAAbbbb"
输出：3

```
 **示例 2：** 

```

输入：jewels = "z", stones = "ZZ"
输出：0

```
 

 **提示：** 
-  `1 <= jewels.length, stones.length <= 50` 
-  `jewels` 和 `stones` 仅由英文字母组成
-  `jewels` 中的所有字符都是 **唯一的** 
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 772.基本计算器 III
[https://leetcode-cn.com/problems/basic-calculator-iii](https://leetcode-cn.com/problems/basic-calculator-iii) 
## 原题

 
**标签**
`栈` `递归` `数学` `字符串` 


## 
```python

```
>
# 773.滑动谜题
[https://leetcode-cn.com/problems/sliding-puzzle](https://leetcode-cn.com/problems/sliding-puzzle) 
## 原题
在一个 2 x 3 的板上（ `board` ）有 5 块砖瓦，用数字 `1~5` 来表示, 以及一块空缺用 `0` 来表示.

一次移动定义为选择 `0` 与一个相邻的数字（上下左右）进行交换.

最终当板 `board` 的结果是 `[[1,2,3],[4,5,0]]` 谜板被解开。

给出一个谜板的初始状态，返回最少可以通过多少次移动解开谜板，如果不能解开谜板，则返回 -1 。

 **示例：** 

```

输入：board = [[1,2,3],[4,0,5]]
输出：1
解释：交换 0 和 5 ，1 步完成

```
```

输入：board = [[1,2,3],[5,4,0]]
输出：-1
解释：没有办法完成谜板

```
```

输入：board = [[4,1,2],[5,0,3]]
输出：5
解释：
最少完成谜板的最少移动次数是 5 ，
一种移动路径:
尚未移动: [[4,1,2],[5,0,3]]
移动 1 次: [[4,1,2],[0,5,3]]
移动 2 次: [[0,1,2],[4,5,3]]
移动 3 次: [[1,0,2],[4,5,3]]
移动 4 次: [[1,2,0],[4,5,3]]
移动 5 次: [[1,2,3],[4,5,0]]

```
```

输入：board = [[3,2,4],[1,5,0]]
输出：14

```
 **提示：** 
-  `board` 是一个如上所述的 2 x 3 的数组.
-  `board[i][j]` 是一个 `[0, 1, 2, 3, 4, 5]` 的排列.
 
**标签**
`广度优先搜索` `数组` `矩阵` 


## 
```python

```
>
# 774.最小化去加油站的最大距离
[https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station](https://leetcode-cn.com/problems/minimize-max-distance-to-gas-station) 
## 原题

 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 775.全局倒置与局部倒置
[https://leetcode-cn.com/problems/global-and-local-inversions](https://leetcode-cn.com/problems/global-and-local-inversions) 
## 原题
给你一个长度为 `n` 的整数数组 `nums` ，表示由范围 `[0, n - 1]` 内所有整数组成的一个排列。

 **全局倒置** 的数目等于满足下述条件不同下标对 `(i, j)` 的数目：
-  `0 <= i < j < n` 
-  `nums[i] > nums[j]` 
 **局部倒置** 的数目等于满足下述条件的下标 `i` 的数目：
-  `0 <= i < n - 1` 
-  `nums[i] > nums[i + 1]` 
当数组 `nums` 中 **全局倒置** 的数量等于 **局部倒置** 的数量时，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：nums = [1,0,2]
输出：true
解释：有 1 个全局倒置，和 1 个局部倒置。

```
 **示例 2：** 

```

输入：nums = [1,2,0]
输出：false
解释：有 2 个全局倒置，和 1 个局部倒置。

```

 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 5000` 
-  `0 <= nums[i] < n` 
-  `nums` 中的所有整数 **互不相同** 
-  `nums` 是范围 `[0, n - 1]` 内所有数字组成的一个排列
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 776.拆分二叉搜索树
[https://leetcode-cn.com/problems/split-bst](https://leetcode-cn.com/problems/split-bst) 
## 原题

 
**标签**
`树` `二叉搜索树` `递归` `二叉树` 


## 
```python

```
>
# 777.在LR字符串中交换相邻字符
[https://leetcode-cn.com/problems/swap-adjacent-in-lr-string](https://leetcode-cn.com/problems/swap-adjacent-in-lr-string) 
## 原题
在一个由 `';L';` , `';R';` 和 `';X';` 三个字符组成的字符串（例如 `"RXXLRXRXL"` ）中进行移动操作。一次移动操作指用一个 `"LX"` 替换一个 `"XL"` ，或者用一个 `"XR"` 替换一个 `"RX"` 。现给定起始字符串 `start` 和结束字符串 `end` ，请编写代码，当且仅当存在一系列移动操作使得 `start` 可以转换成 `end` 时， 返回 `True` 。

 

 **示例 :** 

```
输入: start = "RXXLRXRXL", end = "XRLXXRRLX"
输出: True
解释:
我们可以通过以下几步将start转换成end:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

```
 

 **提示：** 
-  `1 <= len(start) = len(end) <= 10000` 。
-  `start` 和 `end` 中的字符串仅限于 `';L';` , `';R';` 和 `';X';` 。
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 778.水位上升的泳池中游泳
[https://leetcode-cn.com/problems/swim-in-rising-water](https://leetcode-cn.com/problems/swim-in-rising-water) 
## 原题
在一个 `n x n` 的整数矩阵 `grid` 中，每一个方格的值 `grid[i][j]` 表示位置 `(i, j)` 的平台高度。

当开始下雨时，在时间为 `t` 时，水池中的水位为 `t` 。你可以从一个平台游向四周相邻的任意一个平台，但是前提是此时水位必须同时淹没这两个平台。假定你可以瞬间移动无限距离，也就是默认在方格内部游动是不耗时的。当然，在你游泳的时候你必须待在坐标方格里面。

你从坐标方格的左上平台 `(0，0)` 出发。返回 *你到达坐标方格的右下平台 `(n-1, n-1)` 所需的最少时间 。* 

 

 **示例 1:** 

<img src="https://assets.leetcode.com/uploads/2021/06/29/swim1-grid.jpg" />

```

输入: grid = [[0,2],[1,3]]
输出: 3
解释:
时间为0时，你位于坐标方格的位置为 (0, 0)。
此时你不能游向任意方向，因为四个相邻方向平台的高度都大于当前时间为 0 时的水位。
等时间到达 3 时，你才可以游向平台 (1, 1). 因为此时的水位是 3，坐标方格中的平台没有比水位 3 更高的，所以你可以游向坐标方格中的任意位置

```
 **示例 2:** 

<img src="https://assets.leetcode.com/uploads/2021/06/29/swim2-grid-1.jpg" />

```

输入: grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
输出: 16
解释: 最终的路线用加粗进行了标记。
我们必须等到时间为 16，此时才能保证平台 (0, 0) 和 (4, 4) 是连通的

```
 

 **提示:** 
-  `n == grid.length` 
-  `n == grid[i].length` 
-  `1 <= n <= 50` 
-  `0 <= grid[i][j] < n^2` 
-  `grid[i][j]` 中每个值 **均无重复** 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `二分查找` `矩阵` `堆（优先队列）` 


## 
```python

```
>
# 779.第K个语法符号
[https://leetcode-cn.com/problems/k-th-symbol-in-grammar](https://leetcode-cn.com/problems/k-th-symbol-in-grammar) 
## 原题
在第一行我们写上一个 `0` 。接下来的每一行，将前一行中的 `0` 替换为 `01` ， `1` 替换为 `10` 。

给定行数 `N` 和序数 `K` ，返回第 `N` 行中第 `K` 个字符。（ `K` 从1开始）

<br>
 **例子:** 

```
输入: N = 1, K = 1
输出: 0

输入: N = 2, K = 1
输出: 0

输入: N = 2, K = 2
输出: 1

输入: N = 4, K = 5
输出: 1

解释:
第一行: 0
第二行: 01
第三行: 0110
第四行: 01101001

```
<br>
 **注意：** 
-  `N` 的范围 `[1, 30]` .
-  `K` 的范围 `[1, 2^(N-1)]` .
 
**标签**
`位运算` `递归` `数学` 


## 
```python

```
>
# 780.到达终点
[https://leetcode-cn.com/problems/reaching-points](https://leetcode-cn.com/problems/reaching-points) 
## 原题
给定四个整数 `sx` , `sy` ， `tx` 和 `ty` ，如果通过一系列的 **转换** 可以从起点 `(sx, sy)` 到达终点 `(tx, ty)` ，则返回 `true` ，否则返回 `false` 。

从点 `(x, y)` 可以 **转换** 到 `(x, x+y)` 或者 `(x+y, y)` 。

 

 **示例 1:** 

```

输入: sx = 1, sy = 1, tx = 3, ty = 5
输出: true
解释:
可以通过以下一系列转换从起点转换到终点：
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

```
 **示例 2:** 

```

输入: sx = 1, sy = 1, tx = 2, ty = 2 
输出: false

```
 **示例 3:** 

```

输入: sx = 1, sy = 1, tx = 1, ty = 1 
输出: true

```
 

 **提示:** 
-  `1 <= sx, sy, tx, ty <= 10^9` 
 
**标签**
`数学` 


## 
```python

```
>
# 781.森林中的兔子
[https://leetcode-cn.com/problems/rabbits-in-forest](https://leetcode-cn.com/problems/rabbits-in-forest) 
## 原题
森林中有未知数量的兔子。提问其中若干只兔子 **"还有多少只兔子与你（指被提问的兔子）颜色相同?"** ，将答案收集到一个整数数组 `answers` 中，其中 `answers[i]` 是第 `i` 只兔子的回答。

给你数组 `answers` ，返回森林中兔子的最少数量。

 

 **示例 1：** 

```

输入：answers = [1,1,2]
输出：5
解释：
两只回答了 "1" 的兔子可能有相同的颜色，设为红色。 
之后回答了 "2" 的兔子不会是红色，否则他们的回答会相互矛盾。
设回答了 "2" 的兔子为蓝色。 
此外，森林中还应有另外 2 只蓝色兔子的回答没有包含在数组中。 
因此森林中兔子的最少数量是 5 只：3 只回答的和 2 只没有回答的。

```
 **示例 2：** 

```

输入：answers = [10,10,10]
输出：11

```
 

 **提示：** 
-  `1 <= answers.length <= 1000` 
-  `0 <= answers[i] < 1000` 
 
**标签**
`贪心` `数组` `哈希表` `数学` 


## 
```python

```
>
# 782.变为棋盘
[https://leetcode-cn.com/problems/transform-to-chessboard](https://leetcode-cn.com/problems/transform-to-chessboard) 
## 原题
一个 N x N的 `board` 仅由 `0` 和 `1` 组成 。每次移动，你能任意交换两列或是两行的位置。

输出将这个矩阵变为 “棋盘” 所需的最小移动次数。“棋盘” 是指任意一格的上下左右四个方向的值均与本身不同的矩阵。如果不存在可行的变换，输出 -1。

```
示例:
输入: board = [[0,1,1,0],[0,1,1,0],[1,0,0,1],[1,0,0,1]]
输出: 2
解释:
一种可行的变换方式如下，从左到右：

0110     1010     1010
0110 --> 1010 --> 0101
1001     0101     1010
1001     0101     0101

第一次移动交换了第一列和第二列。
第二次移动交换了第二行和第三行。
输入: board = [[0, 1], [1, 0]]
输出: 0
解释:
注意左上角的格值为0时也是合法的棋盘，如：

01
10

也是合法的棋盘.

输入: board = [[1, 0], [1, 0]]
输出: -1
解释:
任意的变换都不能使这个输入变为合法的棋盘。

```
 

 **提示：** 
-  `board` 是方阵，且行列数的范围是 `[2, 30]` 。
-  `board[i][j]` 将只包含 `0` 或 `1` 。
 
**标签**
`位运算` `数组` `数学` `矩阵` 


## 
```python

```
>
# 783.二叉搜索树节点最小距离
[https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes](https://leetcode-cn.com/problems/minimum-distance-between-bst-nodes) 
## 原题
给你一个二叉搜索树的根节点 `root` ，返回 **树中任意两不同节点值之间的最小差值** 。

差值是一个正数，其数值等于两值之差的绝对值。

 
 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst1.jpg" style="width: 292px; height: 301px;" />
```

输入：root = [4,2,6,1,3]
输出：1

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/bst2.jpg" style="width: 282px; height: 301px;" />
```

输入：root = [1,0,48,null,null,12,49]
输出：1

```
 

 **提示：** 
- 树中节点的数目范围是 `[2, 100]` 
-  `0 <= Node.val <= 10^5` 
 

 **注意：** 本题与 530：<a href="https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/">https://leetcode-cn.com/problems/minimum-absolute-difference-in-bst/</a> 相同
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 784.字母大小写全排列
[https://leetcode-cn.com/problems/letter-case-permutation](https://leetcode-cn.com/problems/letter-case-permutation) 
## 原题
给定一个字符串 `S` ，通过将字符串 `S` 中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

 

```
示例：
输入：S = "a1b2"
输出：["a1b2", "a1B2", "A1b2", "A1B2"]

输入：S = "3z4"
输出：["3z4", "3Z4"]

输入：S = "12345"
输出：["12345"]

```
 

 **提示：** 
-  `S` 的长度不超过 `12` 。
-  `S` 仅由数字和字母组成。
 
**标签**
`位运算` `字符串` `回溯` 


## 
```python

```
>
# 785.判断二分图
[https://leetcode-cn.com/problems/is-graph-bipartite](https://leetcode-cn.com/problems/is-graph-bipartite) 
## 原题
存在一个 **无向图** ，图中有 `n` 个节点。其中每个节点都有一个介于 `0` 到 `n - 1` 之间的唯一编号。给你一个二维数组 `graph` ，其中 `graph[u]` 是一个节点数组，由节点 `u` 的邻接节点组成。形式上，对于  `graph[u]` 中的每个 `v` ，都存在一条位于节点 `u` 和节点 `v` 之间的无向边。该无向图同时具有以下属性：

- 不存在自环（ `graph[u]` 不包含 `u` ）。
- 不存在平行边（ `graph[u]` 不包含重复值）。
- 如果 `v` 在 `graph[u]` 内，那么 `u` 也应该在 `graph[v]` 内（该图是无向图）
- 这个图可能不是连通图，也就是说两个节点 `u` 和 `v` 之间可能不存在一条连通彼此的路径。
 **二分图** 定义：如果能将一个图的节点集合分割成两个独立的子集 `A` 和 `B` ，并使图中的每一条边的两个节点一个来自 `A` 集合，一个来自 `B` 集合，就将这个图称为 **二分图** 。

如果图是二分图，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/21/bi2.jpg" style="width: 222px; height: 222px;" />
```

输入：graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
输出：false
解释：不能将节点分割成两个独立的子集，以使每条边都连通一个子集中的一个节点与另一个子集中的一个节点。
```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/21/bi1.jpg" style="width: 222px; height: 222px;" />
```

输入：graph = [[1,3],[0,2],[1,3],[0,2]]
输出：true
解释：可以将节点分成两组: {0, 2} 和 {1, 3} 。
```
 

 **提示：** 
-  `graph.length == n` 
-  `1 <= n <= 100` 
-  `0 <= graph[u].length < n` 
-  `0 <= graph[u][i] <= n - 1` 
-  `graph[u]` 不会包含 `u` 
-  `graph[u]` 的所有值 **互不相同** 
- 如果 `graph[u]` 包含 `v` ，那么 `graph[v]` 也会包含 `u` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `图` 


## 
```python

```
>
# 786.第 K 个最小的素数分数
[https://leetcode-cn.com/problems/k-th-smallest-prime-fraction](https://leetcode-cn.com/problems/k-th-smallest-prime-fraction) 
## 原题
给你一个按递增顺序排序的数组 `arr` 和一个整数 `k` 。数组 `arr` 由 `1` 和若干 **素数** 组成，且其中所有整数互不相同。

对于每对满足 `0 <= i < j < arr.length` 的 `i` 和 `j` ，可以得到分数 `arr[i] / arr[j]` 。

那么第 `k` 个最小的分数是多少呢?  以长度为 `2` 的整数数组返回你的答案, 这里 `answer[0] == arr[i]` 且 `answer[1] == arr[j]` 。
 

 **示例 1：** 

```

输入：arr = [1,2,3,5], k = 3
输出：[2,5]
解释：已构造好的分数,排序后如下所示: 
1/5, 1/3, 2/5, 1/2, 3/5, 2/3
很明显第三个最小的分数是 2/5

```
 **示例 2：** 

```

输入：arr = [1,7], k = 1
输出：[1,7]

```
 

 **提示：** 
-  `2 <= arr.length <= 1000` 
-  `1 <= arr[i] <= 3 * 10^4` 
-  `arr[0] == 1` 
-  `arr[i]` 是一个 **素数** ， `i > 0` 
-  `arr` 中的所有数字 **互不相同** ，且按 **严格递增** 排序
-  `1 <= k <= arr.length * (arr.length - 1) / 2` 
 
**标签**
`数组` `二分查找` `堆（优先队列）` 


## 
```python

```
>
# 787.K 站中转内最便宜的航班
[https://leetcode-cn.com/problems/cheapest-flights-within-k-stops](https://leetcode-cn.com/problems/cheapest-flights-within-k-stops) 
## 原题
有 `n` 个城市通过一些航班连接。给你一个数组 `flights` ，其中 `flights[i] = [from<sub>i</sub>, to<sub>i</sub>, price<sub>i</sub>]` ，表示该航班都从城市 `from<sub>i</sub>` 开始，以价格 `price<sub>i</sub>` 抵达 `to<sub>i</sub>` 。

现在给定所有的城市和航班，以及出发城市 `src` 和目的地 `dst` ，你的任务是找到出一条最多经过 `k` 站中转的路线，使得从 `src` 到 `dst` 的 **价格最便宜** ，并返回该价格。 如果不存在这样的路线，则输出 `-1` 。

 

 **示例 1：** 

```

输入: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
输出: 200
解释: 
城市航班图如下
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height: 180px; width: 246px;" />

从城市 0 到城市 2 在 1 站中转以内的最便宜价格是 200，如图中红色所示。
```
 **示例 2：** 

```

输入: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
输出: 500
解释: 
城市航班图如下
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/02/16/995.png" style="height: 180px; width: 246px;" />

从城市 0 到城市 2 在 0 站中转以内的最便宜价格是 500，如图中蓝色所示。
```
 

 **提示：** 
-  `1 <= n <= 100` 
-  `0 <= flights.length <= (n * (n - 1) / 2)` 
-  `flights[i].length == 3` 
-  `0 <= from<sub>i</sub>, to<sub>i</sub> < n` 
-  `from<sub>i</sub> != to<sub>i</sub>` 
-  `1 <= price<sub>i</sub> <= 10^4` 
- 航班没有重复，且不存在自环
-  `0 <= src, dst, k < n` 
-  `src != dst` 
 
**标签**
`深度优先搜索` `广度优先搜索` `图` `动态规划` `最短路` `堆（优先队列）` 


## 
```python

```
>
# 788.旋转数字
[https://leetcode-cn.com/problems/rotated-digits](https://leetcode-cn.com/problems/rotated-digits) 
## 原题
我们称一个数 X 为好数, 如果它的每位数字逐个地被旋转 180 度后，我们仍可以得到一个有效的，且和 X 不同的数。要求每位数字都要被旋转。

如果一个数的每位数字被旋转以后仍然还是一个数字， 则这个数是有效的。0, 1, 和 8 被旋转后仍然是它们自己；2 和 5 可以互相旋转成对方（在这种情况下，它们以不同的方向旋转，换句话说，2 和 5 互为镜像）；6 和 9 同理，除了这些以外其他的数字旋转以后都不再是有效的数字。

现在我们有一个正整数 `N` , 计算从 `1` 到 `N` 中有多少个数 X 是好数？

 

 **示例：** 

```
输入: 10
输出: 4
解释: 
在[1, 10]中有四个好数： 2, 5, 6, 9。
注意 1 和 10 不是好数, 因为他们在旋转之后不变。

```
 

 **提示：** 
- N 的取值范围是 `[1, 10000]` 。
 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 789.逃脱阻碍者
[https://leetcode-cn.com/problems/escape-the-ghosts](https://leetcode-cn.com/problems/escape-the-ghosts) 
## 原题
你在进行一个简化版的吃豆人游戏。你从 `[0, 0]` 点开始出发，你的目的地是 `target = [x<sub>target</sub>, y<sub>target</sub>]` 。地图上有一些阻碍者，以数组 `ghosts` 给出，第 `i` 个阻碍者从 `ghosts[i] = [x<sub>i</sub>, y<sub>i</sub>]` 出发。所有输入均为 **整数坐标** 。

每一回合，你和阻碍者们可以同时向东，西，南，北四个方向移动，每次可以移动到距离原位置 **1 个单位** 的新位置。当然，也可以选择 **不动** 。所有动作 **同时** 发生。

如果你可以在任何阻碍者抓住你 **之前** 到达目的地（阻碍者可以采取任意行动方式），则被视为逃脱成功。如果你和阻碍者 **同时** 到达了一个位置（包括目的地） **都不算** 是逃脱成功。

只有在你有可能成功逃脱时，输出 `true` ；否则，输出 `false` 。
 

 **示例 1：** 

```

输入：ghosts = [[1,0],[0,3]], target = [0,1]
输出：true
解释：你可以直接一步到达目的地 (0,1) ，在 (1, 0) 或者 (0, 3) 位置的阻碍者都不可能抓住你。 

```
 **示例 2：** 

```

输入：ghosts = [[1,0]], target = [2,0]
输出：false
解释：你需要走到位于 (2, 0) 的目的地，但是在 (1, 0) 的阻碍者位于你和目的地之间。 

```
 **示例 3：** 

```

输入：ghosts = [[2,0]], target = [1,0]
输出：false
解释：阻碍者可以和你同时达到目的地。 

```
 

 **提示：** 
-  `1 <= ghosts.length <= 100` 
-  `ghosts[i].length == 2` 
-  `-10^4 <= x<sub>i</sub>, y<sub>i</sub> <= 10^4` 
- 同一位置可能有 **多个阻碍者** 。
-  `target.length == 2` 
-  `-10^4 <= x<sub>target</sub>, y<sub>target</sub> <= 10^4` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 790.多米诺和托米诺平铺
[https://leetcode-cn.com/problems/domino-and-tromino-tiling](https://leetcode-cn.com/problems/domino-and-tromino-tiling) 
## 原题
有两种形状的瓷砖：一种是 `2 x 1` 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。

<img src="https://assets.leetcode.com/uploads/2021/07/15/lc-domino.jpg" style="height: 195px; width: 362px;" />

给定整数 n ，返回可以平铺 `2 x n` 的面板的方法的数量。 **返回对** `10^9 + 7` **取模** 的值。

平铺指的是每个正方形都必须有瓷砖覆盖。两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。

 

 **示例 1:** 

<img src="https://assets.leetcode.com/uploads/2021/07/15/lc-domino1.jpg" style="height: 226px; width: 500px;" />

```

输入: n = 3
输出: 5
解释: 五种不同的方法如上所示。

```
 **示例 2:** 

```

输入: n = 1
输出: 1

```
 

 **提示：** 
-  `1 <= n <= 1000` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 791.自定义字符串排序
[https://leetcode-cn.com/problems/custom-sort-string](https://leetcode-cn.com/problems/custom-sort-string) 
## 原题
给定两个字符串 `order` 和 `s` 。 `order` 的所有单词都是 **唯一** 的，并且以前按照一些自定义的顺序排序。

对 `s` 的字符进行置换，使其与排序的 `order` 相匹配。更具体地说，如果在 `order` 中的字符 `x` 出现字符 `y` 之前，那么在排列后的字符串中， `x` 也应该出现在 `y` 之前。

返回 *满足这个性质的 `s` 的任意排列* 。

 

 **示例 1:** 

```

输入: order = "cba", s = "abcd"
输出: "cbad"
解释: 
“a”、“b”、“c”是按顺序出现的，所以“a”、“b”、“c”的顺序应该是“c”、“b”、“a”。
因为“d”不是按顺序出现的，所以它可以在返回的字符串中的任何位置。“dcba”、“cdba”、“cbda”也是有效的输出。
```
 **示例 2:** 

```

输入: order = "cbafg", s = "abcd"
输出: "cbad"

```
 

 **提示:** 
-  `1 <= order.length <= 26` 
-  `1 <= s.length <= 200` 
-  `order` 和 `s` 由小写英文字母组成
-  `order` 中的所有字符都 **不同** 
 
**标签**
`哈希表` `字符串` `排序` 


## 
```python

```
>
# 792.匹配子序列的单词数
[https://leetcode-cn.com/problems/number-of-matching-subsequences](https://leetcode-cn.com/problems/number-of-matching-subsequences) 
## 原题
给定字符串 `s` 和字符串数组 `words` , 返回 *`words[i]` 中是 `s` 的子序列的单词个数* 。

字符串的 **子序列** 是从原始字符串中生成的新字符串，可以从中删去一些字符(可以是none)，而不改变其余字符的相对顺序。
- 例如， `“ace”` 是 `“abcde”` 的子序列。
 

 **示例 1:** 

```

输入: s = "abcde", words = ["a","bb","acd","ace"]
输出: 3
解释: 有三个是 s 的子序列的单词: "a", "acd", "ace"。

```
 **Example 2:** 

```

输入: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
输出: 2

```
 

 **提示:** 
-  `1 <= s.length <= 5 * 10^4` 
-  `1 <= words.length <= 5000` 
-  `1 <= words[i].length <= 50` 
-  `words[i]` 和 <font color="#c7254e" face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size: 12.6px; background-color: rgb(249, 242, 244);">s</span></font> 都只由小写字母组成。

<span style="display:block"><span style="height:0px"><span style="position:absolute">​​​​</span></span></span>
 
**标签**
`字典树` `哈希表` `字符串` `排序` 


## 
```python

```
>
# 793.阶乘函数后 K 个零
[https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function](https://leetcode-cn.com/problems/preimage-size-of-factorial-zeroes-function) 
## 原题
 `f(x)` 是 `x!` 末尾是 0 的数量。回想一下 `x! = 1 * 2 * 3 * ... * x` ，且 `0! = 1` 。
- 例如， `f(3) = 0` ，因为 `3! = 6` 的末尾没有 0 ；而 `f(11) = 2` ，因为 `11!= 39916800` 末端有 2 个 0 。
给定 `k` ，找出返回能满足 `f(x) = k` 的非负整数 `x` 的数量。

 

 **示例 1：** **** 

```

输入：k = 0
输出：5
解释：0!, 1!, 2!, 3!, 和 4! 均符合 k = 0 的条件。

```
 **示例 2：** 

```

输入：k = 5
输出：0
解释：没有匹配到这样的 x!，符合 k = 5 的条件。
```
 **示例 3:** 

```

输入: k = 3
输出: 5

```
 

 **提示:** 
-  `0 <= k <= 10^9` 
 
**标签**
`数学` `二分查找` 


## 
```python

```
>
# 794.有效的井字游戏
[https://leetcode-cn.com/problems/valid-tic-tac-toe-state](https://leetcode-cn.com/problems/valid-tic-tac-toe-state) 
## 原题
给你一个字符串数组 `board` 表示井字游戏的棋盘。当且仅当在井字游戏过程中，棋盘有可能达到 `board` 所显示的状态时，才返回 `true` 。

井字游戏的棋盘是一个 `3 x 3` 数组，由字符 `' '` ， `'X'` 和 `'O'` 组成。字符 `' '` 代表一个空位。

以下是井字游戏的规则：
- 玩家轮流将字符放入空位（ `' '` ）中。
- 玩家 1 总是放字符 `'X'` ，而玩家 2 总是放字符 `'O'` 。
-  `'X'` 和 `'O'` 只允许放置在空位中，不允许对已放有字符的位置进行填充。
- 当有 3 个相同（且非空）的字符填充任何行、列或对角线时，游戏结束。
- 当所有位置非空时，也算为游戏结束。
- 如果游戏结束，玩家不允许再放置字符。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/15/tictactoe1-grid.jpg" style="width: 253px; height: 253px;" />
```

输入：board = ["O  ","   ","   "]
输出：false
解释：玩家 1 总是放字符 "X" 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/15/tictactoe2-grid.jpg" style="width: 253px; height: 253px;" />
```

输入：board = ["XOX"," X ","   "]
输出：false
解释：玩家应该轮流放字符。
```
 **示例 3：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/15/tictactoe3-grid.jpg" style="width: 253px; height: 253px;" />
```

输入：board = ["XXX","   ","OOO"]
输出：false

```
 **Example 4:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/15/tictactoe4-grid.jpg" style="width: 253px; height: 253px;" />
```

输入：board = ["XOX","O O","XOX"]
输出：true

```
 

 **提示：** 
-  `board.length == 3` 
-  `board[i].length == 3` 
-  `board[i][j]` 为 `'X'` 、 `'O'` 或 `' '` 
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 795.区间子数组个数
[https://leetcode-cn.com/problems/number-of-subarrays-with-bounded-maximum](https://leetcode-cn.com/problems/number-of-subarrays-with-bounded-maximum) 
## 原题
给你一个整数数组 `nums` 和两个整数： `left` 及 `right` 。找出 `nums` 中连续、非空且其中最大元素在范围 `[left, right]` 内的子数组，并返回满足条件的子数组的个数。

生成的测试用例保证结果符合 **32-bit** 整数范围。

 

 **示例 1：** 

```

输入：nums = [2,1,4,3], left = 2, right = 3
输出：3
解释：满足条件的三个子数组：[2], [2, 1], [3]

```
 **示例 2：** 

```

输入：nums = [2,9,2,5,6], left = 2, right = 8
输出：7

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^9` 
-  `0 <= left <= right <= 10^9` 
 
**标签**
`数组` `双指针` 


## 
```python

```
>
# 796.旋转字符串
[https://leetcode-cn.com/problems/rotate-string](https://leetcode-cn.com/problems/rotate-string) 
## 原题
给定两个字符串, `s` 和 `goal` 。如果在若干次旋转操作之后， `s` 能变成 `goal` ，那么返回 `true` 。

 `s` 的 **旋转操作** 就是将 `s` 最左边的字符移动到最右边。 
- 例如, 若 `s = 'abcde'` ，在旋转一次之后结果就是 `'bcdea'` 。
 

 **示例 1:** 

```

输入: s = "abcde", goal = "cdeab"
输出: true

```
 **示例 2:** 

```

输入: s = "abcde", goal = "abced"
输出: false

```
 

 **提示:** 
-  `1 <= s.length, goal.length <= 100` 
-  `s` 和 `goal` 由小写英文字母组成
 
**标签**
`字符串` `字符串匹配` 


## 
```python

```
>
# 797.所有可能的路径
[https://leetcode-cn.com/problems/all-paths-from-source-to-target](https://leetcode-cn.com/problems/all-paths-from-source-to-target) 
## 原题
给你一个有 `n` 个节点的 **有向无环图（DAG）** ，请你找出所有从节点 `0` 到节点 `n-1` 的路径并输出（ **不要求按特定顺序** ）

<meta charset="UTF-8" /> `graph[i]` 是一个从节点 `i` 可以访问的所有节点的列表（即从节点 `i` 到节点 `graph[i][j]` 存在一条有向边）。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_1.jpg" />

```

输入：graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/09/28/all_2.jpg" />

```

输入：graph = [[4,3,1],[3,2,4],[3],[4],[]]
输出：[[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]

```
 

 **提示：** 
-  `n == graph.length` 
-  `2 <= n <= 15` 
-  `0 <= graph[i][j] < n` 
-  `graph[i][j] != i` （即不存在自环）
-  `graph[i]` 中的所有元素 **互不相同** 
- 保证输入为 **有向无环图（DAG）** 
 

 
**标签**
`深度优先搜索` `广度优先搜索` `图` `回溯` 


## 
```python

```
>
# 798.得分最高的最小轮调
[https://leetcode-cn.com/problems/smallest-rotation-with-highest-score](https://leetcode-cn.com/problems/smallest-rotation-with-highest-score) 
## 原题
给定一个数组 `A` ，我们可以将它按一个非负整数 `K` 进行轮调，这样可以使数组变为 `A[K], A[K+1], A{K+2], ... A[A.length - 1], A[0], A[1], ..., A[K-1]` 的形式。此后，任何值小于或等于其索引的项都可以记作一分。

例如，如果数组为 `[2, 4, 1, 3, 0]` ，我们按 `K = 2` 进行轮调后，它将变成 `[1, 3, 0, 2, 4]` 。这将记作 3 分，因为 1 > 0 [no points], 3 > 1 [no points], 0 <= 2 [one point], 2 <= 3 [one point], 4 <= 4 [one point]。

在所有可能的轮调中，返回我们所能得到的最高分数对应的轮调索引 K。如果有多个答案，返回满足条件的最小的索引 K。

 

 **示例 1：** 

```
输入：[2, 3, 1, 4, 0]
输出：3
解释：
下面列出了每个 K 的得分：
K = 0,  A = [2,3,1,4,0],    score 2
K = 1,  A = [3,1,4,0,2],    score 3
K = 2,  A = [1,4,0,2,3],    score 3
K = 3,  A = [4,0,2,3,1],    score 4
K = 4,  A = [0,2,3,1,4],    score 3
所以我们应当选择 K = 3，得分最高。
```
 **示例 2：** 

```
输入：[1, 3, 0, 2, 4]
输出：0
解释：
A 无论怎么变化总是有 3 分。
所以我们将选择最小的 K，即 0。

```
 

 **提示：** 
-  `A` 的长度最大为 `20000` 。
-  `A[i]` 的取值范围是 `[0, A.length]` 。
 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 799.香槟塔
[https://leetcode-cn.com/problems/champagne-tower](https://leetcode-cn.com/problems/champagne-tower) 
## 原题
我们把玻璃杯摆成金字塔的形状，其中 **第一层** 有 `1` 个玻璃杯， **第二层** 有 `2` 个，依次类推到第 100 层，每个玻璃杯 (250ml) 将盛有香槟。

从顶层的第一个玻璃杯开始倾倒一些香槟，当顶层的杯子满了，任何溢出的香槟都会立刻等流量的流向左右两侧的玻璃杯。当左右两边的杯子也满了，就会等流量的流向它们左右两边的杯子，依次类推。（当最底层的玻璃杯满了，香槟会流到地板上）

例如，在倾倒一杯香槟后，最顶层的玻璃杯满了。倾倒了两杯香槟后，第二层的两个玻璃杯各自盛放一半的香槟。在倒三杯香槟后，第二层的香槟满了 - 此时总共有三个满的玻璃杯。在倒第四杯后，第三层中间的玻璃杯盛放了一半的香槟，他两边的玻璃杯各自盛放了四分之一的香槟，如下图所示。

<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/03/09/tower.png" style="height: 241px; width: 350px;" />

现在当倾倒了非负整数杯香槟后，返回第 `i` 行 `j` 个玻璃杯所盛放的香槟占玻璃杯容积的比例（ `i` 和 `j` 都从0开始）。

 

```

示例 1:
输入: poured(倾倒香槟总杯数) = 1, query_glass(杯子的位置数) = 1, query_row(行数) = 1
输出: 0.00000
解释: 我们在顶层（下标是（0，0））倒了一杯香槟后，没有溢出，因此所有在顶层以下的玻璃杯都是空的。

示例 2:
输入: poured(倾倒香槟总杯数) = 2, query_glass(杯子的位置数) = 1, query_row(行数) = 1
输出: 0.50000
解释: 我们在顶层（下标是（0，0）倒了两杯香槟后，有一杯量的香槟将从顶层溢出，位于（1，0）的玻璃杯和（1，1）的玻璃杯平分了这一杯香槟，所以每个玻璃杯有一半的香槟。

```
<meta charset="UTF-8" />

 **示例 3:** 

```

输入: poured = 100000009, query_row = 33, query_glass = 17
输出: 1.00000

```
 

 **提示:** 
-  `0 <= poured <= 10^9` 
-  `0 <= query_glass <= query_row < 100` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 800.相似 RGB 颜色
[https://leetcode-cn.com/problems/similar-rgb-color](https://leetcode-cn.com/problems/similar-rgb-color) 
## 原题

 
**标签**
`数学` `字符串` `枚举` 


## 
```python

```
>
