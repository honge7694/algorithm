def dfs(candidates_sum, index, path):
    if candidates_sum == 0:
        result.append(path)
        return
    if candidates_sum < 0:
        return
    
    for i in range(index, len(candidates)):
        dfs(candidates_sum-candidates[i], i, path+[candidates[i]])
    
    return result
    
candidates = [2, 3, 6, 7]
result = []
dfs(7, 0, [])
print(result)