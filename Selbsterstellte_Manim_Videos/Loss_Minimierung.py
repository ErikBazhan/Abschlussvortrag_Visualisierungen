from manim import *

config.background_color = WHITE
Tex.set_default(color=BLACK)
MathTex.set_default(color=BLACK)
Text.set_default(color=BLACK)
Paragraph.set_default(color=BLACK)
Rectangle.set_default(color=BLACK)
Arrow.set_default(color=BLACK)
Line.set_default(color=BLACK)
Dot.set_default(color=BLACK)

class StartingPoint(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        text=MathTex("L_k (w_k) = f(x) = \\sum_{n=1}^{5} \\frac{1}{n} \\cdot \\sin(n x)")
        self.play(Write(text))
        self.wait(1)
        self.play(text.animate.scale(0.7).shift(UP*2.5))
        self.wait(1)

        ax = Axes(
            x_range=[0, 10], y_range=[0, 100, 10], axis_config={"include_tip": False}
        )
        labels = ax.get_axis_labels(x_label="x", y_label="f(x)")

        t = ValueTracker(0)

        self.play(Create(ax), Create(labels))
        self.wait(1)

        def func(x):
            return  10 * sum((1/n) * np.sin(n * x) for n in range(1, 6)) + 30
        graph = ax.plot(func, color=MAROON)

        initial_point = [ax.coords_to_point(t.get_value(), func(t.get_value()))]
        dot = Dot(point=initial_point)

        self.play(Create(graph), Create(dot))
        self.wait(1)

        text1=MathTex(r"w_k \rightarrow w_{k+1} = w_k - \alpha \cdot \frac{\partial L_k}{\partial w_k}")
        self.play(Write(text1))
        self.wait(0.5)
        self.play(text1.animate.scale(0.7).shift(UP*1.5))
        self.wait(0.5)

        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), func(t.get_value()))))
        x_space = np.linspace(*ax.x_range[:2],200)
        minimum_index = func(x_space).argmin()

        self.add(graph, dot)
        self.wait(1)
        self.play(t.animate.set_value(x_space[minimum_index]), run_time=4)
        self.wait()