
def gen(nums):
     for i in nums:
          yield (i*2)

doubles = gen([1,2,3,4,5])

print(*doubles)
print(next(doubles))