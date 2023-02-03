import eight_puzzle as eight
from eight_puzzle import Node

board = eight.initial_state() 


#our board for testing purposes
temp_arr = [2,8,4,1,5,0,6,7,3]

for i, row in enumerate(board):
    for j, tile in enumerate(row):
        row[j] = temp_arr[i*len(board[0]) + j]


start = Node(board, None)

solution = eight.uniform_cost_search(start)

eight.displayTrace(solution)