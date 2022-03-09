# Recursive Quicksort solution
def quicksort(ls):
  if (len(ls) == 0) :
    return ls
  else:
    mid = ls.pop(0)
    left  = quicksort(list(filter(lambda x: (x >= mid),ls)))
    right = quicksort(list(filter(lambda x: (x < mid),ls)))
    return right + [mid] + left


# Example
# a = quicksort([3,4,2,12,1,3,4,5,2,12,2,31,2,12,13,1,3,2])
# print(a)