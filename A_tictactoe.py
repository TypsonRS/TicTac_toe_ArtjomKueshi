# In this script you can write your code.
# Start by writing all the functions.
# In the last part after if __name__ == "__main__": you can call the functions to play your game.
# If you run `uv run python tic_tac_toe.py` in the command line the game will start. Try it out! ;) :)
"""
    This script can run a simple game of Tic-Tac-Toe.
    But it also can scale the board and the winning condition.
    Perhaps it could take additional players or even AI players?
"""


def thanks():
    return print("Very nice! This is what we have:")

def users_input():
    """
        Takes user input for names and symbols, strips the symbol to 1 character
    """
    print("Let us start with the user questionary!")                                         # there could be even more players
    print()
    name1 = input("Player 1, what's your name? Hit <Enter> to use 'Player 1' ") or 'Player 1'
    input_symbol1 = input("%s, which symbol do you want to use? Hit <Enter> to use 'x' " % name1) or 'x'
    print()
    name2 = input("Player 2, what's your name? Hit <Enter> to use 'Player 2' ") or 'Player 2'
    input_symbol2 = input("%s, which symbol do you want to use? Hit <Enter> to use 'o' " % name2) or 'o'
    symbol1 = ' '+input_symbol1[0]+' ' # mind the pesky spaces: they are used in board_printer
    symbol2 = ' '+input_symbol2[0]+' '
    print()
    thanks()
    print("- ", name1, "using the symbol", symbol1)
    print("- ", name2, "using the symbol", symbol2)

    return name1, symbol1, name2, symbol2

def board_square():
    """
        Takes any board size, finds the next perfect square, also adds spaces tu users symbols for the correct work of board_printerer 
    """
    print()
    print("We need to create a board. It will be a square (for now) but the size can be your choice.")
    print()
    print("Think big and don't worry if you do not remember all perfect squares.")          # If you think > 1000 the board_printer will use a variable space slicer
    input_size = int(input('Please type any integer or hit <Enter> to use a standard of 9: ') or 9)
    if input_size < 7:
        input_size = 9
    x = 1               # for the spaces added to user symbols on large boards
    y = 1               # one side of board, asking for it would be too easy ;)
    z = 3               # winning condition
    while abs(input_size - (y ** 2)) > abs(input_size - ((y + 1) ** 2)):      # Cheat mode on: it gives the closest perfect square
        y += 1
    print()
    thanks()
    print("The board size will be: ", y ** 2)
    if y > 3:
        print()
        print("\033[92m Amazing! You are setting up a big challenge. Now it's time to think about the winning condition. \033[0m")
        z = int(input('Please type any integer or hit <Enter> to use a standard of 3: ') or 3)
        if y > 10:
            x += 1
        if z > y:
            z = y
            print()             # in the ultimate tic-tac-toe the winning condition is 3 for the 3x3 board and 3 (3x3 boards) for the big 9x9 board.
            print("\033[0;31m You are thinking around the corner? \033[0m", "With the board size of ", y**2, "= ", y,"² the winning condition is restricted to ", y)
    else:
        print("The winning condition is: ", z)
    print()
    print('We are all set to start the game.')
    print("Never mind the leading zeros (c'est la vie).")
    nothing = input("\033[1;33m Please note, a DRAW is not yet implemented. Suit yourself and hit any key! \033[0m") or ''
    return x, y, z

def board_generator():
    """
        Generates the board as a dictionary with a key list from 1 to y^2 and fills values to serve as coordinates
    """
    board_size = y ** 2
    board_fields = list(range(1, board_size + 1))
    board_dictionary = dict((el, str(f"{el:03d}")) for el in board_fields)     # other option without coordinates: dict((el, ' ') for el in board_fields)
    return board_dictionary

def board_printer():
    """
        Prints the board with values

        *** Cheat mode on ***
        How it works:
        row * y + col + 1 calculates the dictionary key for each cell (1-indexed)
        range(y) gives you 0, 1, 2 for both rows and columns
        List comprehension builds each row, then " | ".join() formats it
        *** Cheat mode off ***
        
    """
    print()
    print("Here is the board:")                                   # import and randomize this motivating message
    print('+-----' * y + '+')
    symbol_filler = ' ' * x                                              # can use instead of ' ' for really large boards
    for row in range(y):
        row_values = [board_dictionary[row * y + col + 1] for col in range(y)]  # todo: think that through       
        colored_values = [f"\033[92m{val}\033[0m" if isinstance(val, str) and val.endswith(' ') else val for val in row_values] # this colores the symbols, mind the spaces
        print("| " + " | ".join(colored_values) + " |")                         # todo: study slicing print("example".join(row_values))
        if row < y - 1:
            print('+-----' * y + '+')
    print('+-----' * y + '+')

def ask_field(user):
    """
        Requires user input for a field
    """
    print()
    field = int(input("%s, Your turn! Type a field number! " % user))
    return field

def field_filler(field, symbol):
    """
        Inserts into the dictionary the symbol from last input
    """
    if board_dictionary[field] != symbol1 and board_dictionary[field] != symbol2:       # other check for many players 
        print()
        print("Excellent, '%s' put on field: " % symbol, field)
        board_dictionary[field] = symbol
        #print()
        #print("The board dictionary now is: ")                                         # left for debugging
        #print(board_dictionary)
    else:
        print()
        print("How sad, '%s' not put on field %d, because this field is used." % (symbol, field))
        print("For now you cannot pick again, bad luck ...")                            # better times are ahead
    return board_dictionary                                                  

