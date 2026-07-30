# Pseudocode for Python Tic Tac Toe

## General Ideas

* Tic Tac Toe is played by **two players**.
* The players enter their **names at the start of the game**.
* Player 1 chooses a marker (**X** or **O**).
* Player 2 automatically receives the remaining marker.
* Player 1 always takes the **first turn**.
* The game board is represented using a **3 × 3 nested list** called `board`.
* Each position in the board initially contains `" "` (empty space), meaning the position has not been played.
* During the game, positions are replaced with `"X"` or `"O"` depending on the player's move.
* Players enter moves using **row and column numbers from 1 to 3**.

Example board coordinates:

```text
(1,1) | (1,2) | (1,3)
---------------------
(2,1) | (2,2) | (2,3)
---------------------
(3,1) | (3,2) | (3,3)
```

Example displayed board:

```text
   |   |  
---------
   | O |  
---------
 X | O | X
```

This board would be stored as:

```text
board = [
    [" ", " ", " "],
    [" ", "O", " "],
    ["X", "O", "X"]
]
```

Rules:

* Players take turns placing their marker.
* A player wins by placing **three matching markers in a row, column, or diagonal**.
* If all positions are filled and nobody wins, the game ends in a **draw**.

---

## Game Logic

```text
BEGIN TIC_TAC_TOE_GAME

OUTPUT "Welcome to Tic Tac Toe"

CREATE empty 3 by 3 board

INPUT Player 1 name
INPUT Player 2 name

INPUT Player 1 marker

WHILE Player 1 marker is not "X" AND not "O"
    OUTPUT "Invalid marker. Choose X or O"
    INPUT Player 1 marker
END WHILE

IF Player 1 marker = "X" THEN
    SET Player 2 marker = "O"
ELSE
    SET Player 2 marker = "X"
END IF

SET current player = Player 1

WHILE game has not ended

    OUTPUT current board

    OUTPUT current player's name
    OUTPUT current player's marker

    REPEAT

        INPUT row and column

        IF row OR column is outside 1 to 3 THEN
            OUTPUT "Invalid input"

        ELSE IF selected board position is occupied THEN
            OUTPUT "That spot is already taken"

        ELSE
            PLACE current player's marker on board
        END IF

    UNTIL move is accepted

    IF current player has three markers
       in a row, column, or diagonal THEN

        OUTPUT current board
        OUTPUT current player's name + " wins"

        STOP

    ELSE IF board contains no empty spaces THEN

        OUTPUT current board
        OUTPUT "It's a draw"

        STOP

    ELSE

        SWITCH current player

    END IF

END WHILE

END TIC_TAC_TOE_GAME
```
