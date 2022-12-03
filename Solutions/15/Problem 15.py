'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
'''

# tried importing cache but didnt work :()
from functools import lru_cache

# due to the way the recursive calls are made, the runtime improves from hours to well under a second for grid_size 20
# there is a formula for this but obviously that's cheating...
# maxsize=None maeans it overrides the default 128 limit
@lru_cache(maxsize=None)
def explore(grid_size, x = 0, y = 0):
    routes = 0
    
    if x < grid_size:
        routes += explore(grid_size, x+1, y)
    if y < grid_size:
        routes += explore(grid_size, x, y+1)
    if x == grid_size and y == grid_size:
        return 1
    
    return routes


grid_side_length = 256

print(explore(grid_side_length))