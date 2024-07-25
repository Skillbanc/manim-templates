# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from manim import *
from numpy import size
from AbstractAnim import AbstractAnim

import cvo


class testing2(AbstractAnim):
    def construct(self):
        self.Bisect()

    def Bisect(self):
      

      title = Text("CONSTRUCTION TO BISECT A GIVEN ANGLE",font_size= 36,color = ORANGE).to_edge(UP)
      self.play(Write(title))
      self.wait(3)
        # Step text configurations with smaller font size
      step1_text = Text("Step 1:  With O as centre and any convenient radius, draw\n\n an arc  PQ cutting OM and ON at P and Q respectively .",color = WHITE).scale(0.7).to_edge(DOWN*1.75)
      # self.play(Write(step1_text))
      # self.wait(5)
      


      line_l = Line(LEFT *0.38+DOWN*1 , RIGHT * 4+DOWN*1)
      self.play(Create(line_l))
      O = Dot(LEFT *0.38+DOWN*1)
      self.play(Create(O))
           
        # Label points
      O_label = MathTex("O",color = BLUE).next_to(LEFT *0.38+DOWN*1, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(O_label))
      self.wait(0.5)

      N = Dot(LEFT *-2.5+DOWN*1)
      self.play(Create(N))
      self.wait(0.4)
           
        # Label points
      N_label = MathTex("N",color = BLUE).next_to(LEFT *-2.5+DOWN*1, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(N_label))
      self.wait(0.7)

      angle_degrees = 60
      angle_radians = angle_degrees* DEGREES
      angle_line = Line( ORIGIN,2 * RIGHT).rotate(angle_radians).shift(DOWN*1+LEFT*0.47+UP*1.5).set_length(3.5)
      self.play(Create(angle_line))
      self.wait(1)


      M = Dot(DOWN*1+LEFT*-1.3+UP*2.8)
      self.play(Create(M))
      self.wait(0.5)
           
        # Label points
      M_label = MathTex("M",color = BLUE).next_to(DOWN*1+LEFT*-1.3+UP*2.8, UP)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(M_label))
      self.wait(1.5)
      # self.play(FadeOut(step1_text))



 # Compass arcs

      
      step2_text = Text("Step 2: With P as centre and any radius slightly more than half\n\n of the length of PQ, draw an arc in the interior of the given angle.",color = PINK).scale(0.7).to_edge(DOWN*1.75)
      self.play(Write(step1_text))
      self.wait(5)
      

  # Compass arcs
      arc1 = Arc(radius=3.7, angle=PI/4, arc_center=LEFT *2+DOWN*1)
        
      arc1.set_color(YELLOW)
    
        
      self.play(Create(arc1))
      self.wait(1)
        

      Q = Dot(LEFT *-1.7+DOWN*1)
      self.play(Create(Q))
      self.wait(0.5)
           
        # Label points
      Q_label = MathTex("Q",color = BLUE).next_to(LEFT *-1.7+DOWN*1, DOWN)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(Q_label))
      

      P = Dot(DOWN*1+LEFT*-0.94+UP*2.2)
      self.play(Create(P))
      self.wait(0.6)
           
        # Label points
      P_label = MathTex("P",color = BLUE).next_to(DOWN*1+LEFT*-0.94+UP*2.2, UP+LEFT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(P_label))
      self.wait(1.7)
      self.play(FadeOut(step1_text))
      


      step3_text = Text("Step 3: With Q as centre and without altering radius \n\n (as in step 2) draw another arc in the interior of ∠MON.",color = WHITE).scale(0.7).to_edge(DOWN*1.75)
      self.play(Write(step2_text))
      self.wait(4.5)
      


  # Compass arcs
      arc2 = Arc(radius=3, angle=PI/7, arc_center=LEFT *0.5+DOWN*1+UP*1)
        
      arc2.set_color(YELLOW)
    
      self.play(Create(arc2))
      self.wait(1)
      self.play(FadeOut(step2_text))
        
    
      self.play(Write(step3_text))
      self.wait(4)
 # Compass arcs
      arc3 = Arc(radius=3, angle=PI/7, arc_center=LEFT *0.5+DOWN*1+UP*1).rotate(70)
        
      arc3.set_color(YELLOW)
    
      self.play(Create(arc3))
      self.wait(1)
      self.play(FadeOut(step3_text))
        

      z = Dot(LEFT *-2.39+DOWN*1.05+UP*1.68)
      self.play(Create(z))
      self.play(FadeOut(step3_text))
      he = Text("Met the two arcs intersect at Z.",color=PINK).to_edge(DOWN).scale(0.8)
      self.play(Write(he))
        # Label points
      z_label = MathTex("Z",color = BLUE).next_to(LEFT *-2.39+DOWN*1.05+UP*1.68, UP+RIGHT)
      #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
      self.play(Write(z_label))
    #   he = Text("Let the two arcs intersect at Z.",color=PINK).to_edge(DOWN).scale(0.8)
    #   self.play(Write(he))
      self.play(Unwrite(arc1))
      self.wait(1.4)
      self.play(Unwrite(he))
      
      step4_text = Text("Step 4: Draw ray OZ. Then OZ is the desired bisector of ∠MON..\n\nObserve ∠MOZ = ∠ZON.",color = WHITE).scale(0.7).to_edge(DOWN*1.75)
      self.play(Write(step4_text))
      self.wait(3)
      

      angle_degrees = 30
      angle_radians = angle_degrees* DEGREES
      angle_line = DashedLine( ORIGIN,3.47 * RIGHT).rotate(angle_radians).shift(DOWN*1.55+LEFT*0.47+UP*1.5).set_length(3.7)
      self.play(Create(angle_line))
      self.wait(3)
      self.play(FadeOut(step4_text))
