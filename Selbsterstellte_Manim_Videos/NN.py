from manim import *
import random


config.background_color = WHITE
Tex.set_default(color=BLACK)
MathTex.set_default(color=BLACK)
Text.set_default(color=BLACK)
Paragraph.set_default(color=BLACK)
Rectangle.set_default(color=BLACK)
Arrow.set_default(color=BLACK)
Line.set_default(color=BLACK)

def Arrow2(left, right, buff=0.0, color=BLACK):
    return Arrow(left, right, buff=buff, color=color)


class StartingPoint(MovingCameraScene):
    def setup(self):
        MovingCameraScene.setup(self)

    def construct(self):
        layer_sizes = [5, 4, 3, 2]  
        layers = []
        neuronen_liste = []

        x_offset = LEFT * 1.5
        horizontal_spacing = 1.2

        input_layer = VGroup()
        output_layer = VGroup()

        
        for j in range(layer_sizes[0]):
            neuron = Circle(radius=0.2, color=BLUE, fill_opacity=0).set_fill(BLUE, opacity=0)
            y_pos = UP * (layer_sizes[0] - 1 - 2 * j) * 0.5
            neuron.move_to(RIGHT * 0 + y_pos + x_offset) 
            input_layer.add(neuron)
            neuronen_liste.append(neuron)

        
        self.play(*[FadeIn(neuron) for neuron in input_layer], run_time=0.5)
        layers.append(input_layer)

        
        for i, size in enumerate(layer_sizes[1:], start=1):
            layer = VGroup()
            for j in range(size):
                neuron = Circle(radius=0.2, color=BLUE, fill_opacity=0).set_fill(BLUE, opacity=0)
                y_pos = UP * (size - 1 - 2 * j) * 0.5
                neuron.move_to(RIGHT * i * horizontal_spacing + y_pos + x_offset) 
                layer.add(neuron)
                neuronen_liste.append(neuron)

            if i == len(layer_sizes) - 1:
                output_layer = layer

            layers.append(layer)
            self.play(*[FadeIn(neuron) for neuron in layer], run_time=0.3)

        
        for l in range(len(layers) - 1):
            for n1 in layers[l]:
                for n2 in layers[l + 1]:
                    line = Line(n1.get_center(), n2.get_center(), stroke_width=1)
                    self.play(Create(line), run_time=0.05)
        self.wait(1)


        
        rechteck = Rectangle(width=2, height=layer_sizes[0] * 0.5 + 0.3, color=BLACK)
        rechteck.next_to(input_layer, LEFT, buff=2.5)

        
        label = Text("Replay Buffer", font_size=24).next_to(rechteck, UP, buff=0.2)

        
        self.play(Create(rechteck), Write(label), run_time=0.5)
        self.wait(1)
                    
        
        vector_entries = [MathTex(f"o_{{{i}}}") for i in range(layer_sizes[0])]
        for i, entry in enumerate(vector_entries):
            entry.move_to(input_layer[i].get_center() + LEFT * 2)

        vektor_spalte = VGroup(*vector_entries)

        linke_linie = Line(
            start=vektor_spalte.get_top(),
            end=vektor_spalte.get_bottom(),
            color=BLACK,
            stroke_width=2
        )
        rechte_linie = linke_linie.copy().next_to(vektor_spalte, RIGHT * 0.5, buff=0.3)
        linke_linie.next_to(vektor_spalte, LEFT * 0.5, buff=0.3)

        self.play(
            *[GrowFromPoint(entry, rechteck.get_center()) for entry in vector_entries],
            Create(linke_linie),
            Create(rechte_linie)
        )
        self.wait(1)

        observation_arrows = VGroup()

        for o_entry, neuron in zip(vector_entries, input_layer):
            arrow = Arrow2(o_entry.get_right() + RIGHT*0.1, neuron.get_left(), buff=0.1)
            observation_arrows.add(arrow)

        self.play(*[Create(arrow) for arrow in observation_arrows], run_time=0.5)
        self.wait(0.5)

        
        for _ in range(10):
            animations = []
            for neuron in neuronen_liste:
                neue_opazität = random.uniform(0.05, 1.0)
                animations.append(neuron.animate.set_fill(opacity=neue_opazität))
            self.play(*animations, run_time=0.3)

        self.play(
        FadeOut(rechteck),
        FadeOut(label),
        FadeOut(vektor_spalte),
        FadeOut(observation_arrows),
        FadeOut(rechte_linie),
        FadeOut(linke_linie),
        )

        
        output_entries = [MathTex(f"a_{{{i}}}") for i in range(layer_sizes[-1])]
        for i, entry in enumerate(output_entries):
            entry.move_to(output_layer[i].get_center() + RIGHT * 2)

        output_vector = VGroup(*output_entries)
        output_line_left = Line(
            start=output_vector.get_top(),
            end=output_vector.get_bottom(),
            color=BLACK,
            stroke_width=2
        )
        output_line_right = output_line_left.copy().next_to(output_vector, RIGHT * 0.5, buff=0.3)
        output_line_left.next_to(output_vector, LEFT * 0.5, buff=0.3)

        self.play(
            *[Write(entry) for entry in output_entries],
            Create(output_line_left),
            Create(output_line_right)
        )
        self.wait(1)

        action_arrows = VGroup()

        for neuron, a_entry in zip(output_layer, output_entries):
            arrow = Arrow2(neuron.get_right(), a_entry.get_left() + LEFT*0.1, buff=0.1)
            action_arrows.add(arrow)

        self.play(*[Create(arrow) for arrow in action_arrows], run_time=0.5)
        self.wait(1)

        self.play(neuronen_liste[12].animate.set_fill(opacity=1), run_time=0.5)
        self.play(neuronen_liste[13].animate.set_fill(opacity=0.1), run_time=0.5)
        self.play(action_arrows[0].animate.set_color("#c82424"), output_entries[0].animate.set_color("#c82424"), run_time=1)
        self.play(action_arrows[0].animate.set_color(BLACK), output_entries[0].animate.set_color(BLACK), run_time=1)
        self.wait(1)
    
        self.play(neuronen_liste[12].animate.set_fill(opacity=0.1), run_time=0.5)
        self.play(neuronen_liste[13].animate.set_fill(opacity=1), run_time=0.5)    
        self.play(action_arrows[1].animate.set_color("#c82424"), output_entries[1].animate.set_color("#c82424"), run_time=1)
        self.play(action_arrows[1].animate.set_color(BLACK), output_entries[1].animate.set_color(BLACK), run_time=1)
        self.wait(1)
        

