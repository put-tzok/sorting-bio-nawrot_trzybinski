from time import process_time
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


import sys


def insertion_sort(data):
  for index, value in enumerate(data[1:]):
    while index >= 0 and value < data[index] : 
      data[index + 1] = data[index] 
      index -= 1
    data[index + 1] = value 
  return data


def quick_sort(data):
  pass

def heap_sort(data):
  pass


# main
for sort_function in [selection_sort, insertion_sort, quick_sort, heap_sort]:
  for fill_function in [fill_random, fill_increasing, fill_decreasing]:
    data = fill_function(10)

    start = process_time()
    data = sort_function(data)
    end = process_time()
    print(end - start)



    if data:
      is_sorted(data)
    print(f'{sort_function.__name__}\t{fill_function.__name__} {end - start:8.8} {data}')
