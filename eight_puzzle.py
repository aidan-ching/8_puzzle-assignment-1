import random
import math
from copy import deepcopy


EMPTY = None


class Node:
    def __init__(self, board = None, parent = None, depth = 0, heuristic = 0):
        self.board = board
        self.parent = parent
        self.depth = depth
        if heuristic == 0:
            self.value = heuristic_correct_tile(board)
        self.misplaced_tiles = misplaced_tiles(board)
        self.manhattan_distance = manhattan_distance(board)
        

def initial_state(size):
    #returns the starting state of the board
    nums_in_board = list(range(1, size**2))
    nums_in_board.append(0)

    board = list()
    for i in range(size):
        temp = list()
        for j in range(size):
            temp.append(nums_in_board[i*size + j])
        board.append(temp)
    return board

#returns a board with paramaters size and how many moves that it needs to be solved.
def random_board(size, moves):

    board = initial_state(size)
    explored = list()
    for i in range(moves):
        explored.append(board)
        all_possible_moves = actions(board)
        possible = list()
        for action in all_possible_moves:
            if action not in explored:
                possible.append(action)
        board = random.choice(possible)
    return board

def manhattan_distance(board):
    count = 0
    for y, row in enumerate(board):
        for x, num in enumerate(row):
            if num == 1:
                count += abs(x-0)+abs(y-0)
            if num == 2:
                count += abs(x-1)+abs(y-0)
            if num == 3:
                count += abs(x-2)+abs(y-0)
            if num == 4:
                count += abs(x-0)+abs(y-1)
            if num == 5:
                count += abs(x-1)+abs(y-1)
            if num == 6:
                count += abs(x-2)+abs(y-1)
            if num == 7:
                count += abs(x-0)+abs(y-2)
            if num == 8:
                count += abs(x-1)+abs(y-2)

    return count

        


def display(board):
    for row in board:
        print(row)

def goal(board):
    temp_arr = list()
    for row in board:
        for num in row:
            temp_arr.append(num)

    goal = list(range(1, len(board)*len(board[0])))
    goal.append(0)

    return temp_arr == goal

def actions(board):
    #returns a list of the possible moves we can take from the board
    # we can basically move the blank space in each of the four directions
    moves = list()
    #lets get the coordinates of the blank space first
    x,y = 0,0


    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == 0:
                x = j
                y = i


    #move up
    if y != 0:
        temp = deepcopy(board)
        temp[y][x], temp[y-1][x] = temp[y-1][x], temp[y][x]
        moves.append(temp)

    #move down
    if y != 2:
        temp = deepcopy(board)
        temp[y][x], temp[y+1][x] = temp[y+1][x], temp[y][x]
        moves.append(temp)

    #move left
    if x != 0:
        temp = deepcopy(board)
        temp[y][x], temp[y][x-1] = temp[y][x-1], temp[y][x]
        moves.append(temp)

    #move right
    if x != 2:
        temp = deepcopy(board)
        temp[y][x], temp[y][x+1] = temp[y][x+1], temp[y][x]
        moves.append(temp)

    return moves

def heuristic_correct_tile(board):
    #returns how many of the numbers are in the correct place
    count = 0
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == i*3 + j + 1:
                count += 1
    return count

def uniform_cost_search(start):
    print("Starting State:")
    display(start.board)

    p_queue = list()
    p_queue.append(start)

    explored = list()

    num_expanded_nodes = 0
    max_nodes_in_queue = 0

    while p_queue:
        #take node that has the most value
        max_val = 0
        currNode = None
        #find max val
        p_queue = sorted(p_queue, key=lambda node: node.depth)
        max_nodes_in_queue = max(max_nodes_in_queue, len(p_queue))
        

        currNode = p_queue.pop(0)
        print("The best state to expand with g(n) = " + str(currNode.depth) + " is...")
        display(currNode.board)
        print("Expanding this node...\n")
        num_expanded_nodes += 1

        if goal(currNode.board):
            print("Goal!!!\n")
            print("To solve this problem the search algorithm expanded a total of " + str(num_expanded_nodes) + " nodes.")
            print("The maximum number of nodes in the queue at any one time: " + str(max_nodes_in_queue))
            print("The depth of the goal node was " + str(currNode.depth))            
            return currNode
        #get all the possible moves, add to explored nodes
        possible_moves = actions(currNode.board)
        explored.append(currNode.board)
        #if goal, return, else add to the priority queue
        for move in possible_moves:
            if move not in explored:
                p_queue.append(Node(move, currNode, currNode.depth+1, 0))

    return None

