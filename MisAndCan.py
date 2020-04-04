from copy import deepcopy
import timeit

#Athanasia Karalakou 2015030061
# bfs algorithm based on: https://pythoninwonderland.wordpress.com/2017/03/18/how-to-implement-breadth-first-search-in-python/
class State():
	
	def __init__(self):
		self.lmissionaries =3
		self.lcannibals = 3
		self.lboat = 1
		self.rmissionaries = 0
		self.rcannibals = 0
		self.rboat = 0
		self.parent = None
		
		
	def valid_state(self):	
		#check for movement requirements
		if( self.lmissionaries<0 or self.lcannibals<0 or self.rmissionaries<0 or self.rcannibals<0):
			return False
		if( self.lmissionaries>3 or self.lcannibals>3 or self.rmissionaries>3 or self.rcannibals>3):
			return False	
		if(0 < self.lmissionaries < self.lcannibals or 0 < self.rmissionaries < self.rcannibals ):
			return False	
		return True

	def goal_state(self):
		#check if goal reached
		if (self.lmissionaries==0 and self.lcannibals==0 and self.rcannibals==3 and self.rmissionaries==3):
			return True
		return False

	def __eq__(self, other):
		return (self.lmissionaries==other.lmissionaries and self.lcannibals == other.lcannibals and self.rmissionaries==other.rmissionaries and self.rcannibals==other.rcannibals and self.rboat==other.rboat and self.lboat==other.lboat)
	
	def __ne__(self, other):
		return not self.__eq__(other)	
	

