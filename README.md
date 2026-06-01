# Instructions

Raymarcher I built when I was bored, and I kept improving it month by month.

To try it out:

1. Run `install.bat`.
2. Run `main.py`.
3. Select a `.fb` scene file when prompted.

A sample scene is included (`samplescene.fb`) so you can test it immediately.

---

# How to Make Your Own Scenes

Scenes are stored in `.fb` files.

Each file is a simple text format that defines the camera, objects, and lights.

Comments:

```txt id="cmt1"
// This is a comment
```

---

# Important Rules

## No spaces inside coordinates

Coordinates must be written without spaces.

✅ Correct:

```txt id="ok1"
sphere (0,5,20) 5 #FF0000
```

❌ Incorrect:

```txt id="bad1"
sphere (0, 5, 20) 5 #FF0000
```

---

## Commands are not case-sensitive

```txt id="case1"
sphere
SPHERE
Sphere
```

all work.

---

# Camera (UPDATED)

The camera now supports advanced rendering settings.

### Syntax:

```txt id="cam1"
camera (x,y,z) epsilon MAX_STEPS MAX_DIST FOV #SKY_COLOR (width,height)
```

---

### Parameters:

* `(x,y,z)` → camera position
* `epsilon` → precision of raymarching (smaller = more accurate, slower)
* `MAX_STEPS` → max raymarch iterations
* `MAX_DIST` → max ray travel distance
* `FOV` → field of view (degrees)
* `#SKY_COLOR` → background color (hex)
* `(width,height)` → resolution of render

---

### Example:

```txt id="cam2"
camera (0,5,-20) 0.0001 600 1000 90 #87CEEB (1280,720)
```

---

# Sphere

```txt id="s1"
sphere (x,y,z) radius #RRGGBB
```

Example:

```txt id="s2"
sphere (0,5,20) 5 #FF0000
```

---

# Cube

```txt id="c1"
cube (x1,y1,z1) (x2,y2,z2) #RRGGBB
```

---

# Pyramid

```txt id="p1"
pyramid (x,y,z) size height #RRGGBB
```

---

# Infinite Floor

```txt id="f1"
infinitefloor y_height #COLOR1 #COLOR2 tile_size
```

---

# Light

```txt id="l1"
light (x,y,z)
```

---

# Example Scene (NEW CAMERA FORMAT)

```txt id="ex1"
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
```

---

# Performance Note

Lower epsilon + higher MAX_STEPS = better quality but MUCH slower.

If your scene is slow, try increasing epsilon or lowering MAX_STEPS.

---

# Help Me

This runs at ~60–90 seconds per frame on my low-end PC using the sample scene.

If someone sees this and knows optimization (math, raymarching, caching, vector tricks), contributions are welcome.
