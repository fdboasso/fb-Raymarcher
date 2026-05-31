# Instructions

Raymarcher I built when I was bored, and I kept improving it month by month.

To try it out:

1. Run `install.bat`.
2. Run `main.py`.
3. Select a `.fb` scene file when prompted.

Don't worry, I included a sample scene (`samplescene.fb`) so you can test it immediately.

---

# How to Make Your Own Scenes

Scenes are stored in `.fb` files.

An `.fb` file is a plain text file that describes the camera, objects, and lights in a scene.

Comments can be added using:

```txt
// This is a comment
```

## Important Formatting Rules

### No spaces inside coordinates

Coordinates must be written without spaces.

✅ Correct:

```txt
sphere (0,5,20) 5 #FF0000
```

❌ Incorrect:

```txt
sphere (0, 5, 20) 5 #FF0000
```

The parser will not read coordinates correctly if spaces are included inside coordinate lists.

### Commands are not case-sensitive

All of the following work:

```txt
sphere
Sphere
SPHERE
SpHeRe
```

---

## Camera

Sets the camera position.

Syntax:

```txt
camera (x,y,z)
```

Example:

```txt
camera (0,5,-20)
```

---

## Sphere

Creates a sphere.

Syntax:

```txt
sphere (x,y,z) radius #RRGGBB
```

Example:

```txt
sphere (0,5,20) 5 #FF0000
```

---

## Cube

Creates a cube using two opposite corners.

Syntax:

```txt
cube (x1,y1,z1) (x2,y2,z2) #RRGGBB
```

Example:

```txt
cube (-5,0,10) (5,10,20) #00FF00
```

---

## Pyramid

Creates a pyramid.

Syntax:

```txt
pyramid (x,y,z) size height #RRGGBB
```

Example:

```txt
pyramid (10,0,20) 8 12 #FFFF00
```

---

## Infinite Floor

Creates an infinite checkerboard floor.

Syntax:

```txt
infinitefloor y_height #COLOR1 #COLOR2 tile_size
```

Example:

```txt
infinitefloor 0 #FFFFFF #000000 10
```

---

## Light

Creates a point light.

Syntax:

```txt
light (x,y,z)
```

Example:

```txt
light (0,20,0)
```

---

## Example Scene

```txt
// Camera
camera (0,5,-30)

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

Save it as:

```txt
myscene.fb
```

---

# Color Format

Colors use hexadecimal RGB values.

Examples:

```txt
#FF0000 Red
#00FF00 Green
#0000FF Blue
#FFFFFF White
#000000 Black
#FFFF00 Yellow
#FF00FF Magenta
#00FFFF Cyan
```

---

# Help Me

On my garbage PC, the sample scene renders at about **60–90 seconds per frame**.

If anybody is reading this and likes optimization, please take a look at the code and tell me what can be improved.

Any performance tips, pull requests, or optimization ideas are appreciated.