def possible_states(cur_state):
		nodes=[]
		
		next_state = deepcopy(cur_state)
		next_state.parent=cur_state
		
		#move to the opposite shore
		next_state.rboat = cur_state.lboat
		next_state.lboat = cur_state.rboat
		
		#move to the right shore
		if(cur_state.rboat==0):
			#people moved to the right shore
			next_state.rmissionaries+=2
			next_state.rcannibals+=0
			
			#people left from the left shore
			next_state.lmissionaries-=2
			next_state.lcannibals-=0

			if next_state.valid_state():
				nodes.append(next_state)

		next_state = deepcopy(cur_state)
		next_state.parent=cur_state
		
		#move to the opposite shore
		next_state.rboat = cur_state.lboat
		next_state.lboat = cur_state.rboat
		
		#move to the right shore
		if(cur_state.rboat==0):

			next_state.rmissionaries+=0
			next_state.rcannibals+=2
			
			#people left from the left shore
			next_state.lmissionaries-=0
			next_state.lcannibals-=2

			if next_state.valid_state():
				nodes.append(next_state)

		next_state = deepcopy(cur_state)
		next_state.parent=cur_state
		
		#move to the opposite shore
		next_state.rboat = cur_state.lboat
		next_state.lboat = cur_state.rboat
		
		if(cur_state.rboat==0):

			next_state.rmissionaries+=1
			next_state.rcannibals+=1
			
			#people left from the left shore
			next_state.lmissionaries-=1
			next_state.lcannibals-=1

			if next_state.valid_state():
				nodes.append(next_state)

		next_state = deepcopy(cur_state)
		next_state.parent=cur_state
		
		#move to the opposite shore
		next_state.rboat = cur_state.lboat
		next_state.lboat = cur_state.rboat
		
		if(cur_state.rboat==0):


			next_state.rmissionaries+=1
			next_state.rcannibals+=0
			
			#people left from the left shore
			next_state.lmissionaries-=1
			next_state.lcannibals-=0

			if next_state.valid_state():
				nodes.append(next_state)

		next_state = deepcopy(cur_state)
		next_state.parent=cur_state
		
		#move to the opposite shore
		next_state.rboat = cur_state.lboat
		next_state.lboat = cur_state.rboat
		
		if(cur_state.rboat==0):


			next_state.rmissionaries+=0
			next_state.rcannibals+=1
			
			#people left from the left shore
			next_state.lmissionaries-=0
			next_state.lcannibals-=1

			if next_state.valid_state():
				nodes.append(next_state)

		next_state = deepcopy(cur_state)
		next_state.parent=cur_state
		
		#move to the opposite shore
		next_state.rboat = cur_state.lboat
		next_state.lboat = cur_state.rboat
		
        #move to the left shore
		if(cur_state.rboat==1):
			
			#people left from the right shore
			next_state.rmissionaries-=2
			next_state.rcannibals-=0
			
			#people moved to the left shore
			next_state.lmissionaries+=2
			next_state.lcannibals+=0
		
			if next_state.valid_state():
				nodes.append(next_state)

		next_state = deepcopy(cur_state)
		next_state.parent=cur_state
		
		#move to the opposite shore
		next_state.rboat = cur_state.lboat
		next_state.lboat = cur_state.rboat
		

		if(cur_state.rboat==1):

			next_state.rmissionaries-=0
			next_state.rcannibals-=2
			
			
			next_state.lmissionaries+=0
			next_state.lcannibals+=2
		
			if next_state.valid_state():
				nodes.append(next_state)

		next_state = deepcopy(cur_state)
		next_state.parent=cur_state
		
		#move to the opposite shore
		next_state.rboat = cur_state.lboat
		next_state.lboat = cur_state.rboat
		

		if(cur_state.rboat==1):
			next_state.rmissionaries-=1
			next_state.rcannibals-=1
			
			
			next_state.lmissionaries+=1
			next_state.lcannibals+=1
		
			if next_state.valid_state():
				nodes.append(next_state)

		next_state = deepcopy(cur_state)
		next_state.parent=cur_state
		
		#move to the opposite shore
		next_state.rboat = cur_state.lboat
		next_state.lboat = cur_state.rboat
		

		if(cur_state.rboat==1):

			next_state.rmissionaries-=1
			next_state.rcannibals-=0
			
			
			next_state.lmissionaries+=1
			next_state.lcannibals+=0
		
			if next_state.valid_state():
				nodes.append(next_state)

		next_state = deepcopy(cur_state)
		next_state.parent=cur_state
		
		#move to the opposite shore
		next_state.rboat = cur_state.lboat
		next_state.lboat = cur_state.rboat
		

		if(cur_state.rboat==1):

			next_state.rmissionaries-=0
			next_state.rcannibals-=1
			
			
			next_state.lmissionaries+=0
			next_state.lcannibals+=1
		
			if next_state.valid_state():
				nodes.append(next_state)

		return nodes
	
def breadth_first_search():
	initial_state= State()
	if initial_state.goal_state():
		return initial_state
	# keep track of all visited nodes
	visited = []
	# keep track of nodes to be checked
	queue = [initial_state]

	# keep looping until there are nodes still to be checked
	while queue:
		# pop shallowest node (first node) from queue
		curNode = queue.pop()
		if curNode.goal_state():
			return curNode
		# add node to list of checked nodes
		if curNode not in visited:
			visited.append(curNode)
		
		for child in possible_states(curNode):
			if child in visited:
				continue
			# add child of node to queue
			if child not in queue:
				queue.append(child)

def main():
	
	start = timeit.default_timer() 
	state = breadth_first_search()
	path = []
	i=0
	path.append(state)
	parent = state.parent
	while parent:
			path.append(parent)
			parent = parent.parent
	#reverse path
	path=path[::-1]
	stop = timeit.default_timer()
	#print path
	for state in path:
		i+=1
		print ( "➕:",state.lmissionaries,"🍖:", state.lcannibals,"⛵:", state.lboat,"🌊🌊🌊","➕:",state.rmissionaries,"🍖:", state.rcannibals,"⛵:", state.rboat)
	print("Total Moves:",i,', Running Time: ', round(stop - start,4), "secs")
if __name__ == "__main__":
	main()