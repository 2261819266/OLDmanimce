from manim import *
from sympy import imageset

class IMAGES(Scene):
    def construct(self):
        image_path = "image.png"
        image = imageset(image_path)

        # self.add(image)