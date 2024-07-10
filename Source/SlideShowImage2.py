from manim import *
import pandas as pd
import os
import fnmatch
from AbstractAnim import AbstractAnim
import cvo
# import requests
from PIL import Image
from io import BytesIO
# import matplotlib.pyplot as plt
import urllib.request
import os.path



# Read Excel data into a pandas DataFrame
xlsx_path = "C:\htmllll\internship\slideshow ip\SlideShowVideo.xlsx"
df = pd.read_excel(xlsx_path, sheet_name='Sheet1')  # Adjust sheet_name as per your Excel file

class SlideShowAnimation(AbstractAnim):
    def construct(self):
        self.setBackgroundImage()
        self.setNameWithImage()
        
    def setNameWithImage(self):
        # Loop through each row in the Excel data
        for index, row in df.iterrows():
            

            #c1o1 diagram
            O1name = row['O1 Name']
            C1name = row['C1 Name']
            imageURL = row['Image URL']
            scrollingText = row['Scrollable Text']
            fileExtension = row['File Extension']
            o1_name = (f"{O1name}")
            self.o1Text = Text(o1_name, font_size=32, color=GOLD)
            self.o1Text.to_edge(UP)
            c1_name= Text(f"{C1name}", color=GOLD)
            # c1Text = Text(c1_name, font_size=28, color=GOLD)
            # c1Text.next_to(o1Text, UP)
            # p1=cvo.CVO().CreateCVO(c1_name,"")  
            # p1.setcircleradius(3)
            # p1.setPosition([0,0,0])
            a=Circle(3,color=GOLD).move_to(ORIGIN)
            center=a.get_center()
            # b=Star(outer_radius=0.1,inner_radius=0.05,color=GOLD).move_to(center)
            c1nameposition = a.get_top()
            
            c1_name.move_to(c1nameposition).shift(UP*0.25)
            
            self.ImageURLReader(imageURL, o1_name, fileExtension)
                # Store the result of construct1
            self.play(Create(a),Write(c1_name),self.image_mobject.animate.scale(5))
            # self.play()
            self.play(c1_name.animate.scale(2), run_time=1)
            # self.play(c1_name.animate.scale(0.5), run_time=1)
            # self.play(c1_name.animate.scale(0.75).move_to(c1nameposition).shift(UP*0.25))
            self.play(FadeOut(c1_name),FadeOut(a),self.image_mobject.animate.scale(1.3))
            # Display the text
            self.play(Write(self.o1Text))
            # Fade out the construct1 mobject once the image appears
        #     self.play(
        #         self.image_mobject.animate.shift(LEFT * (config.frame_width + self.image_mobject.width)),
        #     run_time=10,  # Adjust run_time to control the scrolling speed
        #     rate_func=linear  # Use linear rate function for constant speed
        # )
            
            self.ScrollingText(scrollingText)
            self.ImageScale()
            # self.play(FadeOut(a))
        
    def setBackgroundImage(self):

       # Background image
            background_image_path = 'C:\htmllll\internship\slideshow ip\Divaz Vault'
            background = ImageMobject(background_image_path)
            background.scale_to_fit_width(config.frame_width)
            background.scale_to_fit_height(config.frame_height)
            
    #         # Create copies for each corner
            background.scale(0.2)
            self.play(FadeIn(background))
            top_left = background.copy()
            top_right = background.copy()
            bottom_left = background.copy()
            bottom_right = background.copy()
        
#         # Add the images to the scene
            self.play(background.animate.scale(5))
            self.play(background.animate.scale(0),top_left.animate.to_corner(UL), top_right.animate.to_corner(UR)
                    ,bottom_left.animate.to_corner(DL), bottom_right.animate.to_corner(DR))
            
    def ImageURLReader(self, imageURL, o1_name, fileExtension):
        
        # URL of the image
        image_url = imageURL
        imagePath='C:\\htmllll\\internship\\slideshow ip\\'+o1_name+fileExtension
        if not os.path.isfile(imagePath):
            urllib.request.urlretrieve(image_url, imagePath)
        # Create a Manim ImageMobject
        
        self.image_mobject = ImageMobject(imagePath)
        self.image_mobject.move_to(ORIGIN)
        self.image_mobject.scale_to_fit_width(6)
        self.image_mobject.scale_to_fit_height(4)
        self.image_mobject.scale(0.2)
         # Display the image in the center of the screen
        # self.play(FadeIn(self.image_mobject))
        # self.play(self.image_mobject.animate.scale(0.25))
        
    def ImageScale(self):
        
        self.play(self.image_mobject.animate.scale(0),self.o1Text.animate.scale(0))
        # self.wait(2)  # Display for 2 seconds
        # self.play(
        #           # Use linear rate function for constant speed
        # )

    def ScrollingText(self, scrollingText):  
        scrolling_text = Text(scrollingText,color=GOLD)
        
    #     # Set the initial position off the screen to the right
        scrolling_text.move_to(RIGHT*7 + DOWN*3.5)
        self.play(FadeIn(scrolling_text))
    #     # Animate the text moving from right to left across the screen
        self.play(
             scrolling_text.animate.shift(LEFT * (config.frame_width + scrolling_text.width)),
            # run_time=10,  # Adjust run_time to control the scrolling speed
            # rate_func=linear,
            # self.o1Text.animate.shift(LEFT * (config.frame_width + self.o1Text.width)),
            # run_time=10,  # Adjust run_time to control the scrolling speed
            # rate_func=linear,
            # self.image_mobject.animate.shift(LEFT * (config.frame_width + self.image_mobject.width)),
            run_time=10,  # Adjust run_time to control the scrolling speed
            rate_func=linear  # Use linear rate function for constant speed
        )

       

            


# To render the scene
if __name__ == "__main__":
    
    scene = SlideShowAnimation()
    scene.render()