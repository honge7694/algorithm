def dfs(target, index, path):
    if target == 0:
        result.append(path)
        return
    
    if target < 0:
        return

    for i in range(index, len(candidates)):
        dfs(target-candidates[i], i, path + [candidates[i]])


result = []
candidates = [2, 3, 6, 7]
target = 7

print(dfs(target, 0, []))