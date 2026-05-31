import pygame
from PIL import Image

import numpy as np

import time

from camera import *
from reader import *

from tkinter import Tk
from tkinter.filedialog import askopenfilename

import os

pygame.init()

Tk().withdraw()

filename = ""
while not filename:
    filename = askopenfilename(filetypes=[("Fboasso's Scene files", "*.fb")])
objects = load_objects(filename)

if not any(objects[:3]):
    print("Error: Empty .fb file")
    pygame.quit()
    quit()

screen_res = [720, 480]
screen = pygame.display.set_mode(screen_res)

font = pygame.font.Font(None, 50)
text = font.render("", True, (255, 255, 255))
text_rect = text.get_rect(topleft=(0,0))

camera = RayTracer_camera(screen, objects)

line = 0

fps_stopwatch = time.time()
frame_made = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if line < screen_res[1]:
        camera.single_line_render(line)
        screen.fill((0,0,0))

        progress = (line / screen_res[1]) * 100
        text = font.render(f"{progress:.1f}% Baked!", True, (255, 255, 255))
        screen.blit(text, text_rect)

        line += 1

    elif line >= screen_res[1] and not frame_made:
        frame_made = True

        now = time.localtime()
        out = np.clip(camera.framebuffer, 0, 255).astype(np.uint8)

        t = time.time() - fps_stopwatch
        pygame.display.set_caption(f"SPF: {round(t,2)} | SPL: {round(t/screen_res[1],2)}")

        screen.fill((0,0,0))
        surface = pygame.image.frombuffer(out.tobytes(), (screen_res[0], screen_res[1]), "RGB")
        screen.blit(surface, (0, 0))

        name = input("Insert a name for this render: ")
        os.makedirs("screenshots", exist_ok=True)
        filename = (f"screenshots/Image {name} {now.tm_year}{now.tm_mon}{now.tm_mday} {now.tm_hour}-{now.tm_min}-{now.tm_sec}.png")
        Image.fromarray(out).save(filename)
    
    pygame.display.flip()