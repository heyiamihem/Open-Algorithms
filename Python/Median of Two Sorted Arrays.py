def MedianSortedArrays(arr1, arr2):
  arr = arr1 + arr2
  arr.sort()
  n = len(arr)
  if n % 2 == 0: 
    return (arr[n//2]  + arr[n//2 - 1])/2
  return arr[n//2]

print(MedianSortedArrays([1,2,3],[3,4,5,6]))
