from itertools import product

def _product(index, path):
    if len(path) == len(nums):
        result.append(path)
        return
    
    for i in range(index, len(nums)):
        for j in phoneNumber[nums[i]]:
            _product(index+1, path+j)


result = []
phoneNumber = {
    '2' : 'abc',
    '3' : 'def',
    '4' : 'ghi',
    '5' : 'jkl',
    '6' : 'nmo',
    '7' : 'pqrs',
    '8' : 'tuv',
    '9' : 'wxyz'
}
nums = "23"
print(_product(0, ""))
print(result)