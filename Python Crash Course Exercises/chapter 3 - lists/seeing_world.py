tourism = ['asutralia', 'antarctica', 'switzerland', 'france', 'africa']
print(tourism)

print("\nSorting the list #1")
print(sorted(tourism))

print("\nPrinting the original list")
print(tourism)

print("\nSorted in reverse")
print(sorted(tourism, reverse=True))

print("\nThis is the original list #2")
print(tourism)

print("\nReversing the order of the list")
tourism.reverse()
print(tourism)

print("\nChanging back to original order #3")
tourism.reverse()
print(tourism)

print("\nSorting the list in alphabetical order")
tourism.sort()
print(tourism)

print("\nSorting the list in reverse alphabetical order")
tourism.sort(reverse=True)
print(tourism)
