my_input = [ 3,8,1001,8,10,8,105,1,0,0,21,38,63,72,81,106,187,268,349,430,99999,3,9,101,5,9,9,1002,9,3,9,101,3,9,9,4,9,99,3,9,102,3,9,9,101,4,9,9,1002,9,2,9,1001,9,2,9,1002,9,4,9,4,9,99,3,9,1001,9,3,9,4,9,99,3,9,102,5,9,9,4,9,99,3,9,102,4,9,9,1001,9,2,9,1002,9,5,9,1001,9,2,9,102,3,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,99 ]
example = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
example2 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]


class Intcode:
  ADD = 1
  MULTIPLY = 2
  SET = 3
  GET = 4
  JUMPT = 5
  JUMPF = 6
  LT = 7
  EQ = 8
  STOP = 99

  POSITION = 0
  IMMEDIATE = 1
  RELATIVE = 2

  def __init__( self, init_program, init_inputs=None ):
    self.program = init_program[:]
    self.pc = 0 # the program counter
    self.inputs = []
    self.addInput( init_inputs )
    self.output = None

  def getOutput( self ):
    return self.output

  def addInput( self, new_input=None ):
    if new_input is not None:
      if isinstance( new_input, list ):
        self.inputs += new_input
      else:
        self.inputs.append( new_input )

  def process( self, new_input=None ):
    self.addInput( new_input )

    i = self.pc
    data = self.program
    while( 1 ):
      # extract the opCode and mode settings
      cur = str(data[i]).zfill(5)
      opCode = int(cur[-2:])
      (mode1, mode2, mode3) = (int(cur[-3]), int(cur[-4]), int(cur[-5]))

      # nothing to do
      if opCode == self.STOP:
        self.pc = i
        return None

      # extract parameters p1, p2, p3
      if opCode in [ self.SET ]:
        p1 = int(data[i+1])
      else:
        p1 = int(data[data[i+1]]) if mode1 == self.POSITION else int(data[i+1])

      if not opCode in [ self.SET, self.GET ]:
        p2 = int(data[data[i+2]]) if mode2 == self.POSITION else int(data[i+2])

      if opCode in [ self.ADD, self.MULTIPLY, self.LT, self.EQ ]:
        p3 = int(data[i+3])

      if opCode == self.ADD:
        data[p3] = p1 + p2
        i += 4
      elif opCode == self.MULTIPLY:
        data[p3] = p1 * p2
        i += 4
      elif opCode == self.SET:
        data[p1] = self.inputs.pop(0)
        i += 2
      elif opCode == self.GET:
        i += 2
        self.pc = i
        self.output = p1
        return self.output
      elif opCode == self.JUMPT:
        if p1 != 0:
          i = p2
        else:
          i += 3
      elif opCode == self.JUMPF:
        if p1 == 0:
          i = p2
        else:
          i += 3
      elif opCode == self.LT:
        if p1 < p2:
          data[p3] = 1
        else:
          data[p3] = 0
        i += 4
      elif opCode == self.EQ:
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
              amp = Intcode( data[:] )
              result = amp.process( [phase,result])
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

            amp = []
            for p in phases:
              amp.append( Intcode(data[:], p) )

            cur = 0
            last_result = 0
            while( last_result is not None ):
              last_result = amp[cur].process( last_result )
              cur = (cur + 1) % 5

            if amp[4].getOutput() > max:
              max = amp[4].getOutput()

  return max

print( part_one( my_input ) )
print( part_two( my_input ) )
