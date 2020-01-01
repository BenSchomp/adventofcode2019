example = [(-1,0,2),(2,-10,-7),(4,-8,8),(3,5,-1)]
example2 = [(-8, -10, 0), (5, 5, 10), (2, -7, 3), (9, -8, -3)]
my_input = [(3, 3, 0), (4, -16, 2), (-10, -6, 5), (-3, 0, -13)]

class Moon:
	def __init__( self, init_pos=None ):
		self.x = self.y = self.z = 0
		self.dx = self.dy = self.dz = 0

		if init_pos is not None:
			(self.x, self.y, self.z) = init_pos

	def __repr__( self ):
		result = ("<(%d, %d, %d) +/- (%d, %d, %d)>" %
		  (self.x, self.y, self.z, self.dx, self.dy, self.dz))
		return result

	def getPotentialEnergy( self ):
		return abs(self.x) + abs(self.y) + abs(self.z)

	def getKineticEnergy( self ):
		return abs(self.dx) + abs(self.dy) + abs(self.dz)

	def getTotalEnergy( self ):
		return self.getPotentialEnergy() * self.getKineticEnergy()

	def updateGravity( self, other ):
		if( self.x > other.x ):
			self.dx -= 1
			other.dx += 1
		elif( self.x < other.x ):
			self.dx += 1
			other.dx -= 1
		if( self.y > other.y ):
			self.dy -= 1
			other.dy += 1
		elif( self.y < other.y ):
			self.dy += 1
			other.dy -= 1
		if( self.z > other.z ):
			self.dz -= 1
			other.dz += 1
		elif( self.z < other.z ):
			self.dz += 1
			other.dz -= 1

	def applyVelocity( self ):
		self.x += self.dx
		self.y += self.dy
		self.z += self.dz

class System:
	def __init__( self, initial_scan ):
		self.moons = []
		for m in initial_scan:
			moon = Moon( m )
			self.moons.append(moon)

		self.num_moons = len(self.moons)

	def updateMoons( self, steps=None ):
		if steps is None:
			steps = 1

		for step in range(steps):
			for i in range(self.num_moons):
				for j in range(i+1, self.num_moons):
					self.moons[i].updateGravity( self.moons[j] )

			for m in self.moons:
				m.applyVelocity()

	def display( self ):
		print( self.moons )
		print( self.getTotalEnergy() )

	def getTotalEnergy( self ):
		result = 0
		for m in self.moons:
			result += m.getTotalEnergy()

		return result

def part_one( scan, steps ):
	s = System(scan)
	s.updateMoons(steps)
	s.display()

part_one( my_input, 1000 )

