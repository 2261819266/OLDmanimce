from manim import *

# class Begin(Scene) :
#     def construct(self):
#         print(FRAME_HEIGHT) # the height of the screen is 8 
#         print(FRAME_WIDTH)  # FRAME_WIDTH = FRAME_HEIGHT * DEFAULT_PIXEL_WIDTH / DEFAULT_PIXEL_HEIGHT
#         print(ORIGIN)       # ORIGIN => np.array([0, 0, 0])

#         print(RIGHT, UP, LEFT, DOWN)
#         print(UR, UL, DR, DL)
#         print(TOP, BOTTOM, RIGHT_SIDE, LEFT_SIDE)
#         print(IN, OUT)


# class Move(Scene) :
#     def construct(self):
#         mob = Square()
#         self.add(mob)
#         # mob.shift(LEFT * 5)
#         self.play(mob.shift, LEFT * 5)
#         self.play(mob.shift, UP * 2 + RIGHT * 3)
#         self.play(mob.shift, DOWN * 2, RIGHT * 2)

#         self.play(mob.move_to, LEFT * 5 + UP * 2)

#         # aligned_edge : 对齐
#         self.play(mob.move_to, LEFT * 3, aligned_edge = LEFT) 
#         self.play(mob.move_to, LEFT * 3, aligned_edge = RIGHT) 

class Scale(Scene) :
    def construct(self):
        mob = Square()
        # self.add(mob)
        self.play(FadeIn(mob))
        self.play(mob.scale, 2)
        self.play(mob.scale, 0.5)

        mob.scale(2, about_edge = UP)
        # self.play(mob.scale, 2, about_edge = UP)
        # self.play(mob.scale, 0.5, about_edge = DOWN)
        self.play(mob.animate.scale(0.5, about_edge = DOWN))
        self.play(mob.scale, 2, about_point = np.array([-2, -2, 0]))

