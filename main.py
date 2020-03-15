from time import time
from random import randrange


spread = 100

# fill functions
def fill_random(n):
  return [randrange(spread) for _ in range(n)]

def fill_increasing(n):
  return sorted([randrange(spread) for _ in range(n)])

def fill_decreasing(n):
  return sorted([randrange(spread) for _ in range(n)], reverse=True)

def fill_vshape(n):
  pass

# check functions
def is_increasing(data):
  assert all(i < j for i, j in zip(data, data[1:]))

def is_decreasing(data):
  assert all(i > j for i, j in zip(data, data[1:]))

def is_sorted(data):
  assert all(i <= j for i, j in zip(data, data[1:]))

# sort functions
def selection_sort(data):
  for index in range(len(data)): 
    selection_index = index
    for inner_index in range(index + 1, len(data)):
      if data[selection_index] > data[inner_index]:
        selection_index = inner_index
    data[index], data[selection_index] = data[selection_index], data[index]
  return data

def insertion_sort(data):
  for index, value in enumerate(data[1:]):
    while index >= 0 and value < data[index] : 
      data[index + 1] = data[index] 
      index -= 1
    data[index + 1] = value 
  return data

def partition(data, low, high):
  for inner_index in range(low + 1, high):
    if data[inner_index] <= data[high]:
      low += 1
      data[low], data[inner_index] = data[inner_index], data[low]
  data[low + 1], data[high] = data[high], data[low + 1]
  return low + 1

def quick_sort(data, low=None, high=None):
  if low is None and high is None:
    return quick_sort(data, 0, len(data) - 1)
  if low < high:
    index = partition(data, low - 1, high)
    quick_sort(data, low, index - 1)
    quick_sort(data, index + 1, high)
  return data

def heapify(data, high, low): 
  largest = low

  left = 2 * low + 1
  if left < high and data[low] < data[left]:
    largest = left

  right = 2 * low + 2
  if right < high and data[largest] < data[right]:
    largest = right

  if largest != low:
    data[low], data[largest] = data[largest], data[low]
    heapify(data, high, largest)

def heap_sort(data):
  for index in range(len(data), -1, -1):
    heapify(data, len(data), index)
  for index in range(len(data) - 1, 0, -1):
    data[index], data[0] = data[0], data[index]
    heapify(data, index, 0)
  return data

# main
for sort_function in [selection_sort, insertion_sort, quick_sort, heap_sort]:
  for fill_function in [fill_random, fill_increasing, fill_decreasing]:
    data = fill_function(10)

    start = time()
    data = sort_function(data)
    end = time()
    print(end - start)



    if data:
      is_sorted(data)
    print(f'{sort_function.__name__}\t{fill_function.__name__} {end - start:.8} {data}')