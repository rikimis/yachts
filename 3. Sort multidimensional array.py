# 3. Sort multidimensional array

x = [{"name" : "John Doe","age" : 55},
    {"name" : "Richard Roe","age" : 36},
    {"name" : "Ben Dover","age" : 99},
    {"name" : "Dev Null","age" : 12},
    {"name" : "Vymyslene","age" : 12},
    {"name" : "Vymyslene2","age" : 12},
    {"name" : "Mike Rotch","age" : 43}]

def print_array(array):
  for item in array:
    print(item)
  print()


def sortMultiArray(array):
  new = sorted(array, key = lambda d: d['age'])
  del array[:]
  return array.extend(new)
  
print_array(x)
sortMultiArray(x)
print_array(x)

