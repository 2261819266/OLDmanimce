# from manimlib.imports import *

# class WriteText(Scene) :
#     def construct(self):
#         text = TextMobject("A Text")
#         text.to_edge(UP)
#         text.move_to(1 * UP + 0.1 * RIGHT)
#         self.play(text)
#         return super().construct()
from manimlib.imports import *

# class SquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()
#         square = Square()
#         square.flip(UP)
#         square.rotate(-3 * TAU / 16)
#         circle.set_fill(PINK, opacity=0.5)

#         self.play(ShowCreation(square))
#         square.shift(UP * 3)
#         self.play(ShowCreation(circle))
#         circle.move_to(square)
#         square.move_to(0)
#         # self.play(Transform(square, circle))
#         square.scale(-2)
#         self.play(rotate(ORIGIN, 0.5 * PI))
#         self.play(FadeOut(square))
#         self.wait(2)

class RotateObject(Scene):
    def construct(self):
        textM = TextMobject("Text")
        textC = TextMobject("Reference text")
        textM.shift(UP)
        textM.rotate(PI/4) 
        self.play(Write(textM), Write(textC))
        self.wait(2)
        
class concurrent(Scene):
    def construct(self):
        dot1 = Dot()
        dot2 = Dot()
        dot2.shift(UP)
        dot3 = Dot()
        dot3.shift(DOWN)
 
        # 单个动画的演示
        self.play(Write(dot1))
        # 多个动画演示
        self.play(*[
            Transform(i.copy(), j) for i, j in zip([dot1, dot1], [dot2, dot3])
        ]) # 故意使用i,j是为了显示zip的使用

        self.wait()


class ChangeColorAndSizeAnimation(Scene):
    def construct(self):
        text = TextMobject("Text")
        text.scale(2)
        text.shift(LEFT*2)
        self.play(Write(text))
        self.wait()
        self.play(
            text.shift, RIGHT*2,
            text.scale, 2,
            text.set_color, RED_A,
            run_time=2
        )
        self.wait()