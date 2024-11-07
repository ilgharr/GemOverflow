# Main Author:
# Main Reviewer:

# This function duplicates and returns the board. You may find this useful
def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board


# this function is your evaluation function for the board
def evaluate_board (board, player):
    return 0

class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height = 4):
            pass

    def __init__(self, board, player, tree_height = 4):
        self.player = player
        self.board = copy_board(board)
        # you will need to implement the creation of the game tree here.  After this function completes,
        # a full game tree will be created.
        # hint: as with many tree structures, you will need to define a self.root that points to the root
        # of the game tree.  To create the tree itself, a recursive function will likely be the easiest as you will
        # need to apply the minimax algorithm to its creation.




    # this function is a pure stub.  It is here to ensure the game runs.  Once you complete
    # the GameTree, you will use it to determine what to return.
    def get_move(self):
        height = len(self.board)
        width = len(self.board[0])
        if self.player == 1:
            return (0, 0)
        else:
            return (height-1, width-1)
   
    def clear_tree(self):
        pass     

    