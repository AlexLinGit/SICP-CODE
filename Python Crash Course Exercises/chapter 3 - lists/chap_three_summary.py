every_one = ['append', 'insert', 'del', 'pop', 'remove', 'sort', 'sorted', 'reverse', 'len']
print(every_one)

#append
every_one.append('append#1')
print("\nThis is the new list #1")
print(every_one)

#insert
every_one.insert(10, 'insert#2')
print("\nThis is the new list #2")
print(every_one)

#del
del every_one[10]
print("\nDeleting the insert#2")
print(every_one)

#pop
pop_append = every_one.pop(9)
print("\nPopping append#1")
print("I just popped " + pop_append + " and it was pretty cool")
print(every_one)


#inserting extra for remove method
every_one.insert(9, 'extra')
print(every_one)

#remove
every_one.remove('extra')
print("\nRemoving the extra")
print(every_one)

#sort
every_one.sort()
print("\nI'm sorting the list")
print(every_one)

#reverse sorted
print("\nI'm temporarily reverse sorting the list")
print(sorted(every_one, reverse=True))

#"Original" list
print(every_one)

#reverse
print("\nI'm reversing the list")
every_one.reverse()
print(every_one)

#len
print("\nThis is the length of this code")
print(len(every_one))

#summary
print("\n\tAnd that is all the methods/functions learned in chapter 3!!")


