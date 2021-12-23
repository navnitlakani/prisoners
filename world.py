_world = {}
starting_position = (0, 0)
 
def load_tiles(level):
    """Parses a file that describes the world space into the _world object"""
    
    if level == '1':
        file = 'map.txt'
    else:
        file = 'map2.txt' 
       
    with open(file, 'r') as f:
        rows = f.readlines()
    x_max = len(rows[0].split('|')) # Assumes all rows contain the same number of tabs
    for y in range(len(rows)):
        cols = rows[y].split('|')
        for x in range(x_max):
            tile_name = cols[x].replace('\n', '') # Windows users may need to replace '\r\n'
            if tile_name == 'StartingRoom':
                global starting_position
                starting_position = (x, y)
            _world[(x, y)] = None if tile_name == '' else getattr(__import__('tiles'), tile_name)(x, y)

def tile_exists(x, y):
    return _world.get((x, y))