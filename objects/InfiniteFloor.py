import math

class InfiniteFloor:
    def __init__(self, ypos, color, color1, tile_size):
        self.ypos = ypos
        self.color = color
        self.color1 = color1
        self.tile_size = tile_size

    def object_color(self, p):
        tile = (math.floor(p[0]/self.tile_size) + math.floor(p[2]/self.tile_size)) % 2
        return self.color if tile == 0 else self.color1

    def SDF(self, a):
        return a[1] - self.ypos