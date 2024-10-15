import random
import time
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

def state_width(state):
    return len(state)

def state_height(state):
    return len(state[0])

def render(state):

    display_as = {
        0: ' ',
        # This is "unicode" for a filled-in square. You can also just use a thick
        # "ASCII" character like a '$' or '#'.
        1: u"\u2588"
    }
    lines = []
    for y in range(0, state_height(state)):
        line = ''
        for x in range(0, state_width(state)):
            line += display_as[state[x][y]] * 2
        lines.append(line)
    print ("\n".join(lines))

def next_cell_value(cell_coords,state):
    width = state_width(state)
    height = state_height(state)
    x = cell_coords[0]
    y = cell_coords[1]
    n_live_neighbors = 0

    # Iterate around this cell's neighbors
    for x1 in range((x-1), (x+1)+1):
        # Make sure we don't go off the edge of the board
        if x1 < 0 or x1 >= width: continue

        for y1 in range((y-1), (y+1)+1):
            # Make sure we don't go off the edge of the board
            if y1 < 0 or y1 >= height: continue
            # Make sure we don't count the cell as a neighbor of itself!
            if x1 == x and y1 == y: continue

            if state[x1][y1] == 1:
                n_live_neighbors += 1

    if state[x][y] == 1:
        if n_live_neighbors <= 1:
            return 0
        elif n_live_neighbors <= 3:
            return 1
        else:
            return 0
    else:
        if n_live_neighbors == 3:
            return 1
        else:
            return 0

def next_board_state(init_state):

    width = state_width(init_state)
    height = state_height(init_state)
    next_state = dead_state(width, height)

    for x in range(0, width):
        for y in range(0, height):
            next_state[x][y] = next_cell_value((x, y), init_state)

    return next_state

def run_forever(init_state):
    next_state = init_state
    while True:
        render(next_state)
        next_state = next_board_state(next_state)
        time.sleep(0.03)

if __name__ == "__main__":
    init_state = random_state(5, 5)
    # init_state = load_board_state('./toad.txt')
    run_forever(init_state)
