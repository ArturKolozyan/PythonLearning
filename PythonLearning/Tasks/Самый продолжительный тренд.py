nums = input()
nums = nums.split()
nums = list(map(int, nums))

trends = []

for i in range(0, len(nums)):
    trend_nums = [nums[i]]
    for j in range(i + 1, len(nums)):
        if trend_nums[-1] <= nums[j]:
            trend_nums.append(nums[j])
            trends.append(' '.join(list(map(str, trend_nums))))
        else:
            break
for i in range(0, len(nums)):
    trend_nums = [nums[i]]
    for j in range(i + 1, len(nums)):
        if trend_nums[-1] >= nums[j]:
            trend_nums.append(nums[j])
            trends.append(' '.join(list(map(str, trend_nums))))
        else:
            break
finish_trens = []
trends.sort(key=len)
for i in trends:
    if len(i) == len(trends[-1]):
        print(i)
        break