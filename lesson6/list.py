users = ['Daniel', 'Pedro', 'Ana']
data = ['Daniel', 13, 2]
emptyList = []

print("Daniel" in users)
print(users[0])
print(users[-1])

print(users.index('Ana'))

print(users[0:2])
print(users[0:])

print (len(data))

users.append('Sofia')
print(users)

users += ['JSON']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Bob')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Robert', 'JPJ']
print(users)

users.remove('Bob')
print(users)

print(users.pop())
print(users)

del users[0]
print(users)

data.clear()
print(data)

users[1:2] = ['dave']
users.sort()
print(users)

users.sort(key=str.lower)
print(users)

nums = [4, 15, 55, 410, 1, 3]
nums.reverse()
print(nums)

# nums.sort(reverse=True)
# print(nums)

print(sorted(nums, reverse=True))

numsCopy = nums.copy()
myNums = list(nums)
myCopy = nums[:]

print(numsCopy)
print(myNums)
myCopy.sort()
print(myCopy)
print(nums)

print(type(nums))

myList = list([1, 'Diana', True])
print(myList)

#*Tuples

myTuple = tuple(('Dave', 42, True))
anotherTuple = (1,1,3,4)

print(myTuple)
print(type(myTuple))
print(type(anotherTuple))

newList = list(myTuple)
newList.append('Neil')
newTuple = tuple(newList)
print(newTuple)