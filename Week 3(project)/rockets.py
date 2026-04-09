# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# import tkinter as tk
# from tkinter import messagebox
# import time
# import threading

# # -------------------------------
# # CONFIG
# # -------------------------------
# STEP_SIZE = 1.2
# SAFE_DISTANCE = 5
# THRESHOLD = 2

# # -------------------------------
# # INITIAL POSITIONS (CHANGE HERE)
# # -------------------------------
# rocket1 = np.array([10.0, 80.0])
# rocket2 = np.array([80.0, 10.0])
# moon = np.array([80.0, 90.0])

# # Step counters
# steps1 = 0
# steps2 = 0

# # Reached flags
# reached1 = False
# reached2 = False

# # -------------------------------
# # HELPER FUNCTION
# # -------------------------------
# def unit_vector(vec):
#     return vec / np.linalg.norm(vec)

# # -------------------------------
# # COUNTDOWN
# # -------------------------------
# def countdown():
#     for i in range(3, 0, -1):
#         print(f"Launching in {i}...")
#         time.sleep(1)
#     print("🚀 Launch!")

# # -------------------------------
# # UPDATE FUNCTION
# # -------------------------------
# def update(frame):
#     global rocket1, rocket2, steps1, steps2
#     global reached1, reached2

#     # Rocket 1 movement
#     if not reached1:
#         dir1 = unit_vector(moon - rocket1)
#         rocket1 += dir1 * STEP_SIZE
#         steps1 += 1

#         if np.linalg.norm(rocket1 - moon) < THRESHOLD:
#             reached1 = True

#     # Rocket 2 movement
#     if not reached2:
#         dir2 = unit_vector(moon - rocket2)
#         rocket2 += dir2 * STEP_SIZE
#         steps2 += 1

#         if np.linalg.norm(rocket2 - moon) < THRESHOLD:
#             reached2 = True

#     # Collision avoidance (only if both still moving)
#     if not reached1 and not reached2:
#         distance = np.linalg.norm(rocket1 - rocket2)
#         if distance < SAFE_DISTANCE:
#             adjust = unit_vector(rocket1 - rocket2)
#             rocket1 += adjust
#             rocket2 -= adjust

#     # Clear plot
#     ax.clear()

#     # Draw points
#     ax.scatter(*rocket1, color='red', label=f'Rocket 1 (steps: {steps1})')
#     ax.scatter(*rocket2, color='green', label=f'Rocket 2 (steps: {steps2})')
#     ax.scatter(*moon, color='yellow', label='Moon')

#     # Styling
#     ax.set_xlim(0, 100)
#     ax.set_ylim(0, 100)
#     ax.set_title("🚀 Rockets Traveling to Moon")
#     ax.legend()

#     # Stop when BOTH reach
#     if reached1 and reached2:
#         ani.event_source.stop()

#         root = tk.Tk()
#         root.withdraw()

#         messagebox.showinfo(
#             "Mission Complete",
#             f"Rocket 1 steps: {steps1}\nRocket 2 steps: {steps2}"
#         )

# # -------------------------------
# # RUN SIMULATION
# # -------------------------------
# def run_simulation():
#     global fig, ax, ani

#     countdown()

#     fig, ax = plt.subplots()
#     ani = FuncAnimation(fig, update, interval=100)
#     plt.show()

# # -------------------------------
# # START THREAD
# # -------------------------------
# thread = threading.Thread(target=run_simulation)
# thread.start()


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import messagebox
import time
import threading

# -------------------------------
# CONFIG
# -------------------------------
STEP_SIZE = 1.2
SAFE_DISTANCE = 5
THRESHOLD = 2

# -------------------------------
# INITIAL POSITIONS (CHANGE HERE)
# -------------------------------
rocket1 = np.array([10.0, 80.0])
rocket2 = np.array([80.0, 10.0])
moon = np.array([80.0, 90.0])

# Step counters
steps1 = 0
steps2 = 0

# Reached flags
reached1 = False
reached2 = False

# -------------------------------
# HELPER FUNCTION
# -------------------------------
def unit_vector(vec):
    return vec / np.linalg.norm(vec)

# -------------------------------
# COUNTDOWN
# -------------------------------
def countdown():
    for i in range(3, 0, -1):
        print(f"Launching in {i}...")
        time.sleep(1)
    print("🚀 Launch!")

# -------------------------------
# UPDATE FUNCTION
# -------------------------------
def update(frame):
    global rocket1, rocket2, steps1, steps2
    global reached1, reached2

    # Rocket 1 movement
    if not reached1:
        dir1 = unit_vector(moon - rocket1)
        rocket1 += dir1 * STEP_SIZE
        steps1 += 1

        if np.linalg.norm(rocket1 - moon) < THRESHOLD:
            reached1 = True

    # Rocket 2 movement
    if not reached2:
        dir2 = unit_vector(moon - rocket2)
        rocket2 += dir2 * STEP_SIZE
        steps2 += 1

        if np.linalg.norm(rocket2 - moon) < THRESHOLD:
            reached2 = True

    # Collision avoidance
    if not reached1 and not reached2:
        distance = np.linalg.norm(rocket1 - rocket2)
        if distance < SAFE_DISTANCE:
            adjust = unit_vector(rocket1 - rocket2)
            rocket1 += adjust
            rocket2 -= adjust

    # Clear plot
    ax.clear()

    # Draw points
    ax.scatter(*rocket1, color='red', label=f'Rocket 1 (steps: {steps1})')
    ax.scatter(*rocket2, color='green', label=f'Rocket 2 (steps: {steps2})')
    ax.scatter(*moon, color='yellow', label='Moon')

    # Styling
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_title("🚀 Rockets Traveling to Moon")

    # ✅ FIXED LEGEND POSITION
    ax.legend(loc='upper left')

    # Stop when BOTH reach
    if reached1 and reached2:
        ani.event_source.stop()

        root = tk.Tk()
        root.withdraw()

        messagebox.showinfo(
            "Mission Complete",
            f"Rocket 1 steps: {steps1}\nRocket 2 steps: {steps2}"
        )

# -------------------------------
# RUN SIMULATION
# -------------------------------
def run_simulation():
    global fig, ax, ani

    countdown()

    fig, ax = plt.subplots()
    ani = FuncAnimation(fig, update, interval=100)
    plt.show()

# -------------------------------
# START THREAD
# -------------------------------
thread = threading.Thread(target=run_simulation)
thread.start()