#self.play(Write(angle_label))








    # def constdilation(self):
    #     a = Text("Dialtion Construction ",font_size=37,color=PINK).to_edge(UP)
    #     self.play(Write(a))
    #     self.wait(1.8)
   

    #     # Create the original triangle
    #     triangle = Polygon([-3, -2, 0], [1, -2, 0], [-1, 1, 0], color=BLUE)
        
    #     # Create the center of dilation
    #     center = Dot([4, -1, 0], color=RED)
    #     center_label = Text("C", font_size=28,color = ORANGE).next_to(center, DOWN)
        
    #     # Create labels for the original triangle
    #     labels = VGroup(
    #         Text("P", font_size=24,color = BLUE).next_to(triangle.get_vertices()[0], DOWN+LEFT),
    #         Text("Q", font_size=24,color = BLUE).next_to(triangle.get_vertices()[1], DOWN+RIGHT),
    #         Text("R", font_size=24,color = BLUE).next_to(triangle.get_vertices()[2], UP),
    #     )
    #     lab = VGroup(
    #         Dot(color = BLUE).move_to(triangle.get_vertices()[0]),
    #         Dot(color = BLUE).move_to(triangle.get_vertices()[1]),
    #         Dot(color = BLUE).move_to(triangle.get_vertices()[2]),

    #     )

    #     # Create a text box for step descriptions
    #     description = Text("", font_size=24).to_edge(UP)

    #     # Step 1: Draw the original triangle and center
    #     self.play(

         
    #         Write(description.become(Text("Step 1: Draw a  triangle PQR and choose the center of dilation C \nwhich is not on the triangle. ", font_size=29,color = YELLOW).to_edge(DOWN))),
                   
    #     )
    #     self.wait(5)
    #     self.play( Create(triangle), Create(center),Create(lab), Write(center_label), Write(labels))
    #     self.wait(3)

    #     # Step 2: Draw lines from center to vertices
    #     lines = VGroup(*[DashedLine(center.get_center(), vertex) for vertex in triangle.get_vertices()])
    #     self.play(
            
    #         description.animate.become(Text("Step 2: Draw lines from C to P, Q, and R", font_size=29,color = YELLOW).to_edge(DOWN))
    #     )
    #     self.wait(3)
    #     self.play(Create(lines))
    #     self.wait(2)

    #     # Step 3: Extend the lines
    #     extended_lines = VGroup(*[
    #         DashedLine(center.get_center(), vertex + 1.5*(vertex - center.get_center()))
    #         for vertex in triangle.get_vertices()
    #     ])
    #     self.play(
            
    #         description.animate.become(Text("Step 3: Extend the lines from C", font_size=29,color = YELLOW).to_edge(DOWN))
    #     )
    #     self.wait(2.1)
    #     self.play(Transform(lines, extended_lines))
    #     self.wait(3)

    #     # Step 4: Create the dilated triangle
    #     scale_factor = 1.5
    #     dilated_triangle = Polygon(
    #         *[center.get_center() + scale_factor * (vertex - center.get_center())
    #           for vertex in triangle.get_vertices()],
    #         color=GREEN
    #     )
        
    #     # Create labels for the dilated triangle
    #     dilated_labels = VGroup(
    #         Text("P'", font_size=24,color=GREEN).next_to(dilated_triangle.get_vertices()[0], UP+LEFT),
    #         Text("Q'", font_size=24,color=GREEN).next_to(dilated_triangle.get_vertices()[1], UP+RIGHT),
    #         Text("R'", font_size=24,color=GREEN).next_to(dilated_triangle.get_vertices()[2], UP),
    #     )

    #     dot = VGroup(
    #         Dot(color=GREEN).move_to(dilated_triangle.get_vertices()[0]),
    #         Dot(color=GREEN).move_to(dilated_triangle.get_vertices()[1]),
    #         Dot(color=GREEN).move_to(dilated_triangle.get_vertices()[2]),
            
    #     )

        

    #     self.play(
            
    #         description.animate.become(Text("Step 4: By using compasses, Mark\n\n three points P' , Q' and R' \n\non the projections'", font_size=26,color = YELLOW).to_edge(DOWN*9+RIGHT))
    #     )
    #     self.wait(4)
    #     self.play(Create(dot))
    #     self.wait(2)
        
    #     self.play(Write(dilated_labels))
    #     self.wait(3)
    #     b = Text("K = Scale factor",font_size=29,color=PINK).to_edge(RIGHT+DOWN*4)
    #     self.play(Write(b))
    #     self.wait(2)

    #     a = description.animate.become(Text("CP'= k (CP) ",font_size=30,color=YELLOW).to_edge(DOWN+RIGHT*3.5))
    #     self.play(a)
    #     self.wait(4)

    #     # Final step: Show the complete construction
    #     self.play(
    #         description.animate.become(Text("Step 5: Join P'Q', Q'R' and R'P'. So that  P'Q' R' ~  PQR", font_size=29,color = YELLOW).to_edge(DOWN))
    #     )
    #     self.wait(3)
    #     self.play(Create(dilated_triangle))
    #     self.wait(4)










  
#     def Bisect(self):
      

#       title = Text("CONSTRUCTION TO BISECT A GIVEN ANGLE",font_size= 36,color = ORANGE).to_edge(UP)
#       self.play(Write(title))
#       self.wait(3)
#         # Step text configurations with smaller font size
#       step1_text = Text("Step 1:  With O as centre and any convenient radius, draw\n\n an arc  PQ cutting OM and ON at P and Q respectively .",color = WHITE).scale(0.7).to_edge(DOWN*1.75)
#       self.play(Write(step1_text))
#       self.wait(5)
      


#       line_l = Line(LEFT *0.38+DOWN*1 , RIGHT * 4+DOWN*1)
#       self.play(Create(line_l))
#       O = Dot(LEFT *0.38+DOWN*1)
#       self.play(Create(O))
           
#         # Label points
#       O_label = MathTex("O",color = BLUE).next_to(LEFT *0.38+DOWN*1, DOWN)
#       #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
#       self.play(Write(O_label))
#       self.wait(0.5)

#       N = Dot(LEFT *-2.5+DOWN*1)
#       self.play(Create(N))
#       self.wait(0.4)
           
#         # Label points
#       N_label = MathTex("N",color = BLUE).next_to(LEFT *-2.5+DOWN*1, DOWN)
#       #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
#       self.play(Write(N_label))
#       self.wait(0.7)

#       angle_degrees = 60
#       angle_radians = angle_degrees* DEGREES
#       angle_line = Line( ORIGIN,2 * RIGHT).rotate(angle_radians).shift(DOWN*1+LEFT*0.47+UP*1.5).set_length(3.5)
#       self.play(Create(angle_line))
#       self.wait(1)


#       M = Dot(DOWN*1+LEFT*-1.3+UP*2.8)
#       self.play(Create(M))
#       self.wait(0.5)
           
#         # Label points
#       M_label = MathTex("M",color = BLUE).next_to(DOWN*1+LEFT*-1.3+UP*2.8, UP)
#       #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
#       self.play(Write(M_label))
#       self.wait(1.5)
#       self.play(FadeOut(step1_text))



