import pygame
import math
import numpy as np

import vector_math

class RayTracer_camera:
    def __init__(self, screen, objects):
        self.obj = objects[0]
        self.lights = objects[1]

        self.pos = objects[2][0]
        self.epsilon = objects[2][1]
        self.MAX_STEPS = objects[2][2]
        self.MAX_DIST = objects[2][3]
        self.fov = objects[2][4]
        self.sky_color = (lambda c: tuple(int(max(0, min(1, x)) * 255) for x in c))(objects[2][5])
        
        self.screen = screen
        self.screen_res = self.screen.get_size()

        self.line_surface = pygame.Surface((self.screen_res[0], 1))
        self.framebuffer = np.zeros((self.screen_res[1], self.screen_res[0], 3), dtype=np.uint8)

        self.aspect_ratio = self.screen_res[0]/self.screen_res[1]
        self.scale = math.tan(math.radians(self.fov)/2)

        self.ray_dirs = []

        self.generate_ray_dirs()

    def in_shadow(self, p, light):
        light_dir = vector_math.normalize(vector_math.subtract(light.pos, p))

        shadow_origin = vector_math.two_vector_add(p, vector_math.vector_multiply(light_dir, self.epsilon * 10))
        t = 0.0
        max_dist_to_light = vector_math.length(vector_math.subtract(light.pos, p))

        for _ in range(self.MAX_STEPS):
            point = vector_math.two_vector_add(shadow_origin, vector_math.vector_multiply(light_dir, t))
            dist = min(objct.SDF(point) for objct in self.obj)

            if dist > self.MAX_DIST:
                return False

            if dist < self.epsilon:
                return True

            if t > max_dist_to_light:
                return False

            t += dist

        return False
    
    def generate_ray_dirs(self):
        for y in range(self.screen_res[1]):
            rows = []
            for x in range(self.screen_res[0]):
                uv_x = (2 * (x + 0.5) / self.screen_res[0] - 1) * self.aspect_ratio * self.scale
                uv_y = (1 - 2 * (y + 0.5) / self.screen_res[1]) * self.scale
                rows.append(vector_math.normalize((uv_x, uv_y, 1.0)))
            
            self.ray_dirs.append(rows)
    
    def raymarch(self, x, y):
        ray_origin = self.pos
        ray_dir = self.ray_dirs[y][x]
        
        t = 0.0

        p = ray_origin
        for _ in range(self.MAX_STEPS):
            p = (
            ray_origin[0] + ray_dir[0] * t,
            ray_origin[1] + ray_dir[1] * t,
            ray_origin[2] + ray_dir[2] * t
            )
            dist = min(((objct.SDF(p), objct) for objct in self.obj), key=lambda x: x[0])
            if dist[0] < self.epsilon:
                return True, dist[1], p, ray_dir
            
            if dist[0] > self.MAX_DIST:
                return False, None, p, ray_dir

            t += dist[0]
        return False, None, p, ray_dir

    def single_line_render(self, y):
        global framebuffer
        line_framebuf = np.full((self.screen_res[0], 3), self.sky_color, dtype=np.uint8)
        for i in range(self.screen_res[0]):
            hit, objct, p, ray_dir = self.raymarch(i, y)

            if hit:
                base_color = objct.object_color(p)
                normal = vector_math.get_normal(p, objct.SDF)
                final_color = [0.0, 0.0, 0.0]
                for light in self.lights:
                    light_dir = vector_math.normalize(vector_math.subtract(light.pos, p))

                    diffuse = max(vector_math.dot(normal, light_dir), 0.0)
                    specular = vector_math.calculate_specular(p, normal, ray_dir, light.pos)

                    if self.in_shadow(p, light):
                        diffuse *= 0.1
                        specular *= 0.0

                    final_color[0] += base_color[0] * diffuse + specular
                    final_color[1] += base_color[1] * diffuse + specular
                    final_color[2] += base_color[2] * diffuse + specular
                
                line_framebuf[i] = tuple(int(vector_math.clamp(c, 0, 1) * 255) for c in final_color)

        self.framebuffer[y] = line_framebuf