from list_functions import *
from random import randint

array = [randint(0, 100) for i in range(10)]
print('1. Sort function:\nGiven list:', *array)
print('Sorted list in ascending order:', *sort_list(array))
print('Sorted list in descending order:', *sort_list(array, False))

array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'd']
element = 'd'
print('\n2. Search element function:\nGiven list:', *array, '\nElement {} is at the position'.format(element),
      *search_elem_by_value(array, 'd'))
print(search_elem_by_value(array, 'i'))


sequence = ['d', 'e', 'f']
print('\n3. Search sequence function:\nGiven list:', *array, 
      '\nSequence', *sequence, 'found at the positions:',
      search_sequence(array, sequence))
print(search_sequence(array, ['r', 't', 'o']))

array = [randint(0, 100) for i in range(10)]
num = 5
print('\n4. Search {} minimal elements in a given list:'.format(num), *array)
print(*search_first_elemnts(array, 5))

print('\n5. Search {} maximal elements in a given list:'.format(num), *array)
print(*search_first_elemnts(array, 5, False))
print(search_first_elemnts(array, 15, False))

print('\n6. Average value of a given list:', *array, ' - ', average(array))
print('Average value of an empty list:', average([]))


array = ['a', 'b', 'b', 'c', 'd', 'a', 't', 'e', 'c']
print('\n7. Remove duplicates function:\nOriginal list:', *array, '\nNew array: ', *del_dupl(array))