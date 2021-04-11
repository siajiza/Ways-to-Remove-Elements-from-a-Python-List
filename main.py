# List´s created, so could be exist changes like remove, includ or sustituve. [ ]

print('-----Inicial List')

List_user = ['Ana', 'Paz', 'Lola'] # These are the new users List.

print(List_user) # Inicial List ['Ana', 'Paz', 'Lola']
print('\n')
print('-----List 1º change')

List_user.insert(0, 'Max') # we add a new element on the position zero. 

print(List_user) # List 1º change ['Max', 'Ana', 'Paz', 'Lola']
print('\n')
print('-----List 2º change')

List_user.append('Teo') # we add a new element at the end of the list.

print(List_user) # List 2º change ['Max', 'Ana', 'Paz', 'Lola']
print('\n')
print('-----List 3º change')

List_user[1] = 'Leo' # we must sustitue the exinting element called "Ana" for a correct item called "Leo".

print(List_user) # List 3º change ['Max', 'Leo', 'Paz', 'Lola', 'Teo']


# Now we must remove the element []
print('\n')
print('-----List 4º change')

List_user.remove('Paz') # we remove the element from the List_user.

print(List_user)

# Now we popped(remove) the very last element
# with pop() but we don-t only remove we can use this items to another varible, so this "pop()" is going to gives us the avility to use this items on another place.
print('\n')
print('-----List 5º change')

popped_List_user = List_user.pop()

print('-----popped-----')
print(popped_List_user)
print('\n')
print('-----removed-----')
print(List_user)

# Pure delete
print('\n')
print('-----List 6º change')

del List_user[2] # choose the element and then you have to pass in whatever the index is. 

print(List_user)