def A_star_misplaced_tile(start):
    print("Starting State:")
    display(start.board)

    p_queue = list()
    p_queue.append(start)

    explored = list()

    num_expanded_nodes = 0
    max_nodes_in_queue = 0

    while p_queue:
        #take node that has the most value
        max_val = 0
        currNode = None
        #find max val
        p_queue = sorted(p_queue, key=lambda node: node.depth+node.misplaced_tiles)
        max_nodes_in_queue = max(max_nodes_in_queue, len(p_queue))
        

        currNode = p_queue.pop(0)
        print("The best state to expand with g(n) = " + str(currNode.depth) + " and h(n) = " + str(currNode.misplaced_tiles) + " with a total of: " + str(currNode.depth+currNode.misplaced_tiles) + " is...")
        display(currNode.board)
        print("Expanding this node...\n")
        num_expanded_nodes += 1

        if goal(currNode.board):
            print("Goal!!!\n")
            print("To solve this problem the search algorithm expanded a total of " + str(num_expanded_nodes) + " nodes.")
            print("The maximum number of nodes in the queue at any one time: " + str(max_nodes_in_queue))
            print("The depth of the goal node was " + str(currNode.depth))        
            return currNode
        #get all the possible moves, add to explored nodes
        possible_moves = actions(currNode.board)
        explored.append(currNode.board)
        #if goal, return, else add to the priority queue
        for move in possible_moves:
            if move not in explored:
                p_queue.append(Node(move, currNode, currNode.depth+1, 0))

    return None

def string_to_board(inputstr):
    board = initial_state(int(math.sqrt(len(inputstr))))
    temp_arr = list()
    for char in inputstr:
        temp_arr.append(int(char))

    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            row[j] = temp_arr[i*len(board[0]) + j]

    return board


def A_star_manhattan_distance(start):
    print("Starting State:")
    display(start.board)

    p_queue = list()
    p_queue.append(start)

    explored = list()

    num_expanded_nodes = 0
    max_nodes_in_queue = 0

    while p_queue:
        #take node that has the most value
        max_val = 0
        currNode = None
        #find max val
        p_queue = sorted(p_queue, key=lambda node: node.depth+node.manhattan_distance)
        max_nodes_in_queue = max(max_nodes_in_queue, len(p_queue))
        

        currNode = p_queue.pop(0)
        print("The best state to expand with g(n) = " + str(currNode.depth) + " and h(n) = " + str(currNode.manhattan_distance) + " and f(n) = " + str(currNode.depth+currNode.manhattan_distance) + " is...")
        display(currNode.board)
        print("Expanding this node...\n")
        num_expanded_nodes += 1

        if goal(currNode.board):
            print("Goal!!!\n")
            print("To solve this problem the search algorithm expanded a total of " + str(num_expanded_nodes) + " nodes.")
            print("The maximum number of nodes in the queue at any one time: " + str(max_nodes_in_queue))
            print("The depth of the goal node was " + str(currNode.depth))          
            return currNode
        #get all the possible moves, add to explored nodes
        possible_moves = actions(currNode.board)
        explored.append(currNode.board)
        #if goal, return, else add to the priority queue
        for move in possible_moves:
            if move not in explored:
                p_queue.append(Node(move, currNode, currNode.depth+1, 0))

    return None

def misplaced_tiles(board):
    count = 0
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num != i*len(board) + j + 1 and i*len(board)+j+1 != len(board)**2:
                count += 1
    return count

def displayTrace(solution):
    depth = solution.depth

    trace = list()
    while solution.parent != None:
        trace.append(solution.board)
        solution = solution.parent
    trace = trace[::-1]

    for move in trace:
        display(move)
        print("\n")
    print("Solved in " + str(depth) + " steps.")

        


        
