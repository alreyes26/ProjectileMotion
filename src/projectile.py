import numpy as np
import matplotlib.pyplot as plt

plt.style.use("../themes/rose-pine-moon.mplstyle")


class Projectile:
    def __init__(self, v0, theta, time):
        self.initial_velocity = v0
        self.launch_angle = theta
        self.g = 9.81
        self.time_step = time

        theta_rad = np.radians(theta)

        vx = v0 * np.cos(theta_rad)
        vy = v0 * np.sin(theta_rad)

        x, y = 0, 0

        x_data, y_data = [x], [y]

        while y >= 0:
            x += vx * self.time_step
            vy -= self.g * self.time_step
            y += vy * self.time_step

            x_data.append(x)
            y_data.append(y)

        max_index = y_data.index(max(y_data))

        plt.plot(
            x_data,
            y_data,
            linewidth=3
        )

        plt.scatter(
            x_data[0],
            y_data[0],
            s=70,
            label="Launch"
        )

        plt.scatter(
            x_data[max_index],
            y_data[max_index],
            s=70,
            label="Max Height"
        )

        plt.scatter(
            x_data[-1],
            y_data[-1],
            s=70,
            label="Landing"
        )

        plt.xlabel(
            "Horizontal Distance (m)",
            fontsize=11
        )

        plt.ylabel(
            "Vertical Distance (m)",
            fontsize=11
        )

        plt.title(
            "Projectile Motion",
            fontsize=16,
            pad=15
        )

        plt.grid(
            True,
            alpha=0.25
        )

        ax = plt.gca()

        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

        plt.legend(
            frameon=False
        )

        plt.tight_layout()

        plt.show()


if __name__ == "__main__":
    Projectile(
        v0=20,
        theta=45,
        time=0.01
    )