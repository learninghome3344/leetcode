# 1601.最多可达成的换楼请求数目
[https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests](https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests) 
## 原题
我们有 `n` 栋楼，编号从 `0` 到 `n - 1` 。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。

给你一个数组 `requests` ，其中 `requests[i] = [from<sub>i</sub>, to<sub>i</sub>]` ，表示一个员工请求从编号为 `from<sub>i</sub>` 的楼搬到编号为 `to<sub>i</sub>` <sub> </sub>的楼。

一开始 **所有楼都是满的** ，所以从请求列表中选出的若干个请求是可行的需要满足 **每栋楼员工净变化为 0** 。意思是每栋楼 **离开** 的员工数目 **等于** 该楼 **搬入** 的员工数数目。比方说 `n = 3` 且两个员工要离开楼 `0` ，一个员工要离开楼 `1` ，一个员工要离开楼 `2` ，如果该请求列表可行，应该要有两个员工搬入楼 `0` ，一个员工搬入楼 `1` ，一个员工搬入楼 `2` 。

请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/move1.jpg" style="height: 406px; width: 600px;">

```
输入：n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
输出：5
解释：请求列表如下：
从楼 0 离开的员工为 x 和 y ，且他们都想要搬到楼 1 。
从楼 1 离开的员工为 a 和 b ，且他们分别想要搬到楼 2 和 0 。
从楼 2 离开的员工为 z ，且他想要搬到楼 0 。
从楼 3 离开的员工为 c ，且他想要搬到楼 4 。
没有员工从楼 4 离开。
我们可以让 x 和 b 交换他们的楼，以满足他们的请求。
我们可以让 y，a 和 z 三人在三栋楼间交换位置，满足他们的要求。
所以最多可以满足 5 个请求。
```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/move2.jpg" style="height: 327px; width: 450px;">

```
输入：n = 3, requests = [[0,0],[1,2],[2,1]]
输出：3
解释：请求列表如下：
从楼 0 离开的员工为 x ，且他想要回到原来的楼 0 。
从楼 1 离开的员工为 y ，且他想要搬到楼 2 。
从楼 2 离开的员工为 z ，且他想要搬到楼 1 。
我们可以满足所有的请求。
```
 **示例 3：** 

```
输入：n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
输出：4

```
 

 **提示：** 
-  `1 <= n <= 20` 
-  `1 <= requests.length <= 16` 
-  `requests[i].length == 2` 
-  `0 <= from<sub>i</sub>, to<sub>i</sub> < n` 
 
**标签**
`位运算` `数组` `回溯` `枚举` 


