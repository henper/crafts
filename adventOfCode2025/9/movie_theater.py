from input import tiles

max_area = 0
for tile_idx, tile in enumerate(tiles[:-1]):
    for opposite in tiles[tile_idx+1:]:
        ax,ay = tile
        bx,by = opposite

        width  = abs(ax-bx)+1
        height = abs(ay-by)+1

        max_area = max(width*height, max_area)

        #print(f'({ax},{ay}) x ({bx},{by}). Width: {width} Height: {height} Area {width*height}')

print(f'max_area: {max_area}')
