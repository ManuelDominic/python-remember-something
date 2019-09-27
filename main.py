from functools import lru_cache

# Recursive function
def fibonacci(n):
  if(n==1):
      return 1
  elif(n==2):
      return 1
  elif(n>2):
      return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 11):
  print(n, ":", fibonacci(n))

# Memorization function
fibonacci_cache={}

def fibonacci1(n):
  if(n in fibonacci_cache):
      return fibonacci_cache[n]
  if(n==1):
      value=1
  elif(n==2):
      value=1
  elif(n>2):
      value=fibonacci(n-1) + fibonacci(n-2)
  fibonacci_cache[n] = value
  return value

for n in range(1, 1001):
  print(n, ":", fibonacci1(n))



# Memorization function
@lru_cache(maxsize=1000)
def fibonacci2(n):
  if(n==1);
      return 1
  elif(n==2):
      return 1
  elif(n>2):
      return fibonacci(n-1) + fibonacci(n-2)

for n in range(1, 11):
  print(n, ":", fibonacci2(n))


# Bubble sort
def bubble_sort(nums):
  for i in range(len(nums)-1, 0, -1):
      for j in range(i):
          if num[j]>nums[j+1]:
              temp = nums[j+1]
              nums[j] = nums[j+1]
              nums[j+1] = temp

nums = [5, 3, 8, 6, 7, 2]
bubble_sort(nums)
print(nums)


# Selection sort
def selection_sort(nums):
  for i in range(5):
      minpos=1
      for j in range(i, 6):
          if num[j]>nums[minpos]:
              minpos = j
      temp = nums[i]
      nums[i] = nums[minpos]
      nums[minpos] = temp
      print(nums)

nums = [5, 3, 8, 6, 7, 2]
selection_sort(nums)
print(nums)
