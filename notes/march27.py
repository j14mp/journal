import copy

"""
enumerate()
================
Stop using the range(len(someList)) technique. User enumerate() instead.
Enumerate returns two values: the index of the item in a list and the item in the list itself
"""
print('This uses the enumerate() function.')
guns = ['colt', 'beretta', 'arex', 'sig sauer', 'glock', 'canik']
for index, item in enumerate(guns):
	print(f'This is index {index}: {item}.')


"""
sort()
================
sort() modifes the list in place while sorted() returns a copy of a sorted list
"""
print('\nPrinting guns list:')
print(guns)
print('Printing sorted guns list:')
print(sorted(guns))
print('Printing guns list again to show it has not been modifed:')
print(guns)
print('using sort() on guns list to show modifications:')
guns.sort()
print(guns)
print('\n')


"""
\ is a line continuation character.
"""
a = 1 + 2 \
 + 3
print(a)
"""
If multiple string literals are used consecutively, they will be concatenated.
Will not work if a string literal is followed by a non-literal.
i.e. b = 'aaa' c 'bbb'
This is useful if you want to concatenate long strings.
"""
b = 'aaa' 'bbb'
print(b)
s = 'https://ja.wikipedia.org/wiki/'\
    '%E3%83%97%E3%83%AD%E3%82%B0%E3%83'\
    '%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E'

print(s)

"""
variables store references to to values and not the actual values.
Assigning immutable types to variables will change the reference id,
but modifying mutable types will not
"""
print('\n')
spam = 100
print(f'printing spam: {spam}')
print(f'spam id is {id(spam)}')
eggs = spam
print(f'eggs id is {id(eggs)}')
print(f'printing eggs: {eggs}')
print(f'Is the id of spam equal to the id of eggs? : {id(spam) == id(eggs)}')
spam = 42
print('Changing spam to 42...')
print(f'printing spam: {spam}')
print(f'spam id is {id(spam)}')
print(f'printing eggs: {eggs}')
print(f'eggs id is {id(eggs)}')
print(f'Is the id of spam equal to the id of eggs? : {id(spam) == id(eggs)}\n')

cheese = [1,2,3,4,5]
crackers = cheese
crackers.append('mozabique')
print(cheese)
print(crackers)
print(id(cheese) == id(crackers))

biscuit = [1,2,3,4,5]
triscuit = biscuit[::]
print(f'biscuit id: {id(biscuit)}')
print(f'triscuit id: {id(triscuit)}')

band = [1,2,3,4,5]
sand = copy.copy(band)
sand[0] = 'granule'
print(band)
print(sand)

"""
Use .keys() or .values() to find something in a dictionary
"""
dogs = {'Sparky' : 3, 'Matilda' : 10, 'Gold' : 7}

print('Sparky' in dogs.keys())
print('Bud' in dogs.keys())
print(1 in dogs.values())
print(7 in dogs.values())

"""
setdefault()
================
setdefault() sets a dictionary value using one line if a key does not already exist
"""

shrek = {'shrek' : 'ogre', 'donkey' : 'donkey'}
# use this
shrek.setdefault('puss', 'cat')
print(shrek)
"""
not this:
shrek = {'shrek' : 'ogre', 'donkey' : 'donkey'}
if 'puss' not in shrek:
	shrek['puss'] = 'cat'
"""
message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message:
	count.setdefault(character, 0)
	count[character] = count[character] + 1

print(count)



