from manim import *

# class Begin(Scene):
#     def construct(self):
        
        # print(FRAME_HEIGHT) # the height of the screen is 8 
        # print(FRAME_WIDTH)  # FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / DEFAULT_PIXEL_HEIGHT
        # print(ORIGIN)       # ORIGIN => np.array([0, 0, 0])

        # print(RIGHT, UP, LEFT, DOWN)
        # print(UR, UL, DR, DL)
        # print(TOP, BOTTOM, RIGHT_SIDE, LEFT_SIDE)
        # print(IN, OUT)


class Move(Scene):
    def construct(self):
        mob = Square()
        self.add(mob)
        # mob.shift(LEFT * 5)
        self.play(mob.animate.shift(LEFT * 5))
        self.play(mob.animate.shift(UP * 2 + RIGHT * 3))
        self.play(mob.animate.shift(DOWN * 2, RIGHT * 2))

        self.play(mob.animate.move_to(LEFT * 5 + UP * 2))

        # aligned_edge : 对齐
        self.play(mob.animate.move_to(LEFT * 3, aligned_edge = LEFT)) 
        self.play(mob.animate.move_to(LEFT * 3, aligned_edge = RIGHT)) 

class Scale(Scene):
    def construct(self):
        mob = Square()
        # self.add(mob)
        self.play(FadeIn(mob))
        self.play(mob.animate.scale(2))
        self.play(mob.animate.scale(0.5))

        # self.play(mob.scale, 2, about_edge = UP)
        # self.play(mob.scale, 0.5, about_edge = DOWN)
        self.play(mob.animate.scale(2, about_edge = UP))
        self.play(mob.animate.scale(2, about_edge = DOWN))
        # self.play(mob.scale, 2, about_point = np.array([-2, -2, 0]))
        # self.play(mob.animate.scale(0.5, abuot_point = ORIGIN))
        # mob.scale()

class ROTATE(Scene):
    def construct(self):
        mob = Square()
        self.play(Write(mob))
        self.play(mob.animate.shift(LEFT * 2))
        self.play(mob.animate.rotate(PI))
        self.play(Rotate(mob, PI, axis = IN), run_time = 0.5)
        self.play(Rotate(mob, PI / 2, about_point = ORIGIN))

class FLIP(Scene):
    def construct(self):
        mob = Triangle()
        mob.color = PINK
        mob.set_fill(PINK, opacity = 0.5)
        self.play(Create(mob))
        self.play(mob.animate.shift(LEFT * 2 + UP))
        self.play(mob.animate.flip())
        self.play(mob.animate.flip(axis = RIGHT))
        self.play(mob.animate.flip(axis = RIGHT, about_point = ORIGIN))
        self.play(mob.animate.flip(axis = UR, about_point = LEFT * 1.5))
        self.play(mob.animate.flip(axis = IN, about_point = LEFT * 1.5))

class STRETCH(Scene):
    def construct(self):
        mob = Circle()
        mob.color = PINK
        mob.set_fill(PINK, opacity = 0.5)
        self.play(Create(mob))

        self.play(mob.animate.stretch(3, dim = 0))
        self.play(mob.animate.stretch(2, dim = 1))

        self.play(mob.animate.stretch(0.25, dim = 1, about_point = DOWN * 4))
        self.play(mob.animate.stretch(factor = 3, dim = 1, about_edge = DOWN))
        self.wait()

class TO_CORNER(Scene):
    def construct(self):
        n = 7
        mobs = [Circle()] * n
        # self.play(Create(mobs[0]))

        for i in range(0, n):
            mobs[i].to_corner(UL, buff = i * 0.5)
            self.play(Write(mobs[i]))
        # self.play(*[Create(i in mobs)])
        for i in range(0, n):
            mobs[i].to_edge(UP, buff = i * 0.5)
            self.play(Write(mobs[i]))
        self.wait()

class ALIGN_TO(Scene):
    def construct(self):
        circle = Circle().move_to(np.array([2, 3, 0]))
        square = Square().move_to(np.array([-2, -1, -0])).scale(2)
        self.play(Create(circle), Create(square))
        # self.play(Create(square))
        # self.play(circle.animate.align_to(square, DOWN))
        self.play(circle.animate.align_to(square, DL))

class NEXT_TO(Scene):
    def construct(self):
        circle = Circle(radius=1)
        square = Square(side_length=1)
        self.play(Create(circle), Create(square))
        self.play(circle.animate.next_to(square))
        self.play(circle.animate.next_to(square, UP))
        self.play(circle.animate.next_to(square, aligned_edge = DOWN))
        self.play(circle.animate.next_to(square, aligned_edge = ORIGIN))
        self.play(circle.animate.next_to(square, aligned_edge = UP, buff = 4))

# class VGROUP_NEXT_TO(Scene):
#     def construct(self):
#         A = VGroup(Circle(), Circle(), Circle(), Circle(), Circle())
#         B = VGroup(Square(), Square(), Square())
#         self.play(Create(A))
#         self.play(Create(B))

