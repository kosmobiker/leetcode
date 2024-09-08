"""
Given an integer array nums sorted in non-decreasing order,
remove the duplicates in-place such that each unique element appears only once.
The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums be k, to get accepted, you need to do the following things:

    Change the array nums such that the first k elements of nums contain the unique elements in the order
        they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
    Return k.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]
                k += 1

        return k


if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 2, 2, 3, 3, 3, 4]
    expected_nums1 = [1, 2, 3, 4]
    expected_len1 = len(expected_nums1)

    s = Solution()
    k = s.removeDuplicates(nums1)

    assert k == expected_len1, f"Test Case 1 Failed: expected length {expected_len1}, but got {k}"
    for i in range(k):
        assert (
            nums1[i] == expected_nums1[i]
        ), f"Test Case 1 Failed: expected {expected_nums1[i]}, but got {nums1[i]}"

    # Test Case 2
    nums2 = []
    expected_nums2 = []
    expected_len2 = len(expected_nums2)

    k = s.removeDuplicates(nums2)

    assert k == expected_len2, f"Test Case 2 Failed: expected length {expected_len2}, but got {k}"
    assert (
        nums2 == expected_nums2
    ), f"Test Case 2 Failed: expected {expected_nums2}, but got {nums2}"

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    expected_nums3 = [1, 2, 3, 4, 5]
    expected_len3 = len(expected_nums3)

    k = s.removeDuplicates(nums3)

    assert k == expected_len3, f"Test Case 3 Failed: expected length {expected_len3}, but got {k}"
    for i in range(k):
        assert (
            nums3[i] == expected_nums3[i]
        ), f"Test Case 3 Failed: expected {expected_nums3[i]}, but got {nums3[i]}"

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    expected_nums4 = [1]
    expected_len4 = len(expected_nums4)

    k = s.removeDuplicates(nums4)

    assert k == expected_len4, f"Test Case 4 Failed: expected length {expected_len4}, but got {k}"
    for i in range(k):
        assert (
            nums4[i] == expected_nums4[i]
        ), f"Test Case 4 Failed: expected {expected_nums4[i]}, but got {nums4[i]}"
