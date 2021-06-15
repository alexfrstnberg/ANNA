def sort_list(lst, asc_ord=True):
    """Bubble sort of a given list. Returns new list"""

    n = len(lst)
    temp = lst.copy()
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):   
            if asc_ord == True:
                if temp[j] > temp[j + 1]:
                    temp[j], temp[j + 1] = temp[j + 1], temp[j]
            else:
                if temp[j] < temp[j + 1]:
                    temp[j], temp[j + 1] = temp[j + 1], temp[j]
            already_sorted = False
        if already_sorted:
            break

    return temp

def search_elem_by_value(lst, value):
    """Returns element index by its value
    and False if element is not found"""
    
    indices = [i for i, x in enumerate(lst) if x == value]
    
    if len(indices) != 0: return indices
    else:
       try: lst.index(value)
       except ValueError as err: return str(err)


def search_sequence(lst, seq):
    """Returns start index of the searched sequence
    and False if it's not found"""

    return str(lst.index(seq[0])) + '-' + str(lst.index(seq[-1])) \
        if str(seq)[1:-1] in str([lst]) else 'Sequence ' + str(seq)[1:-1] + ' not found'


def search_first_elemnts(lst, num, min=True):
    """Returns first specified number of minimal elements from list"""
    
    try:
        if num > len(lst):
            raise
        temp = lst
        return sort_list(temp)[:num] if min==True else sort_list(temp, False)[:num]
    except: return 'List length {} is less than specified number of elements {}'.format(len(lst), num)
    


def average(lst):
    """Returns average value of the list"""

    try: return sum(lst)/len(lst)
    except: return 'List length isn\'t enough to calculate average value'


def del_dupl(lst):
    """Returns a list without duplicates"""
   
    res = []
    for i in lst:
        if i not in res: res.append(i)
    return res

   