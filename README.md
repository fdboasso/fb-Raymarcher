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

4. A window will open.

5. Click **"Select Scene"** and choose a `.fb` scene file.

6. Click **"Render!"** to start rendering.

A sample scene is included (`Sample Scene.fb`) so you can test it immediately.

---

## Tested Platforms

The project should run on Windows as long as Python and dependencies are installed.

---

# How to Make Your Own Scenes

Scenes are stored in `.fb` files.

Each file is a simple text format that defines the camera, objects, lights, and optional screenshot settings.

Comments:

```txt
// This is a comment
```

---

# Important Rules

## No spaces inside coordinates

Coordinates must be written without spaces.

Correct:

```txt
sphere (0,5,20) 5 #FF0000
```

Incorrect:

```txt
sphere (0, 5, 20) 5 #FF0000
```

---

## Commands are not case-sensitive

```txt
sphere
SPHERE
Sphere
```

all work.

---

# Camera

The camera supports advanced rendering settings.

Syntax:

```txt
camera (x,y,z) epsilon MAX_STEPS MAX_DIST FOV #SKY_COLOR (width,height)
```

Parameters:

* (x,y,z) → camera position
* epsilon → raymarch precision (smaller = more accurate, slower)
* MAX_STEPS → max raymarch iterations
* MAX_DIST → max ray travel distance
* FOV → field of view (degrees)
* #SKY_COLOR → background color
* (width,height) → render resolution

Example:

```txt
camera (0,5,-20) 0.0001 600 1000 90 #87CEEB (1280,720)
```

---

# Sphere

```txt
sphere (x,y,z) radius #RRGGBB
```

Example:

```txt
sphere (0,5,20) 5 #FF0000
```

---

# Cube

```txt
cube (x1,y1,z1) (x2,y2,z2) #RRGGBB
```

---

# Pyramid

```txt
pyramid (x,y,z) size height #RRGGBB
```

---

# Infinite Floor

```txt
infinitefloor y_height #COLOR1 #COLOR2 tile_size
```

---

# Light

```txt
light (x,y,z) #RRGGBB
```

Example:

```txt
light (0,20,0) #FFFFFF
```

---

# Screenshot

Automatically saves the rendered image to the `screenshots` folder.

Syntax:

```txt
screenshot timestamp filename
```

Parameters:

* timestamp → true or false
* filename → output image name

Examples:

```txt
screenshot true MyRender
```

```txt
screenshot false FinalImage
```

---

# Example Scene

```txt
// Camera
camera (0,5,-30) 0.0001 600 1000 90 #87CEEB (1280,720)

// Screenshot
screenshot true SampleRender

// Floor
infinitefloor 0 #FFFFFF #000000 10

// Objects
sphere (0,5,20) 5 #FF0000
cube (-10,0,15) (-2,8,25) #00FF00
pyramid (10,0,20) 8 12 #FFFF00

// Lights
light (0,20,0) #FFFFFF
light (20,30,-10) #FFFFFF
```

---

# Performance Note

Lower epsilon + higher MAX_STEPS = better quality but MUCH slower.

If your scene is slow, increase epsilon or reduce MAX_STEPS.

The renderer displays render progress while rendering and reports timing information after completion.

---

# Help

This runs at ~20–30 seconds per frame on a low-end PC using the sample scene.

If someone knows optimization (math, raymarching, caching, vector tricks), contributions are welcome.
