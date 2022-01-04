/*
 * @lc app=leetcode.cn id=33 lang=cpp
 *
 * [33] 搜索旋转排序数组
 */

// @lc code=start
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int first = 0, last = nums.size() - 1;
        while (first <= last) {
            const int mid = first + (last - first) / 2;
            if (nums[mid] == target) {
                return mid;
            // 保证首到中间的部分是有序的    
            } else if (nums[first] <= nums[mid]) {
                // 判断target的范围
                if (nums[first] <= target && target < nums[mid]) {
                    last = mid - 1;
                } else {
                    first = mid + 1;
                }
            // 首到中间无序，只有一个断点，则中间到尾的部分有序 
            // 等价于nums[mid] <= nums[last-1]
            // 要么first到mid是有序的，要么mid到last是有序的
            } else if (nums[first] > nums[mid]) {
                if (nums[mid] < target && target <= nums[last]) {
                    first = mid + 1;
                } else {
                    last = mid - 1;
                }
            }
        }
        return -1;
    }
};
// @lc code=end

