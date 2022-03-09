from operator import truediv


def bubblesort(ls):
  is_sorted = False
  while not is_sorted:
    swap_made = False
    for i in range(1, len(ls)):
      if ls[i] < ls[i-1]:
        n1 = ls[i]
        n2 = ls[i-1]
        ls[i] = n2
        ls[i-1] = n1 
        swap_made = True
    if not swap_made:
      is_sorted = True
  return ls

print(bubblesort([2,3,1,3,1,4,6,8]))
