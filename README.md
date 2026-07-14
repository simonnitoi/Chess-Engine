# Simple Chess Engine
A simple materialistic chess algorithm and tkinter GUI.

## How it Works
- Uses the python chess library for all board logic and chess function.
- Sends board state to `GreedFish.py` which looks only at material, draws, and checkmates. Uses minimax, alpha-beta pruning, move ordering, and quiescence search.
- Allows for play via a simple tkinter GUI.
- Due to the nature of the algorithm, it is not recommended to go above 5+3 full+quiscence depth, as it is slow.

## Setup
1. Clone the repository.
2. Install dependencies listed in requirements.txt.
3. Run python `main.py`.