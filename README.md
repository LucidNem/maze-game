# Maze Solver

A visualization tool that generates random mazes and solves them using depth-first search algorithm.

## Description

This project implements a maze generator and solver with visual representation using Tkinter. It creates random mazes of customizable size and solves them using a depth-first search algorithm, visualizing the process in real-time.

## Features

- Random maze generation
- Depth-first search pathfinding algorithm
- Visual representation of the maze and solution path
- Animation of the solving process

## How It Works

1. The maze is represented as a grid of cells
2. Each cell has walls between it and adjacent cells
3. The maze generator uses a randomized depth-first search to create a perfect maze (no loops, one solution)
4. The maze solver uses backtracking to find a path from start to end
5. The solving process is animated to show exploration and backtracking

## Dependencies

- Python 3.x
- Tkinter 
## Usage

Run the main script to generate and solve a maze:

```bash
python main.py
```
