# List items are ordered, changeable, and allow duplicate values. List is heterogenous- it can contain different data types
# By ordered we mean that the items have a defined order, and that order will not change

empty_list =[]
empty_list1 = list() #using list constructor
print(type(empty_list))
print(type(empty_list1))

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(len(thislist))
print(thislist[-1]) # -1 index refers to last element
print(thislist[0]) # 0 index refers to first element
print(thislist[2:5])
print(thislist[:4]) # index starting from 0 to 3 (4-1)
print(thislist[2:])

if "apple" in thislist:
    print("yes, apple is in the fruits list")

# changing value of a list
thislist[1]= "blackcurrent"
print(thislist)

thislist[1:2] = ["grapes","watermelon"]
print(thislist)
thislist.insert(2,"Guava")
print(thislist)
thistuple =("kiwi","orange")
thislist.extend(thistuple)
print(thislist)

"""
removing element from the list - remove, pop and del keyword
"""