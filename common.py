from collections import namedtuple
Param = namedtuple('Param', 'addr value')

class Intcode:
  ADD = 1
  MULTIPLY = 2
  SET = 3
  GET = 4
  JUMPT = 5
  JUMPF = 6
  LT = 7
  EQ = 8
  ADJBASE = 9
  STOP = 99

  POSITION = 0
  IMMEDIATE = 1
  RELATIVE = 2

  def __init__( self, init_program, init_inputs=None ):
    self.program = init_program[:]
    self.max_addr = len(self.program) - 1
    self.pc = 0 # the program counter
    self.base = 0
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

  def hack( self, addr, value ):
    self.program[addr] = value

  def getParam( self, p, mode ):
    if mode == self.IMMEDIATE: # 1
      addr = self.pc + p

    elif mode == self.POSITION: # 0
      addr = self.program[self.pc + p]

    elif mode == self.RELATIVE: # 2
      addr = self.program[self.pc + p] + self.base

    if addr > self.max_addr:
      self.program += [0] * (addr - self.max_addr)
      self.max_addr = len(self.program) - 1

    value = int(self.program[addr])
    p = Param(addr, value)

    return p

  def process( self, new_input=None ):
    self.addInput( new_input )

    while( 1 ):
      # extract the opCode and mode settings
      #print( self.program, self.pc, self.inputs, self.base ) # DEBUG
      cur = str(self.program[self.pc]).zfill(5)
      opCode = int(cur[-2:])
      p1 = p2 = p3 = None

      # nothing to do
      if opCode == self.STOP:
        # client can check for None return as a signal that the program is done
        return None

      # extract parameters p1, p2, p3
      (mode1, mode2, mode3) = (int(cur[-3]), int(cur[-4]), int(cur[-5]))
      p1 = self.getParam( 1, mode1)

      if not opCode in [ self.SET, self.GET, self.ADJBASE ]:
        p2 = self.getParam( 2, mode2 )

      if opCode in [ self.ADD, self.MULTIPLY, self.LT, self.EQ ]:
        p3 = self.getParam( 3, mode3 )

      #print( opCode, p1, p2, p3 ) # DEBUG

      if opCode == self.ADD: # 1
        self.program[p3.addr] = p1.value + p2.value
        self.pc += 4
      elif opCode == self.MULTIPLY: # 2
        self.program[p3.addr] = p1.value * p2.value
        self.pc += 4
      elif opCode == self.SET: # 3
        if len(self.inputs) == 0:
          # not perfect, but a client can check for empty list as a signal
          #  that the input buffer is empty
          return []
        self.program[p1.addr] = self.inputs.pop(0)
        self.pc += 2
      elif opCode == self.GET: # 4
        self.pc += 2
        self.output = p1.value
        return self.output
      elif opCode == self.JUMPT: # 5
        if p1.value != 0:
          self.pc = p2.value
        else:
          self.pc += 3
      elif opCode == self.JUMPF: # 6
        if p1.value == 0:
          self.pc = p2.value
        else:
          self.pc += 3
      elif opCode == self.LT: # 7
        if p1.value < p2.value:
          self.program[p3.addr] = 1
        else:
          self.program[p3.addr] = 0
        self.pc += 4
      elif opCode == self.EQ: # 8
        if p1.value == p2.value:
          self.program[p3.addr] = 1
        else:
          self.program[p3.addr] = 0
        self.pc += 4
      elif opCode == self.ADJBASE: # 9
        self.base += p1.value
        self.pc += 2
      else:
        print( 'unknown opCode:', opCode )
        exit()
