import numpy as np


def bezier_curve(P0, P1, P2, P3, t):
    return (
        np.outer((1 - t) ** 3, P0)
        + np.outer(3 * t * (1 - t) ** 2, P1)
        + np.outer(3 * t**2 * (1 - t), P2)
        + np.outer(t**3, P3)
    )


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    P0 = np.array([0, 0])
    P1 = np.array([1, 2])
    P2 = np.array([3, 3])
    P3 = np.array([4, 0])
    t = np.linspace(0, 1, 100)
    B_t = bezier_curve(P0, P1, P2, P3, t)

    plt.plot(
        [P0[0], P1[0], P2[0], P3[0]],
        [P0[1], P1[1], P2[1], P3[1]],
        "ro--",
        label="Control Points",
    )
    plt.plot(B_t[:, 0], B_t[:, 1], label="Bezier Curve")
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.title("Third Degree Bezier Curve")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()
