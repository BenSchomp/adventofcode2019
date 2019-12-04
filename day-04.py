low = 359282
high = 820401

def is_valid( n ):
  has_double1 = has_double2 = False
  matches = 0
  prev = int(n[0])
  for i in n[1:]:
    cur = int(i)
    if cur < prev:
      return (False, False)
    elif cur == prev:
      has_double1 = True
      matches += 1
    else:
      if matches == 1:
        has_double2 = True
      matches = 0

    prev = cur

  return (has_double1, has_double2 or matches == 1)

count1 = count2 = 0
for i in range(low, high+1):
  cur = str(i)
  (valid1, valid2) = is_valid(cur)
  if valid1:
    count1 += 1
  if valid2:
    count2 += 1

print(count1, count2)
