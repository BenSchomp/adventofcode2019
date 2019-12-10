my_input = [ 3,8,1001,8,10,8,105,1,0,0,21,38,63,72,81,106,187,268,349,430,99999,3,9,101,5,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,102,3,9,9,101,4,9,9,1002,9,2,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,102,4,9,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,102,3,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99 ]
example = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
example2 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]

ADD = 1
MULTIPLY = 2
SET = 3
GET = 4
JUMPT = 5
JUMPF = 6
LT = 7
EQ = 8
STOP = 99
POSITION = '0'
IMMEDIATE = '1'

def process( data, i, the_input ):
  output = None
  while( 1 ):
    #print( data )
    cur = str(data[i]).zfill(5)
    opCode = int(cur[-2:])
    (mode1, mode2, mode3) = (cur[-3], cur[-4], cur[-5])

    if opCode == STOP:
      return None

    if opCode in [ SET ]:
      p1 = int(data[i+1])
    else:
      p1 = int(data[data[i+1]]) if mode1 == POSITION else int(data[i+1])
    if not opCode in [ SET, GET ]:
      p2 = int(data[data[i+2]]) if mode2 == POSITION else int(data[i+2])
    if opCode in [ ADD, MULTIPLY, LT, EQ ]:
      p3 = int(data[i+3])

    if opCode == ADD:
      data[p3] = p1 + p2
      i += 4
    elif opCode == MULTIPLY:
      data[p3] = p1 * p2
      i += 4
    elif opCode == SET:
      data[p1] = the_input.pop(0)
      i += 2
    elif opCode == GET:
      i += 2
      return (p1, i)
    elif opCode == JUMPT:
      if p1 != 0:
        i = p2
      else:
        i += 3
    elif opCode == JUMPF:
      if p1 == 0:
        i = p2
      else:
        i += 3
    elif opCode == LT:
      if p1 < p2:
        data[p3] = 1
      else:
        data[p3] = 0
      i += 4
    elif opCode == EQ:
      if p1 == p2:
        data[p3] = 1
      else:
        data[p3] = 0
      i += 4
    else:
      print( 'unknown opCode:', opCode )
      exit(-1)


def part_one( data ):
  max = 0
  for a in range(5):
    for b in range(5):
      if b == a:
        continue
      for c in range(5):
        if c in [a,b]:
          continue
        for d in range(5):
          if d in [a,b,c]:
            continue
          for e in range(5):
            if e in [a,b,c,d]:
              continue

            result = 0
            for phase in [a,b,c,d,e]:
              (result, x) = process( data[:], 0, [phase,result])
            if result > max:
              max = result

  return max

def part_two( data ):

  max = 0
  for a in range(5):
    for b in range(5):
      if b == a:
        continue
      for c in range(5):
        if c in [a,b]:
          continue
        for d in range(5):
          if d in [a,b,c]:
            continue
          for e in range(5):
            if e in [a,b,c,d]:
              continue

            phases = [x+5 for x in [a,b,c,d,e]]

            amp_data = []
            amp_input = []
            result = []
            pc = []
            for i in range(5):
              amp_data.append( data[:] )
              result.append(0)
              pc.append(0)
              amp_input.append([phases[i]])
            amp_input[0].append(0)

            cur_amp = 0
            while( 1 ):
              last_result = process( amp_data[cur_amp], pc[cur_amp], amp_input[cur_amp])
              if last_result:
                (result[cur_amp], pc[cur_amp]) = last_result
              else:
                break

              cur_amp = (cur_amp + 1) % 5
              amp_input[cur_amp].append(last_result[0])

            if result[4] > max:
              max = result[4]

  return max

print( part_one( my_input ) )
print( part_two( my_input ) )
