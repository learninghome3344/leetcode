# 601.体育馆的人流量
[https://leetcode-cn.com/problems/human-traffic-of-stadium](https://leetcode-cn.com/problems/human-traffic-of-stadium) 
## 原题
表： `Stadium` 
```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
visit_date 是表的主键
每日人流量信息被记录在这三列信息中：序号 (id)、日期 (visit_date)、 人流量 (people)
每天只有一行记录，日期随着 id 的增加而增加

```
 

编写一个 SQL 查询以找出每行的人数大于或等于 `100` 且 `id` 连续的三行或更多行记录。

返回按 `visit_date` **升序排列** 的结果表。

查询结果格式如下所示。

 

 **示例 1:** 

```

输入：
Stadium 表:
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 1    | 2017-01-01 | 10        |
| 2    | 2017-01-02 | 109       |
| 3    | 2017-01-03 | 150       |
| 4    | 2017-01-04 | 99        |
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
输出：
+------+------------+-----------+
| id   | visit_date | people    |
+------+------------+-----------+
| 5    | 2017-01-05 | 145       |
| 6    | 2017-01-06 | 1455      |
| 7    | 2017-01-07 | 199       |
| 8    | 2017-01-09 | 188       |
+------+------------+-----------+
解释：
id 为 5、6、7、8 的四行 id 连续，并且每行都有 >= 100 的人数记录。
请注意，即使第 7 行和第 8 行的 visit_date 不是连续的，输出也应当包含第 8 行，因为我们只需要考虑 id 连续的记录。
不输出 id 为 2 和 3 的行，因为至少需要三条 id 连续的记录。
```
 
**标签**
`数据库` 


## 
```python

```
>
# 602.好友申请 II ：谁有最多的好友
[https://leetcode-cn.com/problems/friend-requests-ii-who-has-the-most-friends](https://leetcode-cn.com/problems/friend-requests-ii-who-has-the-most-friends) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 603.连续空余座位
[https://leetcode-cn.com/problems/consecutive-available-seats](https://leetcode-cn.com/problems/consecutive-available-seats) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 604.迭代压缩字符串
[https://leetcode-cn.com/problems/design-compressed-string-iterator](https://leetcode-cn.com/problems/design-compressed-string-iterator) 
## 原题

 
**标签**
`设计` `数组` `哈希表` `字符串` `迭代器` 


## 
```python

```
>
# 605.种花问题
[https://leetcode-cn.com/problems/can-place-flowers](https://leetcode-cn.com/problems/can-place-flowers) 
## 原题
假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给你一个整数数组   `flowerbed` 表示花坛，由若干 `0` 和 `1` 组成，其中 `0` 表示没种植花， `1` 表示种植了花。另有一个数  `n` **** ，能否在不打破种植规则的情况下种入  `n` ** ** 朵花？能则返回 `true` ，不能则返回 `false` 。

 

 **示例 1：** 

```

输入：flowerbed = [1,0,0,0,1], n = 1
输出：true

```
 **示例 2：** 

```

输入：flowerbed = [1,0,0,0,1], n = 2
输出：false

```
 

 **提示：** 
-  `1 <= flowerbed.length <= 2 * 10^4` 
-  `flowerbed[i]` 为 `0` 或 `1` 
-  `flowerbed` 中不存在相邻的两朵花
-  `0 <= n <= flowerbed.length` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 606.根据二叉树创建字符串
[https://leetcode-cn.com/problems/construct-string-from-binary-tree](https://leetcode-cn.com/problems/construct-string-from-binary-tree) 
## 原题
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

 **示例 1:** 

```

输入: 二叉树: [1,2,3,4]
       1
     /   \
    2     3
   /    
  4     

输出: "1(2(4))(3)"

解释: 原本将是“1(2(4)())(3())”，
在你省略所有不必要的空括号对之后，
它将是“1(2(4))(3)”。

```
 **示例 2:** 

```

输入: 二叉树: [1,2,3,null,4]
       1
     /   \
    2     3
     \  
      4 

输出: "1(2()(4))(3)"

解释: 和第一个示例相似，
除了我们不能省略第一个对括号来中断输入和输出之间的一对一映射关系。

```
 
**标签**
`树` `深度优先搜索` `字符串` `二叉树` 


## 
```python

```
>
# 607.销售员
[https://leetcode-cn.com/problems/sales-person](https://leetcode-cn.com/problems/sales-person) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 608.树节点
[https://leetcode-cn.com/problems/tree-node](https://leetcode-cn.com/problems/tree-node) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 609.在系统中查找重复文件
[https://leetcode-cn.com/problems/find-duplicate-file-in-system](https://leetcode-cn.com/problems/find-duplicate-file-in-system) 
## 原题
给你一个目录信息列表 `paths` ，包括目录路径，以及该目录中的所有文件及其内容，请你按路径返回文件系统中的所有重复文件。答案可按 **任意顺序** 返回。

一组重复的文件至少包括 **两个** 具有完全相同内容的文件。

 **输入** 列表中的单个目录信息字符串的格式如下：
-  `"root/d1/d2/.../dm f1.txt(f1_content) f2.txt(f2_content) ... fn.txt(fn_content)"` 
这意味着，在目录 `root/d1/d2/.../dm` 下，有 `n` 个文件 ( `f1.txt` , `f2.txt` ... `fn.txt` ) 的内容分别是 ( `f1_content` , `f2_content` ... `fn_content` ) 。注意： `n >= 1` 且 `m >= 0` 。如果 `m = 0` ，则表示该目录是根目录。

 **输出** 是由 **重复文件路径组** 构成的列表。其中每个组由所有具有相同内容文件的文件路径组成。文件路径是具有下列格式的字符串：
-  `"directory_path/file_name.txt"` 
 

 **示例 1：** 

```

输入：paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
输出：[["root/a/2.txt","root/c/d/4.txt","root/4.txt"],["root/a/1.txt","root/c/3.txt"]]

```
 **示例 2：** 

```

输入：paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)"]
输出：[["root/a/2.txt","root/c/d/4.txt"],["root/a/1.txt","root/c/3.txt"]]

```
 

 **提示：** 
-  `1 <= paths.length <= 2 * 10^4` 
-  `1 <= paths[i].length <= 3000` 
-  `1 <= sum(paths[i].length) <= 5 * 10^5` 
-  `paths[i]` 由英文字母、数字、字符 `'/'` 、 `'.'` 、 `'('` 、 `')'` 和 `' '` 组成
- 你可以假设在同一目录中没有任何文件或目录共享相同的名称。
- 你可以假设每个给定的目录信息代表一个唯一的目录。目录路径和文件信息用单个空格分隔。
 

 **进阶：** 
- 假设您有一个真正的文件系统，您将如何搜索文件？广度搜索还是宽度搜索？
- 如果文件内容非常大（GB级别），您将如何修改您的解决方案？
- 如果每次只能读取 1 kb 的文件，您将如何修改解决方案？
- 修改后的解决方案的时间复杂度是多少？其中最耗时的部分和消耗内存的部分是什么？如何优化？
- 如何确保您发现的重复文件不是误报？
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 610.判断三角形
[https://leetcode-cn.com/problems/triangle-judgement](https://leetcode-cn.com/problems/triangle-judgement) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 611.有效三角形的个数
[https://leetcode-cn.com/problems/valid-triangle-number](https://leetcode-cn.com/problems/valid-triangle-number) 
## 原题
给定一个包含非负整数的数组 `nums` ，返回其中可以组成三角形三条边的三元组个数。

 

 **示例 1:** 

```

输入: nums = [2,2,3,4]
输出: 3
解释:有效的组合是: 
2,3,4 (使用第一个 2)
2,3,4 (使用第二个 2)
2,2,3

```
 **示例 2:** 

```

输入: nums = [4,2,3,4]
输出: 4
```
 

 **提示:** 
-  `1 <= nums.length <= 1000` 
-  `0 <= nums[i] <= 1000` 
 
**标签**
`贪心` `数组` `双指针` `二分查找` `排序` 


## 
```python

```
>
# 612.平面上的最近距离
[https://leetcode-cn.com/problems/shortest-distance-in-a-plane](https://leetcode-cn.com/problems/shortest-distance-in-a-plane) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 613.直线上的最近距离
[https://leetcode-cn.com/problems/shortest-distance-in-a-line](https://leetcode-cn.com/problems/shortest-distance-in-a-line) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 614.二级关注者
[https://leetcode-cn.com/problems/second-degree-follower](https://leetcode-cn.com/problems/second-degree-follower) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 615.平均工资：部门与公司比较
[https://leetcode-cn.com/problems/average-salary-departments-vs-company](https://leetcode-cn.com/problems/average-salary-departments-vs-company) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 616.给字符串添加加粗标签
[https://leetcode-cn.com/problems/add-bold-tag-in-string](https://leetcode-cn.com/problems/add-bold-tag-in-string) 
## 原题

 
**标签**
`字典树` `数组` `哈希表` `字符串` `字符串匹配` 


## 
```python

```
>
# 617.合并二叉树
[https://leetcode-cn.com/problems/merge-two-binary-trees](https://leetcode-cn.com/problems/merge-two-binary-trees) 
## 原题
给你两棵二叉树： `root1` 和 `root2` 。

想象一下，当你将其中一棵覆盖到另一棵之上时，两棵树上的一些节点将会重叠（而另一些不会）。你需要将这两棵树合并成一棵新二叉树。合并的规则是：如果两个节点重叠，那么将这两个节点的值相加作为合并后节点的新值；否则， **不为** null 的节点将直接作为新二叉树的节点。

返回合并后的二叉树。

 **注意:** 合并过程必须从两个树的根节点开始。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/05/merge.jpg" style="height: 163px; width: 600px;" />
```

输入：root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
输出：[3,4,5,5,4,null,7]

```
 **示例 2：** 

```

输入：root1 = [1], root2 = [1,2]
输出：[2,2]

```
 

 **提示：** 
- 两棵树中的节点数目在范围 `[0, 2000]` 内
-  `-10^4 <= Node.val <= 10^4` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 618.学生地理信息报告
[https://leetcode-cn.com/problems/students-report-by-geography](https://leetcode-cn.com/problems/students-report-by-geography) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 619.只出现一次的最大数字
[https://leetcode-cn.com/problems/biggest-single-number](https://leetcode-cn.com/problems/biggest-single-number) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 620.有趣的电影
[https://leetcode-cn.com/problems/not-boring-movies](https://leetcode-cn.com/problems/not-boring-movies) 
## 原题
某城市开了一家新的电影院，吸引了很多人过来看电影。该电影院特别注意用户体验，专门有个 LED显示板做电影推荐，上面公布着影评和相关电影描述。

作为该电影院的信息部主管，您需要编写一个 SQL查询，找出所有影片描述为 **非** `boring` (不无聊) 的并且 **id 为奇数** 的影片，结果请按等级 `rating` 排列。

 

例如，下表 `cinema` :

```

+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+

```
对于上面的例子，则正确的输出是为：

```

+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |
+---------+-----------+--------------+-----------+

```
 

 
**标签**
`数据库` 


## 
```python

```
>
# 621.任务调度器
[https://leetcode-cn.com/problems/task-scheduler](https://leetcode-cn.com/problems/task-scheduler) 
## 原题
给你一个用字符数组  `tasks` 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。

然而，两个 **相同种类** 的任务之间必须有长度为整数 **** `n` **** 的冷却时间，因此至少有连续 `n` 个单位时间内 CPU 在执行不同的任务，或者在待命状态。

你需要计算完成所有任务所需要的 **最短时间** 。

 

 **示例 1：** 

```

输入：tasks = ["A","A","A","B","B","B"], n = 2
输出：8
解释：A -> B -> (待命) -> A -> B -> (待命) -> A -> B
     在本示例中，两个相同类型任务之间必须间隔长度为 n = 2 的冷却时间，而执行一个任务只需要一个单位时间，所以中间出现了（待命）状态。 
```
 **示例 2：** 

```

输入：tasks = ["A","A","A","B","B","B"], n = 0
输出：6
解释：在这种情况下，任何大小为 6 的排列都可以满足要求，因为 n = 0
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
诸如此类

```
 **示例 3：** 

```

输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
输出：16
解释：一种可能的解决方案是：
     A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A

```
 

 **提示：** 
-  `1 <= task.length <= 10^4` 
-  `tasks[i]` 是大写英文字母
-  `n` 的取值范围为 `[0, 100]` 
 
**标签**
`贪心` `数组` `哈希表` `计数` `排序` `堆（优先队列）` 


## 
```python

```
>
# 622.设计循环队列
[https://leetcode-cn.com/problems/design-circular-queue](https://leetcode-cn.com/problems/design-circular-queue) 
## 原题
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：
-  `MyCircularQueue(k)` : 构造器，设置队列长度为 k 。
-  `Front` : 从队首获取元素。如果队列为空，返回 -1 。
-  `Rear` : 获取队尾元素。如果队列为空，返回 -1 。
-  `enQueue(value)` : 向循环队列插入一个元素。如果成功插入则返回真。
-  `deQueue()` : 从循环队列中删除一个元素。如果成功删除则返回真。
-  `isEmpty()` : 检查循环队列是否为空。
-  `isFull()` : 检查循环队列是否已满。
 

 **示例：** 

```
MyCircularQueue circularQueue = new MyCircularQueue(3); // 设置长度为 3
circularQueue.enQueue(1);  // 返回 true
circularQueue.enQueue(2);  // 返回 true
circularQueue.enQueue(3);  // 返回 true
circularQueue.enQueue(4);  // 返回 false，队列已满
circularQueue.Rear();  // 返回 3
circularQueue.isFull();  // 返回 true
circularQueue.deQueue();  // 返回 true
circularQueue.enQueue(4);  // 返回 true
circularQueue.Rear();  // 返回 4
```
 

 **提示：** 
- 所有的值都在 0 至 1000 的范围内；
- 操作数将在 1 至 1000 的范围内；
- 请不要使用内置的队列库。
 
**标签**
`设计` `队列` `数组` `链表` 


## 
```python

```
>
# 623.在二叉树中增加一行
[https://leetcode-cn.com/problems/add-one-row-to-tree](https://leetcode-cn.com/problems/add-one-row-to-tree) 
## 原题
给定一个二叉树的根 `root` 和两个整数 `val` 和 `depth` ，在给定的深度 `depth` 处添加一个值为 `val` 的节点行。

注意，根节点 `root` 位于深度 `1` 。

加法规则如下:
- 给定整数 `depth` ，对于深度为 `depth - 1` 的每个非空树节点 `cur` ，创建两个值为 `val` 的树节点作为 `cur` 的左子树根和右子树根。
-  `cur` 原来的左子树应该是新的左子树根的左子树。
-  `cur` 原来的右子树应该是新的右子树根的右子树。
- 如果 `depth == 1` 意味着 `depth - 1` 根本没有深度，那么创建一个树节点，值 `val` 作为整个原始树的新根，而原始树就是新根的左子树。
 

 **示例 1:** 

<img src="https://assets.leetcode.com/uploads/2021/03/15/addrow-tree.jpg" style="height: 231px; width: 500px;" />

```

输入: root = [4,2,6,3,1,5], val = 1, depth = 2
输出: [4,1,1,2,null,null,6,3,1,5]
```
 **示例 2:** 

<img src="https://assets.leetcode.com/uploads/2021/03/11/add2-tree.jpg" style="height: 277px; width: 500px;" />

```

输入: root = [4,2,null,3,1], val = 1, depth = 3
输出:  [4,2,null,1,1,3,null,null,1]

```
 

 **提示:** 
- 节点数在 `[1, 10^4]` 范围内
- 树的深度在 `[1, 10^4]` 范围内
-  `-100 <= Node.val <= 100` 
-  `-10^5 <= val <= 10^5` 
-  `1 <= depth <= the depth of tree + 1` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 624.数组列表中的最大距离
[https://leetcode-cn.com/problems/maximum-distance-in-arrays](https://leetcode-cn.com/problems/maximum-distance-in-arrays) 
## 原题

 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 625.最小因式分解
[https://leetcode-cn.com/problems/minimum-factorization](https://leetcode-cn.com/problems/minimum-factorization) 
## 原题

 
**标签**
`贪心` `数学` 


## 
```python

```
>
# 626.换座位
[https://leetcode-cn.com/problems/exchange-seats](https://leetcode-cn.com/problems/exchange-seats) 
## 原题
表: `Seat` 

```

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
Id是该表的主键列。
该表的每一行都表示学生的姓名和ID。
Id是一个连续的增量。

```
 

编写SQL查询来交换每两个连续的学生的座位号。如果学生的数量是奇数，则最后一个学生的id不交换。

按 `id` **升序** 返回结果表。

查询结果格式如下所示。

 

 **示例 1:** 

```

输入: 
Seat 表:
+----+---------+
| id | student |
+----+---------+
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
+----+---------+
输出: 
+----+---------+
| id | student |
+----+---------+
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
+----+---------+
解释:
请注意，如果学生人数为奇数，则不需要更换最后一名学生的座位。
```
 
**标签**
`数据库` 


## 
```python

```
>
# 627.变更性别
[https://leetcode-cn.com/problems/swap-salary](https://leetcode-cn.com/problems/swap-salary) 
## 原题


 `Salary` 表：

```

+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| id          | int      |
| name        | varchar  |
| sex         | ENUM     |
| salary      | int      |
+-------------+----------+
id 是这个表的主键。
sex 这一列的值是 ENUM 类型，只能从 ('m', 'f') 中取。
本表包含公司雇员的信息。

```
 

请你编写一个 SQL 查询来交换所有的 `'f'` 和 `'m'` （即，将所有 `'f'` 变为 `'m'` ，反之亦然），仅使用 **单个 update 语句** ，且不产生中间临时表。

注意，你必须仅使用一条 update 语句，且 **不能** 使用 select 语句。

查询结果如下例所示。

 

 **示例 1:** 

```

输入：
Salary 表：
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | m   | 2500   |
| 2  | B    | f   | 1500   |
| 3  | C    | m   | 5500   |
| 4  | D    | f   | 500    |
+----+------+-----+--------+
输出：
+----+------+-----+--------+
| id | name | sex | salary |
+----+------+-----+--------+
| 1  | A    | f   | 2500   |
| 2  | B    | m   | 1500   |
| 3  | C    | f   | 5500   |
| 4  | D    | m   | 500    |
+----+------+-----+--------+
解释：
(1, A) 和 (3, C) 从 'm' 变为 'f' 。
(2, B) 和 (4, D) 从 'f' 变为 'm' 。
```
 
**标签**
`数据库` 


## 
```python

```
>
# 628.三个数的最大乘积
[https://leetcode-cn.com/problems/maximum-product-of-three-numbers](https://leetcode-cn.com/problems/maximum-product-of-three-numbers) 
## 原题
给你一个整型数组 `nums` ，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

 

 **示例 1：** 

```

输入：nums = [1,2,3]
输出：6

```
 **示例 2：** 

```

输入：nums = [1,2,3,4]
输出：24

```
 **示例 3：** 

```

输入：nums = [-1,-2,-3]
输出：-6

```
 

 **提示：** 
-  `3 <= nums.length <= 10^4` 
-  `-1000 <= nums[i] <= 1000` 
 
**标签**
`数组` `数学` `排序` 


## 
```python

```
>
# 629.K个逆序对数组
[https://leetcode-cn.com/problems/k-inverse-pairs-array](https://leetcode-cn.com/problems/k-inverse-pairs-array) 
## 原题
给出两个整数 `n` 和 `k` ，找出所有包含从 `1` 到 `n` 的数字，且恰好拥有 `k` 个逆序对的不同的数组的个数。

逆序对的定义如下：对于数组的第 `i` 个和第 `j` 个元素，如果满 `i` < `j` 且 `a[i]` > `a[j]` ，则其为一个逆序对；否则不是。

由于答案可能很大，只需要返回 答案 mod 10^9 + 7 的值。

 **示例 1:** 

```

输入: n = 3, k = 0
输出: 1
解释: 
只有数组 [1,2,3] 包含了从1到3的整数并且正好拥有 0 个逆序对。

```
 **示例 2:** 

```

输入: n = 3, k = 1
输出: 2
解释: 
数组 [1,3,2] 和 [2,1,3] 都有 1 个逆序对。

```
 **说明:** 
-  `n` 的范围是 [1, 1000] 并且 `k` 的范围是 [0, 1000]。
 
**标签**
`动态规划` 


## 
```python

```
>
# 630.课程表 III
[https://leetcode-cn.com/problems/course-schedule-iii](https://leetcode-cn.com/problems/course-schedule-iii) 
## 原题
这里有 `n` 门不同的在线课程，按从 `1` 到 `n` 编号。给你一个数组 `courses` ，其中 `courses[i] = [duration<sub>i</sub>, lastDay<sub>i</sub>]` 表示第 `i` 门课将会 **持续** 上 `duration<sub>i</sub>` 天课，并且必须在不晚于 `lastDay<sub>i</sub>` 的时候完成。

你的学期从第 `1` 天开始。且不能同时修读两门及两门以上的课程。

返回你最多可以修读的课程数目。

 

 **示例 1：** 

```

输入：courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
输出：3
解释：
这里一共有 4 门课程，但是你最多可以修 3 门：
首先，修第 1 门课，耗费 100 天，在第 100 天完成，在第 101 天开始下门课。
第二，修第 3 门课，耗费 1000 天，在第 1100 天完成，在第 1101 天开始下门课程。
第三，修第 2 门课，耗时 200 天，在第 1300 天完成。
第 4 门课现在不能修，因为将会在第 3300 天完成它，这已经超出了关闭日期。
```
 **示例 2：** 

```

输入：courses = [[1,2]]
输出：1

```
 **示例 3：** 

```

输入：courses = [[3,2],[4,3]]
输出：0

```
 

 **提示:** 
-  `1 <= courses.length <= 10^4` 
-  `1 <= duration<sub>i</sub>, lastDay<sub>i</sub> <= 10^4` 
 
**标签**
`贪心` `数组` `堆（优先队列）` 


## 
```python

```
>
# 631.设计 Excel 求和公式
[https://leetcode-cn.com/problems/design-excel-sum-formula](https://leetcode-cn.com/problems/design-excel-sum-formula) 
## 原题

 
**标签**
`图` `设计` `拓扑排序` 


## 
```python

```
>
# 632.最小区间
[https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists](https://leetcode-cn.com/problems/smallest-range-covering-elements-from-k-lists) 
## 原题
你有 `k` 个 **非递减排列** 的整数列表。找到一个 **最小** 区间，使得 `k` 个列表中的每个列表至少有一个数包含在其中。

我们定义如果 `b-a < d-c` 或者在 `b-a == d-c` 时 `a < c` ，则区间 `[a,b]` 比 `[c,d]` 小。

 

 **示例 1：** 

```

输入：nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
输出：[20,24]
解释： 
列表 1：[4, 10, 15, 24, 26]，24 在区间 [20,24] 中。
列表 2：[0, 9, 12, 20]，20 在区间 [20,24] 中。
列表 3：[5, 18, 22, 30]，22 在区间 [20,24] 中。

```
 **示例 2：** 

```

输入：nums = [[1,2,3],[1,2,3],[1,2,3]]
输出：[1,1]

```
 

 **提示：** 
-  `nums.length == k` 
-  `1 <= k <= 3500` 
-  `1 <= nums[i].length <= 50` 
-  `-10^5 <= nums[i][j] <= 10^5` 
-  `nums[i]` 按非递减顺序排列
 

 
**标签**
`贪心` `数组` `哈希表` `排序` `滑动窗口` `堆（优先队列）` 


## 
```python

```
>
# 633.平方数之和
[https://leetcode-cn.com/problems/sum-of-square-numbers](https://leetcode-cn.com/problems/sum-of-square-numbers) 
## 原题
给定一个非负整数 `c` ，你要判断是否存在两个整数 `a` 和 `b` ，使得 `a^2 + b^2 = c` 。

 

 **示例 1：** 

```

输入：c = 5
输出：true
解释：1 * 1 + 2 * 2 = 5

```
 **示例 2：** 

```

输入：c = 3
输出：false

```
 

 **提示：** 
-  `0 <= c <= 2^31 - 1` 
 
**标签**
`数学` `双指针` `二分查找` 


## 
```python

```
>
# 634.寻找数组的错位排列
[https://leetcode-cn.com/problems/find-the-derangement-of-an-array](https://leetcode-cn.com/problems/find-the-derangement-of-an-array) 
## 原题

 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 635.设计日志存储系统
[https://leetcode-cn.com/problems/design-log-storage-system](https://leetcode-cn.com/problems/design-log-storage-system) 
## 原题

 
**标签**
`设计` `哈希表` `字符串` `有序集合` 


## 
```python

```
>
# 636.函数的独占时间
[https://leetcode-cn.com/problems/exclusive-time-of-functions](https://leetcode-cn.com/problems/exclusive-time-of-functions) 
## 原题
有一个 **单线程** CPU 正在运行一个含有 `n` 道函数的程序。每道函数都有一个位于  `0` 和 `n-1` 之间的唯一标识符。

函数调用 **存储在一个 <a href="https://baike.baidu.com/item/%E8%B0%83%E7%94%A8%E6%A0%88/22718047?fr=aladdin" target="_blank">调用栈</a> 上** ：当一个函数调用开始时，它的标识符将会推入栈中。而当一个函数调用结束时，它的标识符将会从栈中弹出。标识符位于栈顶的函数是 **当前正在执行的函数** 。每当一个函数开始或者结束时，将会记录一条日志，包括函数标识符、是开始还是结束、以及相应的时间戳。

给你一个由日志组成的列表 `logs` ，其中 `logs[i]` 表示第 `i` 条日志消息，该消息是一个按 `"{function_id}:{"start" | "end"}:{timestamp}"` 进行格式化的字符串。例如， `"0:start:3"` 意味着标识符为 `0` 的函数调用在时间戳 `3` 的 **起始开始执行** ；而 `"1:end:2"` 意味着标识符为 `1` 的函数调用在时间戳 `2` 的 **末尾结束执行** 。注意，函数可以 **调用多次，可能存在递归调用** 。

函数的 **独占时间** 定义是在这个函数在程序所有函数调用中执行时间的总和，调用其他函数花费的时间不算该函数的独占时间。例如，如果一个函数被调用两次，一次调用执行 `2` 单位时间，另一次调用执行 `1` 单位时间，那么该函数的 **独占时间** 为 `2 + 1 = 3` 。

以数组形式返回每个函数的 **独占时间** ，其中第 `i` 个下标对应的值表示标识符 `i` 的函数的独占时间。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2019/04/05/diag1b.png" style="width: 550px; height: 239px;" />
```

输入：n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
输出：[3,4]
解释：
函数 0 在时间戳 0 的起始开始执行，执行 2 个单位时间，于时间戳 1 的末尾结束执行。 
函数 1 在时间戳 2 的起始开始执行，执行 4 个单位时间，于时间戳 5 的末尾结束执行。 
函数 0 在时间戳 6 的开始恢复执行，执行 1 个单位时间。 
所以函数 0 总共执行 2 + 1 = 3 个单位时间，函数 1 总共执行 4 个单位时间。 

```
 **示例 2：** 

```

输入：n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
输出：[8]
解释：
函数 0 在时间戳 0 的起始开始执行，执行 2 个单位时间，并递归调用它自身。
函数 0（递归调用）在时间戳 2 的起始开始执行，执行 4 个单位时间。
函数 0（初始调用）恢复执行，并立刻再次调用它自身。
函数 0（第二次递归调用）在时间戳 6 的起始开始执行，执行 1 个单位时间。
函数 0（初始调用）在时间戳 7 的起始恢复执行，执行 1 个单位时间。
所以函数 0 总共执行 2 + 4 + 1 + 1 = 8 个单位时间。

```
 **示例 3：** 

```

输入：n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
输出：[7,1]
解释：
函数 0 在时间戳 0 的起始开始执行，执行 2 个单位时间，并递归调用它自身。
函数 0（递归调用）在时间戳 2 的起始开始执行，执行 4 个单位时间。
函数 0（初始调用）恢复执行，并立刻调用函数 1 。
函数 1在时间戳 6 的起始开始执行，执行 1 个单位时间，于时间戳 6 的末尾结束执行。
函数 0（初始调用）在时间戳 7 的起始恢复执行，执行 1 个单位时间，于时间戳 7 的末尾结束执行。
所以函数 0 总共执行 2 + 4 + 1 = 7 个单位时间，函数 1 总共执行 1 个单位时间。 
```
 **示例 4：** 

```

输入：n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:7","1:end:7","0:end:8"]
输出：[8,1]

```
 **示例 5：** 

```

输入：n = 1, logs = ["0:start:0","0:end:0"]
输出：[1]

```
 

 **提示：** 
-  `1 <= n <= 100` 
-  `1 <= logs.length <= 500` 
-  `0 <= function_id < n` 
-  `0 <= timestamp <= 10^9` 
- 两个开始事件不会在同一时间戳发生
- 两个结束事件不会在同一时间戳发生
- 每道函数都有一个对应  `"start"` 日志的 `"end"` 日志
 
**标签**
`栈` `数组` 


## 
```python

```
>
# 637.二叉树的层平均值
[https://leetcode-cn.com/problems/average-of-levels-in-binary-tree](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree) 
## 原题
给定一个非空二叉树的根节点<meta charset="UTF-8" /> `root` , 以数组的形式返回每一层节点的平均值。与实际答案相差 `10^-5` 以内的答案可以被接受。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/avg1-tree.jpg" />

```

输入：root = [3,9,20,null,null,15,7]
输出：[3.00000,14.50000,11.00000]
解释：第 0 层的平均值为 3,第 1 层的平均值为 14.5,第 2 层的平均值为 11 。
因此返回 [3, 14.5, 11] 。

```
 **示例 2:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/avg2-tree.jpg" />

```

输入：root = [3,9,20,15,7]
输出：[3.00000,14.50000,11.00000]

```
 

 **提示：** 

<meta charset="UTF-8" />
- 树中节点数量在 `[1, 10^4]` 范围内
-  `-2^31 <= Node.val <= 2^31 - 1` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 638.大礼包
[https://leetcode-cn.com/problems/shopping-offers](https://leetcode-cn.com/problems/shopping-offers) 
## 原题
在 LeetCode 商店中， 有 `n` 件在售的物品。每件物品都有对应的价格。然而，也有一些大礼包，每个大礼包以优惠的价格捆绑销售一组物品。

给你一个整数数组 `price` 表示物品价格，其中 `price[i]` 是第 `i` 件物品的价格。另有一个整数数组 `needs` 表示购物清单，其中 `needs[i]` 是需要购买第 `i` 件物品的数量。

还有一个数组 `special` 表示大礼包， `special[i]` 的长度为 `n + 1` ，其中 `special[i][j]` 表示第 `i` 个大礼包中内含第 `j` 件物品的数量，且 `special[i][n]` （也就是数组中的最后一个整数）为第 `i` 个大礼包的价格。

返回 **确切** 满足购物清单所需花费的最低价格，你可以充分利用大礼包的优惠活动。你不能购买超出购物清单指定数量的物品，即使那样会降低整体价格。任意大礼包可无限次购买。

 

 **示例 1：** 

```

输入：price = [2,5], special = [[3,0,5],[1,2,10]], needs = [3,2]
输出：14
解释：有 A 和 B 两种物品，价格分别为 ¥2 和 ¥5 。 
大礼包 1 ，你可以以 ¥5 的价格购买 3A 和 0B 。 
大礼包 2 ，你可以以 ¥10 的价格购买 1A 和 2B 。 
需要购买 3 个 A 和 2 个 B ， 所以付 ¥10 购买 1A 和 2B（大礼包 2），以及 ¥4 购买 2A 。
```
 **示例 2：** 

```

输入：price = [2,3,4], special = [[1,1,0,4],[2,2,1,9]], needs = [1,2,1]
输出：11
解释：A ，B ，C 的价格分别为 ¥2 ，¥3 ，¥4 。
可以用 ¥4 购买 1A 和 1B ，也可以用 ¥9 购买 2A ，2B 和 1C 。 
需要买 1A ，2B 和 1C ，所以付 ¥4 买 1A 和 1B（大礼包 1），以及 ¥3 购买 1B ， ¥4 购买 1C 。 
不可以购买超出待购清单的物品，尽管购买大礼包 2 更加便宜。
```
 

 **提示：** 
-  `n == price.length` 
-  `n == needs.length` 
-  `1 <= n <= 6` 
-  `0 <= price[i] <= 10` 
-  `0 <= needs[i] <= 10` 
-  `1 <= special.length <= 100` 
-  `special[i].length == n + 1` 
-  `0 <= special[i][j] <= 50` 
 
**标签**
`位运算` `记忆化搜索` `数组` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 639.解码方法 II
[https://leetcode-cn.com/problems/decode-ways-ii](https://leetcode-cn.com/problems/decode-ways-ii) 
## 原题
一条包含字母 `A-Z` 的消息通过以下的方式进行了 **编码** ：

```

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
```
要 **解码** 一条已编码的消息，所有的数字都必须分组，然后按原来的编码方案反向映射回字母（可能存在多种方式）。例如， `"11106"` 可以映射为：
-  `"AAJF"` 对应分组 `(1 1 10 6)` 
-  `"KJF"` 对应分组 `(11 10 6)` 
注意，像 `(1 11 06)` 这样的分组是无效的，因为 `"06"` 不可以映射为 `'F'` ，因为 `"6"` 与 `"06"` 不同。

 **除了** 上面描述的数字字母映射方案，编码消息中可能包含 `'*'` 字符，可以表示从 `'1'` 到 `'9'` 的任一数字（不包括 `'0'` ）。例如，编码字符串 `"1*"` 可以表示 `"11"` 、 `"12"` 、 `"13"` 、 `"14"` 、 `"15"` 、 `"16"` 、 `"17"` 、 `"18"` 或 `"19"` 中的任意一条消息。对 `"1*"` 进行解码，相当于解码该字符串可以表示的任何编码消息。

给你一个字符串 `s` ，由数字和 `'*'` 字符组成，返回 **解码** 该字符串的方法 **数目** 。

由于答案数目可能非常大，返回 `10^9 + 7` 的 <b>模</b> 。

 

 **示例 1：** 

```

输入：s = "*"
输出：9
解释：这一条编码消息可以表示 "1"、"2"、"3"、"4"、"5"、"6"、"7"、"8" 或 "9" 中的任意一条。
可以分别解码成字符串 "A"、"B"、"C"、"D"、"E"、"F"、"G"、"H" 和 "I" 。
因此，"*" 总共有 9 种解码方法。

```
 **示例 2：** 

```

输入：s = "1*"
输出：18
解释：这一条编码消息可以表示 "11"、"12"、"13"、"14"、"15"、"16"、"17"、"18" 或 "19" 中的任意一条。
每种消息都可以由 2 种方法解码（例如，"11" 可以解码成 "AA" 或 "K"）。
因此，"1*" 共有 9 * 2 = 18 种解码方法。

```
 **示例 3：** 

```

输入：s = "2*"
输出：15
解释：这一条编码消息可以表示 "21"、"22"、"23"、"24"、"25"、"26"、"27"、"28" 或 "29" 中的任意一条。
"21"、"22"、"23"、"24"、"25" 和 "26" 由 2 种解码方法，但 "27"、"28" 和 "29" 仅有 1 种解码方法。
因此，"2*" 共有 (6 * 2) + (3 * 1) = 12 + 3 = 15 种解码方法。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s[i]` 是 `0 - 9` 中的一位数字或字符 `'*'` 
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 640.求解方程
[https://leetcode-cn.com/problems/solve-the-equation](https://leetcode-cn.com/problems/solve-the-equation) 
## 原题
求解一个给定的方程，将 `x` 以字符串 `"x=#value"` 的形式返回。该方程仅包含 `'+'` ， `'-'` 操作，变量 `x` 和其对应系数。

如果方程没有解，请返回 `"No solution"` 。如果方程有无限解，则返回 `“Infinite solutions”` 。

如果方程中只有一个解，要保证返回值 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'x'</span></span></font></font> 是一个整数。

 

 **示例 1：** 

```

输入: equation = "x+5-3+x=6+x-2"
输出: "x=2"

```
 **示例 2:** 

```

输入: equation = "x=x"
输出: "Infinite solutions"

```
 **示例 3:** 

```

输入: equation = "2x=x"
输出: "x=0"

```
 

 

 **提示:** 
-  `3 <= equation.length <= 1000` 
-  `equation` 只有一个 `'='` .
-  `equation` 方程由整数组成，其绝对值在 `[0, 100]` 范围内，不含前导零和变量 `'x'` 。 <span style="display:block"><span style="height:0px"><span style="position:absolute">​​​</span></span></span>
 
**标签**
`数学` `字符串` `模拟` 


## 
```python

```
>
# 641.设计循环双端队列
[https://leetcode-cn.com/problems/design-circular-deque](https://leetcode-cn.com/problems/design-circular-deque) 
## 原题
设计实现双端队列。

实现 `MyCircularDeque` 类:
-  `MyCircularDeque(int k)` ：构造函数,双端队列最大为 `k` 。
-  `boolean insertFront()` ：将一个元素添加到双端队列头部。 如果操作成功返回 `true` ，否则返回 `false` 。
-  `boolean insertLast()` ：将一个元素添加到双端队列尾部。如果操作成功返回 `true` ，否则返回 `false` 。
-  `boolean deleteFront()` ：从双端队列头部删除一个元素。 如果操作成功返回 `true` ，否则返回 `false` 。
-  `boolean deleteLast()` ：从双端队列尾部删除一个元素。如果操作成功返回 `true` ，否则返回 `false` 。
-  `int getFront()` )：从双端队列头部获得一个元素。如果双端队列为空，返回 `-1` 。
-  `int getRear()` ：获得双端队列的最后一个元素。 如果双端队列为空，返回 `-1` 。
-  `boolean isEmpty()` ：若双端队列为空，则返回 `true` ，否则返回 `false` 。
-  `boolean isFull()` ：若双端队列满了，则返回 `true` ，否则返回 `false` 。
 

 **示例 1：** 

```

输入
["MyCircularDeque", "insertLast", "insertLast", "insertFront", "insertFront", "getRear", "isFull", "deleteLast", "insertFront", "getFront"]
[[3], [1], [2], [3], [4], [], [], [], [4], []]
输出
[null, true, true, true, false, 2, true, true, true, 4]

解释
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			        // 返回 true
circularDeque.insertLast(2);			        // 返回 true
circularDeque.insertFront(3);			        // 返回 true
circularDeque.insertFront(4);			        // 已经满了，返回 false
circularDeque.getRear();  				// 返回 2
circularDeque.isFull();				        // 返回 true
circularDeque.deleteLast();			        // 返回 true
circularDeque.insertFront(4);			        // 返回 true
circularDeque.getFront();				// 返回 4
 
```
 

 **提示：** 
-  `1 <= k <= 1000` 
-  `0 <= value <= 1000` 
-  `insertFront` , `insertLast` , `deleteFront` , `deleteLast` , `getFront` , `getRear` , `isEmpty` , `isFull` 调用次数不大于 `2000` 次
 
**标签**
`设计` `队列` `数组` `链表` 


## 
```python

```
>
# 642.设计搜索自动补全系统
[https://leetcode-cn.com/problems/design-search-autocomplete-system](https://leetcode-cn.com/problems/design-search-autocomplete-system) 
## 原题

 
**标签**
`设计` `字典树` `字符串` `数据流` 


## 
```python

```
>
# 643.子数组最大平均数 I
[https://leetcode-cn.com/problems/maximum-average-subarray-i](https://leetcode-cn.com/problems/maximum-average-subarray-i) 
## 原题
给你一个由 `n` 个元素组成的整数数组 `nums` 和一个整数 `k` 。

请你找出平均数最大且 **长度为 `k` ** 的连续子数组，并输出该最大平均数。

任何误差小于 `10^-5` 的答案都将被视为正确答案。

 

 **示例 1：** 

```

输入：nums = [1,12,-5,-6,50,3], k = 4
输出：12.75
解释：最大平均数 (12-5-6+50)/4 = 51/4 = 12.75

```
 **示例 2：** 

```

输入：nums = [5], k = 1
输出：5.00000

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= k <= n <= 10^5` 
-  `-10^4 <= nums[i] <= 10^4` 
 
**标签**
`数组` `滑动窗口` 


## 
```python

```
>
# 644.子数组最大平均数 II
[https://leetcode-cn.com/problems/maximum-average-subarray-ii](https://leetcode-cn.com/problems/maximum-average-subarray-ii) 
## 原题

 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 645.错误的集合
[https://leetcode-cn.com/problems/set-mismatch](https://leetcode-cn.com/problems/set-mismatch) 
## 原题
集合 `s` 包含从 `1` 到  `n`  的整数。不幸的是，因为数据错误，导致集合里面某一个数字复制了成了集合里面的另外一个数字的值，导致集合 **丢失了一个数字** 并且 **有一个数字重复** 。

给定一个数组 `nums` 代表了集合 `S` 发生错误后的结果。

请你找出重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

 

 **示例 1：** 

```

输入：nums = [1,2,2,4]
输出：[2,3]

```
 **示例 2：** 

```

输入：nums = [1,1]
输出：[1,2]

```
 

 **提示：** 
-  `2 <= nums.length <= 10^4` 
-  `1 <= nums[i] <= 10^4` 
 
**标签**
`位运算` `数组` `哈希表` `排序` 


## 
```python

```
>
# 646.最长数对链
[https://leetcode-cn.com/problems/maximum-length-of-pair-chain](https://leetcode-cn.com/problems/maximum-length-of-pair-chain) 
## 原题
给出  `n`  个数对。 在每一个数对中，第一个数字总是比第二个数字小。

现在，我们定义一种跟随关系，当且仅当  `b < c`  时，数对 `(c, d)`  才可以跟在  `(a, b)`  后面。我们用这种形式来构造一个数对链。

给定一个数对集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

 

 **示例：** 

```

输入：[[1,2], [2,3], [3,4]]
输出：2
解释：最长的数对链是 [1,2] -> [3,4]

```
 

 **提示：** 
- 给出数对的个数在  `[1, 1000]` 范围内。
 
**标签**
`贪心` `数组` `动态规划` `排序` 


## 
```python

```
>
# 647.回文子串
[https://leetcode-cn.com/problems/palindromic-substrings](https://leetcode-cn.com/problems/palindromic-substrings) 
## 原题
给你一个字符串 `s` ，请你统计并返回这个字符串中 **回文子串** 的数目。

 **回文字符串** 是正着读和倒过来读一样的字符串。

 **子字符串** 是字符串中的由连续字符组成的一个序列。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。

 

 **示例 1：** 

```

输入：s = "abc"
输出：3
解释：三个回文子串: "a", "b", "c"

```
 **示例 2：** 

```

输入：s = "aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"
```
 

 **提示：** 
-  `1 <= s.length <= 1000` 
-  `s` 由小写英文字母组成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 648.单词替换
[https://leetcode-cn.com/problems/replace-words](https://leetcode-cn.com/problems/replace-words) 
## 原题
在英语中，我们有一个叫做 `词根` (root) 的概念，可以词根 **后面** 添加其他一些词组成另一个较长的单词——我们称这个词为 `继承词` (successor)。例如，词根 `an` ，跟随着单词 `other` (其他)，可以形成新的单词 `another` (另一个)。

现在，给定一个由许多 **词根** 组成的词典 `dictionary` 和一个用空格分隔单词形成的句子 `sentence` 。你需要将句子中的所有 **继承词** 用 **词根** 替换掉。如果 **继承词** 有许多可以形成它的 **词根** ，则用 **最短** 的词根替换它。

你需要输出替换之后的句子。

 

 **示例 1：** 

```

输入：dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
输出："the cat was rat by the bat"

```
 **示例 2：** 

```

输入：dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
输出："a a b c"

```
 

 **提示：** 
-  `1 <= dictionary.length <= 1000` 
-  `1 <= dictionary[i].length <= 100` 
-  `dictionary[i]` 仅由小写字母组成。
-  `1 <= sentence.length <= 10^6` 
-  `sentence` 仅由小写字母和空格组成。
-  `sentence` 中单词的总量在范围 `[1, 1000]` 内。
-  `sentence` 中每个单词的长度在范围 `[1, 1000]` 内。
-  `sentence` 中单词之间由一个空格隔开。
-  `sentence` 没有前导或尾随空格。
 

 
**标签**
`字典树` `数组` `哈希表` `字符串` 


## 
```python

```
>
# 649.Dota2 参议院
[https://leetcode-cn.com/problems/dota2-senate](https://leetcode-cn.com/problems/dota2-senate) 
## 原题
Dota2 的世界里有两个阵营： `Radiant` (天辉)和  `Dire` (夜魇)

Dota2 参议院由来自两派的参议员组成。现在参议院希望对一个 Dota2 游戏里的改变作出决定。他们以一个基于轮为过程的投票进行。在每一轮中，每一位参议员都可以行使两项权利中的 `**一**` 项：
- 
	 `禁止一名参议员的权利` ：

	参议员可以让另一位参议员在这一轮和随后的几轮中丧失 **所有的权利** 。
	
- 
	 `宣布胜利` ：
	
          如果参议员发现有权利投票的参议员都是 **同一个阵营的** ，他可以宣布胜利并决定在游戏中的有关变化。

 

给定一个字符串代表每个参议员的阵营。字母 “R” 和 “D” 分别代表了  `Radiant` （天辉）和  `Dire` （夜魇）。然后，如果有 `n` 个参议员，给定字符串的大小将是  `n` 。

以轮为基础的过程从给定顺序的第一个参议员开始到最后一个参议员结束。这一过程将持续到投票结束。所有失去权利的参议员将在过程中被跳过。

假设每一位参议员都足够聪明，会为自己的政党做出最好的策略，你需要预测哪一方最终会宣布胜利并在 Dota2 游戏中决定改变。输出应该是  `Radiant`  或  `Dire` 。

 

 **示例 1：** 

```

输入："RD"
输出："Radiant"
解释：第一个参议员来自 Radiant 阵营并且他可以使用第一项权利让第二个参议员失去权力，因此第二个参议员将被跳过因为他没有任何权利。然后在第二轮的时候，第一个参议员可以宣布胜利，因为他是唯一一个有投票权的人

```
 **示例 2：** 

```

输入："RDD"
输出："Dire"
解释：
第一轮中,第一个来自 Radiant 阵营的参议员可以使用第一项权利禁止第二个参议员的权利
第二个来自 Dire 阵营的参议员会被跳过因为他的权利被禁止
第三个来自 Dire 阵营的参议员可以使用他的第一项权利禁止第一个参议员的权利
因此在第二轮只剩下第三个参议员拥有投票的权利,于是他可以宣布胜利

```
 

 **提示：** 
- 给定字符串的长度在 `[1, 10,000]` 之间.
 

 
**标签**
`贪心` `队列` `字符串` 


## 
```python

```
>
# 650.只有两个键的键盘
[https://leetcode-cn.com/problems/2-keys-keyboard](https://leetcode-cn.com/problems/2-keys-keyboard) 
## 原题
最初记事本上只有一个字符 `'A'` 。你每次可以对这个记事本进行两种操作：
-  `Copy All` （复制全部）：复制这个记事本中的所有字符（不允许仅复制部分字符）。
-  `Paste` （粘贴）：粘贴 **上一次** 复制的字符。
给你一个数字 `n` ，你需要使用最少的操作次数，在记事本上输出 **恰好** `n` 个 `'A'` 。返回能够打印出 `n` 个 `'A'` 的最少操作次数。

 

 **示例 1：** 

```

输入：3
输出：3
解释：
最初, 只有一个字符 'A'。
第 1 步, 使用 Copy All 操作。
第 2 步, 使用 Paste 操作来获得 'AA'。
第 3 步, 使用 Paste 操作来获得 'AAA'。

```
 **示例 2：** 

```

输入：n = 1
输出：0

```
 

 **提示：** 
-  `1 <= n <= 1000` 
 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 651.4键键盘
[https://leetcode-cn.com/problems/4-keys-keyboard](https://leetcode-cn.com/problems/4-keys-keyboard) 
## 原题

 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 652.寻找重复的子树
[https://leetcode-cn.com/problems/find-duplicate-subtrees](https://leetcode-cn.com/problems/find-duplicate-subtrees) 
## 原题
给定一棵二叉树 `root` ，返回所有 **重复的子树** 。

对于同一类的重复子树，你只需要返回其中任意 **一棵** 的根结点即可。

如果两棵树具有 **相同的结构** 和 **相同的结点值** ，则它们是 **重复** 的。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e1.jpg" style="height: 236px; width: 300px;" />

```

输入：root = [1,2,3,4,null,2,4,null,null,4]
输出：[[2,4],[4]]
```
 **示例 2：** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e2.jpg" style="height: 125px; width: 200px;" />

```

输入：root = [2,1,1]
输出：[[1]]
```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode.com/uploads/2020/08/16/e33.jpg" style="height: 202px; width: 300px;" />** 

```

输入：root = [2,2,2,3,null,3,null]
输出：[[2,3],[3]]
```
 

 **提示：** 
- 树中的结点数在 `[1,10^4]` 范围内。
-  `-200 <= Node.val <= 200` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 653.两数之和 IV - 输入 BST
[https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst](https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst) 
## 原题
给定一个二叉搜索树 `root` 和一个目标结果 `k` ，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 `true` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_1.jpg" style="height: 229px; width: 400px;" />
```

输入: root = [5,3,6,2,4,null,7], k = 9
输出: true

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/21/sum_tree_2.jpg" style="height: 229px; width: 400px;" />
```

输入: root = [5,3,6,2,4,null,7], k = 28
输出: false

```
 

 **提示:** 
- 二叉树的节点个数的范围是 `[1, 10^4]` .
-  `-10^4 <= Node.val <= 10^4` 
-  `root` 为二叉搜索树
-  `-10^5 <= k <= 10^5` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉搜索树` `哈希表` `双指针` `二叉树` 


## 
```python

```
>
# 654.最大二叉树
[https://leetcode-cn.com/problems/maximum-binary-tree](https://leetcode-cn.com/problems/maximum-binary-tree) 
## 原题
给定一个不重复的整数数组 `nums` 。 **最大二叉树** 可以用下面的算法从 `nums` 递归地构建:
- 创建一个根节点，其值为 `nums` 中的最大值。
- 递归地在最大值 **左边** 的 **子数组前缀上** 构建左子树。
- 递归地在最大值 **右边** 的 **子数组后缀上** 构建右子树。
返回 *`nums` 构建的* ** *最大二叉树* ** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/tree1.jpg" />
```

输入：nums = [3,2,1,6,0,5]
输出：[6,3,5,null,2,0,null,null,1]
解释：递归调用如下所示：
- [3,2,1,6,0,5] 中的最大值是 6 ，左边部分是 [3,2,1] ，右边部分是 [0,5] 。
    - [3,2,1] 中的最大值是 3 ，左边部分是 [] ，右边部分是 [2,1] 。
        - 空数组，无子节点。
        - [2,1] 中的最大值是 2 ，左边部分是 [] ，右边部分是 [1] 。
            - 空数组，无子节点。
            - 只有一个元素，所以子节点是一个值为 1 的节点。
    - [0,5] 中的最大值是 5 ，左边部分是 [0] ，右边部分是 [] 。
        - 只有一个元素，所以子节点是一个值为 0 的节点。
        - 空数组，无子节点。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/24/tree2.jpg" />
```

输入：nums = [3,2,1]
输出：[3,null,2,null,1]

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `0 <= nums[i] <= 1000` 
-  `nums` 中的所有整数 **互不相同** 
 
**标签**
`栈` `树` `数组` `分治` `二叉树` `单调栈` 


## 
```python

```
>
# 655.输出二叉树
[https://leetcode-cn.com/problems/print-binary-tree](https://leetcode-cn.com/problems/print-binary-tree) 
## 原题
在一个 m*n 的二维字符串数组中输出二叉树，并遵守以下规则：
- 行数 `m` 应当等于给定二叉树的高度。
- 列数 `n` 应当总是奇数。
- 根节点的值（以字符串格式给出）应当放在可放置的第一行正中间。根节点所在的行与列会将剩余空间划分为两部分（ **左下部分和右下部分** ）。你应该将左子树输出在左下部分，右子树输出在右下部分。左下和右下部分应当有相同的大小。即使一个子树为空而另一个非空，你不需要为空的子树输出任何东西，但仍需要为另一个子树留出足够的空间。然而，如果两个子树都为空则不需要为它们留出任何空间。
- 每个未使用的空间应包含一个空的字符串 `""` 。
- 使用相同的规则输出子树。
 **示例 1:** 

```

输入:
     1
    /
   2
输出:
[["", "1", ""],
 ["2", "", ""]]

```
 **示例 2:** 

```

输入:
     1
    / \
   2   3
    \
     4
输出:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]

```
 **示例 3:** 

```

输入:
      1
     / \
    2   5
   / 
  3 
 / 
4 
输出:
[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]

```
 **注意:** 二叉树的高度在范围 [1, 10] 中。

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 656.金币路径
[https://leetcode-cn.com/problems/coin-path](https://leetcode-cn.com/problems/coin-path) 
## 原题

 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 657.机器人能否返回原点
[https://leetcode-cn.com/problems/robot-return-to-origin](https://leetcode-cn.com/problems/robot-return-to-origin) 
## 原题
在二维平面上，有一个机器人从原点 `(0, 0)` 开始。给出它的移动顺序，判断这个机器人在完成移动后是否在 ** `(0, 0)` 处结束** 。

移动顺序由字符串 `moves` 表示。字符 `move[i]` 表示其第 `i` 次移动。机器人的有效动作有 `R` （右）， `L` （左）， `U` （上）和 `D` （下）。

如果机器人在完成所有动作后返回原点，则返回 `true` 。否则，返回 `false` 。

 **注意：** 机器人“面朝”的方向无关紧要。 `“R”` 将始终使机器人向右移动一次， `“L”` 将始终向左移动等。此外，假设每次移动机器人的移动幅度相同。

 

 **示例 1:** 

```

输入: moves = "UD"
输出: true
解释：机器人向上移动一次，然后向下移动一次。所有动作都具有相同的幅度，因此它最终回到它开始的原点。因此，我们返回 true。
```
 **示例 2:** 

```

输入: moves = "LL"
输出: false
解释：机器人向左移动两次。它最终位于原点的左侧，距原点有两次 “移动” 的距离。我们返回 false，因为它在移动结束时没有返回原点。
```
 

 **提示:** 
-  `1 <= moves.length <= 2 * 10^4` 
-  `moves` 只包含字符 `'U'` , `'D'` , `'L'` 和 `'R'` 
 
**标签**
`字符串` `模拟` 


## 
```python

```
>
# 658.找到 K 个最接近的元素
[https://leetcode-cn.com/problems/find-k-closest-elements](https://leetcode-cn.com/problems/find-k-closest-elements) 
## 原题
给定一个 **排序好** 的数组 `arr` ，两个整数 `k` 和 `x` ，从数组中找到最靠近 `x` （两数之差最小）的 `k` 个数。返回的结果必须要是按升序排好的。

整数 `a` 比整数 `b` 更接近 `x` 需要满足：
-  `|a - x| < |b - x|` 或者
-  `|a - x| == |b - x|` 且 `a < b` 
 

 **示例 1：** 

```

输入：arr = [1,2,3,4,5], k = 4, x = 3
输出：[1,2,3,4]

```
 **示例 2：** 

```

输入：arr = [1,2,3,4,5], k = 4, x = -1
输出：[1,2,3,4]

```
 

 **提示：** 
-  `1 <= k <= arr.length` 
-  `1 <= arr.length <= 10^4` <meta charset="UTF-8" />
-  `arr` 按 **升序** 排列
-  `-10^4 <= arr[i], x <= 10^4` 
 
**标签**
`数组` `双指针` `二分查找` `排序` `堆（优先队列）` 


## 
```python

```
>
# 659.分割数组为连续子序列
[https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences](https://leetcode-cn.com/problems/split-array-into-consecutive-subsequences) 
## 原题
给你一个按升序排序的整数数组 `num` （可能包含重复数字），请你将它们分割成一个或多个长度至少为 3 的子序列，其中每个子序列都由连续整数组成。

如果可以完成上述分割，则返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入: [1,2,3,3,4,5]
输出: True
解释:
你可以分割出这样两个连续子序列 : 
1, 2, 3
3, 4, 5

```
 **示例 2：** 

```

输入: [1,2,3,3,4,4,5,5]
输出: True
解释:
你可以分割出这样两个连续子序列 : 
1, 2, 3, 4, 5
3, 4, 5

```
 **示例 3：** 

```

输入: [1,2,3,4,4,5]
输出: False

```
 

<b>提示：</b>
-  `1 <= nums.length <= 10000` 
 
**标签**
`贪心` `数组` `哈希表` `堆（优先队列）` 


## 
```python

```
>
# 660.移除 9
[https://leetcode-cn.com/problems/remove-9](https://leetcode-cn.com/problems/remove-9) 
## 原题

 
**标签**
`数学` 


## 
```python

```
>
# 661.图片平滑器
[https://leetcode-cn.com/problems/image-smoother](https://leetcode-cn.com/problems/image-smoother) 
## 原题
 **图像平滑器** 是大小为 `3 x 3` 的过滤器，可以计算是周围的8个单元和它本身的值求平均灰度(即蓝色平滑器中9个单元的平均值)来应用于图像的每个单元。如果一个单元的一个或多个周围的单元不存在，我们不考虑它的平均值(即红色平滑器中的四个单元的平均值)。

<img src="https://assets.leetcode.com/uploads/2021/05/03/smoother-grid.jpg" style="height: 493px; width: 493px;" />

给定一个代表图像灰度的 `m x n` 整数矩阵 `img` ， *返回对图像的每个单元格平滑处理后的图像* 。

 

 **示例 1:** 

<img src="https://assets.leetcode.com/uploads/2021/05/03/smooth-grid.jpg" />

```

输入:img = [[1,1,1],[1,0,1],[1,1,1]]
输出:[[0, 0, 0],[0, 0, 0], [0, 0, 0]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): 平均(3/4) = 平均(0.75) = 0
对于点 (0,1), (1,0), (1,2), (2,1): 平均(5/6) = 平均(0.83333333) = 0
对于点 (1,1): 平均(8/9) = 平均(0.88888889) = 0

```
 **示例 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/03/smooth2-grid.jpg" />
```

输入: img = [[100,200,100],[200,50,200],[100,200,100]]
输出: [[137,141,137],[141,138,141],[137,141,137]]
解释:
对于点 (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
对于点 (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
对于点 (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138

```
 

 **提示:** 
-  `m == img.length` 
-  `n == img[i].length` 
-  `1 <= m, n <= 200` 
-  `0 <= img[i][j] <= 255` 
 
**标签**
`数组` `矩阵` 


## 
```python

```
>
# 662.二叉树最大宽度
[https://leetcode-cn.com/problems/maximum-width-of-binary-tree](https://leetcode-cn.com/problems/maximum-width-of-binary-tree) 
## 原题
给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与 **满二叉树（full binary tree）** 结构相同，但一些节点为空。

每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的 `null` 节点也计入长度）之间的长度。

 **示例 1:** 

```

输入: 

           1
         /   \
        3     2
       / \     \  
      5   3     9 

输出: 4
解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。

```
 **示例 2:** 

```

输入: 

          1
         /  
        3    
       / \       
      5   3     

输出: 2
解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。

```
 **示例 3:** 

```

输入: 

          1
         / \
        3   2 
       /        
      5      

输出: 2
解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。

```
 **示例 4:** 

```

输入: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
输出: 8
解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。

```
 **注意:** 答案在32位有符号整数的表示范围内。

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 663.均匀树划分
[https://leetcode-cn.com/problems/equal-tree-partition](https://leetcode-cn.com/problems/equal-tree-partition) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 664.奇怪的打印机
[https://leetcode-cn.com/problems/strange-printer](https://leetcode-cn.com/problems/strange-printer) 
## 原题
有台奇怪的打印机有以下两个特殊要求：
- 打印机每次只能打印由 **同一个字符** 组成的序列。
- 每次可以在从起始到结束的任意位置打印新字符，并且会覆盖掉原来已有的字符。
给你一个字符串 `s` ，你的任务是计算这个打印机打印它需要的最少打印次数。
 

 **示例 1：** 

```

输入：s = "aaabbb"
输出：2
解释：首先打印 "aaa" 然后打印 "bbb"。

```
 **示例 2：** 

```

输入：s = "aba"
输出：2
解释：首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。

```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `s` 由小写英文字母组成
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 665.非递减数列
[https://leetcode-cn.com/problems/non-decreasing-array](https://leetcode-cn.com/problems/non-decreasing-array) 
## 原题
给你一个长度为 `n` 的整数数组<meta charset="UTF-8" /> `nums` ，请你判断在 **最多** 改变 `1` 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中任意的 `i` `(0 <= i <= n-2)` ，总满足 `nums[i] <= nums[i + 1]` 。

 

 **示例 1:** 

```

输入: nums = [4,2,3]
输出: true
解释: 你可以通过把第一个 4 变成 1 来使得它成为一个非递减数列。

```
 **示例 2:** 

```

输入: nums = [4,2,1]
输出: false
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。

```
 

 **提示：** 
<meta charset="UTF-8" />
-  `n == nums.length` 
-  `1 <= n <= 10^4` 
-  `-10^5 <= nums[i] <= 10^5` 
 
**标签**
`数组` 


## 
```python

```
>
# 666.路径总和 IV
[https://leetcode-cn.com/problems/path-sum-iv](https://leetcode-cn.com/problems/path-sum-iv) 
## 原题

 
**标签**
`树` `深度优先搜索` `数组` `二叉树` 


## 
```python

```
>
# 667.优美的排列 II
[https://leetcode-cn.com/problems/beautiful-arrangement-ii](https://leetcode-cn.com/problems/beautiful-arrangement-ii) 
## 原题
给你两个整数 `n` 和 `k` ，请你构造一个答案列表 `answer` ，该列表应当包含从 `1` 到 `n` 的 `n` 个不同正整数，并同时满足下述条件：
- 假设该列表是 `answer = [a<sub>1</sub>, a<sub>2</sub>, a<sub>3</sub>, ... , a<sub>n</sub>]` ，那么列表 `[|a<sub>1</sub> - a<sub>2</sub>|, |a<sub>2</sub> - a<sub>3</sub>|, |a<sub>3</sub> - a<sub>4</sub>|, ... , |a<sub>n-1</sub> - a<sub>n</sub>|]` 中应该有且仅有 `k` 个不同整数。
返回列表 `answer` 。如果存在多种答案，只需返回其中 **任意一种** 。

 

 **示例 1：** 

```

输入：n = 3, k = 1
输出：[1, 2, 3]
解释：[1, 2, 3] 包含 3 个范围在 1-3 的不同整数，并且 [1, 1] 中有且仅有 1 个不同整数：1

```
 **示例 2：** 

```

输入：n = 3, k = 2
输出：[1, 3, 2]
解释：[1, 3, 2] 包含 3 个范围在 1-3 的不同整数，并且 [2, 1] 中有且仅有 2 个不同整数：1 和 2

```
 

 **提示：** 
-  `1 <= k < n <= 10^4` 
 

 
**标签**
`数组` `数学` 


## 
```python

```
>
# 668.乘法表中第k小的数
[https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table](https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table) 
## 原题
几乎每一个人都用 <a href="https://baike.baidu.com/item/%E4%B9%98%E6%B3%95%E8%A1%A8">乘法表</a>。但是你能在乘法表中快速找到第 `k` 小的数字吗？

给定高度 `m` 、宽度 `n` 的一张 `m * n` 的乘法表，以及正整数 `k` ，你需要返回表中第 `k` 小的数字。

 **例 1：** 

```

输入: m = 3, n = 3, k = 5
输出: 3
解释: 
乘法表:
1	2	3
2	4	6
3	6	9

第5小的数字是 3 (1, 2, 2, 3, 3).

```
 **例 2：** 

```

输入: m = 2, n = 3, k = 6
输出: 6
解释: 
乘法表:
1	2	3
2	4	6

第6小的数字是 6 (1, 2, 2, 3, 4, 6).

```
 **注意：** 
-  `m` 和 `n` 的范围在 [1, 30000] 之间。
-  `k` 的范围在 [1, m * n] 之间。
 
**标签**
`二分查找` 


## 
```python

```
>
# 669.修剪二叉搜索树
[https://leetcode-cn.com/problems/trim-a-binary-search-tree](https://leetcode-cn.com/problems/trim-a-binary-search-tree) 
## 原题
给你二叉搜索树的根节点 `root` ，同时给定最小边界 `low` 和最大边界 `high` 。通过修剪二叉搜索树，使得所有节点的值在 `[low, high]` 中。修剪树 **不应该** 改变保留在树中的元素的相对结构 (即，如果没有被移除，原有的父代子代关系都应当保留)。 可以证明，存在 **唯一的答案** 。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim1.jpg" style="height: 126px; width: 450px;" />
```

输入：root = [1,0,2], low = 1, high = 2
输出：[1,null,2]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/09/trim2.jpg" style="height: 277px; width: 450px;" />
```

输入：root = [3,0,4,null,2,null,null,1], low = 1, high = 3
输出：[3,2,null,1]

```
 

 **提示：** 
- 树中节点数在范围 `[1, 10^4]` 内
-  `0 <= Node.val <= 10^4` 
- 树中每个节点的值都是 **唯一** 的
- 题目数据保证输入是一棵有效的二叉搜索树
-  `0 <= low <= high <= 10^4` 
 
**标签**
`树` `深度优先搜索` `二叉搜索树` `二叉树` 


## 
```python

```
>
# 670.最大交换
[https://leetcode-cn.com/problems/maximum-swap](https://leetcode-cn.com/problems/maximum-swap) 
## 原题
给定一个非负整数，你 **至多** 可以交换一次数字中的任意两位。返回你能得到的最大值。

 **示例 1 :** 

```

输入: 2736
输出: 7236
解释: 交换数字2和数字7。

```
 **示例 2 :** 

```

输入: 9973
输出: 9973
解释: 不需要交换。

```
 **注意:** 
- 给定数字的范围是 [0, 10^8]
 
**标签**
`贪心` `数学` 


## 
```python

```
>
# 671.二叉树中第二小的节点
[https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree](https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree) 
## 原题
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为 `2` 或 `0` 。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，即 `root.val = min(root.left.val, root.right.val)` 总成立。

给出这样的一个二叉树，你需要输出所有节点中的 **第二小的值** 。

如果第二小的值不存在的话，输出 -1 **。** 

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg" style="height: 210px; width: 300px;" />
```

输入：root = [2,2,5,null,null,5,7]
输出：5
解释：最小的值是 2 ，第二小的值是 5 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg" style="height: 113px; width: 200px;" />
```

输入：root = [2,2,2]
输出：-1
解释：最小的值是 2, 但是不存在第二小的值。

```
 

 **提示：** 
- 树中节点数目在范围 `[1, 25]` 内
-  `1 <= Node.val <= 2^31 - 1` 
- 对于树中每个节点 `root.val == min(root.left.val, root.right.val)` 
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 672.灯泡开关 Ⅱ
[https://leetcode-cn.com/problems/bulb-switcher-ii](https://leetcode-cn.com/problems/bulb-switcher-ii) 
## 原题
现有一个房间，墙上挂有 `n` 只已经打开的灯泡和 4 个按钮。在进行了 `m` 次未知操作后，你需要返回这 `n` 只灯泡可能有多少种不同的状态。

假设这 `n` 只灯泡被编号为 [1, 2, 3 ..., n]，这 4 个按钮的功能如下：
- 将所有灯泡的状态反转（即开变为关，关变为开）
- 将编号为偶数的灯泡的状态反转
- 将编号为奇数的灯泡的状态反转
- 将编号为 `3k+1` 的灯泡的状态反转（k = 0, 1, 2, ...)
 **示例 1:** 

```
输入: n = 1, m = 1.
输出: 2
说明: 状态为: [开], [关]

```
 **示例 2:** 

```
输入: n = 2, m = 1.
输出: 3
说明: 状态为: [开, 关], [关, 开], [关, 关]

```
 **示例 3:** 

```
输入: n = 3, m = 1.
输出: 4
说明: 状态为: [关, 开, 关], [开, 关, 开], [关, 关, 关], [关, 开, 开].

```
 **注意：** `n` 和 `m` 都属于 [0, 1000].

 
**标签**
`位运算` `深度优先搜索` `广度优先搜索` `数学` 


## 
```python

```
>
# 673.最长递增子序列的个数
[https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence](https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence) 
## 原题
给定一个未排序的整数数组<meta charset="UTF-8" /> `nums` ， *返回最长递增子序列的个数* 。

 **注意** 这个数列必须是 **严格** 递增的。

 

 **示例 1:** 

```

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

```
 **示例 2:** 

```

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。

```
 

 **提示:** 

<meta charset="UTF-8" />
-  `1 <= nums.length <= 2000` 
-  `-10^6 <= nums[i] <= 10^6` 
 
**标签**
`树状数组` `线段树` `数组` `动态规划` 


## 
```python

```
>
# 674.最长连续递增序列
[https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence) 
## 原题
给定一个未经排序的整数数组，找到最长且 **连续递增的子序列** ，并返回该序列的长度。

 **连续递增的子序列** 可以由两个下标 `l` 和 `r` （ `l < r` ）确定，如果对于每个 `l <= i < r` ，都有 `nums[i] < nums[i + 1]` ，那么子序列 `[nums[l], nums[l + 1], ..., nums[r - 1], nums[r]]` 就是连续递增子序列。

 

 **示例 1：** 

```

输入：nums = [1,3,5,4,7]
输出：3
解释：最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为 5 和 7 在原数组里被 4 隔开。 

```
 **示例 2：** 

```

输入：nums = [2,2,2,2,2]
输出：1
解释：最长连续递增序列是 [2], 长度为1。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^4` 
-  `-10^9 <= nums[i] <= 10^9` 
 
**标签**
`数组` 


## 
```python

```
>
# 675.为高尔夫比赛砍树
[https://leetcode-cn.com/problems/cut-off-trees-for-golf-event](https://leetcode-cn.com/problems/cut-off-trees-for-golf-event) 
## 原题
你被请来给一个要举办高尔夫比赛的树林砍树。树林由一个  `m x n` 的矩阵表示， 在这个矩阵中：
-  `0` 表示障碍，无法触碰
-  `1`  表示地面，可以行走
-  `比 1 大的数`  表示有树的单元格，可以行走，数值表示树的高度
每一步，你都可以向上、下、左、右四个方向之一移动一个单位，如果你站的地方有一棵树，那么你可以决定是否要砍倒它。

你需要按照树的高度从低向高砍掉所有的树，每砍过一颗树，该单元格的值变为 `1` （即变为地面）。

你将从 `(0, 0)` 点开始工作，返回你砍完所有树需要走的最小步数。 如果你无法砍完所有的树，返回 `-1` 。

可以保证的是，没有两棵树的高度是相同的，并且你至少需要砍倒一棵树。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/trees1.jpg" style="width: 242px; height: 242px;" />
```

输入：forest = [[1,2,3],[0,0,4],[7,6,5]]
输出：6
解释：沿着上面的路径，你可以用 6 步，按从最矮到最高的顺序砍掉这些树。
```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/11/26/trees2.jpg" style="width: 242px; height: 242px;" />
```

输入：forest = [[1,2,3],[0,0,0],[7,6,5]]
输出：-1
解释：由于中间一行被障碍阻塞，无法访问最下面一行中的树。

```
 **示例 3：** 

```

输入：forest = [[2,3,4],[0,0,5],[8,7,6]]
输出：6
解释：可以按与示例 1 相同的路径来砍掉所有的树。
(0,0) 位置的树，可以直接砍去，不用算步数。

```
 

 **提示：** 
-  `m == forest.length` 
-  `n == forest[i].length` 
-  `1 <= m, n <= 50` 
-  `0 <= forest[i][j] <= 10^9` 
 
**标签**
`广度优先搜索` `数组` `矩阵` `堆（优先队列）` 


## 
```python

```
>
# 676.实现一个魔法字典
[https://leetcode-cn.com/problems/implement-magic-dictionary](https://leetcode-cn.com/problems/implement-magic-dictionary) 
## 原题
设计一个使用单词列表进行初始化的数据结构，单词列表中的单词 **互不相同** 。 如果给出一个单词，请判定能否只将这个单词中 **一个** 字母换成另一个字母，使得所形成的新单词存在于你构建的字典中。

实现 `MagicDictionary` 类：
-  `MagicDictionary()` 初始化对象
-  `void buildDict(String[] dictionary)` 使用字符串数组  `dictionary` 设定该数据结构， `dictionary` 中的字符串互不相同
-  `bool search(String searchWord)` 给定一个字符串 `searchWord` ，判定能否只将字符串中 **一个** 字母换成另一个字母，使得所形成的新字符串能够与字典中的任一字符串匹配。如果可以，返回 `true` ；否则，返回 `false` 。
 
 **示例：** 

```

输入
["MagicDictionary", "buildDict", "search", "search", "search", "search"]
[[], [["hello", "leetcode"]], ["hello"], ["hhllo"], ["hell"], ["leetcoded"]]
输出
[null, null, false, true, false, false]

解释
MagicDictionary magicDictionary = new MagicDictionary();
magicDictionary.buildDict(["hello", "leetcode"]);
magicDictionary.search("hello"); // 返回 False
magicDictionary.search("hhllo"); // 将第二个 'h' 替换为 'e' 可以匹配 "hello" ，所以返回 True
magicDictionary.search("hell"); // 返回 False
magicDictionary.search("leetcoded"); // 返回 False

```
 

 **提示：** 
-  `1 <= dictionary.length <= 100` 
-  `1 <= dictionary[i].length <= 100` 
-  `dictionary[i]` 仅由小写英文字母组成
-  `dictionary` 中的所有字符串 **互不相同** 
-  `1 <= searchWord.length <= 100` 
-  `searchWord` 仅由小写英文字母组成
-  `buildDict` 仅在 `search` 之前调用一次
- 最多调用 `100` 次 `search` 
 
**标签**
`设计` `字典树` `哈希表` `字符串` 


## 
```python

```
>
# 677.键值映射
[https://leetcode-cn.com/problems/map-sum-pairs](https://leetcode-cn.com/problems/map-sum-pairs) 
## 原题
设计一个 map ，满足以下几点:
- 字符串表示键，整数表示值
- 返回具有前缀等于给定字符串的键的值的总和
实现一个 `MapSum` 类：
-  `MapSum()` 初始化 `MapSum` 对象
-  `void insert(String key, int val)` 插入 `key-val` 键值对，字符串表示键 `key` ，整数表示值 `val` 。如果键 `key` 已经存在，那么原来的键值对 `key-value` 将被替代成新的键值对。
-  `int sum(string prefix)` 返回所有以该前缀 `prefix` 开头的键 `key` 的值的总和。
 

 **示例 1：** 

```

输入：
["MapSum", "insert", "sum", "insert", "sum"]
[[], ["apple", 3], ["ap"], ["app", 2], ["ap"]]
输出：
[null, null, 3, null, 5]

解释：
MapSum mapSum = new MapSum();
mapSum.insert("apple", 3);  
mapSum.sum("ap");           // 返回 3 (apple = 3)
mapSum.insert("app", 2);    
mapSum.sum("ap");           // 返回 5 (apple + app = 3 + 2 = 5)

```
 

 **提示：** 
-  `1 <= key.length, prefix.length <= 50` 
-  `key` 和 `prefix` 仅由小写英文字母组成
-  `1 <= val <= 1000` 
- 最多调用 `50` 次 `insert` 和 `sum` 
 
**标签**
`设计` `字典树` `哈希表` `字符串` 


## 
```python

```
>
# 678.有效的括号字符串
[https://leetcode-cn.com/problems/valid-parenthesis-string](https://leetcode-cn.com/problems/valid-parenthesis-string) 
## 原题
给定一个只包含三种字符的字符串： `（` ， `）` 和 `*` ，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则：
- 任何左括号 `(` 必须有相应的右括号 `)` 。
- 任何右括号 `)` 必须有相应的左括号 `(` 。
- 左括号 `(` 必须在对应的右括号之前 `)` 。
-  `*` 可以被视为单个右括号 `)` ，或单个左括号 `(` ，或一个空字符串。
- 一个空字符串也被视为有效字符串。
 **示例 1:** 

```

输入: "()"
输出: True

```
 **示例 2:** 

```

输入: "(*)"
输出: True

```
 **示例 3:** 

```

输入: "(*))"
输出: True

```
 **注意:** 
- 字符串大小将在 [1，100] 范围内。
 
**标签**
`栈` `贪心` `字符串` `动态规划` 


## 
```python

```
>
# 679.24 点游戏
[https://leetcode-cn.com/problems/24-game](https://leetcode-cn.com/problems/24-game) 
## 原题
给定一个长度为4的整数数组 `cards` 。你有 `4` 张卡片，每张卡片上都包含一个范围在 `[1,9]` 的数字。您应该使用运算符 `['+', '-', '*', '/']` 和括号 `'('` 和 `')'` 将这些卡片上的数字排列成数学表达式，以获得值24。

你须遵守以下规则:
- 除法运算符 `'/'` 表示实数除法，而不是整数除法。

	
- 例如， `4 /(1 - 2 / 3)= 4 /(1 / 3)= 12` 。
	
	
- 每个运算都在两个数字之间。特别是，不能使用 `“-”` 作为一元运算符。
	
- 例如，如果 `cards =[1,1,1,1]` ，则表达式 `“-1 -1 -1 -1”` 是 **不允许** 的。
	
	
- 你不能把数字串在一起
	
- 例如，如果 `cards =[1,2,1,2]` ，则表达式 `“12 + 12”` 无效。
	
	
如果可以得到这样的表达式，其计算结果为 `24` ，则返回 `true` ，否则返回 `false` 。

 

 **示例 1:** 

```

输入: cards = [4, 1, 8, 7]
输出: true
解释: (8-4) * (7-1) = 24

```
 **示例 2:** 

```

输入: cards = [1, 2, 1, 2]
输出: false

```
 

 **提示:** 
-  `cards.length == 4` 
-  `1 <= cards[i] <= 9` 
 
**标签**
`数组` `数学` `回溯` 


## 
```python

```
>
# 680.验证回文字符串 Ⅱ
[https://leetcode-cn.com/problems/valid-palindrome-ii](https://leetcode-cn.com/problems/valid-palindrome-ii) 
## 原题
给定一个非空字符串  `s` ， **最多** 删除一个字符。判断是否能成为回文字符串。

 

 **示例 1:** 

```

输入: s = "aba"
输出: true

```
 **示例 2:** 

```

输入: s = "abca"
输出: true
解释: 你可以删除c字符。

```
 **示例 3:** 

```

输入: s = "abc"
输出: false
```
 

 **提示:** 
-  `1 <= s.length <= 10^5` 
-  `s` 由小写英文字母组成
 
**标签**
`贪心` `双指针` `字符串` 


## 
```python

```
>
# 681.最近时刻
[https://leetcode-cn.com/problems/next-closest-time](https://leetcode-cn.com/problems/next-closest-time) 
## 原题

 
**标签**
`字符串` `枚举` 


## 
```python

```
>
# 682.棒球比赛
[https://leetcode-cn.com/problems/baseball-game](https://leetcode-cn.com/problems/baseball-game) 
## 原题
你现在是一场采用特殊赛制棒球比赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。

比赛开始时，记录是空白的。你会得到一个记录操作的字符串列表 `ops` ，其中 `ops[i]` 是你需要记录的第 `i` 项操作， `ops` 遵循下述规则：
- 整数 `x` - 表示本回合新获得分数 `x` 
-  `"+"` - 表示本回合新获得的得分是前两次得分的总和。题目数据保证记录此操作时前面总是存在两个有效的分数。
-  `"D"` - 表示本回合新获得的得分是前一次得分的两倍。题目数据保证记录此操作时前面总是存在一个有效的分数。
-  `"C"` - 表示前一次得分无效，将其从记录中移除。题目数据保证记录此操作时前面总是存在一个有效的分数。
请你返回记录中所有得分的总和。

 

 **示例 1：** 

```

输入：ops = ["5","2","C","D","+"]
输出：30
解释：
"5" - 记录加 5 ，记录现在是 [5]
"2" - 记录加 2 ，记录现在是 [5, 2]
"C" - 使前一次得分的记录无效并将其移除，记录现在是 [5].
"D" - 记录加 2 * 5 = 10 ，记录现在是 [5, 10].
"+" - 记录加 5 + 10 = 15 ，记录现在是 [5, 10, 15].
所有得分的总和 5 + 10 + 15 = 30

```
 **示例 2：** 

```

输入：ops = ["5","-2","4","C","D","9","+","+"]
输出：27
解释：
"5" - 记录加 5 ，记录现在是 [5]
"-2" - 记录加 -2 ，记录现在是 [5, -2]
"4" - 记录加 4 ，记录现在是 [5, -2, 4]
"C" - 使前一次得分的记录无效并将其移除，记录现在是 [5, -2]
"D" - 记录加 2 * -2 = -4 ，记录现在是 [5, -2, -4]
"9" - 记录加 9 ，记录现在是 [5, -2, -4, 9]
"+" - 记录加 -4 + 9 = 5 ，记录现在是 [5, -2, -4, 9, 5]
"+" - 记录加 9 + 5 = 14 ，记录现在是 [5, -2, -4, 9, 5, 14]
所有得分的总和 5 + -2 + -4 + 9 + 5 + 14 = 27

```
 **示例 3：** 

```

输入：ops = ["1"]
输出：1

```
 

 **提示：** 
-  `1 <= ops.length <= 1000` 
-  `ops[i]` 为 `"C"` 、 `"D"` 、 `"+"` ，或者一个表示整数的字符串。整数范围是 `[-3 * 10^4, 3 * 10^4]` 
- 对于 `"+"` 操作，题目数据保证记录此操作时前面总是存在两个有效的分数
- 对于 `"C"` 和 `"D"` 操作，题目数据保证记录此操作时前面总是存在一个有效的分数
 
**标签**
`栈` `数组` `模拟` 


## 
```python

```
>
# 683.K 个关闭的灯泡
[https://leetcode-cn.com/problems/k-empty-slots](https://leetcode-cn.com/problems/k-empty-slots) 
## 原题

 
**标签**
`树状数组` `数组` `有序集合` `滑动窗口` 


## 
```python

```
>
# 684.冗余连接
[https://leetcode-cn.com/problems/redundant-connection](https://leetcode-cn.com/problems/redundant-connection) 
## 原题
树可以看成是一个连通且 **无环 ** 的  **无向 ** 图。

给定往一棵  `n` 个节点 (节点值  `1～n` ) 的树中添加一条边后的图。添加的边的两个顶点包含在 `1` 到 `n`  中间，且这条附加的边不属于树中已存在的边。图的信息记录于长度为 `n` 的二维数组 `edges`  ， `edges[i] = [a<sub>i</sub>, b<sub>i</sub>]`  表示图中在 `ai` 和 `bi` 之间存在一条边。

请找出一条可以删去的边，删除后可使得剩余部分是一个有着 `n` 个节点的树。如果有多个答案，则返回数组  `edges`  中最后出现的边。

 

 **示例 1：** 

<img alt="" src="https://pic.leetcode-cn.com/1626676174-hOEVUL-image.png" style="width: 152px; " />

```

输入: edges = [[1,2], [1,3], [2,3]]
输出: [2,3]

```
 **示例 2：** 

<img alt="" src="https://pic.leetcode-cn.com/1626676179-kGxcmu-image.png" style="width: 250px; " />

```

输入: edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
输出: [1,4]

```
 

 **提示:** 
-  `n == edges.length` 
-  `3 <= n <= 1000` 
-  `edges[i].length == 2` 
-  `1 <= ai < bi <= edges.length` 
-  `ai != bi` 
-  `edges` 中无重复元素
- 给定的图是连通的 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `图` 


## 
```python

```
>
# 685.冗余连接 II
[https://leetcode-cn.com/problems/redundant-connection-ii](https://leetcode-cn.com/problems/redundant-connection-ii) 
## 原题
在本问题中，有根树指满足以下条件的 **有向** 图。该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。

输入一个有向图，该图由一个有着 `n` 个节点（节点值不重复，从 `1` 到 `n` ）的树及一条附加的有向边构成。附加的边包含在 `1` 到 `n` 中的两个不同顶点间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组  `edges` 。 每个元素是一对 `[u<sub>i</sub>, v<sub>i</sub>]` ，用以表示 **有向** 图中连接顶点 `u<sub>i</sub>` 和顶点 `v<sub>i</sub>` 的边，其中 `u<sub>i</sub>` 是 `v<sub>i</sub>` 的一个父节点。

返回一条能删除的边，使得剩下的图是有 `n` 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/graph1.jpg" style="width: 222px; height: 222px;" />
```

输入：edges = [[1,2],[1,3],[2,3]]
输出：[2,3]

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode.com/uploads/2020/12/20/graph2.jpg" style="width: 222px; height: 382px;" />
```

输入：edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
输出：[4,1]

```
 

 **提示：** 
-  `n == edges.length` 
-  `3 <= n <= 1000` 
-  `edges[i].length == 2` 
-  `1 <= u<sub>i</sub>, v<sub>i</sub> <= n` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `图` 


## 
```python

```
>
# 686.重复叠加字符串匹配
[https://leetcode-cn.com/problems/repeated-string-match](https://leetcode-cn.com/problems/repeated-string-match) 
## 原题
给定两个字符串 `a` 和 `b` ，寻找重复叠加字符串 `a` 的最小次数，使得字符串 `b` 成为叠加后的字符串 `a` 的子串，如果不存在则返回 `-1` 。

 **注意：** 字符串 `"abc"` 重复叠加 0 次是 `""` ，重复叠加 1 次是 `"abc"` ，重复叠加 2 次是 `"abcabc"` 。

 

 **示例 1：** 

```
输入：a = "abcd", b = "cdabcdab"
输出：3
解释：a 重复叠加三遍后为 "abcdabcdabcd", 此时 b 是其子串。

```
 **示例 2：** 

```
输入：a = "a", b = "aa"
输出：2

```
 **示例 3：** 

```
输入：a = "a", b = "a"
输出：1

```
 **示例 4：** 

```
输入：a = "abc", b = "wxyz"
输出：-1

```
 

 **提示：** 
-  `1 <= a.length <= 10^4` 
-  `1 <= b.length <= 10^4` 
-  `a` 和 `b` 由小写英文字母组成
 
**标签**
`字符串` `字符串匹配` 


## 
```python

```
>
# 687.最长同值路径
[https://leetcode-cn.com/problems/longest-univalue-path](https://leetcode-cn.com/problems/longest-univalue-path) 
## 原题
给定一个二叉树的<meta charset="UTF-8" /> `root` ，返回 *最长的路径的长度* ，这个路径中的 *每个节点具有相同值* 。 这条路径可以经过也可以不经过根节点。

 **两个节点之间的路径长度** 由它们之间的边数表示。

 

 **示例 1:** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/ex1.jpg" />

```

输入：root = [5,4,5,1,1,5]
输出：2

```
 **示例 2:** 

<img alt="" src="https://assets.leetcode.com/uploads/2020/10/13/ex2.jpg" />

```

输入：root = [1,4,5,4,4,5]
输出：2

```
 

 **提示:** 
- 树的节点数的范围是<meta charset="UTF-8" /> `[0, 10^4]` 
-  `-1000 <= Node.val <= 1000` 
- 树的深度将不超过 `1000` 
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 688.骑士在棋盘上的概率
[https://leetcode-cn.com/problems/knight-probability-in-chessboard](https://leetcode-cn.com/problems/knight-probability-in-chessboard) 
## 原题
在一个 `n x n` 的国际象棋棋盘上，一个骑士从单元格 `(row, column)` 开始，并尝试进行 `k` 次移动。行和列是 **从 0 开始** 的，所以左上单元格是 `(0,0)` ，右下单元格是 `(n - 1, n - 1)` 。

象棋骑士有8种可能的走法，如下图所示。每次移动在基本方向上是两个单元格，然后在正交方向上是一个单元格。

<img src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/knight.png" style="height: 300px; width: 300px;" />

每次骑士要移动时，它都会随机从8种可能的移动中选择一种(即使棋子会离开棋盘)，然后移动到那里。

骑士继续移动，直到它走了 `k` 步或离开了棋盘。

返回 *骑士在棋盘停止移动后仍留在棋盘上的概率* 。

 

 **示例 1：** 

```

输入: n = 3, k = 2, row = 0, column = 0
输出: 0.0625
解释: 有两步(到(1,2)，(2,1))可以让骑士留在棋盘上。
在每一个位置上，也有两种移动可以让骑士留在棋盘上。
骑士留在棋盘上的总概率是0.0625。

```
 **示例 2：** 

```

输入: n = 1, k = 0, row = 0, column = 0
输出: 1.00000

```
 

 **提示:** 
-  `1 <= n <= 25` 
-  `0 <= k <= 100` 
-  `0 <= row, column <= n` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 689.三个无重叠子数组的最大和
[https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays](https://leetcode-cn.com/problems/maximum-sum-of-3-non-overlapping-subarrays) 
## 原题
给你一个整数数组 `nums` 和一个整数 `k` ，找出三个长度为 `k` 、互不重叠、且全部数字和（ `3 * k` 项）最大的子数组，并返回这三个子数组。

以下标的数组形式返回结果，数组中的每一项分别指示每个子数组的起始位置（下标从 **0** 开始）。如果有多个结果，返回字典序最小的一个。

 

 **示例 1：** 

```

输入：nums = [1,2,1,2,6,7,5,1], k = 2
输出：[0,3,5]
解释：子数组 [1, 2], [2, 6], [7, 5] 对应的起始下标为 [0, 3, 5]。
也可以取 [2, 1], 但是结果 [1, 3, 5] 在字典序上更大。

```
 **示例 2：** 

```

输入：nums = [1,2,1,2,1,2,1,2,1], k = 2
输出：[0,2,4]

```
 

 **提示：** 
-  `1 <= nums.length <= 2 * 10^4` 
-  `1 <= nums[i] < 2^16` 
-  `1 <= k <= floor(nums.length / 3)` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 690.员工的重要性
[https://leetcode-cn.com/problems/employee-importance](https://leetcode-cn.com/problems/employee-importance) 
## 原题
给定一个保存员工信息的数据结构，它包含了员工 **唯一的 id** ， **重要度 ** 和 **直系下属的 id** 。

比如，员工 1 是员工 2 的领导，员工 2 是员工 3 的领导。他们相应的重要度为 15 , 10 , 5 。那么员工 1 的数据结构是 [1, 15, [2]] ，员工 2的 数据结构是 [2, 10, [3]] ，员工 3 的数据结构是 [3, 5, []] 。注意虽然员工 3 也是员工 1 的一个下属，但是由于 **并不是直系** 下属，因此没有体现在员工 1 的数据结构中。

现在输入一个公司的所有员工信息，以及单个员工 id ，返回这个员工和他所有下属的重要度之和。

 

 **示例：** 

```

输入：[[1, 5, [2, 3]], [2, 3, []], [3, 3, []]], 1
输出：11
解释：
员工 1 自身的重要度是 5 ，他有两个直系下属 2 和 3 ，而且 2 和 3 的重要度均为 3 。因此员工 1 的总重要度是 5 + 3 + 3 = 11 。

```
 

 **提示：** 
- 一个员工最多有一个 **直系** 领导，但是可以有多个 **直系** 下属
- 员工数量不超过 2000 。
 
**标签**
`深度优先搜索` `广度优先搜索` `哈希表` 


## 
```python

```
>
# 691.贴纸拼词
[https://leetcode-cn.com/problems/stickers-to-spell-word](https://leetcode-cn.com/problems/stickers-to-spell-word) 
## 原题
我们有 `n` 种不同的贴纸。每个贴纸上都有一个小写的英文单词。

您想要拼写出给定的字符串 `target` ，方法是从收集的贴纸中切割单个字母并重新排列它们。如果你愿意，你可以多次使用每个贴纸，每个贴纸的数量是无限的。

返回你需要拼出 `target` 的最小贴纸数量。如果任务不可能，则返回 `-1` 。

 **注意：** 在所有的测试用例中，所有的单词都是从 `1000` 个最常见的美国英语单词中随机选择的，并且 `target` 被选择为两个随机单词的连接。

 

 **示例 1：** 

```

输入： stickers = ["with","example","science"], target = "thehat"
输出：3
解释：
我们可以使用 2 个 "with" 贴纸，和 1 个 "example" 贴纸。
把贴纸上的字母剪下来并重新排列后，就可以形成目标 “thehat“ 了。
此外，这是形成目标字符串所需的最小贴纸数量。

```
 **示例 2:** 

```

输入：stickers = ["notice","possible"], target = "basicbasic"
输出：-1
解释：我们不能通过剪切给定贴纸的字母来形成目标“basicbasic”。
```
 

 **提示:** 
-  `n == stickers.length` 
-  `1 <= n <= 50` 
-  `1 <= stickers[i].length <= 10` 
-  `1 <= target <= 15` 
-  `stickers[i]` 和 `target` 由小写英文单词组成
 
**标签**
`位运算` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 692.前K个高频单词
[https://leetcode-cn.com/problems/top-k-frequent-words](https://leetcode-cn.com/problems/top-k-frequent-words) 
## 原题
给一非空的单词列表，返回前 *k* 个出现次数最多的单词。

返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。

 **示例 1：** 

```

输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
输出: ["i", "love"]
解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
    注意，按字母顺序 "i" 在 "love" 之前。

```
 

 **示例 2：** 

```

输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
输出: ["the", "is", "sunny", "day"]
解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
    出现次数依次为 4, 3, 2 和 1 次。

```
 

 **注意：** 
- 假定 *k* 总为有效值， 1 ≤ *k* ≤ 集合元素数。
- 输入的单词均由小写字母组成。
 

 **扩展练习：** 
- 尝试以 *O* ( *n* log *k* ) 时间复杂度和 *O* ( *n* ) 空间复杂度解决。
 
**标签**
`字典树` `哈希表` `字符串` `桶排序` `计数` `排序` `堆（优先队列）` 


## 
```python

```
>
# 693.交替位二进制数
[https://leetcode-cn.com/problems/binary-number-with-alternating-bits](https://leetcode-cn.com/problems/binary-number-with-alternating-bits) 
## 原题
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

 

 **示例 1：** 

```

输入：n = 5
输出：true
解释：5 的二进制表示是：101

```
 **示例 2：** 

```

输入：n = 7
输出：false
解释：7 的二进制表示是：111.
```
 **示例 3：** 

```

输入：n = 11
输出：false
解释：11 的二进制表示是：1011.
```
 

 **提示：** 
-  `1 <= n <= 2^31 - 1` 
 
**标签**
`位运算` 


## 
```python

```
>
# 694.不同岛屿的数量
[https://leetcode-cn.com/problems/number-of-distinct-islands](https://leetcode-cn.com/problems/number-of-distinct-islands) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `哈希表` `哈希函数` 


## 
```python

```
>
# 695.岛屿的最大面积
[https://leetcode-cn.com/problems/max-area-of-island](https://leetcode-cn.com/problems/max-area-of-island) 
## 原题
给你一个大小为 `m x n` 的二进制矩阵 `grid` 。

 **岛屿** 是由一些相邻的 `1` (代表土地) 构成的组合，这里的「相邻」要求两个 `1` 必须在 **水平或者竖直的四个方向上** 相邻。你可以假设 `grid` 的四个边缘都被 `0` （代表水）包围着。

岛屿的面积是岛上值为 `1` 的单元格的数目。

计算并返回 `grid` 中最大的岛屿面积。如果没有岛屿，则返回面积为 `0` 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg" style="width: 500px; height: 310px;" />
```

输入：grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
输出：6
解释：答案不应该是 11 ，因为岛屿只能包含水平或垂直这四个方向上的 1 。

```
 **示例 2：** 

```

输入：grid = [[0,0,0,0,0,0,0,0]]
输出：0

```
 

 **提示：** 
-  `m == grid.length` 
-  `n == grid[i].length` 
-  `1 <= m, n <= 50` 
-  `grid[i][j]` 为 `0` 或 `1` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` 


## 
```python

```
>
# 696.计数二进制子串
[https://leetcode-cn.com/problems/count-binary-substrings](https://leetcode-cn.com/problems/count-binary-substrings) 
## 原题
给定一个字符串 `s` ，统计并返回具有相同数量 `0` 和 `1` 的非空（连续）子字符串的数量，并且这些子字符串中的所有 `0` 和所有 `1` 都是成组连续的。

重复出现（不同位置）的子串也要统计它们出现的次数。
 

 **示例 1：** 

```

输入：s = "00110011"
输出：6
解释：6 个子串满足具有相同数量的连续 1 和 0 ："0011"、"01"、"1100"、"10"、"0011" 和 "01" 。
注意，一些重复出现的子串（不同位置）要统计它们出现的次数。
另外，"00110011" 不是有效的子串，因为所有的 0（还有 1 ）没有组合在一起。
```
 **示例 2：** 

```

输入：s = "10101"
输出：4
解释：有 4 个子串："10"、"01"、"10"、"01" ，具有相同数量的连续 1 和 0 。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s[i]` 为 `'0'` 或 `'1'` 
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 697.数组的度
[https://leetcode-cn.com/problems/degree-of-an-array](https://leetcode-cn.com/problems/degree-of-an-array) 
## 原题
给定一个非空且只包含非负数的整数数组 `nums` ，数组的 **度** 的定义是指数组里任一元素出现频数的最大值。

你的任务是在 `nums` 中找到与 `nums` 拥有相同大小的度的最短连续子数组，返回其长度。

 

 **示例 1：** 

```

输入：nums = [1,2,2,3,1]
输出：2
解释：
输入数组的度是 2 ，因为元素 1 和 2 的出现频数最大，均为 2 。
连续子数组里面拥有相同度的有如下所示：
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
最短连续子数组 [2, 2] 的长度为 2 ，所以返回 2 。

```
 **示例 2：** 

```

输入：nums = [1,2,2,3,1,4,2]
输出：6
解释：
数组的度是 3 ，因为元素 2 重复出现 3 次。
所以 [2,2,3,1,4,2] 是最短子数组，因此返回 6 。

```
 

 **提示：** 
-  `nums.length` 在 `1` 到 `50,000` 范围内。
-  `nums[i]` 是一个在 `0` 到 `49,999` 范围内的整数。
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 698.划分为k个相等的子集
[https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets](https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets) 
## 原题
给定一个整数数组 `nums` 和一个正整数 `k` ，找出是否有可能把这个数组分成 `k` 个非空子集，其总和都相等。

 **示例 1：** 

```
输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。
```
 

 **提示：** 
-  `1 <= k <= len(nums) <= 16` 
-  `0 < nums[i] < 10000` 
 
**标签**
`位运算` `记忆化搜索` `数组` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 699.掉落的方块
[https://leetcode-cn.com/problems/falling-squares](https://leetcode-cn.com/problems/falling-squares) 
## 原题
在无限长的数轴（即 x 轴）上，我们根据给定的顺序放置对应的正方形方块。

第 `i` 个掉落的方块（ `positions[i] = (left, side_length)` ）是正方形，其中 `left 表示该方块最左边的点位置(positions[i][0])，side_length 表示该方块的边长(positions[i][1])。` 

每个方块的底部边缘平行于数轴（即 x 轴），并且从一个比目前所有的落地方块更高的高度掉落而下。在上一个方块结束掉落，并保持静止后，才开始掉落新方块。

方块的底边具有非常大的粘性，并将保持固定在它们所接触的任何长度表面上（无论是数轴还是其他方块）。邻接掉落的边不会过早地粘合在一起， `因为只有底边才具有粘性。` 

 

返回一个堆叠高度列表 `ans` 。每一个堆叠高度 `ans[i]` 表示在通过 `positions[0], positions[1], ..., positions[i]` 表示的方块掉落结束后，目前所有已经落稳的方块堆叠的最高高度。

 

 

 **示例 1:** 

```
输入: [[1, 2], [2, 3], [6, 1]]
输出: [2, 5, 5]
解释:

第一个方块 positions[0] = [1, 2] 掉落：
_aa
_aa
-------
方块最大高度为 2 。

第二个方块 positions[1] = [2, 3] 掉落：
__aaa
__aaa
__aaa
_aa__
_aa__
--------------
方块最大高度为5。
大的方块保持在较小的方块的顶部，不论它的重心在哪里，因为方块的底部边缘有非常大的粘性。

第三个方块 positions[1] = [6, 1] 掉落：
__aaa
__aaa
__aaa
_aa
_aa___a
-------------- 
方块最大高度为5。

因此，我们返回结果[2, 5, 5]。

```
 

 **示例 2:** 

```
输入: [[100, 100], [200, 100]]
输出: [100, 100]
解释: 相邻的方块不会过早地卡住，只有它们的底部边缘才能粘在表面上。

```
 

 **注意:** 
-  `1 <= positions.length <= 1000` .
-  `1 <= positions[i][0] <= 10^8` .
-  `1 <= positions[i][1] <= 10^6` .
 

 
**标签**
`线段树` `数组` `有序集合` 


## 
```python

```
>
# 700.二叉搜索树中的搜索
[https://leetcode-cn.com/problems/search-in-a-binary-search-tree](https://leetcode-cn.com/problems/search-in-a-binary-search-tree) 
## 原题
给定二叉搜索树（BST）的根节点<meta charset="UTF-8" /> `root` 和一个整数值<meta charset="UTF-8" /> `val` 。

你需要在 BST 中找到节点值等于 `val` 的节点。 返回以该节点为根的子树。 如果节点不存在，则返回<meta charset="UTF-8" /> `null` 。

 

 **示例 1:** 

<img alt="" src="https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg" style="height: 179px; width: 250px;" /><meta charset="UTF-8" />

```

输入：root = [4,2,7,1,3], val = 2
输出：[2,1,3]

```
 **Example 2:** 
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg" style="height: 179px; width: 250px;" />
```

输入：root = [4,2,7,1,3], val = 5
输出：[]

```
 

 **提示：** 
- 数中节点数在 `[1, 5000]` 范围内
-  `1 <= Node.val <= 10^7` 
-  `root` 是二叉搜索树
-  `1 <= val <= 10^7` 
 
**标签**
`树` `二叉搜索树` `二叉树` 


## 
```python

```
>