## 
```python

```
>
# 1602.找到二叉树中最近的右侧节点
[https://leetcode-cn.com/problems/find-nearest-right-node-in-binary-tree](https://leetcode-cn.com/problems/find-nearest-right-node-in-binary-tree) 
## 原题

 
**标签**
`树` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 1603.设计停车系统
[https://leetcode-cn.com/problems/design-parking-system](https://leetcode-cn.com/problems/design-parking-system) 
## 原题
请你给一个停车场设计一个停车系统。停车场总共有三种不同大小的车位：大，中和小，每种尺寸分别有固定数目的车位。

请你实现  `ParkingSystem`  类：
-  `ParkingSystem(int big, int medium, int small)`  初始化  `ParkingSystem`  类，三个参数分别对应每种停车位的数目。
-  `bool addCar(int carType)`  检查是否有  `carType`  对应的停车位。  `carType`  有三种类型：大，中，小，分别用数字  `1` ，  `2`  和  `3`  表示。 **一辆车只能停在**   ** ** `carType`  对应尺寸的停车位中。如果没有空车位，请返回  `false`  ，否则将该车停入车位并返回  `true`  。
 

 **示例 1：** 

```

输入：
["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
[[1, 1, 0], [1], [2], [3], [1]]
输出：
[null, true, true, false, false]

解释：
ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
parkingSystem.addCar(1); // 返回 true ，因为有 1 个空的大车位
parkingSystem.addCar(2); // 返回 true ，因为有 1 个空的中车位
parkingSystem.addCar(3); // 返回 false ，因为没有空的小车位
parkingSystem.addCar(1); // 返回 false ，因为没有空的大车位，唯一一个大车位已经被占据了

```
 

 **提示：** 
-  `0 <= big, medium, small <= 1000` 
-  `carType`  取值为  `1` ，  `2`  或  `3` 
- 最多会调用  `addCar`  函数  `1000`  次
 
**标签**
`设计` `计数` `模拟` 


## 
```python

```
>
# 1604.警告一小时内使用相同员工卡大于等于三次的人
[https://leetcode-cn.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period](https://leetcode-cn.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period) 
## 原题
力扣公司的员工都使用员工卡来开办公室的门。每当一个员工使用一次他的员工卡，安保系统会记录下员工的名字和使用时间。如果一个员工在一小时时间内使用员工卡的次数大于等于三次，这个系统会自动发布一个 **警告**  。

给你字符串数组  `keyName`  和  `keyTime` ，其中  `[keyName[i], keyTime[i]]`  对应一个人的名字和他在  **某一天** 内使用员工卡的时间。

使用时间的格式是 **24小时制**  ，形如 ** "HH:MM"**  ，比方说  `"23:51"` 和  `"09:49"`  。

请你返回去重后的收到系统警告的员工名字，将它们按 **字典序** **升序 ** 排序后返回。

请注意  `"10:00"` - `"11:00"`  视为一个小时时间范围内，而  `"23:51"` - `"00:10"`  不被视为一小时内，因为系统记录的是某一天内的使用情况。

 

 **示例 1：** 

```

输入：keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
输出：["daniel"]
解释："daniel" 在一小时内使用了 3 次员工卡（"10:00"，"10:40"，"11:00"）。

```
 **示例 2：** 

```

输入：keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
输出：["bob"]
解释："bob" 在一小时内使用了 3 次员工卡（"21:00"，"21:20"，"21:30"）。

```
 **示例 3：** 

```

输入：keyName = ["john","john","john"], keyTime = ["23:58","23:59","00:01"]
输出：[]

```
 **示例 4：** 

```

输入：keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
输出：["clare","leslie"]

```
 

 **提示：** 
-  `1 <= keyName.length, keyTime.length <= 10^5` 
-  `keyName.length == keyTime.length` 
-  `keyTime` 格式为  **"HH:MM" ** 。
- 保证  `[keyName[i], keyTime[i]]`  形成的二元对  **互不相同 ** 。
-  `1 <= keyName[i].length <= 10` 
-  `keyName[i]`  只包含小写英文字母。
 
**标签**
`数组` `哈希表` `字符串` `排序` 


## 
```python

```
>
# 1605.给定行和列的和求可行矩阵
[https://leetcode-cn.com/problems/find-valid-matrix-given-row-and-column-sums](https://leetcode-cn.com/problems/find-valid-matrix-given-row-and-column-sums) 
## 原题
给你两个非负整数数组  `rowSum` 和  `colSum`  ，其中  `rowSum[i]`  是二维矩阵中第 `i`  行元素的和， `colSum[j]`  是第 `j`  列元素的和。换言之你不知道矩阵里的每个元素，但是你知道每一行和每一列的和。

请找到大小为  `rowSum.length x colSum.length`  的任意 **非负整数**  矩阵，且该矩阵满足  `rowSum` 和  `colSum`  的要求。

请你返回任意一个满足题目要求的二维矩阵，题目保证存在 **至少一个**  可行矩阵。

 

 **示例 1：** 

```

输入：rowSum = [3,8], colSum = [4,7]
输出：[[3,0],
      [1,7]]
解释：
第 0 行：3 + 0 = 3 == rowSum[0]
第 1 行：1 + 7 = 8 == rowSum[1]
第 0 列：3 + 1 = 4 == colSum[0]
第 1 列：0 + 7 = 7 == colSum[1]
行和列的和都满足题目要求，且所有矩阵元素都是非负的。
另一个可行的矩阵为：[[1,2],
                  [3,5]]

```
 **示例 2：** 

```

输入：rowSum = [5,7,10], colSum = [8,6,8]
输出：[[0,5,0],
      [6,1,0],
      [2,0,8]]

```
 **示例 3：** 

```

输入：rowSum = [14,9], colSum = [6,9,8]
输出：[[0,9,5],
      [6,0,3]]

```
 **示例 4：** 

```

输入：rowSum = [1,0], colSum = [1]
输出：[[1],
      [0]]

```
 **示例 5：** 

```

输入：rowSum = [0], colSum = [0]
输出：[[0]]

```
 

 **提示：** 
-  `1 <= rowSum.length, colSum.length <= 500` 
-  `0 <= rowSum[i], colSum[i] <= 10^8` 
-  `sum(rows) == sum(columns)` 
 
**标签**
`贪心` `数组` `矩阵` 


## 
```python

```
>
# 1606.找到处理最多请求的服务器
[https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests](https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests) 
## 原题
你有 `k`  个服务器，编号为 `0`  到 `k-1`  ，它们可以同时处理多个请求组。每个服务器有无穷的计算能力但是 **不能同时处理超过一个请求**  。请求分配到服务器的规则如下：
- 第  `i`  （序号从 0 开始）个请求到达。
- 如果所有服务器都已被占据，那么该请求被舍弃（完全不处理）。
- 如果第  `(i % k)`  个服务器空闲，那么对应服务器会处理该请求。
- 否则，将请求安排给下一个空闲的服务器（服务器构成一个环，必要的话可能从第 0 个服务器开始继续找下一个空闲的服务器）。比方说，如果第 `i`  个服务器在忙，那么会查看第 `(i+1)`  个服务器，第 `(i+2)`  个服务器等等。
给你一个 **严格递增**  的正整数数组  `arrival`  ，表示第  `i`  个任务的到达时间，和另一个数组  `load`  ，其中  `load[i]`  表示第  `i`  个请求的工作量（也就是服务器完成它所需要的时间）。你的任务是找到 **最繁忙的服务器**  。最繁忙定义为一个服务器处理的请求数是所有服务器里最多的。

请你返回包含所有  **最繁忙服务器**  序号的列表，你可以以任意顺序返回这个列表。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/03/load-1.png" style="height: 221px; width: 389px;" />

```

输入：k = 3, arrival = [1,2,3,4,5], load = [5,2,3,3,3] 
输出：[1] 
解释：
所有服务器一开始都是空闲的。
前 3 个请求分别由前 3 台服务器依次处理。
请求 3 进来的时候，服务器 0 被占据，所以它呗安排到下一台空闲的服务器，也就是服务器 1 。
请求 4 进来的时候，由于所有服务器都被占据，该请求被舍弃。
服务器 0 和 2 分别都处理了一个请求，服务器 1 处理了两个请求。所以服务器 1 是最忙的服务器。

```
 **示例 2：** 

```

输入：k = 3, arrival = [1,2,3,4], load = [1,2,1,2]
输出：[0]
解释：
前 3 个请求分别被前 3 个服务器处理。
请求 3 进来，由于服务器 0 空闲，它被服务器 0 处理。
服务器 0 处理了两个请求，服务器 1 和 2 分别处理了一个请求。所以服务器 0 是最忙的服务器。

```
 **示例 3：** 

```

输入：k = 3, arrival = [1,2,3], load = [10,12,11]
输出：[0,1,2]
解释：每个服务器分别处理了一个请求，所以它们都是最忙的服务器。

```
 **示例 4：** 

```

输入：k = 3, arrival = [1,2,3,4,8,9,10], load = [5,2,10,3,1,2,2]
输出：[1]

```
 **示例 5：** 

```

输入：k = 1, arrival = [1], load = [1]
输出：[0]

```
 

 **提示：** 
-  `1 <= k <= 10^5` 
-  `1 <= arrival.length, load.length <= 10^5` 
-  `arrival.length == load.length` 
-  `1 <= arrival[i], load[i] <= 10^9` 
-  `arrival`  保证 **严格递增**  。
 
**标签**
`贪心` `数组` `有序集合` `堆（优先队列）` 


## 
```python

```
>
# 1607.没有卖出的卖家
[https://leetcode-cn.com/problems/sellers-with-no-sales](https://leetcode-cn.com/problems/sellers-with-no-sales) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1608.特殊数组的特征值
[https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x](https://leetcode-cn.com/problems/special-array-with-x-elements-greater-than-or-equal-x) 
## 原题
给你一个非负整数数组 `nums` 。如果存在一个数 `x` ，使得 `nums` 中恰好有 `x` 个元素 **大于或者等于** `x` ，那么就称 `nums` 是一个 **特殊数组** ，而 `x` 是该数组的 **特征值** 。

注意： `x` **不必** 是 `nums` 的中的元素。

如果数组 `nums` 是一个 **特殊数组** ，请返回它的特征值 `x` 。否则，返回 `-1` 。可以证明的是，如果 `nums` 是特殊数组，那么其特征值 `x` 是 **唯一的** 。

 

 **示例 1：** 

```
输入：nums = [3,5]
输出：2
解释：有 2 个元素（3 和 5）大于或等于 2 。

```
 **示例 2：** 

```
输入：nums = [0,0]
输出：-1
解释：没有满足题目要求的特殊数组，故而也不存在特征值 x 。
如果 x = 0，应该有 0 个元素 >= x，但实际有 2 个。
如果 x = 1，应该有 1 个元素 >= x，但实际有 0 个。
如果 x = 2，应该有 2 个元素 >= x，但实际有 0 个。
x 不能取更大的值，因为 nums 中只有两个元素。
```
 **示例 3：** 

```
输入：nums = [0,4,3,0,4]
输出：3
解释：有 3 个元素大于或等于 3 。

```
 **示例 4：** 

```
输入：nums = [3,6,7,7,0]
输出：-1

```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `0 <= nums[i] <= 1000` 
 
**标签**
`数组` `二分查找` `排序` 


## 
```python

```
>
# 1609.奇偶树
[https://leetcode-cn.com/problems/even-odd-tree](https://leetcode-cn.com/problems/even-odd-tree) 
## 原题
如果一棵二叉树满足下述几个条件，则可以称为 **奇偶树** ：
- 二叉树根节点所在层下标为 `0` ，根的子节点所在层下标为 `1` ，根的孙节点所在层下标为 `2` ，依此类推。
-  **偶数下标** 层上的所有节点的值都是 **奇** 整数，从左到右按顺序 **严格递增** 
-  **奇数下标** 层上的所有节点的值都是 **偶** 整数，从左到右按顺序 **严格递减** 
给你二叉树的根节点，如果二叉树为 **奇偶树** ，则返回 `true` ，否则返回 `false` 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/sample_1_1966.png" style="height: 229px; width: 362px;" />** 

```

输入：root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
输出：true
解释：每一层的节点值分别是：
0 层：[1]
1 层：[10,4]
2 层：[3,7,9]
3 层：[12,8,6,2]
由于 0 层和 2 层上的节点值都是奇数且严格递增，而 1 层和 3 层上的节点值都是偶数且严格递减，因此这是一棵奇偶树。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/sample_2_1966.png" style="height: 167px; width: 363px;" />** 

```

输入：root = [5,4,2,3,3,7]
输出：false
解释：每一层的节点值分别是：
0 层：[5]
1 层：[4,2]
2 层：[3,3,7]
2 层上的节点值不满足严格递增的条件，所以这不是一棵奇偶树。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/sample_1_333_1966.png" style="height: 167px; width: 363px;" />

```

输入：root = [5,9,1,3,5,7]
输出：false
解释：1 层上的节点值应为偶数。

```
 **示例 4：** 

```

输入：root = [1]
输出：true

```
 **示例 5：** 

```

输入：root = [11,8,6,1,3,9,11,30,20,18,16,12,10,4,2,17]
输出：true

```
 

 **提示：** 
- 树中节点数在范围 `[1, 10^5]` 内
-  `1 <= Node.val <= 10^6` 
 
**标签**
`树` `广度优先搜索` `二叉树` 


## 
```python

```
>
# 1610.可见点的最大数目
[https://leetcode-cn.com/problems/maximum-number-of-visible-points](https://leetcode-cn.com/problems/maximum-number-of-visible-points) 
## 原题
给你一个点数组 `points` 和一个表示角度的整数 `angle` ，你的位置是 `location` ，其中 `location = [pos<sub>x</sub>, pos<sub>y</sub>]` 且 `points[i] = [x<sub>i</sub>, y<sub>i</sub>]` 都表示 X-Y 平面上的整数坐标。

最开始，你面向东方进行观测。你 **不能** 进行移动改变位置，但可以通过 **自转** 调整观测角度。换句话说， `pos<sub>x</sub>` 和 `pos<sub>y</sub>` 不能改变。你的视野范围的角度用 `angle` 表示， 这决定了你观测任意方向时可以多宽。设 `d` 为你逆时针自转旋转的度数，那么你的视野就是角度范围 `[d - angle/2, d + angle/2]` 所指示的那片区域。

<video autoplay="" controls="" height="360" muted="" style="max-width:100%;height:auto;" width="750"><source src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/angle.mp4" type="video/mp4" />Your browser does not support the video tag or this video format.</video>

对于每个点，如果由该点、你的位置以及从你的位置直接向东的方向形成的角度 **位于你的视野中** ，那么你就可以看到它。

同一个坐标上可以有多个点。你所在的位置也可能存在一些点，但不管你的怎么旋转，总是可以看到这些点。同时，点不会阻碍你看到其他点。

返回你能看到的点的最大数目。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/89a07e9b-00ab-4967-976a-c723b2aa8656.png" style="height: 300px; width: 400px;" />

```

输入：points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
输出：3
解释：阴影区域代表你的视野。在你的视野中，所有的点都清晰可见，尽管 [2,2] 和 [3,3]在同一条直线上，你仍然可以看到 [3,3] 。
```
 **示例 2：** 

```

输入：points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
输出：4
解释：在你的视野中，所有的点都清晰可见，包括你所在位置的那个点。
```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/04/5010bfd3-86e6-465f-ac64-e9df941d2e49.png" style="height: 348px; width: 690px;" />

```

输入：points = [[1,0],[2,1]], angle = 13, location = [1,1]
输出：1
解释：如图所示，你只能看到两点之一。
```
 

 **提示：** 
-  `1 <= points.length <= 10^5` 
-  `points[i].length == 2` 
-  `location.length == 2` 
-  `0 <= angle < 360` 
-  `0 <= pos<sub>x</sub>, pos<sub>y</sub>, x<sub>i</sub>, y<sub>i</sub> <= 100` 
 
**标签**
`几何` `数组` `数学` `排序` `滑动窗口` 


## 
```python

```
>
# 1611.使整数变为 0 的最少操作次数
[https://leetcode-cn.com/problems/minimum-one-bit-operations-to-make-integers-zero](https://leetcode-cn.com/problems/minimum-one-bit-operations-to-make-integers-zero) 
## 原题
给你一个整数 `n` ，你需要重复执行多次下述操作将其转换为 `0` ：
- 翻转 `n` 的二进制表示中最右侧位（第 `0` 位）。
- 如果第 `(i-1)` 位为 `1` 且从第 `(i-2)` 位到第 `0` 位都为 `0` ，则翻转 `n` 的二进制表示中的第 `i` 位。
返回将 `n` 转换为 `0` 的最小操作次数。

 

 **示例 1：** 

```

输入：n = 0
输出：0

```
 **示例 2：** 

```

输入：n = 3
输出：2
解释：3 的二进制表示为 "11"
"11" -> "01" ，执行的是第 2 种操作，因为第 0 位为 1 。
"01" -> "00" ，执行的是第 1 种操作。

```
 **示例 3：** 

```

输入：n = 6
输出：4
解释：6 的二进制表示为 "110".
"110" -> "010" ，执行的是第 2 种操作，因为第 1 位为 1 ，第 0 到 0 位为 0 。
"010" -> "011" ，执行的是第 1 种操作。
"011" -> "001" ，执行的是第 2 种操作，因为第 0 位为 1 。
"001" -> "000" ，执行的是第 1 种操作。

```
 **示例 4：** 

```

输入：n = 9
输出：14

```
 **示例 5：** 

```

输入：n = 333
输出：393

```
 

 **提示：** 
-  `0 <= n <= 10^9` 
 
**标签**
`位运算` `记忆化搜索` `动态规划` 


## 
```python

```
>
# 1612.检查两棵二叉表达式树是否等价
[https://leetcode-cn.com/problems/check-if-two-expression-trees-are-equivalent](https://leetcode-cn.com/problems/check-if-two-expression-trees-are-equivalent) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1613.找到遗失的ID
[https://leetcode-cn.com/problems/find-the-missing-ids](https://leetcode-cn.com/problems/find-the-missing-ids) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1614.括号的最大嵌套深度
[https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses](https://leetcode-cn.com/problems/maximum-nesting-depth-of-the-parentheses) 
## 原题
如果字符串满足以下条件之一，则可以称之为 **有效括号字符串** **（valid parentheses string** ，可以简写为 **VPS** ）：
- 字符串是一个空字符串 `""` ，或者是一个不为 `"("` 或 `")"` 的单字符。
- 字符串可以写为 `AB` （ `A` 与 `B`  字符串连接），其中 `A` 和 `B` 都是 **有效括号字符串** 。
- 字符串可以写为 `(A)` ，其中 `A` 是一个 **有效括号字符串** 。
类似地，可以定义任何有效括号字符串  `S` 的 **嵌套深度** `depth(S)` ：
-  `depth("") = 0` 
-  `depth(C) = 0` ，其中 `C` 是单个字符的字符串，且该字符不是 `"("` 或者 `")"` 
-  `depth(A + B) = max(depth(A), depth(B))` ，其中 `A` 和 `B` 都是 **有效括号字符串** 
-  `depth("(" + A + ")") = 1 + depth(A)` ，其中 `A` 是一个 **有效括号字符串** 
例如： `""` 、 `"()()"` 、 `"()(()())"` 都是 **有效括号字符串** （嵌套深度分别为 0、1、2），而 `")("` 、 `"(()"` 都不是 **有效括号字符串** 。

给你一个 **有效括号字符串** `s` ，返回该字符串的 `s` **嵌套深度** 。

 

 **示例 1：** 

```

输入：s = "(1+(2*3)+((8)/4))+1"
输出：3
解释：数字 8 在嵌套的 3 层括号中。

```
 **示例 2：** 

```

输入：s = "(1)+((2))+(((3)))"
输出：3

```
 **示例 3：** 

```

输入：s = "1+(2*3)/(2-1)"
输出：1

```
 **示例 4：** 

```

输入：s = "1"
输出：0

```
 

 **提示：** 
-  `1 <= s.length <= 100` 
-  `s` 由数字 `0-9` 和字符 `'+'` 、 `'-'` 、 `'*'` 、 `'/'` 、 `'('` 、 `')'` 组成
- 题目数据保证括号表达式 `s` 是 **有效的括号表达式** 
 
**标签**
`栈` `字符串` 


## 
```python

```
>
# 1615.最大网络秩
[https://leetcode-cn.com/problems/maximal-network-rank](https://leetcode-cn.com/problems/maximal-network-rank) 
## 原题
 `n` 座城市和一些连接这些城市的道路 `roads` 共同组成一个基础设施网络。每个 `roads[i] = [a<sub>i</sub>, b<sub>i</sub>]` 都表示在城市 `a<sub>i</sub>` 和 `b<sub>i</sub>` 之间有一条双向道路。

两座不同城市构成的 **城市对** 的 **网络秩** 定义为：与这两座城市 **直接** 相连的道路总数。如果存在一条道路直接连接这两座城市，则这条道路只计算 **一次** 。

整个基础设施网络的 **最大网络秩** 是所有不同城市对中的 **最大网络秩** 。

给你整数 `n` 和数组 `roads` ，返回整个基础设施网络的 **最大网络秩** 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/11/ex1.png" style="width: 292px; height: 172px;" />** 

```

输入：n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
输出：4
解释：城市 0 和 1 的网络秩是 4，因为共有 4 条道路与城市 0 或 1 相连。位于 0 和 1 之间的道路只计算一次。

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/11/ex2.png" style="width: 292px; height: 172px;" />** 

```

输入：n = 5, roads = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
输出：5
解释：共有 5 条道路与城市 1 或 2 相连。

```
 **示例 3：** 

```

输入：n = 8, roads = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
输出：5
解释：2 和 5 的网络秩为 5，注意并非所有的城市都需要连接起来。

```
 

 **提示：** 
-  `2 <= n <= 100` 
-  `0 <= roads.length <= n * (n - 1) / 2` 
-  `roads[i].length == 2` 
-  `0 <= a<sub>i</sub>, b<sub>i</sub> <= n-1` 
-  `a<sub>i</sub> != b<sub>i</sub>` 
- 每对城市之间 **最多只有一条**  道路相连
 
**标签**
`图` 


## 
```python

```
>
# 1616.分割两个字符串得到回文串
[https://leetcode-cn.com/problems/split-two-strings-to-make-palindrome](https://leetcode-cn.com/problems/split-two-strings-to-make-palindrome) 
## 原题
给你两个字符串  `a` 和  `b`  ，它们长度相同。请你选择一个下标，将两个字符串都在  **相同的下标** 分割开。由  `a`  可以得到两个字符串：  `a<sub>prefix</sub>`  和  `a<sub>suffix</sub>`  ，满足  `a = a<sub>prefix</sub> + a<sub>suffix</sub>` <sub> </sub>，同理，由  `b` 可以得到两个字符串  `b<sub>prefix</sub>` 和  `b<sub>suffix</sub>`  ，满足  `b = b<sub>prefix</sub> + b<sub>suffix</sub>`  。请你判断  `a<sub>prefix</sub> + b<sub>suffix</sub>` 或者  `b<sub>prefix</sub> + a<sub>suffix</sub>`  能否构成回文串。

当你将一个字符串  `s`  分割成  `s<sub>prefix</sub>` 和  `s<sub>suffix</sub>`  时，  `s<sub>suffix</sub>` 或者  `s<sub>prefix</sub>` 可以为空。比方说，  `s = "abc"`  那么  `"" + "abc"`  ，  `"a" + "bc" ` ，  `"ab" + "c"`  和  `"abc" + ""`  都是合法分割。

如果 **能构成回文字符串** ，那么请返回  `true` ，否则返回 * * `false`  。

 **注意** ，  `x + y`  表示连接字符串  `x` 和  `y`  。

 

 **示例 1：** 

```

输入：a = "x", b = "y"
输出：true
解释：如果 a 或者 b 是回文串，那么答案一定为 true ，因为你可以如下分割：
aprefix = "", asuffix = "x"
bprefix = "", bsuffix = "y"
那么 aprefix + bsuffix = "" + "y" = "y" 是回文串。

```
 **示例 2：** 

```

输入：a = "abdef", b = "fecab"
输出：true

```
 **示例 3：** 

```

输入：a = "ulacfd", b = "jizalu"
输出：true
解释：在下标为 3 处分割：
aprefix = "ula", asuffix = "cfd"
bprefix = "jiz", bsuffix = "alu"
那么 aprefix + bsuffix = "ula" + "alu" = "ulaalu" 是回文串。
```
 **示例 4：** 

```

输入：a = "xbdef", b = "xecab"
输出：false

```
 

 **提示：** 
-  `1 <= a.length, b.length <= 10^5` 
-  `a.length == b.length` 
-  `a` 和  `b`  都只包含小写英文字母
 
**标签**
`贪心` `双指针` `字符串` 


## 
```python

```
>
# 1617.统计子树中城市之间最大距离
[https://leetcode-cn.com/problems/count-subtrees-with-max-distance-between-cities](https://leetcode-cn.com/problems/count-subtrees-with-max-distance-between-cities) 
## 原题
给你  `n`  个城市，编号为从  `1` 到  `n`  。同时给你一个大小为  `n-1`  的数组  `edges`  ，其中  `edges[i] = [u<sub>i</sub>, v<sub>i</sub>]`  表示城市  `u<sub>i</sub>`  和  `v<sub>i</sub>` <sub> </sub>之间有一条双向边。题目保证任意城市之间只有唯一的一条路径。换句话说，所有城市形成了一棵  **树**  。

一棵  **子树**  是城市的一个子集，且子集中任意城市之间可以通过子集中的其他城市和边到达。两个子树被认为不一样的条件是至少有一个城市在其中一棵子树中存在，但在另一棵子树中不存在。

对于  `d`  从  `1` 到  `n-1`  ，请你找到城市间  **最大距离**  恰好为 `d`  的所有子树数目。

请你返回一个大小为  `n-1`  的数组，其中第 * * `d` * * 个元素（ **下标从 1 开始** ）是城市间 **最大距离** 恰好等于  `d`  的子树数目。

 **请注意** ，两个城市间距离定义为它们之间需要经过的边的数目。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/11/p1.png" style="width: 161px; height: 181px;" />** 

```

输入：n = 4, edges = [[1,2],[2,3],[2,4]]
输出：[3,4,0]
解释：
子树 {1,2}, {2,3} 和 {2,4} 最大距离都是 1 。
子树 {1,2,3}, {1,2,4}, {2,3,4} 和 {1,2,3,4} 最大距离都为 2 。
不存在城市间最大距离为 3 的子树。

```
 **示例 2：** 

```

输入：n = 2, edges = [[1,2]]
输出：[1]

```
 **示例 3：** 

```

输入：n = 3, edges = [[1,2],[2,3]]
输出：[2,1]

```
 

 **提示：** 
-  `2 <= n <= 15` 
-  `edges.length == n-1` 
-  `edges[i].length == 2` 
-  `1 <= u<sub>i</sub>, v<sub>i</sub> <= n` 
- 题目保证  `(u<sub>i</sub>, v<sub>i</sub>)`  所表示的边互不相同。
 
**标签**
`位运算` `树` `动态规划` `状态压缩` `枚举` 


## 
```python

```
>
# 1618.找出适应屏幕的最大字号
[https://leetcode-cn.com/problems/maximum-font-to-fit-a-sentence-in-a-screen](https://leetcode-cn.com/problems/maximum-font-to-fit-a-sentence-in-a-screen) 
## 原题

 
**标签**
`数组` `字符串` `二分查找` `交互` 


## 
```python

```
>
# 1619.删除某些元素后的数组均值
[https://leetcode-cn.com/problems/mean-of-array-after-removing-some-elements](https://leetcode-cn.com/problems/mean-of-array-after-removing-some-elements) 
## 原题
给你一个整数数组  `arr`  ，请你删除最小  `5%`  的数字和最大 `5%`  的数字后，剩余数字的平均值。

与 **标准答案**  误差在  `10^-5`  的结果都被视为正确结果。

 

 **示例 1：** 

```

输入：arr = [1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3]
输出：2.00000
解释：删除数组中最大和最小的元素后，所有元素都等于 2，所以平均值为 2 。

```
 **示例 2：** 

```

输入：arr = [6,2,7,5,1,2,0,3,10,2,5,0,5,5,0,8,7,6,8,0]
输出：4.00000

```
 **示例 3：** 

```

输入：arr = [6,0,7,0,7,5,7,8,3,4,0,7,8,1,6,8,1,1,2,4,8,1,9,5,4,3,8,5,10,8,6,6,1,0,6,10,8,2,3,4]
输出：4.77778

```
 **示例 4：** 

```

输入：arr = [9,7,8,7,7,8,4,4,6,8,8,7,6,8,8,9,2,6,0,0,1,10,8,6,3,3,5,1,10,9,0,7,10,0,10,4,1,10,6,9,3,6,0,0,2,7,0,6,7,2,9,7,7,3,0,1,6,1,10,3]
输出：5.27778

```
 **示例 5：** 

```

输入：arr = [4,8,4,10,0,7,1,3,7,8,8,3,4,1,6,2,1,1,8,0,9,8,0,3,9,10,3,10,1,10,7,3,2,1,4,9,10,7,6,4,0,8,5,1,2,1,6,2,5,0,7,10,9,10,3,7,10,5,8,5,7,6,7,6,10,9,5,10,5,5,7,2,10,7,7,8,2,0,1,1]
输出：5.29167

```
 

 **提示：** 
-  `20 <= arr.length <= 1000` 
-  `arr.length` <b> </b>是  `20`  的 ** 倍数**  
-  `0 <= arr[i] <= 10^5` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 1620.网络信号最好的坐标
[https://leetcode-cn.com/problems/coordinate-with-maximum-network-quality](https://leetcode-cn.com/problems/coordinate-with-maximum-network-quality) 
## 原题
给你一个数组 `towers`  和一个整数 `radius`  ，数组中包含一些网络信号塔，其中  `towers[i] = [x<sub>i</sub>, y<sub>i</sub>, q<sub>i</sub>]`  表示第  `i`  个网络信号塔的坐标是  `(x<sub>i</sub>, y<sub>i</sub>)`  且信号强度参数为  `q<sub>i</sub>` <sub> </sub>。所有坐标都是在  X-Y 坐标系内的  **整数**  坐标。两个坐标之间的距离用 **欧几里得距离**  计算。

整数  `radius`  表示一个塔 **能到达 ** 的 **最远距离**  。如果一个坐标跟塔的距离在 `radius`  以内，那么该塔的信号可以到达该坐标。在这个范围以外信号会很微弱，所以 `radius`  以外的距离该塔是 **不能到达的**  。

如果第 `i`  个塔能到达 `(x, y)`  ，那么该塔在此处的信号为  `⌊q<sub>i</sub> / (1 + d)⌋`  ，其中  `d`  是塔跟此坐标的距离。一个坐标的 <b>网络信号</b> 是所有 **能到达 ** 该坐标的塔的信号强度之和。

请你返回 **网络信号**  最大的整数坐标点。如果有多个坐标网络信号一样大，请你返回字典序最小的一个坐标。

 **注意：** 
- 坐标  `(x1, y1)`  字典序比另一个坐标  `(x2, y2)`  小：要么  `x1 < x2`  ，要么  `x1 == x2` 且  `y1 < y2`  。
-  `⌊val⌋`  表示小于等于  `val`  的最大整数（向下取整函数）。
 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/17/untitled-diagram.png" style="width: 176px; height: 176px;" />
```

输入：towers = [[1,2,5],[2,1,7],[3,1,9]], radius = 2
输出：[2,1]
解释：
坐标 (2, 1) 信号强度之和为 13
- 塔 (2, 1) 强度参数为 7 ，在该点强度为 ⌊7 / (1 + sqrt(0)⌋ = ⌊7⌋ = 7
- 塔 (1, 2) 强度参数为 5 ，在该点强度为 ⌊5 / (1 + sqrt(2)⌋ = ⌊2.07⌋ = 2
- 塔 (3, 1) 强度参数为 9 ，在该点强度为 ⌊9 / (1 + sqrt(1)⌋ = ⌊4.5⌋ = 4
没有别的坐标有更大的信号强度。
```
 **示例 2：** 

```

输入：towers = [[23,11,21]], radius = 9
输出：[23,11]

```
 **示例 3：** 

```

输入：towers = [[1,2,13],[2,1,7],[0,1,9]], radius = 2
输出：[1,2]

```
 **示例 4：** 

```

输入：towers = [[2,1,9],[0,1,9]], radius = 2
输出：[0,1]
解释：坐标 (0, 1) 和坐标 (2, 1) 都是强度最大的位置，但是 (0, 1) 字典序更小。

```
 

 **提示：** 
-  `1 <= towers.length <= 50` 
-  `towers[i].length == 3` 
-  `0 <= x<sub>i</sub>, y<sub>i</sub>, q<sub>i</sub> <= 50` 
-  `1 <= radius <= 50` 
 
**标签**
`数组` `枚举` 


## 
```python

```
>
# 1621.大小为 K 的不重叠线段的数目
[https://leetcode-cn.com/problems/number-of-sets-of-k-non-overlapping-line-segments](https://leetcode-cn.com/problems/number-of-sets-of-k-non-overlapping-line-segments) 
## 原题
给你一维空间的  `n`  个点，其中第  `i`  个点（编号从  `0` 到  `n-1` ）位于  `x = i`  处，请你找到  **恰好**   `k`   **个不重叠**  线段且每个线段至少覆盖两个点的方案数。线段的两个端点必须都是  **整数坐标**  。这  `k`  个线段不需要全部覆盖全部  `n`  个点，且它们的端点  **可以 ** 重合。

请你返回 `k`  个不重叠线段的方案数。由于答案可能很大，请将结果对  `10^9 + 7`   **取余** 后返回。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/17/ex1.png" style="width: 179px; height: 222px;" />
```

输入：n = 4, k = 2
输出：5
解释：
如图所示，两个线段分别用红色和蓝色标出。
上图展示了 5 种不同的方案 {(0,2),(2,3)}，{(0,1),(1,3)}，{(0,1),(2,3)}，{(1,2),(2,3)}，{(0,1),(1,2)} 。
```
 **示例 2：** 

```

输入：n = 3, k = 1
输出：3
解释：总共有 3 种不同的方案 {(0,1)}, {(0,2)}, {(1,2)} 。

```
 **示例 3：** 

```

输入：n = 30, k = 7
输出：796297179
解释：画 7 条线段的总方案数为 3796297200 种。将这个数对 10^9 + 7 取余得到 796297179 。

```
 **示例 4：** 

```

输入：n = 5, k = 3
输出：7

```
 **示例 5：** 

```

输入：n = 3, k = 2
输出：1
```
 

 **提示：** 
-  `2 <= n <= 1000` 
-  `1 <= k <= n-1` 
 
**标签**
`数学` `动态规划` 


## 
```python

```
>
# 1622.奇妙序列
[https://leetcode-cn.com/problems/fancy-sequence](https://leetcode-cn.com/problems/fancy-sequence) 
## 原题
请你实现三个 API `append` ， `addAll`  和  `multAll`  来实现奇妙序列。

请实现  `Fancy`  类 ：
-  `Fancy()`  初始化一个空序列对象。
-  `void append(val)` 将整数  `val`  添加在序列末尾。
-  `void addAll(inc)`  将所有序列中的现有数值都增加  `inc`  。
-  `void multAll(m)`  将序列中的所有现有数值都乘以整数  `m`  。
-  `int getIndex(idx)` 得到下标为  `idx`  处的数值（下标从 0 开始），并将结果对  `10^9 + 7`  取余。如果下标大于等于序列的长度，请返回  `-1`  。
 

 **示例：** 

```

输入：
["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll", "append", "multAll", "getIndex", "getIndex", "getIndex"]
[[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
输出：
[null, null, null, null, null, 10, null, null, null, 26, 34, 20]

解释：
Fancy fancy = new Fancy();
fancy.append(2);   // 奇妙序列：[2]
fancy.addAll(3);   // 奇妙序列：[2+3] -> [5]
fancy.append(7);   // 奇妙序列：[5, 7]
fancy.multAll(2);  // 奇妙序列：[5*2, 7*2] -> [10, 14]
fancy.getIndex(0); // 返回 10
fancy.addAll(3);   // 奇妙序列：[10+3, 14+3] -> [13, 17]
fancy.append(10);  // 奇妙序列：[13, 17, 10]
fancy.multAll(2);  // 奇妙序列：[13*2, 17*2, 10*2] -> [26, 34, 20]
fancy.getIndex(0); // 返回 26
fancy.getIndex(1); // 返回 34
fancy.getIndex(2); // 返回 20

```
 

 **提示：** 
-  `1 <= val, inc, m <= 100` 
-  `0 <= idx <= 10^5` 
- 总共最多会有  `10^5`  次对  `append` ， `addAll` ， `multAll`  和  `getIndex`  的调用。
 
**标签**
`设计` `线段树` `数学` 


## 
```python

```
>
# 1623.三人国家代表队
[https://leetcode-cn.com/problems/all-valid-triplets-that-can-represent-a-country](https://leetcode-cn.com/problems/all-valid-triplets-that-can-represent-a-country) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1624.两个相同字符之间的最长子字符串
[https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters](https://leetcode-cn.com/problems/largest-substring-between-two-equal-characters) 
## 原题
给你一个字符串 `s` ，请你返回 **两个相同字符之间的最长子字符串的长度** *，* 计算长度时不含这两个字符。如果不存在这样的子字符串，返回 `-1` 。

 **子字符串** 是字符串中的一个连续字符序列。

 

 **示例 1：** 

```
输入：s = "aa"
输出：0
解释：最优的子字符串是两个 'a' 之间的空子字符串。
```
 **示例 2：** 

```
输入：s = "abca"
输出：2
解释：最优的子字符串是 "bc" 。

```
 **示例 3：** 

```
输入：s = "cbzxy"
输出：-1
解释：s 中不存在出现出现两次的字符，所以返回 -1 。

```
 **示例 4：** 

```
输入：s = "cabbac"
输出：4
解释：最优的子字符串是 "abba" ，其他的非最优解包括 "bb" 和 "" 。

```
 

 **提示：** 
-  `1 <= s.length <= 300` 
-  `s` 只含小写英文字母
 
**标签**
`哈希表` `字符串` 


## 
```python

```
>
# 1625.执行操作后字典序最小的字符串
[https://leetcode-cn.com/problems/lexicographically-smallest-string-after-applying-operations](https://leetcode-cn.com/problems/lexicographically-smallest-string-after-applying-operations) 
## 原题
给你一个字符串 `s` 以及两个整数 `a` 和 `b` 。其中，字符串 `s` 的长度为偶数，且仅由数字 `0` 到 `9` 组成。

你可以在 `s` 上按任意顺序多次执行下面两个操作之一：
- 累加：将  `a` 加到 `s` 中所有下标为奇数的元素上（ **下标从 0 开始** ）。数字一旦超过 `9` 就会变成 `0` ，如此循环往复。例如， `s = "3456"` 且 `a = 5` ，则执行此操作后 `s` 变成 `"3951"` 。
- 轮转：将 `s` 向右轮转 `b` 位。例如， `s = "3456"` 且 `b = 1` ，则执行此操作后 `s` 变成 `"6345"` 。
请你返回在 `s` 上执行上述操作任意次后可以得到的 **字典序最小** 的字符串。

如果两个字符串长度相同，那么字符串 `a` 字典序比字符串 `b` 小可以这样定义：在 `a` 和 `b` 出现不同的第一个位置上，字符串 `a` 中的字符出现在字母表中的时间早于 `b` 中的对应字符。例如， `"0158”` 字典序比 `"0190"` 小，因为不同的第一个位置是在第三个字符，显然 `'5'` 出现在 `'9'` 之前。

 

 **示例 1：** 

```

输入：s = "5525", a = 9, b = 2
输出："2050"
解释：执行操作如下：
初态："5525"
轮转："2555"
累加："2454"
累加："2353"
轮转："5323"
累加："5222"
累加："5121"
轮转："2151"
累加："2050"​​​​​​​​​​​​
无法获得字典序小于 "2050" 的字符串。

```
 **示例 2：** 

```

输入：s = "74", a = 5, b = 1
输出："24"
解释：执行操作如下：
初态："74"
轮转："47"
累加："42"
轮转："24"​​​​​​​​​​​​
无法获得字典序小于 "24" 的字符串。

```
 **示例 3：** 

```

输入：s = "0011", a = 4, b = 2
输出："0011"
解释：无法获得字典序小于 "0011" 的字符串。

```
 **示例 4：** 

```

输入：s = "43987654", a = 7, b = 3
输出："00553311"

```
 

 **提示：** 
-  `2 <= s.length <= 100` 
-  `s.length` 是偶数
-  `s` 仅由数字 `0` 到 `9` 组成
-  `1 <= a <= 9` 
-  `1 <= b <= s.length - 1` 
 
**标签**
`广度优先搜索` `字符串` 


## 
```python

```
>
# 1626.无矛盾的最佳球队
[https://leetcode-cn.com/problems/best-team-with-no-conflicts](https://leetcode-cn.com/problems/best-team-with-no-conflicts) 
## 原题
假设你是球队的经理。对于即将到来的锦标赛，你想组合一支总体得分最高的球队。球队的得分是球队中所有球员的分数 **总和** 。

然而，球队中的矛盾会限制球员的发挥，所以必须选出一支 **没有矛盾** 的球队。如果一名年龄较小球员的分数 **严格大于** 一名年龄较大的球员，则存在矛盾。同龄球员之间不会发生矛盾。

给你两个列表 `scores` 和 `ages` ，其中每组 `scores[i]` 和 `ages[i]` 表示第 `i` 名球员的分数和年龄。请你返回 **所有可能的无矛盾球队中得分最高那支的分数** 。

 

 **示例 1：** 

```
输入：scores = [1,3,5,10,15], ages = [1,2,3,4,5]
输出：34
解释：你可以选中所有球员。
```
 **示例 2：** 

```
输入：scores = [4,5,6,5], ages = [2,1,2,1]
输出：16
解释：最佳的选择是后 3 名球员。注意，你可以选中多个同龄球员。

```
 **示例 3：** 

```
输入：scores = [1,2,3,5], ages = [8,9,10,1]
输出：6
解释：最佳的选择是前 3 名球员。

```
 

 **提示：** 
-  `1 <= scores.length, ages.length <= 1000` 
-  `scores.length == ages.length` 
-  `1 <= scores[i] <= 10^6` 
-  `1 <= ages[i] <= 1000` 
 
**标签**
`数组` `动态规划` `排序` 


## 
```python

```
>
# 1627.带阈值的图连通性
[https://leetcode-cn.com/problems/graph-connectivity-with-threshold](https://leetcode-cn.com/problems/graph-connectivity-with-threshold) 
## 原题
有 `n` 座城市，编号从 `1` 到 `n` 。编号为 `x` 和 `y` 的两座城市直接连通的前提是： `x` 和 `y` 的公因数中，至少有一个 **严格大于** 某个阈值 `threshold` 。更正式地说，如果存在整数 `z` ，且满足以下所有条件，则编号 `x` 和 `y` 的城市之间有一条道路：
-  `x % z == 0` 
-  `y % z == 0` 
-  `z > threshold` 
给你两个整数 `n` 和 `threshold` ，以及一个待查询数组，请你判断每个查询 `queries[i] = [a<sub>i</sub>, b<sub>i</sub>]` 指向的城市 `a<sub>i</sub>` 和 `b<sub>i</sub>` 是否连通（即，它们之间是否存在一条路径）。

返回数组 `answer` ，其中 `answer.length == queries.length` 。如果第 `i` 个查询中指向的城市 `a<sub>i</sub>` 和 `b<sub>i</sub>` 连通，则 `answer[i]` 为 `true` ；如果不连通，则 `answer[i]` 为 `false` 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/18/ex1.jpg" style="width: 382px; height: 181px;" />

 

```

输入：n = 6, threshold = 2, queries = [[1,4],[2,5],[3,6]]
输出：[false,false,true]
解释：每个数的因数如下：
1:   1
2:   1, 2
3:   1, 3
4:   1, 2, 4
5:   1, 5
6:   1, 2, 3, 6
所有大于阈值的的因数已经加粗标识，只有城市 3 和 6 共享公约数 3 ，因此结果是： 
[1,4]   1 与 4 不连通
[2,5]   2 与 5 不连通
[3,6]   3 与 6 连通，存在路径 3--6

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/18/tmp.jpg" style="width: 532px; height: 302px;" />

 

```

输入：n = 6, threshold = 0, queries = [[4,5],[3,4],[3,2],[2,6],[1,3]]
输出：[true,true,true,true,true]
解释：每个数的因数与上一个例子相同。但是，由于阈值为 0 ，所有的因数都大于阈值。因为所有的数字共享公因数 1 ，所以所有的城市都互相连通。

```
 **示例 3：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/16/ex3.jpg" style="width: 282px; height: 282px;" />

 

```

输入：n = 5, threshold = 1, queries = [[4,5],[4,5],[3,2],[2,3],[3,4]]
输出：[false,false,false,false,false]
解释：只有城市 2 和 4 共享的公约数 2 严格大于阈值 1 ，所以只有这两座城市是连通的。
注意，同一对节点 [x, y] 可以有多个查询，并且查询 [x，y] 等同于查询 [y，x] 。

```
 

 **提示：** 
-  `2 <= n <= 10^4` 
-  `0 <= threshold <= n` 
-  `1 <= queries.length <= 10^5` 
-  `queries[i].length == 2` 
-  `1 <= a<sub>i</sub>, b<sub>i</sub> <= cities` 
-  `a<sub>i</sub> != b<sub>i</sub>` 
 
**标签**
`并查集` `数组` `数学` 


## 
```python

```
>
# 1628.设计带解析函数的表达式树
[https://leetcode-cn.com/problems/design-an-expression-tree-with-evaluate-function](https://leetcode-cn.com/problems/design-an-expression-tree-with-evaluate-function) 
## 原题

 
**标签**
`栈` `树` `设计` `数学` `二叉树` 


## 
```python

```
>
# 1629.按键持续时间最长的键
[https://leetcode-cn.com/problems/slowest-key](https://leetcode-cn.com/problems/slowest-key) 
## 原题
LeetCode 设计了一款新式键盘，正在测试其可用性。测试人员将会点击一系列键（总计 `n` 个），每次一个。

给你一个长度为 `n` 的字符串 `keysPressed` ，其中 `keysPressed[i]` 表示测试序列中第 `i` 个被按下的键。 `releaseTimes` 是一个升序排列的列表，其中 `releaseTimes[i]` 表示松开第 `i` 个键的时间。字符串和数组的 **下标都从 0 开始** 。第 `0` 个键在时间为 `0` 时被按下，接下来每个键都 **恰好** 在前一个键松开时被按下。

测试人员想要找出按键 **持续时间最长** 的键。第 `i` ^ 次按键的持续时间为 `releaseTimes[i] - releaseTimes[i - 1]` ，第 `0` 次按键的持续时间为 `releaseTimes[0]` 。

注意，测试期间，同一个键可以在不同时刻被多次按下，而每次的持续时间都可能不同。

请返回单次按键 **持续时间最长** 的键，如果有多个这样的键，则返回 **按字母顺序排列最大** 的那个键。

 

 **示例 1：** 

```

输入：releaseTimes = [9,29,49,50], keysPressed = "cbcd"
输出："c"
解释：按键顺序和持续时间如下：
按下 'c' ，持续时间 9（时间 0 按下，时间 9 松开）
按下 'b' ，持续时间 29 - 9 = 20（松开上一个键的时间 9 按下，时间 29 松开）
按下 'c' ，持续时间 49 - 29 = 20（松开上一个键的时间 29 按下，时间 49 松开）
按下 'd' ，持续时间 50 - 49 = 1（松开上一个键的时间 49 按下，时间 50 松开）
按键持续时间最长的键是 'b' 和 'c'（第二次按下时），持续时间都是 20
'c' 按字母顺序排列比 'b' 大，所以答案是 'c'

```
 **示例 2：** 

```

输入：releaseTimes = [12,23,36,46,62], keysPressed = "spuda"
输出："a"
解释：按键顺序和持续时间如下：
按下 's' ，持续时间 12
按下 'p' ，持续时间 23 - 12 = 11
按下 'u' ，持续时间 36 - 23 = 13
按下 'd' ，持续时间 46 - 36 = 10
按下 'a' ，持续时间 62 - 46 = 16
按键持续时间最长的键是 'a' ，持续时间 16
```
 

 **提示：** 
-  `releaseTimes.length == n` 
-  `keysPressed.length == n` 
-  `2 <= n <= 1000` 
-  `1 <= releaseTimes[i] <= 10^9` 
-  `releaseTimes[i] < releaseTimes[i+1]` 
-  `keysPressed` 仅由小写英文字母组成
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 1630.等差子数组
[https://leetcode-cn.com/problems/arithmetic-subarrays](https://leetcode-cn.com/problems/arithmetic-subarrays) 
## 原题
如果一个数列由至少两个元素组成，且每两个连续元素之间的差值都相同，那么这个序列就是 **等差数列** 。更正式地，数列 `s` 是等差数列，只需要满足：对于每个有效的 `i` ， `s[i+1] - s[i] == s[1] - s[0]` 都成立。

例如，下面这些都是 **等差数列** ：

```
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```
下面的数列 **不是等差数列** ：

```
1, 1, 2, 5, 7
```
给你一个由 `n` 个整数组成的数组 `nums` ，和两个由 `m` 个整数组成的数组 `l` 和 `r` ，后两个数组表示 `m` 组范围查询，其中第 `i` 个查询对应范围 `[l[i], r[i]]` 。所有数组的下标都是 **从 0 开始** 的。

返回 `boolean` 元素构成的答案列表 `answer` 。如果子数组 `nums[l[i]], nums[l[i]+1], ... , nums[r[i]]` 可以 **重新排列** 形成 **等差数列** ， `answer[i]` 的值就是 `true` ；否则 `answer[i]` 的值就是 `false` 。

 

 **示例 1：** 

```
输入：nums = [4,6,5,9,3,7], l = [0,0,2], r = [2,3,5]
输出：[true,false,true]
解释：
第 0 个查询，对应子数组 [4,6,5] 。可以重新排列为等差数列 [6,5,4] 。
第 1 个查询，对应子数组 [4,6,5,9] 。无法重新排列形成等差数列。
第 2 个查询，对应子数组 [5,9,3,7] 。可以重新排列为等差数列 [3,5,7,9] 。
```
 **示例 2：** 

```
输入：nums = [-12,-9,-3,-12,-6,15,20,-25,-20,-15,-10], l = [0,1,6,4,8,7], r = [4,4,9,7,9,10]
输出：[false,true,false,false,true,true]

```
 

 **提示：** 
-  `n == nums.length` 
-  `m == l.length` 
-  `m == r.length` 
-  `2 <= n <= 500` 
-  `1 <= m <= 500` 
-  `0 <= l[i] < r[i] < n` 
-  `-10^5 <= nums[i] <= 10^5` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 1631.最小体力消耗路径
[https://leetcode-cn.com/problems/path-with-minimum-effort](https://leetcode-cn.com/problems/path-with-minimum-effort) 
## 原题
你准备参加一场远足活动。给你一个二维  `rows x columns`  的地图  `heights`  ，其中  `heights[row][col]`  表示格子  `(row, col)`  的高度。一开始你在最左上角的格子  `(0, 0)`  ，且你希望去最右下角的格子  `(rows-1, columns-1)`  （注意下标从 **0** 开始编号）。你每次可以往 **上** ， **下** ， **左** ， **右**  四个方向之一移动，你想要找到耗费 **体力** 最小的一条路径。

一条路径耗费的 **体力值**  是路径上相邻格子之间 **高度差绝对值**  的 **最大值**  决定的。

请你返回从左上角走到右下角的最小 ** 体力消耗值**  。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/ex1.png" style="width: 300px; height: 300px;" />

```

输入：heights = [[1,2,2],[3,8,2],[5,3,5]]
输出：2
解释：路径 [1,3,5,3,5] 连续格子的差值绝对值最大为 2 。
这条路径比路径 [1,2,2,2,5] 更优，因为另一条路径差值最大值为 3 。

```
 **示例 2：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/ex2.png" style="width: 300px; height: 300px;" />

```

输入：heights = [[1,2,3],[3,8,4],[5,3,5]]
输出：1
解释：路径 [1,2,3,4,5] 的相邻格子差值绝对值最大为 1 ，比路径 [1,3,5,3,5] 更优。

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/ex3.png" style="width: 300px; height: 300px;" />
```

输入：heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
输出：0
解释：上图所示路径不需要消耗任何体力。

```
 

 **提示：** 
-  `rows == heights.length` 
-  `columns == heights[i].length` 
-  `1 <= rows, columns <= 100` 
-  `1 <= heights[i][j] <= 10^6` 
 
**标签**
`深度优先搜索` `广度优先搜索` `并查集` `数组` `二分查找` `矩阵` `堆（优先队列）` 


## 
```python

```
>
# 1632.矩阵转换后的秩
[https://leetcode-cn.com/problems/rank-transform-of-a-matrix](https://leetcode-cn.com/problems/rank-transform-of-a-matrix) 
## 原题
给你一个  `m x n`  的矩阵 `matrix`  ，请你返回一个新的矩阵 * * `answer`  ，其中 * * `answer[row][col]`  是  `matrix[row][col]`  的秩。

每个元素的 <b>秩</b> 是一个整数，表示这个元素相对于其他元素的大小关系，它按照如下规则计算：
- 秩是从 1 开始的一个整数。
- 如果两个元素  `p` 和  `q`  在 **同一行**  或者 **同一列**  ，那么：
	
- 如果  `p < q` ，那么  `rank(p) < rank(q)` 
- 如果  `p == q`  ，那么  `rank(p) == rank(q)` 
- 如果  `p > q`  ，那么  `rank(p) > rank(q)` 
	
	
- <b>秩</b> 需要越 **小**  越好。
题目保证按照上面规则  `answer`  数组是唯一的。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/rank1.jpg" style="width: 442px; height: 162px;" />
```

输入：matrix = [[1,2],[3,4]]
输出：[[1,2],[2,3]]
解释：
matrix[0][0] 的秩为 1 ，因为它是所在行和列的最小整数。
matrix[0][1] 的秩为 2 ，因为 matrix[0][1] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
matrix[1][0] 的秩为 2 ，因为 matrix[1][0] > matrix[0][0] 且 matrix[0][0] 的秩为 1 。
matrix[1][1] 的秩为 3 ，因为 matrix[1][1] > matrix[0][1]， matrix[1][1] > matrix[1][0] 且 matrix[0][1] 和 matrix[1][0] 的秩都为 2 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/rank2.jpg" style="width: 442px; height: 162px;" />
```

输入：matrix = [[7,7],[7,7]]
输出：[[1,1],[1,1]]

```
 **示例 3：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/rank3.jpg" style="width: 601px; height: 322px;" />
```

输入：matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
输出：[[4,2,3],[1,3,4],[5,1,6],[1,3,4]]

```
 **示例 4：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/25/rank4.jpg" style="width: 601px; height: 242px;" />
```

输入：matrix = [[7,3,6],[1,4,5],[9,8,2]]
输出：[[5,1,4],[1,2,3],[6,3,1]]

```
 

 **提示：** 
-  `m == matrix.length` 
-  `n == matrix[i].length` 
-  `1 <= m, n <= 500` 
-  `-10^9 <= matrix[row][col] <= 10^9` 
 
**标签**
`贪心` `并查集` `图` `拓扑排序` `数组` `矩阵` 


## 
```python

```
>
# 1633.各赛事的用户注册率
[https://leetcode-cn.com/problems/percentage-of-users-attended-a-contest](https://leetcode-cn.com/problems/percentage-of-users-attended-a-contest) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1634.求两个多项式链表的和
[https://leetcode-cn.com/problems/add-two-polynomials-represented-as-linked-lists](https://leetcode-cn.com/problems/add-two-polynomials-represented-as-linked-lists) 
## 原题

 
**标签**
`链表` `数学` `双指针` 


## 
```python

```
>
# 1635.Hopper 公司查询 I
[https://leetcode-cn.com/problems/hopper-company-queries-i](https://leetcode-cn.com/problems/hopper-company-queries-i) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1636.按照频率将数组升序排序
[https://leetcode-cn.com/problems/sort-array-by-increasing-frequency](https://leetcode-cn.com/problems/sort-array-by-increasing-frequency) 
## 原题
给你一个整数数组  `nums`  ，请你将数组按照每个值的频率 **升序** 排序。如果有多个值的频率相同，请你按照数值本身将它们 **降序** 排序。 

请你返回排序后的数组。

 

 **示例 1：** 

```
输入：nums = [1,1,2,2,2,3]
输出：[3,1,1,2,2,2]
解释：'3' 频率为 1，'1' 频率为 2，'2' 频率为 3 。

```
 **示例 2：** 

```
输入：nums = [2,3,1,3,2]
输出：[1,3,3,2,2]
解释：'2' 和 '3' 频率都为 2 ，所以它们之间按照数值本身降序排序。

```
 **示例 3：** 

```
输入：nums = [-1,1,-6,4,5,-6,1,4,1]
输出：[5,-1,4,4,-6,-6,1,1,1]
```
 

 **提示：** 
-  `1 <= nums.length <= 100` 
-  `-100 <= nums[i] <= 100` 
 
**标签**
`数组` `哈希表` `排序` 


## 
```python

```
>
# 1637.两点之间不包含任何点的最宽垂直面积
[https://leetcode-cn.com/problems/widest-vertical-area-between-two-points-containing-no-points](https://leetcode-cn.com/problems/widest-vertical-area-between-two-points-containing-no-points) 
## 原题
给你  `n`  个二维平面上的点 `points` ，其中  `points[i] = [x<sub>i</sub>, y<sub>i</sub>]`  ，请你返回两点之间内部不包含任何点的  **最宽垂直面积**  的宽度。

 **垂直面积** 的定义是固定宽度，而 y 轴上无限延伸的一块区域（也就是高度为无穷大）。 **最宽垂直面积**  为宽度最大的一个垂直面积。

请注意，垂直区域  **边上**  的点  **不在**  区域内。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/31/points3.png" style="width: 276px; height: 371px;" />​
```

输入：points = [[8,7],[9,9],[7,4],[9,7]]
输出：1
解释：红色区域和蓝色区域都是最优区域。

```
 **示例 2：** 

```

输入：points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
输出：3

```
 

 **提示：** 
-  `n == points.length` 
-  `2 <= n <= 10^5` 
-  `points[i].length == 2` 
-  `0 <= x<sub>i</sub>, y<sub>i</sub> <= 10^9` 
 
**标签**
`数组` `排序` 


## 
```python

```
>
# 1638.统计只差一个字符的子串数目
[https://leetcode-cn.com/problems/count-substrings-that-differ-by-one-character](https://leetcode-cn.com/problems/count-substrings-that-differ-by-one-character) 
## 原题
给你两个字符串  `s` 和  `t`  ，请你找出 `s`  中的非空子串的数目，这些子串满足替换 **一个不同字符**  以后，是 `t`  串的子串。换言之，请你找到 `s`  和 `t`  串中 **恰好**  只有一个字符不同的子字符串对的数目。

比方说，  `" **compute** r"` 和  `" **computa** tion"` 加粗部分只有一个字符不同：  `'e'` / `'a'`  ，所以这一对子字符串会给答案加 1 。

请你返回满足上述条件的不同子字符串对数目。

一个 **子字符串**  是一个字符串中连续的字符。

 

 **示例 1：** 

```

输入：s = "aba", t = "baba"
输出：6
解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
加粗部分分别表示 s 和 t 串选出来的子字符串。

```

 **示例 2：** 

```

输入：s = "ab", t = "bb"
输出：3
解释：以下为只相差 1 个字符的 s 和 t 串的子字符串对：
("ab", "bb")
("ab", "bb")
("ab", "bb")
加粗部分分别表示 s 和 t 串选出来的子字符串。

```

 **示例 3：** 

```

输入：s = "a", t = "a"
输出：0

```
 **示例 4：** 

```

输入：s = "abe", t = "bbc"
输出：10

```
 

 **提示：** 
-  `1 <= s.length, t.length <= 100` 
-  `s` 和  `t`  都只包含小写英文字母。
 
**标签**
`哈希表` `字符串` `动态规划` 


## 
```python

```
>
# 1639.通过给定词典构造目标字符串的方案数
[https://leetcode-cn.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary](https://leetcode-cn.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary) 
## 原题
给你一个字符串列表 `words`  和一个目标字符串  `target` 。 `words` 中所有字符串都  **长度相同**   。

你的目标是使用给定的 `words`  字符串列表按照下述规则构造  `target`  ：
- 从左到右依次构造  `target`  的每一个字符。
- 为了得到  `target` 第  `i`  个字符（下标从 **0**  开始），当  `target[i] = words[j][k]`  时，你可以使用  `words`  列表中第 `j`  个字符串的第 `k`  个字符。
- 一旦你使用了 `words`  中第 `j`  个字符串的第 `k`  个字符，你不能再使用 `words`  字符串列表中任意单词的第 `x`  个字符（ `x <= k` ）。也就是说，所有单词下标小于等于 `k`  的字符都不能再被使用。
- 请你重复此过程直到得到目标字符串  `target`  。
 **请注意** ， 在构造目标字符串的过程中，你可以按照上述规定使用 `words`  列表中 **同一个字符串**  的 **多个字符**  。

请你返回使用 `words`  构造 `target`  的方案数。由于答案可能会很大，请对 `10^9 + 7`   **取余**  后返回。

（译者注：此题目求的是有多少个不同的 `k`  序列，详情请见示例。）

 

 **示例 1：** 

```

输入：words = ["acca","bbbb","caca"], target = "aba"
输出：6
解释：总共有 6 种方法构造目标串。
"aba" -> 下标为 0 ("acca")，下标为 1 ("bbbb")，下标为 3 ("caca")
"aba" -> 下标为 0 ("acca")，下标为 2 ("bbbb")，下标为 3 ("caca")
"aba" -> 下标为 0 ("acca")，下标为 1 ("bbbb")，下标为 3 ("acca")
"aba" -> 下标为 0 ("acca")，下标为 2 ("bbbb")，下标为 3 ("acca")
"aba" -> 下标为 1 ("caca")，下标为 2 ("bbbb")，下标为 3 ("acca")
"aba" -> 下标为 1 ("caca")，下标为 2 ("bbbb")，下标为 3 ("caca")

```
 **示例 2：** 

```

输入：words = ["abba","baab"], target = "bab"
输出：4
解释：总共有 4 种不同形成 target 的方法。
"bab" -> 下标为 0 ("baab")，下标为 1 ("baab")，下标为 2 ("abba")
"bab" -> 下标为 0 ("baab")，下标为 1 ("baab")，下标为 3 ("baab")
"bab" -> 下标为 0 ("baab")，下标为 2 ("baab")，下标为 3 ("baab")
"bab" -> 下标为 1 ("abba")，下标为 2 ("baab")，下标为 3 ("baab")

```
 **示例 3：** 

```

输入：words = ["abcd"], target = "abcd"
输出：1

```
 **示例 4：** 

```

输入：words = ["abab","baba","abba","baab"], target = "abba"
输出：16

```
 

 **提示：** 
-  `1 <= words.length <= 1000` 
-  `1 <= words[i].length <= 1000` 
-  `words`  中所有单词长度相同。
-  `1 <= target.length <= 1000` 
-  `words[i]`  和  `target`  都仅包含小写英文字母。
 
**标签**
`数组` `字符串` `动态规划` 


## 
```python

```
>
# 1640.能否连接形成数组
[https://leetcode-cn.com/problems/check-array-formation-through-concatenation](https://leetcode-cn.com/problems/check-array-formation-through-concatenation) 
## 原题
给你一个整数数组 `arr` ，数组中的每个整数 **互不相同** 。另有一个由整数数组构成的数组 `pieces` ，其中的整数也 **互不相同** 。请你以 **任意顺序** 连接 `pieces` 中的数组以形成 `arr` 。但是， **不允许** 对每个数组 `pieces[i]` 中的整数重新排序。

如果可以连接 `pieces` 中的数组形成 `arr` ，返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：arr = [85], pieces = [[85]]
输出：true

```
 **示例 2：** 

```

输入：arr = [15,88], pieces = [[88],[15]]
输出：true
解释：依次连接 [15] 和 [88]

```
 **示例 3：** 

```

输入：arr = [49,18,16], pieces = [[16,18,49]]
输出：false
解释：即便数字相符，也不能重新排列 pieces[0]

```
 **示例 4：** 

```

输入：arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
输出：true
解释：依次连接 [91]、[4,64] 和 [78]
```
 **示例 5：** 

```

输入：arr = [1,3,5,7], pieces = [[2,4,6,8]]
输出：false

```
 

 **提示：** 
-  `1 <= pieces.length <= arr.length <= 100` 
-  `sum(pieces[i].length) == arr.length` 
-  `1 <= pieces[i].length <= arr.length` 
-  `1 <= arr[i], pieces[i][j] <= 100` 
-  `arr` 中的整数 **互不相同** 
-  `pieces` 中的整数 **互不相同** （也就是说，如果将 `pieces` 扁平化成一维数组，数组中的所有整数互不相同）
 
**标签**
`数组` `哈希表` 


## 
```python

```
>
# 1641.统计字典序元音字符串的数目
[https://leetcode-cn.com/problems/count-sorted-vowel-strings](https://leetcode-cn.com/problems/count-sorted-vowel-strings) 
## 原题
给你一个整数 `n` ，请返回长度为 `n` 、仅由元音 ( `a` , `e` , `i` , `o` , `u` ) 组成且按 **字典序排列** 的字符串数量。

字符串 `s` 按 **字典序排列** 需要满足：对于所有有效的 `i` ， `s[i]` 在字母表中的位置总是与 `s[i+1]` 相同或在 `s[i+1]` 之前。

 

 **示例 1：** 

```

输入：n = 1
输出：5
解释：仅由元音组成的 5 个字典序字符串为 ["a","e","i","o","u"]

```
 **示例 2：** 

```

输入：n = 2
输出：15
解释：仅由元音组成的 15 个字典序字符串为
["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"]
注意，"ea" 不是符合题意的字符串，因为 'e' 在字母表中的位置比 'a' 靠后

```
 **示例 3：** 

```

输入：n = 33
输出：66045

```
 

 **提示：** 
-  `1 <= n <= 50`  
 
**标签**
`动态规划` 


## 
```python

```
>
# 1642.可以到达的最远建筑
[https://leetcode-cn.com/problems/furthest-building-you-can-reach](https://leetcode-cn.com/problems/furthest-building-you-can-reach) 
## 原题
给你一个整数数组 `heights` ，表示建筑物的高度。另有一些砖块 `bricks` 和梯子 `ladders` 。

你从建筑物 `0` 开始旅程，不断向后面的建筑物移动，期间可能会用到砖块或梯子。

当从建筑物 `i` 移动到建筑物 `i+1` （下标 **从 0 开始** ）时：
- 如果当前建筑物的高度 **大于或等于** 下一建筑物的高度，则不需要梯子或砖块
- 如果当前建筑的高度 **小于** 下一个建筑的高度，您可以使用 **一架梯子** 或 ** `(h[i+1] - h[i])` 个砖块** 

如果以最佳方式使用给定的梯子和砖块，返回你可以到达的最远建筑物的下标（下标 **从 0 开始** ）。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/10/31/q4.gif" style="width: 562px; height: 561px;" />
```

输入：heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1
输出：4
解释：从建筑物 0 出发，你可以按此方案完成旅程：
- 不使用砖块或梯子到达建筑物 1 ，因为 4 >= 2
- 使用 5 个砖块到达建筑物 2 。你必须使用砖块或梯子，因为 2 = 6
- 使用唯一的梯子到达建筑物 4 。你必须使用砖块或梯子，因为 6 < 9
无法越过建筑物 4 ，因为没有更多砖块或梯子。

```
 **示例 2：** 

```

输入：heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2
输出：7

```
 **示例 3：** 

```

输入：heights = [14,3,19,3], bricks = 17, ladders = 0
输出：3

```
 

 **提示：** 
-  `1 <= heights.length <= 10^5` 
-  `1 <= heights[i] <= 10^6` 
-  `0 <= bricks <= 10^9` 
-  `0 <= ladders <= heights.length` 
 
**标签**
`贪心` `数组` `堆（优先队列）` 


## 
```python

```
>
# 1643.第 K 条最小指令
[https://leetcode-cn.com/problems/kth-smallest-instructions](https://leetcode-cn.com/problems/kth-smallest-instructions) 
## 原题
Bob 站在单元格 `(0, 0)` ，想要前往目的地 `destination` ： `(row, column)` 。他只能向 **右** 或向 **下** 走。你可以为 Bob 提供导航 **指令** 来帮助他到达目的地 `destination` 。

 **指令** 用字符串表示，其中每个字符：
-  `'H'` ，意味着水平向右移动
-  `'V'` ，意味着竖直向下移动
能够为 Bob 导航到目的地 `destination` 的指令可以有多种，例如，如果目的地 `destination` 是 `(2, 3)` ， `"HHHVV"` 和 `"HVHVH"` 都是有效 **指令** 。
然而，Bob 很挑剔。因为他的幸运数字是 `k` ，他想要遵循 **按字典序排列后的第 `k` 条最小指令** 的导航前往目的地 `destination` 。 `k`   的编号 **从 1 开始** 。

给你一个整数数组 `destination` 和一个整数 `k` ，请你返回可以为Bob提供前往目的地  `destination` 导航的 **按字典序排列后的第 `k` 条最小指令** 。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/01/ex1.png" style="width: 300px;" />

```

输入：destination = [2,3], k = 1
输出："HHHVV"
解释：能前往 (2, 3) 的所有导航指令 按字典序排列后 如下所示：
["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"].

```
 **示例 2：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/01/ex2.png" style="width: 300px; height: 229px;" />** 

```

输入：destination = [2,3], k = 2
输出："HHVHV"

```
 **示例 3：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/01/ex3.png" style="width: 300px; height: 229px;" />** 

```

输入：destination = [2,3], k = 3
输出："HHVVH"

```
 

 **提示：** 
-  `destination.length == 2` 
-  `1 <= row, column <= 15` 
-  `1 <= k <= nCr(row + column, row)` ，其中 `nCr(a, b)` 表示组合数，即从 `a` 个物品中选 `b` 个物品的不同方案数。
 
**标签**
`数组` `数学` `动态规划` `组合数学` 


## 
```python

```
>
# 1644.二叉树的最近公共祖先 II
[https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-ii](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-ii) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1646.获取生成数组中的最大值
[https://leetcode-cn.com/problems/get-maximum-in-generated-array](https://leetcode-cn.com/problems/get-maximum-in-generated-array) 
## 原题
给你一个整数 `n` 。按下述规则生成一个长度为 `n + 1` 的数组 `nums` ：
-  `nums[0] = 0` 
-  `nums[1] = 1` 
- 当 `2 <= 2 * i <= n` 时， `nums[2 * i] = nums[i]` 
- 当 `2 <= 2 * i + 1 <= n` 时， `nums[2 * i + 1] = nums[i] + nums[i + 1]` 
返回生成数组 `nums` 中的 **最大** 值。

 

 **示例 1：** 

```

输入：n = 7
输出：3
解释：根据规则：
  nums[0] = 0
  nums[1] = 1
  nums[(1 * 2) = 2] = nums[1] = 1
  nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
  nums[(2 * 2) = 4] = nums[2] = 1
  nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
  nums[(3 * 2) = 6] = nums[3] = 2
  nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
因此，nums = [0,1,1,2,1,3,2,3]，最大值 3

```
 **示例 2：** 

```

输入：n = 2
输出：1
解释：根据规则，nums[0]、nums[1] 和 nums[2] 之中的最大值是 1

```
 **示例 3：** 

```

输入：n = 3
输出：2
解释：根据规则，nums[0]、nums[1]、nums[2] 和 nums[3] 之中的最大值是 2

```
 

 **提示：** 
-  `0 <= n <= 100` 
 
**标签**
`数组` `动态规划` `模拟` 


## 
```python

```
>
# 1647.字符频次唯一的最小删除次数
[https://leetcode-cn.com/problems/minimum-deletions-to-make-character-frequencies-unique](https://leetcode-cn.com/problems/minimum-deletions-to-make-character-frequencies-unique) 
## 原题
如果字符串 `s` 中 **不存在** 两个不同字符 **频次** 相同的情况，就称 `s` 是 **优质字符串** 。

给你一个字符串 `s` ，返回使 `s` 成为 **优质字符串** 需要删除的 **最小** 字符数。

字符串中字符的 **频次** 是该字符在字符串中的出现次数。例如，在字符串 `"aab"` 中， `'a'` 的频次是 `2` ，而 `'b'` 的频次是 `1` 。

 

 **示例 1：** 

```

输入：s = "aab"
输出：0
解释：s 已经是优质字符串。

```
 **示例 2：** 

```

输入：s = "aaabbbcc"
输出：2
解释：可以删除两个 'b' , 得到优质字符串 "aaabcc" 。
另一种方式是删除一个 'b' 和一个 'c' ，得到优质字符串 "aaabbc" 。
```
 **示例 3：** 

```

输入：s = "ceabaacb"
输出：2
解释：可以删除两个 'c' 得到优质字符串 "eabaab" 。
注意，只需要关注结果字符串中仍然存在的字符。（即，频次为 0 的字符会忽略不计。）

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s` 仅含小写英文字母
 
**标签**
`贪心` `字符串` `排序` 


## 
```python

```
>
# 1648.销售价值减少的颜色球
[https://leetcode-cn.com/problems/sell-diminishing-valued-colored-balls](https://leetcode-cn.com/problems/sell-diminishing-valued-colored-balls) 
## 原题
你有一些球的库存  `inventory`  ，里面包含着不同颜色的球。一个顾客想要  **任意颜色** 总数为  `orders`  的球。

这位顾客有一种特殊的方式衡量球的价值：每个球的价值是目前剩下的  **同色球**  的数目。比方说还剩下  `6`  个黄球，那么顾客买第一个黄球的时候该黄球的价值为  `6`  。这笔交易以后，只剩下  `5`  个黄球了，所以下一个黄球的价值为  `5`  （也就是球的价值随着顾客购买同色球是递减的）

给你整数数组  `inventory`  ，其中  `inventory[i]`  表示第  `i`  种颜色球一开始的数目。同时给你整数  `orders`  ，表示顾客总共想买的球数目。你可以按照 **任意顺序**  卖球。

请你返回卖了 `orders`  个球以后 **最大**  总价值之和。由于答案可能会很大，请你返回答案对 `10^9 + 7`   **取余数**  的结果。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/08/jj.gif" style="width: 480px; height: 270px;" />
```

输入：inventory = [2,5], orders = 4
输出：14
解释：卖 1 个第一种颜色的球（价值为 2 )，卖 3 个第二种颜色的球（价值为 5 + 4 + 3）。
最大总和为 2 + 5 + 4 + 3 = 14 。

```
 **示例 2：** 

```

输入：inventory = [3,5], orders = 6
输出：19
解释：卖 2 个第一种颜色的球（价值为 3 + 2），卖 4 个第二种颜色的球（价值为 5 + 4 + 3 + 2）。
最大总和为 3 + 2 + 5 + 4 + 3 + 2 = 19 。

```
 **示例 3：** 

```

输入：inventory = [2,8,4,10,6], orders = 20
输出：110

```
 **示例 4：** 

```

输入：inventory = [1000000000], orders = 1000000000
输出：21
解释：卖 1000000000 次第一种颜色的球，总价值为 500000000500000000 。 500000000500000000 对 10^9 + 7 取余为 21 。

```
 

 **提示：** 
-  `1 <= inventory.length <= 10^5` 
-  `1 <= inventory[i] <= 10^9` 
-  `1 <= orders <= min(sum(inventory[i]), 10^9)` 
 
**标签**
`贪心` `数组` `数学` `二分查找` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1649.通过指令创建有序数组
[https://leetcode-cn.com/problems/create-sorted-array-through-instructions](https://leetcode-cn.com/problems/create-sorted-array-through-instructions) 
## 原题
给你一个整数数组  `instructions`  ，你需要根据  `instructions`  中的元素创建一个有序数组。一开始你有一个空的数组  `nums`  ，你需要  **从左到右**  遍历  `instructions`  中的元素，将它们依次插入  `nums`  数组中。每一次插入操作的  **代价**  是以下两者的 **较小值**  ：
-  `nums`  中 **严格小于 **   `instructions[i]`  的数字数目。
-  `nums`  中 **严格大于 **   `instructions[i]`  的数字数目。
比方说，如果要将  `3` 插入到  `nums = [1,2,3,5]`  ，那么插入操作的  **代价**  为  `min(2, 1)` (元素  `1`  和   `2`  小于  `3`  ，元素  `5`  大于  `3`  ），插入后  `nums` 变成  `[1,2,3,3,5]`  。

请你返回将  `instructions`  中所有元素依次插入  `nums`  后的 **总最小代价 ** 。由于答案会很大，请将它对  `10^9 + 7`  <b>取余</b> 后返回。

 

 **示例 1：** 

```
输入：instructions = [1,5,6,2]
输出：1
解释：一开始 nums = [] 。
插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
插入 5 ，代价为 min(1, 0) = 0 ，现在 nums = [1,5] 。
插入 6 ，代价为 min(2, 0) = 0 ，现在 nums = [1,5,6] 。
插入 2 ，代价为 min(1, 2) = 1 ，现在 nums = [1,2,5,6] 。
总代价为 0 + 0 + 0 + 1 = 1 。
```
 **示例 2:** 

```
输入：instructions = [1,2,3,6,5,4]
输出：3
解释：一开始 nums = [] 。
插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
插入 2 ，代价为 min(1, 0) = 0 ，现在 nums = [1,2] 。
插入 3 ，代价为 min(2, 0) = 0 ，现在 nums = [1,2,3] 。
插入 6 ，代价为 min(3, 0) = 0 ，现在 nums = [1,2,3,6] 。
插入 5 ，代价为 min(3, 1) = 1 ，现在 nums = [1,2,3,5,6] 。
插入 4 ，代价为 min(3, 2) = 2 ，现在 nums = [1,2,3,4,5,6] 。
总代价为 0 + 0 + 0 + 0 + 1 + 2 = 3 。

```
 **示例 3：** 

```
输入：instructions = [1,3,3,3,2,4,2,1,2]
输出：4
解释：一开始 nums = [] 。
插入 1 ，代价为 min(0, 0) = 0 ，现在 nums = [1] 。
插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3] 。
插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3] 。
插入 3 ，代价为 min(1, 0) = 0 ，现在 nums = [1,3,3,3] 。
插入 2 ，代价为 min(1, 3) = 1 ，现在 nums = [1,2,3,3,3] 。
插入 4 ，代价为 min(5, 0) = 0 ，现在 nums = [1,2,3,3,3,4] 。
​​​​​插入 2 ，代价为 min(1, 4) = 1 ，现在 nums = [1,2,2,3,3,3,4] 。
插入 1 ，代价为 min(0, 6) = 0 ，现在 nums = [1,1,2,2,3,3,3,4] 。
插入 2 ，代价为 min(2, 4) = 2 ，现在 nums = [1,1,2,2,2,3,3,3,4] 。
总代价为 0 + 0 + 0 + 0 + 1 + 0 + 1 + 0 + 2 = 4 。

```
 

 **提示：** 
-  `1 <= instructions.length <= 10^5` 
-  `1 <= instructions[i] <= 10^5` 
 
**标签**
`树状数组` `线段树` `数组` `二分查找` `分治` `有序集合` `归并排序` 


## 
```python

```
>
# 1650.二叉树的最近公共祖先 III
[https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-iii](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-iii) 
## 原题

 
**标签**
`树` `哈希表` `二叉树` 


## 
```python

```
>
# 1652.拆炸弹
[https://leetcode-cn.com/problems/defuse-the-bomb](https://leetcode-cn.com/problems/defuse-the-bomb) 
## 原题
你有一个炸弹需要拆除，时间紧迫！你的情报员会给你一个长度为  `n`  的  **循环**  数组  `code`  以及一个密钥  `k`  。

为了获得正确的密码，你需要替换掉每一个数字。所有数字会  **同时**  被替换。
- 如果  `k > 0`  ，将第  `i`  个数字用 **接下来**   `k`  个数字之和替换。
- 如果  `k < 0`  ，将第  `i`  个数字用 **之前**   `k`  个数字之和替换。
- 如果  `k == 0`  ，将第  `i`  个数字用  `0`  替换。
由于  `code`  是循环的，  `code[n-1]`  下一个元素是  `code[0]`  ，且  `code[0]`  前一个元素是  `code[n-1]`  。

给你 **循环**  数组  `code`  和整数密钥  `k`  ，请你返回解密后的结果来拆除炸弹！

 

 **示例 1：** 

```

输入：code = [5,7,1,4], k = 3
输出：[12,10,16,13]
解释：每个数字都被接下来 3 个数字之和替换。解密后的密码为 [7+1+4, 1+4+5, 4+5+7, 5+7+1]。注意到数组是循环连接的。

```
 **示例 2：** 

```

输入：code = [1,2,3,4], k = 0
输出：[0,0,0,0]
解释：当 k 为 0 时，所有数字都被 0 替换。

```
 **示例 3：** 

```

输入：code = [2,4,9,3], k = -2
输出：[12,5,6,13]
解释：解密后的密码为 [3+9, 2+3, 4+2, 9+4] 。注意到数组是循环连接的。如果 k 是负数，那么和为 之前 的数字。

```
 

 **提示：** 
-  `n == code.length` 
-  `1 <= n <= 100` 
-  `1 <= code[i] <= 100` 
-  `-(n - 1) <= k <= n - 1` 
 
**标签**
`数组` 


## 
```python

```
>
# 1653.使字符串平衡的最少删除次数
[https://leetcode-cn.com/problems/minimum-deletions-to-make-string-balanced](https://leetcode-cn.com/problems/minimum-deletions-to-make-string-balanced) 
## 原题
给你一个字符串  `s`  ，它仅包含字符  `'a'` 和  `'b'` ​​​​ 。

你可以删除  `s`  中任意数目的字符，使得  `s` **平衡**  。我们称  `s`   **平衡的**  当不存在下标对  `(i,j)`  满足  `i < j` 且  `s[i] = 'b'`  同时  `s[j]= 'a'`  。

请你返回使 `s`   **平衡**  的 **最少**  删除次数。

 

 **示例 1：** 

```

输入：s = "aababbab"
输出：2
解释：你可以选择以下任意一种方案：
下标从 0 开始，删除第 2 和第 6 个字符（"aababbab" -> "aaabbb"），
下标从 0 开始，删除第 3 和第 6 个字符（"aababbab" -> "aabbbb"）。

```
 **示例 2：** 

```

输入：s = "bbaaaaabb"
输出：2
解释：唯一的最优解是删除最前面两个字符。

```
 

 **提示：** 
-  `1 <= s.length <= 10^5` 
-  `s[i]`  要么是  `'a'` 要么是  `'b'` ​ ** ** 。​
 
**标签**
`栈` `字符串` `动态规划` 


## 
```python

```
>
# 1654.到家的最少跳跃次数
[https://leetcode-cn.com/problems/minimum-jumps-to-reach-home](https://leetcode-cn.com/problems/minimum-jumps-to-reach-home) 
## 原题
有一只跳蚤的家在数轴上的位置  `x`  处。请你帮助它从位置  `0`  出发，到达它的家。

跳蚤跳跃的规则如下：
- 它可以 **往前** 跳恰好 `a`  个位置（即往右跳）。
- 它可以 **往后**  跳恰好 `b`  个位置（即往左跳）。
- 它不能 **连续** 往后跳 `2` 次。
- 它不能跳到任何  `forbidden`  数组中的位置。
跳蚤可以往前跳 **超过**  它的家的位置，但是它 **不能跳到负整数**  的位置。

给你一个整数数组  `forbidden`  ，其中  `forbidden[i]`  是跳蚤不能跳到的位置，同时给你整数  `a` ，  `b`  和  `x`  ，请你返回跳蚤到家的最少跳跃次数。如果没有恰好到达 `x`  的可行方案，请你返回 `-1` 。

 

 **示例 1：** 

```

输入：forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
输出：3
解释：往前跳 3 次（0 -> 3 -> 6 -> 9），跳蚤就到家了。

```
 **示例 2：** 

```

输入：forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
输出：-1

```
 **示例 3：** 

```

输入：forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
输出：2
解释：往前跳一次（0 -> 16），然后往回跳一次（16 -> 7），跳蚤就到家了。

```
 

 **提示：** 
-  `1 <= forbidden.length <= 1000` 
-  `1 <= a, b, forbidden[i] <= 2000` 
-  `0 <= x <= 2000` 
-  `forbidden`  中所有位置互不相同。
- 位置  `x`  不在 `forbidden`  中。
 
**标签**
`广度优先搜索` `数组` `动态规划` 


## 
```python

```
>
# 1655.分配重复整数
[https://leetcode-cn.com/problems/distribute-repeating-integers](https://leetcode-cn.com/problems/distribute-repeating-integers) 
## 原题
给你一个长度为  `n`  的整数数组  `nums`  ，这个数组中至多有  `50`  个不同的值。同时你有 `m`  个顾客的订单 `quantity`  ，其中，整数  `quantity[i]`  是第  `i`  位顾客订单的数目。请你判断是否能将 `nums`  中的整数分配给这些顾客，且满足：
- 第  `i`  位顾客 **恰好 ** 有  `quantity[i]`  个整数。
- 第  `i`  位顾客拿到的整数都是 **相同的**  。
- 每位顾客都满足上述两个要求。
如果你可以分配 `nums`  中的整数满足上面的要求，那么请返回  `true`  ，否则返回 `false`  。

 

 **示例 1：** 

```
输入：nums = [1,2,3,4], quantity = [2]
输出：false
解释：第 0 位顾客没办法得到两个相同的整数。

```
 **示例 2：** 

```
输入：nums = [1,2,3,3], quantity = [2]
输出：true
解释：第 0 位顾客得到 [3,3] 。整数 [1,2] 都没有被使用。

```
 **示例 3：** 

```
输入：nums = [1,1,2,2], quantity = [2,2]
输出：true
解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [2,2] 。

```
 **示例 4：** 

```
输入：nums = [1,1,2,3], quantity = [2,2]
输出：false
解释：尽管第 0 位顾客可以得到 [1,1] ，第 1 位顾客没法得到 2 个一样的整数。
```
 **示例 5：** 

```
输入：nums = [1,1,1,1,1], quantity = [2,3]
输出：true
解释：第 0 位顾客得到 [1,1] ，第 1 位顾客得到 [1,1,1] 。

```
 

 **提示：** 
-  `n == nums.length` 
-  `1 <= n <= 10^5` 
-  `1 <= nums[i] <= 1000` 
-  `m == quantity.length` 
-  `1 <= m <= 10` 
-  `1 <= quantity[i] <= 10^5` 
-  `nums`  中至多有  `50`  个不同的数字。
 
**标签**
`位运算` `数组` `动态规划` `回溯` `状态压缩` 


## 
```python

```
>
# 1656.设计有序流
[https://leetcode-cn.com/problems/design-an-ordered-stream](https://leetcode-cn.com/problems/design-an-ordered-stream) 
## 原题
有 `n` 个 `(id, value)` 对，其中 `id` 是 `1` 到 `n` 之间的一个整数， `value` 是一个字符串。不存在 `id` 相同的两个  `(id, value)` 对。

设计一个流，以 **任意** 顺序获取 `n`  个  `(id, value)`  对，并在多次调用时 **按 `id` 递增的顺序** 返回一些值。

实现 `OrderedStream` 类：
-  `OrderedStream(int n)` 构造一个能接收 `n` 个值的流，并将当前指针 `ptr` 设为 `1` 。
-  `String[] insert(int id, String value)` 向流中存储新的 `(id, value)` 对。存储后：
	
- 如果流存储有 `id = ptr` 的 `(id, value)` 对，则找出从 `id = ptr` 开始的 **最长 id 连续递增序列** ，并 **按顺序** 返回与这些 id 关联的值的列表。然后，将 `ptr` 更新为最后那个  `id + 1`  。
- 
		否则，返回一个空列表。
		
	
	
 

 **示例：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/15/q1.gif" style="width: 682px; height: 240px;" />** 

```

输入
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
输出
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

解释
OrderedStream os= new OrderedStream(5);
os.insert(3, "ccccc"); // 插入 (3, "ccccc")，返回 []
os.insert(1, "aaaaa"); // 插入 (1, "aaaaa")，返回 ["aaaaa"]
os.insert(2, "bbbbb"); // 插入 (2, "bbbbb")，返回 ["bbbbb", "ccccc"]
os.insert(5, "eeeee"); // 插入 (5, "eeeee")，返回 []
os.insert(4, "ddddd"); // 插入 (4, "ddddd")，返回 ["ddddd", "eeeee"]

```
 

 **提示：** 
-  `1 <= n <= 1000` 
-  `1 <= id <= n` 
-  `value.length == 5` 
-  `value` 仅由小写字母组成
- 每次调用 `insert` 都会使用一个唯一的 `id` 
- 恰好调用 `n` 次 `insert` 
 
**标签**
`设计` `数组` `哈希表` `数据流` 


## 
```python

```
>
# 1657.确定两个字符串是否接近
[https://leetcode-cn.com/problems/determine-if-two-strings-are-close](https://leetcode-cn.com/problems/determine-if-two-strings-are-close) 
## 原题
如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 **接近** ：
- 操作 1：交换任意两个 **现有** 字符。

	
- 例如， `a **b** cd **e** -> a **e** cd **b**` 
	
	
- 操作 2：将一个 **现有** 字符的每次出现转换为另一个 **现有** 字符，并对另一个字符执行相同的操作。
	
- 例如， `**aa** c **abb** -> **bb** c **baa**` （所有 `a` 转化为 `b` ，而所有的 `b` 转换为 `a` ）
	
	
你可以根据需要对任意一个字符串多次使用这两种操作。

给你两个字符串， `word1` 和 `word2` 。如果 `word1` 和 `word2`  **接近** ，就返回 `true` ；否则，返回 `false` 。

 

 **示例 1：** 

```

输入：word1 = "abc", word2 = "bca"
输出：true
解释：2 次操作从 word1 获得 word2 。
执行操作 1："abc" -> "acb"
执行操作 1："acb" -> "bca"

```
 **示例 2：** 

```

输入：word1 = "a", word2 = "aa"
输出：false
解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
```
 **示例 3：** 

```

输入：word1 = "cabbba", word2 = "abbccc"
输出：true
解释：3 次操作从 word1 获得 word2 。
执行操作 1："cabbba" -> "caabbb"
执行操作 2："caabbb" -> "baaccc"
执行操作 2："baaccc" -> "abbccc"

```
 **示例 4：** 

```

输入：word1 = "cabbba", word2 = "aabbss"
输出：false
解释：不管执行多少次操作，都无法从 word1 得到 word2 ，反之亦然。
```
 

 **提示：** 
-  `1 <= word1.length, word2.length <= 10^5` 
-  `word1` 和 `word2` 仅包含小写英文字母
 
**标签**
`哈希表` `字符串` `排序` 


## 
```python

```
>
# 1658.将 x 减到 0 的最小操作数
[https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero](https://leetcode-cn.com/problems/minimum-operations-to-reduce-x-to-zero) 
## 原题
给你一个整数数组 `nums` 和一个整数 `x` 。每一次操作时，你应当移除数组 `nums` 最左边或最右边的元素，然后从 `x` 中减去该元素的值。请注意，需要 **修改** 数组以供接下来的操作使用。

如果可以将 `x`   **恰好** 减到  `0` ，返回 **最小操作数** ；否则，返回 `-1` 。

 

 **示例 1：** 

```

输入：nums = [1,1,4,2,3], x = 5
输出：2
解释：最佳解决方案是移除后两个元素，将 x 减到 0 。

```
 **示例 2：** 

```

输入：nums = [5,6,7,8,9], x = 4
输出：-1

```
 **示例 3：** 

```

输入：nums = [3,2,20,1,1,3], x = 10
输出：5
解释：最佳解决方案是移除后三个元素和前两个元素（总共 5 次操作），将 x 减到 0 。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^4` 
-  `1 <= x <= 10^9` 
 
**标签**
`数组` `哈希表` `二分查找` `前缀和` `滑动窗口` 


## 
```python

```
>
# 1659.最大化网格幸福感
[https://leetcode-cn.com/problems/maximize-grid-happiness](https://leetcode-cn.com/problems/maximize-grid-happiness) 
## 原题
给你四个整数 `m` 、 `n` 、 `introvertsCount` 和 `extrovertsCount` 。有一个 `m x n` 网格，和两种类型的人：内向的人和外向的人。总共有  `introvertsCount` 个内向的人和 `extrovertsCount` 个外向的人。

请你决定网格中应当居住多少人，并为每个人分配一个网格单元。 注意， **不必** 让所有人都生活在网格中。

每个人的 **幸福感** 计算如下：
- 内向的人 **开始** 时有 `120` 个幸福感，但每存在一个邻居（内向的或外向的）他都会 **失去**    `30` 个幸福感。
- 外向的人 **开始** 时有 `40` 个幸福感，每存在一个邻居（内向的或外向的）他都会 **得到**    `20` 个幸福感。
邻居是指居住在一个人所在单元的上、下、左、右四个直接相邻的单元中的其他人。

 **网格幸福感**  是每个人幸福感的 **总和** 。 返回 **最大可能的网格幸福感** 。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/15/grid_happiness.png" style="width: 261px; height: 121px;" />
```

输入：m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
输出：240
解释：假设网格坐标 (row, column) 从 1 开始编号。
将内向的人放置在单元 (1,1) ，将外向的人放置在单元 (1,3) 和 (2,3) 。
- 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (0 * 30)（0 位邻居）= 120
- 位于 (1,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
- 位于 (2,3) 的外向的人的幸福感：40（初始幸福感）+ (1 * 20)（1 位邻居）= 60
网格幸福感为：120 + 60 + 60 = 240
上图展示该示例对应网格中每个人的幸福感。内向的人在浅绿色单元中，而外向的人在浅紫色单元中。

```
 **示例 2：** 

```

输入：m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
输出：260
解释：将内向的人放置在单元 (1,1) 和 (3,1) ，将外向的人放置在单元 (2,1) 。
- 位于 (1,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
- 位于 (2,1) 的外向的人的幸福感：40（初始幸福感）+ (2 * 20)（2 位邻居）= 80
- 位于 (3,1) 的内向的人的幸福感：120（初始幸福感）- (1 * 30)（1 位邻居）= 90
网格幸福感为 90 + 80 + 90 = 260

```
 **示例 3：** 

```

输入：m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
输出：240

```
 

 **提示：** 
-  `1 <= m, n <= 5` 
-  `0 <= introvertsCount, extrovertsCount <= min(m * n, 6)` 
 
**标签**
`位运算` `记忆化搜索` `动态规划` `状态压缩` 


## 
```python

```
>
# 1660.纠正二叉树
[https://leetcode-cn.com/problems/correct-a-binary-tree](https://leetcode-cn.com/problems/correct-a-binary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` `广度优先搜索` `哈希表` `二叉树` 


## 
```python

```
>
# 1661.每台机器的进程平均运行时间
[https://leetcode-cn.com/problems/average-time-of-process-per-machine](https://leetcode-cn.com/problems/average-time-of-process-per-machine) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1662.检查两个字符串数组是否相等
[https://leetcode-cn.com/problems/check-if-two-string-arrays-are-equivalent](https://leetcode-cn.com/problems/check-if-two-string-arrays-are-equivalent) 
## 原题
给你两个字符串数组 `word1` 和 `word2` 。如果两个数组表示的字符串相同，返回 `true` ；否则，返回 `false` *。* 

 **数组表示的字符串**  是由数组中的所有元素 **按顺序** 连接形成的字符串。

 

 **示例 1：** 

```

输入：word1 = ["ab", "c"], word2 = ["a", "bc"]
输出：true
解释：
word1 表示的字符串为 "ab" + "c" -> "abc"
word2 表示的字符串为 "a" + "bc" -> "abc"
两个字符串相同，返回 true
```
 **示例 2：** 

```

输入：word1 = ["a", "cb"], word2 = ["ab", "c"]
输出：false

```
 **示例 3：** 

```

输入：word1  = ["abc", "d", "defg"], word2 = ["abcddefg"]
输出：true

```
 

 **提示：** 
-  `1 <= word1.length, word2.length <= 10^3` 
-  `1 <= word1[i].length, word2[i].length <= 10^3` 
-  `1 <= sum(word1[i].length), sum(word2[i].length) <= 10^3` 
-  `word1[i]` 和 `word2[i]` 由小写字母组成
 
**标签**
`数组` `字符串` 


## 
```python

```
>
# 1663.具有给定数值的最小字符串
[https://leetcode-cn.com/problems/smallest-string-with-a-given-numeric-value](https://leetcode-cn.com/problems/smallest-string-with-a-given-numeric-value) 
## 原题
 **小写字符** 的 **数值** 是它在字母表中的位置（从 `1` 开始），因此 `a` 的数值为 `1` ， `b` 的数值为 `2` ， `c` 的数值为 `3` ，以此类推。

字符串由若干小写字符组成， **字符串的数值** 为各字符的数值之和。例如，字符串 `"abe"` 的数值等于 `1 + 2 + 5 = 8` 。

给你两个整数 `n` 和 `k` 。返回 **长度** 等于 `n` 且 **数值** 等于 `k` 的 **字典序最小** 的字符串。

注意，如果字符串 `x` 在字典排序中位于 `y` 之前，就认为 `x` 字典序比 `y` 小，有以下两种情况：
-  `x` 是 `y` 的一个前缀；
- 如果 `i` 是  `x[i] != y[i]` 的第一个位置，且 `x[i]`  在字母表中的位置比  `y[i]`  靠前。
 

 **示例 1：** 

```

输入：n = 3, k = 27
输出："aay"
解释：字符串的数值为 1 + 1 + 25 = 27，它是数值满足要求且长度等于 3 字典序最小的字符串。
```
 **示例 2：** 

```

输入：n = 5, k = 73
输出："aaszz"

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
-  `n <= k <= 26 * n` 
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 1664.生成平衡数组的方案数
[https://leetcode-cn.com/problems/ways-to-make-a-fair-array](https://leetcode-cn.com/problems/ways-to-make-a-fair-array) 
## 原题
给你一个整数数组  `nums`  。你需要选择 **恰好**  一个下标（下标从 **0**  开始）并删除对应的元素。请注意剩下元素的下标可能会因为删除操作而发生改变。

比方说，如果  `nums = [6,1,7,4,1]`  ，那么：
- 选择删除下标 `1` ，剩下的数组为  `nums = [6,7,4,1]`  。
- 选择删除下标  `2`  ，剩下的数组为  `nums = [6,1,4,1]`  。
- 选择删除下标  `4`  ，剩下的数组为  `nums = [6,1,7,4]`  。
如果一个数组满足奇数下标元素的和与偶数下标元素的和相等，该数组就是一个 **平衡数组** 。

请你返回删除操作后，剩下的数组 * * `nums` * * 是  **平衡数组** 的  **方案数**  。

 

 **示例 1：** 

```

输入：nums = [2,1,6,4]
输出：1
解释：
删除下标 0 ：[1,6,4] -> 偶数元素下标为：1 + 4 = 5 。奇数元素下标为：6 。不平衡。
删除下标 1 ：[2,6,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：6 。平衡。
删除下标 2 ：[2,1,4] -> 偶数元素下标为：2 + 4 = 6 。奇数元素下标为：1 。不平衡。
删除下标 3 ：[2,1,6] -> 偶数元素下标为：2 + 6 = 8 。奇数元素下标为：1 。不平衡。
只有一种让剩余数组成为平衡数组的方案。

```
 **示例 2：** 

```

输入：nums = [1,1,1]
输出：3
解释：你可以删除任意元素，剩余数组都是平衡数组。

```
 **示例 3：** 

```

输入：nums = [1,2,3]
输出：0
解释：不管删除哪个元素，剩下数组都不是平衡数组。

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^4` 
 
**标签**
`数组` `动态规划` 


## 
```python

```
>
# 1665.完成所有任务的最少初始能量
[https://leetcode-cn.com/problems/minimum-initial-energy-to-finish-tasks](https://leetcode-cn.com/problems/minimum-initial-energy-to-finish-tasks) 
## 原题
给你一个任务数组  `tasks` ，其中  `tasks[i] = [actual<sub>i</sub>, minimum<sub>i</sub>]`  ：
-  `actual<sub>i</sub>`  是完成第 `i`  个任务 **需要耗费**  的实际能量。
-  `minimum<sub>i</sub>`  是开始第 `i`  个任务前需要达到的最低能量。
比方说，如果任务为  `[10, 12]`  且你当前的能量为  `11`  ，那么你不能开始这个任务。如果你当前的能量为  `13`  ，你可以完成这个任务，且完成它后剩余能量为 `3`  。

你可以按照 **任意顺序**  完成任务。

请你返回完成所有任务的 **最少**  初始能量。

 

 **示例 1：** 

```
输入：tasks = [[1,2],[2,4],[4,8]]
输出：8
解释：
一开始有 8 能量，我们按照如下顺序完成任务：
    - 完成第 3 个任务，剩余能量为 8 - 4 = 4 。
    - 完成第 2 个任务，剩余能量为 4 - 2 = 2 。
    - 完成第 1 个任务，剩余能量为 2 - 1 = 1 。
注意到尽管我们有能量剩余，但是如果一开始只有 7 能量是不能完成所有任务的，因为我们无法开始第 3 个任务。
```
 **示例 2：** 

```
输入：tasks = [[1,3],[2,4],[10,11],[10,12],[8,9]]
输出：32
解释：
一开始有 32 能量，我们按照如下顺序完成任务：
    - 完成第 1 个任务，剩余能量为 32 - 1 = 31 。
    - 完成第 2 个任务，剩余能量为 31 - 2 = 29 。
    - 完成第 3 个任务，剩余能量为 29 - 10 = 19 。
    - 完成第 4 个任务，剩余能量为 19 - 10 = 9 。
    - 完成第 5 个任务，剩余能量为 9 - 8 = 1 。
```
 **示例 3：** 

```
输入：tasks = [[1,7],[2,8],[3,9],[4,10],[5,11],[6,12]]
输出：27
解释：
一开始有 27 能量，我们按照如下顺序完成任务：
    - 完成第 5 个任务，剩余能量为 27 - 5 = 22 。
    - 完成第 2 个任务，剩余能量为 22 - 2 = 20 。
    - 完成第 3 个任务，剩余能量为 20 - 3 = 17 。
    - 完成第 1 个任务，剩余能量为 17 - 1 = 16 。
    - 完成第 4 个任务，剩余能量为 16 - 4 = 12 。
    - 完成第 6 个任务，剩余能量为 12 - 6 = 6 。

```
 

 **提示：** 
-  `1 <= tasks.length <= 10^5` 
-  `1 <= actual<sub>​i</sub> <= minimum<sub>i</sub> <= 10^4` 
 
**标签**
`贪心` `数组` `排序` 


## 
```python

```
>
# 1666.改变二叉树的根节点
[https://leetcode-cn.com/problems/change-the-root-of-a-binary-tree](https://leetcode-cn.com/problems/change-the-root-of-a-binary-tree) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1667.修复表中的名字
[https://leetcode-cn.com/problems/fix-names-in-a-table](https://leetcode-cn.com/problems/fix-names-in-a-table) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1668.最大重复子字符串
[https://leetcode-cn.com/problems/maximum-repeating-substring](https://leetcode-cn.com/problems/maximum-repeating-substring) 
## 原题
给你一个字符串  `sequence`  ，如果字符串 `word`  连续重复  `k`  次形成的字符串是  `sequence`  的一个子字符串，那么单词  `word` 的 **重复值为 `k` ** **** 。单词 `word`  的 **最** **大重复值**  是单词  `word`  在  `sequence`  中最大的重复值。如果  `word`  不是  `sequence`  的子串，那么重复值  `k`  为 `0` 。

给你一个字符串 `sequence`  和 `word`  ，请你返回 **最大重复值  `k` ** 。

 

 **示例 1：** 

```

输入：sequence = "ababc", word = "ab"
输出：2
解释："abab" 是 "ababc" 的子字符串。

```
 **示例 2：** 

```

输入：sequence = "ababc", word = "ba"
输出：1
解释："ba" 是 "ababc" 的子字符串，但 "baba" 不是 "ababc" 的子字符串。

```
 **示例 3：** 

```

输入：sequence = "ababc", word = "ac"
输出：0
解释："ac" 不是 "ababc" 的子字符串。

```
 

 **提示：** 
-  `1 <= sequence.length <= 100` 
-  `1 <= word.length <= 100` 
-  `sequence` 和  `word`  都只包含小写英文字母。
 
**标签**
`字符串` `字符串匹配` 


## 
```python

```
>
# 1669.合并两个链表
[https://leetcode-cn.com/problems/merge-in-between-linked-lists](https://leetcode-cn.com/problems/merge-in-between-linked-lists) 
## 原题
给你两个链表 `list1` 和 `list2` ，它们包含的元素分别为 `n` 个和 `m` 个。

请你将 `list1` 中下标从 `a` 到 `b` 的全部节点都删除，并将 `list2` 接在被删除节点的位置。

下图中蓝色边和节点展示了操作后的结果：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/28/fig1.png" style="height: 130px; width: 504px;" />
请你返回结果链表的头指针。

 

 **示例 1：** 

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/28/merge_linked_list_ex1.png" style="width: 406px; height: 140px;" />

```

输入：list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
输出：[0,1,2,1000000,1000001,1000002,5]
解释：我们删除 list1 中下标为 3 和 4 的两个节点，并将 list2 接在该位置。上图中蓝色的边和节点为答案链表。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/11/28/merge_linked_list_ex2.png" style="width: 463px; height: 140px;" />
```

输入：list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
输出：[0,1,1000000,1000001,1000002,1000003,1000004,6]
解释：上图中蓝色的边和节点为答案链表。

```
 

 **提示：** 
-  `3 <= list1.length <= 10^4` 
-  `1 <= a <= b < list1.length - 1` 
-  `1 <= list2.length <= 10^4` 
 
**标签**
`链表` 


## 
```python

```
>
# 1670.设计前中后队列
[https://leetcode-cn.com/problems/design-front-middle-back-queue](https://leetcode-cn.com/problems/design-front-middle-back-queue) 
## 原题
请你设计一个队列，支持在前，中，后三个位置的 `push`  和 `pop`  操作。

请你完成  `FrontMiddleBack`  类：
-  `FrontMiddleBack()`  初始化队列。
-  `void pushFront(int val)` 将  `val`  添加到队列的 **最前面**  。
-  `void pushMiddle(int val)` 将  `val`  添加到队列的 **正中间**  。
-  `void pushBack(int val)`  将  `val`  添加到队里的 **最后面**  。
-  `int popFront()`  将 **最前面** 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 `-1`  。
-  `int popMiddle()` 将 <b>正中间</b> 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 `-1`  。
-  `int popBack()` 将 **最后面** 的元素从队列中删除并返回值，如果删除之前队列为空，那么返回 `-1`  。
请注意当有  **两个**  中间位置的时候，选择靠前面的位置进行操作。比方说：
- 将 `6`  添加到  `[1, 2, 3, 4, 5]`  的中间位置，结果数组为  `[1, 2, **6** , 3, 4, 5]`  。
- 从  `[1, 2, **3** , 4, 5, 6]`  的中间位置弹出元素，返回  `3`  ，数组变为  `[1, 2, 4, 5, 6]`  。
 

 **示例 1：** 

```

输入：
["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle", "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
[[], [1], [2], [3], [4], [], [], [], [], []]
输出：
[null, null, null, null, null, 1, 3, 4, 2, -1]

解释：
FrontMiddleBackQueue q = new FrontMiddleBackQueue();
q.pushFront(1);   // [1]
q.pushBack(2);    // [1, 2]
q.pushMiddle(3);  // [1, 3, 2]
q.pushMiddle(4);  // [1, 4, 3, 2]
q.popFront();     // 返回 1 -> [4, 3, 2]
q.popMiddle();    // 返回 3 -> [4, 2]
q.popMiddle();    // 返回 4 -> [2]
q.popBack();      // 返回 2 -> []
q.popFront();     // 返回 -1 -> [] （队列为空）

```
 

 **提示：** 
-  `1 <= val <= 10^9` 
- 最多调用  `1000`  次  `pushFront` ，  `pushMiddle` ，  `pushBack` ，  `popFront` ，  `popMiddle`  和  `popBack` 。
 
**标签**
`设计` `队列` `数组` `链表` `数据流` 


## 
```python

```
>
# 1671.得到山形数组的最少删除次数
[https://leetcode-cn.com/problems/minimum-number-of-removals-to-make-mountain-array](https://leetcode-cn.com/problems/minimum-number-of-removals-to-make-mountain-array) 
## 原题
我们定义  `arr`  是 <b>山形数组</b> 当且仅当它满足：
-  `arr.length >= 3` 
- 存在某个下标  `i`  （ **从 0 开始** ） 满足  `0 < i < arr.length - 1`  且：
	
-  `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]` 
-  `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]` 
	
	
给你整数数组  `nums` ​ ，请你返回将 `nums`  变成 **山形状数组**  的​ **最少**  删除次数。

 

 **示例 1：** 

```
输入：nums = [1,3,1]
输出：0
解释：数组本身就是山形数组，所以我们不需要删除任何元素。

```
 **示例 2：** 

```
输入：nums = [2,1,1,5,6,2,3,1]
输出：3
解释：一种方法是将下标为 0，1 和 5 的元素删除，剩余元素为 [1,5,6,3,1] ，是山形数组。

```
 **示例 3：** 

```
输入：nums = [4,3,2,1,1,2,3,1]
输出：4

```
 **提示：** 

```
输入：nums = [1,2,3,4,4,3,2,1]
输出：1

```
 

 **提示：** 
-  `3 <= nums.length <= 1000` 
-  `1 <= nums[i] <= 10^9` 
- 题目保证  `nums` 删除一些元素后一定能得到山形数组。
 
**标签**
`贪心` `数组` `二分查找` `动态规划` 


## 
```python

```
>
# 1672.最富有客户的资产总量
[https://leetcode-cn.com/problems/richest-customer-wealth](https://leetcode-cn.com/problems/richest-customer-wealth) 
## 原题
给你一个 `m x n` 的整数网格 `accounts` ，其中 `accounts[i][j]` 是第 `i​​​​​^​​​​​​​` 位客户在第 `j` 家银行托管的资产数量。返回最富有客户所拥有的 **资产总量** 。

客户的 **资产总量** 就是他们在各家银行托管的资产数量之和。最富有客户就是 **资产总量** 最大的客户。

 

 **示例 1：** 

```
输入：accounts = [[1,2,3],[3,2,1]]
输出：6
解释：
第 1 位客户的资产总量 = 1 + 2 + 3 = 6
第 2 位客户的资产总量 = 3 + 2 + 1 = 6
两位客户都是最富有的，资产总量都是 6 ，所以返回 6 。

```
 **示例 2：** 

```
输入：accounts = [[1,5],[7,3],[3,5]]
输出：10
解释：
第 1 位客户的资产总量 = 6
第 2 位客户的资产总量 = 10 
第 3 位客户的资产总量 = 8
第 2 位客户是最富有的，资产总量是 10
```
 **示例 3：** 

```
输入：accounts = [[2,8,7],[7,1,3],[1,9,5]]
输出：17

```
 

 **提示：** 
-  `m == accounts.length` 
-  `n == accounts[i].length` 
-  `1 <= m, n <= 50` 
-  `1 <= accounts[i][j] <= 100` 
 
**标签**
`数组` `矩阵` 


## 
```python

```
>
# 1673.找出最具竞争力的子序列
[https://leetcode-cn.com/problems/find-the-most-competitive-subsequence](https://leetcode-cn.com/problems/find-the-most-competitive-subsequence) 
## 原题
给你一个整数数组 `nums` 和一个正整数 `k` ，返回长度为 `k` 且最具 **竞争力** 的 `nums` 子序列。

数组的子序列是从数组中删除一些元素（可能不删除元素）得到的序列。

在子序列  `a` 和子序列  `b` 第一个不相同的位置上，如果  `a`  中的数字小于 `b` 中对应的数字，那么我们称子序列 `a` 比子序列 `b` （相同长度下）更具 **竞争力** 。 例如， `[1,3,4]` 比 `[1,3,5]` 更具竞争力，在第一个不相同的位置，也就是最后一个位置上，  `4` 小于 `5` 。

 

 **示例 1：** 

```

输入：nums = [3,5,2,6], k = 2
输出：[2,6]
解释：在所有可能的子序列集合 {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]} 中，[2,6] 最具竞争力。

```
 **示例 2：** 

```

输入：nums = [2,4,3,3,5,4,9,6], k = 4
输出：[2,3,3,4]

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `0 <= nums[i] <= 10^9` 
-  `1 <= k <= nums.length` 
 
**标签**
`栈` `贪心` `数组` `单调栈` 


## 
```python

```
>
# 1674.使数组互补的最少操作次数
[https://leetcode-cn.com/problems/minimum-moves-to-make-array-complementary](https://leetcode-cn.com/problems/minimum-moves-to-make-array-complementary) 
## 原题
给你一个长度为 **偶数** `n` 的整数数组 `nums` 和一个整数 `limit` 。每一次操作，你可以将 `nums` 中的任何整数替换为  `1`  到  `limit` 之间的另一个整数。

如果对于所有下标 `i` （ **下标从** `0` **开始** ）， `nums[i] + nums[n - 1 - i]`  都等于同一个数，则数组 `nums` 是 **互补的** 。例如，数组 `[1,2,3,4]` 是互补的，因为对于所有下标  `i` ， `nums[i] + nums[n - 1 - i] = 5` 。

返回使数组 **互补** 的 **最少**  操作次数。

 

 **示例 1：** 

```

输入：nums = [1,2,4,3], limit = 4
输出：1
解释：经过 1 次操作，你可以将数组 nums 变成 [1,2,2,3]（加粗元素是变更的数字）：
nums[0] + nums[3] = 1 + 3 = 4.
nums[1] + nums[2] = 2 + 2 = 4.
nums[2] + nums[1] = 2 + 2 = 4.
nums[3] + nums[0] = 3 + 1 = 4.
对于每个 i ，nums[i] + nums[n-1-i] = 4 ，所以 nums 是互补的。

```
 **示例 2：** 

```

输入：nums = [1,2,2,1], limit = 2
输出：2
解释：经过 2 次操作，你可以将数组 nums 变成 [2,2,2,2] 。你不能将任何数字变更为 3 ，因为 3 > limit 。

```
 **示例 3：** 

```

输入：nums = [1,2,1,2], limit = 2
输出：0
解释：nums 已经是互补的。

```
 

 **提示：** 
-  `n == nums.length` 
-  `2 <= n <= 10^5` 
-  `1 <= nums[i] <= limit <= 10^5` 
-  `n` 是偶数。
 
**标签**
`数组` `哈希表` `前缀和` 


## 
```python

```
>
# 1675.数组的最小偏移量
[https://leetcode-cn.com/problems/minimize-deviation-in-array](https://leetcode-cn.com/problems/minimize-deviation-in-array) 
## 原题
给你一个由 `n` 个正整数组成的数组 `nums` 。

你可以对数组的任意元素执行任意次数的两类操作：
- 如果元素是 **偶数** ， **除以** `2` 

	
- 例如，如果数组是 `[1,2,3,4]` ，那么你可以对最后一个元素执行此操作，使其变成 `[1,2,3, **2** ]` 
	
	
- 如果元素是 **奇数** ， **乘上** `2` 
	
- 例如，如果数组是 `[1,2,3,4]` ，那么你可以对第一个元素执行此操作，使其变成 `[ **2** ,2,3,4]` 
	
	
数组的 **偏移量** 是数组中任意两个元素之间的 **最大差值** 。

返回数组在执行某些操作之后可以拥有的 **最小偏移量** 。

 

 **示例 1：** 

```
输入：nums = [1,2,3,4]
输出：1
解释：你可以将数组转换为 [1,2,3,2]，然后转换成 [2,2,3,2]，偏移量是 3 - 2 = 1

```
 **示例 2：** 

```
输入：nums = [4,1,5,20,3]
输出：3
解释：两次操作后，你可以将数组转换为 [4,2,5,5,3]，偏移量是 5 - 2 = 3

```
 **示例 3：** 

```
输入：nums = [2,10,8]
输出：3

```
 

 **提示：** 
-  `n == nums.length` 
-  `2 <= n <= 10^<span style="">5</span>` 
-  `1 <= nums[i] <= 10^9` 
 
**标签**
`贪心` `数组` `有序集合` `堆（优先队列）` 


## 
```python

```
>
# 1676.二叉树的最近公共祖先 IV
[https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-iv](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree-iv) 
## 原题

 
**标签**
`树` `深度优先搜索` `二叉树` 


## 
```python

```
>
# 1677.发票中的产品金额
[https://leetcode-cn.com/problems/products-worth-over-invoices](https://leetcode-cn.com/problems/products-worth-over-invoices) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1678.设计 Goal 解析器
[https://leetcode-cn.com/problems/goal-parser-interpretation](https://leetcode-cn.com/problems/goal-parser-interpretation) 
## 原题
请你设计一个可以解释字符串 `command` 的 **Goal 解析器** 。 `command` 由 `"G"` 、 `"()"` 和/或 `"(al)"` 按某种顺序组成。Goal 解析器会将 `"G"` 解释为字符串 `"G"` 、 `"()"` 解释为字符串 `"o"` ， `"(al)"` 解释为字符串 `"al"` 。然后，按原顺序将经解释得到的字符串连接成一个字符串。

给你字符串 `command` ，返回 **Goal ****** 解析器** 对 `command` 的解释结果。

 

 **示例 1：** 

```
输入：command = "G()(al)"
输出："Goal"
解释：Goal 解析器解释命令的步骤如下所示：
G -> G
() -> o
(al) -> al
最后连接得到的结果是 "Goal"

```
 **示例 2：** 

```
输入：command = "G()()()()(al)"
输出："Gooooal"

```
 **示例 3：** 

```
输入：command = "(al)G(al)()()G"
输出："alGalooG"

```
 

 **提示：** 
-  `1 <= command.length <= 100` 
-  `command` 由 `"G"` 、 `"()"` 和/或 `"(al)"` 按某种顺序组成
 
**标签**
`字符串` 


## 
```python

```
>
# 1679.K 和数对的最大数目
[https://leetcode-cn.com/problems/max-number-of-k-sum-pairs](https://leetcode-cn.com/problems/max-number-of-k-sum-pairs) 
## 原题
给你一个整数数组 `nums` 和一个整数 `k` 。

每一步操作中，你需要从数组中选出和为 `k` 的两个整数，并将它们移出数组。

返回你可以对数组执行的最大操作数。

 

 **示例 1：** 

```

输入：nums = [1,2,3,4], k = 5
输出：2
解释：开始时 nums = [1,2,3,4]：
- 移出 1 和 4 ，之后 nums = [2,3]
- 移出 2 和 3 ，之后 nums = []
不再有和为 5 的数对，因此最多执行 2 次操作。
```
 **示例 2：** 

```

输入：nums = [3,1,3,4,3], k = 6
输出：1
解释：开始时 nums = [3,1,3,4,3]：
- 移出前两个 3 ，之后nums = [1,4,3]
不再有和为 6 的数对，因此最多执行 1 次操作。
```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^9` 
-  `1 <= k <= 10^9` 
 
**标签**
`数组` `哈希表` `双指针` `排序` 


## 
```python

```
>
# 1680.连接连续二进制数字
[https://leetcode-cn.com/problems/concatenation-of-consecutive-binary-numbers](https://leetcode-cn.com/problems/concatenation-of-consecutive-binary-numbers) 
## 原题
给你一个整数  `n`  ，请你将  `1`  到 `n`  的二进制表示连接起来，并返回连接结果对应的 **十进制**  数字对 `10^9 + 7`  取余的结果。

 

 **示例 1：** 

```
输入：n = 1
输出：1
解释：二进制的 "1" 对应着十进制的 1 。

```
 **示例 2：** 

```
输入：n = 3
输出：27
解释：二进制下，1，2 和 3 分别对应 "1" ，"10" 和 "11" 。
将它们依次连接，我们得到 "11011" ，对应着十进制的 27 。

```
 **示例 3：** 

```
输入：n = 12
输出：505379714
解释：连接结果为 "1101110010111011110001001101010111100" 。
对应的十进制数字为 118505380540 。
对 10^9 + 7 取余后，结果为 505379714 。

```
 

 **提示：** 
-  `1 <= n <= 10^5` 
 
**标签**
`位运算` `数学` `模拟` 


## 
```python

```
>
# 1681.最小不兼容性
[https://leetcode-cn.com/problems/minimum-incompatibility](https://leetcode-cn.com/problems/minimum-incompatibility) 
## 原题
给你一个整数数组  `nums` ​​​ 和一个整数  `k`  。你需要将这个数组划分到  `k`  个相同大小的子集中，使得同一个子集里面没有两个相同的元素。

一个子集的 **不兼容性**  是该子集里面最大值和最小值的差。

请你返回将数组分成 `k`  个子集后，各子集 **不兼容性** 的 **和**  的 **最小值**  ，如果无法分成分成 `k`  个子集，返回 `-1`  。

子集的定义是数组中一些数字的集合，对数字顺序没有要求。

 

 **示例 1：** 

```

输入：nums = [1,2,1,4], k = 2
输出：4
解释：最优的分配是 [1,2] 和 [1,4] 。
不兼容性和为 (2-1) + (4-1) = 4 。
注意到 [1,1] 和 [2,4] 可以得到更小的和，但是第一个集合有 2 个相同的元素，所以不可行。
```
 **示例 2：** 

```

输入：nums = [6,3,8,1,3,1,2,2], k = 4
输出：6
解释：最优的子集分配为 [1,2]，[2,3]，[6,8] 和 [1,3] 。
不兼容性和为 (2-1) + (3-2) + (8-6) + (3-1) = 6 。

```
 **示例 3：** 

```

输入：nums = [5,3,3,6,3,3], k = 3
输出：-1
解释：没办法将这些数字分配到 3 个子集且满足每个子集里没有相同数字。

```
 

 **提示：** 
-  `1 <= k <= nums.length <= 16` 
-  `nums.length` 能被  `k` 整除。
-  `1 <= nums[i] <= nums.length` 
 
**标签**
`位运算` `数组` `动态规划` `状态压缩` 


## 
```python

```
>
# 1682.最长回文子序列 II
[https://leetcode-cn.com/problems/longest-palindromic-subsequence-ii](https://leetcode-cn.com/problems/longest-palindromic-subsequence-ii) 
## 原题

 
**标签**
`字符串` `动态规划` 


## 
```python

```
>
# 1683.无效的推文
[https://leetcode-cn.com/problems/invalid-tweets](https://leetcode-cn.com/problems/invalid-tweets) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1684.统计一致字符串的数目
[https://leetcode-cn.com/problems/count-the-number-of-consistent-strings](https://leetcode-cn.com/problems/count-the-number-of-consistent-strings) 
## 原题
给你一个由不同字符组成的字符串  `allowed`  和一个字符串数组  `words`  。如果一个字符串的每一个字符都在 `allowed`  中，就称这个字符串是 **一致字符串** 。

请你返回  `words`  数组中  **一致字符串** 的数目。

 

 **示例 1：** 

```

输入：allowed = "ab", words = ["ad","bd","aaab","baa","badab"]
输出：2
解释：字符串 "aaab" 和 "baa" 都是一致字符串，因为它们只包含字符 'a' 和 'b' 。

```
 **示例 2：** 

```

输入：allowed = "abc", words = ["a","b","c","ab","ac","bc","abc"]
输出：7
解释：所有字符串都是一致的。

```
 **示例 3：** 

```

输入：allowed = "cad", words = ["cc","acd","b","ba","bac","bad","ac","d"]
输出：4
解释：字符串 "cc"，"acd"，"ac" 和 "d" 是一致字符串。

```
 

 **提示：** 
-  `1 <= words.length <= 10^4` 
-  `1 <= allowed.length <=^ 26` 
-  `1 <= words[i].length <= 10` 
-  `allowed`  中的字符 **互不相同**  。
-  `words[i]` 和  `allowed`  只包含小写英文字母。
 
**标签**
`位运算` `数组` `哈希表` `字符串` 


## 
```python

```
>
# 1685.有序数组中差绝对值之和
[https://leetcode-cn.com/problems/sum-of-absolute-differences-in-a-sorted-array](https://leetcode-cn.com/problems/sum-of-absolute-differences-in-a-sorted-array) 
## 原题
给你一个 **非递减 ** 有序整数数组  `nums`  。

请你建立并返回一个整数数组 * * `result` ，它跟 * * `nums`  长度相同，且 `result[i]`  等于 * * `nums[i]`  与数组中所有其他元素差的绝对值之和。

换句话说，  `result[i]`  等于  `sum(|nums[i]-nums[j]|)` ，其中  `0 <= j < nums.length` 且  `j != i`  （下标从 0 开始）。

 

 **示例 1：** 

```

输入：nums = [2,3,5]
输出：[4,3,5]
解释：假设数组下标从 0 开始，那么
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4，
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3，
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5。

```
 **示例 2：** 

```

输入：nums = [1,4,6,8,10]
输出：[24,15,13,15,21]

```
 

 **提示：** 
-  `2 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= nums[i + 1] <= 10^4` 
 
**标签**
`数组` `数学` `前缀和` 


## 
```python

```
>
# 1686.石子游戏 VI
[https://leetcode-cn.com/problems/stone-game-vi](https://leetcode-cn.com/problems/stone-game-vi) 
## 原题
Alice 和 Bob 轮流玩一个游戏，Alice 先手。

一堆石子里总共有  `n`  个石子，轮到某个玩家时，他可以 **移出**  一个石子并得到这个石子的价值。Alice 和 Bob 对石子价值有 **不一样的的评判标准**  。双方都知道对方的评判标准。

给你两个长度为 `n`  的整数数组  `aliceValues` 和  `bobValues`  。 `aliceValues[i]` 和  `bobValues[i]`  分别表示 Alice 和 Bob 认为第  `i`  个石子的价值。

所有石子都被取完后，得分较高的人为胜者。如果两个玩家得分相同，那么为平局。两位玩家都会采用 <b>最优策略</b> 进行游戏。

请你推断游戏的结果，用如下的方式表示：
- 如果 Alice 赢，返回  `1`  。
- 如果 Bob 赢，返回  `-1`  。
- 如果游戏平局，返回  `0`  。
 

 **示例 1：** 

```

输入：aliceValues = [1,3], bobValues = [2,1]
输出：1
解释：
如果 Alice 拿石子 1 （下标从 0开始），那么 Alice 可以得到 3 分。
Bob 只能选择石子 0 ，得到 2 分。
Alice 获胜。

```
 **示例 2：** 

```

输入：aliceValues = [1,2], bobValues = [3,1]
输出：0
解释：
Alice 拿石子 0 ， Bob 拿石子 1 ，他们得分都为 1 分。
打平。

```
 **示例 3：** 

```

输入：aliceValues = [2,4,3], bobValues = [1,6,7]
输出：-1
解释：
不管 Alice 怎么操作，Bob 都可以得到比 Alice 更高的得分。
比方说，Alice 拿石子 1 ，Bob 拿石子 2 ， Alice 拿石子 0 ，Alice 会得到 6 分而 Bob 得分为 7 分。
Bob 会获胜。

```
 

 **提示：** 
-  `n == aliceValues.length == bobValues.length` 
-  `1 <= n <= 10^5` 
-  `1 <= aliceValues[i], bobValues[i] <= 100` 
 
**标签**
`贪心` `数组` `数学` `博弈` `排序` `堆（优先队列）` 


## 
```python

```
>
# 1687.从仓库到码头运输箱子
[https://leetcode-cn.com/problems/delivering-boxes-from-storage-to-ports](https://leetcode-cn.com/problems/delivering-boxes-from-storage-to-ports) 
## 原题
你有一辆货运卡车，你需要用这一辆车把一些箱子从仓库运送到码头。这辆卡车每次运输有  **箱子数目的限制**  和 **总重量的限制**  。

给你一个箱子数组  `boxes`  和三个整数 `portsCount` , `maxBoxes`  和  `maxWeight`  ，其中  `boxes[i] = [ports<sub>​​i</sub>​, weight<sub>i</sub>]`  。
-  `ports<sub>​​i</sub>`  表示第  `i`  个箱子需要送达的码头，  `weights<sub>i</sub>`  是第  `i`  个箱子的重量。
-  `portsCount`  是码头的数目。
-  `maxBoxes` 和  `maxWeight`  分别是卡车每趟运输箱子数目和重量的限制。
箱子需要按照 **数组顺序**  运输，同时每次运输需要遵循以下步骤：
- 卡车从  `boxes`  队列中按顺序取出若干个箱子，但不能违反  `maxBoxes` 和  `maxWeight`  限制。
- 对于在卡车上的箱子，我们需要 **按顺序**  处理它们，卡车会通过 **一趟行程**  将最前面的箱子送到目的地码头并卸货。如果卡车已经在对应的码头，那么不需要 **额外行程**  ，箱子也会立马被卸货。
- 卡车上所有箱子都被卸货后，卡车需要 **一趟行程**  回到仓库，从箱子队列里再取出一些箱子。
卡车在将所有箱子运输并卸货后，最后必须回到仓库。

请你返回将所有箱子送到相应码头的 <b>最少行程</b> 次数。

 

 **示例 1：** 

```
输入：boxes = [[1,1],[2,1],[1,1]], portsCount = 2, maxBoxes = 3, maxWeight = 3
输出：4
解释：最优策略如下：
- 卡车将所有箱子装上车，到达码头 1 ，然后去码头 2 ，然后再回到码头 1 ，最后回到仓库，总共需要 4 趟行程。
所以总行程数为 4 。
注意到第一个和第三个箱子不能同时被卸货，因为箱子需要按顺序处理（也就是第二个箱子需要先被送到码头 2 ，然后才能处理第三个箱子）。

```
 **示例 2：** 

```
输入：boxes = [[1,2],[3,3],[3,1],[3,1],[2,4]], portsCount = 3, maxBoxes = 3, maxWeight = 6
输出：6
解释：最优策略如下：
- 卡车首先运输第一个箱子，到达码头 1 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第二、第三、第四个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第五个箱子，到达码头 3 ，回到仓库，总共 2 趟行程。
总行程数为 2 + 2 + 2 = 6 。

```
 **示例 3：** 

```
输入：boxes = [[1,4],[1,2],[2,1],[2,1],[3,2],[3,4]], portsCount = 3, maxBoxes = 6, maxWeight = 7
输出：6
解释：最优策略如下：
- 卡车运输第一和第二个箱子，到达码头 1 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第三和第四个箱子，到达码头 2 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第五和第六个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
总行程数为 2 + 2 + 2 = 6 。

```
 **示例 4：** 

```
输入：boxes = [[2,4],[2,5],[3,1],[3,2],[3,7],[3,1],[4,4],[1,3],[5,2]], portsCount = 5, maxBoxes = 5, maxWeight = 7
输出：14
解释：最优策略如下：
- 卡车运输第一个箱子，到达码头 2 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第二个箱子，到达码头 2 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第三和第四个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第五个箱子，到达码头 3 ，然后回到仓库，总共 2 趟行程。
- 卡车运输第六和第七个箱子，到达码头 3 ，然后去码头 4 ，然后回到仓库，总共 3 趟行程。
- 卡车运输第八和第九个箱子，到达码头 1 ，然后去码头 5 ，然后回到仓库，总共 3 趟行程。
总行程数为 2 + 2 + 2 + 2 + 3 + 3 = 14 。

```
 

 **提示：** 
-  `1 <= boxes.length <= 10^5` 
-  `1 <= portsCount, maxBoxes, maxWeight <= 10^5` 
-  `1 <= ports<sub>​​i</sub> <= portsCount` 
-  `1 <= weights<sub>i</sub> <= maxWeight` 
 
**标签**
`线段树` `队列` `数组` `动态规划` `单调队列` `堆（优先队列）` 


## 
```python

```
>
# 1688.比赛中的配对次数
[https://leetcode-cn.com/problems/count-of-matches-in-tournament](https://leetcode-cn.com/problems/count-of-matches-in-tournament) 
## 原题
给你一个整数 `n` ，表示比赛中的队伍数。比赛遵循一种独特的赛制：
- 如果当前队伍数是 **偶数** ，那么每支队伍都会与另一支队伍配对。总共进行 `n / 2` 场比赛，且产生 `n / 2` 支队伍进入下一轮。
- 如果当前队伍数为 **奇数** ，那么将会随机轮空并晋级一支队伍，其余的队伍配对。总共进行 `(n - 1) / 2` 场比赛，且产生 `(n - 1) / 2 + 1` 支队伍进入下一轮。
返回在比赛中进行的配对次数，直到决出获胜队伍为止。

 

 **示例 1：** 

```
输入：n = 7
输出：6
解释：比赛详情：
- 第 1 轮：队伍数 = 7 ，配对次数 = 3 ，4 支队伍晋级。
- 第 2 轮：队伍数 = 4 ，配对次数 = 2 ，2 支队伍晋级。
- 第 3 轮：队伍数 = 2 ，配对次数 = 1 ，决出 1 支获胜队伍。
总配对次数 = 3 + 2 + 1 = 6

```
 **示例 2：** 

```
输入：n = 14
输出：13
解释：比赛详情：
- 第 1 轮：队伍数 = 14 ，配对次数 = 7 ，7 支队伍晋级。
- 第 2 轮：队伍数 = 7 ，配对次数 = 3 ，4 支队伍晋级。 
- 第 3 轮：队伍数 = 4 ，配对次数 = 2 ，2 支队伍晋级。
- 第 4 轮：队伍数 = 2 ，配对次数 = 1 ，决出 1 支获胜队伍。
总配对次数 = 7 + 3 + 2 + 1 = 13

```
 

 **提示：** 
-  `1 <= n <= 200` 
 
**标签**
`数学` `模拟` 


## 
```python

```
>
# 1689.十-二进制数的最少数目
[https://leetcode-cn.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers](https://leetcode-cn.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers) 
## 原题
如果一个十进制数字不含任何前导零，且每一位上的数字不是 `0` 就是 `1` ，那么该数字就是一个 **十-二进制数** 。例如， `101` 和 `1100` 都是 **十-二进制数** ，而 `112` 和 `3001` 不是。

给你一个表示十进制整数的字符串 `n` ，返回和为 `n` 的 **十-二进制数** 的最少数目。

 

 **示例 1：** 

```
输入：n = "32"
输出：3
解释：10 + 11 + 11 = 32

```
 **示例 2：** 

```
输入：n = "82734"
输出：8

```
 **示例 3：** 

```
输入：n = "27346209830709182346"
输出：9

```
 

 **提示：** 
-  `1 <= n.length <= 10^5` 
-  `n` 仅由数字组成
-  `n` 不含任何前导零并总是表示正整数
 
**标签**
`贪心` `字符串` 


## 
```python

```
>
# 1690.石子游戏 VII
[https://leetcode-cn.com/problems/stone-game-vii](https://leetcode-cn.com/problems/stone-game-vii) 
## 原题
石子游戏中，爱丽丝和鲍勃轮流进行自己的回合， **爱丽丝先开始** 。

有 `n` 块石子排成一排。每个玩家的回合中，可以从行中 **移除** 最左边的石头或最右边的石头，并获得与该行中剩余石头值之 **和** 相等的得分。当没有石头可移除时，得分较高者获胜。

鲍勃发现他总是输掉游戏（可怜的鲍勃，他总是输），所以他决定尽力 **减小得分的差值** 。爱丽丝的目标是最大限度地 **扩大得分的差值** 。

给你一个整数数组  `stones` ，其中 `stones[i]` 表示 **从左边开始** 的第 `i` 个石头的值，如果爱丽丝和鲍勃都 **发挥出最佳水平** ，请返回他们 **得分的差值** 。

 

 **示例 1：** 

```

输入：stones = [5,3,1,4,2]
输出：6
解释：
- 爱丽丝移除 2 ，得分 5 + 3 + 1 + 4 = 13 。游戏情况：爱丽丝 = 13 ，鲍勃 = 0 ，石子 = [5,3,1,4] 。
- 鲍勃移除 5 ，得分 3 + 1 + 4 = 8 。游戏情况：爱丽丝 = 13 ，鲍勃 = 8 ，石子 = [3,1,4] 。
- 爱丽丝移除 3 ，得分 1 + 4 = 5 。游戏情况：爱丽丝 = 18 ，鲍勃 = 8 ，石子 = [1,4] 。
- 鲍勃移除 1 ，得分 4 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [4] 。
- 爱丽丝移除 4 ，得分 0 。游戏情况：爱丽丝 = 18 ，鲍勃 = 12 ，石子 = [] 。
得分的差值 18 - 12 = 6 。

```
 **示例 2：** 

```

输入：stones = [7,90,5,1,100,10,10,2]
输出：122
```
 

 **提示：** 
-  `n == stones.length` 
-  `2 <= n <= 1000` 
-  `1 <= stones[i] <= 1000` 
 
**标签**
`数组` `数学` `动态规划` `博弈` 


## 
```python

```
>
# 1691.堆叠长方体的最大高度
[https://leetcode-cn.com/problems/maximum-height-by-stacking-cuboids](https://leetcode-cn.com/problems/maximum-height-by-stacking-cuboids) 
## 原题
给你 `n` 个长方体 `cuboids` ，其中第 `i` 个长方体的长宽高表示为 `cuboids[i] = [width<sub>i</sub>, length<sub>i</sub>, height<sub>i</sub>]` （ **下标从 0 开始** ）。请你从 `cuboids` 选出一个 **子集** ，并将它们堆叠起来。

如果 `width<sub>i</sub> <= width<sub>j</sub>` 且 `length<sub>i</sub> <= length<sub>j</sub>` 且 `height<sub>i</sub> <= height<sub>j</sub>` ，你就可以将长方体 `i` 堆叠在长方体 `j` 上。你可以通过旋转把长方体的长宽高重新排列，以将它放在另一个长方体上。

返回 **堆叠长方体**   `cuboids` 可以得到的 **最大高度** 。

 

 **示例 1：** 

 **<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/12/12/image.jpg" style="width: 420px; height: 299px;" />** 

```

输入：cuboids = [[50,45,20],[95,37,53],[45,23,12]]
输出：190
解释：
第 1 个长方体放在底部，53x37 的一面朝下，高度为 95 。
第 0 个长方体放在中间，45x20 的一面朝下，高度为 50 。
第 2 个长方体放在上面，23x12 的一面朝下，高度为 45 。
总高度是 95 + 50 + 45 = 190 。

```
 **示例 2：** 

```

输入：cuboids = [[38,25,45],[76,35,3]]
输出：76
解释：
无法将任何长方体放在另一个上面。
选择第 1 个长方体然后旋转它，使 35x3 的一面朝下，其高度为 76 。

```
 **示例 3：** 

```

输入：cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
输出：102
解释：
重新排列长方体后，可以看到所有长方体的尺寸都相同。
你可以把 11x7 的一面朝下，这样它们的高度就是 17 。
堆叠长方体的最大高度为 6 * 17 = 102 。

```
 

 **提示：** 
-  `n == cuboids.length` 
-  `1 <= n <= 100` 
-  `1 <= width<sub>i</sub>, length<sub>i</sub>, height<sub>i</sub> <= 100` 
 
**标签**
`数组` `动态规划` `排序` 


## 
```python

```
>
# 1692.计算分配糖果的不同方式
[https://leetcode-cn.com/problems/count-ways-to-distribute-candies](https://leetcode-cn.com/problems/count-ways-to-distribute-candies) 
## 原题

 
**标签**
`动态规划` 


## 
```python

```
>
# 1693.每天的领导和合伙人
[https://leetcode-cn.com/problems/daily-leads-and-partners](https://leetcode-cn.com/problems/daily-leads-and-partners) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1694.重新格式化电话号码
[https://leetcode-cn.com/problems/reformat-phone-number](https://leetcode-cn.com/problems/reformat-phone-number) 
## 原题
给你一个字符串形式的电话号码 `number` 。 `number` 由数字、空格 `' '` 、和破折号 `'-'` 组成。

请你按下述方式重新格式化电话号码。
- 首先， **删除** 所有的空格和破折号。
- 其次，将数组从左到右 **每 3 个一组** 分块， **直到** 剩下 4 个或更少数字。剩下的数字将按下述规定再分块：
	
- 2 个数字：单个含 2 个数字的块。
- 3 个数字：单个含 3 个数字的块。
- 4 个数字：两个分别含 2 个数字的块。
	
	
最后用破折号将这些块连接起来。注意，重新格式化过程中 **不应该** 生成仅含 1 个数字的块，并且 **最多** 生成两个含 2 个数字的块。

返回格式化后的电话号码。

 

 **示例 1：** 

```

输入：number = "1-23-45 6"
输出："123-456"
解释：数字是 "123456"
步骤 1：共有超过 4 个数字，所以先取 3 个数字分为一组。第 1 个块是 "123" 。
步骤 2：剩下 3 个数字，将它们放入单个含 3 个数字的块。第 2 个块是 "456" 。
连接这些块后得到 "123-456" 。
```
 **示例 2：** 

```

输入：number = "123 4-567"
输出："123-45-67"
解释：数字是 "1234567".
步骤 1：共有超过 4 个数字，所以先取 3 个数字分为一组。第 1 个块是 "123" 。
步骤 2：剩下 4 个数字，所以将它们分成两个含 2 个数字的块。这 2 块分别是 "45" 和 "67" 。
连接这些块后得到 "123-45-67" 。

```
 **示例 3：** 

```

输入：number = "123 4-5678"
输出："123-456-78"
解释：数字是 "12345678" 。
步骤 1：第 1 个块 "123" 。
步骤 2：第 2 个块 "456" 。
步骤 3：剩下 2 个数字，将它们放入单个含 2 个数字的块。第 3 个块是 "78" 。
连接这些块后得到 "123-456-78" 。
```
 **示例 4：** 

```

输入：number = "12"
输出："12"

```
 **示例 5：** 

```

输入：number = "--17-5 229 35-39475 "
输出："175-229-353-94-75"

```
 

 **提示：** 
-  `2 <= number.length <= 100` 
-  `number` 由数字和字符 `'-'` 及 `' '` 组成。
-  `number` 中至少含 **2** 个数字。
 
**标签**
`字符串` 


## 
```python

```
>
# 1695.删除子数组的最大得分
[https://leetcode-cn.com/problems/maximum-erasure-value](https://leetcode-cn.com/problems/maximum-erasure-value) 
## 原题
给你一个正整数数组 `nums` ，请你从中删除一个含有 **若干不同元素** 的子数组 **。** 删除子数组的 **得分** 就是子数组各元素之 **和** 。

返回 **只删除一个** 子数组可获得的 **最大得分** *。* 

如果数组 `b` 是数组 `a` 的一个连续子序列，即如果它等于 `a[l],a[l+1],...,a[r]` ，那么它就是  `a` 的一个子数组。

 

 **示例 1：** 

```

输入：nums = [4,2,4,5,6]
输出：17
解释：最优子数组是 [2,4,5,6]

```
 **示例 2：** 

```

输入：nums = [5,2,1,2,5,2,1,2,5]
输出：8
解释：最优子数组是 [5,2,1] 或 [1,2,5]

```
 

 **提示：** 
-  `1 <= nums.length <= 10^5` 
-  `1 <= nums[i] <= 10^4` 
 
**标签**
`数组` `哈希表` `滑动窗口` 


## 
```python

```
>
# 1696.跳跃游戏 VI
[https://leetcode-cn.com/problems/jump-game-vi](https://leetcode-cn.com/problems/jump-game-vi) 
## 原题
给你一个下标从 **0** 开始的整数数组 `nums`  和一个整数 `k`  。

一开始你在下标  `0`  处。每一步，你最多可以往前跳  `k`  步，但你不能跳出数组的边界。也就是说，你可以从下标  `i`  跳到  `[i + 1， min(n - 1, i + k)]`   **包含** 两个端点的任意位置。

你的目标是到达数组最后一个位置（下标为 `n - 1`  ），你的 **得分**  为经过的所有数字之和。

请你返回你能得到的 **最大得分**  。

 

 **示例 1：** 

```

输入：nums = [1,-1,-2,4,-7,3], k = 2
输出：7
解释：你可以选择子序列 [1,-1,4,3] （上面加粗的数字），和为 7 。

```
 **示例 2：** 

```

输入：nums = [10,-5,-2,4,0,3], k = 3
输出：17
解释：你可以选择子序列 [10,4,3] （上面加粗数字），和为 17 。

```
 **示例 3：** 

```

输入：nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
输出：0

```
 

 **提示：** 
-   `1 <= nums.length, k <= 10^5` 
-  `-10^4 <= nums[i] <= 10^4` 
 
**标签**
`队列` `数组` `动态规划` `滑动窗口` `单调队列` `堆（优先队列）` 


## 
```python

```
>
# 1697.检查边长度限制的路径是否存在
[https://leetcode-cn.com/problems/checking-existence-of-edge-length-limited-paths](https://leetcode-cn.com/problems/checking-existence-of-edge-length-limited-paths) 
## 原题
给你一个 `n`  个点组成的无向图边集  `edgeList`  ，其中  `edgeList[i] = [u<sub>i</sub>, v<sub>i</sub>, dis<sub>i</sub>]`  表示点  `u<sub>i</sub>` 和点  `v<sub>i</sub>`  之间有一条长度为  `dis<sub>i</sub>`  的边。请注意，两个点之间可能有 **超过一条边 ** 。

给你一个查询数组 `queries`  ，其中  `queries[j] = [p<sub>j</sub>, q<sub>j</sub>, limit<sub>j</sub>]`  ，你的任务是对于每个查询  `queries[j]`  ，判断是否存在从  `p<sub>j</sub>`  到  `q<sub>j</sub>` <sub> </sub>的路径，且这条路径上的每一条边都 **严格小于**   `limit<sub>j</sub>`  。

请你返回一个 <b>布尔数组</b> * * `answer` * * ，其中 * * `answer.length == queries.length`  ，当  `queries[j]`  的查询结果为  `true`  时，  `answer` 第 * * `j`  个值为 * * `true` * * ，否则为  `false`  。

 

 **示例 1：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/12/19/h.png" style="width: 267px; height: 262px;" />
```

输入：n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
输出：[false,true]
解释：上图为给定的输入数据。注意到 0 和 1 之间有两条重边，分别为 2 和 16 。
对于第一个查询，0 和 1 之间没有小于 2 的边，所以我们返回 false 。
对于第二个查询，有一条路径（0 -> 1 -> 2）两条边都小于 5 ，所以这个查询我们返回 true 。

```
 **示例 2：** 
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/12/19/q.png" style="width: 390px; height: 358px;" />
```

输入：n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
输出：[true,false]
解释：上图为给定数据。

```
 

 **提示：** 
-  `2 <= n <= 10^5` 
-  `1 <= edgeList.length, queries.length <= 10^5` 
-  `edgeList[i].length == 3` 
-  `queries[j].length == 3` 
-  `0 <= u<sub>i</sub>, v<sub>i</sub>, p<sub>j</sub>, q<sub>j</sub> <= n - 1` 
-  `u<sub>i</sub> != v<sub>i</sub>` 
-  `p<sub>j</sub> != q<sub>j</sub>` 
-  `1 <= dis<sub>i</sub>, limit<sub>j</sub> <= 10^9` 
- 两个点之间可能有 **多条**  边。
 
**标签**
`并查集` `图` `数组` `排序` 


## 
```python

```
>
# 1698.字符串的不同子字符串个数
[https://leetcode-cn.com/problems/number-of-distinct-substrings-in-a-string](https://leetcode-cn.com/problems/number-of-distinct-substrings-in-a-string) 
## 原题

 
**标签**
`字典树` `字符串` `后缀数组` `哈希函数` `滚动哈希` 


## 
```python

```
>
# 1699.两人之间的通话次数
[https://leetcode-cn.com/problems/number-of-calls-between-two-persons](https://leetcode-cn.com/problems/number-of-calls-between-two-persons) 
## 原题

 
**标签**
`数据库` 


## 
```python

```
>
# 1700.无法吃午餐的学生数量
[https://leetcode-cn.com/problems/number-of-students-unable-to-eat-lunch](https://leetcode-cn.com/problems/number-of-students-unable-to-eat-lunch) 
## 原题
学校的自助午餐提供圆形和方形的三明治，分别用数字  `0`  和  `1`  表示。所有学生站在一个队列里，每个学生要么喜欢圆形的要么喜欢方形的。<br>
餐厅里三明治的数量与学生的数量相同。所有三明治都放在一个  **栈**  里，每一轮：
- 如果队列最前面的学生  **喜欢**  栈顶的三明治，那么会  **拿走它**  并离开队列。
- 否则，这名学生会  **放弃这个三明治**  并回到队列的尾部。
这个过程会一直持续到队列里所有学生都不喜欢栈顶的三明治为止。

给你两个整数数组  `students` 和  `sandwiches`  ，其中  `sandwiches[i]`  是栈里面第  `i^​​​​​​`  个三明治的类型（ `i = 0`  是栈的顶部），  `students[j]`  是初始队列里第  `j^​​​​​​`  名学生对三明治的喜好（ `j = 0`  是队列的最开始位置）。请你返回无法吃午餐的学生数量。

 

 **示例 1：** 

```
输入：students = [1,1,0,0], sandwiches = [0,1,0,1]
输出：0 
解释：
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [1,0,0,1]。
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [0,0,1,1]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = [0,1,1]，三明治栈为 sandwiches = [1,0,1]。
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [1,1,0]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = [1,0]，三明治栈为 sandwiches = [0,1]。
- 最前面的学生放弃最顶上的三明治，并回到队列的末尾，学生队列变为 students = [0,1]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = [1]，三明治栈为 sandwiches = [1]。
- 最前面的学生拿走最顶上的三明治，剩余学生队列为 students = []，三明治栈为 sandwiches = []。
所以所有学生都有三明治吃。

```
 **示例 2：** 

```
输入：students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
输出：3

```
 

 **提示：** 
-  `1 <= students.length, sandwiches.length <= 100` 
-  `students.length == sandwiches.length` 
-  `sandwiches[i]`  要么是  `0`  ，要么是  `1`  。
-  `students[i]`  要么是  `0`  ，要么是  `1`  。
 
**标签**
`栈` `队列` `数组` `模拟` 


## 
```python

```
>
