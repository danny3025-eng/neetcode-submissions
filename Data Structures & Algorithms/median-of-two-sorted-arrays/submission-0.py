class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    # Get the lengths of both input arrays
        m, n = len(nums1), len(nums2)
    
    # Calculate the total number of elements combined
        total = m + n
    
    # Find the middle index (or upper-middle index for even totals)
        half = total // 2
    
    # Initialize pointers 'i' for nums1 and 'j' for nums2
        i, j = 0, 0
    
    # Track the last two numbers processed to handle both even and odd totals
        prev, curr = 0, 0

    # Loop up to the middle element (half + 1 times) to find the median
        for count in range(half + 1):
        # Store the current element as 'prev' before updating 'curr'
            prev = curr
        
        # Check if the next element should be taken from nums1:
        # 1. 'i < m' ensures nums1 still has elements left to check.
        # 2. 'j >= n' means nums2 is empty, OR 'nums1[i] <= nums2[j]' means nums1 has the smaller value.
            if i < m and (j >= n or nums1[i] <= nums2[j]):
            # Move the value from nums1 into the current tracker
                curr = nums1[i]
            # Advance the pointer for nums1
                i += 1
            else:
            # Otherwise, move the value from nums2 into the current tracker
                curr = nums2[j]
            # Advance the pointer for nums2
                j += 1

    # If the total number of elements is odd, the median is the exact middle element
        if total % 2 == 1:
            return float(curr)
        else:
            return (prev + curr) / 2.0