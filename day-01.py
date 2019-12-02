import math

def part_one( input ):
  total_fuel = 0
  for mass in input:
    fuel = math.floor(mass / 3.)
    fuel -= 2
    #print( mass, fuel)
    total_fuel += fuel

  return total_fuel

def calc_fuel( mass ):
  result = math.floor( mass / 3.0 ) - 2
  return result if result > 0 else 0

def calc( mass ):
  total = mass
  fuel_required = calc_fuel( mass )

  if fuel_required <= 0:
    return fuel_required
  else:
    return fuel_required + calc( fuel_required )

def part_two( input ):
  total_fuel = 0
  for mass in input:
    total_fuel += calc( mass )

  return total_fuel


my_input = [ 119965, 69635, 134375, 71834, 124313, 109114, 80935, 146441, 120287, 85102, 148451, 69703, 143836, 75280, 83963, 108849, 133032, 109359, 78119, 104402, 89156, 116946, 132008, 131627, 124358, 56060, 141515, 75639, 146945, 95026, 99256, 57751, 148607, 100505, 65002, 78485, 84473, 112331, 82177, 111298, 131964, 125753, 63970, 77100, 90922, 119326, 51747, 104086, 141344, 54409, 69642, 70193, 109730, 73782, 92049, 90532, 147093, 62719, 79829, 142640, 85242, 128001, 71403, 75365, 90146, 147194, 76903, 68895, 56817, 142352, 77843, 64082, 106953, 115590, 87224, 58146, 134018, 127111, 51996, 134433, 148768, 103906, 52848, 108577, 77646, 95930, 67333, 98697, 55870, 78927, 148519, 68724, 93076, 73736, 140291, 121184, 111768, 71920, 104822, 87534 ]
example = [ 12, 14, 1969, 100756 ]

print( part_one( my_input ) )
print( part_two( my_input ) )
