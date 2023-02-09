import eight_puzzle as eight
import time
from eight_puzzle import Node

print("Welcome to 862210672 8 puzzle solver.")
puzzle_choice = input("Type \"1\" to use a default puzzle, or \"2\" to enter your own puzzle, or \"3\" to generate a random puzzle\n")
if puzzle_choice == "1":
    inputstr = "185762340"
    board = eight.string_to_board(inputstr)
elif puzzle_choice == "2":
    inputstr = input("Enter a 9 digit number representing the 8 puzzle.\n")
    board = eight.string_to_board(inputstr)
elif puzzle_choice == "3":
    shuffle_amt = input("Enter how many moves to shuffle the puzzle from the original position: ")
    board = eight.random_board(3, int(shuffle_amt))

print("Enter your choice of algorithm: ")
print("1. Uniform Cost Search")
print("2. A* with the Misplaced Tile heuristic")
print("3. A* with the Euclidean distance heuristic\n")

algo_choice = input()
start = Node(board, None)

if algo_choice == "1":
    start_time = time.time()
    solution = eight.uniform_cost_search(start)
    print("--- %s seconds ---" % (time.time() - start_time))
elif algo_choice == "2":
    start_time = time.time()
    solution = eight.A_star_misplaced_tile(start)
    print("--- %s seconds ---" % (time.time() - start_time))
elif algo_choice == "3":
    start_time = time.time()
    solution = eight.A_star_manhattan_distance(start)
    print("--- %s seconds ---" % (time.time() - start_time))