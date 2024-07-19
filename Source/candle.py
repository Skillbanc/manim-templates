from manim import *

class Candle3(ThreeDScene):
    def construct(self):
        # Set up the camera
        self.set_camera_orientation(phi=75 * DEGREES, theta=-45 * DEGREES)
        
        # Create the candle body (a cylinder)
        candle_body = Cylinder(radius=0.5, height=2, direction=UP)
        candle_body.set_color(WHITE)

        # Create the candle flame (a cone)
        flame = Cone(base_radius=0.3, height=0.5, direction=UP)
        flame.set_color(YELLOW)
        flame.move_to(candle_body.get_top() + UP * 0.25)

        # Create the candle wick (a cylinder)
        wick = Cylinder(radius=0.05, height=0.3, direction=UP)
        wick.set_color(BLACK)
        wick.move_to(candle_body.get_top() + UP * 0.15)

        # Add the candle body, wick, and flame to the scene
        self.add(candle_body, wick, flame)

        # Add some lighting to make the scene more realistic
        #self.add_light_source(PointLight(color=WHITE, intensity=0.5, point=3*OUT))

        # Rotate the camera to showcase the 3D effect
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(6)

# To render this scene, use the command in the terminal:
# manim -pqh script_name.py Candle
if __name__ == "__main__":
    scene = Candle3()
    scene.render()