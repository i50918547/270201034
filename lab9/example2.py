def get_reversed(l):
  if len(l) == 0:
    return []
  return [l.pop()] + get_reversed(l)

print(get_reversed([1, 2, 3, 4]))
  
