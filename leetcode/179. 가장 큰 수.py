# 1. 앞자리를 비교
# 2. 앞자리가 같다면, 뒷자리를 비교
def largestNumber(nums):
	
	for i in range(1, len(nums)):
		for j in range(1, i+1):
			cmp = i - j
			
			# 십의 자리
			a = int(str(nums[cmp])[0])
			b = int(str(nums[cmp+1])[0])
			
			# 뒤자리 비교
			if a == b:
				c = int(str(nums[cmp])[-1])
				d = int(str(nums[cmp+1])[-1])
				
				if c < d:
					nums[cmp], nums[cmp+1] = nums[cmp+1], nums[cmp]
			
			# 앞자리수 비교
			elif a < b:
				nums[cmp], nums[cmp+1] = nums[cmp+1], nums[cmp]

	return ''.join(map(str, nums))


nums = [10, 2]
# print(largestNumber(nums))

nums2 = [3, 30, 34, 5, 9]
print(largestNumber(nums2))