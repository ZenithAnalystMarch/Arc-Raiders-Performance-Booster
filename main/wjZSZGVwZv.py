def fibonacci(n):
 if n <= 0:
  return []
 if n == 1:
  return [0]
 if n == 2:
  return [0, 1]
 fib_seq = [0, 1]
 for i in range(2, n):
  fib_seq.append(fib_seq[-1] + fib_seq[-2])
 return fib_seq

def prime(n):
 if n <= 1:
  return False
 for i in range(2, int(n ** 0.5) + 1):
  if n % i == 0:
   return False
 return True

def primes_up_to(n):
 return [i for i in range(2, n + 1) if prime(i)]

def is_palindrome(s):
 return s == s[::-1]

def filter_palindromes(words):
 return [word for word in words if is_palindrome(word)]

def factorial(n):
 if n == 0:
  return 1
 return n * factorial(n - 1)

def gcd(a, b):
 while b:
  a, b = b, a % b
 return a

def lcm(a, b):
 return abs(a * b) // gcd(a, b)

def count_vowels(s):
 return sum(1 for char in s if char.lower() in 'aeiou')

def reverse_words(s):
 return ' '.join(s.split()[::-1])

def char_count(s):
 return {char: s.count(char) for char in set(s)}

def flatten(nested_list):
 return [item for sublist in nested_list for item in sublist]

def unique(lst):
 return list(set(lst))

def merge_dicts(dict1, dict2):
 return {**dict1, **dict2}

def sort_dict_by_value(d):
 return dict(sorted(d.items(), key=lambda item: item[1]))

def binary_search(arr, target):
 left, right = 0, len(arr) - 1
 while left <= right:
  mid = (left + right) // 2
  if arr[mid] == target:
   return mid
  elif arr[mid] < target:
   left = mid + 1
  else:
   right = mid - 1
 return -1

def selection_sort(arr):
 for i in range(len(arr)):
  min_idx = i
  for j in range(i + 1, len(arr)):
   if arr[j] < arr[min_idx]:
    min_idx = j
  arr[i], arr[min_idx] = arr[min_idx], arr[i]
 return arr
