from manim import *
from numpy import *

g = 9.8
L = 2
mu = 0.1

def get_theta_double_dot(theta, theta_dot):
    return -mu * theta_dot - (g / L) * np.sin(theta)

def theta(t):
    theta = THETA_0
    theta_dot = THETA_DOT_0
    delta_t = 0.01
    for time in np.arange(0, t, delta_t):
        theta_double_dot = get_theta_double_dot(
            theta, theta_dot
        )
        theta += theta_dot * delta_t
        theta_dot += theta_double_dot * delta_t
    return theta

class a(Scene):
    def construct(self):
        t = 10
        # th = theta(t)
        # print(th)