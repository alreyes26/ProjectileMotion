import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, v0, theta, time):
        self.initial_velocity = v0
        self.launch_angle = np.degrees(theta)
        self.g = 9.81
        self.time = time
        theta_rad = np.radians(theta)
        vx = v0 * np.cos(theta_rad)
        vy = v0 * np.sin(theta_rad)
        x, y = 0, 0
        x_data, y_data = [x], [y]

        while y >= 0:
        x += vx * dt
        vy -= g * dt
        y += vy * dt
        x_data.append(x)
        y_data.append(y)

        plt.plot(x_data, y_data)
        plt.xlabel("Horizontal Distance (m)")
        plt.ylabel("Vertical Distance (m)")
        plt.title("Projectile Motion")
        plt.grid(True)
        plt.show()
        