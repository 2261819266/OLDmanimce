# from manim import *

# def exp(x): return np.exp(x)

# def f(x) :
#     return exp(1j * x) - exp(2j * x) + exp(3j * x) + 1

# class COMPLEX(Scene):
#     def construct(self):
#         grid = ComplexPlane().add_coordinates()

#         self.play(FadeIn(grid))


#         # func = ParametricFunction(f, t_range=(0, 2 * PI))

#         for i in np.arange(0, 2 * PI, 0.01):
#             dot = Dot(grid.n2p(f(i)), radius=0.04, color = RED)
#             self.add(dot)
#             # self.play(FadeIn(dot), run_time = 0.05)

#         # self.play(Write(func))

#         self.wait()

# import numpy as np
# import matplotlib.pyplot as plt
# from manim import *

# P = 1
# k = 1
# m = 1


# # 定义二次曲线方程
# def quadratic_equation(t, v):
#     # return a*x**2 + b*x + c
#     # return ((6 nroot(P k^(2) x,3))/(m))-((π)/(sqrt(3)))=ln(1+((3 nroot(P k,3) y)/((nroot(P,3)-nroot(k,3) y)^(2))))-2 sqrt(3) tan^(-1)(((1+2 nroot(((k)/(P)),3) y)/(sqrt(3))))
#     return 6 * (P * k ** 2 * t) ** 3 / m - PI / sqrt(3)

# # 生成 x 值的范围
# x = np.linspace(-5, 5, 1000)

# # 计算 y 值
# y = quadratic_equation(x)

# # 绘制曲线
# plt.plot(x, y)

# # 添加标题和坐标轴标签
# plt.title("Quadratic Curve")
# plt.xlabel("x")
# plt.ylabel("y")

# # 显示图形
# plt.show()

from manim import *

m = 1
f = 1
P = 1

def equationOnLeft(t, v):
    return m * f ** 2 / P * t

def equationOnRight(t, v):
    return -f / P * v - np.log(1 - f / P * v)


class DrawEquation(Scene):
    

    def construct(self):

        grid = ComplexPlane().add_coordinates()

        delta_x = 0.01
        delta_y = 0.00001
        delta_y2 = 0.01
        x_range = np.arange(0, 7.5, delta_x)
        y_range = np.arange(-0.01, 1, delta_y)
        delta = 0.01
        
        self.play(FadeIn(grid))
        
        y = 0
        # for x in x_range:
        #     while (abs(equationOnLeft(x, y) - equationOnRight(x, y)) > delta and y < 10):
        #         y += 0.001
        #     dot = Dot(grid.n2p(x + y * 1j))
        #     self.add(dot)
            

        for x in x_range: 
            if (abs(x) > 0.01):
                y_range = np.arange(max(0, -np.exp(-x) + 1), 1, delta_y)
            # if (x > 0.5): y_range = np.arange(0.5, 1, delta_y)
            # if (x > 1): y_range = np.arange(0.75, 1, delta_y)
            # if (x > 2): y_range = np.arange(0.85, 1, delta_y)
            for y in y_range:
                if (abs(equationOnLeft(x, y) - equationOnRight(x, y)) < delta):
                    dot = Dot(grid.n2p(x + y * 1j), radius=0.02, color=RED)
                    self.add(dot)
                    # y_range = (y - delta_y *200, 1, delta_y)
                    # print(y)
                    break


        self.wait()