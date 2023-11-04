def dfs(index, path):
    result.append(path)
    
    for i in range(index, len(nums)):
        dfs(i+1, path+[nums[i]])

result = []
nums = [1, 2, 3]
dfs(0, [])
print(result)


