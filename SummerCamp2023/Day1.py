# It is for the "Peking University Strong Foundation" in 2023

from manim import *

def sin(x): return np.sin(x)
def cos(x): return np.cos(x)

class P2(Scene):

    def construct(self):
        
        def f(x):
            return 1 + cos(x) + 1j * sin(x) - cos(2 * x) - 1j * sin(2 * x) + cos(3 * x) + 1j * sin(3 * x)
        grid = ComplexPlane().add_coordinates()

        self.play(FadeIn(grid))

        func = ParametricFunction(
            lambda x : np.array([
                1 + cos(x) - cos(2 * x) + cos(3 * x),
                sin(x) - sin(2 * x) + sin(3 * x),
                0
            ]), t_range=(0, PI * 2)
        )

        self.play(FadeIn(func))

        for i in range(1, 6):
            dot = Dot(grid.n2p(f(i)))    
            self.play(FadeIn(dot))
            self.play(FadeOut(dot))


        self.wait()

class P5(Scene):
    def construct(self):
        t = 2
        grid = NumberPlane(
            x_range=(-PI, PI, PI / 2)
        ).scale(t, about_point = ORIGIN)

        def f(x): return max(sin(x), cos(x), -1 / PI * x + 1)
        r = (0, PI)

        self.play(FadeIn(grid))
        self.play(Write(FunctionGraph(lambda x : sin(x), x_range=r, color = RED).scale(t, about_point = ORIGIN)))
        self.play(Write(FunctionGraph(lambda x : cos(x), x_range=r, color = BLUE).scale(t, about_point = ORIGIN)))
        self.play(Write(FunctionGraph(lambda x : -1 / PI * x + 1, x_range=r, color = GREEN).scale(t, about_point = ORIGIN)))
        self.play(Write(FunctionGraph(f, x_range=r).scale(t, about_point = ORIGIN)))

        self.wait()