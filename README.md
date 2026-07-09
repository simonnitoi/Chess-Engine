# Simple Chess Engine
A simple brute force materialistic chess algorithm.

## How it Works
- Uses the python chess library for all board logic and chess function.
- Sends board state to `GreedFish.py` which looks only at material, draws, and checkmates.
- Due to the nature of the algorithm, it is not recommended to go above 4 plies of depth in live play and 3 plies in self-play, as it is slow.

## Setup
1. Clone the repository.
2. Install dependencies listed in requirements.txt.
3. Run python `main.py`.