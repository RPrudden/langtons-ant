highway_seq = ['S', 'W', 'S', 'W', 'N', 'W', 'N', 'E', 'S', 'W', 'S', 'E', 'N', 'W', 'N', 'W', 'N', 'E', 'S', 'W', 'S', 'W', 'N', 'E', 'S', 'E', 'N', 'W', 'S', 'W', 'S', 'W', 'N', 'E', 'S', 'E', 'S', 'E', 'N', 'E', 'S', 'E', 'N', 'W', 'S', 'W', 'N', 'W', 'S', 'W', 'N', 'E', 'S', 'E', 'N', 'E', 'S', 'E', 'S', 'E', 'N', 'E', 'N', 'W', 'N', 'W', 'N', 'W', 'S', 'W', 'N', 'E', 'S', 'E', 'N', 'E', 'N', 'W', 'N', 'E', 'S', 'W', 'S', 'E', 'S', 'W', 'N', 'E', 'N', 'W', 'N', 'W', 'N', 'E', 'S', 'W', 'S', 'W', 'S', 'E', 'N', 'W', 'N', 'E']
right = {'N':'E', 'E':'S', 'S':'W', 'W':'N'}
highway_seq_2 = [right[t] for t in highway_seq]
highway_seq_3 = [right[right[t]] for t in highway_seq]
highway_seq_4 = [right[right[right[t]]] for t in highway_seq]

class Grid():
	def __init__(self, startpts, ant):
		'''
		Args:
		  * startpts (list): points which start off black (x,y tuples)
		  * ant: Ant
		'''
		self.points = startpts
		self.ant = ant


	def squareIsBlack(self, pt):
		'''
		Args:
		  * pt (tuple): x,y point
		'''
		return (pt in self.points)


	def stepForward(self):
		'''
		Ant reverses the colour of its square, turns, and moves forward.
		'''
		if self.squareIsBlack(self.ant.position):
			self.ant.turn('L')
			self.points.remove(self.ant.position)
		else:
			self.ant.turn('R')
			self.points.append(self.ant.position)

		self.ant.goForwards()


	def score(self):
		'''
		Number of moves until the highway sequence comes up.
		'''
		for i in range(200000):
			if self.ant.memory.moves in [highway_seq, highway_seq_2, highway_seq_3, highway_seq_4]:
				break
			self.stepForward()
		return i

