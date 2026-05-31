import numpy as np

class Pyramid:
    def __init__(self, pos, size, height, color):
        self.size = size
        self.height = height
        self.color = color
        self.pos = np.array(pos, dtype=float)
    
    def object_color(self, p):
        return self.color

    def SDF(self, p):
        p = np.array(p, dtype=float)

        p -= self.pos

        h = self.height
        
        p[0] /= self.size
        p[2] /= self.size
        
        m2 = h**2 + 0.25
        
        p[0], p[2] = abs(p[0]), abs(p[2])

        if p[2] > p[0]: p[0], p[2] = p[2], p[0]
            
        p[0] -= 0.5
        p[2] -= 0.5

        q = np.array([
            p[2],
            h * p[1] - 0.5 * p[0],
            h * p[0] + 0.5 * p[1]
        ])
        
        s = max(-q[0], 0.0)

        t = np.clip(
            (q[1] - 0.5 * p[2]) / (m2 + 0.25),
            0.0,
            1.0
        )
        
        a = m2 * (q[0] + s)**2 + q[1]**2
        b = m2 * (q[0] + 0.5 * t)**2 + (q[1] - m2 * t)**2
        
        d2 = (
            min(a, b)
            if min(q[1], -q[0] * m2 - q[1] * 0.5) <= 0.0
            else 0.0
        )
        
        return (
            np.sqrt((d2 + q[2]**2) / m2)
            * np.sign(max(q[2], -p[1]))
            * self.size
        )