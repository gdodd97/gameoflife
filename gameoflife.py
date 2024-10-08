import random
board_state = []

def dead_state(dead_width, dead_height):
    board_state = []  # Initialize a new list to avoid referencing old values
    for i in range(dead_height):
        dead_row = [0] * dead_width  # Create a row of zeroes
        board_state.append(dead_row)
    return board_state

def random_state(board_width, board_height):
    state = dead_state(board_width, board_height)
    for i in range(board_height):
        for j in range(board_width):
            random_number = random.random()
            if random_number >= 0.5:
                state[i][j] = 0  # Directly modify the state matrix
            else:
                state[i][j] = 1
    return state

def render(state):
    for i in state:
        print('|', end = ' ')
        for j in i:
            if j == 0:
                print('X', end =  ' ')
            if j == 1:
                print('O', end = ' ')
        print('|\n')

def next_board_state(state):
    #todo create function to intake current board state and calculate next board state. 
    return state

a_random_state = random_state(5,5)
render(a_random_state)
