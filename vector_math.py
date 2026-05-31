import math
import pygame

def length(v):
    return math.sqrt(v[0]**2 + v[1]**2 + v[2]**2)

def subtract(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def reflect(d, n):
    d_dot_n = dot(d, n)
    return (
        d[0] - 2 * d_dot_n * n[0],
        d[1] - 2 * d_dot_n * n[1],
        d[2] - 2 * d_dot_n * n[2],
    )

def clamp(x, a, b):
    return max(a, min(b, x))

def vector_multiply(v, b):
    return (v[0]*b, v[1]*b, v[2]*b)

def two_vector_add(v, vv):
    return (v[0]+vv[0], v[1]+vv[1], v[2]+vv[2])

def normalize(v):
    x, y, z = v
    inv_length = 1.0 / math.sqrt(x*x + y*y + z*z)
    return (
        x * inv_length,
        y * inv_length,
        z * inv_length
    )

def get_normal(p, SDF):
    eps = 0.0001

    dx = SDF((p[0] + eps, p[1], p[2])) - SDF((p[0] - eps, p[1], p[2]))
    dy = SDF((p[0], p[1] + eps, p[2])) - SDF((p[0], p[1] - eps, p[2]))
    dz = SDF((p[0], p[1], p[2] + eps)) - SDF((p[0], p[1], p[2] - eps))

    return normalize((dx, dy, dz))

def calculate_specular(p, n, rd, light_pos, shininess=32.0, ks=1.0):
    L = pygame.Vector3([
        light_pos[0] - p[0],
        light_pos[1] - p[1],
        light_pos[2] - p[2]
    ]).normalize().xyz
    
    V = pygame.Vector3([
        -rd[0],
        -rd[1],
        -rd[2]
    ]).normalize().xyz

    H = pygame.Vector3([
        L[0] + V[0],
        L[1] + V[1],
        L[2] + V[2]
    ]).normalize().xyz
    
    return ks * (max(0.0, dot(n, H)) ** shininess)