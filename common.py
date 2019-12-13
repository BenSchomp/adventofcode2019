
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
