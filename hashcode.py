problem = []
itt = 0
boardDimensions = []
numberOfDrones=0
numberOfTurns=0
maxPayload=0
packageWeights=[]
warehouses=[]
warehouses = {}

def setUpProblem():
	with open('test.txt') as f:
		for line in f:
			problem.append(line)
def setUpBoard():
	global numberOfDrones
	global numberOfTurns
	global maxPayload
	x = problem[itt].split(' ')
	boardDimensions.append(int(x[0]))
	boardDimensions.append(int(x[1]))
	numberOfDrones=int(x[2])
	numberOfTurns=int(x[3])
	maxPayload=int(x[4])
	itt+=1
def setTypesOfDrones():
	x = problem[itt].split(' ')
	for i in x:
		packageWeights.append(int(i))
	itt+=1
def setUpWarehouses():
	for i in range(int(problem[itt])):




setUpProblem()
setUpBoard()
setTypesOfDrones()


