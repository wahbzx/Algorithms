
# Iteratively
def binSearch(ls, target):
  # left and right pointers initialised at beginning and end of list
  l = 0
  r = len(ls)-1
  while l <= r:
    mid = l + (r - l)//2
    # Target found
    if ls[mid] == target:
      return mid
    # Check the right half of the list
    if ls[mid] < target:
      l = mid + 1
    # Check the left half of the list
    else:
      r = mid - 1
  # Returns -1 if element is not found
  return -1

# Example: print(binSearch([1,2,3,4,5,6,7,8,9],9))  


  
