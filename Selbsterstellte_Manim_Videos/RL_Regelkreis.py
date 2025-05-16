from manim import *

#Config for white background:
config.background_color = WHITE
Tex.set_default(color=BLACK)
MathTex.set_default(color=BLACK)
Text.set_default(color=BLACK)
Paragraph.set_default(color=BLACK)
def Arrow2(left, right, buff=0.0, color=BLACK):
    return Arrow(left, right, buff=buff, color=color)
Rectangle.set_default(color = BLACK)
Arrow.set_default(color = BLACK)
Line.set_default(color = BLACK)


class StartingPoint(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)


    def construct(self):
        
        agent = Rectangle(width=2, height=1)
        pt1 = agent.copy()
        
        
        agent.move_to([-2, 2.5, 0])
        self.play(GrowFromPoint(agent, ORIGIN))
        self.wait(0.5)
        agent_text = MathTex(r"\text{RL-Agent}").move_to(agent.get_center()).scale(0.7)
        self.play(Write(agent_text))
        
        
        pt1.next_to(agent, RIGHT*10)
        self.play(GrowFromPoint(pt1, ORIGIN))
        self.wait(0.5)
        pt1_text = MathTex(r"\text{Umgebung}").move_to(pt1.get_center()).scale(0.7)
        self.play(Write(pt1_text))

        arrow2 = Line(agent.get_right(), pt1.get_left()).add_tip(tip_width=0.3, tip_length=0.3)
        aktion_text = MathTex(r"a_k \in A").next_to(arrow2.get_top(), UP)
        self.play(Write(aktion_text))
        self.wait(0.5)
        self.play(Create(arrow2))
        self.wait(0.5)
        self.play(FadeToColor(arrow2, "#c82424", run_time = 0.5))
        self.play(FadeToColor(arrow2, BLACK, run_time = 0.5))

        arrow3_line1 = Line(pt1.get_bottom(), pt1.get_bottom() + DOWN*3)
        arrow3_line2 = Line(arrow3_line1.get_end(), agent.get_bottom() + DOWN*3)
        env_zustand_text = MathTex(r"s_k \in S").next_to(arrow3_line2.get_top(), UP)
        self.play(Write(env_zustand_text))
        env_belohnung_text = MathTex(r"r_k \in R").next_to(arrow3_line2.get_top(), DOWN)
        self.play(Write(env_belohnung_text))
        arrow3_line3 = Line(arrow3_line2.get_end(), agent.get_bottom()).add_tip(tip_width=0.3, tip_length=0.3)
        self.wait(0.5)
        
        self.play(Create(arrow3_line1))
        self.play(Create(arrow3_line2))
        self.play(Create(arrow3_line3))

        
        arrowgroup = Group(arrow3_line1, arrow3_line2, arrow3_line3)

        self.play(FadeToColor(arrowgroup, "#c82424", run_time = 0.5))
        self.play(FadeToColor(arrowgroup, BLACK, run_time = 0.5))

        n = 2
        for i in range(n):
            aktion_text_it = MathTex(f"a_{{k+{i+1}}} \in A").move_to(aktion_text.get_center())
            env_zustand_it = MathTex(f"s_{{k+{i+1}}} \in S").move_to(env_zustand_text.get_center())
            env_belohnung_it = MathTex(f"r_{{k+{i+1}}} \in R").move_to(env_belohnung_text.get_center())
            self.play(Transform(aktion_text, aktion_text_it))
            self.play(FadeToColor(arrow2, "#c82424", run_time = 0.5))
            self.play(FadeToColor(arrow2, BLACK, run_time = 0.5))
            self.play(Transform(env_zustand_text, env_zustand_it), Transform(env_belohnung_text, env_belohnung_it))
            self.play(FadeToColor(arrowgroup, "#c82424", run_time = 0.5))
            self.play(FadeToColor(arrowgroup, BLACK, run_time = 0.5))
            self.wait(0.5)





    