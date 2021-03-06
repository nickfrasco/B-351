# Assignment 1
import math

#################################
# Problem 1
#################################
# Objectives:
# (1) Write a recursive function to compute the nth fibonacci number

def fib(n):
    if n <= 1:
        return n
    else:
        return(fib(n-1) + fib(n-2))



#################################
# Problem 2
#################################
# Objectives:
# (1) Write a function which returns a list of the first and last items in a given list

def firstLast(n):
    if len(n) > 1:
    	newlist = [n[0],n[-1]]
    	return newlist
    else:
    	return n




#################################
# Problem 3
#################################
# Objectives:
# (1) Write a function which takes a matrix and returns the transpose of that matrix
# Note: A matrix is represented as a 2-d array: [[1,2,3],[4,5,6],[7,8,9]]


def transpose(matrix):

	return [[matrix[x][i] for x in range(len(matrix))] for i in range(len(matrix[0]))]
	#for row in n_matrix:
	#	print(row)




#################################
# Problem 4
#################################
# Objectives:
# (1) Write a function which takes two points of the same dimension, and finds the euclidean distance between them
# Note: A point is represented as a tuple: (0,0)

def euclidean(p1,p2):
    dist = [(a-b) **2 for a,b in zip(p1,p2)]
    dist = math.sqrt(sum(dist))
    return dist
    



#################################
# Problem 5
#################################

# A Node is an object
# - value : Number
# - children : List of Nodes
class Node:
    def __init__(self, value, children):
        self.value = value
        self.children = children
        


exampleTree = Node(1,[Node(2,[]),Node(3,[Node(4,[Node(5,[]),Node(6,[Node(7,[])])])])])



# Objectives:
# (1) Write a function to calculate the sum of every node in a tree (iteratively)

def sumNodes(root):
	
	currentNode = [root]
	nodeList = []
	
	while currentNode:
	
		newLevel = [] #check here if needed
		for i in currentNode:
			nodeList.append(i.value)
			newLevel.extend(i.children)
		currentNode = newLevel
		
	return sum(nodeList)
	
	
		

# (2) Write a function to calculate the sum of every node in a tree (recursively)

def sumNodesRec(root):
    sum = 0   #init
    for child in root.children:
    	sum += sumNodesRec(child)
    return root.value + sum
    



#################################
# Problem 6
#################################
# Objectives:
# (1) Write a function compose, which takes an inner and outer function
# and returns a new function applying the inner then the outer function to a value

def compose(f_outer, f_inner):
	return lambda x: f_outer(f_inner(3))





#################################
# Bonus
#################################
# Objectives:
# (1) Create a string which has each level of the tree on a new line

def treeToString(root):
    visited = []
    unvisited = [root.children]
    
    for i in unvisited:
    	visited.append(i.value)
    	print(visited)
    
    
    	


