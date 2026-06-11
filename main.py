import pygame
from PIL import Image

import numpy as np

import time

from camera import *
from reader import *

from tkinter import Tk
from tkinter.filedialog import askopenfilename

import os

from concurrent.futures import ThreadPoolExecutor

pygame.init()

objects = None
camera = None
screen_res = (800, 600)
render_mode = False

screen = pygame.display.set_mode(screen_res)
pygame.display.set_caption(".FB raymarcher")

line = 0
frame_made = False

clock = pygame.time.Clock()
fps_stopwatch = 0

font = pygame.font.Font(None, 50)

filename = None

cores_amount = os.cpu_count()
executor = ThreadPoolExecutor(max_workers=max(1, os.cpu_count()))

title = font.render(".FB Raymarcher", True, (255, 255, 255))
title_rect = title.get_rect(center=(screen_res[0]/2, 100))

SS_button_size = (400, 100)
button_color = (100, 200, 100)
Select_scene_rect = pygame.Rect(screen_res[0]/2-SS_button_size[0]/2, 200-SS_button_size[1]/2, SS_button_size[0], SS_button_size[1])
SS_text = font.render("Select Scene", True, (0, 0, 0))
SS_text_rect = SS_text.get_rect(center=(screen_res[0]/2, 200))

button_size = (200, 100)
Render_rect = pygame.Rect(screen_res[0]/2-SS_button_size[0]/2, 350-SS_button_size[1]/2, SS_button_size[0], SS_button_size[1])
Render_text = font.render("Render!", True, (0, 0, 0))
Render_text_rect = Render_text.get_rect(center=(screen_res[0]/2, 350))

Error_text = font.render("", True, (255, 0, 0))
Error_text_rect = Render_text.get_rect(center=(screen_res[0]//2, 450))

Percent_text = font.render("", True, (255, 0, 0))
Percent_text_rect = Render_text.get_rect(topleft=(0, 0))

def update_error(text):
    global Error_text, Error_text_rect, filename
    Error_text = font.render(text, True, (255, 0, 0))
    Error_text_rect = Error_text.get_rect(center=(screen_res[0] // 2, 450))
    if text:
        filename = None

def Select_scene():
    global objects, camera, screen_res, screen, Error_text, filename, Error_text_rect

    Tk().withdraw()

    filename = askopenfilename(filetypes=[("Fboasso's Scene files", "*.fb")])
    if not filename:
        filename = None
        return

    objects = load_objects(filename)

    if not any(objects[:3]):
        update_error("Error: Empty .fb file.")
        return
    elif not objects[2]:
        update_error("Error: There's no camera.")
        return

    screen_res = objects[2][6]

    camera = RayTracer_camera(screen, objects)
    update_error("")

def Render():
    global render_mode, fps_stopwatch, screen, line, frame_made

    screen = pygame.display.set_mode(objects[2][6])
    fps_stopwatch = time.time()
    render_mode = True

    line = 0
    frame_made = False

running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))
    if not render_mode:
        mouse_pos = pygame.mouse.get_pos()

        screen.blit(title, title_rect)

        screen.blit(Error_text, Error_text_rect)

        pygame.draw.rect(screen, button_color, Select_scene_rect)
        screen.blit(SS_text, SS_text_rect)
        if Select_scene_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, (150, 255, 150), Select_scene_rect, 3)

            if event.type == pygame.MOUSEBUTTONDOWN:
                Select_scene()

        if filename != None:
            pygame.draw.rect(screen, button_color, Render_rect)
            screen.blit(Render_text, Render_text_rect)
            if Render_rect.collidepoint(mouse_pos):
                pygame.draw.rect(screen, (150, 255, 150), Render_rect, 3)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    Render()

    elif line < screen_res[1] and render_mode:
        start = line
        end = min(line + cores_amount, screen_res[1])

        list(
            executor.map(
                camera.single_line_render,
                range(start, end)
            )
        )

        line = end

        progress = (line / screen_res[1]) * 100
        Percent_text = font.render(f"{progress:.1f}% Baked!", True, (255, 255, 255))
        screen.blit(Percent_text, Percent_text_rect)

    elif line >= screen_res[1] and not frame_made and render_mode:
        frame_made = True

        now = time.localtime()
        out = np.clip(camera.framebuffer, 0, 255).astype(np.uint8)

        t = time.time() - fps_stopwatch
        pygame.display.set_caption(f"SPF: {round(t,2)} |  SPL: {round(t/screen_res[1],2)}")

        screen.fill((0,0,0))
        surface = pygame.surfarray.make_surface(out.swapaxes(0, 1))
        screen.blit(surface, (0, 0))
        if objects[3]:
            if objects[3][1]:
                os.makedirs("screenshots", exist_ok=True)
                filename = (f"screenshots/{objects[3][1]} {now.tm_year}{now.tm_mon}{now.tm_mday} {now.tm_hour}-{now.tm_min}-{now.tm_sec}.png")
                Image.fromarray(out).save(filename)
            else:
                os.makedirs("screenshots", exist_ok=True)
                filename = (f"screenshots/{objects[3][1]}.png")
                Image.fromarray(out).save(filename)

    if frame_made:
        screen.blit(surface, (0, 0))
    pygame.display.flip()