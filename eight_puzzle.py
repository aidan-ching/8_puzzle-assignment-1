import random
from copy import deepcopy


EMPTY = None


class Node:
    def __init__(self, board = None, parent = None):
        self.board = board
        self.parent = parent
        self.value = utility(board)
        

def initial_state():
    #returns the starting state of the board
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def shuffle(board):
    count = len(board) * len(board[0])
    temp_arr = list(range(0, count))

    random.shuffle(temp_arr)

    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            row[j] = temp_arr[i*len(board[0]) + j]

def display(board):
    for row in board:
        print(row)
    print("\n")

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

def utility(board):
    #returns how many of the numbers are in the correct place
    count = 0
    for i, row in enumerate(board):
        for j, num in enumerate(row):
            if num == i*3 + j + 1:
                count += 1
    return count

def uniform_cost_search(start):
    p_queue = list()
    p_queue.append(start)

    explored = list()

    while p_queue:
        #take node that has the most value
        max_val = 0
        currNode = None
        #find max val
        for node in p_queue:
            if node.value > max_val:
                max_val = node.value
        #pop first node with the max val
        for i, node in enumerate(p_queue):
            if node.value == max_val:
                currNode = p_queue.pop(i)
                break
        #get all the possible moves, add to explored nodes
        possible_moves = actions(currNode.board)
        explored.append(currNode.board)
        #if goal, return, else add to the priority queue
        for move in possible_moves:
            if goal(move):
                return Node(move, currNode)
            if move not in explored:
                p_queue.append(Node(move, currNode))

    return None


def displayTrace(solution):
    trace = list()
    while solution.parent != None:
        trace.append(solution.board)
        solution = solution.parent
    trace = trace[::-1]

    for move in trace:
        display(move)

        


        
