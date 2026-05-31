import vector_math

class Sphere:
    def __init__(self, pos, radius, color):
        self.pos = pos
        self.radius = radius
        self.color = color
    
    def object_color(self, p):
        return self.color

    def SDF(self, a):
        return vector_math.length(vector_math.subtract(a, self.pos)) - self.radius