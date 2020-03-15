from time import time
from random import sample, randrange
from sys import setrecursionlimit

setrecursionlimit(10000)

# fill functions
def fill_random(n):
  return sample(range(10 * n), n)

def fill_increasing(n):
  return sorted(fill_random(n))

def fill_decreasing(n):
  return sorted(fill_random(n), reverse=True)

def fill_vshape(n):
  pass

# check functions
def is_random(data):
  pass

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

def insertion_sort(data):
  for index, value in enumerate(data[1:]):
    while index >= 0 and value < data[index] : 
      data[index + 1] = data[index] 
      index -= 1
    data[index + 1] = value 

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

zipped = [(fill_random, is_random),
          (fill_increasing, is_increasing),
          (fill_decreasing, is_decreasing)]

# main
for sort_function in [selection_sort, insertion_sort, quick_sort, heap_sort]:
  for fill_function, check_function in zipped:
    data = fill_function(1000)
    check_function(data)

    start = time()
    sort_function(data)
    end = time()

    is_sorted(data)
    print(f'{sort_function.__name__}\t{fill_function.__name__} {round((end - start) * 1000, 3)}')
