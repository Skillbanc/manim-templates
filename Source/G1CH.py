# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla
import json
from manim import *
from numpy import size
from AbstractAnim import AbstractAnim
from manim import MarkupText
import cvo
import numpy as np

class Algebra(AbstractAnim):
    def construct(self):
        title = Text("Geeta's Pencil Packets", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP))
        self.wait(1)

        # Create larger packets
        packets = VGroup(*[Rectangle(height=3, width=2.5, fill_opacity=0.5, fill_color=BLUE) for _ in range(3)])
        packets.arrange(RIGHT, buff=0.8)
        packets.next_to(title, DOWN, buff=0.8)

        # Label packets
        labels = VGroup(*[Text(f"Packet {i+1}", font_size=28).next_to(packet, UP) for i, packet in enumerate(packets)])

        self.play(Create(packets), Write(labels))
        self.wait(1)

        # Create larger pencils
        pencil = Rectangle(height=0.5, width=0.1, fill_opacity=1, fill_color=YELLOW, stroke_color=DARK_BROWN)
        pencil_tip = Triangle(fill_color=DARK_BROWN, fill_opacity=1).scale(0.1).rotate(PI).next_to(pencil, DOWN, buff=0)
        pencil_group = VGroup(pencil, pencil_tip)

        # Function to create and arrange pencils in a packet
        def create_pencils_in_packet(packet):
            pencils = VGroup(*[pencil_group.copy() for _ in range(15)])
            
            # Calculate the available space in the packet
            packet_width = packet.width * 0.9
            packet_height = packet.height * 0.9
            
            # Arrange pencils in a 3x5 grid (3 rows, 5 columns)
            rows, cols = 3, 5
            x_spacing = packet_width / cols
            y_spacing = packet_height / rows
            
            for i, pencil in enumerate(pencils):
                row = i // cols
                col = i % cols
                x = packet.get_left()[0] + (col + 0.5) * x_spacing
                y = packet.get_bottom()[1] + (row + 0.5) * y_spacing
                pencil.move_to(np.array([x, y, 0]))
            
            return pencils

        # Show pencils in each packet
        all_pencils = VGroup()
        for i, packet in enumerate(packets):
            pencils = create_pencils_in_packet(packet)
            all_pencils.add(pencils)
            self.play(FadeIn(pencils), run_time=1)
            count = Text(f"15 pencils", font_size=24).next_to(packet, DOWN)
            self.play(Write(count))
            self.wait(2)

        # Show multiplication
        equation = MathTex("15 + 15 + 15", "=", "15 ","*"," 3 = 45") 
        equation.scale(1)
        equation.next_to(packets, DOWN, buff=1.2)
        self.play(Write(equation))
        self.wait(1)

        # Final answer
        answer = Text("There are 45 pencils in total!", font_size=30, color=YELLOW)
        answer.next_to(equation, DOWN, buff=0.7)
        self.play(Write(answer))
        self.wait(2)

if __name__ == "__main__":
    scene = Algebra()
    scene.render()
