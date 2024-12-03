# Game Improvements

Put link to your video demonstrating your feature here.  See assignment specs on what is required for this component

[Video Link](https://seneca-my.sharepoint.com/:v:/g/personal/kjgamis_myseneca_ca/EaTG1B1lMLlDruu5ruEe-uUBiTuVQOySAzfMMgTMpOBRig?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D&e=pwvcTc)

## Part C: Game Improvements

### 1. Added a timer to the game

Each human player is given 5 seconds for their turn, which does not apply to the AI. A counter is implemented such 
that if the player does not make a move within the time limit, the player will forfeit their turn and the it will be 
the opponent's turn. The timer is reset after each move, or when the game reset button is pressed. It is rendered 
as a descending countdown in the game.

Challenge in implementing the timer:

The timer is implemented by utilizing pygame's `pygame.time.get_ticks()` to calculate how much time has passed since
the turn started. The timer is then displayed on the screen as a countdown. The challenge was to ensure that the timer
was accurate and that it would reset after each player's turn. Additionally, when the timer reaches 0, the player's 
turn is forfeited by changing the `current_player` to the opponent..

### 2. Added a reset button

A reset button is added to the game that allows players to reset the game at anytime. Upon clicking the button, the 
moves, scoreboard and timer will be reset and the game will start from the beginning.

```python
reset_button_rect = pygame.Rect(900, 170, 200, 50)

# check for reset button click
elif event.type == pygame.MOUSEBUTTONDOWN:
        x, y = event.pos
        # Check if the mouse click is inside the reset button area
        if reset_button_rect.collidepoint(x, y):
            board = Board(GRID_SIZE[1], GRID_SIZE[0], p1_sprites, p2_sprites)
            status = ["", ""]
            current_player = 0
            player_scores = [0, 0]
            tournament_winner = False
            has_winner = False
            overflowing = False
            overflow_boards = Queue()
            numsteps = 0
            grid_col = -1
            grid_row = -1
            choice = [None, None]
            start_ticks = 0

# draw reset button as with black fill with white text
pygame.draw.rect(window, BLACK, (900, 170, 200, 50), 0)
font = pygame.font.Font(None, 36)
text = font.render("Reset", 1, WHITE)
window.blit(text, (950, 175))

...

```

Challenge in implementing the reset button:

I needed to learn how to draw elements in `pygame`, such as a simple rectangle, and how to detect mouse clicks within 
the boundary of the rectangle. I also needed to learn how to reset the game state when the reset button is clicked, 
thus it was important to determine which variables needed to be reset and how to reset them. Given more time, I 
would have implemented a cleaner solution to reset the game, such as creating a `reset()` function that would reset
all the necessary variables as the "base" state of the game to keep it modular and cleaner.

Currently, the timer is buggy when a player is againt the AI bot. The timer does not reset after the AI makes a move.
Given the time, I would investigate the cause of this bug and fix it.

### 2. Added a score counter to the game

A score counter is implemented to keep track of the number of wins for each player. The score is displayed in its 
dedicated scoreboard and is updated after each round. The score is reset when the reset button is clicked.

The purpose of the score counter is to simulate a tournament-style game where players can compete against each other 
until a certain number of wins is reached, in this case, 3 wins. This adds a competitive element to the game and allows 
players to track their progress.

```python
# init player scores and tournament winner
player_scores = [0, 0]  # Player 1 and Player 2 scores
tournament_winner = False

# check if there is a winner and update the score accordingly
win = board.check_win()
if win != 0:
    winner = 1
    p1_wins = p1_wins + 1
    if win == -1:
        winner = 2
        p2_wins = p2_wins + 1
    has_winner = True
    
    if player_scores[0] == 3:
        tournament_winner = 1  # Player 1 wins the tournament
    elif player_scores[1] == 3:
        tournament_winner = 2  # Player 2 wins the tournament

    board.reset()

# draw the scoreboard
pygame.draw.rect(window, BLACK, (900, 300, 200, 100), 2)
text = font.render("Score", 1, BLACK)
window.blit(text, (910, 305))

# Display the scores
text = font.render("Player 1:       " + str(player_scores[0]), 1, BLACK)
window.blit(text, (910, 335))
text = font.render("Player 2:       " + str(player_scores[1]), 1, BLACK)
window.blit(text, (910, 365))

# Display tournament instructions
text = font.render("The first player to score", 1, BLACK)
window.blit(text, (850, 500))
text = font.render("3pts wins the tournament", 1, BLACK)
window.blit(text, (850, 525))
```

The implementation of the scoreboard was relatively straightforward. I needed to keep track of the number of wins, 
and this was done by updating the scores after each round, incrementing the score of the winning player, and then 
checking if the score of either player reached 3. If a player reached 3 wins, the tournament winner would be declared.

Challenge in implementing the score counter:

The challenge in implementing the score counter was to ensure that the score was updated correctly after each round. 
Additionally, the scoreboard does not update when a player is against the AI bot. Given more time, I would investigate
the cause of this bug and fix it.
