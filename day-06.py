example = [ 'COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L' ]
example.append( 'K)YOU')
example.append( 'I)SAN')
uom = {}


def walk1( name, height ):
  node = uom[name]
  children_score = 0
  for child in node:
    children_score += walk1( child, height+1)

  return height + children_score

def walk2( name ):
  node = uom[name]
  children_score = 0
  found = False

  for child in node:
    child_score = walk2( child )
    if child_score >= 0:
      children_score += child_score

      if found:
        print( 'part_two', children_score )
        exit()

      found = True

  if name == 'YOU' or name == 'SAN':
    return 0
  if found:
    return children_score + 1
  return -1 

# build the tree
file = open('day-06.txt', 'r')
for line in file:
  line = line.strip()
  (parent, child) = line.split(')')

  if child not in uom:
    uom[child] = []

  if parent not in uom:
    uom[parent] = [child]
  else:
    uom[parent].append(child)

file.close()
#print( uom )

# walk and score the tree
print( 'part_one', walk1( 'COM', 0 ) )
walk2( 'COM' )



