from manim import *

class CubeScene(ThreeDScene):
    def const(self):
        # Setting up the camera for a 3D scene
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)
        
        # Creating a cube
        cube = Cube()
        
        # Adding the cube to the scene
        self.add(cube)
        
        # Animating the rotation of the cube
        self.play(Rotate(cube, angle=PI/4, axis=UP))
        self.play(Rotate(cube, angle=PI/4, axis=RIGHT))
        
        # Keeping the final frame for a while
        self.wait(2)

if __name__ == "__main__":
    # Rendering the scene
    config.pixel_height = 600
    config.pixel_width = 800
    config.frame_rate = 30
    config.background_color = WHITE
    scene = CubeScene()
    scene.render()