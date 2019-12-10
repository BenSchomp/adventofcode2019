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

    angle = atan2(rise, run)
    visible.add(angle)

  if len(visible) > best:
    best = len(visible)
    best_location = location

print( best, best_location )
