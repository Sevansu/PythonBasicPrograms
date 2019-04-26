def sort(x):
      if len(x) < 2:
          return x
      else:
          p = x[0]
          less = [i for i in x[1:] if i <= p]
          greater = [i for i in x[1:] if i > p]
          return sort(less) + [p] + sort(greater)


arr = [10, 7, 8, 9, 1, 5, 2, 4, 3, 6]
print("Sorted array")
print(sort(arr))
