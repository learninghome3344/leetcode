# 1101.彼此熟识的最早时间
[https://leetcode-cn.com/problems/the-earliest-moment-when-everyone-become-friends](https://leetcode-cn.com/problems/the-earliest-moment-when-everyone-become-friends) 
## 原题

 
**标签**
`并查集` `数组` 


## 
```python

```
>
# 1102.得分最高的路径
[https://leetcode-cn.com/problems/path-with-maximum-minimum-value](https://leetcode-cn.com/problems/path-with-maximum-minimum-value) 
## 原题

 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `矩阵` `堆（优先队列）` 


## 
```python

```
>
# 1103.分糖果 II
[https://leetcode-cn.com/problems/distribute-candies-to-people](https://leetcode-cn.com/problems/distribute-candies-to-people) 
## 原题
排排坐，分糖果。

我们买了一些糖果 `candies` ，打算把它们分给排好队的 ** `n = num_people` ** 个小朋友。

给第一个小朋友 1 颗糖果，第二个小朋友 2 颗，依此类推，直到给最后一个小朋友 `n` 颗糖果。

然后，我们再回到队伍的起点，给第一个小朋友 `n + 1` 颗糖果，第二个小朋友 `n + 2` 颗，依此类推，直到给最后一个小朋友 `2 * n` 颗糖果。

重复上述过程（每次都比上一次多给出一颗糖果，当到达队伍终点后再次从队伍起点开始），直到我们分完所有的糖果。注意，就算我们手中的剩下糖果数不够（不比前一次发出的糖果多），这些糖果也会全部发给当前的小朋友。

返回一个长度为 `num_people` 、元素之和为 `candies` 的数组，以表示糖果的最终分发情况（即 `ans[i]` 表示第 `i` 个小朋友分到的糖果数）。

 

 **示例 1：** 

```
输入：candies = 7, num_people = 4
输出：[1,2,3,1]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0,0]。
第三次，ans[2] += 3，数组变为 [1,2,3,0]。
第四次，ans[3] += 1（因为此时只剩下 1 颗糖果），最终数组变为 [1,2,3,1]。

```
 **示例 2：** 

```
输入：candies = 10, num_people = 3
输出：[5,2,3]
解释：
第一次，ans[0] += 1，数组变为 [1,0,0]。
第二次，ans[1] += 2，数组变为 [1,2,0]。
第三次，ans[2] += 3，数组变为 [1,2,3]。
第四次，ans[0] += 4，最终数组变为 [5,2,3]。

```
 

 **提示：** 
-  `1 <= candies <= 10^9` 
-  `1 <= num_people <= 1000` 
 
**标签**
`数学` `模拟` 


## 
```python

```
>
# 1104.二叉树寻路
[https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree](https://leetcode-cn.com/problems/path-in-zigzag-labelled-binary-tree) 
## 原题
在一棵无限的二叉树上，每个节点都有两个子节点，树中的节点 **逐行** 依次按 “之” 字形进行标记。

如下图所示，在奇数行（即，第一行、第三行、第五行&hellip;&hellip;）中，按从左到右的顺序进行标记；

而偶数行（即，第二行、第四行、第六行&hellip;&hellip;）中，按从右到左的顺序进行标记。

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/28/tree.png" style="height: 138px; width: 300px;">

给你树上某一个节点的标号 `label` ，请你返回从根节点到该标号为 `label` 节点的路径，该路径是由途经的节点标号所组成的。

 

 **示例 1：** 

```
输入：label = 14
输出：[1,3,4,14]

```
 **示例 2：** 

```
输入：label = 26
输出：[1,2,6,10,26]

```
 

 **提示：** 
-  `1 <= label <= 10^6` 
 
**标签**
`树` `数学` `二叉树` 


## 
```python

```
>
# 1105.填充书架
[https://leetcode-cn.com/problems/filling-bookcase-shelves](https://leetcode-cn.com/problems/filling-bookcase-shelves) 
## 原题
附近的家居城促销，你买回了一直心仪的可调节书架，打算把自己的书都整理到新的书架上。

你把要摆放的书 `books` 都整理好，叠成一摞：从上往下，第 `i` 本书的厚度为 `books[i][0]` ，高度为 `books[i][1]` 。

 **按顺序** 将这些书摆放到总宽度为 `shelf_width` 的书架上。

先选几本书放在书架上（它们的厚度之和小于等于书架的宽度 `shelf_width` ），然后再建一层书架。重复这个过程，直到把所有的书都放在书架上。

需要注意的是，在上述过程的每个步骤中， **摆放书的顺序与你整理好的顺序相同** 。 例如，如果这里有 5 本书，那么可能的一种摆放情况是：第一和第二本书放在第一层书架上，第三本书放在第二层书架上，第四和第五本书放在最后一层书架上。

每一层所摆放的书的最大高度就是这一层书架的层高，书架整体的高度为各层高之和。

以这种方式布置书架，返回书架整体可能的最小高度。

 

 **示例：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/06/28/shelves.png" style="width: 150px;">

```
输入：books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
输出：6
解释：
3 层书架的高度和为 1 + 3 + 2 = 6 。
第 2 本书不必放在第一层书架上。

```
 

 **提示：** 
-  `1 <= books.length <= 1000` 
-  `1 <= books[i][0] <= shelf_width <= 1000` 
-  `1 <= books[i][1] <= 1000` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1106.解析布尔表达式
[https://leetcode-cn.com/problems/parsing-a-boolean-expression](https://leetcode-cn.com/problems/parsing-a-boolean-expression) 
## 原题
给你一个以字符串形式表述的 <a href="https://baike.baidu.com/item/%E5%B8%83%E5%B0%94%E8%A1%A8%E8%BE%BE%E5%BC%8F/1574380?fr=aladdin" target="_blank">布尔表达式</a>（boolean） `expression` ，返回该式的运算结果。

有效的表达式需遵循以下约定：
-  `"t"` ，运算结果为 `True` 
-  `"f"` ，运算结果为 `False` 
-  `"!(expr)"` ，运算过程为对内部表达式 `expr` 进行逻辑 **非的运算** （NOT）
-  `"&amp;(expr1,expr2,...)"` ，运算过程为对 2 个或以上内部表达式 `expr1, expr2, ...` 进行逻辑 **与的运算** （AND）
-  `"|(expr1,expr2,...)"` ，运算过程为对 2 个或以上内部表达式 `expr1, expr2, ...` 进行逻辑 **或的运算** （OR）
 

 **示例 1：** 

```
输入：expression = "!(f)"
输出：true

```
 **示例 2：** 

```
输入：expression = "|(f,t)"
输出：true

```
 **示例 3：** 

```
输入：expression = "&amp;(t,f)"
输出：false

```
 **示例 4：** 

```
输入：expression = "|(&amp;(t,f,t),!(t))"
输出：false

```
 

 **提示：** 
-  `1 <= expression.length <= 20000` 
-  `expression[i]` 由 `{';(';, ';)';, ';&amp;';, ';|';, ';!';, ';t';, ';f';, ';,';}` 中的字符组成。
-  `expression` 是以上述形式给出的有效表达式，表示一个布尔值。
 
**标签**
`栈` `递归` `字符串` 


## 
```python

```
>
# 1107.每日新用户统计
[https://leetcode-cn.com/problems/new-users-daily-count](https://leetcode-cn.com/problems/new-users-daily-count) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1108.IP 地址无效化
[https://leetcode-cn.com/problems/defanging-an-ip-address](https://leetcode-cn.com/problems/defanging-an-ip-address) 
## 原题
给你一个有效的 <a href="https://baike.baidu.com/item/IPv4" target="_blank">IPv4</a> 地址 `address` ，返回这个 IP 地址的无效化版本。

所谓无效化 IP 地址，其实就是用 `"[.]"` 代替了每个 `"."` 。

 

 **示例 1：** 

```
输入：address = "1.1.1.1"
输出："1[.]1[.]1[.]1"

```
 **示例 2：** 

```
输入：address = "255.100.50.0"
输出："255[.]100[.]50[.]0"

```
 

 **提示：** 
- 给出的 `address` 是一个有效的 IPv4 地址
 
**标签**
`字符串` 


## 
```python

```
>
# 1109.航班预订统计
[https://leetcode-cn.com/problems/corporate-flight-bookings](https://leetcode-cn.com/problems/corporate-flight-bookings) 
## 原题
这里有 `n` 个航班，它们分别从 `1` 到 `n` 进行编号。

有一份航班预订表 `bookings` ，表中第 `i` 条预订记录 `bookings[i] = [first<sub>i</sub>, last<sub>i</sub>, seats<sub>i</sub>]` 意味着在从 `first<sub>i</sub>` 到 `last<sub>i</sub>` （ **包含** `first<sub>i</sub>` 和 `last<sub>i</sub>` ）的 **每个航班** 上预订了 `seats<sub>i</sub>` 个座位。

请你返回一个长度为 `n` 的数组 `answer` ，里面的元素是每个航班预定的座位总数。

 

 **示例 1：** 

```

输入：bookings = [[1,2,10],[2,3,20],[2,5,25]], n = 5
输出：[10,55,45,25,25]
解释：
航班编号        1   2   3   4   5
预订记录 1 ：   10  10
预订记录 2 ：       20  20
预订记录 3 ：       25  25  25  25
总座位数：      10  55  45  25  25
因此，answer = [10,55,45,25,25]

```
 **示例 2：** 

```

输入：bookings = [[1,2,10],[2,2,15]], n = 2
输出：[10,25]
解释：
航班编号        1   2
预订记录 1 ：   10  10
预订记录 2 ：       15
总座位数：      10  25
因此，answer = [10,25]

```
 

 **提示：** 
-  `1 <= n <= 2 * 10^4` 
-  `1 <= bookings.length <= 2 * 10^4` 
-  `bookings[i].length == 3` 
-  `1 <= first<sub>i</sub> <= last<sub>i</sub> <= n` 
-  `1 <= seats<sub>i</sub> <= 10^4` 
 
**标签**
`数组` `前缀和` 


## 
```python

```
>
# 1110.删点成林
[https://leetcode-cn.com/problems/delete-nodes-and-return-forest](https://leetcode-cn.com/problems/delete-nodes-and-return-forest) 
## 原题
给出二叉树的根节点 `root` ，树上每个节点都有一个不同的值。

如果节点值在 `to_delete` 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

返回森林中的每棵树。你可以按任意顺序组织答案。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/07/05/screen-shot-2019-07-01-at-53836-pm.png" style="height: 150px; width: 237px;" />** 

```

输入：root = [1,2,3,4,5,6,7], to_delete = [3,5]
输出：[[1,2,null,4],[6],[7]]

```
 **示例 2：** 

```

输入：root = [1,2,4,null,3], to_delete = [3]
输出：[[1,2,4]]

```
 

 **提示：** 
- 树中的节点数最大为 `1000` 。
- 每个节点都有一个介于 `1` 到 `1000` 之间的值，且各不相同。
-  `to_delete.length <= 1000` 
-  `to_delete` 包含一些从 `1` 到 `1000` 、各不相同的值。
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1111.有效括号的嵌套深度
[https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings](https://leetcode-cn.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings) 
## 原题
 **有效括号字符串** 定义：对于每个左括号，都能找到与之对应的右括号，反之亦然。详情参见题末「 **有效括号字符串** 」部分。

 **嵌套深度** `depth` 定义：即有效括号字符串嵌套的层数， `depth(A)` 表示有效括号字符串 `A` 的嵌套深度。详情参见题末「 **嵌套深度** 」部分。

有效括号字符串类型与对应的嵌套深度计算方法如下图所示：

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/04/01/1111.png" style="height: 152px; width: 600px;">

 

给你一个「有效括号字符串」 `seq` ，请你将其分成两个不相交的有效括号字符串， `A` 和 `B` ，并使这两个字符串的深度最小。
- 不相交：每个 `seq[i]` 只能分给 `A` 和 `B` 二者中的一个，不能既属于 `A` 也属于 `B` 。
-  `A` 或 `B` 中的元素在原字符串中可以不连续。
-  `A.length + B.length = seq.length` 
- 深度最小： `max(depth(A), depth(B))` 的可能取值最小。 
划分方案用一个长度为 `seq.length` 的答案数组 `answer` 表示，编码规则如下：
-  `answer[i] = 0` ， `seq[i]` 分给 `A` 。
-  `answer[i] = 1` ， `seq[i]` 分给 `B` 。
如果存在多个满足要求的答案，只需返回其中任意 **一个** 即可。

 

 **示例 1：** 

```
输入：seq = "(()())"
输出：[0,1,1,1,1,0]

```
 **示例 2：** 

```
输入：seq = "()(())()"
输出：[0,0,0,1,1,0,1,1]
解释：本示例答案不唯一。
按此输出 A = "()()", B = "()()", max(depth(A), depth(B)) = 1，它们的深度最小。
像 [1,1,1,0,0,1,1,1]，也是正确结果，其中 A = "()()()", B = "()", max(depth(A), depth(B)) = 1 。 

```
 

 **提示：** 
-  `1 < seq.size <= 10000` 
 

 **有效括号字符串：** 

```
仅由 "(" 和 ")" 构成的字符串，对于每个左括号，都能找到与之对应的右括号，反之亦然。
下述几种情况同样属于有效括号字符串：

  1. 空字符串
  2. 连接，可以记作 AB（A 与 B 连接），其中 A 和 B 都是有效括号字符串
  3. 嵌套，可以记作 (A)，其中 A 是有效括号字符串

```
 **嵌套深度：** 

```
类似地，我们可以定义任意有效括号字符串 s 的 嵌套深度 depth(S)：

  1. s 为空时，depth("") = 0
  2. s 为 A 与 B 连接时，depth(A + B) = max(depth(A), depth(B))，其中 A 和 B 都是有效括号字符串
  3. s 为嵌套情况，depth("(" + A + ")") = 1 + depth(A)，其中 A 是有效括号字符串

例如：""，"()()"，和 "()(()())" 都是有效括号字符串，嵌套深度分别为 0，1，2，而 ")(" 和 "(()" 都不是有效括号字符串。

```
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 1112.每位学生的最高成绩
[https://leetcode-cn.com/problems/highest-grade-for-each-student](https://leetcode-cn.com/problems/highest-grade-for-each-student) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1113.报告的记录
[https://leetcode-cn.com/problems/reported-posts](https://leetcode-cn.com/problems/reported-posts) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1114.按序打印
[https://leetcode-cn.com/problems/print-in-order](https://leetcode-cn.com/problems/print-in-order) 
## 原题
给你一个类：

```

public class Foo {
  public void first() { print("first"); }
  public void second() { print("second"); }
  public void third() { print("third"); }
}
```
三个不同的线程 A、B、C 将会共用一个 `Foo` 实例。
- 线程 A 将会调用 `first()` 方法
- 线程 B 将会调用 `second()` 方法
- 线程 C 将会调用 `third()` 方法
请设计修改程序，以确保 `second()` 方法在 `first()` 方法之后被执行， `third()` 方法在 `second()` 方法之后被执行。

 **提示：** 
- 尽管输入中的数字似乎暗示了顺序，但是我们并不保证线程在操作系统中的调度顺序。
- 你看到的输入格式主要是为了确保测试的全面性。
 

 **示例 1：** 

```

输入：nums = [1,2,3]
输出："firstsecondthird"
解释：
有三个线程会被异步启动。输入 [1,2,3] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 second() 方法，线程 C 将会调用 third() 方法。正确的输出是 "firstsecondthird"。

```
 **示例 2：** 

```

输入：nums = [1,3,2]
输出："firstsecondthird"
解释：
输入 [1,3,2] 表示线程 A 将会调用 first() 方法，线程 B 将会调用 third() 方法，线程 C 将会调用 second() 方法。正确的输出是 "firstsecondthird"。
```
 
 **提示：** 
-  `nums` 是 `[1, 2, 3]` 的一组排列
 
**标签**
`多线程` 


## 
```python

```
>
# 1115.交替打印 FooBar
[https://leetcode-cn.com/problems/print-foobar-alternately](https://leetcode-cn.com/problems/print-foobar-alternately) 
## 原题
给你一个类：

```

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}

```
两个不同的线程将会共用一个 `FooBar` 实例：
- 线程 A 将会调用 `foo()` 方法，而
- 线程 B 将会调用 `bar()` 方法
请设计修改程序，以确保 `"foobar"` 被输出 `n` 次。

 

 **示例 1：** 

```

输入：n = 1
输出："foobar"
解释：这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。

```
 **示例 2：** 

```

输入：n = 2
输出："foobarfoobar"
解释："foobar" 将被输出两次。

```
 

 **提示：** 
-  `1 <= n <= 1000` 
 
**标签**
`多线程` 


## 
```python

```
>
# 1116.打印零与奇偶数
[https://leetcode-cn.com/problems/print-zero-even-odd](https://leetcode-cn.com/problems/print-zero-even-odd) 
## 原题
现有函数 `printNumber` 可以用一个整数参数调用，并输出该整数到控制台。
- 例如，调用 `printNumber(7)` 将会输出 `7` 到控制台。
给你类 `ZeroEvenOdd` 的一个实例，该类中有三个函数： `zero` 、 `even` 和 `odd` 。 `ZeroEvenOdd` 的相同实例将会传递给三个不同线程：
-  **线程 A：** 调用 `zero()` ，只输出 `0` 
-  **线程 B：** 调用 `even()` ，只输出偶数
-  **线程 C：** 调用 `odd()` ，只输出奇数
修改给出的类，以输出序列 `"010203040506..."` ，其中序列的长度必须为 `2n` 。

实现 `ZeroEvenOdd` 类：
-  `ZeroEvenOdd(int n)` 用数字 `n` 初始化对象，表示需要输出的数。
-  `void zero(printNumber)` 调用 `printNumber` 以输出一个 0 。
-  `void even(printNumber)` 调用 `printNumber` 以输出偶数。
-  `void odd(printNumber)` 调用 `printNumber` 以输出奇数。
 

 **示例 1：** 

```

输入：n = 2
输出："0102"
解释：三条线程异步执行，其中一个调用 zero()，另一个线程调用 even()，最后一个线程调用odd()。正确的输出为 "0102"。

```
 **示例 2：** 

```

输入：n = 5
输出："0102030405"

```
 

 **提示：** 
-  `1 <= n <= 1000` 
 
**标签**
`多线程` 


## 
```python

```
>
# 1117.H2O 生成
[https://leetcode-cn.com/problems/building-h2o](https://leetcode-cn.com/problems/building-h2o) 
## 原题
现在有两种线程，氧 `oxygen` 和氢 `hydrogen` ，你的目标是组织这两种线程来产生水分子。

存在一个屏障（barrier）使得每个线程必须等候直到一个完整水分子能够被产生出来。

氢和氧线程会被分别给予 `releaseHydrogen` 和 `releaseOxygen` 方法来允许它们突破屏障。

这些线程应该三三成组突破屏障并能立即组合产生一个水分子。

你必须保证产生一个水分子所需线程的结合必须发生在下一个水分子产生之前。

换句话说:
- 如果一个氧线程到达屏障时没有氢线程到达，它必须等候直到两个氢线程到达。
- 如果一个氢线程到达屏障时没有其它线程到达，它必须等候直到一个氧线程和另一个氢线程到达。
书写满足这些限制条件的氢、氧线程同步代码。

 

 **示例 1:** 

```

输入: water = "HOH"
输出: "HHO"
解释: "HOH" 和 "OHH" 依然都是有效解。

```
 **示例 2:** 

```

输入: water = "OOHHHH"
输出: "HHOHHO"
解释: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" 和 "OHHOHH" 依然都是有效解。

```
 

 **提示：** 
-  `3 * n == water.length` 
-  `1 <= n <= 20` 
-  `water[i] == 'O' or 'H'` 
- 输入字符串 `water` 中的 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'H'</span></span></font></font> 总数将会是 `2 * n` 。
- 输入字符串 `water` 中的 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'O'</span></span></font></font> 总数将会是 `n` 。
 
**标签**
`多线程` 


## 
```python

```
>
# 1118.一月有多少天
[https://leetcode-cn.com/problems/number-of-days-in-a-month](https://leetcode-cn.com/problems/number-of-days-in-a-month) 
## 原题

 
**标签**
`数学` 


## 
```python

```
>
# 1119.删去字符串中的元音
[https://leetcode-cn.com/problems/remove-vowels-from-a-string](https://leetcode-cn.com/problems/remove-vowels-from-a-string) 
## 原题

 
**标签**
`字符串` 


## 
```python

```
>
# 1120.子树的最大平均值
[https://leetcode-cn.com/problems/maximum-average-subtree](https://leetcode-cn.com/problems/maximum-average-subtree) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1121.将数组分成几个递增序列
[https://leetcode-cn.com/problems/divide-array-into-increasing-sequences](https://leetcode-cn.com/problems/divide-array-into-increasing-sequences) 
## 原题

 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1122.数组的相对排序
[https://leetcode-cn.com/problems/relative-sort-array](https://leetcode-cn.com/problems/relative-sort-array) 
## 原题
给你两个数组， `arr1` 和 `arr2` ， `arr2` 中的元素各不相同， `arr2` 中的每个元素都出现在 `arr1` 中。

对 `arr1` 中的元素进行排序，使 `arr1` 中项的相对顺序和 `arr2` 中的相对顺序相同。未在 `arr2` 中出现过的元素需要按照升序放在 `arr1` 的末尾。

 

 **示例 1：** 

```

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]

```
 **示例  2:** 

```

输入：arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
输出：[22,28,8,6,17,44]

```
 

 **提示：** 
-  `1 <= arr1.length, arr2.length <= 1000` 
-  `0 <= arr1[i], arr2[i] <= 1000` 
-  `arr2` 中的元素 `arr2[i]` **各不相同** 
-  `arr2` 中的每个元素 `arr2[i]` 都出现在 `arr1` 中
 
**标签**
`数组` `哈希表` `计数排序` `排序` 


## 
```python

```
>
# 1123.最深叶节点的最近公共祖先
[https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves](https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves) 
## 原题
给你一个有根节点<meta charset="UTF-8" /> `root` 的二叉树，返回它 *最深的叶节点的最近公共祖先* 。

回想一下：
-  **叶节点** 是二叉树中没有子节点的节点
- 树的根节点的 **深度** 为 `0` ，如果某一节点的深度为 `d` ，那它的子节点的深度就是 `d+1` 
- 如果我们假定 `A` 是一组节点 `S` 的 **最近公共祖先** ， `S` 中的每个节点都在以 `A` 为根节点的子树中，且 `A` 的深度达到此条件下可能的最大值。
 

 **示例 1：** 
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/01/sketch1.png" style="height: 340px; width: 400px;" />
```

输入：root = [3,5,1,6,2,0,8,null,null,7,4]
输出：[2,7,4]
解释：我们返回值为 2 的节点，在图中用黄色标记。
在图中用蓝色标记的是树的最深的节点。
注意，节点 6、0 和 8 也是叶节点，但是它们的深度是 2 ，而节点 7 和 4 的深度是 3 。

```
 **示例 2：** 

```

输入：root = [1]
输出：[1]
解释：根节点是树中最深的节点，它是它本身的最近公共祖先。

```
 **示例 3：** 

```

输入：root = [0,1,3,null,2]
输出：[2]
解释：树中最深的叶节点是 2 ，最近公共祖先是它自己。
```
 

 **提示：** 
- 树中的节点数将在<meta charset="UTF-8" /> `[1, 1000]` 的范围内。
-  `0 <= Node.val <= 1000` 
- 每个节点的值都是 **独一无二** 的。
 

 **注意：** 本题与力扣 865 重复：<a href="https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/">https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/</a>

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `哈希表` `二叉树` 


## 
```python

```
>
# 1124.表现良好的最长时间段
[https://leetcode-cn.com/problems/longest-well-performing-interval](https://leetcode-cn.com/problems/longest-well-performing-interval) 
## 原题
给你一份工作时间表 `hours` ，上面记录着某一位员工每天的工作小时数。

我们认为当员工一天中的工作小时数大于 `8` 小时的时候，那么这一天就是「 **劳累的一天** 」。

所谓「表现良好的时间段」，意味在这段时间内，「劳累的天数」是严格 **大于** 「不劳累的天数」。

请你返回「表现良好时间段」的最大长度。

 

 **示例 1：** 

```

输入：hours = [9,9,6,0,6,6,9]
输出：3
解释：最长的表现良好时间段是 [9,9,6]。
```
 **示例 2：** 

```

输入：hours = [6,6,6]
输出：0

```
 

 **提示：** 
-  `1 <= hours.length <= 10^4` 
-  `0 <= hours[i] <= 16` 
 
**标签**
`栈` `数组` `哈希表` `前缀和` `单调栈` 


## 
```python

```
>
# 1125.最小的必要团队
[https://leetcode-cn.com/problems/smallest-sufficient-team](https://leetcode-cn.com/problems/smallest-sufficient-team) 
## 原题
作为项目经理，你规划了一份需求的技能清单  `req_skills` ，并打算从备选人员名单  `people`  中选出些人组成一个「必要团队」（ 编号为  `i`  的备选人员  `people[i]`  含有一份该备选人员掌握的技能列表）。

所谓「必要团队」，就是在这个团队中，对于所需求的技能列表  `req_skills` 中列出的每项技能，团队中至少有一名成员已经掌握。可以用每个人的编号来表示团队中的成员：
- 例如，团队  `team = [0, 1, 3]`  表示掌握技能分别为  `people[0]` ， `people[1]` ，和  `people[3]`  的备选人员。
请你返回 **任一**  规模最小的必要团队，团队成员用人员编号表示。你可以按 **任意顺序** 返回答案，题目数据保证答案存在。

 

 **示例 1：** 

```

输入：req_skills = ["java","nodejs","reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
输出：[0,2]

```
 **示例 2：** 

```

输入：req_skills = ["algorithms","math","java","reactjs","csharp","aws"], people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
输出：[1,2]

```
 

 **提示：** 
-  `1 <= req_skills.length <= 16` 
-  `1 <= req_skills[i].length <= 16` 
-  `req_skills[i]` 由小写英文字母组成
-  `req_skills` 中的所有字符串 **互不相同** 
-  `1 <= people.length <= 60` 
-  `0 <= people[i].length <= 16` 
-  `1 <= people[i][j].length <= 16` 
-  `people[i][j]` 由小写英文字母组成
-  `people[i]` 中的所有字符串 **互不相同** 
-  `people[i]` 中的每个技能是 `req_skills` 中的技能
- 题目数据保证「必要团队」一定存在
 
**标签**
`位运算` `数组` `动态规划` `状态压缩` 


## 
```python

```
>
# 1126.查询活跃业务
[https://leetcode-cn.com/problems/active-businesses](https://leetcode-cn.com/problems/active-businesses) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1127.用户购买平台
[https://leetcode-cn.com/problems/user-purchase-platform](https://leetcode-cn.com/problems/user-purchase-platform) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1128.等价多米诺骨牌对的数量
[https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs](https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs) 
## 原题
给你一个由一些多米诺骨牌组成的列表 `dominoes` 。

如果其中某一张多米诺骨牌可以通过旋转 `0` 度或 `180` 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。

形式上， `dominoes[i] = [a, b]` 和 `dominoes[j] = [c, d]` 等价的前提是 `a==c` 且 `b==d` ，或是 `a==d` 且 `b==c` 。

在 `0 <= i < j < dominoes.length` 的前提下，找出满足 `dominoes[i]` 和 `dominoes[j]` 等价的骨牌对 `(i, j)` 的数量。

 

 **示例：** 

```
输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1

```
 

 **提示：** 
-  `1 <= dominoes.length <= 40000` 
-  `1 <= dominoes[i][j] <= 9` 
 
**标签**
`数组` `哈希表` `计数` 


## 
```python

```
>
# 1129.颜色交替的最短路径
[https://leetcode-cn.com/problems/shortest-path-with-alternating-colors](https://leetcode-cn.com/problems/shortest-path-with-alternating-colors) 
## 原题
在一个有向图中，节点分别标记为 `0, 1, ..., n-1` 。这个图中的每条边不是红色就是蓝色，且存在自环或平行边。

 `red_edges` 中的每一个 `[i, j]` 对表示从节点 `i` 到节点 `j` 的红色有向边。类似地， `blue_edges` 中的每一个 `[i, j]` 对表示从节点 `i` 到节点 `j` 的蓝色有向边。

返回长度为 `n` 的数组 `answer` ，其中 `answer[X]` 是从节点 `0` 到节点 `X` 的红色边和蓝色边交替出现的最短路径的长度。如果不存在这样的路径，那么 `answer[x] = -1` 。

 

 **示例 1：** 

```
输入：n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
输出：[0,1,-1]

```
 **示例 2：** 

```
输入：n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
输出：[0,1,-1]

```
 **示例 3：** 

```
输入：n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
输出：[0,-1,-1]

```
 **示例 4：** 

```
输入：n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
输出：[0,1,2]

```
 **示例 5：** 

```
输入：n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
输出：[0,1,1]

```
 

 **提示：** 
-  `1 <= n <= 100` 
-  `red_edges.length <= 400` 
-  `blue_edges.length <= 400` 
-  `red_edges[i].length == blue_edges[i].length == 2` 
-  `0 <= red_edges[i][j], blue_edges[i][j] < n` 
 
**标签**
`广度优先搜索` `图` 


## 
```python

```
>
# 1130.叶值的最小代价生成树
[https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values](https://leetcode-cn.com/problems/minimum-cost-tree-from-leaf-values) 
## 原题
给你一个正整数数组 `arr` ，考虑所有满足以下条件的二叉树：
- 每个节点都有 0 个或是 2 个子节点。
- 数组 `arr` 中的值与树的中序遍历中每个叶节点的值一一对应。（知识回顾：如果一个节点有 0 个子节点，那么该节点为叶节点。）
- 每个非叶节点的值等于其左子树和右子树中叶节点的最大值的乘积。
在所有这样的二叉树中，返回每个非叶节点的值的最小可能总和。这个和的值是一个 32 位整数。

 

 **示例：** 

```
输入：arr = [6,2,4]
输出：32
解释：
有两种可能的树，第一种的非叶节点的总和为 36，第二种非叶节点的总和为 32。

    24            24
   /  \          /  \
  12   4        6    8
 /  \               / \
6    2             2   4
```
 

 **提示：** 
-  `2 <= arr.length <= 40` 
-  `1 <= arr[i] <= 15` 
- 答案保证是一个 32 位带符号整数，即小于 `2^31` 。
 
**标签**
`栈` `贪心` `动态规划` `单调栈` 


## 
```python

```
>
# 1131.绝对值表达式的最大值
[https://leetcode-cn.com/problems/maximum-of-absolute-value-expression](https://leetcode-cn.com/problems/maximum-of-absolute-value-expression) 
## 原题
给你两个长度相等的整数数组，返回下面表达式的最大值：

 `|arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|` 

其中下标 `i` ， `j` 满足 `0 <= i, j < arr1.length` 。

 

 **示例 1：** 

```
输入：arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
输出：13

```
 **示例 2：** 

```
输入：arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
输出：20
```
 

 **提示：** 
-  `2 <= arr1.length == arr2.length <= 40000` 
-  `-10^6 <= arr1[i], arr2[i] <= 10^6` 
 
**标签**
`数组` `数学` 


## 
```python

```
>
# 1132.报告的记录 II
[https://leetcode-cn.com/problems/reported-posts-ii](https://leetcode-cn.com/problems/reported-posts-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1133.最大唯一数
[https://leetcode-cn.com/problems/largest-unique-number](https://leetcode-cn.com/problems/largest-unique-number) 
## 原题

 
**标签**
`数组` `哈希表` `排序` 


## 
```python

```
>
# 1134.阿姆斯特朗数
[https://leetcode-cn.com/problems/armstrong-number](https://leetcode-cn.com/problems/armstrong-number) 
## 原题

 
**标签**
`数学` 


## 
```python

```
>
# 1135.最低成本联通所有城市
[https://leetcode-cn.com/problems/connecting-cities-with-minimum-cost](https://leetcode-cn.com/problems/connecting-cities-with-minimum-cost) 
## 原题

 
**标签**
`并查集` `图` `最小生成树` `堆（优先队列）` 


## 
```python

```
>
# 1136.平行课程
[https://leetcode-cn.com/problems/parallel-courses](https://leetcode-cn.com/problems/parallel-courses) 
## 原题

 
**标签**
`图` `拓扑排序` 


## 
```python

```
>
# 1137.第 N 个泰波那契数
[https://leetcode-cn.com/problems/n-th-tribonacci-number](https://leetcode-cn.com/problems/n-th-tribonacci-number) 
## 原题
泰波那契序列 T<sub>n</sub> 定义如下： 

T<sub>0</sub> = 0, T<sub>1</sub> = 1, T<sub>2</sub> = 1, 且在 n >= 0 的条件下 T<sub>n+3</sub> = T<sub>n</sub> + T<sub>n+1</sub> + T<sub>n+2</sub>

给你整数 `n` ，请返回第 n 个泰波那契数 T<sub>n </sub>的值。

 

 **示例 1：** 

```
输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4

```
 **示例 2：** 

```
输入：n = 25
输出：1389537

```
 

 **提示：** 
-  `0 <= n <= 37` 
- 答案保证是一个 32 位整数，即 `answer <= 2^31 - 1` 。
 
**标签**
`记忆化搜索` `数学` `动态规划` 


## 
```python

```
>
# 1138.字母板上的路径
[https://leetcode-cn.com/problems/alphabet-board-path](https://leetcode-cn.com/problems/alphabet-board-path) 
## 原题
我们从一块字母板上的位置 `(0, 0)` 出发，该坐标对应的字符为 `board[0][0]` 。

在本题里，字母板为 `board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]` ，如下所示。

<img alt="" src="https://assets.leetcode.com/uploads/2019/07/28/azboard.png" style="width: 300px;" />

我们可以按下面的指令规则行动：
- 如果方格存在， `'U'` 意味着将我们的位置上移一行；
- 如果方格存在， `'D'` 意味着将我们的位置下移一行；
- 如果方格存在， `'L'` 意味着将我们的位置左移一列；
- 如果方格存在， `'R'` 意味着将我们的位置右移一列；
-  `'!'` 会把在我们当前位置 `(r, c)` 的字符 `board[r][c]` 添加到答案中。
（注意，字母板上只存在有字母的位置。）

返回指令序列，用最小的行动次数让答案和目标 `target` 相同。你可以返回任何达成目标的路径。

 

 **示例 1：** 

```

输入：target = "leet"
输出："DDR!UURRR!!DDD!"

```
 **示例 2：** 

```

输入：target = "code"
输出："RR!DDRR!UUL!R!"

```
 

 **提示：** 
-  `1 <= target.length <= 100` 
-  `target` 仅含有小写英文字母。
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1139.最大的以 1 为边界的正方形
[https://leetcode-cn.com/problems/largest-1-bordered-square](https://leetcode-cn.com/problems/largest-1-bordered-square) 
## 原题
给你一个由若干 `0` 和 `1` 组成的二维网格 `grid` ，请你找出边界全部由 `1` 组成的最大 **正方形** 子网格，并返回该子网格中的元素数量。如果不存在，则返回 `0` 。

 

 **示例 1：** 

```
输入：grid = [[1,1,1],[1,0,1],[1,1,1]]
输出：9

```
 **示例 2：** 

```
输入：grid = [[1,1,0,0]]
输出：1

```
 

 **提示：** 
-  `1 <= grid.length <= 100` 
-  `1 <= grid[0].length <= 100` 
-  `grid[i][j]` 为 `0` 或 `1` 
 
**标签**
`数组` `动态规划` `矩阵` 


## 
```python

```
>
# 1140.石子游戏 II
[https://leetcode-cn.com/problems/stone-game-ii](https://leetcode-cn.com/problems/stone-game-ii) 
## 原题
爱丽丝和鲍勃继续他们的石子游戏。许多堆石子 **排成一行** ，每堆都有正整数颗石子 `piles[i]` 。游戏以谁手中的石子最多来决出胜负。

爱丽丝和鲍勃轮流进行，爱丽丝先开始。最初， `M = 1` 。

在每个玩家的回合中，该玩家可以拿走剩下的 **前** `X` 堆的所有石子，其中 `1 <= X <= 2M` 。然后，令 `M = max(M, X)` 。

游戏一直持续到所有石子都被拿走。

假设爱丽丝和鲍勃都发挥出最佳水平，返回爱丽丝可以得到的最大数量的石头。

 

 **示例 1：** 

```

输入：piles = [2,7,9,4,4]
输出：10
解释：如果一开始Alice取了一堆，Bob取了两堆，然后Alice再取两堆。爱丽丝可以得到2 + 4 + 4 = 10堆。如果Alice一开始拿走了两堆，那么Bob可以拿走剩下的三堆。在这种情况下，Alice得到2 + 7 = 9堆。返回10，因为它更大。

```
 **示例 2:** 

```

输入：piles = [1,2,3,4,5,100]
输出：104

```
 

 **提示：** 
-  `1 <= piles.length <= 100` 
- <meta charset="UTF-8" /> `1 <= piles[i] <= 10^4` 
 
**标签**
`数组` `数学` `动态规划` `博弈` 


## 
```python

```
>
# 1141.查询近30天活跃用户数
[https://leetcode-cn.com/problems/user-activity-for-the-past-30-days-i](https://leetcode-cn.com/problems/user-activity-for-the-past-30-days-i) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1142.过去30天的用户活动 II
[https://leetcode-cn.com/problems/user-activity-for-the-past-30-days-ii](https://leetcode-cn.com/problems/user-activity-for-the-past-30-days-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1143.最长公共子序列
[https://leetcode-cn.com/problems/longest-common-subsequence](https://leetcode-cn.com/problems/longest-common-subsequence) 
## 原题
给定两个字符串  `text1` 和  `text2` ，返回这两个字符串的最长 **公共子序列** 的长度。如果不存在 **公共子序列** ，返回 `0` 。

一个字符串的  **子序列** * * 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
- 例如， `"ace"` 是 `"abcde"` 的子序列，但 `"aec"` 不是 `"abcde"` 的子序列。
两个字符串的 **公共子序列** 是这两个字符串所共同拥有的子序列。

 

 **示例 1：** 

```

输入：text1 = "abcde", text2 = "ace" 
输出：3  
解释：最长公共子序列是 "ace" ，它的长度为 3 。

```
 **示例 2：** 

```

输入：text1 = "abc", text2 = "abc"
输出：3
解释：最长公共子序列是 "abc" ，它的长度为 3 。

```
 **示例 3：** 

```

输入：text1 = "abc", text2 = "def"
输出：0
解释：两个字符串没有公共子序列，返回 0 。

```
 

 **提示：** 
-  `1 <= text1.length, text2.length <= 1000` 
-  `text1` 和  `text2` 仅由小写英文字符组成。
 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1144.递减元素使数组呈锯齿状
[https://leetcode-cn.com/problems/decrease-elements-to-make-array-zigzag](https://leetcode-cn.com/problems/decrease-elements-to-make-array-zigzag) 
## 原题
给你一个整数数组 `nums` ，每次 **操作** 会从中选择一个元素并 **将该元素的值减少 1** 。

如果符合下列情况之一，则数组 `A` 就是 **锯齿数组** ：
- 每个偶数索引对应的元素都大于相邻的元素，即 `A[0] > A[1] < A[2] > A[3] < A[4] > ...` 
- 或者，每个奇数索引对应的元素都大于相邻的元素，即 `A[0] < A[1] > A[2] < A[3] > A[4] < ...` 
返回将数组 `nums` 转换为锯齿数组所需的最小操作次数。

 

 **示例 1：** 

```
输入：nums = [1,2,3]
输出：2
解释：我们可以把 2 递减到 0，或把 3 递减到 1。

```
 **示例 2：** 

```
输入：nums = [9,6,1,6,2]
输出：4

```
 

 **提示：** 
-  `1 <= nums.length <= 1000` 
-  `1 <= nums[i] <= 1000` 
 
**标签**
`贪心` `数组` 


## 
```python

```
>
# 1145.二叉树着色游戏
[https://leetcode-cn.com/problems/binary-tree-coloring-game](https://leetcode-cn.com/problems/binary-tree-coloring-game) 
## 原题
有两位极客玩家参与了一场「二叉树着色」的游戏。游戏中，给出二叉树的根节点 `root` ，树上总共有 `n` 个节点，且 `n` 为奇数，其中每个节点上的值从 `1` 到 `n` 各不相同。

 

游戏从「一号」玩家开始（「一号」玩家为红色，「二号」玩家为蓝色），最开始时，

「一号」玩家从 `[1, n]` 中取一个值 `x` （ `1 <= x <= n` ）；

「二号」玩家也从 `[1, n]` 中取一个值 `y` （ `1 <= y <= n` ）且 `y != x` 。

「一号」玩家给值为 `x` 的节点染上红色，而「二号」玩家给值为 `y` 的节点染上蓝色。

 

之后两位玩家轮流进行操作，每一回合，玩家选择一个他之前涂好颜色的节点，将所选节点一个 **未着色** 的邻节点（即左右子节点、或父节点）进行染色。

如果当前玩家无法找到这样的节点来染色时，他的回合就会被跳过。

若两个玩家都没有可以染色的节点时，游戏结束。着色节点最多的那位玩家获得胜利 ✌️。

 

现在，假设你是「二号」玩家，根据所给出的输入，假如存在一个 `y` 值可以确保你赢得这场游戏，则返回 `true` ；若无法获胜，就请返回 `false` 。

 

 **示例：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/08/04/1480-binary-tree-coloring-game.png" style="height: 186px; width: 300px;">** 

```
输入：root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
输出：True
解释：第二个玩家可以选择值为 2 的节点。

```
 

 **提示：** 
- 二叉树的根节点为 `root` ，树上由 `n` 个节点，节点上的值从 `1` 到 `n` 各不相同。
-  `n` 为奇数。
-  `1 <= x <= n <= 100` 
 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1146.快照数组
[https://leetcode-cn.com/problems/snapshot-array](https://leetcode-cn.com/problems/snapshot-array) 
## 原题
实现支持下列接口的「快照数组」- SnapshotArray：
-  `SnapshotArray(int length)` - 初始化一个与指定长度相等的 类数组 的数据结构。 **初始时，每个元素都等于** **0** 。
-  `void set(index, val)` - 会将指定索引 `index` 处的元素设置为 `val` 。
-  `int snap()` - 获取该数组的快照，并返回快照的编号 `snap_id` （快照号是调用 `snap()` 的总次数减去 `1` ）。
-  `int get(index, snap_id)` - 根据指定的 `snap_id` 选择快照，并返回该快照指定索引 `index` 的值。
 

 **示例：** 

```
输入：["SnapshotArray","set","snap","set","get"]
     [[3],[0,5],[],[0,6],[0,0]]
输出：[null,null,0,null,5]
解释：
SnapshotArray snapshotArr = new SnapshotArray(3); // 初始化一个长度为 3 的快照数组
snapshotArr.set(0,5);  // 令 array[0] = 5
snapshotArr.snap();  // 获取快照，返回 snap_id = 0
snapshotArr.set(0,6);
snapshotArr.get(0,0);  // 获取 snap_id = 0 的快照中 array[0] 的值，返回 5
```
 

 **提示：** 
-  `1 <= length <= 50000` 
- 题目最多进行 `50000` 次 `set` ， `snap` ，和 `get` 的调用 。
-  `0 <= index < length` 
-  `0 <= snap_id <` 我们调用 `snap()` 的总次数
-  `0 <= val <= 10^9` 
 
**标签**
`设计` `数组` `哈希表` `二分查找` 


## 
```python

```
>
# 1147.段式回文
[https://leetcode-cn.com/problems/longest-chunked-palindrome-decomposition](https://leetcode-cn.com/problems/longest-chunked-palindrome-decomposition) 
## 原题
你会得到一个字符串 `text` 。你应该把它分成 `k` 个子字符串 `(subtext1, subtext2，…， subtextk)` ，要求满足:
-  `subtext<sub>i</sub>` <sub> </sub>是非空字符串
- 所有子字符串的连接等于 `text` ( 即 `subtext<sub>1</sub> + subtext<sub>2</sub> + ... + subtext<sub>k</sub> == text` )
-  `subtext<sub>i</sub> == subtext<sub>k - i + 1</sub>` <sub> </sub>表示所有 <font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">i</span></span></font></font> 的有效值( 即 `1 <= i <= k` )
返回 `k` 可能最大值。

 

 **示例 1：** 

```

输入：text = "ghiabcdefhelloadamhelloabcdefghi"
输出：7
解释：我们可以把字符串拆分成 "(ghi)(abcdef)(hello)(adam)(hello)(abcdef)(ghi)"。

```
 **示例 2：** 

```

输入：text = "merchant"
输出：1
解释：我们可以把字符串拆分成 "(merchant)"。

```
 **示例 3：** 

```

输入：text = "antaprezatepzapreanta"
输出：11
解释：我们可以把字符串拆分成 "(a)(nt)(a)(pre)(za)(tpe)(za)(pre)(a)(nt)(a)"。

```
 **示例 4：** 

```

输入：text = "aaa"
输出：3
解释：我们可以把字符串拆分成 "(a)(a)(a)"。

```
 

 **提示：** 
-  `1 <= text.length <= 1000` 
-  `text` 仅由小写英文字符组成
 
**标签**
`贪心` `双指针` `字符串` `动态规划` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 1148.文章浏览 I
[https://leetcode-cn.com/problems/article-views-i](https://leetcode-cn.com/problems/article-views-i) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1149.文章浏览 II
[https://leetcode-cn.com/problems/article-views-ii](https://leetcode-cn.com/problems/article-views-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1150.检查一个数是否在数组中占绝大多数
[https://leetcode-cn.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array](https://leetcode-cn.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array) 
## 原题

 
**标签**
`数组` `二分查找` 


## 
```python

```
>
# 1151.最少交换次数来组合所有的 1
[https://leetcode-cn.com/problems/minimum-swaps-to-group-all-1s-together](https://leetcode-cn.com/problems/minimum-swaps-to-group-all-1s-together) 
## 原题

 
**标签**
`数组` `滑动窗口` 


## 
```python

```
>
# 1152.用户网站访问行为分析
[https://leetcode-cn.com/problems/analyze-user-website-visit-pattern](https://leetcode-cn.com/problems/analyze-user-website-visit-pattern) 
## 原题

 
**标签**
`数组` `哈希表` `排序` 


## 
```python

```
>
# 1153.字符串转化
[https://leetcode-cn.com/problems/string-transforms-into-another-string](https://leetcode-cn.com/problems/string-transforms-into-another-string) 
## 原题

 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1154.一年中的第几天
[https://leetcode-cn.com/problems/day-of-the-year](https://leetcode-cn.com/problems/day-of-the-year) 
## 原题
给你一个字符串 `date` ，按 `YYYY-MM-DD` 格式表示一个 <a href="https://baike.baidu.com/item/公元/17855" target="_blank">现行公元纪年法</a> 日期。返回该日期是当年的第几天。

 

 **示例 1：** 

```

输入：date = "2019-01-09"
输出：9
解释：给定日期是2019年的第九天。
```
 **示例 2：** 

```

输入：date = "2019-02-10"
输出：41

```
 

 **提示：** 
-  `date.length == 10` 
-  `date[4] == date[7] == '-'` ，其他的 `date[i]` 都是数字
-  `date` 表示的范围从 1900 年 1 月 1 日至 2019 年 12 月 31 日
 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 1155.掷骰子的N种方法
[https://leetcode-cn.com/problems/number-of-dice-rolls-with-target-sum](https://leetcode-cn.com/problems/number-of-dice-rolls-with-target-sum) 
## 原题
这里有 `n` 个一样的骰子，每个骰子上都有 `k` 个面，分别标号为 `1` 到 `k` 。

给定三个整数 `n` , `k` 和 `target` ，返回可能的方式(从总共 `k^n` 种方式中)滚动骰子的数量，使正面朝上的数字之和等于 `target` 。

答案可能很大，你需要对 `10^9 + 7` **取模** 。

 

 **示例 1：** 

```

输入：n = 1, k = 6, target = 3
输出：1
解释：你扔一个有6张脸的骰子。
得到3的和只有一种方法。

```
 **示例 2：** 

```

输入：n = 2, k = 6, target = 7
输出：6
解释：你扔两个骰子，每个骰子有6个面。
得到7的和有6种方法1+6 2+5 3+4 4+3 5+2 6+1。

```
 **示例 3：** 

```

输入：n = 30, k = 30, target = 500
输出：222616187
解释：返回的结果必须是对 10^9 + 7 取模。
```
 

 **提示：** 
-  `1 <= n, k <= 30` 
-  `1 <= target <= 1000` 
 
**标签**
`动态规划` 


## 
```python

```
>
# 1156.单字符重复子串的最大长度
[https://leetcode-cn.com/problems/swap-for-longest-repeated-character-substring](https://leetcode-cn.com/problems/swap-for-longest-repeated-character-substring) 
## 原题
如果字符串中的所有字符都相同，那么这个字符串是单字符重复的字符串。

给你一个字符串 `text` ，你只能交换其中两个字符一次或者什么都不做，然后得到一些单字符重复的子串。返回其中最长的子串的长度。

 

 **示例 1：** 

```
输入：text = "ababa"
输出：3

```
 **示例 2：** 

```
输入：text = "aaabaaa"
输出：6

```
 **示例 3：** 

```
输入：text = "aaabbaaa"
输出：4

```
 **示例 4：** 

```
输入：text = "aaaaa"
输出：5

```
 **示例 5：** 

```
输入：text = "abcdef"
输出：1

```
 

 **提示：** 
-  `1 <= text.length <= 20000` 
-  `text` 仅由小写英文字母组成。
 
**标签**
`字符串` `滑动窗口` 


## 
```python

```
>
# 1157.子数组中占绝大多数的元素
[https://leetcode-cn.com/problems/online-majority-element-in-subarray](https://leetcode-cn.com/problems/online-majority-element-in-subarray) 
## 原题
设计一个数据结构，有效地找到给定子数组的 **多数元素** 。

子数组的 **多数元素** 是在子数组中出现 `threshold` 次数或次数以上的元素。

实现 `MajorityChecker` 类:
-  `MajorityChecker(int[] arr)` 会用给定的数组 `arr` 对 `MajorityChecker` 初始化。
-  `int query(int left, int right, int threshold)` 返回子数组中的元素 `arr[left...right]` 至少出现 `threshold` 次数，如果不存在这样的元素则返回 `-1` 。
 

 **示例 1：** 

```

输入:
["MajorityChecker", "query", "query", "query"]
[[[1, 1, 2, 2, 1, 1]], [0, 5, 4], [0, 3, 3], [2, 3, 2]]
输出：
[null, 1, -1, 2]

解释：
MajorityChecker majorityChecker = new MajorityChecker([1,1,2,2,1,1]);
majorityChecker.query(0,5,4); // 返回 1
majorityChecker.query(0,3,3); // 返回 -1
majorityChecker.query(2,3,2); // 返回 2

```
 

 **提示：** 
-  `1 <= arr.length <= 2 * 10^4` 
-  `1 <= arr[i] <= 2 * 10^4` 
-  `0 <= left <= right < arr.length` 
-  `threshold <= right - left + 1` 
-  `2 * threshold > right - left + 1` 
- 调用 `query` 的次数最多为 `10^4` 
 
**标签**
`设计` `树状数组` `线段树` `数组` `二分查找` 


## 
```python

```
>
# 1158.市场分析 I
[https://leetcode-cn.com/problems/market-analysis-i](https://leetcode-cn.com/problems/market-analysis-i) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1159.市场分析 II
[https://leetcode-cn.com/problems/market-analysis-ii](https://leetcode-cn.com/problems/market-analysis-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1160.拼写单词
[https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters](https://leetcode-cn.com/problems/find-words-that-can-be-formed-by-characters) 
## 原题
给你一份『词汇表』（字符串数组） `words` 和一张『字母表』（字符串） `chars` 。

假如你可以用 `chars` 中的『字母』（字符）拼写出 `words` 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。

注意：每次拼写（指拼写词汇表中的一个单词）时， `chars` 中的每个字母都只能用一次。

返回词汇表 `words` 中你掌握的所有单词的 **长度之和** 。

 

 **示例 1：** 

```
输入：words = ["cat","bt","hat","tree"], chars = "atach"
输出：6
解释： 
可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。

```
 **示例 2：** 

```
输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
输出：10
解释：
可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。

```
 

 **提示：** 
-  `1 <= words.length <= 1000` 
-  `1 <= words[i].length, chars.length <= 100` 
- 所有字符串中都仅包含小写英文字母
 
**标签**
`数组` `哈希表` `字符串` 


## 
```python

```
>
# 1161.最大层内元素和
[https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree](https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree) 
## 原题
给你一个二叉树的根节点 `root` 。设根节点位于二叉树的第 `1` 层，而根节点的子节点位于第 `2` 层，依此类推。

请返回层内元素之和 **最大** 的那几层（可能只有一层）的层号，并返回其中 **最小** 的那个。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/08/17/capture.jpeg" style="height: 175px; width: 200px;" />** 

```

输入：root = [1,7,0,7,-8,null,null]
输出：2
解释：
第 1 层各元素之和为 1，
第 2 层各元素之和为 7 + 0 = 7，
第 3 层各元素之和为 7 + -8 = -1，
所以我们返回第 2 层的层号，它的层内元素之和最大。

```
 **示例 2：** 

```

输入：root = [989,null,10250,98693,-89388,null,null,null,-32127]
输出：2

```
 

 **提示：** 
- 树中的节点数在<meta charset="UTF-8" /> `[1, 10^4]` 范围内<meta charset="UTF-8" />
-  `-10^5 <= Node.val <= 10^5` 
 
**标签**
`树` `深度优先搜索` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 1162.地图分析
[https://leetcode-cn.com/problems/as-far-from-land-as-possible](https://leetcode-cn.com/problems/as-far-from-land-as-possible) 
## 原题
你现在手里有一份大小为<meta charset="UTF-8" /> `n x n` 的 网格 `grid` ，上面的每个 单元格 都用 `0` 和 `1` 标记好了。其中 `0` 代表海洋， `1` 代表陆地，请你找出一个海洋单元格，这个海洋单元格到离它最近的陆地单元格的距离是最大的。如果网格上只有陆地或者海洋，请返回 `-1` 。

我们这里说的距离是「曼哈顿距离」（ Manhattan Distance）： `(x0, y0)` 和 `(x1, y1)` 这两个单元格之间的距离是 `|x0 - x1| + |y0 - y1|` 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/08/17/1336_ex1.jpeg" />** 

```

输入：grid = [[1,0,1],[0,0,0],[1,0,1]]
输出：2
解释： 
海洋单元格 (1, 1) 和所有陆地单元格之间的距离都达到最大，最大距离为 2。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/08/17/1336_ex2.jpeg" />** 

```

输入：grid = [[1,0,0],[0,0,0],[0,0,0]]
输出：4
解释： 
海洋单元格 (2, 2) 和所有陆地单元格之间的距离都达到最大，最大距离为 4。

```
 

 **提示：** 

<meta charset="UTF-8" />
-  `n == grid.length` 
-  `n == grid[i].length` 
-  `1 <= n <= 100` 
-  `grid[i][j]` 不是 `0` 就是 `1` 
 
**标签**
`广度优先搜索` `数组` `动态规划` `矩阵` 


## 
```python

```
>
# 1163.按字典序排在最后的子串
[https://leetcode-cn.com/problems/last-substring-in-lexicographical-order](https://leetcode-cn.com/problems/last-substring-in-lexicographical-order) 
## 原题
给你一个字符串 `s` ，找出它的所有子串并按字典序排列，返回排在最后的那个子串。

 

 **示例 1：** 

```

输入：s = "abab"
输出："bab"
解释：我们可以找出 7 个子串 ["a", "ab", "aba", "abab", "b", "ba", "bab"]。按字典序排在最后的子串是 "bab"。

```
 **示例 2：** 

```

输入：s = "leetcode"
输出："tcode"

```
 

 **提示：** 
-  `1 <= s.length <= 4 * 10^5` 
-  `s` 仅含有小写英文字符。
 
**标签**
`双指针` `字符串` 


## 
```python

```
>
# 1164.指定日期的产品价格
[https://leetcode-cn.com/problems/product-price-at-a-given-date](https://leetcode-cn.com/problems/product-price-at-a-given-date) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1165.单行键盘
[https://leetcode-cn.com/problems/single-row-keyboard](https://leetcode-cn.com/problems/single-row-keyboard) 
## 原题

 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1166.设计文件系统
[https://leetcode-cn.com/problems/design-file-system](https://leetcode-cn.com/problems/design-file-system) 
## 原题

 
**标签**
`设计` `字典树` `哈希表` `字符串` 


## 
```python

```
>
# 1167.连接棒材的最低费用
[https://leetcode-cn.com/problems/minimum-cost-to-connect-sticks](https://leetcode-cn.com/problems/minimum-cost-to-connect-sticks) 
## 原题

 
**标签**
`贪心` `数组` `堆（优先队列）` 


## 
```python

```
>
# 1168.水资源分配优化
[https://leetcode-cn.com/problems/optimize-water-distribution-in-a-village](https://leetcode-cn.com/problems/optimize-water-distribution-in-a-village) 
## 原题

 
**标签**
`并查集` `图` `最小生成树` 


## 
```python

```
>
# 1169.查询无效交易
[https://leetcode-cn.com/problems/invalid-transactions](https://leetcode-cn.com/problems/invalid-transactions) 
## 原题
如果出现下述两种情况，交易 **可能无效** ：
- 交易金额超过<meta charset="UTF-8" /> `$1000` 
- 或者，它和 **另一个城市** 中 **同名** 的另一笔交易相隔不超过 `60` 分钟（包含 60 分钟整）
给定字符串数组交易清单<meta charset="UTF-8" /> `transaction` 。每个交易字符串 `transactions[i]` 由一些用逗号分隔的值组成，这些值分别表示交易的名称，时间（以分钟计），金额以及城市。

返回 `transactions` ，返回可能无效的交易列表。你可以按 **任何顺序** 返回答案。

 

 **示例 1：** 

```

输入：transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
输出：["alice,20,800,mtv","alice,50,100,beijing"]
解释：第一笔交易是无效的，因为第二笔交易和它间隔不超过 60 分钟、名称相同且发生在不同的城市。同样，第二笔交易也是无效的。
```
 **示例 2：** 

```

输入：transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
输出：["alice,50,1200,mtv"]

```
 **示例 3：** 

```

输入：transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
输出：["bob,50,1200,mtv"]

```
 

 **提示：** 
-  `transactions.length <= 1000` 
- 每笔交易 `transactions[i]` 按 `"{name},{time},{amount},{city}"` 的格式进行记录
- 每个交易名称 `{name}` 和城市 `{city}` 都由小写英文字母组成，长度在 `1` 到 `10` 之间
- 每个交易时间 `{time}` 由一些数字组成，表示一个 `0` 到 `1000` 之间的整数
- 每笔交易金额 `{amount}` 由一些数字组成，表示一个 `0` 到 `2000` 之间的整数
 
**标签**
`数组` `哈希表` `字符串` `排序` 


## 
```python

```
>
# 1170.比较字符串最小字母出现频次
[https://leetcode-cn.com/problems/compare-strings-by-frequency-of-the-smallest-character](https://leetcode-cn.com/problems/compare-strings-by-frequency-of-the-smallest-character) 
## 原题
定义一个函数  `f(s)` ，统计  `s`  中 **（按字典序比较）最小字母的出现频次** ，其中 `s`  是一个非空字符串。

例如，若  `s = "dcce"` ，那么  `f(s) = 2` ，因为字典序最小字母是  `"c"` ，它出现了 2 次。

现在，给你两个字符串数组待查表  `queries`  和词汇表  `words` 。对于每次查询  `queries[i]` ，需统计 `words` 中满足  `f(queries[i])`  < `f(W)`  的 **词的数目** ， `W` 表示词汇表  `words`  中的每个词。

请你返回一个整数数组  `answer`  作为答案，其中每个  `answer[i]`  是第 `i` 次查询的结果。

 

 **示例 1：** 

```

输入：queries = ["cbd"], words = ["zaaaz"]
输出：[1]
解释：查询 f("cbd") = 1，而 f("zaaaz") = 3 所以 f("cbd") < f("zaaaz")。

```
 **示例 2：** 

```

输入：queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
输出：[1,2]
解释：第一个查询 f("bbb")  f("cc")。

```
 

 **提示：** 
-  `1 <= queries.length <= 2000` 
-  `1 <= words.length <= 2000` 
-  `1 <= queries[i].length, words[i].length <= 10` 
-  `queries[i][j]` 、 `words[i][j]` 都由小写英文字母组成
 
**标签**
`数组` `哈希表` `字符串` `二分查找` `排序` 


## 
```python

```
>
# 1171.从链表中删去总和值为零的连续节点
[https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list](https://leetcode-cn.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list) 
## 原题
给你一个链表的头节点 `head` ，请你编写代码，反复删去链表中由 **总和** 值为 `0` 的连续节点组成的序列，直到不存在这样的序列为止。

删除完毕后，请你返回最终结果链表的头节点。

 

你可以返回任何满足题目要求的答案。

（注意，下面示例中的所有序列，都是对 `ListNode` 对象序列化的表示。）

 **示例 1：** 

```
输入：head = [1,2,-3,3,1]
输出：[3,1]
提示：答案 [1,2,1] 也是正确的。

```
 **示例 2：** 

```
输入：head = [1,2,3,-3,4]
输出：[1,2,4]

```
 **示例 3：** 

```
输入：head = [1,2,3,-3,-2]
输出：[1]

```
 

 **提示：** 
- 给你的链表中可能有 `1` 到 `1000` 个节点。
- 对于链表中的每个节点，节点的值： `-1000 <= node.val <= 1000` .
 
**标签**
`哈希表` `链表` 


## 
```python

```
>
# 1172.餐盘栈
[https://leetcode-cn.com/problems/dinner-plate-stacks](https://leetcode-cn.com/problems/dinner-plate-stacks) 
## 原题
我们把无限数量 &infin; 的栈排成一行，按从左到右的次序从 0 开始编号。每个栈的的最大容量 `capacity` 都相同。

实现一个叫「餐盘」的类 `DinnerPlates` ：
-  `DinnerPlates(int capacity)` - 给出栈的最大容量 `capacity` 。
-  `void push(int val)` - 将给出的正整数 `val` 推入 **从左往右第一个** 没有满的栈。
-  `int pop()` - 返回 **从右往左第一个** 非空栈顶部的值，并将其从栈中删除；如果所有的栈都是空的，请返回 `-1` 。
-  `int popAtStack(int index)` - 返回编号 `index` 的栈顶部的值，并将其从栈中删除；如果编号 `index` 的栈是空的，请返回 `-1` 。
 

 **示例：** 

```
输入： 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
输出：
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

解释：
DinnerPlates D = DinnerPlates(2);  // 初始化，栈最大容量 capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // 栈的现状为：    2  4
                                    1  3  5
                                    ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 2。栈的现状为：      4
                                          1  3  5
                                          ﹈ ﹈ ﹈
D.push(20);        // 栈的现状为：  20  4
                                   1  3  5
                                   ﹈ ﹈ ﹈
D.push(21);        // 栈的现状为：  20  4 21
                                   1  3  5
                                   ﹈ ﹈ ﹈
D.popAtStack(0);   // 返回 20。栈的现状为：       4 21
                                            1  3  5
                                            ﹈ ﹈ ﹈
D.popAtStack(2);   // 返回 21。栈的现状为：       4
                                            1  3  5
                                            ﹈ ﹈ ﹈ 
D.pop()            // 返回 5。栈的现状为：        4
                                            1  3 
                                            ﹈ ﹈  
D.pop()            // 返回 4。栈的现状为：    1  3 
                                           ﹈ ﹈   
D.pop()            // 返回 3。栈的现状为：    1 
                                           ﹈   
D.pop()            // 返回 1。现在没有栈。
D.pop()            // 返回 -1。仍然没有栈。

```
 

 **提示：** 
-  `1 <= capacity <= 20000` 
-  `1 <= val <= 20000` 
-  `0 <= index <= 100000` 
- 最多会对 `push` ， `pop` ，和 `popAtStack` 进行 `200000` 次调用。
 
**标签**
`栈` `设计` `哈希表` `堆（优先队列）` 


## 
```python

```
>
# 1173.即时食物配送 I
[https://leetcode-cn.com/problems/immediate-food-delivery-i](https://leetcode-cn.com/problems/immediate-food-delivery-i) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1174.即时食物配送 II
[https://leetcode-cn.com/problems/immediate-food-delivery-ii](https://leetcode-cn.com/problems/immediate-food-delivery-ii) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1175.质数排列
[https://leetcode-cn.com/problems/prime-arrangements](https://leetcode-cn.com/problems/prime-arrangements) 
## 原题
请你帮忙给从 `1` 到 `n` 的数设计排列方案，使得所有的「质数」都应该被放在「质数索引」（索引从 1 开始）上；你需要返回可能的方案总数。

让我们一起来回顾一下「质数」：质数一定是大于 1 的，并且不能用两个小于它的正整数的乘积来表示。

由于答案可能会很大，所以请你返回答案 **模 mod `10^9 + 7` ** 之后的结果即可。

 

 **示例 1：** 

```
输入：n = 5
输出：12
解释：举个例子，[1,2,5,4,3] 是一个有效的排列，但 [5,2,3,4,1] 不是，因为在第二种情况里质数 5 被错误地放在索引为 1 的位置上。

```
 **示例 2：** 

```
输入：n = 100
输出：682289015

```
 

 **提示：** 
-  `1 <= n <= 100` 
 
**标签**
`数学` 


## 
```python

```
>
# 1176.健身计划评估
[https://leetcode-cn.com/problems/diet-plan-performance](https://leetcode-cn.com/problems/diet-plan-performance) 
## 原题

 
**标签**
`数组` `滑动窗口` 


## 
```python

```
>
# 1177.构建回文串检测
[https://leetcode-cn.com/problems/can-make-palindrome-from-substring](https://leetcode-cn.com/problems/can-make-palindrome-from-substring) 
## 原题
给你一个字符串 `s` ，请你对 `s` 的子串进行检测。

每次检测，待检子串都可以表示为 `queries[i] = [left, right, k]` 。我们可以 **重新排列** 子串 `s[left], ..., s[right]` ，并从中选择 **最多** `k` 项替换成任何小写英文字母。 

如果在上述检测过程中，子串可以变成回文形式的字符串，那么检测结果为 `true` ，否则结果为 `false` 。

返回答案数组 `answer[]` ，其中 `answer[i]` 是第 `i` 个待检子串 `queries[i]` 的检测结果。

注意：在替换时，子串中的每个字母都必须作为 **独立的** 项进行计数，也就是说，如果 `s[left..right] = "aaa"` 且 `k = 2` ，我们只能替换其中的两个字母。（另外，任何检测都不会修改原始字符串 `s` ，可以认为每次检测都是独立的）

 

 **示例：** 

```
输入：s = "abcda", queries = [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
输出：[true,false,false,true,true]
解释：
queries[0] : 子串 = "d"，回文。
queries[1] : 子串 = "bc"，不是回文。
queries[2] : 子串 = "abcd"，只替换 1 个字符是变不成回文串的。
queries[3] : 子串 = "abcd"，可以变成回文的 "abba"。 也可以变成 "baab"，先重新排序变成 "bacd"，然后把 "cd" 替换为 "ab"。
queries[4] : 子串 = "abcda"，可以变成回文的 "abcba"。

```
 

 **提示：** 
-  `1 <= s.length, queries.length <= 10^5` 
-  `0 <= queries[i][0] <= queries[i][1] < s.length` 
-  `0 <= queries[i][2] <= s.length` 
-  `s` 中只有小写英文字母
 
**标签**
`位运算` `哈希表` `字符串` `前缀和` 


## 
```python

```
>
# 1178.猜字谜
[https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle](https://leetcode-cn.com/problems/number-of-valid-words-for-each-puzzle) 
## 原题
外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。

字谜的迷面  `puzzle` 按字符串形式给出，如果一个单词  `word`  符合下面两个条件，那么它就可以算作谜底：
- 单词  `word`  中包含谜面  `puzzle`  的第一个字母。
- 单词  `word`  中的每一个字母都可以在谜面  `puzzle`  中找到。<br />
	例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）都不能作为谜底。
返回一个答案数组  `answer` ，数组中的每个元素  `answer[i]`  是在给出的单词列表 `words` 中可以作为字谜迷面  `puzzles[i]`  所对应的谜底的单词数目。

 

 **示例：** 

```

输入：
words = ["aaaa","asas","able","ability","actt","actor","access"], 
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]
输出：[1,1,3,2,4,0]
解释：
1 个单词可以作为 "aboveyz" 的谜底 : "aaaa" 
1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"
3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"
2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"
4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"
没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。

```
 

 **提示：** 
-  `1 <= words.length <= 10^5` 
-  `4 <= words[i].length <= 50` 
-  `1 <= puzzles.length <= 10^4` 
-  `puzzles[i].length == 7` 
-  `words[i][j]` , `puzzles[i][j]`  都是小写英文字母。
- 每个  `puzzles[i]`  所包含的字符都不重复。
 
**标签**
`位运算` `字典树` `数组` `哈希表` `字符串` 


## 
```python

```
>
# 1179.重新格式化部门表
[https://leetcode-cn.com/problems/reformat-department-table](https://leetcode-cn.com/problems/reformat-department-table) 
## 原题
部门表 `Department` ：

```

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| revenue       | int     |
| month         | varchar |
+---------------+---------+
(id, month) 是表的联合主键。
这个表格有关于每个部门每月收入的信息。
月份（month）可以取下列值 ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]。

```
 

编写一个 SQL 查询来重新格式化表，使得新的表中有一个部门 id 列和一些对应 **每个月** 的收入（revenue）列。

查询结果格式如下面的示例所示：

```

Department 表：
+------+---------+-------+
| id   | revenue | month |
+------+---------+-------+
| 1    | 8000    | Jan   |
| 2    | 9000    | Jan   |
| 3    | 10000   | Feb   |
| 1    | 7000    | Feb   |
| 1    | 6000    | Mar   |
+------+---------+-------+

查询得到的结果表：
+------+-------------+-------------+-------------+-----+-------------+
| id   | Jan_Revenue | Feb_Revenue | Mar_Revenue | ... | Dec_Revenue |
+------+-------------+-------------+-------------+-----+-------------+
| 1    | 8000        | 7000        | 6000        | ... | null        |
| 2    | 9000        | null        | null        | ... | null        |
| 3    | null        | 10000       | null        | ... | null        |
+------+-------------+-------------+-------------+-----+-------------+

注意，结果表有 13 列 (1个部门 id 列 + 12个月份的收入列)。

```
 
**标签**
`数据库` 


## 
```python

```
>
# 1180.统计只含单一字母的子串
[https://leetcode-cn.com/problems/count-substrings-with-only-one-distinct-letter](https://leetcode-cn.com/problems/count-substrings-with-only-one-distinct-letter) 
## 原题

 
**标签**
`数学` `字符串` 


## 
```python

```
>
# 1181.前后拼接
[https://leetcode-cn.com/problems/before-and-after-puzzle](https://leetcode-cn.com/problems/before-and-after-puzzle) 
## 原题

 
**标签**
`数组` `哈希表` `字符串` `排序` 


## 
```python

```
>
# 1182.与目标颜色间的最短距离
[https://leetcode-cn.com/problems/shortest-distance-to-target-color](https://leetcode-cn.com/problems/shortest-distance-to-target-color) 
## 原题

 
**标签**
`数组` `二分查找` `动态规划` 


## 
```python

```
>
# 1183.矩阵中 1 的最大数量
[https://leetcode-cn.com/problems/maximum-number-of-ones](https://leetcode-cn.com/problems/maximum-number-of-ones) 
## 原题

 
**标签**
`贪心` `堆（优先队列）` 


## 
```python

```
>
# 1184.公交站间的距离
[https://leetcode-cn.com/problems/distance-between-bus-stops](https://leetcode-cn.com/problems/distance-between-bus-stops) 
## 原题
环形公交路线上有 `n` 个站，按次序从 `0` 到 `n - 1` 进行编号。我们已知每一对相邻公交站之间的距离， `distance[i]` 表示编号为 `i` 的车站和编号为 `(i + 1) % n` 的车站之间的距离。

环线上的公交车都可以按顺时针和逆时针的方向行驶。

返回乘客从出发点 `start` 到目的地 `destination` 之间的最短距离。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1.jpg" style="height: 240px; width: 388px;">

```
输入：distance = [1,2,3,4], start = 0, destination = 1
输出：1
解释：公交站 0 和 1 之间的距离是 1 或 9，最小值是 1。
```
 

 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1-1.jpg" style="height: 240px; width: 388px;">

```
输入：distance = [1,2,3,4], start = 0, destination = 2
输出：3
解释：公交站 0 和 2 之间的距离是 3 或 7，最小值是 3。

```
 

 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/08/untitled-diagram-1-2.jpg" style="height: 240px; width: 388px;">

```
输入：distance = [1,2,3,4], start = 0, destination = 3
输出：4
解释：公交站 0 和 3 之间的距离是 6 或 4，最小值是 4。

```
 

 **提示：** 
-  `1 <= n <= 10^4` 
-  `distance.length == n` 
-  `0 <= start, destination < n` 
-  `0 <= distance[i] <= 10^4` 
 
**标签**
`数组` 


## 
```python

```
>
# 1185.一周中的第几天
[https://leetcode-cn.com/problems/day-of-the-week](https://leetcode-cn.com/problems/day-of-the-week) 
## 原题
给你一个日期，请你设计一个算法来判断它是对应一周中的哪一天。

输入为三个整数： `day` 、 `month` 和 `year` ，分别表示日、月、年。

您返回的结果必须是这几个值中的一个 `{"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}` 。

 

 **示例 1：** 

```
输入：day = 31, month = 8, year = 2019
输出："Saturday"

```
 **示例 2：** 

```
输入：day = 18, month = 7, year = 1999
输出："Sunday"

```
 **示例 3：** 

```
输入：day = 15, month = 8, year = 1993
输出："Sunday"

```
 

 **提示：** 
- 给出的日期一定是在 `1971` 到 `2100` 年之间的有效日期。
 
**标签**
`数学` 


## 
```python

```
>
# 1186.删除一次得到子数组最大和
[https://leetcode-cn.com/problems/maximum-subarray-sum-with-one-deletion](https://leetcode-cn.com/problems/maximum-subarray-sum-with-one-deletion) 
## 原题
给你一个整数数组，返回它的某个 **非空** 子数组（连续元素）在执行一次可选的删除操作后，所能得到的最大元素总和。换句话说，你可以从原数组中选出一个子数组，并可以决定要不要从中删除一个元素（只能删一次哦），（删除后）子数组中至少应当有一个元素，然后该子数组（剩下）的元素总和是所有子数组之中最大的。

注意，删除一个元素后，子数组 **不能为空** 。

 

 **示例 1：** 

```

输入：arr = [1,-2,0,3]
输出：4
解释：我们可以选出 [1, -2, 0, 3]，然后删掉 -2，这样得到 [1, 0, 3]，和最大。
```
 **示例 2：** 

```

输入：arr = [1,-2,-2,3]
输出：3
解释：我们直接选出 [3]，这就是最大和。

```
 **示例 3：** 

```

输入：arr = [-1,-1,-1,-1]
输出：-1
解释：最后得到的子数组不能为空，所以我们不能选择 [-1] 并从中删去 -1 来得到 0。
     我们应该直接选择 [-1]，或者选择 [-1, -1] 再从中删去一个 -1。

```
 

 **提示：** 
<meta charset="UTF-8" />
-  `1 <= arr.length <= 10^5` 
-  `-10^4 <= arr[i] <= 10^4` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1187.使数组严格递增
[https://leetcode-cn.com/problems/make-array-strictly-increasing](https://leetcode-cn.com/problems/make-array-strictly-increasing) 
## 原题
给你两个整数数组 `arr1` 和 `arr2` ，返回使 `arr1` 严格递增所需要的最小「操作」数（可能为 0）。

每一步「操作」中，你可以分别从 `arr1` 和 `arr2` 中各选出一个索引，分别为 `i` 和 `j` ， `0 <= i < arr1.length` 和 `0 <= j < arr2.length` ，然后进行赋值运算 `arr1[i] = arr2[j]` 。

如果无法让 `arr1` 严格递增，请返回 `-1` 。

 

 **示例 1：** 

```
输入：arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
输出：1
解释：用 2 来替换 5，之后 arr1 = [1, 2, 3, 6, 7]。

```
 **示例 2：** 

```
输入：arr1 = [1,5,3,6,7], arr2 = [4,3,1]
输出：2
解释：用 3 来替换 5，然后用 4 来替换 3，得到 arr1 = [1, 3, 4, 6, 7]。

```
 **示例 3：** 

```
输入：arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
输出：-1
解释：无法使 arr1 严格递增。
```
 

 **提示：** 
-  `1 <= arr1.length, arr2.length <= 2000` 
-  `0 <= arr1[i], arr2[i] <= 10^9` 
 

 
**标签**
`数组` `二分查找` `动态规划` 


## 
```python

```
>
# 1188.设计有限阻塞队列
[https://leetcode-cn.com/problems/design-bounded-blocking-queue](https://leetcode-cn.com/problems/design-bounded-blocking-queue) 
## 原题

 
**标签**
`多线程` 


## 
```python

```
>
# 1189.“气球” 的最大数量
[https://leetcode-cn.com/problems/maximum-number-of-balloons](https://leetcode-cn.com/problems/maximum-number-of-balloons) 
## 原题
给你一个字符串 `text` ，你需要使用 `text` 中的字母来拼凑尽可能多的单词 **"balloon"（气球）** 。

字符串 `text` 中的每个字母最多只能被使用一次。请你返回最多可以拼凑出多少个单词 **"balloon"** 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/14/1536_ex1_upd.jpeg" style="height: 35px; width: 154px;">** 

```
输入：text = "nlaebolko"
输出：1

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/14/1536_ex2_upd.jpeg" style="height: 35px; width: 233px;">** 

```
输入：text = "loonbalxballpoon"
输出：2

```
 **示例 3：** 

```
输入：text = "leetcode"
输出：0

```
 

 **提示：** 
-  `1 <= text.length <= 10^4` 
-  `text` 全部由小写英文字母组成
 
**标签**
`哈希表` `字符串` `计数` 


## 
```python

```
>
# 1190.反转每对括号间的子串
[https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses](https://leetcode-cn.com/problems/reverse-substrings-between-each-pair-of-parentheses) 
## 原题
给出一个字符串  `s` （仅含有小写英文字母和括号）。

请你按照从括号内到外的顺序，逐层反转每对匹配括号中的字符串，并返回最终的结果。

注意，您的结果中 **不应** 包含任何括号。

 

 **示例 1：** 

```

输入：s = "(abcd)"
输出："dcba"

```
 **示例 2：** 

```

输入：s = "(u(love)i)"
输出："iloveu"
解释：先反转子字符串 "love" ，然后反转整个字符串。
```
 **示例 3：** 

```

输入：s = "(ed(et(oc))el)"
输出："leetcode"
解释：先反转子字符串 "oc" ，接着反转 "etco" ，然后反转整个字符串。
```
 **示例 4：** 

```

输入：s = "a(bcdefghijkl(mno)p)q"
输出："apmnolkjihgfedcbq"

```
 

 **提示：** 
-  `0 <= s.length <= 2000` 
-  `s` 中只有小写英文字母和括号
- 题目测试用例确保所有括号都是成对出现的
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 1191.K 次串联后最大子数组之和
[https://leetcode-cn.com/problems/k-concatenation-maximum-sum](https://leetcode-cn.com/problems/k-concatenation-maximum-sum) 
## 原题
给定一个整数数组 `arr` 和一个整数 `k` ，通过重复 `k` 次来修改数组。

例如，如果 `arr = [1, 2]` ，<meta charset="UTF-8" /> `k = 3` ，那么修改后的数组将是 `[1, 2, 1, 2, 1, 2]` 。

返回修改后的数组中的最大的子数组之和。注意，子数组长度可以是 `0` ，在这种情况下它的总和也是 `0` 。

由于 **结果可能会很大** ，需要返回的<meta charset="UTF-8" /> `10^9 + 7` 的 **模** 。

 

 **示例 1：** 

```

输入：arr = [1,2], k = 3
输出：9

```
 **示例 2：** 

```

输入：arr = [1,-2,1], k = 5
输出：2

```
 **示例 3：** 

```

输入：arr = [-1,-2], k = 7
输出：0

```
 

 **提示：** 
<meta charset="UTF-8" />
-  `1 <= arr.length <= 10^5` 
-  `1 <= k <= 10^5` 
-  `-10^4 <= arr[i] <= 10^4` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1192.查找集群内的「关键连接」
[https://leetcode-cn.com/problems/critical-connections-in-a-network](https://leetcode-cn.com/problems/critical-connections-in-a-network) 
## 原题
力扣数据中心有 `n` 台服务器，分别按从 `0` 到 `n-1` 的方式进行了编号。它们之间以「服务器到服务器」点对点的形式相互连接组成了一个内部集群，其中连接 `connections` 是无向的。从形式上讲， `connections[i] = [a, b]` 表示服务器 `a` 和 `b` 之间形成连接。任何服务器都可以直接或者间接地通过网络到达任何其他服务器。

 *「关键连接」* 是在该集群中的重要连接，也就是说，假如我们将它移除，便会导致某些服务器无法访问其他服务器。

请你以任意顺序返回该集群内的所有 「关键连接」。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/original_images/critical-connections-in-a-network.png" style="height: 205px; width: 200px;" />** 

```

输入：n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
输出：[[1,3]]
解释：[[3,1]] 也是正确的。
```
 **示例 2:** 

```

输入：n = 2, connections = [[0,1]]
输出：[[0,1]]

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `n-1 <= connections.length <= 10^5` 
-  `connections[i][0] != connections[i][1]` 
- 不存在重复的连接
 
**标签**
`深度优先搜索` `图` `双连通分量` 


## 
```python

```
>
# 1193.每月交易 I
[https://leetcode-cn.com/problems/monthly-transactions-i](https://leetcode-cn.com/problems/monthly-transactions-i) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1194.锦标赛优胜者
[https://leetcode-cn.com/problems/tournament-winners](https://leetcode-cn.com/problems/tournament-winners) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1195.交替打印字符串
[https://leetcode-cn.com/problems/fizz-buzz-multithreaded](https://leetcode-cn.com/problems/fizz-buzz-multithreaded) 
## 原题
编写一个可以从 1 到 n 输出代表这个数字的字符串的程序，但是：
- 如果这个数字可以被 3 整除，输出 "fizz"。
- 如果这个数字可以被 5 整除，输出 "buzz"。
- 如果这个数字可以同时被 3 和 5 整除，输出 "fizzbuzz"。
例如，当  `n = 15` ，输出：  `1, 2, fizz, 4, buzz, fizz, 7, 8, fizz, buzz, 11, fizz, 13, 14, fizzbuzz` 。

假设有这么一个类：

```

class FizzBuzz {
  public FizzBuzz(int n) { ... }               // constructor
  public void fizz(printFizz) { ... }          // only output "fizz"
  public void buzz(printBuzz) { ... }          // only output "buzz"
  public void fizzbuzz(printFizzBuzz) { ... }  // only output "fizzbuzz"
  public void number(printNumber) { ... }      // only output the numbers
}
```
请你实现一个有四个线程的多线程版   `FizzBuzz` ， 同一个  `FizzBuzz`  实例会被如下四个线程使用：
- 线程A将调用  `fizz()`  来判断是否能被 3 整除，如果可以，则输出  `fizz` 。
- 线程B将调用  `buzz()`  来判断是否能被 5 整除，如果可以，则输出  `buzz` 。
- 线程C将调用  `fizzbuzz()`  来判断是否同时能被 3 和 5 整除，如果可以，则输出  `fizzbuzz` 。
- 线程D将调用  `number()`  来实现输出既不能被 3 整除也不能被 5 整除的数字。
 

 **提示：** 
- 本题已经提供了打印字符串的相关方法，如 `printFizz()` 等，具体方法名请参考答题模板中的注释部分。
 

 
**标签**
`多线程` 


## 
```python

```
>
# 1196.最多可以买到的苹果数量
[https://leetcode-cn.com/problems/how-many-apples-can-you-put-into-the-basket](https://leetcode-cn.com/problems/how-many-apples-can-you-put-into-the-basket) 
## 原题

 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1197.进击的骑士
[https://leetcode-cn.com/problems/minimum-knight-moves](https://leetcode-cn.com/problems/minimum-knight-moves) 
## 原题

 
**标签**
`广度优先搜索` 


## 
```python

```
>
# 1198.找出所有行中最小公共元素
[https://leetcode-cn.com/problems/find-smallest-common-element-in-all-rows](https://leetcode-cn.com/problems/find-smallest-common-element-in-all-rows) 
## 原题

 
**标签**
`数组` `哈希表` `二分查找` `计数` `矩阵` 


## 
```python

```
>
# 1199.建造街区的最短时间
[https://leetcode-cn.com/problems/minimum-time-to-build-blocks](https://leetcode-cn.com/problems/minimum-time-to-build-blocks) 
## 原题

 
**标签**
`贪心` `数学` `堆（优先队列）` 


## 
```python

```
>
# 1200.最小绝对差
[https://leetcode-cn.com/problems/minimum-absolute-difference](https://leetcode-cn.com/problems/minimum-absolute-difference) 
## 原题
给你个整数数组 `arr` ，其中每个元素都 **不相同** 。

请你找到所有具有最小绝对差的元素对，并且按升序的顺序返回。

 

 **示例 1：** 

```
输入：arr = [4,2,1,3]
输出：[[1,2],[2,3],[3,4]]

```
 **示例 2：** 

```
输入：arr = [1,3,6,10,15]
输出：[[1,3]]

```
 **示例 3：** 

```
输入：arr = [3,8,-10,23,19,-4,-14,27]
输出：[[-14,-10],[19,23],[23,27]]

```
 

 **提示：** 
-  `2 <= arr.length <= 10^5` 
-  `-10^6 <= arr[i] <= 10^6` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
