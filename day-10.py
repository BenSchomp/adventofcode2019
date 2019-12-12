my_input = [
'#..#.#.#.######..#.#...##',
'##.#..#.#..##.#..######.#',
'.#.##.#..##..#.#.####.#..',
'.#..##.#.#..#.#...#...#.#',
'#...###.##.##..##...#..#.',
'##..#.#.#.###...#.##..#.#',
'###.###.#.##.##....#####.',
'.#####.#.#...#..#####..#.',
'.#.##...#.#...#####.##...',
'######.#..##.#..#.#.#....',
'###.##.#######....##.#..#',
'.####.##..#.##.#.#.##...#',
'##...##.######..##..#.###',
'...###...#..#...#.###..#.',
'.#####...##..#..#####.###',
'.#####..#.#######.###.##.',
'#...###.####.##.##.#.##.#',
'.#.#.#.#.#.##.#..#.#..###',
'##.#.####.###....###..##.',
'#..##.#....#..#..#.#..#.#',
'##..#..#...#..##..####..#',
'....#.....##..#.##.#...##',
'.##..#.#..##..##.#..##..#',
'.##..#####....#####.#.#.#',
'#..#..#..##...#..#.#.#.##']
example1 = [
'......#.#.',
'#..#.#....',
'..#######.',
'.#.#.###..',
'.#..#.....',
'..#....#.#',
'#..#....#.',
'.##.#..###',
'##...#..#.',
'.#....####']
example2 = [
'.#....#####...#..',
'##...##.#####..##',
'##...#...#.#####.',
'..#.....#...###..',
'..#.#.....#....##']
example3 = [
'.#..##.###...#######',
'##.############..##.',
'.#.######.########.#',
'.###.#######.####.#.',
'#####.##.#.##.###.##',
'..#####..#.#########',
'####################',
'#.####....###.#.#.##',
'##.#################',
'#####.##.###..####..',
'..######..##.#######',
'####.##.####...##..#',
'.#####..#.######.###',
'##...#.##########...',
'#.##########.#######',
'.####.#.###.###.#.##',
'....##.##.###..#####',
'.#.#.###########.###',
'#.#.#.#####.####.###',
'###.##.####.##.#..##']

from math import atan2, sqrt, pi

def getAngle( source, dest ):
  rise = source[1]-dest[1]
  run = source[0]-dest[0]

  angle = atan2(rise, run)
  return angle

def getDist( source, dest ):
  return sqrt((dest[0]-source[0])**2 + (dest[1]-source[1])**2)

asteroids = set() 
y = 0
for line in my_input:
  x = 0
  for digit in line:
    if digit == '#':
      asteroids.add((x,y))
    x += 1
  y += 1

height = y
width = x

# part_one
best = 0
for location in asteroids:
  visible = set()
  for asteroid in asteroids:
    if location == asteroid:
      continue

    visible.add( getAngle( location, asteroid ) )

  if len(visible) > best:
    best = len(visible)
    best_location = location

print( 'part_one:', best )

# part_two
# calculate angle and distance from laser location to each asteroid
targets = {}
angles = set()
for asteroid in asteroids:
  x = asteroid[0]
  y = asteroid[1]
  angle = getAngle( best_location, asteroid )
  distance = getDist( best_location, asteroid )
  node = (distance, (x,y))
  if angle not in targets:
    targets[angle] = [node]
  else:
    targets[angle].append( node )
    targets[angle].sort()

  angles.add( angle )

angles = sorted(angles)

# start laser straight up (ie pi/2)
a = 0
num_angles = len(angles)
while a < num_angles and angles[a] < (pi/2):
  a += 1

# laser is set ... start shootin' shit
count = 0
while len(targets) > 0:
  cur_angle = angles[a]

  if cur_angle in targets:
    count += 1
    casualty = targets[cur_angle].pop(0)
    #print( count, casualty[1], cur_angle, casualty[0] )

    if len(targets[cur_angle]) < 1:
      del targets[cur_angle]

    if count == 200:
      print( 'part_two:', casualty[1][0]*100 + casualty[1][1] )
      exit()

  a = (a + 1) % num_angles
