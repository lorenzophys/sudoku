# Sudoku
## What's that?
**Sudoku** (/suːˈdoʊkuː/, /-ˈdɒk-/, /sə-/, originally called Number Place) is a logic-based, combinatorial number-placement puzzle. The objective is to fill a 9×9 grid with digits so that each column, each row, and each of the nine 3×3 subgrids that compose the grid (also called "boxes", "blocks", or "regions") contain all of the digits from 1 to 9. The puzzle setter provides a partially completed grid, which for a well-posed puzzle has a single solution.  [Wiki][wiki]

## How to use it?
You can play the playable version of it with your mouse and keyboard running */playable/main.py*.  
To use the text-based solver */solver/solver.py* import the SudokuSolver class and pass the board (2D list) to the constructor:
```python
game = SudokuSolver(board)
game.solve()
```
To see the backtracking algorithm in action run */solver/main.py* and press the Spacebar.

## Requirements
Python version: 3  
Libraries: pygame

## License
This project is licensed under the **MIT License** - see the *LICENSE.md* file for details

[wiki]: https://en.wikipedia.org/wiki/Sudoku
