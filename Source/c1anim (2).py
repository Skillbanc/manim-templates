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

class C1Anim(AbstractAnim):
    
    def construct(self):
        #  p1=cvo.CVO().CreateCVO("o1name","o2name","c1name","c2name")
         p10=cvo.CVO().CreateCVO("Person","John Doe").setPosition([0,2.5,0])
       
         self.construct1(p10,p10)

# from manim import *
# import numpy as np
# import math

# class C1Anim( Scene ):
#     def construct( self ):

#         axes = Axes( x_range = [0, 1, 1], y_range = [0, 1, 1], x_length = 4, y_length = 4,
#                      axis_config = {"include_tip": True, "numbers_to_exclude": [0]} ).add_coordinates()

#         pc = lambda t: axes.coords_to_point( np.cos( t * 0.5 * PI ), np.sin( t * 0.5 * PI ) )
#         xone = pc(0)
#         t_parameter = ValueTracker(0)
#         e1 = Arrow( start = xone, end = xone + RIGHT, color = GREEN, buff = 0 ).add_updater(
#             lambda mob: mob.move_to( pc( t_parameter.get_value() ) ) #.rotate( t_parameter.get_value() * PI / 2 )
#         ).update()
#         e2 = Arrow( start = xone, end = xone + UP, color = GREEN, buff = 0 ).add_updater(
#             lambda mob: mob.move_to( pc( t_parameter.get_value() ) )
#         ).update()
#         g1 = ParametricFunction( pc,
#                                  t_range=[0, 1],
#                                  scaling=axes.x_axis.scaling, color=YELLOW )
#         grp1 = VGroup( axes, g1, e1, e2 )
#         self.add(grp1)
#         self.play( UpdateFromAlphaFunc( t_parameter, 
#                                         lambda mob, alpha: mob.set_value( alpha ) ),                      
#                                         run_time=6 )
#         self.wait( )
      
if __name__ == "__main__":
    scene = C1Anim()
    scene.render()
    