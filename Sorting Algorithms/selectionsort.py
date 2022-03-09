# Selection Sort
def selectionsort(ls):
  for i in range(0, len(ls)):
    x = ls[i]
    minIndex = i
    for j in range(i, len(ls)):
      if ls[j] < ls[minIndex]:
        minIndex = j
    # Swap the new minimum and the current elem
    ls[i] = ls[minIndex]
    ls[minIndex] = x
  return ls

# Example
# print(selectionsort([2,3,1,3,1,234,2,9]))