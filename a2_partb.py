# Main Author: Ilghar Rahno 137542213
# Main Reviewer:

# This function duplicates and returns the board.
def copy_board(board):
    current_board = []
    height = len(board)
    # Copy each row of the board
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board


# This function evaluates the board state by calculating the difference in pieces between players
def evaluate_board(board, player):
    player_pieces = 0
    opponent_pieces = 0
    # Count pieces for both players
    for row in board:
        for cell in row:
            if cell > 0:
                if player == 1:
                    player_pieces += cell
                else:
                    opponent_pieces += cell
            elif cell < 0:
                if player == -1:
                    player_pieces -= cell
                else:
                    opponent_pieces -= cell
    # Return very high or very low value if one player has no pieces
    if opponent_pieces == 0 and player_pieces > 0:
        return float('inf')
    if player_pieces == 0 and opponent_pieces > 0:
        return float('-inf')
    # Return the difference in pieces for the current player
    return player_pieces - opponent_pieces if player == 1 else opponent_pieces - player_pieces


# Class representing a game tree for decision making
class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height=4):
            self.board = copy_board(board)
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.children = []
            self.value = evaluate_board(board, player)
            # Expand the tree if the current depth is less than the maximum tree height
            if depth < tree_height:
                self.expand()

        # Expands the tree by generating possible moves and their corresponding states
        def expand(self):
            next_player = 1 if self.player == -1 else -1
            for move in self.get_possible_moves(self.board, self.player):
                new_board = self.make_move(self.board, move, self.player)
                self.children.append(GameTree.Node(new_board, self.depth + 1, next_player, self.tree_height))

        # Returns a list of all possible moves for the given board state and player
        def get_possible_moves(self, board, player):
            possible_moves = []
            rows = len(board)
            cols = len(board[0]) if rows > 0 else 0
            # Possible moves are empty cells
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] == 0:
                        possible_moves.append((r, c))
            return possible_moves

        # Returns a new board state after making a move
        def make_move(self, board, move, player):
            new_board = copy_board(board)
            r, c = move
            new_board[r][c] = player
            return new_board

    # Initializes the game tree
    def __init__(self, board, player, tree_height=4):
        self.player = player
        self.board = copy_board(board)
        self.root = self.Node(board, 0, player, tree_height)

    # Minimax algorithm for optimizing the game play
    def minimax(self, node, depth, maximizing_player):
        if depth == 0 or not node.children:
            return node.value
        if maximizing_player:
            max_eval = float('-inf')
            for child in node.children:
                evl = self.minimax(child, depth - 1, False)
                max_eval = max(max_eval, evl)
            return max_eval
        else:
            min_eval = float('inf')
            for child in node.children:
                evl = self.minimax(child, depth - 1, True)
                min_eval = min(min_eval, evl)
            return min_eval

    # Returns the best move based on the minimax evaluation
    def get_move(self):
        best_value = float('-inf') if self.player == 1 else float('inf')
        best_move = None
        for child in self.root.children:
            evl = self.minimax(child, self.root.tree_height - self.root.depth, self.player == -1)
            if (self.player == 1 and evl > best_value) or (self.player == -1 and evl < best_value):
                best_value = evl
                best_move = child
        if best_move:
            for r in range(len(self.board)):
                for c in range(len(self.board[0])):
                    if self.board[r][c] != best_move.board[r][c]:
                        return (r, c + 1)
        return None

    def clear_tree(self):
        self.root = None