#  # Compass arcs

      
#       step2_text = Text("Step 2: With P as centre and any radius slightly more than half\n\n of the length of PQ, draw an arc in the interior of the given angle.",color = PINK).scale(0.7).to_edge(DOWN*1.75)
#       self.play(Write(step2_text))
#       self.wait(5)
      

#   # Compass arcs
#       arc1 = Arc(radius=3.7, angle=PI/4, arc_center=LEFT *2+DOWN*1)
        
#       arc1.set_color(YELLOW)
    
        
#       self.play(Create(arc1))
#       self.wait(1)
        

#       Q = Dot(LEFT *-1.7+DOWN*1)
#       self.play(Create(Q))
#       self.wait(0.5)
           
#         # Label points
#       Q_label = MathTex("Q",color = BLUE).next_to(LEFT *-1.7+DOWN*1, DOWN)
#       #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
#       self.play(Write(Q_label))
      

#       P = Dot(DOWN*1+LEFT*-0.94+UP*2.2)
#       self.play(Create(P))
#       self.wait(0.6)
           
#         # Label points
#       P_label = MathTex("P",color = BLUE).next_to(DOWN*1+LEFT*-0.94+UP*2.2, UP+LEFT)
#       #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
#       self.play(Write(P_label))
#       self.wait(1.7)
#       self.play(FadeOut(step2_text))
      


#       step3_text = Text("Step 3: With Q as centre and without altering radius \n\n (as in step 2) draw another arc in the interior of ∠MON.",color = WHITE).scale(0.7).to_edge(DOWN*1.75)
#       self.play(Write(step3_text))
#       self.wait(4.5)
      


#   # Compass arcs
#       arc2 = Arc(radius=3, angle=PI/7, arc_center=LEFT *0.5+DOWN*1+UP*1)
        
#       arc2.set_color(YELLOW)
    
#       self.play(Create(arc2))
#       self.wait(1)
        
    

#  # Compass arcs
#       arc3 = Arc(radius=3, angle=PI/7, arc_center=LEFT *0.5+DOWN*1+UP*1).rotate(70)
        
#       arc3.set_color(YELLOW)
    
#       self.play(Create(arc3))
#       self.wait(1)
        

#       z = Dot(LEFT *-2.39+DOWN*1.05+UP*1.68)
#       self.play(Create(z))
#       self.play(FadeOut(step3_text))
#       he = Text("Let the two arcs intersect at Z.",color=PINK).to_edge(DOWN).scale(0.8)
#       self.play(Write(he))
#         # Label points
#       z_label = MathTex("Z",color = BLUE).next_to(LEFT *-2.39+DOWN*1.05+UP*1.68, UP+RIGHT)
#       #  end_label = MathTex("B",color = BLUE).next_to(end_point, DOWN)
#       self.play(Write(z_label))
#     #   he = Text("Let the two arcs intersect at Z.",color=PINK).to_edge(DOWN).scale(0.8)
#     #   self.play(Write(he))
#       self.play(Unwrite(arc1))
#       self.wait(1.4)
#       self.play(Unwrite(he))
      
#       step4_text = Text("Step 4: Draw ray OZ. Then OZ is the desired bisector of ∠MON..\n\nObserve ∠MOZ = ∠ZON.",color = WHITE).scale(0.7).to_edge(DOWN*1.75)
#       self.play(Write(step4_text))
#       self.wait(3)
      

