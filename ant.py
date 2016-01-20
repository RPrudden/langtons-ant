import numpy as np

class Moves():
	def __init__(self):
		self.moves = []


	def add(self, move):
		if not len(self.moves) < 104:
			self.moves = self.moves[1:]
		self.moves.append(move)


class Ant():
	compass = {'N':(0,1), 'E':(1,0), 'S':(0,-1), 'W':(-1,0)}
	ways = {'L':[[0,1],[-1,0]], 'R':[[0,-1],[1,0]]}

	def __init__(self, direction='N', position=(0,0)):
		'''
		Args: 
		  * direction (str): N,E,S,W
		  * position (tuple): x and y position (ints)
		'''
		self.invcompass = {self.compass[d]:d for d in self.compass.keys()}

		self.direction = self.compass[direction]
		self.position = position

		self.memory = Moves()


	def getDirection(self):
		'''
		Get compass direction (N/E/S/W).
		'''
		return self.invcompass[self.direction]


	def turn(self, way):
		'''
		Turn left or right (change direction).
		Args:
		  * way (str): which way to turn (L/R)
		'''
		newdir = np.matmul(np.array(self.direction), np.array(self.ways[way]))
		self.direction = tuple(newdir)
		self.memory.add(self.invcompass[self.direction])


	def goForwards(self):
		'''
		Move one step forward in current direction.
		'''
		newpos = np.add(np.array(self.position), np.array(self.direction))
		self.position = tuple(newpos)