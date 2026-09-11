import array as arr

num = arr.array('i',[1,2,3,4,5,6])
print(num)
print(num[0])
num.append(7)
print(num)


a = arr.array('i', [1, 2, 3])
a.insert(0,4)

for i in range(0, 3):
    print(a[i], end=" ")
a.append(10)
print(a)

nums = arr.array('i',[1,2,3,4,5,6,7,8,1,2,3,4,5,1,2,3,4,1,2,2])
count = nums.count(2)
print(count)

nums.extend([10,11,12,14,15])
print(*nums)
nums.reverse()
print(*nums)
for i in nums:
    print(i)
