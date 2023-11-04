# 1. 배열 정렬
# 2. 짝수인덱스만 더함.

def arrayPairSum(nums):
    result = 0

    nums.sort()
    for i in range(0, len(nums), 2):
        result += nums[i]

    return result

nums = [1, 4, 3, 2]
nums2 = [6, 2, 6, 5, 1, 2]
print(arrayPairSum(nums2))
