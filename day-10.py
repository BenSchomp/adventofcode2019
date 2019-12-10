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

from fractions import Fraction

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

best = 0
for location in asteroids:
  visible = set()
  for asteroid in asteroids:
    if location == asteroid:
      continue

    rise = asteroid[1]-location[1]
    run = asteroid[0]-location[0]

    if run == 0:
      if rise > 0:
        slope = 'inf'
      else:
        slope = '-inf'
    elif rise == 0:
      if run > 0:
        slope = '+0'
      else:
        slope = '-0'
    else:
      slope = Fraction( rise, run )
      # objects along the same slope are blocked,
      #  hence the tracking via the visible set
      # however the location might between in the middle
      #  of two objects on the same slope, so make each object's
      #  slope "unique" by indicating if it is to the Left or Right
      #  of vertical
      if run < 0:
        slope = str(slope)+'L'
      else:
        slope = str(slope)+'R'

    visible.add(slope)

  if len(visible) > best:
    best = len(visible)
    best_location = location

print( best, best_location )