#       angle_degrees = 30
#       angle_radians = angle_degrees* DEGREES
#       angle_line = DashedLine( ORIGIN,3.47 * RIGHT).rotate(angle_radians).shift(DOWN*1.55+LEFT*0.47+UP*1.5).set_length(3.7)
#       self.play(Create(angle_line))
#       self.wait(3)
#       self.play(FadeOut(step4_text))
# #self.play(Write(angle_label))










 
    # def rotationalsymmetry(self):
         
    #     a = Text("Rotational Symmetry", font_size=40, color=YELLOW).to_edge(UP)
    #     self.play(Write(a))
    #     self.wait(2)


    #     specific_condition = Text("Rotational symmetry is a geometric property where an object looks the\n\n same after being rotated by a certain angle around a fixed point.", font_size=30,color=BLUE).to_edge(DOWN*7.5)
    #     self.play( Write(specific_condition))
    #     self.wait(6.7)
    #     self.play(
        
    #     FadeOut(specific_condition),
    #     FadeOut(a)
    #     )
    
    #     self.wait(1)

    #     shapes = [
    #     (Circle(radius=2, color=BLUE), "Circle", "Infinite"),
    #     (Square(side_length=4, color=GREEN), "Square", 4),
    #     (Triangle(color=RED).scale(2), "Triangle", 3),
    #     (Rectangle(width=4, height=2, color=YELLOW), "Rectangle", 2)
    #      ]

    #     for shape, name, symmetries in shapes:
    #        self.show_symmetry(shape, name, symmetries)
    #        self.wait(1)
    #        self.clear()
    # def show_symmetry(self, shape, shape_name, symmetries):
        
    #    # Create the shape
    #  shape.move_to(ORIGIN)

    # # Create a dot at the center
    #  center_dot = Dot(color=WHITE)

    # # Create an arrow to show rotation
    #  arrow = Arrow(start=ORIGIN, end=shape.get_top(), color=ORANGE)

    # # Group the shape and arrow
    #  group = VGroup(shape, arrow)

    # # Add elements to the scene
    #  self.play(Create(group), Create(center_dot))
    #  self.wait(1)

    # # Create and display the shape name
    #  name_text = Text(shape_name, font_size=36).to_edge(UP)
    #  self.play(Write(name_text))


    # # Rotate the shape
    #  if symmetries == "Infinite":
    #     self.play(Rotate(group, angle=2*PI, about_point=ORIGIN), run_time=5)
    #     check_text = Text(" A circle has infinite rotational symmetry around at any angle.", color=GREEN, font_size=29).to_edge(DOWN*1.6)
    #     self.play(Write(check_text))
    #     self.wait(2)
    #  else:
    #     for i in range(symmetries):
    #         self.play(
    #             Rotate(group, angle=2*PI/symmetries, about_point=ORIGIN),
    #             run_time=2
    #         )
    #         angle = 360 / symmetries * (i + 1)
    #         check_text = Text(f" It is similar  at  {angle}°", color=WHITE, font_size=34).to_edge(DOWN*1.6)
    #         self.play(Write(check_text))
    #         self.wait(2)
    #         if i < symmetries - 1:
    #             self.play(FadeOut(check_text))

    #  self.wait(2)

    # # Final message
    #  if symmetries == "Infinite":
    #     final_text = Text("Order of Rotation is Infinite. ", font_size=36).to_edge(DOWN)
    #  else:
    #     self.wait(1.5)
    #     final_text = Text(f"Order of Rotation is {symmetries}. ", font_size=36).to_edge(DOWN)
    
    #  self.play(
      
    #     FadeOut(check_text),
    #     Write(final_text)
    # )
    #  self.wait(3)






    # def constdilation(self):
    #     a = Text("Dialtion Construction ",font_size=37,color=PINK).to_edge(UP)
    #     self.play(Write(a))
    #     self.wait(1.8)
   

    #     # Create the original triangle
    #     triangle = Polygon([-3, -2, 0], [1, -2, 0], [-1, 1, 0], color=BLUE)
        
    #     # Create the center of dilation
    #     center = Dot([4, -1, 0], color=RED)
    #     center_label = Text("C", font_size=28,color = ORANGE).next_to(center, DOWN)
        
    #     # Create labels for the original triangle
    #     labels = VGroup(
    #         Text("P", font_size=24,color = BLUE).next_to(triangle.get_vertices()[0], DOWN+LEFT),
    #         Text("Q", font_size=24,color = BLUE).next_to(triangle.get_vertices()[1], DOWN+RIGHT),
    #         Text("R", font_size=24,color = BLUE).next_to(triangle.get_vertices()[2], UP),
    #     )
        

    #     # Create a text box for step descriptions
    #     description = Text("", font_size=24).to_edge(UP)

    #     # Step 1: Draw the original triangle and center
    #     self.play(

         
    #         Write(description.become(Text("Step 1: Draw a  PQR and choose the center of dilation C which is not on the \ntriangle. ", font_size=25,color = YELLOW).to_edge(DOWN))),
                   
    #     )
    #     self.wait(5)
    #     self.play( Create(triangle), Create(center), Write(center_label), Write(labels))
    #     self.wait(3)

    #     # Step 2: Draw lines from center to vertices
    #     lines = VGroup(*[DashedLine(center.get_center(), vertex) for vertex in triangle.get_vertices()])
    #     self.play(
            
    #         description.animate.become(Text("Step 2: Draw lines from C to P, Q, and R", font_size=29,color = YELLOW).to_edge(DOWN))
    #     )
    #     self.wait(3)
    #     self.play(Create(lines))
    #     self.wait(2)

    #     # Step 3: Extend the lines
    #     extended_lines = VGroup(*[
    #         DashedLine(center.get_center(), vertex + 1.5*(vertex - center.get_center()))
    #         for vertex in triangle.get_vertices()
    #     ])
    #     self.play(
            
    #         description.animate.become(Text("Step 3: Extend the lines from C", font_size=29,color = YELLOW).to_edge(DOWN))
    #     )
    #     self.wait(2.1)
    #     self.play(Transform(lines, extended_lines))
    #     self.wait(3)

    #     # Step 4: Create the dilated triangle
    #     scale_factor = 1.5
    #     dilated_triangle = Polygon(
    #         *[center.get_center() + scale_factor * (vertex - center.get_center())
    #           for vertex in triangle.get_vertices()],
    #         color=GREEN
    #     )
        
    #     # Create labels for the dilated triangle
    #     dilated_labels = VGroup(
    #         Text("P'", font_size=24,color=GREEN).next_to(dilated_triangle.get_vertices()[0], UP+LEFT),
    #         Text("Q'", font_size=24,color=GREEN).next_to(dilated_triangle.get_vertices()[1], UP+RIGHT),
    #         Text("R'", font_size=24,color=GREEN).next_to(dilated_triangle.get_vertices()[2], UP),
    #     )
      


    #     self.play(
            
    #         description.animate.become(Text("Step 4: By using compasses, Mark three points P' , Q' and R' \non the projections'", font_size=26,color = YELLOW).to_edge(DOWN))
    #     )
    #     self.wait(3)
        
    #     self.play(Write(dilated_labels))
    #     self.wait(3)
    #     b = Text("K = Scale factor",font_size=28,color=PINK).to_edge(RIGHT)
    #     self.play(Write(b))
    #     self.wait(2)

    #     a = description.animate.become(Text("CP'= k (CP) = 2 CP \nCQ' = 2 CQ \nCR' = 2 CR",font_size=25,color=YELLOW).to_edge(DOWN+RIGHT*2.5))
    #     self.play(a)
    #     self.wait(3.5)

    #     # Final step: Show the complete construction
    #     self.play(
    #         description.animate.become(Text("Join P'Q', Q'R' and R'P'. So that  P'Q' R' ~  PQR", font_size=29,color = YELLOW).to_edge(DOWN))
    #     )
    #     self.wait(3)
    #     self.play(Create(dilated_triangle))
    #     self.wait(4)






    # # Title
    #     title = Text("Checking Similarity",color = YELLOW).scale(1.2).to_edge(UP)
    #     self.play(Write(title))
    #     self.wait(2.3)
    #     # Create two squares
    #     square1 = Square(side_length=2, color=BLUE)
    #     square2 = Square(side_length=2.5, color=RED)

    #     # Position the squares
    #     square1.shift(LEFT * 2.5)
    #     square2.shift(RIGHT * 2.5)

    #     # Add labels
    #     label1 = Text("Square 1",font_size=23).next_to(square1, UP*1.5)
    #     label2 = Text("Square 2",font_size=23).next_to(square2, UP*1.7)

    #     # Create angle indicators (small squares)
    #     angle_indicators1 = self.create_angle_indicators(square1, BLUE)
    #     angle_indicators2 = self.create_angle_indicators(square2, RED)

    #     # Create side labels with lengths in cm
    #     side_labels1 = self.create_side_labels(square1, "2 cm")
    #     side_labels2 = self.create_side_labels(square2, "3 cm")

    #     # Animation
    #     self.play(Create(square1), Create(square2))
    #     self.play(Write(label1), Write(label2))
    #     self.wait(1)

    #     self.play(Create(VGroup(*angle_indicators1)), Create(VGroup(*angle_indicators2)))
    #     self.wait(1)

    #     self.play(Write(VGroup(*side_labels1)), Write(VGroup(*side_labels2)))
    #     self.wait(1)

    #     # Show angle equality
    #     angle_text = Text("All angles = 90°",font_size=26).to_edge(DOWN*2.5)
    #     self.play(Write(angle_text))
    #     self.wait(1)

    #     # Show similarity conclusion
    #     similarity_text = Text("Squares are similar!",font_size=30).next_to(angle_text, DOWN)
    #     self.play(Write(similarity_text))
    #     self.wait(2)

    # def create_angle_indicators(self, square, color):
    #     indicators = []
    #     for i in range(4):
    #         indicator = Square(side_length=0.2, color=color)
    #         indicator.move_to(square.get_vertices()[i])
    #         indicator.shift((square.get_center() - square.get_vertices()[i]) * 0.09)
    #         indicators.append(indicator)
    #     return indicators

    # def create_side_labels(self, square, label):
    #     labels = []
    #     for i in range(4):
    #         mid_point = (square.get_vertices()[i] + square.get_vertices()[(i+1) % 4]) / 2
    #         direction = mid_point - square.get_center()
    #         side_label = Text(label).scale(0.4).move_to(mid_point + direction * 0.4)
    #         labels.append(side_label)
    #     return labels



















    # def CopyAngleWithCompass(self):
    #        # Title for the scene
    #     title = Text("CONSTRUCTING A COPY OF AN ANGLE OF UNKNOWN MEASUREMENT",font_size= 27,color = YELLOW).to_edge(UP)
    #     self.play(Write(title))
    #     self.wait(3)
     
    #     # Step 1: Create the original angle
    #     point_A = Dot(ORIGIN, color=YELLOW)
    #     point_B = Dot(2*RIGHT, color=YELLOW)
    #     point_C = Dot(2*UP+RIGHT, color=YELLOW)
        
    #     line_AB = Line(point_A.get_center(), point_B.get_center())
    #     line_AC = Line(point_A.get_center(), point_C.get_center())
        
    #     original_angle = Angle(line_AB, line_AC, radius=0.5, color=BLUE)
        
    #     label_A = Text("A").next_to(point_A, DOWN+LEFT, buff=0.1).scale(0.7)
    #     label_B = Text("B").next_to(point_B, DOWN, buff=0.1).scale(0.7)
    #     label_C = Text("C").next_to(point_C, UP, buff=0.1).scale(0.7)

    #     step1_text = Text(" Unknown measurement angle diagram of ABC").scale(0.8).to_edge(DOWN)
        
    #     self.play(
    #         Create(VGroup(point_A, point_B, point_C, line_AB, line_AC, original_angle)),
    #         Write(VGroup(label_A, label_B, label_C)),
    #         Write(step1_text)
    #     )
    #     self.wait(2)

    #     # Step 2: Draw the base line for the new angle
    #     step2_text = Text("Step 1: Now draw base line DE with pencil for coping \n angle of unknown measurement.").scale(0.65).to_edge(DOWN)
    #     point_D = Dot(3*LEFT + 2*DOWN, color=YELLOW)
    #     point_E = Dot(0.1*RIGHT + 2*DOWN, color=YELLOW)
    #     base_line = Line(point_D.get_center(), point_E.get_center())
        
    #     label_D = Text("D").next_to(point_D, DOWN, buff=0.1).scale(0.7)
    #     label_E = Text("E").next_to(point_E, DOWN, buff=0.1).scale(0.7)
        
    #     self.play(
    #         ReplacementTransform(step1_text, step2_text),
    #         Create(VGroup(point_D, point_E, base_line)),
    #         Write(VGroup(label_D, label_E))
    #     )
    #     self.wait(5)

    #     # Step 3: Draw an arc with compass centered at the vertex of the original angle
    #     step3_text = Text("Step 2: Now setup the pencil with compass and place the compass\n at A and draw an arc to cut the rays AC and AB.").scale(0.65).to_edge(DOWN)
    #     arc1 = Arc(radius=2, angle=original_angle.get_value(), color=RED)
    #     arc1.shift(point_A.get_center())
        
    #     self.play(ReplacementTransform(step2_text, step3_text), Create(arc1))
    #     self.wait(5.5)

    #     # Step 4: Draw an arc with the same radius centered at the start of the new base line
    #     step4_text = Text("Step 3: Draw arc with  compass from D with radius AB").scale(0.7).to_edge(DOWN)
    #     arc2 = Arc(radius=2, angle=PI/2.9, color=RED)
    #     arc2.shift(point_D.get_center())
        
    #     self.play(ReplacementTransform(step3_text, step4_text), Create(arc2))
    #     self.wait(5)

    #     # Step 5: Draw a line from the start of the base line to the intersection of the arcs
    #     step5_text = Text("Step 4: Draw line DF  to arc intersection").scale(0.8).to_edge(DOWN)
    #     point_F = Dot(point_D.get_center() + 1.85*UP+RIGHT, color=YELLOW)
    #     new_line = Line(point_D.get_center(), point_F.get_center(), color=GREEN)
        
    #     label_F = Text("F").next_to(point_F, UP, buff=0.1).scale(0.7)
        
    #     self.play(
    #         ReplacementTransform(step4_text, step5_text),
    #         Create(VGroup(point_F, new_line)),
    #         Write(label_F)
    #     )
    #     self.wait(4.5)

    #     # Step 6: Highlight the copied angle
    #     step6_text = Text("Step 5: Copied angle FDE complete").scale(0.8).to_edge(DOWN)
    #     copied_angle = Angle(base_line, new_line, radius=0.5, color=GREEN)
        
    #     self.play(ReplacementTransform(step5_text, step6_text), Create(copied_angle))
    #     self.wait(4)

    #     # Add final labels
    #     original_label = Text("Original Angle of Unknown \nmeasurement ABC",color=BLUE).scale(0.6).next_to(original_angle, UP+LEFT)
    #     copied_label = Text("Copied Angle FDE",color=BLUE).scale(0.55).next_to(copied_angle, DOWN*-1+LEFT)
        
    #     self.play(Write(original_label), Write(copied_label))
    #     self.wait(3.7)

    #     # Optional: Clean up and show only the final result
    #     final_text = Text("Final Result: ∠ABC ≅ ∠FDE").scale(0.8).to_edge(DOWN)
    #     self.wait(3.2)
    #     self.play(
    #         FadeOut(arc1, arc2, step6_text),
    #         ReplacementTransform(VGroup(original_label, copied_label), final_text)
    #     )




    # def similaritycheck1(self):

    #     # Title
    #     title = Text("Checking Similarity").scale(1.2).to_edge(UP)
    #     self.play(Write(title))
    #     self.wait(2.3)

    #     # Create two squares
    #     square1 = Square(side_length=2, color=BLUE).shift(LEFT * 3)
    #     square2 = Square(side_length=3, color=RED).shift(RIGHT * 3)

    #     # Label vertices
    #     labels1 = self.label_vertices(square1, ['A', 'B', 'C', 'D'])
    #     labels2 = self.label_vertices(square2, ['P', 'Q', 'R', 'S'])

    #     # Show squares and labels
    #     self.play(Create(square1), Create(square2))
    #     self.play(*[Write(label) for label in labels1 + labels2])

    #     # Show measurements for square1
    #     self.show_measurements(square1, 2, BLUE)
        
    #     # Show measurements for square2
    #     self.show_measurements(square2, 3, RED)

    #     # Show similarity ratio
    #     self.show_similarity_ratio(square1, square2)

    #     # Conclusion
    #     conclusion = Text("The squares are similar!",color=YELLOW).scale(0.8).to_edge(DOWN*2)
    #     self.play(Write(conclusion))
    #     self.wait(3.3)

    # def label_vertices(self, square, labels):
    #     labeled_points = []
    #     for i, point in enumerate(square.get_vertices()):
    #         label = Text(labels[i], color=square.get_color()).scale(0.5).next_to(point, point - square.get_center())
    #         labeled_points.append(label)
    #     return labeled_points

    # def show_measurements(self, square, side_length, color):
    #     vertices = square.get_vertices()
    #     for i in range(4):
    #         # Side length
    #         start, end = vertices[i], vertices[(i+1) % 4]
    #         side = Line(start, end, color=color)
    #         length_label = Text(f"{side_length}", color=WHITE).scale(0.6).next_to(side, IN, buff=0.1)
    #         self.play(Create(side), Write(length_label))

    #         # # Angle
    #         angle = Angle(
    #             Line(vertices[i], vertices[i-1]),
    #             Line(vertices[i], vertices[(i+1) % 4]),
    #             radius=0.1,
    #             color=color
    #          )
    #         # Square Angle (90 degrees)
            
    #         angle_label = Text("90°", color=WHITE).scale(0.4).move_to(angle.point_from_proportion(0.5))
    #         self.play(Create(angle), Write(angle_label))

    # def show_similarity_ratio(self, square1, square2):
    #     ratio = square2.side_length / square1.side_length
    #     ratio_text = Text("").scale(0.8).to_edge(DOWN)
    #     self.play(Write(ratio_text))












    # def CopyAngleWithCompass(self):
    #        # Title for the scene
    #     title = Text("CONSTRUCTING A COPY OF AN ANGLE OF UNKNOWN MEASURE",font_size= 30,color = YELLOW).to_edge(UP)
    #     self.play(Write(title))
    #     self.wait(3)
     
    #     # Step 1: Create the original angle
    #     point_A = Dot(ORIGIN, color=YELLOW)
    #     point_B = Dot(2*RIGHT, color=YELLOW)
    #     point_C = Dot(2*UP+RIGHT, color=YELLOW)
        
    #     line_AB = Line(point_A.get_center(), point_B.get_center())
    #     line_AC = Line(point_A.get_center(), point_C.get_center())
        
    #     original_angle = Angle(line_AB, line_AC, radius=0.5, color=BLUE)
        
    #     label_A = Text("A").next_to(point_A, DOWN+LEFT, buff=0.1).scale(0.7)
    #     label_B = Text("B").next_to(point_B, DOWN, buff=0.1).scale(0.7)
    #     label_C = Text("C").next_to(point_C, UP, buff=0.1).scale(0.7)

    #     step1_text = Text(" Unknown measurement angle diagram of ABC").scale(0.8).to_edge(DOWN)
        
    #     self.play(
    #         Create(VGroup(point_A, point_B, point_C, line_AB, line_AC, original_angle)),
    #         Write(VGroup(label_A, label_B, label_C)),
    #         Write(step1_text)
    #     )
    #     self.wait(2)

    #     # Step 2: Draw the base line for the new angle
    #     step2_text = Text("Step 1: Now draw base line DE with pencil for coping \n angle of unknown measurement.").scale(0.65).to_edge(DOWN)
    #     point_D = Dot(3*LEFT + 2*DOWN, color=YELLOW)
    #     point_E = Dot(0.1*RIGHT + 2*DOWN, color=YELLOW)
    #     base_line = Line(point_D.get_center(), point_E.get_center())
        
    #     label_D = Text("D").next_to(point_D, DOWN, buff=0.1).scale(0.7)
    #     label_E = Text("E").next_to(point_E, DOWN, buff=0.1).scale(0.7)
        
    #     self.play(
    #         ReplacementTransform(step1_text, step2_text),
    #         Create(VGroup(point_D, point_E, base_line)),
    #         Write(VGroup(label_D, label_E))
    #     )
    #     self.wait(5)

    #     # Step 3: Draw an arc with compass centered at the vertex of the original angle
    #     step3_text = Text("Step 2: Now setup the pencil with compass and place the compass\n at A and draw an arc to cut the rays AC and AB.").scale(0.65).to_edge(DOWN)
    #     arc1 = Arc(radius=2, angle=original_angle.get_value(), color=RED)
    #     arc1.shift(point_A.get_center())
        
    #     self.play(ReplacementTransform(step2_text, step3_text), Create(arc1))
    #     self.wait(5.5)

    #     # Step 4: Draw an arc with the same radius centered at the start of the new base line
    #     step4_text = Text("Step 3: Draw arc with  compass from D with radius AB").scale(0.7).to_edge(DOWN)
    #     arc2 = Arc(radius=2, angle=PI/2.9, color=RED)
    #     arc2.shift(point_D.get_center())
        
    #     self.play(ReplacementTransform(step3_text, step4_text), Create(arc2))
    #     self.wait(4)

    #     # Step 5: Draw a line from the start of the base line to the intersection of the arcs
    #     step5_text = Text("Step 4: Draw line DF  to arc intersection").scale(0.8).to_edge(DOWN)
    #     point_F = Dot(point_D.get_center() + 1.85*UP+RIGHT, color=YELLOW)
    #     new_line = Line(point_D.get_center(), point_F.get_center(), color=GREEN)
        
    #     label_F = Text("F").next_to(point_F, UP, buff=0.1).scale(0.7)
        
    #     self.play(
    #         ReplacementTransform(step4_text, step5_text),
    #         Create(VGroup(point_F, new_line)),
    #         Write(label_F)
    #     )
    #     self.wait(4)

    #     # Step 6: Highlight the copied angle
    #     step6_text = Text("Step 5: Copied angle FDE complete").scale(0.8).to_edge(DOWN)
    #     copied_angle = Angle(base_line, new_line, radius=0.5, color=GREEN)
        
    #     self.play(ReplacementTransform(step5_text, step6_text), Create(copied_angle))
    #     self.wait(4)

    #     # Add final labels
    #     original_label = Text("Original Angle of Unknown \nmeasurement ABC",color=BLUE).scale(0.6).next_to(original_angle, UP+LEFT)
    #     copied_label = Text("Copied Angle FDE",color=BLUE).scale(0.55).next_to(copied_angle, DOWN*-1+LEFT)
        
    #     self.play(Write(original_label), Write(copied_label))
    #     self.wait(3.7)

    #     # Optional: Clean up and show only the final result
    #     final_text = Text("Final Result: ∠ABC ≅ ∠FDE").scale(0.8).to_edge(DOWN)
    #     self.wait(3.2)
    #     self.play(
    #         FadeOut(arc1, arc2, step6_text),
    #         ReplacementTransform(VGroup(original_label, copied_label), final_text)
    #     )
        
















