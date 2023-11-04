import bisect

def search(nums1, nums2):
	result = []
	
	if len(nums1) > len(nums2):
		for num in nums2:
			if num in nums1:
				result.append(num)
	elif len(nums1) < len(nums2):
		for num in nums1:
			if num in nums2:
				result.append(num)
	else:
		for num in nums2:
			if num in nums1:
				result.append(num)
				
	return list(set(result))
		
	
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(search(nums1, nums2))


## 다른 풀이
def intersec_arrays(nums1, nums2):
    if not nums1 or not nums2:
        return []

    result = set()
    nums2.sort()
    for n1 in nums1:
        idx = bisect.bisect_left(nums2, n1)
        if len(nums2) > idx and n1 == nums2[idx]:
            result.add(n1)

    return list(result)