class SET_HEIGHT_AND_WWIDTH(Scene):
    def construct(self):
        mob = Square()
        self.play(Create(mob))
        self.play(mob.animate.set_height(7))
        self.play(mob.animate.set_width(6))
        # mob.set_height(4, stretch = True)
        # self.play(mob.animate.set_height(7, STRETCH(True)))
        self.play(mob.animate.set_width(6))
        self.wait()
        


class LINE(Scene):
    def construct(self):
        line = Line(np.array([-4, -3, 0]), np.array([0, 3, 0]))
        line2 = Line(np.array([-4, -3, 0]), np.array([0, 4, 0]), buff = 1, stroke_width = 30)
        self.play(Create(line), Create(line2))
        self.play(line2.animate.put_start_and_end_on(np.array([-2, 2, 0]), np.array([0, -2, 0])))
        self.play(line2.animate.scale(2))

        line3 = DashedLine()
        self.play(Create(line3))

        line4 = Line(np.array([-2, 2, 0]), np.array([0, -3, 0]), path_arc = PI * 1.5)
        self.play(Create(line4))

class ARROW(Scene):
    def construct(self):
        vec = Arrow(buff = 0, tip_length = 0.2)
        self.play(Create(vec))
        vec2 = Vector(LEFT + UP * 2)
        self.play(Create(vec2))

        vec3 = DoubleArrow(UP * 3, UP * 2 + RIGHT * 4)
        self.play(Create(vec3))

        cir = Circle()
        line = TangentLine(cir, alpha = 0.4, length = 5)
        self.play(Create(cir), Create(line))

class ARC(Scene):
    def construct(self):
        arc = Arc(
            # arc_center = LEFT * 1,
            radius = 2,
            stroke_width = 10,
            # start_angle = PI / 6,
            angle = PI * 10,
            color = BLUE
        )
        # self.add(arc)
        self.play(Write(arc), run_time = 1)

        self.wait()

class IMG(Scene):
    def construct(self):
        img = ImageMobject(
            "logo.png"
        )
        # self.add(img)
        self.play(FadeIn(img))
        self.play(img.animate.shift(LEFT * 3))
        self.play(FadeOut(img))

class TEXT(Scene):
    def construct(self):
        text = Text("This is a text", color = BLUE, background_stroke_color = RED)
        self.play(FadeIn(text))
        # self.wait(2)
        self.play(text.animate.shift(UP * 2))
        
        t2 = Tex("\\LaTeX\\\\a")
        self.play(Create(t2))
        self.play(t2.animate.shift(DOWN * 2))

        t = Tex("abc", "de")
        # self.play(Create(t[1][0]))
        self.play(Create(t))

        self.play(t[0].animate.shift(DOWN))

        # print(t[0])


        self.wait()

class TEX(Scene):
    def construct(self):
        t = MathTex("\\sum^n_{i=1}i^3=?\\\\dsfdf").scale(2)
        self.play(Create(t))

        t2 = Text("abc\n", font = "Consolas")
        self.play(FadeIn(t2))

        
        self.wait()
        

class NUMBERLINE(Scene):
    def construct(self):
        axis = NumberLine(
            (-3, 4, 0.5),
            # include_ticks = False,   # 刻度
            include_tip=True,
            # include_numbers=True,
            unit_size=1.5,
            label_direction=UP
        )
        axis.add_numbers({-1, 2})
        self.play(FadeIn(axis))

        dot = Dot(axis.n2p(3))
        self.play(FadeIn(dot))
        # print(axis.p2n(dot))

        self.wait()

class AXES(Scene):
    def construct(self):
        axes = Axes(
            (-8, 4), (-2, 3),
            # lines_center_point = ORIGIN,
            axis_config = {
                "include_numbers": True,
            },
            # x_length = 2,
            # unit_size = 2,
        )


        self.play(FadeIn(axes))

        self.wait()

class NUMBERPLANE(Scene):
    def construct(self):
        grid = NumberPlane(
            axis_config = {
                "stroke_color": RED,
            },
        ).add_coordinates()

        self.play(FadeIn(grid))
        # self.play(grid.animate.apply_function(
        #     lambda p : p + RIGHT * p[1]
        # ))

        grid.prepare_for_nonlinear_transform()
        self.play(grid.animate.apply_function(
            lambda p : p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0
            ])
        ))

        self.wait()

class COMPLEXPLANE(Scene):
    def construct(self):
        grid = ComplexPlane().add_coordinates()
        # dot = Dot(grid.n2p(-3+2j))
        dot = Dot(grid.n2p(2 * np.exp(1j * PI / 4)))

        self.play(FadeIn(grid), FadeIn(dot))
        grid.prepare_for_nonlinear_transform()

        # self.play(grid.animate.apply_complex_function(
        #     lambda z : np.exp(z)
        # ))

        self.wait()

class PARAMETRICFUNCTION(Scene):
    def construct(self):
        func = ParametricFunction(
            lambda t : np.array([
                2 * np.sin(3 * t) * np.cos(t),
                2 * np.sin(3 * t) * np.sin(t),
                0
            ]),
            t_range=(0, 2 * PI)
            
        )
        self.play(Write(func))

        self.wait()

class FUNCTIONGRAPH(Scene):
    def construct(self):
        func = FunctionGraph(
            lambda x : x ** 2
        )

        self.play(FadeIn(func))

        self.wait()

