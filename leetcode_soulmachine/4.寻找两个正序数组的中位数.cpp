/*
 * @lc app=leetcode.cn id=4 lang=cpp
 *
 * [4] 寻找两个正序数组的中位数
 */

// @lc code=start
class Solution {
public:
    // 迭代器写法
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(), len2 = nums2.size(), total = len1 + len2;
        if (total % 2 == 1) {
            return findkMin(nums1.begin(), len1, nums2.begin(), len2, total / 2 + 1);
        } else {
            return 0.5 * (findkMin(nums1.begin(), len1, nums2.begin(), len2, total / 2) + 
                    findkMin(nums1.begin(), len1, nums2.begin(), len2, total / 2 + 1));
        }
    }

    // iter1表示迭代到该处时数组开头，len1表示此时数组的长度
    double findkMin(vector<int>::iterator iter1, int len1, vector<int>::iterator iter2, int len2, int k) {
        if (len1 > len2) return findkMin(iter2, len2, iter1, len1, k);
        if (len1 == 0) return *(iter2 + k - 1);
        if (k == 1) return min(*iter1, *iter2);

        int p1 = min(k/2, len1);
        int p2 = k - p1;
        if (*(iter1 + p1 - 1) < *(iter2 + p2 -1)) {
            return findkMin(iter1+p1, len1-p1, iter2, len2, k-p1);
        } else {
            return findkMin(iter1, len1, iter2+p2, len2-p2, k-p2);
        }
    }

    /* 
    // 数组式写法
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int len1 = nums1.size(), len2 = nums2.size(), total = len1 + len2;
        if (total % 2 == 1) {
            return findkMin(nums1, len1, nums2, len2, total / 2 + 1);
        } else {
            return 0.5 * (findkMin(nums1, len1, nums2, len2, total / 2) + findkMin(nums1, len1, nums2, len2, total / 2 + 1));
        }
    }

    double findkMin(vector<int>& nums1, int a, vector<int>& nums2, int b, int k) {
        if (a > b) return findkMin(nums2, b, nums1, a, k);
        if (a == 0) return nums2[k-1];
        if (k == 1) return min(nums1[nums1.size() - a], nums2[nums2.size() - b]);

        int pa = min(k/2, a);
        int pb = k - pa;

        if (nums1[nums1.size() - a + pa - 1] < nums2[nums2.size() - b + pb - 1]) {
            return findkMin(nums1, a-pa, nums2, b, k-pa);
        } else {
            return findkMin(nums1, a, nums2, b-pb, k-pb);
        }
    }
    */
};
// @lc code=end

