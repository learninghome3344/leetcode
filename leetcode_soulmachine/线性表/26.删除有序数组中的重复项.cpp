/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
class Solution {
public:
    // int removeDuplicates(vector<int>& nums) {
    //     if (nums.size() < 2) return nums.size();
    //     int index = 0;
    //     for (int i = 0; i < nums.size(); i++) {
    //         if (nums[i] != nums[index]) {
    //             nums[++index] = nums[i];
    //         }
    //     }
    //     return index+1;
    // }

    // int removeDuplicates(vector<int>& nums) {
    //     return distance(nums.begin(), unique(nums.begin(), nums.end()));
    // }

    int removeDuplicates(vector<int>& nums) {
        return distance(nums.begin(), remove1(nums.begin(), nums.end()));
    }
    // https://en.cppreference.com/w/cpp/algorithm/unique
    template<class ForwardIt>
    ForwardIt remove1(ForwardIt first, ForwardIt last)
    {
        if (first == last)
            return last;
        // first 指向去重前的数组中的element， result指向去重后的数组中的element
        /**
         * @brief [1,1,2]
         * first指向第2个1, result指向第一个1, 检测到!(*result == *first)为false则退出if并进行下一次循环
         * first指向2，result指向第2个1，检测到!(*result == *first)为true，再检查++result != first也为true才进行move操作
         * 
         * 以[1,2,2]为例
         * first指向第一个2，result指向1，检测到!(*result == *first)，如果进行move操作，那么实际上会覆盖掉1，
         * 因此必须加上 第二个判断条件 ++result != first
         * 显然result表示的含义是循环进行到当前这一步时已经生成的非重数组的最大索引
         */
        ForwardIt result = first;
        while (++first != last) {
            if (!(*result == *first) && ++result != first) {
                *result = std::move(*first);
            }
        }
        return ++result;
    }
};
// @lc code=end

