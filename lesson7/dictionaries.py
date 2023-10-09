#Dictionaries

band = {
  "vocals": "Plant",
  "guitar": "Page"
}

band2 = dict(vocals = "Plants", guitar = "Page")

print(band)
print(band2)
print(type(band2))
print(len(band2))

#Access items

print(band["guitar"])
print(band.get("guitar"))

#All keys

print(band.keys())

#All values

print(band.values())

#Key/value pairs

print(band.items())

#Verify if a key exist

print("guitar" in band)
print("triangle" in band)

#Change values

band["guitar"] = "Coverdale"
band.update({
  "bass": "JPJ"
})
print(band)

#Remove values

print(band.pop("bass"))
print(band)

band["drums"] = "Bonham"
print(band)

print(band.popitem()) #remove tuple
print(band)

#Delete and clear
band["drums"] = "Bonham"
del band["drums"]
print(band)

band2.clear()
print(band2)

del band2

#Copy dictionaries

# band2 = band # create a reference
# print("Bad copy")
# print(band2)
# print(band)

# band2["drums"] = "Daniel"
# print(band)

band2 = band.copy()
band2["drums"] = "Daniel"
print("Good copy")
print(band)
print(band2)

#or use the dict() constructor function
band3 = dict(band)
print("Good copy")
print(band3)


# Nested dictionaries

member1 = {
  "name": "Plant",
  "instrument": "Vocal"
}

member2 = {
  "name": "Page",
  "instrument": "Guitar"
}

band = {
  "member1": member1,
  "member2": member2
}

print(band)
print(band["member1"]["name"])

#Sets

nums = {1,2,3,4}
nums2 = set((1,2,3,4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

#No duplicates allowed

nums = {1,2,2,3}
print(nums)

#True is a dupe of 1, False is a dupe of 0

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

#Check if a value is in a set
print(2 in nums)
#But you cannot refer to an element in the set whit an index position or a key

#Add a new value to a set
nums.add(8)
print(nums)

#Add elements from one set to another
moreNums = {5,6,7}
nums.update(moreNums)
print(nums)
#you can use update with lists, tuples and dictionaries, too.

#Merge two set to create a new set
one = {1,2,3}
two = {4,5,6}

myNewSet = one.union(two)
print(myNewSet)

#Keep only the duplicates
one = {1,2,3}
two = {2,3,4}

one.intersection_update(two)
print(one)

#Keep everything except the duplicates
one = {1,2,3}
two = {2,3,4}

one.symmetric_difference_update(two)
print(one)

