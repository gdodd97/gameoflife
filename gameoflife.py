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
    #todo build a render function that will print the board state as a pretty grid, replacing live cells with hashtags and dead cells with a space. 
    return state

width = 5
height = 5
print (random_state(width, height))
