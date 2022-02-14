# 2. Sort array

def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1


def quickSort1(array, low, high):
  if low < high:
    pivot = partition(array, low, high)
    quickSort1(array, low, pivot - 1)
    quickSort1(array, pivot + 1, high)

def quickSort(array):
    quickSort1(array, 0, len(array) - 1)


array = [7, 5, 1, 12, 7, 135, 1, -12]
print(array)
quickSort(array)
print(array)
