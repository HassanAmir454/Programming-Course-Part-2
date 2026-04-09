import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- Cube vertices ---
cube = np.array([
    [-1,-1,-1], [1,-1,-1],
    [1, 1,-1], [-1, 1,-1],
    [-1,-1, 1], [1,-1, 1],
    [1, 1, 1], [-1, 1, 1]
])

# --- Edges ---
edges = [
    (0,1),(1,2),(2,3),(3,0),
    (4,5),(5,6),(6,7),(7,4),
    (0,4),(1,5),(2,6),(3,7)
]

# --- Rotation matrices ---
def rotate_x(theta):
    return np.array([
        [1, 0, 0],
        [0, np.cos(theta), -np.sin(theta)],
        [0, np.sin(theta),  np.cos(theta)]
    ])

def rotate_y(theta):
    return np.array([
        [ np.cos(theta), 0, np.sin(theta)],
        [0, 1, 0],
        [-np.sin(theta), 0, np.cos(theta)]
    ])

def rotate_z(theta):
    return np.array([
        [np.cos(theta), -np.sin(theta), 0],
        [np.sin(theta),  np.cos(theta), 0],
        [0, 0, 1]
    ])

def transform(shape, ax, ay, az):
    return shape @ rotate_x(ax) @ rotate_y(ay) @ rotate_z(az)

# --- UI ---
root = Tk()
root.title("Rotate Cube in 3D")

fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(111, projection='3d')
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack()

def update(val):
    ax.clear()

    rx = np.radians(x_slider.get())
    ry = np.radians(y_slider.get())
    rz = np.radians(z_slider.get())

    rotated = transform(cube, rx, ry, rz)

    for edge in edges:
        points = rotated[list(edge)]
        ax.plot(points[:,0], points[:,1], points[:,2], 'b')

    ax.set_xlim([-3,3])
    ax.set_ylim([-3,3])
    ax.set_zlim([-3,3])

    canvas.draw()

# --- Sliders ---
x_slider = Scale(root, from_=0, to=360, label="X", orient=HORIZONTAL, command=update)
y_slider = Scale(root, from_=0, to=360, label="Y", orient=HORIZONTAL, command=update)
z_slider = Scale(root, from_=0, to=360, label="Z", orient=HORIZONTAL, command=update)

x_slider.pack()
y_slider.pack()
z_slider.pack()

update(0)
root.mainloop()