#    ###construction of circle 
#     def ConstructCircleWithCompass(self):
#         # Title
#         title = Text("Construction of a Circle",color=PINK).to_edge(UP)
#         self.play(Write(title))
#         self.wait(3)
        
#         # Step 1: Draw the center point
#         step1_text = Text("Step 1: Mark the center point as O.",font_size= 40).next_to(title, DOWN).shift(DOWN * 5)
#         center_point = Dot(point=ORIGIN, color=BLUE)
        
#         self.play(Write(step1_text))
#         self.play(Create(center_point))
#         a = Text("O",color = ORANGE,font_size=24).next_to(center_point,DOWN)
#         self.play(Write(a))
#         self.wait(3)

#         # Step 2: Set the compass radius
#         step2_text = Text("Step 2: Set the compass required radius with the help \nof scale.",font_size=40).next_to(title, DOWN).shift(DOWN * 5)
#         # radius_line = Line(ORIGIN, 2*RIGHT, color=YELLOW)
        
        
#         self.play(Transform(step1_text, step2_text))
#         # self.play(Create(radius_line))
#         # b = Text("radius",font_size=24).next_to(radius_line,UP)
#         # self.play(Write(b))
#         self.wait(3.6)

#         # Step 3: Draw the circle with the compass
#         step3_text = Text("Step 3: Place your compass at O and draw the circle. ",font_size=40).next_to(title, DOWN).shift(DOWN * 5)
#         circle = Circle(radius=2, color=GREEN)
        
