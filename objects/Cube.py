import vector_math

class Cube:
    def __init__(self, corner1, corner2, color):
        self.corner1 = corner1
        self.corner2 = corner2
        self.color = color

    def object_color(self, p):
        return self.color

    def SDF(self, a):
        center = (
            (self.corner1[0] + self.corner2[0]) * 0.5,
            (self.corner1[1] + self.corner2[1]) * 0.5,
            (self.corner1[2] + self.corner2[2]) * 0.5
        )
        
        half_size = (
            (self.corner2[0] - self.corner1[0]) * 0.5,
            (self.corner2[1] - self.corner1[1]) * 0.5,
            (self.corner2[2] - self.corner1[2]) * 0.5
        )
        
        p_local = vector_math.subtract(a, center)
        d = (
            abs(p_local[0]) - half_size[0],
            abs(p_local[1]) - half_size[1],
            abs(p_local[2]) - half_size[2]
        )
        
        outside = (
            max(d[0], 0.0),
            max(d[1], 0.0),
            max(d[2], 0.0)
        )
        outside_dist = vector_math.length(outside)
        
        inside_dist = min(max(d[0], max(d[1], d[2])), 0.0)
        
        return outside_dist + inside_dist