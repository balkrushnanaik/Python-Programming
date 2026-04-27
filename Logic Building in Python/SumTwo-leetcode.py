nums = [5,2,3,9,3,2,9,2,4,6]
n=len(nums)
target = 13

for i in range(0,n-1):
    for j in range(i+1,n):
        if nums[i] + nums[j] == target:
            print(f"Sum of  {i} and {j} index match value == {target}")
            break



