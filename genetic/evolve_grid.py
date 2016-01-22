import random
import math

import sys
sys.path.append("..")

from grid import *
from ant import *
	
def makeRandomGrid():
	nant = Ant('E', (0,0))
	startpts = []
	npts = random.randint(0,20)
	mnpts = random.randint(0,20)
	m = random.randint(1,2)
	nfarpts = random.randint(0,20)
	for i in range(npts*mnpts*m):
	    startpts.append((random.randint(-20,20), random.randint(-20,20)))
	for i in range(0):
	    startpts.append((random.randint(-200,200), random.randint(-200,200)))
	g = Grid(startpts, nant)
	return g


def makeExtraGrid():
	nant = Ant('E', (0,0))
	startpts = []
	for i in range(50):
	    startpts.append((random.randint(-20,20), random.randint(-20,20)))
	    startpts.append((random.randint(-200,200), random.randint(-200,200)))
	    startpts.append((random.randint(-2000,2000), random.randint(-2000,2000)))
	    startpts.append((random.randint(-100000,100000), random.randint(-100000,100000)))
	g = Grid(startpts, nant)
	return g


def addNoise(pts, accuracy=10):
	newpts = []
	for p in pts:
		r = random.randint(0, accuracy)
		if r == 0:
			newpts.append((p[0]+random.randint(-1,1), p[1]))
		elif r == 1:
			newpts.append((p[0], p[1]+random.randint(-1,1)))
		elif r == 2:
			newpts.append((random.randint(min(p[1],10*p[1]), max(p[1],10*p[1])), random.randint(min(p[0],10*p[0]), max(p[0],10*p[0]))))
			newpts.append(p)
		elif r == 3:
			pass
		else:
			newpts.append(p)
	return newpts


def getRandomChild(g1, g2):
	allpts = g1.startpts + g2.startpts
	random.shuffle(allpts)
	nant = Ant('E', (0,0))
	half = len(allpts)/2
	size = random.randint(min(half-2,2), half+2)
	newpts = addNoise(allpts[:size])
	return Grid(newpts, nant)


def getCircleChild(g1, g2):
	nant = Ant('E', (0,0))
	allpts = g1.startpts + g2.startpts
	random.shuffle(allpts)
	newpts = [p for p in g1.startpts if sum(p) < 10] + [p for p in g2.startpts if sum(p) > 10]
	newpts += allpts[:5]
	newpts = addNoise(newpts)
	return Grid(newpts, nant)


def getSplitChild(g1, g2):
	nant = Ant('E', (0,0))
	allpts = g1.startpts + g2.startpts
	random.shuffle(allpts)
	newpts = [p for p in g1.startpts if p[0]>0] + [p for p in g2.startpts if p[0]<0]
	newpts += allpts[:5]
	newpts = addNoise(newpts)
	return Grid(newpts, nant)


def getPatchChild(g1, g2):
	nant = Ant('E', (0,0))
	allpts = g1.startpts + g2.startpts
	random.shuffle(allpts)
	corners = allpts[:2]
	bottom = min([c[1] for c in corners])
	left = min([c[0] for c in corners])
	top = max([c[1] for c in corners])
	right = max([c[0] for c in corners])

	ng1 = [p for p in g1.startpts if not (left<p[0]<right and bottom<p[1]<top)]
	ng2 = [p for p in g2.startpts if left<p[0]<right and bottom<p[1]<top]
	newpts = ng1 + ng2 + 3*([(0,0), (0,200), (200,0), (200,200), (0,-200), (-200,0), (-200,-200), (-200,200), (200,-200)])
	newpts = addNoise(newpts)
	return Grid(newpts, nant)


combiners = [getRandomChild, getSplitChild, getCircleChild, getPatchChild]


def getNextGen(parents, scores, population):
	children = []

	totalscore = sum([scores[x] for x in parents])

	for p in parents:
		nchildren = min(int(math.exp(scores[p]*len(parents)/totalscore)), int(population*1))
		for i in range(nchildren):
			others = [q for q in parents if q != p]
			p2 = others[random.randint(0, len(others)-1)]
			combiner = combiners[random.randint(0,len(combiners)-1)]
			children.append(combiner(p, p2))
	random.shuffle(children)
	parents.sort(lambda x, y: (scores[x] - scores[y]) / max(abs(scores[x] - scores[y]), 1))
	return children[:population]


def getWinners(grids, scores):
	# for g, s in scores.items():
	# 	print g.startpts, s
	grids.sort(lambda x, y: (scores[x] - scores[y]) / max(abs(scores[x] - scores[y]), 1) )	
	winners = grids[1:]
	return winners


def runGeneration(number, winners, scores, population, defaultgrids):
	if number == 0:
		grids = defaultgrids
	else:
		grids = getNextGen(winners, scores, population)
	scores = {g: g.score() for g in grids}
	winners = grids
	return [grids, scores, winners]


def evolve(generations=50, population=200, defaultgrids=None):
	if not defaultgrids:
		defaultgrids = [makeRandomGrid() for i in range(population)]

	history = {}
	best = [None, 0]
	winners = scores = None

	for i in range(generations):
		grids, scores, winners = runGeneration(i, winners, scores, population, defaultgrids)
		history[i] = scores
		thisbest = max(scores.values())
		if thisbest > best[1]:
			best = ({scores[k]:k for k in scores}[thisbest], thisbest)
		print sum(history[i].values()), max(history[i].values())

	print best
	return best


def metaEvolve():
	grids = []
	for i in range(10):
		ans = evolve()
		if ans[1] > 15000:
			grids.append(ans[0])
	print grids

	evolve(5, len(grids), grids)

if __name__=="__main__":
	evolve()
