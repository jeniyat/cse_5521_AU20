# Homework-1
## Submission requirements
⋅⋅* SubmitonefiletoCarmen:search.py
⋅⋅* Expected time commitment: 4-8 hrs
⋅⋅* Due: Friday, Sept. 21, 11:59pm

## Preparation

Download or clone this repository. This code, and the idea for the assignment, comes from [UC Berkeley](https://inst.eecs.berkeley.edu//~cs188/pacman/home.html).

⋅⋅* Open up the Windows Command Line or Mac Terminal or Linux Terminal.
⋅⋅* Change your directory to the folder with the pacman code. You should see a file called commands.txt and two folders: layouts and py.
⋅⋅* Run some of these commands (as listed in commands.txt) to make sure your setup works. Below are some examples:
```
python py/pacman.py
```
```
python py/pacman.py --layout tinyMaze --pacman GoWestAgent
```
⋅⋅* Make sure you can execute pacman. See what happens when you run this command:

```
python py/pacman.py --layout tinyMaze --pacman GoWestAgent
```

## Task 1 (3 pts)

Open the file py/search.py and find the function [depthFirstSearch](./py/search.py#L70) which reads:
```
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].
    Your search algorithm needs to return a list of actions that reaches
    the goal. Make sure that you implement the graph search version of DFS,
    which avoids expanding any already visited states. 
    Otherwise your implementation may run infinitely!
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    """
    YOUR CODE HERE
    """

    util.raiseNotDefined()
    
```

  
Take this template and finish the code so that depth-first search works. You can test it with pacman by running this command:
• python py/pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
Note that the comments above the code will be helpful. Submit just this file (search.py) to Carmen,
along with a text file with your answers to Task 1.
def depthFirstSearch(problem):
    """
Search the deepest nodes in the search tree first [p 85].
Your search algorithm needs to return a list of actions that reaches the goal. Make sure to implement a graph search algorithm [Fig. 3.7].
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
print "Start:", problem.getStartState()
print "Is the start a goal?", problem.isGoalState(problem.getStartState()) print "Start's successors:", problem.getSuccessors(problem.getStartState()) """
closedset = []
openset = [problem.getStartState()] # openset starts with starting state parents = {}
while len(openset) > 0:
state = openset.pop() # get most-recently-added element from openset
# ...
if # ...
print "Found goal!"
# retrieve series of steps that brought us here (use the parents map) actions = []
while state != problem.getStartState():
# ...
            print actions # just to see the resulting actions
            return actions
        else:
for (next_state, action, cost) in problem.getSuccessors(state): # next_state is something like (4, 2) (coordinates)
# action is something like WEST
# cost is not used for depth-first search
# ...
Task 2 (2 pts)
(Note that this should be simple if you've completed task 1....)
Implement breadth-first search for pacman, in the breadthFirstSearch function. Test with:
• python py/pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

Useful Python code
Task 3 below asks you to implement UCS for Pacman. So, you want to have an openset that's ordered by a heuristic value. Python has "heaps" for this purpose. Whenever you "pop" a value from a heap, the lowest value comes out. Use a tuple to keep the value and other data together.
from heapq import heappush, heappop
openset = []
heappush(openset, (5, "foo"))
heappush(openset, (7, "bar"))
heappush(openset, (3, "baz"))
heappush(openset, (9, "quux"))
best = heappop(openset)
print best
Task 3 (3 pts)
Open the file py/search.py and find the function uniformCostSearch which reads:
def uniformCostSearch(problem):
"Search the node of least total cost first." "*** YOUR CODE HERE ***" util.raiseNotDefined()
Add this line of code above that function:
from heapq import heappush, heappop
Take the template and finish the code so that UCS works. (You might want to adapt your implementation of DFS or BFS.) Test your code with:
• python py/pacman.py -l mediumMaze -p SearchAgent -a fn=ucs Task 4 (2 pts)
Finish the implementation of A* search. You can use the argument heuristic as a function like so: dist = heuristic(state, problem)
You can test it with pacman by running this command:
• python py/pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
