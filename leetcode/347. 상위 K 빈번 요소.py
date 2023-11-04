import collections


def topKFrequent(nums, k):
    num_freq = collections.Counter(nums).most_common(k)
    return [i[0] for i in num_freq]


nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))
