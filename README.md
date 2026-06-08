Raymarcher I built when I was bored, and kept improving month by month. According to the folder properties, development started on Monday, March 16, 2026, at 8:22:11 PM.

## Running the Project

1. Make sure Python 3 is installed.
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the program:

```bash
python main.py
```

4. When prompted, select a `.fb` scene file.

A sample scene is included (`Sample Scene.fb`) so you can test it immediately.

---

## Tested Platforms

The project should run on Windows as long as Python and dependencies are installed.

---

# How to Make Your Own Scenes

Scenes are stored in `.fb` files.

Each file is a simple text format that defines the camera, objects, and lights.

Comments:

```txt
// This is a comment
```

---

# Important Rules

## No spaces inside coordinates

Coordinates must be written without spaces.

Correct:
sphere (0,5,20) 5 #FF0000

Incorrect:
sphere (0, 5, 20) 5 #FF0000

---

## Commands are not case-sensitive

sphere
SPHERE
Sphere

all work.

---

# Camera

The camera supports advanced rendering settings.

Syntax:
camera (x,y,z) epsilon MAX_STEPS MAX_DIST FOV #SKY_COLOR (width,height)

Parameters:
- (x,y,z) → camera position
- epsilon → raymarch precision (smaller = more accurate, slower)
- MAX_STEPS → max raymarch iterations
- MAX_DIST → max ray travel distance
- FOV → field of view (degrees)
- #SKY_COLOR → background color
- (width,height) → resolution

Example:
camera (0,5,-20) 0.0001 600 1000 90 #87CEEB (1280,720)

---

# Sphere

sphere (x,y,z) radius #RRGGBB

Example:
sphere (0,5,20) 5 #FF0000

---

# Cube

cube (x1,y1,z1) (x2,y2,z2) #RRGGBB

---

# Pyramid

pyramid (x,y,z) size height #RRGGBB

---

# Infinite Floor

infinitefloor y_height #COLOR1 #COLOR2 tile_size

---

# Light

light (x,y,z)

---

# Example Scene

// Camera
camera (0,5,-30) 0.0001 600 1000 90 #87CEEB (1280,720)

// Floor
infinitefloor 0 #FFFFFF #000000 10

// Objects
sphere (0,5,20) 5 #FF0000
cube (-10,0,15) (-2,8,25) #00FF00
pyramid (10,0,20) 8 12 #FFFF00

// Lights
light (0,20,0)
light (20,30,-10)

---

# Performance Note

Lower epsilon + higher MAX_STEPS = better quality but MUCH slower.

If your scene is slow, increase epsilon or reduce MAX_STEPS.

---

# Help

This runs at ~60–90 seconds per frame on a low-end PC using the sample scene.

If someone knows optimization (math, raymarching, caching, vector tricks), contributions are welcome.
