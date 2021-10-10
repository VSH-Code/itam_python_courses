def summation(nums):
    nums = [n * (-2) if n < 0 else n for n in nums]
    return(sum([x / max(nums) for x in nums]))

nums = list(map(int, input().split()))
print(summation(nums))
