from manim import *
import pandas as pd
import os
import fnmatch
from AbstractAnim import AbstractAnim
import cvo
import requests
from PIL import Image
from io import BytesIO
import matplotlib.pyplot as plt
import urllib.request
import os.path



# Read Excel data into a pandas DataFrame
xlsx_path = "/Users/hridaybhushan/Downloads/SlideShowTest.xlsx"
df = pd.read_excel(xlsx_path, sheet_name='Sheet1')  # Adjust sheet_name as per your Excel file

class SlideShowAnimation(AbstractAnim):
    def construct(self):
        self.setNameWithImage()
        
        #self.ImageURLReader()

    def setNameWithImage(self):
        
        # Folder containing final images
        images_folder = "/Users/hridaybhushan/Downloads/Final images"
        
        # List of possible file extensions to check
        image_extensions = ['.png', '.jpg', '.jpeg']  # Add more extensions as needed
        
        # Loop through each row in the Excel data
        for index, row in df.iterrows():
            self.setBackgroundImage()

            #c1o1 diagram
            O1name = row['O1 Name']
            C1name = row['C1 Name']
            imageURL = row['Image URL']
            scrollingText = row['Scrollable Text']
            fileExtension = row['File Extension']
            o1_name = f"{O1name}"  # Assuming "Garu" suffix as per previous instructions
            c1_name = f"{C1name}"
            p1=cvo.CVO().CreateCVO(c1_name,"")
           
                
            p1.setcircleradius(3)
   
            p1.setPosition([0,0,0])
            self.ImageURLReader(imageURL, o1_name, fileExtension)
            self.construct1(p1,p1)
            self.ImageScale()
            self.ScrollingText(scrollingText)
            self.fadeOutCurrentScene()
            
            

    def setBackgroundImage(self):

        # Background image
            background_image_path = '/Users/hridaybhushan/Downloads/Divaz Vault.jpg'
            background = ImageMobject(background_image_path)
            background.scale_to_fit_width(config.frame_width)
            background.scale_to_fit_height(config.frame_height)
            
            # Create copies for each corner
            background.scale(0.2)
            self.play(FadeIn(background))
            top_left = background.copy()
            top_right = background.copy()
            bottom_left = background.copy()
            bottom_right = background.copy()
            
            # Add the images to the scene
            self.play(background.animate.scale(5))
            self.play(background.animate.scale(0),top_left.animate.to_corner(UL), top_right.animate.to_corner(UR)
                      ,bottom_left.animate.to_corner(DL), bottom_right.animate.to_corner(DR))
            
            
            
            

    def ImageURLReader(self, imageURL, o1_name, fileExtension):
        
        # URL of the image
        image_url = imageURL
        imagePath='/Users/hridaybhushan/Downloads/Skillbanc TempImage/'+o1_name+fileExtension
        if os.path.isfile(imagePath):
            pass
        else:
            urllib.request.urlretrieve(image_url, imagePath)
        # Create a Manim ImageMobject
        self.image_mobject = ImageMobject(imagePath)
        self.image_mobject.scale_to_fit_width(6)
        self.image_mobject.scale_to_fit_height(4)
        
         # Display the image in the center of the screen
        self.play(FadeIn(self.image_mobject))
        self.play(self.image_mobject.animate.scale(0.25))
        
    

    def ImageScale(self):
        
        self.play(self.image_mobject.animate.scale(4))
        self.wait(2)  # Display for 2 seconds
        # Create a text object

    def ScrollingText(self, scrollingText):  
        scrolling_text = Text(scrollingText)
        
        # Set the initial position off the screen to the right
        scrolling_text.move_to(RIGHT*5 + DOWN*2.5)
        self.play(FadeIn(scrolling_text))
        # Animate the text moving from right to left across the screen
        self.play(
            scrolling_text.animate.shift(LEFT * (config.frame_width + scrolling_text.width)),
            run_time=10,  # Adjust run_time to control the scrolling speed
            rate_func=linear  # Use linear rate function for constant speed
        )

       
                    


# To render the scene
if __name__ == "__main__":
    
    scene = SlideShowAnimation()
    scene.render()