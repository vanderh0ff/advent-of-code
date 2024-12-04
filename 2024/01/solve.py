import heapq
import regex
from collections import defaultdict

counts = defaultdict(int)
left_list, right_list = [], []
with open('input.txt') as lists:
    for line in lists.readlines():
        l, r = list(map(int, line.strip().split('   ')))
        heapq.heappush(left_list, l)
        heapq.heappush(right_list, r)
        counts[r] += 1

simmilarirty = 0
for left in left_list:
    simmilarirty += left * counts[left]



difference = 0
for _ in range(len(left_list)):
    difference += abs(heapq.heappop(left_list) - heapq.heappop(right_list))
print(difference)
print(simmilarirty)



