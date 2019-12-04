low = 359282
high = 820401

def is_valid( n ):
  has_double = False
  prev = int(n[0])
  for i in n[1:]:
    cur = int(i)
    if cur < prev:
      return False
    elif cur == prev:
      has_double = True

    prev = cur
    
  return has_double

def is_valid2( n ):
  has_double = False
  matches = 0
  prev = int(n[0])
  for i in n[1:]:
    cur = int(i)
    if cur < prev:
      return False
    elif cur == prev:
      matches += 1
    else:
      if matches == 1:
        has_double = True
      matches = 0

    prev = cur

  return has_double or matches == 1

count = count2 = 0
for i in range(low, high+1):
  cur = str(i)
  if is_valid(cur):
    count += 1
  if is_valid2(cur):
    count2 += 1

print( count, count2 )