def check_winner(check_name, check_symbol):
    """
        Checking z same consecutive symbols in rows, columns and diagonals
        
        *** Cheat mode on ***
        Check all diagonals (both directions)
        For each possible diagonal offset, generate the sequence of keys
        and check for z consecutive symbols
        *** Cheat mode off ***

    """

    current_symbol = check_symbol  
    be_winner = ''

    # Check columns
    for row_start in range(1, len(board_dictionary) + 1, y):
        # Keys in the current row
        row_keys = list(range(row_start, row_start + y))
        # Check every window of length z in this row
        for i in range(len(row_keys) - z + 1):
            # Get the keys for the current window
            combo_keys = row_keys[i:i + z]
            # Concatenate the corresponding values
            compare_str = ''.join(board_dictionary[k] for k in combo_keys)
            # Check for a match
            if compare_str == current_symbol * z:
                be_winner = check_name

    # Check columns
    for col_start in range(1, y + 1):
        col_keys = [col_start + offset * y for offset in range(y)]
        # Slide a window of length z down the column
        for i in range(len(col_keys) - z + 1):
            combo_keys = col_keys[i:i + z]
            compare_str = ''.join(board_dictionary[k] for k in combo_keys)
            if compare_str == current_symbol * z:
                be_winner = check_name

    # Main diagonals (top-left to bottom-right)
    for start_row in range(y):
        diag_keys = []
        row, col = start_row, 0
        while row < y and col < y:
            key = row * y + col + 1
            diag_keys.append(key)
            row += 1
            col += 1
        # Check this diagonal for winning sequences
        for i in range(len(diag_keys) - z + 1):
            combo_keys = diag_keys[i:i + z]
            compare_str = ''.join(board_dictionary[k] for k in combo_keys)
            if compare_str == current_symbol * z:
                be_winner = check_name

    for start_col in range(1, y):
        diag_keys = []
        row, col = 0, start_col
        while row < y and col < y:
            key = row * y + col + 1
            diag_keys.append(key)
            row += 1
            col += 1
        # Check this diagonal for winning sequences
        for i in range(len(diag_keys) - z + 1):
            combo_keys = diag_keys[i:i + z]
            compare_str = ''.join(board_dictionary[k] for k in combo_keys)
            if compare_str == current_symbol * z:
                be_winner = check_name

    # Anti-diagonals (top-right to bottom-left)
    for start_row in range(y):
        diag_keys = []
        row, col = start_row, y - 1
        while row < y and col >= 0:
            key = row * y + col + 1
            diag_keys.append(key)
            row += 1
            col -= 1
        # Check this diagonal for winning sequences
        for i in range(len(diag_keys) - z + 1):
            combo_keys = diag_keys[i:i + z]
            compare_str = ''.join(board_dictionary[k] for k in combo_keys)
            if compare_str == current_symbol * z:
                be_winner = check_name

    for start_col in range(y - 1):
        diag_keys = []
        row, col = 0, start_col
        while row < y and col >= 0:
            key = row * y + col + 1
            diag_keys.append(key)
            row += 1
            col -= 1
        # Check this diagonal for winning sequences
        for i in range(len(diag_keys) - z + 1):
            combo_keys = diag_keys[i:i + z]
            compare_str = ''.join(board_dictionary[k] for k in combo_keys)
            if compare_str == current_symbol * z:
                be_winner = check_name
    return be_winner

def draw_checker(check_name, check_symbol):
    """
        Checks if winning is impossible on the current board        # perhaps the AI can play too?

        Draft: this will call check_winner and 
        append subsequently to all empty fields 
        the symbol of every player once.
        If be_winner == '' it returns draw
    """
    pass
    #print()
    #check_winner(check_name, check_symbol)
        #be_winner = 'draw'
    #return be_winner


# ... write as many functions as you need ...


# Tic-tac-toe game
if __name__ == "__main__":
    running = ''
    score1 = 0 # in a default value for many players
    score2 = 0
    print('\033[92m Welcome to a new version of Tic-Tac-Toe! \033[0m')
    print()
    name1, symbol1, name2, symbol2 = users_input()
    while running == '':
        # Start a new round of Tic-tac-toe
        winner = ''
        print()
        print("- ", name1, " score: ", score1) 
        print("- ", name2, " score: ", score2)
        print()  
        print('\033[92m Let us start a new round of Tic-Tac-Toe! \033[0m')
        x, y, z = board_square()        # x is for spaces in user symbols, y² is board size, z is winning condition
        board_dictionary = board_generator()
        board_printer()
        # the input beginns here
        for i in range(y**2):
            while winner == '':
                #draw_checker(name1, symbol1)                       PRIO
                pick1 = ask_field(name1) #check valid field loop    PRIO          
                field_filler(pick1, symbol1)
                board_printer()
                winner = check_winner(name1, symbol1)
                if winner != '':
                    break                                                                     # into one loop for many players
                #draw_checker(name1, symbol1)                       PRIO
                pick2 = ask_field(name2) #check valid field loop    PRIO
                field_filler(pick2, symbol2)
                board_printer()
                winner = check_winner(name2, symbol2)
        print()
        print(winner, "\033[92m Is the winner! \033[0m")
        print()
        if winner == name1:                                                                    # into one loop for many players
            score1 += 1
            print(name2, ",","\033[1;33m how about a revanche? \033[0m")           
        elif winner == name2:
            score2 += 1
            print(name1, ",","\033[1;33m how about a revanche? \033[0m")
        else:
            print("It's a draw! Shall we start a new round?") 
        running = input("Hit <Enter> for yes or any other key for no: ") or ''
        print()
        thanks()
        print()
    print("The game is over.")