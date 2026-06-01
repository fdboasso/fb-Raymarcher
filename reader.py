import ast

from objects.Sphere import Sphere
from objects.InfiniteFloor import InfiniteFloor
from objects.Cube import Cube
from objects.Light import Light
from objects.Pyramid import Pyramid

def Scene_Reader(filename):
    objects = []
    lights = []
    camera = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]

        for line in lines:
            if line.startswith("//"):
                continue

            if line.lower().startswith("sphere"):
                arguments = line.split()

                pos = tuple(ast.literal_eval(arguments[1]))
                radius = int(arguments[2])
                color = arguments[3]
                objects.append(Sphere(pos, radius, hex_to_rgb(color)))

            if line.lower().startswith("infinitefloor"):
                arguments = line.split()

                y_height = int(arguments[1])
                color1 = arguments[2]
                color2 = arguments[3]
                tile_size = int(arguments[4])
                objects.append(InfiniteFloor(y_height, hex_to_rgb(color1), hex_to_rgb(color2), tile_size))

            if line.lower().startswith("pyramid"):
                arguments = line.split()

                pos = tuple(ast.literal_eval(arguments[1]))
                size = int(arguments[2])
                height = int(arguments[3])
                color = arguments[4]

                objects.append(Pyramid(pos, size, height, hex_to_rgb(color)))

            if line.lower().startswith("cube"):
                arguments = line.split()

                corner1 = list(ast.literal_eval(arguments[1]))

                corner2 = list(ast.literal_eval(arguments[2]))

                color = hex_to_rgb(arguments[3])

                objects.append(Cube(corner1, corner2, color))

            if line.lower().startswith("light"):
                arguments = line.split()

                pos = ast.literal_eval(arguments[1])
                lights.append(Light(pos))

            if line.lower().startswith("camera"):
                arguments = line.split()
                pos = tuple(ast.literal_eval(arguments[1]))
                epsilon = float(arguments[2])
                MAX_STEPS = int(arguments[3])
                MAX_DIST = float(arguments[4])
                FOV = float(arguments[5])
                sky_color = hex_to_rgb(arguments[6])
                resolution = tuple(ast.literal_eval(arguments[7]))
                camera = [pos, epsilon, MAX_STEPS, MAX_DIST, FOV, sky_color, resolution]

    except FileNotFoundError:
        print("Error: The file was not found.")

    return [objects, lights, camera]

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i:i+2], 16) / 255 for i in (0, 2, 4))

def load_objects(path):
    return Scene_Reader(path)