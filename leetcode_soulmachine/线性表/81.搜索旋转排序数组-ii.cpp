/*
 * @lc app=leetcode.cn id=81 lang=cpp
 *
 * [81] 搜索旋转排序数组 II
 */

// @lc code=start
/*
# 和1的区别在于有重复元素，因此可能出现
# 1,2,1,1,1
# 此时nums[first] <= nums[mid]，但是first~mid并不是有序的
# 因此需要将<和=分开，<时可以保证有，=时直接让first+1即可。
*/
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int first = 0, last = nums.size() - 1;
        while (first <= last) {
            int mid = first + (last - first) / 2;
            if (nums[mid] == target) {
                return true;
            } else if (nums[first] < nums[mid]) {
                if (nums[first] <= target && target < nums[mid]) {
                    last = mid - 1;
                } else {
                    first = mid + 1;
                }
            } else if (nums[first] == nums[mid]) {
                ++first;
            } else {
                if (nums[mid] < target && target <= nums[last]) {
                    first = mid + 1;
                } else {
                    last = mid - 1;
                }
            }
        }
        return false;
    }
};
// @lc code=end

