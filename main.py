"""
CMPS 2200  Recitation 1
"""

import tabulate
import time


###

def linear_search(mylist, key):
    """ done. """
    for i, v in enumerate(mylist):
        if v == key:
            return i
    return -1

def test_linear_search():
    """ done. """
    assert linear_search([1, 2, 3, 4, 5], 5) == 4
    assert linear_search([1, 2, 3, 4, 5], 1) == 0
    assert linear_search([1, 2, 3, 4, 5], 6) == -1

def binary_search(mylist, key):
    """ done. """

    return _binary_search(mylist, key, 0, len(mylist) - 1)



def _binary_search(mylist, key, left, right):
  while left <= right:
    mid = (left + right) // 2
    if mylist[mid] == key:
        return mid
    elif mylist[mid] > key:
        right = mid - 1
    else:
        left = mid + 1
  return -1

def test_binary_search():
  assert binary_search([1,2,3,4,5], 5) == 4
  assert binary_search([1,2,3,4,5], 1) == 0
  assert binary_search([1,2,3,4,5], 6) == -1
  assert binary_search([5,6,7,8,9], 6) == 1
  assert binary_search([5,6,7,8,9], 8) == 3

def time_search(search_fn, mylist, key):
    start = time.time()
    result = search_fn(mylist, key)
    end = time.time()
    return (end - start) * 1000, result  # Return both time and result


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  results = []
  for n in sizes:
    n = int(n)
    mylist = list(range(n))
    key = -1
    linear_search_time, linear_search_result =       time_search(linear_search, mylist, key)
  binary_search_time, binary_search_result = time_search(binary_search, mylist, key)
  results.append((n, linear_search_time, linear_search_result,   binary_search_time, binary_search_result))
  return results
 




def print_results(results):
    """ done """
    print(tabulate.tabulate(results,
                            headers=['n', 'linear', 'binary'],
                            floatfmt=".3f",
                            tablefmt="github"))

 
print_results(compare_search())