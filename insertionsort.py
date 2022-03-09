# Insertion Sort - iterative
def insertionsort(ls):
  i = 1
  while i < len(ls):
    x = ls[i]
    j = i - 1
    while j >= 0 and ls[j] > x:
      ls[j + 1] = ls[j]
      j -= 1
    ls[j + 1] = x
    i += 1
  return ls

print(insertionsort([2,4,1,4,15,7]))