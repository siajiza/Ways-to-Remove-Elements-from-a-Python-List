# Work with elements from a list[ ] on Python: Remove, change or sustite.

<h3>List´s created, so could be exist changes like remove, includ or sustituve.</h3>

<h2>Inicial List # These are the new users List.</h2>

List_user = ['Ana', 'Paz', 'Lola'] 

    print(List_user) 
    ['Ana', 'Paz', 'Lola']

<h2>List 1º changes # we add a new element on the index [0] (position zero). </h2>

List_user.insert(0, 'Max') 

    print(List_user) 
    ['Max', 'Ana', 'Paz', 'Lola']


<h2>List 2º change # we add a new element at the end of the list.</h2>

List_user.append('Teo') 

    print(List_user) 
    ['Max', 'Ana', 'Paz', 'Lola']


<h2>List 3º change # we must sustitue the exinting element called "Ana" for a correct item called "Leo".</h2>

List_user[1] = 'Leo' 

    print(List_user)  
    ['Max', 'Leo', 'Paz', 'Lola', 'Teo']
    

<h1># Now, we will learn to remove the elements: remove( ), pop( ) and del.</h1>

<h2>List 4º change # we remove the element from the List_user.</h2>

List_user.remove('Paz') 

    print(List_user)
    ['Max', 'Leo', 'Lola', 'Teo']


<h1>#Now, we popped(remove) the very last element.</h1>

With pop() but we don-t only remove we can use this items to another varible, so this "pop()" is going to gives us the avility to use this items on another place.

<h2>List 5º change</h2>

popped_List_user = List_user.pop()

<h4>Using popped</h4>

    print(popped_List_user)
    Teo

<h4>Using removed # print the list insted of to return the item to use it on another place.</h4>

    print(List_user)
    ['Max', 'Leo', 'Lola']

<h2>List 6º change: Pure delete # choose the element and then you have to pass in whatever the index is. </h2>

del List_user[2] 

    print(List_user)
    ['Max', 'Leo']
    
