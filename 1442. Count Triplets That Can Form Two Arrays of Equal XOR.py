'''Given an array of integers arr.

We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).

Let's define a and b as follows:

a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.

Return the number of triplets (i, j and k) Where a == b.

 

Example 1:

Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)
Example 2:

Input: arr = [1,1,1,1,1]
Output: 10
 

Constraints:

1 <= arr.length <= 300
1 <= arr[i] <= 108'''

# Solution ----------------------------------------------------------------------------------------------------------------------------------

from typing import List

class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefixXor = [0] * (n + 1)
        for i in range(n):
            prefixXor[i + 1] = prefixXor[i] ^ arr[i]
        count = 0
        for j in range(n):
            for k in range(j + 1, n):
                if prefixXor[j] == prefixXor[k + 1]:
                    count += (k - j)
        return count