#         self.play(Transform(step1_text, step3_text))
#         self.wait(2)
        
#         self.play(Create(circle))
#         self.wait(3)

#         radius_line = Line(ORIGIN, 2*RIGHT, color=YELLOW)
        
        
#         # self.play(Transform(step1_text, step2_text))
#         self.play(Create(radius_line))
#         b = Text("radius",font_size=24).next_to(radius_line,UP)
#         self.play(Write(b))
#         self.wait(3)

#         # Final Diagram
#         final_text = Text("Final Circle Diagram",font_size=40).next_to(title, DOWN).shift(DOWN * 5)
#         final_diagram = VGroup(center_point, radius_line, circle)
        
#         self.play(Transform(step1_text, final_text))
#         self.play(final_diagram.animate.move_to(ORIGIN))
#         self.wait(4)
   
    # def Perpendiculars(self):
    #     # Create the protractor arc
    #     protractor = Arc(radius=2, angle=PI, color=BLUE)
        
    #     # Create the center point
    #     center_point = Dot(ORIGIN, color=WHITE)

    #     # Create degree markings and labels
    #     degree_markings = VGroup()
    #     for degree in range(0, 181, 10):  # Labels every 10 degrees
    #         angle = degree * DEGREES
            
    #         # Create longer marks for multiples of 30 degrees
    #         mark_length = 0.2 if degree % 30 == 0 else 0.1
    #         mark = Line(
    #             start=(2 - mark_length) * UP,
    #             end=2 * UP,
    #         ).rotate(angle, about_point=ORIGIN).set_color(GRAY)
    #         degree_markings.add(mark)
            
    #         # Add labels
    #         label = Text(str(degree), font_size=13)
    #         label_radius = 2.2  # Slightly larger than the arc radius
    #         label_pos = label_radius * UP
    #         label.move_to(label_pos).rotate(angle, about_point=ORIGIN+)
    #         label.rotate(angle - PI/2, about_point=label.get_center())  # Rotate label to align with arc
    #         degree_markings.add(label)

    #     # Create a label for the protractor
    #     protractor_label = Text("180° Protractor", color=YELLOW).to_edge(UP)

    #     # Animation sequence
    #     self.play(Create(protractor), Create(center_point))
    #     self.play(Create(degree_markings), Write(protractor_label))
    #     self.wait(2)

    #     # Fade out everything
    #     self.play(
    #         FadeOut(protractor), FadeOut(center_point), FadeOut(degree_markings),
    #         FadeOut(protractor_label)
    #     )








        

    # def Perpendiculars(self):
    #     # Create title
    #     title = Text("Draw Angle Using Protractor", color=YELLOW).to_edge(UP)
    #     self.play(Write(title))

    #     # Step 1: Place the protractor
    #     step1 = Text("Step 1: Place the protractor having 180° ", color=WHITE, font_size=33).to_edge(DOWN)
    #     protractor = Arc(radius=2, angle=PI, color=BLUE)
    #     protractor_center = Dot(color=WHITE)

    #   # Add degree markings and labels
    #     degree_markings = VGroup()
    #     for degree in range(0, 181, 1):  # Changed to 181 to include 180 degrees
    #          angle = degree * DEGREES
    #          mark_length = 0.1 if degree % 10 == 0 else 0.05  # Longer marks for multiples of 10
    #          mark = Line(
    #          start=(2 - mark_length) * UP,
    #          end=2 * UP,
    #        ).rotate(angle, about_point=ORIGIN).set_color(GRAY)
    #     degree_markings.add(mark)
    
    #     if degree % 10 == 0:  # Labels for multiples of 10
    #      label = Text(str(degree), font_size=12).next_to(mark, UP, buff=0.1)
    #      label.rotate(angle - PI/2, about_point=ORIGIN)  # Rotate to align with the arc
    #     degree_markings.add(label) 

    #     self.play(Write(step1))
    #     self.play(Create(protractor), Create(protractor_center))
    #     self.wait(1)
    #     self.play(FadeOut(step1))

    #     # Step 2: Draw the base line
    #     step2 = Text("Step 2: Draw the base line", color=WHITE, font_size=33).to_edge(DOWN)
    #     base_line = Line(ORIGIN, 3 * RIGHT, color=WHITE)
        
    #     self.play(Write(step2))
    #     self.play(Create(base_line))
    #     self.wait(1)
    #     self.play(FadeOut(step2))

    #     # Step 3: Locate the 40° mark
    #     step3 = Text("Step 3: Locate the 40° mark", color=WHITE, font_size=33).to_edge(DOWN)
    #     a = Text("40°",font_size=20).shift(1.6 * UP+RIGHT*1.57)
    #     angle_40_mark = Dot(1.3 * UP+RIGHT*1.57).rotate(1 * DEGREES).set_color(RED)
        
    #     self.play(Write(step3))
    #     self.play(Write(a))
    #     self.play(Create(angle_40_mark))
    #     self.wait(1)
    #     self.play(FadeOut(step3))

    #     # Step 4: Draw the angle line
    #     step4 = Text("Step 4: Draw the angle line", color=WHITE, font_size=33).to_edge(DOWN)
    #     angle_line = Line(ORIGIN, 2.3 * (np.cos(40 * DEGREES) * RIGHT + np.sin(40 * DEGREES) * UP), color=RED)
        
    #     self.play(Write(step4))
    #     self.play(Create(angle_line))
    #     self.wait(1)
    #     self.play(FadeOut(step4))

    #     # Step 5: Label the angle
    #     step5 = Text("Step 5: Label the angle", color=WHITE, font_size=33).to_edge(DOWN)
    #     angle_arc = Arc(radius=0.5, angle=40*DEGREES, color=GREEN)
    #     angle_label = MathTex("40^\\circ", color=GREEN).next_to(angle_arc, RIGHT).shift(0.3 * UP)
        
    #     self.play(Write(step5))
    #     self.play(Create(angle_arc), Write(angle_label))
    #     self.wait(1)
    #     self.play(FadeOut(step5))

    #     # Final message
    #     final_message = Text("A   40° angle is drawn", color=WHITE, font_size=33).to_edge(DOWN)
    #     self.play(Write(final_message))
    #     self.wait(4)

    #     # Fade out everything
    #     self.play(
    #         FadeOut(protractor), FadeOut(protractor_center), FadeOut(degree_markings),
    #         FadeOut(base_line), FadeOut(angle_line), FadeOut(angle_arc),
    #         FadeOut(angle_label), FadeOut(title), FadeOut(final_message),
    #         FadeOut(angle_40_mark),FadeOut(a)
    #     )















   
    # def Perpendiculars(self):
  
    #     # Create title
    #     title = Text("Drawing a 40° Angle", color=YELLOW).to_edge(UP)
    #     self.play(Write(title))

    #     # Step 1: Place the protractor
    #     step1 = Text("Step 1: Place the protractor", color=WHITE, font_size=33).to_edge(DOWN)
    #     protractor = Arc(radius=2, angle=PI, color=BLUE)
    #     protractor_center = Dot(color=WHITE)
        
       

    #     self.play(Write(step1))
    #     self.play(Create(protractor), Create(protractor_center))
    #     self.wait(1)
    #     self.play(FadeOut(step1))

    #     # Step 2: Draw the base line
    #     step2 = Text("Step 2: Draw the base line", color=WHITE, font_size=33).to_edge(DOWN)
    #     base_line = Line(ORIGIN, 3 * RIGHT, color=WHITE)
        
    #     self.play(Write(step2))
    #     self.play(Create(base_line))
    #     self.wait(1)
    #     self.play(FadeOut(step2))

    #     # Step 3: Locate the 40° mark
    #     step3 = Text("Step 3: Locate the 40° mark", color=WHITE, font_size=33).to_edge(DOWN)
    #     angle_40_mark = Dot(2 * UP).rotate(40 * DEGREES, about_point=ORIGIN).set_color(RED)
        
    #     self.play(Write(step3))
    #     self.play(Create(angle_40_mark))
    #     self.wait(1)
    #     self.play(FadeOut(step3))

    #     # Step 4: Draw the angle line
    #     step4 = Text("Step 4: Draw the angle line", color=WHITE, font_size=33).to_edge(DOWN)
    #     angle_line = Line(ORIGIN, 2.3 * (np.cos(40 * DEGREES) * RIGHT + np.sin(40 * DEGREES) * UP), color=RED)
        
    #     self.play(Write(step4))
    #     self.play(Create(angle_line))
    #     self.wait(1)
    #     self.play(FadeOut(step4))

    #     # Step 5: Label the angle
    #     step5 = Text("Step 5: Label the angle", color=WHITE, font_size=33).to_edge(DOWN)
    #     angle_arc = Arc(radius=0.5, angle=40*DEGREES, color=GREEN)
    #     angle_label = MathTex("40^\\circ", color=GREEN).next_to(angle_arc, RIGHT).shift(0.3 * UP)
        
    #     self.play(Write(step5))
    #     self.play(Create(angle_arc), Write(angle_label))
    #     self.wait(1)
    #     self.play(FadeOut(step5))

    #     # Final message
    #     final_message = Text("A 40° angle is drawn", color=WHITE, font_size=33).to_edge(DOWN)
    #     self.play(Write(final_message))
    #     self.wait(2)

    #     # Fade out everything
    #     self.play(
    #         FadeOut(protractor), FadeOut(protractor_center), FadeOut(degree_markings),
    #         FadeOut(base_line), FadeOut(angle_line), FadeOut(angle_arc),
    #         FadeOut(angle_label), FadeOut(title), FadeOut(final_message),
    #         FadeOut(angle_40_mark)
    #     )






if __name__ == "__main__":
    scene = testing2()
    scene.render()
