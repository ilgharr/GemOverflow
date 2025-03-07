# **Gem Overflow DSA Project**

This project involves implementing a custom Hash Table, creating a Game Tree-based AI bot using the Minimax algorithm, and enhancing a 2D board game with visual animations.

---

### **Hash Table Implementation**

**Objective:**
Implement a `HashTable` class with the following features:
1. Support for collision handling using **chaining** or **linear probing**.
2. Dynamically resize the table when the **load factor exceeds 0.7**.

#### **Member Functions**
- `__init__(self, capacity=32)`: Initializes the hash table with `capacity` (default: 32).
- `insert(self, key, value)`: Adds a new key-value pair if the key doesn’t exist. Returns `True` on success, `False` otherwise.
- `modify(self, key, value)`: Modifies an existing key-value pair. Returns `True` on success, `False` otherwise.
- `remove(self, key)`: Removes a key-value pair by key. Returns `True` on success, `False` otherwise.
- `search(self, key)`: Searches for a key and returns the associated value, or `None` if the key is not found.
- `capacity(self)`: Returns the total capacity of the hash table.
- `__len__(self)`: Returns the number of elements in the hash table.
---

### **PGame Tree and AI-based Bot**

**Objective:**  
Develop and implement a **Game Tree** to create an AI bot that selects the optimal moves for a simple 2D board game.

#### **Requirements**
1. **Evaluation Function:**
   - `evaluate_board(board, player)`:
     - **Input**: `board` (2D grid) and `player` (+1 or -1).
     - **Output**: Score of the board (higher for favorable boards, lower for unfavorable boards).
2. **Game Tree:**
   - Build the tree with nodes representing different game states up to a depth (`tree_height`).
   - Use the **Minimax Algorithm** to evaluate moves and score states:
     - **Even Levels** (player's turn): Take the **maximum** score from child nodes.
     - **Odd Levels** (opponent's turn): Take the **minimum** score from child nodes.

---

#### **GameTree Class**
- `__init__(board, player, tree_height=4)`: Build a game tree to a depth defined by `tree_height`.
- `get_move(self)`: Returns the best possible move `(row, col)` for the current state.
- `clear_tree(self)`: Clears the tree for garbage collection.

---

## **How to Use**

1. Clone the repository:
   ```bash
   git clone <REPO_LINK>
   cd <REPO_DIRECTORY>
   ```
2. Run the game:
   ```bash
   python game.py
   ```

---