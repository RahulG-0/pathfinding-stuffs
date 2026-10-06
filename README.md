# Pathfinding

An interactive A* pathfinding visualizer in Pygame, plus a screen-capture speed test.

## A* visualizer (`a-star.py`)

Draw a start point, an end point and walls on a grid, then watch A* search for the shortest path.

| Input | Action |
|---|---|
| Left click | Place the start, then the end, then walls |
| Right click | Erase a cell |
| Space | Run the search |
| C | Clear the grid |

The search uses a priority queue ordered by `f = g + h`, with Manhattan distance as the heuristic, and reconstructs the path by walking back through the `came_from` map.

## Screen capture test (`live pathfinding.py`)

Measures how fast the screen can be grabbed with `mss` and downscaled with OpenCV. It was a first step toward running pathfinding on a live view of the screen; the pathfinding part is not connected yet.

## Run

```bash
pip install pygame numpy
python a-star.py
```

The capture test additionally needs `mss`, `pillow`, `pyautogui` and `opencv-python`.
